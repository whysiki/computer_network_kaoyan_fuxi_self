
## tcp Test-NetConnection
```ps
PS C:\Users\Administrator> Test-NetConnection -ComputerName www.example.com -Port 443

ComputerName     : www.example.com
RemoteAddress    : 93.184.215.14
RemotePort       : 443
InterfaceAlias   : WLAN
SourceAddress    : 192.168.100.222
TcpTestSucceeded : True

PS C:\Users\Administrator> Test-NetConnection -ComputerName 93.184.215.14 -Port 443

ComputerName     : 93.184.215.14
RemoteAddress    : 93.184.215.14
RemotePort       : 443
InterfaceAlias   : WLAN
SourceAddress    : 192.168.100.222
TcpTestSucceeded : True
```


在 Windows 系统上，有几种方法可以检查本机是否能够通过特定的 TCP 或 UDP 端口连接到互联网。以下是一些常用的方法和工具：

### 方法一：使用 `telnet` 命令检查 TCP 端口

1. **启用 telnet 客户端**（如果尚未启用）：
   - 打开“控制面板”，选择“程序”，然后点击“启用或关闭 Windows 功能”。
   - 在列表中找到“Telnet 客户端”，勾选并点击“确定”以启用。

2. **使用 telnet 检查端口连通性**：
   - 打开命令提示符（cmd）。
   - 输入以下命令，检查特定的 TCP 端口：
     ```
     telnet <目标主机> <端口号>
     ```
     例如，检查本机是否能通过 TCP 端口 80 连接到某个网站：
     ```
     telnet www.example.com 80
     ```
   - 如果连接成功，屏幕上会显示一个空白窗口，表示连接成功。如果连接失败，会显示错误消息。

### 方法二：使用 `Test-NetConnection` PowerShell 命令检查 TCP 端口

1. **打开 PowerShell**：
   - 搜索 PowerShell 或在命令提示符中输入 `powershell` 并按 Enter。

2. **使用 `Test-NetConnection` 命令**：
   - 输入以下命令检查特定的 TCP 端口：
     ```
     Test-NetConnection -ComputerName <目标主机> -Port <端口号>
     ```
     例如，检查本机是否能通过 TCP 端口 443 连接到某个网站：
     ```
     Test-NetConnection -ComputerName www.example.com -Port 443
     ```

### 方法三：使用第三方工具检查 UDP 端口

由于 telnet 和 `Test-NetConnection` 主要用于检查 TCP 端口，对于 UDP 端口的检查，可以使用以下方法：

1. **使用 `nmap` 工具**：
   - `nmap` 是一个功能强大的网络扫描工具，可以用于检查 UDP 端口。
   - 下载并安装 `nmap`（可以从 [nmap 官方网站](https://nmap.org/download.html) 获取）。
   - 打开命令提示符，使用以下命令检查特定的 UDP 端口：
     ```
     nmap -sU -p <端口号> <目标主机>
     ```
     例如，检查本机是否能通过 UDP 端口 53 连接到某个 DNS 服务器：
     ```
     nmap -sU -p 53 8.8.8.8
     ```

### 方法四：使用在线工具

有一些在线工具可以帮助检查特定端口的连通性，例如 [CanYouSeeMe.org](http://www.canyouseeme.org/)。输入要检查的端口号，工具会帮助你检测该端口是否对外开放并可访问。

通过上述方法，你可以检查本机是否能够通过特定的 TCP 或 UDP 端口连接到互联网。