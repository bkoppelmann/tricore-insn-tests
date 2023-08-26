from isa import DReg, Insn

insnlist = [
    Insn("add.f", DReg(5), [DReg(6), DReg(7)]),
    Insn("cmp.f", DReg(5), [DReg(6), DReg(7)]),
    Insn("div.f", DReg(5), [DReg(6), DReg(7)]),
    Insn("ftoi", DReg(5), [DReg(6)]),
    Insn("ftoiz", DReg(5), [DReg(6)]),
    #Insn("ftoq31", DReg(5), [DReg(6), DReg(7)]),
    #Insn("ftoq31z", DReg(5), [DReg(6), DReg(7)]),
    Insn("ftou", DReg(5), [DReg(6)]),
    Insn("ftouz", DReg(5), [DReg(6)]),
    Insn("ftohp", DReg(5), [DReg(6)]),
    Insn("hptof", DReg(5), [DReg(6)]),
    Insn("itof", DReg(5), [DReg(6)]),
    Insn("madd.f", DReg(5), [DReg(6), DReg(7), DReg(8)]),
    Insn("msub.f", DReg(5), [DReg(6), DReg(7), DReg(8)]),
    Insn("mul.f", DReg(5), [DReg(6), DReg(7)]),
    #Insn("q31tof", DReg(5), [DReg(6), DReg(7)]),
    #Insn("qseed.f", DReg(5), [DReg(6), DReg(7)]),
    Insn("sub.f", DReg(5), [DReg(6), DReg(7)]),
    Insn("updfl", DReg(5), []),
    Insn("utof", DReg(5), [DReg(6)]),
]

