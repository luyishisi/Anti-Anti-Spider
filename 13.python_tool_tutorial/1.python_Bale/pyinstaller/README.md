

# PyInstaller – 将 Python 程序转换成独立的执行文件（跨平台）。

https://github.com/pyinstaller/pyinstaller

# 安装：
A：pip install pyinstaller
b：https://pypi.org/project/PyInstaller/#files 下载源码，进入目录后 python setup.py install

# 用法：
pyinstaller /path/to/yourscript.py

# 注意：
操作系统不互通，linux下打包的只能再linux下运行，windows下打包只能再windows下运行
生成的可执行文件再dist目录下，可执行文件的名字与py文件名一致

该命令会在同目录下生成这样文件结构：其中requests_baidu.py 是我原始脚本命令 dist/requests_baidu是生成的可执行文件，需要保持文件结构才能正常运行


.

├── baidu.html

├── build

│   └── requests_baidu

│       ├── base_library.zip

│       ├── localpycos

│       │   └── struct.pyo

│       ├── out00-Analysis.toc

│       ├── out00-COLLECT.toc

│       ├── out00-EXE.toc

│       ├── out00-PKG.pkg

│       ├── out00-PKG.toc

│       ├── out00-PYZ.pyz

│       ├── out00-PYZ.toc

│       ├── requests_baidu

│       ├── warnrequests_baidu.txt

│       └── xref-requests_baidu.html

├── dist

│   └── requests_baidu

│       ├── baidu.html

│       ├── base_library.zip

│       ├── _bz2.so

│       ├── _codecs_cn.so

│       ├── _codecs_hk.so

│       ├── _codecs_iso2022.so

│       ├── _codecs_jp.so

│       ├── _codecs_kr.so

│       ├── _codecs_tw.so

│       ├── _ctypes.so

│       ├── _hashlib.so

│       ├── _json.so

│       ├── libbz2.so.1.0

│       ├── libcrypto.so.1.0.0

│       ├── libexpat.so.1

│       ├── liblzma.so.5

│       ├── libpython3.5m.so.1.0

│       ├── libreadline.so.6

│       ├── libssl.so.1.0.0

│       ├── libtinfo.so.5

│       ├── libz.so.1

│       ├── _lzma.so

│       ├── _multibytecodec.so

│       ├── _opcode.so

│       ├── readline.so

│       ├── requests_baidu

│       ├── resource.so

│       ├── _ssl.so

│       └── termios.so

├── __pycache__

│   └── requests_baidu.cpython-35.pyc

├── requests_baidu.py

├── requests_baidu.spec

└── test.zip

6 directories, 46 files
