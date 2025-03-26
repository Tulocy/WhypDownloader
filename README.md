# Whyp 音频下载器 🎧

一个用于解析并下载 [Whyp.it](https://whyp.it) 上音频的 Python 小工具。

## ✨ 功能特色

- 输入 Whyp 音频链接，一键下载 `.mp3`
- 自动提取音频标题，命名保存
- 下载进度条显示百分比
- 图形界面简洁美观，背景可自定义
- 支持打包为 `.exe`，无需安装 Python 环境

## 📦 使用方法

1. 安装依赖：
pip install requests

2. 运行主程序：
python whyp_gui.py

3. 打包：
pyinstaller --onefile --noconsole --icon=logo_dark.ico whyp_gui.py

生成的可执行程序在 `dist/` 目录下。

## 📁 文件结构
Whpy/ ├── whyp_gui.py # 主程序 ├── logo_dark.ico # 程序图标 ├── README.md # 项目说明 ├── .gitignore # 忽略文件 └── dist/ └── whyp_gui.exe # 可执行文件

---

## 6️⃣ 提交并推送到 GitHub

先连接远程仓库（把下面的 URL 换成你自己的仓库地址）：

```bash
git remote add origin https://github.com/你的用户名/WhypDownloader.git

然后添加所有文件并提交：
git add .
git commit -m "首次提交：添加 GUI 下载器源码"
git push -u origin master
