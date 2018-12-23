import win32gui, win32con, win32ui
import time
import aircv as ac
import numpy
from PIL import Image
from pyautotools.tools.helper import *


#屏幕截图
def screenshot(handle, width, height, sleep=0.2, saveimg=False):
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    # print('屏幕截图')
    time.sleep(sleep)
    try:
        hwndDC = win32gui.GetWindowDC(handle)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        # saveDC，将截图保存到saveBitmap中
        oldMap = saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（width，height）的图片
        saveDC.BitBlt((-7, -30), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
    
        if saveimg:
            t = time.time()
            # print('截图')
            saveBitMap.SaveBitmapFile(saveDC, "screen/%s.bmp" % t)
        #获取图像信息
        bmpinfo = saveBitMap.GetInfo() 
        #获取图片数据结构
        bmpstr = saveBitMap.GetBitmapBits(True)
        #转换成BGR数据格式，供CV2使用
        pil_im = Image.frombuffer('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr,'raw','BGRX',0,1)
        #转换成numpy格式数组,因为CV2只能读取numpy格式数据
        pil_array = numpy.array(pil_im)
        #最终截图数据
        # cv_im = cv2.cvtColor(pil_array, cv2.COLOR_RGB2BGR)
        #释放bitmap and DC
        saveDC.SelectObject(oldMap)
        mfcDC.DeleteDC()
        saveDC.DeleteDC()
        win32gui.ReleaseDC(handle, hwndDC)
        win32gui.DeleteObject(saveBitMap.GetHandle())
        #返回截图数据
        return pil_array
    except Exception:
        pass

'''
匹配图片
suorceImage:原图像
searchImage:要查找的图片
confidence:查找阈值
all:是否匹配所有相同目标
maxcon:匹配相同目标数量
'''

def locateImage(suorceImage, searchImage, confidence, isAll = False, maxcon = 10):
    searchImage = ac.imread(searchImage)
    if isAll:
        result = ac.find_all_template(suorceImage, searchImage, confidence, maxcon)        
        if result:
            positionList = []
            for r in result:
                positionList.append(r['result'])
            return positionList
        else:
            return None
    else:
        result = ac.find_template(suorceImage, searchImage, confidence)
        if result:
            return result['result']
        else:
            return None
    
