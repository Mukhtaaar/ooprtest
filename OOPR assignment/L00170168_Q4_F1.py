import socket
ip = '192.168.196.128' #the Ip address of the virtual machine I have created
port_list = (20, 80, 8080, 139, 445, 23, 21, 22)
for port in port_list:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #connecting directly to an IPV4 address
    result = s.connect_ex((ip, port))
    if result ==0:                    #means the port is open
        print('port:',port, 'SSH') #as Instructed in CA2 assignment if port 22 is open I should print SSH
    else:
        print('port:',port, 'HTTP')
