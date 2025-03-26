import requests
import tkinter as tk
from tkinter import messagebox, ttk
import re
import string
import os

# 清理非法文件名
def sanitize_filename(title):
    invalid_chars = r'\/:*?"<>|'
    return ''.join(c for c in title if c not in invalid_chars and c in string.printable).strip().replace(" ", "_")

# 下载逻辑（含进度条）
def download_whyp():
    url = entry.get().strip()
    match = re.search(r'tracks/(\d+).*?token=([a-zA-Z0-9]+)', url)
    if not match:
        messagebox.showerror("❌ 错误", "无法解析链接，请检查格式")
        return

    track_id, token = match.group(1), match.group(2)
    api_url = f"https://api.whyp.it/api/tracks/{track_id}?token={token}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json().get("track", {})
        title = data.get("title", f"whyp_{track_id}")
        audio_url = data.get("audio_url")
        if not audio_url:
            messagebox.showerror("⚠️ 无法下载", "未找到有效音频链接")
            return

        # 显示进度条
        progress_bar.pack(pady=(10, 5))
        progress_label.pack()
        progress_bar["value"] = 0
        progress_label.config(text="0%")
        status_label.config(text="🔽 正在下载...", fg=text_color)
        root.update_idletasks()

        filename = f"{sanitize_filename(title)}.mp3"
        r = requests.get(audio_url, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://whyp.it/"}, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        downloaded = 0

        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent = int((downloaded / total_size) * 100)
                    progress_bar["value"] = percent
                    progress_label.config(text=f"{percent}%")
                    root.update_idletasks()

        status_label.config(text="✅ 下载完成", fg=text_color)
    except Exception as e:
        messagebox.showerror("❌ 出错了", str(e))

# 色彩配置
bg_color = "#D6E0E9"
text_color = "#53575A"
button_bg = "#9BC0E2"
button_active = "#87afd2"

# 主窗口
root = tk.Tk()
root.title("Whyp 音频下载器")
root.geometry("520x300")
root.resizable(False, False)
root.configure(bg=bg_color)

# 图标
icon_path = os.path.join(os.path.dirname(__file__), "logo_dark.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# 样式设置
style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry",
    font=("微软雅黑", 11),
    padding=6,
    relief="flat",
    borderwidth=4)
style.configure("Custom.TButton",
    font=("微软雅黑", 12),
    padding=10,
    background=button_bg,
    foreground=text_color,
    borderwidth=0)
style.map("Custom.TButton",
    background=[("active", button_active)],
    foreground=[("active", text_color)])
style.configure("TProgressbar",
    thickness=14,
    troughcolor="#d1d9e0",
    background="#9fbdd4")

# 控件布局
label = tk.Label(root, text="请输入 Whyp 音频链接：", font=("微软雅黑", 13, "bold"), bg=bg_color, fg=text_color)
label.pack(anchor="w", padx=30, pady=(30, 10))

entry = ttk.Entry(root, width=60, style="TEntry", foreground=text_color)
entry.pack(padx=30, pady=(0, 25))

button = ttk.Button(root, text="点击下载", style="Custom.TButton", command=download_whyp)
button.pack(pady=(0, 25))

progress_bar = ttk.Progressbar(root, orient="horizontal", length=420, mode="determinate")
progress_label = tk.Label(root, text="", font=("微软雅黑", 10), fg=text_color, bg=bg_color)

# 初始隐藏进度条和百分比
progress_bar.pack_forget()
progress_label.pack_forget()

status_label = tk.Label(root, text="", font=("微软雅黑", 11), fg=text_color, bg=bg_color)
status_label.pack(pady=(5, 5))

# 启动应用
root.mainloop()
