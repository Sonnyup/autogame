from fun import *
import time
from setting import *



def duizhang():
    fScreenShot(0.7) #截图
    _publicFun()#调用共用函数
    dianPos = fLocate(dianBtn)
    if dianPos:
        fLeftClick(dianPos,(10,8))
    
    dian2Pos = fLocate(dian2Btn)
    if dian2Pos:
        fLeftClick(dian2Pos,(10,8))

    dian3Pos = fLocate(dian3Btn)
    if dian3Pos:
        fLeftClick(dian3Pos,(10,8))

    tsfPos = fLocate(tsFlag)
    if tsfPos:
        tsPos = fLocate(tsBtn)
        if tsPos:
            fLeftClick(tsPos ,(10,8))
    else:
        chachaPos = fLocate(chachaBtn)
        if chachaPos:
            # pass
            fLeftClick(chachaPos,(10,8))
    
    kuaijinPos = fLocate(kuaijinBtn)
    if kuaijinPos:
        fLeftClick(kuaijinPos,(10,8))
    
    renyiPos = fLocate(renyiBtn)
    if renyiPos:
        fLeftClick(renyiPos,(10,8))
    
    tiaoguoPos = fLocate(tiaoguoBtn)
    if tiaoguoPos:
        fLeftClick(tiaoguoPos,(10,8))
        
    yanPos = fLocate(yanBtn)
    if yanPos:
        fLeftClick(yanPos,(10,8))
    
    bossPos = fLocate(bossBtn)
    if bossPos:
        fLeftClick(bossPos,(10,8))
    else :
        daoPos = fLocate(daoBtn)
        if daoPos:
            fLeftClick(daoPos,(10,8))
        daoPos2 = fLocate(daoBtn2)
        if daoPos2:
            fLeftClick(daoPos2,(10,8))
    
    wenhaoPos = fLocate(wenhaoBtn)
    if wenhaoPos:
        fLeftClick(wenhaoPos,(10,8))
    
    beijingPos = fLocate(beijingBtn)
    if beijingPos:
        fLeftClick(beijingPos,(10,8))

    lipinPos = fLocate(lipinBtn)
    if lipinPos:
        fLeftClick(lipinPos,(10,8))
    
    hdjlPos = fLocate(hdjlBtn)
    if hdjlPos:
        fLeftClick((800 , 320) ,(100 ,100))

    fxPos = fLocate(fxFlag,0.7)
    if fxPos:
        fLeftClick((800 , 320) ,(100 ,100))
    
    
    

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
        for i in range(4):                
            time.sleep(0.5)
            fLeftClick((800 , 320) ,(100 ,100))

    shibaiPos = fLocate(shibaiFlag)#失败标识
    if shibaiPos:
        time.sleep(1)
        fLeftClick((800 , 320) ,(100 ,100))

    fudanPos = fLocate(fudanFlag)#福蛋标识
    if fudanPos:
        # time.sleep(1)
        print('点击福蛋')
        fLeftClick((800 , 320) ,(100 ,100))

while 1:
    try:
        duizhang()
    except Exception:
        pass
    
# fScreenShot(0.7,True) #截图