import os
import paramiko
import time
raspiIP='192.168.100.81'
portpi=22
userpi='root'
passpi='fakhrilak'




# stdin,stdout,stderr=ssh.exec_command(cmd)

domain = str(input("masukan name domain map = "))
toIp = input("masukan ip tujuan = ")
toPort = input("masukan port tujuan = ")
fromPort = input("masukan port raspi = ")
k = open(str(domain)+'_zilog.conf', 'w')
print("///////////////////////////////////SET UP RASPBERY PI//////////////////////////")
arrpi = ["server {",
"          listen       "+fromPort+";",
"          location / {",
"               proxy_pass http://localhost:5000;",
"               proxy_set_header Host "+domain+".localhost;",
"               proxy_set_header        X-Real-IP $remote_addr;",
"               proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;",
"               proxy_set_header        X-Forwarded-Proto $scheme;",
"               proxy_http_version 1.1;",
"               proxy_set_header Upgrade $http_upgrade;",
"               proxy_set_header Connection 'upgrade';",
        '}',
'}']
for i in arrpi:
    k.write(i)
    k.write("\n")
k.detach()
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(raspiIP,portpi,userpi,passpi)
ftp_client=ssh.open_sftp()
ftp_client.put(str(domain)+'_zilog.conf',"/etc/nginx/conf.d/"+str(domain)+'_zilog.conf')
ftp_client.close()
stdin,stdout,stderr=ssh.exec_command("systemctl restart nginx")
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
ssh.close()
# rooted = os.system("sudo rm -rf "+str(domain)+'_zilog.conf')
time.sleep(3)

raspiIP='192.168.100.81'
port=4001
username='root'
password='stt123'




print("///////////////////////////////////SET UP 170 SERVER////////////////////////////")
f = open(str(domain)+'_zilog.conf', 'w')
arr = ["server {",
"        listen     80;",
"        listen     [::]:80;",
"        server_name    "+str(domain)+".localhost;",
"            location / {",
"                proxy_pass http://"+str(toIp)+":"+str(toPort)+"/;",
"                proxy_set_header        X-Real-IP $remote_addr;",
"                proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;",
"                proxy_set_header        X-Forwarded-Proto $scheme;",
"                proxy_http_version 1.1;",
"                proxy_set_header Upgrade $http_upgrade;",
"                proxy_set_header Connection 'upgrade';",
"            }",
"}"
]
for j in arr:
    f.write(j)
    f.write("\n")
f.detach()
ssh1=paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh1.connect(raspiIP,port,username,password)
ftp_client=ssh1.open_sftp()
ftp_client.put(str(domain)+'_zilog.conf',"/etc/nginx/conf.d/"+str(domain)+'_zilog.conf')
ftp_client.close()
stdin,stdout,stderr=ssh1.exec_command("systemctl restart nginx")
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
ssh1.close()
# rooted = os.system("rm -rf "+str(domain)+'_zilog.conf')
time.sleep(3)
print("///////////////////////////////////SET UP LOCAL SERVER////////////////////////////")
f = open(str(domain)+'_zilog.conf', 'w')
arrmypc = ["server {",
"        listen     8080;",
"        server_name    "+str(domain)+".localhost;",
"            location / {",
"                proxy_pass http://192.168.100.81:"+str(fromPort)+";",
"                proxy_set_header        X-Real-IP $remote_addr;",
"                proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;",
"                proxy_set_header        X-Forwarded-Proto $scheme;",
"                proxy_http_version 1.1;",
"                proxy_set_header Upgrade $http_upgrade;",
"                proxy_set_header Connection 'upgrade';",
"            }",
"}"
]
for k in arrmypc:
    f.write(k)
    f.write("\n")
rooted = os.popen("sudo chown root:root "+str(domain)+'_zilog.conf').read()
print(rooted)
moved = os.popen("sudo mv "+str(domain)+'_zilog.conf'+" /etc/nginx/conf.d/"+str(domain)+'_zilog.conf').read()
print(moved)
# removed = os.system("rm -rf "+str(domain)+'_zilog.conf')




