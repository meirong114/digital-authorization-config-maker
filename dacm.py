import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Scale
import subprocess
import os
import webbrowser

def compress_files(output_filename, files):
    # 调用7za.exe进行压缩
    subprocess.run(['7za', 'a', f'-tzip', output_filename] + files, check=True)
    subprocess.run(["./7-Zip/7zFM.exe", output_filename])

def generate_introduction():
    # 打开介绍生成器
    intro_window = tk.Toplevel(root)
    intro_window.title("明日方舟电子通行证干员数据生成器")

    tk.Label(intro_window, text="名称:").grid(row=0, column=0)
    name_entry = tk.Entry(intro_window)
    name_entry.grid(row=0, column=1)

    tk.Label(intro_window, text="性别:").grid(row=1, column=0)
    gender_var = tk.StringVar(value="女")
    tk.Radiobutton(intro_window, text="女", variable=gender_var, value="女").grid(row=1, column=1)
    tk.Radiobutton(intro_window, text="男", variable=gender_var, value="男").grid(row=1, column=2)

    tk.Label(intro_window, text="阵营:").grid(row=2, column=0)
    faction_entry = tk.Entry(intro_window)
    faction_entry.grid(row=2, column=1)

    tk.Label(intro_window, text="职业:").grid(row=3, column=0)
    job_entry = tk.Entry(intro_window)
    job_entry.grid(row=3, column=1)

    def save_introduction():
        with open("介绍.txt", "w") as f:
            f.write(f"[名称]{name_entry.get()}\n[性别]{gender_var.get()}\n[阵营]{faction_entry.get()}\n[职业]{job_entry.get()}")
        intro_window.destroy()

    tk.Button(intro_window, text="保存", command=save_introduction).grid(row=4, column=1)

def fill_information():
    # 打开信息填写
    info_window = tk.Toplevel(root)
    info_window.title("信息填写")

    tk.Label(info_window, text="角色名称:").grid(row=0, column=0)
    char_name_entry = tk.Entry(info_window)
    char_name_entry.grid(row=0, column=1)

    tk.Label(info_window, text="星级:").grid(row=1, column=0)
    star_scale = Scale(info_window, from_=1, to=6, orient=tk.HORIZONTAL)
    star_scale.grid(row=1, column=1)
    star_scale.set(6)  # 默认星级

    def save_info():
        with open("信息.txt", "w") as f:
            f.write(f"{char_name_entry.get()}\n{int(star_scale.get())}")
        info_window.destroy()

    tk.Button(info_window, text="保存", command=save_info).grid(row=2, column=1)

def select_career_image():
    # 选择职业图片
    filename = filedialog.askopenfilename(filetypes=[("PNG 图片文档", "*.png")])
    if filename:
        with open("职业.png", "wb") as f:
            f.write(open(filename, "rb").read())

def select_main_video():
    # 选择主视频MP4格式
    filename = filedialog.askopenfilename(filetypes=[("MP4 视频档案", "*.mp4")])
    if filename:
        with open("char.mp4", "wb") as f:
            f.write(open(filename, "rb").read())

def start_generating():
    # 开始生成
    output_filename = "config.usr"
    files = ["char.mp4", "介绍.txt", "信息.txt", "职业.png"]
    compress_files(output_filename, files)
    messagebox.showinfo("成功", "配置文件已生成")

def open_github(self):
    # 打开GitHub
    webbrowser.open("https://github.com/meirong114/digital-authorization-config-maker")

def open_baiyin(event=None):
    webbrowser.open("https://live.bilibili.com/1716534530")

def open_prts(self):
    webbrowser.open("https://prts.wiki")

# 创建主窗口
root = tk.Tk()
root.title("明日方舟电子通行证干员数据生成器")
root.iconphoto(True, tk.PhotoImage(file="app.png"))
root.geometry("500x300")

# 创建按钮
tk.Button(root, text="打开介绍生成器", command=generate_introduction).grid(row=0, column=0, padx=10, pady=5)
tk.Button(root, text="打开信息填写", command=fill_information).grid(row=1, column=0, padx=10, pady=5)
tk.Button(root, text="选择职业图片", command=select_career_image).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="选择主视频MP4格式", command=select_main_video).grid(row=3, column=0, padx=10, pady=5)
generate_button = tk.Button(root, text="开始生成", command=start_generating)
generate_button.grid(row=4, column=0, padx=10, pady=5)

# 创建快捷键
root.bind('<Control-s>', lambda event: start_generating())

# 创建左下角文字
github_label = tk.Label(root, text="点按打开Github", fg="red", cursor="hand2")
github_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
github_label.bind("<Button-1>", open_github)

baiyin_label = tk.Label(root, text="友情链接：白银今天下班了吗", fg="green", cursor="hand2")
baiyin_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)
baiyin_label.bind("<Button-1>", open_baiyin)

prts_label = tk.Label(root, text="干员差分下载：PRTS", fg="black", cursor="hand2")
prts_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)
prts_label.bind("<Button-1>", open_prts)

# 运行主循环
root.mainloop()
