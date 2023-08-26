from isa import DReg, EReg, PReg, AReg, Insn, Const

insnlist = [
    Insn("abs", DReg(0), [ DReg(0)]),
    Insn("abs.b", DReg(0), [ DReg(0)]),
    Insn("abs.h", DReg(0), [ DReg(0)]),
    Insn("absdif", DReg(0), [ DReg(0),Const(9)]),
    Insn("absdif", DReg(0), [ DReg(0), DReg(2)]),
    Insn("absdif.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("absdif.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("absdifs", DReg(0), [ DReg(0),Const(9)]),
    Insn("absdifs", DReg(0), [ DReg(0), DReg(2)]),
    Insn("absdifs.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("abss", DReg(0), [ DReg(0)]),
    Insn("abss.h", DReg(0), [ DReg(0)]),
    Insn("add", DReg(0), [ DReg(0),Const(9)]),
    Insn("add", DReg(0), [ DReg(0), DReg(2)]),
    Insn("add", DReg(0), [Const(4)]),
    Insn("add", DReg(0), [ DReg(15),Const(4)]),
    Insn("add", DReg(15), [ DReg(0),Const(4)]),
    Insn("add", DReg(0), [ DReg(0)]),
    Insn("add", DReg(0), [ DReg(15), DReg(2)]),
    Insn("add", DReg(15), [ DReg(0), DReg(2)]),
    Insn("add.a", AReg(0), [ AReg(0), AReg(2)]),
    Insn("add.a", AReg(0), [Const(4)]),
    Insn("add.a", AReg(0), [ AReg(0)]),
    Insn("add.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("add.f", DReg(0), [ DReg(0), DReg(2)]),
    Insn("add.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("addc", DReg(0), [ DReg(0),Const(9)]),
    Insn("addc", DReg(0), [ DReg(0), DReg(2)]),
    Insn("addi", DReg(0), [ DReg(0),Const(16)]),
    Insn("addih", DReg(0), [ DReg(0),Const(16)]),
    Insn("addih.a", AReg(0), [ AReg(0),Const(16)]),
    Insn("adds", DReg(0), [ DReg(0),Const(9)]),
    Insn("adds", DReg(0), [ DReg(0), DReg(2)]),
    Insn("adds", DReg(0), [ DReg(0)]),
    Insn("adds.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("adds.hu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("adds.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("adds.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("addsc.a", AReg(0), [ AReg(0), DReg(2),Const(2)]),
    Insn("addsc.a", AReg(0), [ AReg(0), DReg(15),Const(2)]),
    Insn("addsc.at", AReg(0), [ AReg(0), DReg(2)]),
    Insn("addx", DReg(0), [ DReg(0),Const(9)]),
    Insn("addx", DReg(0), [ DReg(0), DReg(2)]),
    Insn("and", DReg(0), [ DReg(0),Const(9)]),
    Insn("and", DReg(0), [ DReg(0), DReg(2)]),
    Insn("and", DReg(15), [Const(8)]),
    Insn("and", DReg(0), [ DReg(0)]),
    Insn("and.and.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("and.andn.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("and.eq", DReg(0), [ DReg(0),Const(9)]),
    Insn("and.eq", DReg(0), [ DReg(0), DReg(2)]),
    Insn("and.ge", DReg(0), [ DReg(0),Const(9)]),
    Insn("and.ge", DReg(0), [ DReg(0), DReg(2)]),
    Insn("and.ge.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("and.ge.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("and.lt", DReg(0), [ DReg(0),Const(9)]),
    Insn("and.lt", DReg(0), [ DReg(0), DReg(2)]),
    Insn("and.lt.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("and.lt.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("and.ne", DReg(0), [ DReg(0),Const(9)]),
    Insn("and.ne", DReg(0), [ DReg(0), DReg(2)]),
    Insn("and.nor.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("and.or.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("and.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("andn", DReg(0), [ DReg(0),Const(9)]),
    Insn("andn", DReg(0), [ DReg(0), DReg(2)]),
    Insn("andn.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("bmerge", DReg(0), [ DReg(0), DReg(2)]),
    Insn("bsplit", EReg(0), [ DReg(2)]),
    Insn("cadd", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("cadd", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("cadd", DReg(0), [ DReg(15),Const(4)]),
    Insn("caddn", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("caddn", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("caddn", DReg(0), [ DReg(15),Const(4)]),
    Insn("clo", DReg(0), [ DReg(0)]),
    Insn("clo.h", DReg(0), [ DReg(0)]),
    Insn("cls", DReg(0), [ DReg(0)]),
    Insn("cls.h", DReg(0), [ DReg(0)]),
    Insn("clz", DReg(0), [ DReg(0)]),
    Insn("clz.h", DReg(0), [ DReg(0)]),
    Insn("cmov", DReg(0), [ DReg(15),Const(4)]),
    Insn("cmov", DReg(0), [ DReg(15), DReg(2)]),
    Insn("cmovn", DReg(0), [ DReg(15),Const(4)]),
    Insn("cmovn", DReg(0), [ DReg(15), DReg(2)]),
    Insn("cmp.f", DReg(0), [ DReg(0), DReg(2)]),
    Insn("crc32.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("crc32b.w", DReg(0), [ DReg(0), DReg(2)]),
    Insn("crc32l.w", DReg(0), [ DReg(0), DReg(2)]),
    Insn("csub", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("csubn", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("dextr", DReg(0), [ DReg(0), DReg(2), Const(4)]),
    Insn("dextr", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("div", EReg(0), [ DReg(2), DReg(3)]),
    Insn("div.f", DReg(0), [ DReg(0), DReg(2)]),
    Insn("div.u", EReg(0), [ DReg(2), DReg(3)]),
    Insn("dvadj", EReg(0), [ EReg(2), DReg(4)]),
    Insn("dvinit", EReg(0), [ DReg(2), DReg(3)]),
    Insn("dvinit.b", EReg(0), [ DReg(2), DReg(3)]),
    Insn("dvinit.bu", EReg(0), [ DReg(2), DReg(3)]),
    Insn("dvinit.h", EReg(0), [ DReg(2), DReg(3)]),
    Insn("dvinit.hu", EReg(0), [ DReg(2), DReg(3)]),
    Insn("dvinit.u", EReg(0), [ DReg(2), DReg(3)]),
#    Insn("dvstep", EReg(0), [ EReg(2), DReg(4)]),
    Insn("dvstep.u", EReg(0), [ EReg(2), DReg(4)]),
    Insn("eq", DReg(0), [ DReg(0),Const(9)]),
    Insn("eq", DReg(0), [ DReg(0), DReg(2)]),
    Insn("eq", DReg(15), [ DReg(0),Const(4)]),
    Insn("eq", DReg(15), [ DReg(0), DReg(2)]),
    Insn("eq.a", DReg(0), [ AReg(0), AReg(2)]),
    Insn("eq.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("eq.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("eq.w", DReg(0), [ DReg(0), DReg(2)]),
    Insn("eqany.b", DReg(0), [ DReg(0),Const(9)]),
    Insn("eqany.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("eqany.h", DReg(0), [ DReg(0),Const(9)]),
    Insn("eqany.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("eqz.a", DReg(0), [ AReg(0)]),
    Insn("ftohp", DReg(0), [ DReg(0)]),
    Insn("ftoi", DReg(0), [ DReg(0)]),
    Insn("ftoiz", DReg(0), [ DReg(0)]),
    Insn("ftou", DReg(0), [ DReg(0)]),
    Insn("ftouz", DReg(0), [ DReg(0)]),
    Insn("ge", DReg(0), [ DReg(0),Const(9)]),
    Insn("ge", DReg(0), [ DReg(0), DReg(2)]),
    Insn("ge.a", DReg(0), [ AReg(0), AReg(2)]),
    Insn("ge.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("ge.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("hptof", DReg(0), [ DReg(0)]),
    Insn("imask", EReg(0), [Const(4), Const(4), Const(4)]),
    Insn("imask", EReg(0), [Const(4), DReg(2), Const(4)]),
    Insn("imask", EReg(0), [ DReg(2), Const(4), Const(4)]),
    Insn("imask", EReg(0), [ DReg(2), DReg(3), Const(4)]),
    Insn("ins.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("insert", DReg(0), [ DReg(0),Const(4), Const(4), Const(4)]),
    Insn("insert", DReg(0), [ DReg(0),Const(4), EReg(2)]),
    Insn("insert", DReg(0), [ DReg(0),Const(4), DReg(2), Const(4)]),
    Insn("insert", DReg(0), [ DReg(0), DReg(2), Const(4), Const(4)]),
    Insn("insert", DReg(0), [ DReg(0), DReg(2), EReg(4)]),
    Insn("insert", DReg(0), [ DReg(0), DReg(2), DReg(3), Const(4)]),
    Insn("insn.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("itof", DReg(0), [ DReg(0)]),
    Insn("ixmax", EReg(0), [ EReg(2), DReg(4)]),
    Insn("ixmax.u", EReg(0), [ EReg(2), DReg(4)]),
    Insn("ixmin", EReg(0), [ EReg(2), DReg(4)]),
    Insn("ixmin.u", EReg(0), [ EReg(2), DReg(4)]),
    Insn("lt", DReg(0), [ DReg(0),Const(9)]),
    Insn("lt", DReg(0), [ DReg(0), DReg(2)]),
    Insn("lt", DReg(15), [ DReg(0),Const(4)]),
    Insn("lt", DReg(15), [ DReg(0), DReg(2)]),
    Insn("lt.a", DReg(0), [ AReg(0), AReg(2)]),
    Insn("lt.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("lt.bu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("lt.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("lt.hu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("lt.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("lt.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("lt.w", DReg(0), [ DReg(0), DReg(2)]),
    Insn("lt.wu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("madd", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("madd", EReg(0), [ EReg(2), DReg(4),Const(9)]),
    Insn("madd", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("madd", EReg(0), [ EReg(2), DReg(4), DReg(5)]),
    Insn("madd.f", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("madd.q", DReg(0), [ DReg(0), DReg(2), DReg(3),Const(2)]),
    Insn("madd.q", EReg(0), [ EReg(2), DReg(4), DReg(5),Const(2)]),
    Insn("madd.u", EReg(0), [ EReg(2), DReg(4),Const(9)]),
    Insn("madd.u", EReg(0), [ EReg(2), DReg(4), DReg(5)]),
    Insn("madds", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("madds", EReg(0), [ EReg(2), DReg(4),Const(9)]),
    Insn("madds", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("madds", EReg(0), [ EReg(2), DReg(4), DReg(5)]),
    Insn("madds.q", DReg(0), [ DReg(0), DReg(2), DReg(3),Const(2)]),
    Insn("madds.q", EReg(0), [ EReg(2), DReg(4), DReg(5),Const(2)]),
    Insn("madds.u", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("madds.u", EReg(0), [ EReg(2), DReg(4),Const(9)]),
    Insn("madds.u", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("madds.u", EReg(0), [ EReg(2), DReg(4), DReg(5)]),
    Insn("max", DReg(0), [ DReg(0),Const(9)]),
    Insn("max", DReg(0), [ DReg(0), DReg(2)]),
    Insn("max.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("max.bu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("max.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("max.hu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("max.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("max.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("min", DReg(0), [ DReg(0),Const(9)]),
    Insn("min", DReg(0), [ DReg(0), DReg(2)]),
    Insn("min.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("min.bu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("min.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("min.hu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("min.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("min.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("mov", DReg(0), [Const(16)]),
    Insn("mov", EReg(0), [Const(16)]),
    Insn("mov", DReg(0), [ DReg(0)]),
    Insn("mov", EReg(0), [ DReg(2)]),
    Insn("mov", EReg(0), [ DReg(2), DReg(3)]),
    Insn("mov", DReg(15), [Const(8)]),
    Insn("mov", DReg(0), [Const(4)]),
    Insn("mov", EReg(0), [Const(4)]),
    Insn("mov", DReg(0), [ DReg(0)]),
    Insn("mov.a", AReg(0), [ DReg(0)]),
    Insn("mov.a", AReg(0), [Const(4)]),
    Insn("mov.a", AReg(0), [ DReg(0)]),
    Insn("mov.aa", AReg(0), [ AReg(0)]),
    Insn("mov.aa", AReg(0), [ AReg(0)]),
    Insn("mov.d", DReg(0), [ AReg(0)]),
    Insn("mov.d", DReg(0), [ AReg(0)]),
    Insn("mov.u", DReg(0), [Const(16)]),
    Insn("movh", DReg(0), [Const(16)]),
    Insn("movh.a", AReg(0), [Const(16)]),
    Insn("msub", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("msub", EReg(0), [ EReg(2), DReg(4),Const(9)]),
    Insn("msub", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("msub", EReg(0), [ EReg(2), DReg(4), DReg(5)]),
    Insn("msub.f", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("msub.q", DReg(0), [ DReg(0), DReg(2), DReg(3),Const(2)]),
    Insn("msub.q", EReg(0), [ EReg(2), DReg(4), DReg(5),Const(2)]),
    Insn("msub.u", EReg(0), [ EReg(2), DReg(4),Const(9)]),
    Insn("msub.u", EReg(0), [ EReg(2), DReg(4), DReg(5)]),
    Insn("msubs", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("msubs", EReg(0), [ EReg(2), DReg(4),Const(9)]),
    Insn("msubs", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("msubs", EReg(0), [ EReg(2), DReg(4), DReg(5)]),
    Insn("msubs.q", DReg(0), [ DReg(0), DReg(2), DReg(3),Const(2)]),
    Insn("msubs.q", EReg(0), [ EReg(2), DReg(4), DReg(5),Const(2)]),
    Insn("msubs.u", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("msubs.u", EReg(0), [ EReg(2), DReg(4),Const(9)]),
    Insn("msubs.u", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("msubs.u", EReg(0), [ EReg(2), DReg(4), DReg(5)]),
    Insn("mul", DReg(0), [ DReg(0),Const(9)]),
    Insn("mul", EReg(0), [ DReg(2),Const(9)]),
    Insn("mul", DReg(0), [ DReg(0), DReg(2)]),
    Insn("mul", EReg(0), [ DReg(2), DReg(3)]),
    Insn("mul", DReg(0), [ DReg(0)]),
    Insn("mul.f", DReg(0), [ DReg(0), DReg(2)]),
    Insn("mul.q", DReg(0), [ DReg(0), DReg(2),Const(2)]),
    Insn("mul.q", EReg(0), [ DReg(2), DReg(3),Const(2)]),
    Insn("mul.u", EReg(0), [ DReg(2),Const(9)]),
    Insn("mul.u", EReg(0), [ DReg(2), DReg(3)]),
    Insn("muls", DReg(0), [ DReg(0),Const(9)]),
    Insn("muls", DReg(0), [ DReg(0), DReg(2)]),
    Insn("muls.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("muls.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("nand", DReg(0), [ DReg(0),Const(9)]),
    Insn("nand", DReg(0), [ DReg(0), DReg(2)]),
    Insn("nand.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("ne", DReg(0), [ DReg(0),Const(9)]),
    Insn("ne", DReg(0), [ DReg(0), DReg(2)]),
    Insn("ne.a", DReg(0), [ AReg(0), AReg(2)]),
    Insn("nez.a", DReg(0), [ AReg(0)]),
    Insn("nor", DReg(0), [ DReg(0),Const(9)]),
    Insn("nor", DReg(0), [ DReg(0), DReg(2)]),
    Insn("nor.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("or", DReg(0), [ DReg(0),Const(9)]),
    Insn("or", DReg(0), [ DReg(0), DReg(2)]),
    Insn("or", DReg(15), [Const(8)]),
    Insn("or", DReg(0), [ DReg(0)]),
    Insn("or.and.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("or.andn.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("or.eq", DReg(0), [ DReg(0),Const(9)]),
    Insn("or.eq", DReg(0), [ DReg(0), DReg(2)]),
    Insn("or.ge", DReg(0), [ DReg(0),Const(9)]),
    Insn("or.ge", DReg(0), [ DReg(0), DReg(2)]),
    Insn("or.ge.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("or.ge.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("or.lt", DReg(0), [ DReg(0),Const(9)]),
    Insn("or.lt", DReg(0), [ DReg(0), DReg(2)]),
    Insn("or.lt.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("or.lt.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("or.ne", DReg(0), [ DReg(0),Const(9)]),
    Insn("or.ne", DReg(0), [ DReg(0), DReg(2)]),
    Insn("or.nor.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("or.or.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("or.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("orn", DReg(0), [ DReg(0),Const(9)]),
    Insn("orn", DReg(0), [ DReg(0), DReg(2)]),
    Insn("orn.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("pack", DReg(0), [ EReg(2), DReg(4)]),
    Insn("parity", DReg(0), [ DReg(0)]),
    Insn("popcnt.w", DReg(0), [ DReg(0)]),
    Insn("rsub", DReg(0), [ DReg(0),Const(9)]),
    Insn("rsubs", DReg(0), [ DReg(0),Const(9)]),
    Insn("rsubs.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("sat.b", DReg(0), [ DReg(0)]),
    Insn("sat.bu", DReg(0), [ DReg(0)]),
    Insn("sat.h", DReg(0), [ DReg(0)]),
    Insn("sat.hu", DReg(0), [ DReg(0)]),
    Insn("sel", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("sel", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("seln", DReg(0), [ DReg(0), DReg(2),Const(9)]),
    Insn("seln", DReg(0), [ DReg(0), DReg(2), DReg(3)]),
    Insn("sh", DReg(0), [ DReg(0),Const(9)]),
    Insn("sh", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sh", DReg(0), [Const(4)]),
    Insn("sh.and.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("sh.andn.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("sh.eq", DReg(0), [ DReg(0),Const(9)]),
    Insn("sh.eq", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sh.ge", DReg(0), [ DReg(0),Const(9)]),
    Insn("sh.ge", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sh.ge.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("sh.ge.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sh.h", DReg(0), [ DReg(0),Const(9)]),
    Insn("sh.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sh.lt", DReg(0), [ DReg(0),Const(9)]),
    Insn("sh.lt", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sh.lt.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("sh.lt.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sh.nand.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("sh.ne", DReg(0), [ DReg(0),Const(9)]),
    Insn("sh.ne", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sh.nor.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("sh.or.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("sh.orn.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("sh.xnor.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("sh.xor.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("sha", DReg(0), [ DReg(0),Const(9)]),
    Insn("sha", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sha", DReg(0), [Const(4)]),
    Insn("sha.h", DReg(0), [ DReg(0),Const(9)]),
    Insn("sha.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("shas", DReg(0), [ DReg(0),Const(9)]),
    Insn("shas", DReg(0), [ DReg(0), DReg(2)]),
    Insn("shuffle", DReg(0), [ DReg(0),Const(9)]),
    Insn("sub", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sub", DReg(0), [ DReg(0)]),
    Insn("sub", DReg(0), [ DReg(15), DReg(2)]),
    Insn("sub", DReg(15), [ DReg(0), DReg(2)]),
    Insn("sub.a", AReg(0), [ AReg(0), AReg(2)]),
    Insn("sub.a", AReg(10), [Const(8)]),
    Insn("sub.b", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sub.f", DReg(0), [ DReg(0), DReg(2)]),
    Insn("sub.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("subc", DReg(0), [ DReg(0), DReg(2)]),
    Insn("subs", DReg(0), [ DReg(0), DReg(2)]),
    Insn("subs", DReg(0), [ DReg(0)]),
    Insn("subs.h", DReg(0), [ DReg(0), DReg(2)]),
    Insn("subs.hu", DReg(0), [ DReg(0), DReg(2)]),
    Insn("subs.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("subx", DReg(0), [ DReg(0), DReg(2)]),
    Insn("unpack", EReg(0), [ DReg(2)]),
    Insn("utof", DReg(0), [ DReg(0)]),
    Insn("xnor", DReg(0), [ DReg(0),Const(9)]),
    Insn("xnor", DReg(0), [ DReg(0), DReg(2)]),
    Insn("xnor.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
    Insn("xor", DReg(0), [ DReg(0),Const(9)]),
    Insn("xor", DReg(0), [ DReg(0), DReg(2)]),
    Insn("xor", DReg(0), [ DReg(0)]),
    Insn("xor.eq", DReg(0), [ DReg(0),Const(9)]),
    Insn("xor.eq", DReg(0), [ DReg(0), DReg(2)]),
    Insn("xor.ge", DReg(0), [ DReg(0),Const(9)]),
    Insn("xor.ge", DReg(0), [ DReg(0), DReg(2)]),
    Insn("xor.ge.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("xor.ge.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("xor.lt", DReg(0), [ DReg(0),Const(9)]),
    Insn("xor.lt", DReg(0), [ DReg(0), DReg(2)]),
    Insn("xor.lt.u", DReg(0), [ DReg(0),Const(9)]),
    Insn("xor.lt.u", DReg(0), [ DReg(0), DReg(2)]),
    Insn("xor.ne", DReg(0), [ DReg(0),Const(9)]),
    Insn("xor.ne", DReg(0), [ DReg(0), DReg(2)]),
    Insn("xor.t", DReg(0), [ DReg(0), Const(4), DReg(2), Const(4)]),
]
