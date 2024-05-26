import os,win32gui,win32con,win32api,requests,time,io
from PIL import Image
t = time.localtime()

def set_wallpaper(img):
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "10")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面与设置壁纸
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img, win32con.SPIF_SENDWININICHANGE)

def get_img_type(file_path):
    try:
        with Image.open(file_path) as img:
            format = img.format
            if format:
                return "." + format.lower()
            else:
                return os.path.splitext(file_path)[1].lower()
    except IOError:
        return "Unknown"


sys_user_path = os.environ['USERPROFILE']
# 是否开启图片格式转换，开启后将所有图片格式转为jpg
# win7及以下系统可能不支持部分图片格式如webp，开启此选项即可
img_type_convert = False
# 注意路径书写问题
url = "https://t.alcy.cc/ysz/" #在线图片链接
img_path = sys_user_path+"\Pictures\\" #保存的文件夹，注意必须由\\结尾
img_name = "壁纸自动更换缓存"+str(t.tm_year)+"年"+str(t.tm_mon)+"月"+str(t.tm_mday)+"日"+str(t.tm_hour)+"时"+str(t.tm_min)+"分"+str(t.tm_sec)+"秒" #文件名格式，文件后缀会自动添加
# 开始获取图片
img = requests.get(url)
# 假设你已经获取到了一个Response对象，命名为img
# 将Response对象的内容读取到BytesIO对象中
img_stream = io.BytesIO(img.content)

# 正常流程，直接保存原格式
if not img_type_convert:
    # print("进入标准流程")
    # 获取图片的类型
    img_type = get_img_type(img_stream)
    # 保存图片
    open(img_path+img_name+img_type, "wb").write(img.content)
    img_path_finally = img_path+img_name+img_type

#这段用于转换图片格式为jpg，作为兼容选项而保留
if img_type_convert:
    # print("进入兼容流程")
    # 处理图片格式
    im=Image.open(img_stream)
    im.load()
    # 保存图片
    im.save(img_path+img_name+".jpg")
    img_path_finally = img_path+img_name+".jpg"

# 关闭BytesIO对象，释放内存
img_stream.close()

#切换时要检查一下图片是否存在
if os.path.exists(img_path_finally):
    set_wallpaper(img_path_finally)
else:
    print('图片不存在，切换失败')