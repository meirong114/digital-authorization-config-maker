# setup.py
import sys
import os
from cx_Freeze import setup, Executable

# 基础设置
build_exe_options = {
    "packages": [
        "tkinter", 
        "requests"
    ],
    "includes": [],
    "include_files": [
        ("app.ico", "app.ico"),
        ("app.png", "app.png"),
        ("7za.exe", "7za.exe"),
        ("sevenzip", "sevenzip"),
        ("configs", "configs")
    ],
    "excludes": [],
    "optimize": 2,
}

# 平台特定设置
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # 无控制台窗口

# 主程序配置
executables = [
    Executable(
        "dacm.py",
        base=base,
        target_name="DataCreator.exe",
        uac_admin=True,  # 请求管理员权限
        icon="app.ico" if os.path.exists("app.ico") else None,
    )
]

setup(
    name="A Data Creator",
    version="1.0.0",
    description="明日方舟电子通行证干员数据生成器",
    options={"build_exe": build_exe_options},
    executables=executables
)
