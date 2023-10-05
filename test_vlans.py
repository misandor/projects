import unittest
import getpass
import telnetlib

class TestVlan(unittest.TestCase):
    def setUp(self):
        self.Host = "192.168.122.11"
        self.user = input("Enter your username: ")
        self.password = getpass.getpass()
        self.tn = telnetlib.Telnet(self.Host)

    def clean(self):
        self.tn.close()

    def login(self):
        self.tn.read_until(b"Username")
        self.tn.write(self.user.encode('ascii') + b"\n")
        if self.password:
            self.tn.read_until(b"Password: ")
            self.tn.write(self.password.encode('ascii') + b"\n")

    def test_vlan(self):
        self.tn.write(b"show vlan-switch\n")
        self.assertIn("Python_vlan_17", "Vlan 'Python_vlan_17' not found in the list")

if __name__ == '__main__':
    unittest.main()



