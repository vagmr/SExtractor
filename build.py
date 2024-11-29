import PyInstaller.__main__
import os
import shutil
from datetime import datetime


def clean_dist():
    """清理dist目录"""
    if os.path.exists("dist"):
        shutil.rmtree("dist")


def build():
    """使用PyInstaller构建程序"""
    PyInstaller.__main__.run(
        [
            "run.py",
            "--name=CyberExtract",
            "--icon=logo.ico",
            "--noconsole",
            "--noconfirm",
            "--clean",
            # 添加所需的数据文件和路径
            "--add-data=main/locale;main/locale",
            "--add-data=src;src",  # 添加src目录
            "--add-data=main;main",  # 添加main目录
            "--add-data=libs;libs",  # 添加libs目录
            # 添加必要的隐式导入
            "--hidden-import=main.mainWindow",
            "--hidden-import=main.ui_mainWindow",
            "--hidden-import=main.configManager",
            "--hidden-import=main.batchManager",
            "--hidden-import=main.statusBar",
            "--hidden-import=src.main_extract_txt",
            "--hidden-import=src.main_extract_bin",
            "--hidden-import=src.main_extract_json",
            "--hidden-import=src.main_extract",
            "--hidden-import=src.merge_json",
            "--hidden-import=src.common",
            "--hidden-import=src.extract_Cyberworks",
            # 如果有其他需要打包的数据文件，在这里添加
        ]
    )


def create_version_file(version):
    """创建版本信息文件"""
    with open("dist/CyberExtract/version.txt", "w", encoding="utf-8") as f:
        f.write(f"Version: {version}\n")
        f.write(f'Build Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


if __name__ == "__main__":
    import sys

    version = sys.argv[1] if len(sys.argv) > 1 else "unknown"

    clean_dist()
    build()
    create_version_file(version)
