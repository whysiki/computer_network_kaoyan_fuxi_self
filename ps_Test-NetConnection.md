`Test-NetConnection` 是 PowerShell 中用于测试网络连接的 cmdlet。

它是 Windows PowerShell 4.0 版本引入的。该命令用于执行各种网络连接测试，包括测试端口的可达性、路由跟踪、以及使用 PowerShell Remoting 进行连接等。以下是 `Test-NetConnection` 命令的基本用法和参数解释：

### 基本用法：

```powershell
Test-NetConnection -ComputerName <目标计算机> -Port <端口号>
```

### 参数解释：

- `-ComputerName`：指定要测试的目标计算机的名称或 IP 地址。
- `-Port`：指定要测试的端口号。
- `-InformationLevel`：指定输出信息的详细级别。常见的值有 "Detailed"、"Terse" 和 "Quiet"。默认是 "Detailed"，会提供详细的连接信息。
- `-CommonTCPPort`：指定一个常见的 TCP 端口，用于快速测试网络连接。
- `-TraceRoute`：执行路由跟踪，显示从本地到目标计算机的路由信息。
- `-RemotePort`：使用 PowerShell Remoting 测试连接。
- `-UdpTest`：执行 UDP 连接测试。

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

这个命令提供了一种方便的方式来在 PowerShell 中测试网络连接，帮助管理员诊断网络问题。
