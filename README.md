# 自动更换在线壁纸

适用于 windows 的在线壁纸自动更换 python 脚本

本脚本会自动获取图片接口的图片并去重后保存自本地  
如果不想在本地保存一堆图片可自行更改图片的文件名，当文件名重复时将会覆盖旧图片  
由于 windows 的限制，必须将图片保存到硬盘上后才能设置壁纸，无法做到0写入

## 安装方法

确保你电脑已经有 python 环境，如没有请前往 [python官网](https://www.python.org/downloads/) 下载安装  
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

### 升级说明

从旧版升级时需要查看

<details>
  <summary>点击展开</summary>

由于新版本判断重复的逻辑变更  
如果你之前有在使用[此版本](https://github.com/xiaotian2333/Auto-wallpaper-change/commit/79249a5ac6c2c33874844e158afc25597d723f9a)及更久之前的版本，那么升级时务必先查看下方的升级步骤  
否则将可能产生一张重复的图片

1. 下载`md5.py` [点此下载](https://github.com/xiaotian2333/Auto-wallpaper-change/blob/main/md5.py)  
2. 下载完毕后将`md5.py`放置在图片目录内
3. 运行`md5.py`，当输出`数据已成功写入JSON文件`时说明运行完毕  
4. 现在可以删除`md5.py`了

</details>

## 兼容性声明

仅测试 `win10-python311` 环境可用  
为 win7 及更低版本准备了兼容模式，但不保证可用，需要自行测试

>如果有标准模式和兼容模式都无法运行的情况的请带上系统及 python 环境提 issues
