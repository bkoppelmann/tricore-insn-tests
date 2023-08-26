.PHONY: tsim all

QEMU = /home/juander/code/qemu/build/qemu-system-tricore
QARGS = -M tricore_testboard -cpu tc37x -nographic -d cpu,exec,nochain -D qemu.log -singlestep

all: test.elf

gdb: test.elf
	cgdb $(QEMU) -- --args $(QEMU) $(QARGS) --kernel $<

qemu: test.elf
	$(QEMU) $(QARGS) -kernel $<

tsim: test.elf
	tsim -S 0x80000000 -e -o $<

tsim16p_e: test.elf
	tsim16p_e -tc162p -S 0x80000000 -e -o $<

%.elf: %.o
	tricore-ld -Tlink.ld --mcpu=tc162 -o $@ $<

%.o: %.S
	tricore-as -mtc162 -o $@ $<

clean:
	rm -f *.elf *.o
