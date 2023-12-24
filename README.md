# IPTV_analysis

#### 介绍
把开源搜集到的 IPTV 源文件，或许有效的链接，并转成群晖 IPTV 管理系统能直接识别的频道，输出到新的 M3U 文件中。

#### 软件架构
该软件使用 Python 3 环境运行，个人版本 Python 3.11.4，如运行有问题请参考相关版本的变化。


#### 安装教程

1.  安装 Python 3.11 运行环境。
2.  代码运行需要 `requests` 、`random` 、`time` 、`re`，因此在运行之前，应该执行 `pip` 命进行库的安装:```pip install requests```。

#### 使用说明

1.  在代码存放的当前目录，准备好原始 `ipty.py` 文件，以及原始的 `M3U` 文件。
2.  直接运行即可：``` python ipty.py ```。
3.  如果程序运行长时间不再执行，请直接关闭并收集当前目录下，新生产的 `M3U` 文件即可。

#### 参与贡献

1.  无


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
