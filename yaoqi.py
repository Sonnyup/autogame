from fun import *
import time
from setting import *


# zuduiBtn = 'image/yaoqi/zudui.bmp'
# yqfyBtn = 'image/yaoqi/yqfy.bmp' #妖气封印按钮
# yqfyTip = 'image/yaoqi/yqfy2.bmp'
# rhfBtn = 'image/yaoqi/rhf.bmp'
# yqfyrhfTip = 'image/yaoqi/yqfyrhf.bmp'
# zdppBtn= 'image/yaoqi/zdpp.bmp' #自动匹配

def start():        
    fScreenShot(0.5) #截图
    zuduiPos = fLocate(zuduiBtn) #组队按钮
    yqfyBtnPos = fLocate(yqfyBtn) #妖气封印按钮
    yqfyTipPos = fLocate(yqfyTip) #妖气封印标识

    yqPos = fLocate(yqBtnImg) #日和坊按钮
    yqTipPos = fLocate(yqTipImg) #妖气日和坊标记

    zdppPos = fLocate(zdppBtn) #自动匹配
    readyPos = fLocate(readyBtn,0.95)#准备按钮
    chaPos = fLocate(chaBtn) #自动匹配
    fightPos = fLocate(fightBtn)#开始战斗按钮
    shuaxinPos = fLocate(sxBtn)#刷新按钮
    jiaruPos = fLocate(jrBtn) #加入按钮

    if zuduiPos:
        fLeftClick(zuduiPos,(2,3))#组队按钮
    
    if chaPos:
        fLeftClick(chaPos,(2,3)) #拒绝协作

    if fightPos:
        fLeftClick(fightPos,(2,3))#开始战斗

    if readyPos:
        fLeftClick(readyPos,(10,10))#准备
        print("点击准备")

    if yqfyBtnPos:#妖气封印
        if yqfyTipPos:#选中标识
            if yqPos:#妖气副本
                if yqTipPos:#选中目标标识
                    pass
                else:
                    fLeftClick(yqPos)
            else:
                fDragMouse((360,400),(350,200),(10,10),25)#滑动
        else:
            fLeftClick(yqfyBtnPos,(3,3))

    if zdppPos:
        fLeftClick(zdppPos,(2,3))

    # if yqTipPos:
    #     if jiaruPos:
    #         fLeftClick(jiaruPos,(10,10))#加入
    #         print("点击加入组队")

    #     if shuaxinPos:
    #         # time.sleep(0.2)
    #         fLeftClick(shuaxinPos,(3,5))

    _publicFun()#调用共用函数

#共用功能
def _publicFun():
    readyPos = fLocate(readyBtn,0.95)#准备按钮
    if readyPos:
        fLeftClick(readyPos,(10,10))
        print("点击准备")

    dAcceptPos = fLocate(dAcceptBtn)#拒绝任何协作
    if dAcceptPos:
        fLeftClick((630,420),(10,8))#拒绝任何协作

    winPos = fLocate(winFlag,0.9)#胜利标识        
    if winPos:
        print("战斗胜利")
        for i in range(4):                
            time.sleep(0.5)
            fLeftClick((800 , 320) ,(100 ,100))

    shibaiPos = fLocate(shibaiFlag)#失败标识
    if shibaiPos:      
        print("战斗失败")       
        time.sleep(1)
        fLeftClick((800 , 320) ,(100 ,100))

    fudanPos = fLocate(fudanFlag)#福蛋标识
    if fudanPos:
        # time.sleep(1)
        print('点击福蛋')
        fLeftClick((800 , 320) ,(100 ,100))

# fScreenShot(0.7,True) #截图
while 1:
    try:
        start()
    except:
        pass