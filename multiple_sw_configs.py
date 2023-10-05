import getpass
import telnetlib

user = input('Enter the username: ')
password = getpass.getpass()  #password input

for m in range(11, 16):
    HOST = f'192.168.122.{m}'
    tn = telnetlib.Telnet(HOST, timeout=20)
    tn.read_until(b'Username: ') #b before the string indicates that is a bytes object
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"vlan database\n")

    for m in range(2, 20):
        vlan_command = f"vlan {m} name Python_vlan_{m}\n"
        tn.write(vlan_command.encode('ascii'))

    output = tn.read_all().decode('ascii')
    print(output)
