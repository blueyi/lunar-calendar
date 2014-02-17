关于
===
lunar-calendar 可以在linux下显示中国传统的农历.

已编译好的deb包, 可以在这里获取 https://github.com/LiuLang/lunar-calendar-packages


依赖包
=====

* python3-gi gtk3的python3绑定


手动安装
=======
请根据你的发行版, 先安装上面列出的依赖包

* 安装: `# pip3 install lunar-calendar`
* 升级: `# pip3 install upgrade lunar-calendar`

自定义节日
=========
lunar-calendar 可以很方便的加入新的节日, 或者修改默认的节日.

打开 ~/.config/lunar-calendar/holidays.ini 按照里面的说明进行编辑, 保存后,
重新启动lunar-calendear程序, 就可以使用你刚才编辑好的节日了.

截屏
====
<img src="screenshots/lunar-calendar.png?raw=true" title="Lunar Calendar" />


版权
====
依赖GPLv3通用许可协议发布
