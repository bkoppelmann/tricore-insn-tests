_start:
#  movh %d10, hi:0xc4000b80
#  mov.u %d11, lo:0xc4000b80
#  or %d10, %d11
#  mtcr $psw, %d10
  _test_1:
 mov.u %d0,65535
 movh %d10,65535
 or %d0,%d10
 mov.u %d1,16
 movh %d10,0
 or %d1,%d10
 rstv
 insert %d3,%d0,10,%d1,8
  debug
