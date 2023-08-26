#
#  Copyright (c) 2023 Bastian Koppelmann <kbastian@mail.upb.de>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see <http://www.gnu.org/licenses/>.
#
import os, sys, re
import argparse
import importlib
from isa import DReg, AReg, Const, EReg

qemu = "qemu-system-tricore"
tsim = "tsim16p_e"
errors = set()

def load_reg(f, reg, val):
    if reg == "d15":
        sys.stderr.write("load_reg: Cannot use d15")
    f.write(f"  movh %d15, hi:{val}\n")
    f.write(f"  mov.u %{reg}, lo:{val}\n")
    f.write(f"  or %{reg}, %d15\n")

def set_rm(f, val):
    rm = 0x00000b80 | ((val & 3)<< 24)
    f.write(".text\n")
    load_reg(f, "d10", rm)
    f.write("  mtcr $psw, %d10\n")

def write_tests(path, insn, i, rm):
    with open(path, 'w') as f:
        set_rm(f, rm)
        for t in range(i, i+100):
            f.write("_test_{:x}:\n".format(t))
            f.write(insn.gen_test())
        f.write("  debug\n")

def compile(testpath):
    with open(f"{testpath}/run_compile.sh", 'w') as f:
        cmd = f"tricore-as -mtc162 -o {testpath}/test.o {testpath}/test.S 2>{testpath}/compile.log"
        f.write("#!/bin/bash\n")
        f.write("cd ../../\n")
        f.write(cmd + "\n")

        os.system(cmd)

        cmd = f"tricore-ld -Tlink.ld --mcpu=tc162 -o {testpath}/test.elf {testpath}/test.o 2>>{testpath}/compile.log"
        f.write(cmd + "\n")
        os.system(cmd)
        os.system(f'chmod u+x {testpath}/run_compile.sh')

def run_qemu(testpath):
    sys.stdout.write(" QEMU...")
    sys.stdout.flush()
    cmd = f"{qemu} -M tricore_testboard -cpu tc37x -nographic -d cpu,exec,nochain -D {testpath}/qemu.log -singlestep -kernel {testpath}/test.elf 2>/dev/null 1>/dev/null"
    with open(f"{testpath}/run_qemu.sh", 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("cd ../../\n")
        f.write(cmd + "\n")
        os.system(f'chmod u+x {testpath}/run_qemu.sh')
    os.system(cmd)

def run_tsim(testpath):
    sys.stdout.write(" TSIM...")
    sys.stdout.flush()
    cmd = f"{tsim} -tc162p -S 0x80000000 -z -trace-instr-file {testpath}/tsim.result -e -o {testpath}/test.elf"
    with open(f"{testpath}/run_tsim.sh", 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("cd ../../\n")
        f.write(cmd + "\n")
        os.system(f'chmod u+x {testpath}/run_tsim.sh')
    os.system(cmd)

def evaluate(testpath, insn, test_num):
    sys.stdout.write(" Evaluate...")
    sys.stdout.flush()
    cmd = f"./EvaluateResults.py {testpath}/tsim.result {testpath}/qemu.log > {testpath}/result.txt"
    with open(f"{testpath}/run_eval.sh", 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("cd ../../\n")
        f.write(cmd + "\n")
        os.system(f'chmod u+x {testpath}/run_eval.sh')

    res = os.system(cmd)
    if (res != 0):
        sys.stdout.write( " [\u001b[31mFAIL\u001b[0m]\n")
        fail_insn = get_first_failing_insn(testpath)
        generate_qemu_test(testpath, insn, fail_insn)
        sys.exit(1)
    else:
        sys.stdout.write( " [\u001b[32mOK\u001b[0m]\n")
        #insn_id = insn.testid_to_offset(0, 4)
        #generate_qemu_test(testpath, insn, insn_id, test_num+1)
        os.system(f"rm -r {testpath}")

def get_op_prefix(reg):
    if isinstance(reg, DReg):
        if reg.val == 15:
            return "D15"
        return "D"
    elif isinstance(reg, AReg):
        return "A"
    elif isinstance(reg, EReg):
        return "E"
    elif isinstance(reg, Const):
        return "I"
    return "NO_PREFIX"

def get_immediates_from_insn(insn_str):
    res = []
    toks = [x.strip() for x in insn_str.split(',')]
    toks = [toks[0].split()[1]] + toks[1:]
    for tok in toks:
        if tok.startswith("D"):
            continue
        if tok.startswith("E"):
            continue
        if tok.startswith("A"):
            continue
        res.append(tok)
    return res

def get_first_failing_insn(path):
    insn_num = None
    with open(os.path.join(path, "result.txt"), 'r') as f:
        errors = f.readlines()
        pat = "Error at Instruction (\d+)"
        m = re.search(pat, errors[0])
        if m is not None:
            insn_num = int(m.group(1))
            print("Test ID {}".format(insn.offset_to_testid(insn_num, 4)))
    return insn_num


def generate_qemu_test(path, insn, insn_num, test_num=None):
    with open(os.path.join(path, "tsim.result"), 'r') as f:
        tsim_data = f.readlines()
        insn_line = tsim_data[insn_num-1]
        pat = r"\d+\(\d+,\d+\)\s+[0-9a-f]+\s+(.*)DATA_[A-Z0-9]+\s+[0-9:a-z]+\s+[a-zA-Z:a-z]+\s+(.*)"
        m = re.search(pat, insn_line)
        if m is not None:
            insn_str = m.group(1)
            imms = get_immediates_from_insn(insn_str)
            regs = m.group(2)
            pat = r"d(\d+)\[([0-9a-f]+)\]"
            d_regs = re.findall(pat, regs)
            d_map = dict()
            for r, val in d_regs:
                d_map[int(r)] = int(val, 16)

            pat = r"a(\d+)\[([0-9a-f]+)\]"
            a_regs = re.findall(pat, regs)
            a_map = dict()
            for r, val in a_regs:
                a_map[int(r)] = int(val, 16)

            res = "TEST_"
            res += get_op_prefix(insn.dst)
            res += "_"

            for op in insn.args:
                res += get_op_prefix(op)

            if test_num is None:
                res += f"({insn.name}, #NUM, "
            else:
                res += f"({insn.name}, {test_num}, "

            if isinstance(insn.dst, DReg):
                 res += hex(d_map[insn.dst.val])
            elif isinstance(insn.dst, AReg):
                 res += hex(a_map[insn.dst.val])
            elif isinstance(insn.dst, EReg):
                 res += hex(d_map[insn.dst.val]) + " ,"
                 res += hex(d_map[insn.dst.val + 1])
            res += ', '

            const_idx = 0
            for op in insn.args:
                if isinstance(op, DReg):
                     res += hex(d_map[op.val])
                elif isinstance(op, AReg):
                     res += hex(a_map[op.val])
                elif isinstance(op, EReg):
                     res += hex(d_map[op.val]) + " ,"
                     res += hex(d_map[op.val + 1])
                elif isinstance(op, Const):
                      res += imms[const_idx]
                      const_idx += 1
                else:
                      raise RuntimeError("FOO")
                res += " ,"

            res = res[:-1]
            res += ")\n"
            with open(os.path.join(path, "qemu.pattern"), 'w') as fw:
                fw.write(res)

def run(insn, i, rm, test_num):
    num_str = "{:03d}".format(test_num)
    testpath = f'test/{num_str}_{insn.name}_rm_{rm}_{i}'
    os.system(f"mkdir -p {testpath}")
    write_tests(f"{testpath}/test.S", insn, i, rm)
    compile(testpath)
    run_tsim(testpath)
    run_qemu(testpath)
    evaluate(testpath, insn, test_num)



def main():
    global qemu, tsim
    parser = argparse.ArgumentParser()
    parser.add_argument('--qemu', type=str, nargs=1, required=False)
    parser.add_argument('--tsim', type=str, nargs=1, required=False)
    parser.add_argument('--num', type=int, nargs=1, required=True)
    parser.add_argument('--rm', type=int, nargs=1, required=True)
    parser.add_argument('--insnlist', type=str, nargs=1, required=True)
    args = parser.parse_args()

    qemu = args.qemu[0]
    tsim = args.tsim[0]

    import_path = args.insnlist[0].replace("/", ".")[:-3]
    mod = importlib.import_module(import_path, package="insnlist")

    for rm in range(args.rm[0]):
        sys.stdout.write(f"=============== RM {rm} ===============\n")
        for test_num, insn in enumerate(mod.insnlist):
            sys.stdout.write(f"--------------- {insn.name} ---------------\n")
            i = 0
            inc = 100
            for i in range(0, args.num[0], inc):
                if i + inc > args.num[0]:
                    inc = args.num[0] - i
                sys.stdout.write("Block {:10} - {:10}".format(i, i+inc))
                sys.stdout.flush()
                run(insn, i, rm, test_num)
                i += inc

    print("All successfull")
main()
