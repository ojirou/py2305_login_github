import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": []}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="login_github",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("login_github.py", base=base, icon='ojirou.ico')]
)