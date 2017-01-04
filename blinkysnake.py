import linecache

a = linecache.getlines('/proc/net/dev')

e1 = a[0]
e2 = a[1]

a = a[2:]

_, headers_receive, headers_transmit = e2.split('|')
headers_receive = headers_receive.split()
headers_transmit = headers_transmit.split()

inames = []
ifaces = {}
for i in a:
  name, values = i.split(':')
  values = values.split()
  ifaces[name] = {'Receive': {}, 'Transmit': {}}
  for x in range(len(headers_receive)):
    ifaces[name]['Receive'][headers_receive[x]] = values[x]
  for x in range(len(headers_transmit)):
    ifaces[name]['Transmit'][headers_transmit[x]] = values[x + len(headers_receive)]

def listifaces():
  for key, value in ifaces.iteritems():
    inames.append(key.strip()) 
  return(inames)

def ifconfig():
	return(ifaces)

def ifaceinfo(iface):
  return(ifaces[iface])

