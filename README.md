# 一键自动化解除一加7T&amp;7TPro强制加密data

其实没什么可说的，整个程序很鸡肋，我人也很菜，就简单介绍一下几个目录和文件的作用吧。

flash\img文件夹：里面存放了所有的img镜像文件，刷入系统的时候用的(解包生成的文件会移动到这里)

flash\platform文件夹：adb和fastboot工具，用于刷入系统。

flash\flash-all.bat文件:工具如果遇到刷入失败情况，可以手动打开备用脚本刷入

tools\python文件夹：里面存放了python环境(考虑到部分用户电脑没有python环境，就直接给它放进来了，看我菜吧)

tools\drive文件夹：存放了一加手机的驱动文件，防止用户没有驱动，刷不进去。

tools文件夹其他文件：一些解包打包img镜像的源码(别人开源的)，解包payload.bin文件的源码，7z解压工具

auto.py：这个是软件的核心（也就是这一小段是我自己写的，菜），不多赘述。

运行过程还会生成temp文件夹，就是放临时文件的地方，自己看源码。
