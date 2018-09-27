# -*- coding: utf-8 -*-

'''
Tip_010101 文件和目录操作-01
1. 显示搜索根目录下，每个子目录中文件的个数和总Bytes数量
2. 忽略名称中带CVS的子目录
3. https://docs.python.org/3.6/library/os.html
'''
import os
from os.path import join, getsize
for root, dirs, files in os.walk('..'):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories

'''
Tip_010102 文件和目录操作-02
1. 递归遍历目录目录中所有的文件和子目录
'''
import os
rootDir = r'..'
for root, dirs, files in os.walk(rootDir):
    print('{}{}'.format(root, os.sep))
    for i in files:
        print('{}{}{}'.format(root, os.sep, i))

'''
Tip_010103 文件和目录操作-03
1. 临时文件
2. 临时目录
3. with statement: https://docs.python.org/2.5/whatsnew/pep-343.html
'''
import tempfile

with tempfile.NamedTemporaryFile() as tmpFile:
    path = tmpFile.name
    print(path)
    tmpFile.write('haha\n'.encode())
    tmpFile.flush()
    print(open(path).read())

# print(open(path).read()) # NotFound

path = tempfile.mkdtemp() 
tmp = tempfile.NamedTemporaryFile(dir=path)
print(tmp.name)
#临时目录不会被自动删除，需要手动删除
# os.removedirs(path)
# import shutil
# shutil.rmtree(path)

'''
Tip_010201 Subprocess
1. call / check_output / Popen
1. https://docs.python.org/3.6/library/subprocess.html
'''
import subprocess, sys
# output=`ls -l`
output = subprocess.check_output(['ls', '-l'])

# output=`ls -l | grep hda`
p1 = subprocess.Popen(["ls", '-l'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "hda"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]

output=subprocess.check_output("ls -l | grep py", shell=True)
 
sts = os.system("ls" + " -l")
sts = subprocess.call("ls" + " -l", shell=True)
 
try:
    retcode = subprocess.call("ls" + " -l", shell=True)
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)

pid = subprocess.Popen(["ls", "-l"]).pid
print(pid)

'''
Tip_010301 FTP
1. https://docs.python.org/3.6/library/ftplib.html
'''
from ftplib import FTP
# ftp = FTP('ftp.debian.org')     # connect to host, default port
# ftp.login()                     # user anonymous, passwd anonymous@
# ftp.cwd('debian')               # change into "debian" directory
# ftp.retrlines('LIST')           # list directory contents
# ftp.retrbinary('RETR README', open('README', 'wb').write)
# ftp.quit()

with FTP("ftp1.at.proftpd.org") as ftp:
    ftp.login()
    ftp.dir()

'''
Tip_010302 SSH
'''
import paramiko, socket

paramiko.util.log_to_file('ssh.log')
ssh_con=paramiko.SSHClient()
ssh_con.load_system_host_keys()
ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh_con.connect(hostname='65.52.172.145',username='pear',password='a44e604C32792')
except paramiko.AuthenticationException:
    print("Auth Failed!")
except socket.error:
    print("Server is unreachable!")
else:
    stdin,stdout,stderr = ssh_con.exec_command('uname -a')
    print(stdout.read())
finally:
    ssh_con.close()
