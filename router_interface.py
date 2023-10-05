import getpass
import telnetlib


HOST = '192.168.122.10'
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST, timeout=5)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii')+b'\n')
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int fa1/0\n")
tn.write(b"ip add 10.10.13.13 255.255.255.240\n")
tn.write(b"no sh\n")
tn.write(b"int fa0/1\n")
tn.write(b"ip add 10.10.14.14 255.255.255.240\n")
tn.write(b"no sh\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"wr\n")
tn.write(b"end\n")

print(tn.read_all().decode('ascii'))
