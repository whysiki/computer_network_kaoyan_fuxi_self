#!/bin/bash

# 更新系统
echo "更新系统..."
sudo apt update && sudo apt upgrade -y

# 安装常用工具
echo "安装常用工具..."
sudo apt install -y git curl wget vim htop build-essential

# 安装Python和pip
echo "安装Python和pip..."
sudo apt install -y python3 python3-pip

# 安装Docker
echo "安装Docker..."
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce
sudo usermod -aG docker $USER

# 安装常用编程语言和环境
echo "安装Node.js..."
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install -y nodejs

echo "安装Java..."
sudo apt install -y openjdk-11-jdk

# 设置防火墙
echo "设置防火墙..."
sudo ufw allow OpenSSH
sudo ufw enable

# 清理不需要的软件包
echo "清理不需要的软件包..."
sudo apt autoremove -y

echo "初始化完成！请重新启动系统以应用所有更改。"
