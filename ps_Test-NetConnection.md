`Test-NetConnection` 是 PowerShell 中用于测试网络连接的 cmdlet。

它是 Windows PowerShell 4.0 版本引入的。该命令用于执行各种网络连接测试，包括测试端口的可达性、路由跟踪、以及使用 PowerShell Remoting 进行连接等。以下是 `Test-NetConnection` 命令的基本用法和参数解释：



Test-NetConnection -ComputerName -UdpTest example.com  -Port 80


### 基本用法：

```powershell
Test-NetConnection -ComputerName <目标计算机> -Port <端口号>
```
 ⚡S ❯❯ Get-Help Test-NetConnection

名称
    Test-NetConnection

语法
    Test-NetConnection [[-ComputerName] <string>]  [<CommonParameters>]

    Test-NetConnection [[-ComputerName] <string>] [-CommonTCPPort] {HTTP | RDP | SMB | WINRM}  [<CommonParameters>]

    Test-NetConnection [[-ComputerName] <string>]  [<CommonParameters>]

    Test-NetConnection [[-ComputerName] <string>]  [<CommonParameters>]


别名
    TNC


备注
    Get-Help 无法在此计算机上找到此 cmdlet 的帮助文件。只能显示部分帮助。
        -- 若要下载和安装包含此 cmdlet 的模块的帮助文件，请使用 Update-Help。



<!-- `Test-NetConnection` 命令的语法如下：

```powershell
Test-NetConnection [[-ComputerName] <string>] [-CommonTCPPort] {HTTP | RDP | SMB | WINRM} [<CommonParameters>]
```

让我们逐步解释这个语法：

- `[-ComputerName] <string>`：这是一个可选参数，用于指定要测试网络连接的目标计算机的名称或 IP 地址。如果不提供此参数，将默认为本地计算机。 -->

- `[-CommonTCPPort] {HTTP | RDP | SMB | WINRM}`：这是一个可选参数，用于指定要测试的常见 TCP 端口。你可以选择测试以下服务的端口：HTTP、RDP（远程桌面协议）、SMB（服务器消息块）、WINRM（Windows 远程管理服务）。你需要选择这些服务之一，并在花括号中提供相应的服务名称。

<!-- - `<CommonParameters>`：这是一组通用的 PowerShell 命令参数，可以应用于多个 PowerShell 命令。这包括参数，如 `-Verbose`、`-Debug`、`-ErrorAction` 等。

现在，让我们看几个示例来说明这个命令的使用：

1. **测试远程计算机的 HTTP 连接：**

   ```powershell
   Test-NetConnection -ComputerName remoteServer -CommonTCPPort HTTP
   ```

   这将测试与名为 "remoteServer" 的远程计算机的 HTTP 连接。

2. **测试本地计算机的 RDP 连接：**

   ```powershell
   Test-NetConnection -CommonTCPPort RDP
   ```

   这将测试本地计算机的远程桌面连接（RDP）。

3. **测试远程计算机的 SMB 连接：**

   ```powershell
   Test-NetConnection -ComputerName remoteServer -CommonTCPPort SMB
   ```

   这将测试与名为 "remoteServer" 的远程计算机的 SMB 连接。

4. **测试本地计算机的 WINRM 连接：**

   ```powershell
   Test-NetConnection -CommonTCPPort WINRM
   ```

   这将测试本地计算机的 Windows 远程管理服务（WINRM）连接。

总的来说，`Test-NetConnection` 是一个用于测试网络连接的方便工具，可以在 PowerShell 环境中轻松执行。通过选择目标计算机和要测试的服务端口，你可以检查网络连接的可用性和端口的开放状态。 -->











<!-- ### 参数解释：

- `-ComputerName`：指定要测试的目标计算机的名称或 IP 地址。
- `-Port`：指定要测试的端口号。
- `-InformationLevel`：指定输出信息的详细级别。常见的值有 "Detailed"、"Terse" 和 "Quiet"。默认是 "Detailed"，会提供详细的连接信息。
- `-CommonTCPPort`：指定一个常见的 TCP 端口，用于快速测试网络连接。
- `-TraceRoute`：执行路由跟踪，显示从本地到目标计算机的路由信息。
- `-RemotePort`：使用 PowerShell Remoting 测试连接。
- udp
- Test-NetConnection -ComputerName example.com -Port 53 -Udp


### 示例：

1. **测试 TCP 连接**：

   ```powershell
   Test-NetConnection -ComputerName example.com -Port 80
   ```

   这将测试到 `example.com` 的 80 端口的 TCP 连接。你会看到一些关于连接的详细信息，包括是否成功连接。
2. **使用 TraceRoute**：

   ```powershell
   Test-NetConnection -ComputerName example.com -TraceRoute
   ```

   这将执行路由跟踪，显示从本地到 `example.com` 的路由信息。
3. **使用 PowerShell Remoting 连接**：

   ```powershell
   Test-NetConnection -ComputerName example.com -RemotePort 5985
   ```

   这将测试到 `example.com` 的 WinRM 服务是否可达（5985 是默认的 WinRM 端口）。

这个命令提供了一种方便的方式来在 PowerShell 中测试网络连接，帮助管理员诊断网络问题。 -->
