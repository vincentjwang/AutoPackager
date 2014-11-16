import subprocess

filename = r'F:\C# Code Center\ChatRoom\ChatRoom\ChatRoom.csproj'
p = subprocess.Popen(['C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe', filename], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line
