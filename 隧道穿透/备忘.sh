sudo nano /etc/resolv.conf
root@pccacg1:~# nano /etc/systemd/resolved.conf

`/etc/resolv.conf` 和 `/etc/systemd/resolved.conf` 这两个文件在系统中的作用和配置内容有所不同。

### `/etc/resolv.conf`
`/etc/resolv.conf` 是一个用于配置系统 DNS 解析器的文件。它包含了 DNS 服务器的地址，当系统需要解析域名时，会查询这个文件中的 DNS 服务器。

**常见内容示例**：
```plaintext
nameserver 8.8.8.8
nameserver 8.8.4.4
```
这个文件直接指定了系统用来进行域名解析的 DNS 服务器。

### `/etc/systemd/resolved.conf`
`/etc/systemd/resolved.conf` 是 `systemd-resolved` 服务的配置文件。`systemd-resolved` 是一个提供 DNS 解析的服务，通过配置这个文件，可以控制 `systemd-resolved` 的行为和设置。

**常见内容示例**：
```plaintext
[Resolve]
DNS=8.8.8.8 8.8.4.4
FallbackDNS=
Domains=
LLMNR=no
MulticastDNS=no
DNSSEC=no
Cache=no
DNSStubListener=yes
```
这个文件可以配置多个选项，如 DNS 服务器、是否启用 LLMNR、多播 DNS、DNSSEC 等等。修改这个文件需要重启 `systemd-resolved` 服务以使更改生效。

### 差别总结
- **用途**：
  - `/etc/resolv.conf`：用于配置系统级别的 DNS 服务器。
  - `/etc/systemd/resolved.conf`：用于配置 `systemd-resolved` 服务的行为。

- **应用场景**：
  - `/etc/resolv.conf`：直接影响系统和所有应用的 DNS 解析。
  - `/etc/systemd/resolved.conf`：影响 `systemd-resolved` 服务的配置，需要这个服务运行并启用。

- **修改方式**：
  - 修改 `/etc/resolv.conf` 不需要重启服务，但需要确保 `systemd-resolved` 不会覆盖它。
  - 修改 `/etc/systemd/resolved.conf` 后需要重启 `systemd-resolved` 服务：
    ```bash
    sudo systemctl restart systemd-resolved
    ```

希望这些解释能帮助你理解这两个文件的差异和各自的用途。



https://github.com.cnpmjs.org/
https://hub.fastgit.org/


git clone https://hub.fastgit.org/wanhebin/clash-for-linux.git

git clone https://github.com/wnlen/clash-for-linux.git

git clone https://hub.fastgit.org/wnlen/clash-for-linux.git