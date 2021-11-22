import telnetlib

host = '192.168.50.10'
password = '123456'

tn = telnetlib.Telnet(host)
tn.read_until(b'Password:')
tn.write(password.encode('ascii') + b"\n")
print(tn.read_until(b'<R1>').decode('ascii'))
tn.close()
