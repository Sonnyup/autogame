import win32gui
import win32api
import win32con
import time
from pyautotools.tools.helper import *

'''
鼠标动作类
'''
#单击鼠标左键
def leftClick(handle, position):
    time.sleep(0.1)
    x = int(position[0])
    y = int(position[1])
    # print(x,y)
    tmp = win32api.MAKELONG(x, y)#鼠标坐标
    # tem = win32api.MAKELONG(350,250)
    win32gui.PostMessage(handle, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
    win32api.PostMessage(handle,win32con.WM_MOUSEMOVE,0 ,tmp)
    time.sleep(0.1)
    win32api.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    time.sleep(0.1)
    win32api.PostMessage(handle,win32con.WM_MOUSEMOVE,0 ,tmp)
    time.sleep(0.1)
    win32api.PostMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
    #debugPrint(a, b, c)
    #debugPrint('结束')

#滑动  t:时间 100 = 1秒
def sliding(handle, start, end, t):
    sx, sy, ex, ey = int(start[0]), int(start[1]), int(end[0]), int(end[1])
    time.sleep(0.1)
    pos1 = win32api.MAKELONG(sx,sy)#鼠标坐标 - 起始位置
    pos2 = win32api.MAKELONG(ex,ey)#鼠标坐标 - 结束位置
    win32gui.PostMessage(handle, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
    #光标移动到初始位置
    win32api.PostMessage(handle,win32con.WM_MOUSEMOVE,0 ,pos1)
    time.sleep(0.2)
    #按下鼠标左键
    win32api.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos1)
    time.sleep(0.2)

    tempx, tempy = sx, sy
    x, y = 0, 0
    for i in range(t):
        # print("tx:%d,ty:%d" % (tempx,tempy))
        # print("x:%d,y:%d" % (x,y))
        time.sleep(0.01)           
        if sx > ex:                
            x = tempx = tempx - ((sx - ex) / t)
        elif sx < ex:
            x = tempx = tempx + ((ex - sx) / t)

        if sy > ey:
            y = tempy = tempy - ((sy - ey) / t)
        elif sy < ey:
            y = tempy = tempy + ((ey - sy) / t)
        pos2 = win32api.MAKELONG(int(x), int(y))
        #光标移动到结束位置
        win32api.PostMessage(handle,win32con.WM_MOUSEMOVE,0 ,pos2)

    time.sleep(0.2)
    #抬起鼠标左键
    win32api.PostMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, pos2)
    
