# 自动更换在线壁纸

适用于 windows 的在线壁纸自动更换 python 脚本

## 安装方法

确保你电脑已经有 python 环境  
输入以下命令安装依赖

``` cmd
pip install pywin32 requests
```

如果在中国大陆且网络环境不佳，可以尝试使用清华大学镜像站进行安装

``` cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pywin32 requests
```

在运行脚本前需要打开文件更换图片文件的保存位置，默认位置为个人图片库目录  
该位置通常为`C:\Users\用户名\Pictures\`

更改完毕后即可开始运行脚本

``` cmd
python mian.py
```

或使用任务计划程序定时运行  
详细配置教程可以参考网上的文章[点此查看](https://www.cnblogs.com/funnyzpc/p/11746439.html)

> 可以自行打开文件更换接口和运行模式等  

## 兼容性声明

仅测试 win10 python311 环境可用  
为 win7 及更低版本准备了兼容模式，但不保证可用，需要自行测试

>如果有标准模式和兼容模式都无法运行的情况的请带上系统及 python 环境提 issues
