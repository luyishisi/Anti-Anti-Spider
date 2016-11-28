测试项目

功能:

使用crontab每天定时启动

定时语句要主要得开启可视化界面:
这样每分钟运行一次,用于测试效果,之后修改定时即可,
 */1 * * * * export DISPLAY=:0; python ~/selenium_so.py >> log1.txt


自动化登录http://stackoverflow.com/


注册了一个小号来测试是否能用于刷帐号的每天持续登录银牌.

每次启动都会在同一目录下生成一个以时间命名的截图和时间命名的html文件




 
