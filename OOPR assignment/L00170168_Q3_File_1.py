import paramiko

ip= "192.168.196.128"          #the ip adress of the virtual machine I have created
port = 22                      #the SSH server port which is 22
user = "l00170168"
password = "Hooyoqeex2"

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #add any missing keys when I'm connecting remote server
    session.connect(ip.rstrip("\n"),
    username=user_name, password=user_password)
    connection = session.invoke_shell()
    session.exec_command('mkdir This\n')
except:                                                         #catching for any errors
       print("Connection succesful..")
