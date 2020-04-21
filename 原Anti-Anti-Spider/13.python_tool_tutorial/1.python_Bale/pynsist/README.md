

Pynsist是为Python应用程序构建Windows安装程序的工具。

安装程序将Python本身捆绑在一起，因此可以将应用程序分发给没有安装Python的用户。

首先他需要安装nsis，

windows下可以https://sourceforge.net/projects/nsis/ 直接下载安装
linux下可以sudo apt-get install nsis

再安装：pip install pynsist

样例代码是打包请请求百度首页的简单爬虫代码，

在本目录下执行命令：pynsist installer.cfg

打包完成后在build/nsis下会有个My_App_1.0.exe 文件，别人从window中打开即可自动运行安装命令，自动安装python以及你项目中的依赖包。





具体installer.cfg要怎么配置参看
http://pynsist.readthedocs.io/en/latest/index.html
