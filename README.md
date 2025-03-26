<<<<<<< HEAD
# Whyp 音频下载器 🎧

一个用于解析并下载 [Whyp.it](https://whyp.it) 音频的 Python 小工具。

---


## ✨ 功能特色

- 🔗 输入 Whyp 链接，一键解析 `.mp3` 文件
- 📥 自动命名保存，支持下载进度条 + 百分比显示
- 🖼️ 图形界面简洁可爱，颜色可自定义
- 🧊 可打包成 `.exe`，无 Python 环境也可运行
- 🛡️ 开源可控，纯净无后门

---

## 💻 使用方法

### 🧩 安装依赖（源码方式）

```bash
pip install requests
```

### 🚀 运行程序

```bash
python whyp_gui.py
```

### 📦 打包成 .exe

```bash
pyinstaller --onefile --noconsole --icon=logo_dark.ico whyp_gui.py
```

生成的可执行程序在 `dist/` 目录下。

## 🧾 文件结构

```bash
WhypDownloader/
├── whyp_gui.py        # 主程序
├── logo_dark.ico      # 图标文件
├── README.md
├── .gitignore
├── LICENSE            # MIT 开源协议
└── dist/
    └── whyp_gui.exe   # 打包后的程序
```

---

## 📁 下载安装

[点此下载最新版本 ⬇](https://github.com/Tulocy/WhypDownloader/releases/latest)

---

## 📃 开源协议

本项目采用 MIT License 进行开源。
你可以自由地复制、修改、再发布，但请保留原作者署名，作者不对使用造成的问题负责。
