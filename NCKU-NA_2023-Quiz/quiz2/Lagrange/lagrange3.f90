PROGRAM LAGRANGE
IMPLICIT NONE

INTEGER::I,N,M
REAL(KIND=8),ALLOCATABLE::XU(:),YU(:)
REAL(KIND=8),ALLOCATABLE::XIN(:),YIN(:)

OPEN(311,FILE='INPUT.DAT',STATUS='UNKNOWN')
OPEN(312,FILE='OUTPUT.DAT',STATUS='UNKNOWN')

READ (311,*) N,M
ALLOCATE(XIN(N))
ALLOCATE(YIN(N))
ALLOCATE(XU(M))
ALLOCATE(YU(M))
DO I=1,N
 READ(311,*) XIN(I),YIN(I)
END DO
DO I=1,M
 READ(311,*) XU(I)
END DO

CALL lagra1(XIN,N,YIN,XU,M,YU)
DO I=1,M
WRITE(312,*) XU(I),YU(I)
END DO

WRITE(*,*) 'DONE!'
READ (*,*)

STOP
END PROGRAM

      subroutine lagra1(x,nd,y,xi,ni,yi)
!---LAGRANGE INTERPOLATINON METHOD
      implicit none
      integer::i,j,mm,ni,nd
      real(kind=8)::xi(ni),yi(ni)
      real(kind=8)::x(nd),y(nd)   
      real(kind=8)::pn,pi,xx
!
 1000 do 1013 mm=1,ni
      xx=xi(mm)
      pn=0.
      do 1012 i=1,nd
      pi=1.
      do 1011 j=1,nd
      if(i.eq.j) go to 1011
      pi=pi*(xx-x(j))/(x(i)-x(j))
 1011 continue
 1012 pn=pn+y(i)*pi
      yi(mm)=pn
 1013 continue
 2000 return
      end