from pyautotools.tools import *
from pyautotools.tools.helper import *
import win32gui

def hello():
    print('hello')

'''
单击鼠标左键
handle：窗口句柄
position:单击左边，元组类型(x,y)
offset:偏移，元组类型（x,y）
'''
def lClick(handle, position, offset = (0,0)):
    x = int(position[0]) + rands(0,offset[0]) #加上随机偏移
    y = int(position[1]) + rands(0,offset[1]) #加上随机偏移
    mouse.leftClick(handle, (x,y))


'''
拖动鼠标
handle:窗口句柄
start:起始坐标
end:结束坐标
t:拖动时长，根据需求自己定义。建议不低于20。100=1秒
offset:偏移
'''
def dragMouse(handle, start, end, t = 30, offset = (0,0)):
    print(start)
    sx = int(start[0]) + rands(0,offset[0])
    sy = int(start[1]) + rands(0,offset[1])
    ex = int(end[0]) + rands(0,offset[0])
    ey = int(end[1]) + rands(0,offset[1])

    mouse.sliding(handle, (sx,sy), (ex,ey), t)

'''
窗口截图
handle:窗口句柄
width:截屏宽度
height:截屏高度
sleep:截屏间隔
saveimg:是否存储截图文件
'''
def screenShot(handle, sleep=0.5, saveimg=False):

    left,top,right,bottom = 0,0,0,0
    #获取窗口位置
    try:
        left, top, right, bottom = win32gui.GetWindowRect(handle)
    except Exception:
        print('未获取到窗口尺寸')
    #窗口尺寸
    width = right - left
    height = bottom - top
    return screen.screenshot(handle,width,height,sleep,saveimg)


'''
区域截图
handle:窗口句柄
width:截屏宽度
height:截屏高度
sleep:截屏间隔
saveimg:是否存储截图文件
'''
def areaShot(handle, width, height, sleep=0.5, saveimg=False):
    
    return screen.screenshot(handle,width,height,sleep,saveimg)


'''
查找图片坐标
sourceImage:原图像
searchImage:要查找的图片
confidence:查找阈值
'''
def locate(sourceImage, searchImage, confidence = 0.9):

    return screen.locateImage(sourceImage, searchImage, confidence, False)


'''
查找图片全部坐标
sourceImage:原图像
searchImage:要查找的图片
confidence:查找阈值
maxcon:匹配相同目标数量
'''
def locateAll(sourceImage, searchImage, confidence = 0.9, maxcon = 10):

    return screen.locateImage(sourceImage, searchImage, confidence, True, maxcon)

'''
截屏并查找图片坐标
sourceImage:原图像
searchImage:要查找的图片
confidence:查找阈值
'''
def locateAndSort(handle,searchImage,confidence = 0.9,sleep=0.5):
    
    sourceImage = screenShot(handle,sleep)
    return screen.locateImage(sourceImage, searchImage, confidence, False)

'''
截屏并查找图片全部坐标
sourceImage:原图像
searchImage:要查找的图片
confidence:查找阈值
maxcon:匹配相同目标数量
'''
def locateAndSortAll(handle,searchImage,confidence = 0.9,maxcon = 10,sleep=0.5):
    
    sourceImage = screenShot(handle,sleep)
    return screen.locateImage(sourceImage, searchImage, confidence, True,maxcon)