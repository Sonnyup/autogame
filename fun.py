import pyautotools.autotools as at
import win32gui
import time
from setting import *


#获取游戏窗口列表
def windowList(targetTitle):
    hWndList = []
    winDict = {}
    i = 1
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    for hwnd in hWndList:
        clsname = win32gui.GetClassName(hwnd)
        title = win32gui.GetWindowText(hwnd)
        if (title.find(targetTitle) >= 0):    
            print('%d.句柄：%d，窗口名：%s，类名：%s' % (i,hwnd,title,clsname))
            winDict[i] = (title,hwnd,clsname)
            i +=1
            
    if winDict == {}:
        print('未检测到游戏进程！')
        exit()
    else:
        while True:
            num = input("选择游戏窗口：")
            if num.isdigit():
                num = int(num)
                if num <= len(winDict):
                    print("选择了：%s窗口, 类名：%s" % (winDict[num][0],winDict[num][2]))
                    return winDict[num][1]
                else:
                    print("所选窗口不存在，请重新选择！")
            else:
                print("请输入数字！")
            
print('开启本程序前，请先配置好出战队伍！')
hwnd = windowList('阴阳师') #首次运行程序时加载

image_data = '' #截屏数据
#截图功能封装
def fScreenShot(sleep = 0.5, saveimg = False):
    global image_data
    image_data = at.screenShot(hwnd,sleep,saveimg) #截图
    # print('截图')

#找图功能封装-单个
def fLocate(searchImage,confidence = 0.9):
    global image_data
    return at.locate(image_data,searchImage,confidence) #找图

#找图功能封装-全部
def fLocateAll(searchImage,confidence = 0.9):
    global image_data
    return at.locateAll(image_data,searchImage,confidence) #找图


#点击鼠标左键封装
def fLeftClick(position,offset=(0,0)):
    at.lClick(hwnd,position,offset)

#拖动界面
def fDragMouse(handle, start, end, t = 30, offset = (0,0)):
    at.dragMouse(handle, start, end, t = 30, offset = (0,0))
