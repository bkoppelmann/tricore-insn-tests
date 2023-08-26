from random import randint, getrandbits
import math

class Const:
    def __init__(self, width):
        self.width = width
    def __str__(self):
        return str(getrandbits(self.width-1))


class Reg:
    PREFIX = ""
    def __init__(self, val):
        self.val = val
        self.num_to_load = 0
    def __str__(self):
            return self.PREFIX + str(self.val)

    def get_random(self):
        return randint(0, 2**32)


class RandomReg(Reg):
    def __init__(self):
        super().__init__(randint(0, 15))


class DReg(Reg):
    PREFIX = "%d"
    NUM_TO_LOAD = 3

    def load_random(self):
        res = ""
        val = self.get_random()
        res += f"# DReg({self.val})\n"
        res += f"movh %d10, up:{hex(val)}\n"
        res += f"mov.u {self.PREFIX}{self.val}, lo:{hex(val)}\n"
        res += f"or {self.PREFIX}{self.val}, %d10\n"
        self.num_to_load = 3

        return res

class AReg(Reg):
    PREFIX = "%a"
    NUM_TO_LOAD = 4
    def load_random(self):
        res = ""
        val = self.get_random()
        res += f"# AReg({self.val})\n"
        res += f"movh %d10, hi:{hex(val)}\n"
        res += f"mov.u %d11, lo:{hex(val)}\n"
        res += f"or %d10, %d11\n"
        res += f"mov.a {self}, %d10\n"

        return res


class EReg(Reg):
    PREFIX = "%e"
    NUM_TO_LOAD = 8

    def load_random(self):
        res = ""
        res += f"# EReg({self.val})\n"
        val_lo = self.get_random()
        res += f"movh %d10, up:{hex(val_lo)}\n"
        res += f"mov.u %d11, lo:{hex(val_lo)}\n"
        res += f"or %d10, %d11\n"
        res += f"mov %d{self.val}, %d10\n"

        val_up = self.get_random()
        res += f"movh %d10, up:{hex(val_up)}\n"
        res += f"mov.u %d11, lo:{hex(val_up)}\n"
        res += f"or %d10, %d11\n"
        res += f"mov %d{self.val + 1}, %d10\n"

        return res

    def __str__(self):
        return f"{self.PREFIX}{self.val}"


class PReg(Reg):
    PREFIX = "%a"

class RandomDReg(RandomReg):
    PREFIX = "%d"

class RandomAReg(RandomReg):
    PREFIX = "%a"

class RandomEReg(RandomReg):
    PREFIX = "%e"
    def __init__(self):
        self.val = randint(0, 6) << 1

class RandomPReg(RandomReg):
    PREFIX = "a"
    def __init__(self):
        self.val = randint(0, 7) << 1


class Insn():
    def __init__(self, name, dst, args):
        self.name = name
        self.args = args
        self.dst = dst
        self.num_asm = 2 # rstv + insn 
        for arg in self.args:
            if isinstance(arg, Reg):
                self.num_asm += arg.NUM_TO_LOAD


    def offset_to_testid(self, off, size_preamble):
        return int(math.floor((off - size_preamble) / self.num_asm))

    def testid_to_offset(self, id, size_preamble):
        return id * self.num_asm + size_preamble + self.num_asm

    def gen_test(self):
        res = ""
        for arg in self.args:
            if isinstance(arg, Reg):
                res += arg.load_random()
            elif isinstance(arg, Const):
                pass
            else:
                raise RuntimeError("Unknown arg for '" + self.name + "'")
        res += str(self) + "\n"
        return res

    def __str__(self):
        res = "rstv\n"
        res += self.name + " "
        res += str(self.dst) + ", "
        for arg in self.args:
            res += str(arg) + ", "
        res = res[:-2] if len(self.args) > 0 else res
        return res

