import telnetlib
import time

host_ip = '184.105.247.70'
user = 'pyclass'
password = '88newclass'

TIMEOUT = 6
PORT = 23

con = telnetlib.Telnet(host_ip, PORT, TIMEOUT)
con.read_until('sername:', TIMEOUT)
con.write(user + '\n')
con.read_until('assword:', TIMEOUT)
con.write(password + '\n')

time.sleep(1)

output = con.read_very_eager()
print output

con.write('show ip int brief' + '\n')
time.sleep(1)

output = con.read_very_eager()
print output

con.close()
