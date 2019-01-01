from fun import *
import time
from setting import *

pullNum = 1 #拖动次数
boss = False
fireNum = 0 #战斗次数

#查找经验怪并开始战斗
def findexp():
    global boss #boss标识
    global fireNum
    
    fScreenShot(0.5)
    # time.sleep(0.1)

    #经验怪标识
    
    for e in exp: 
        expPos = fLocate(e,0.8)
        if expPos:
            # print(e)
            break
    bossPos = fLocate(bossBtn,0.8) #boss
    if bossPos:
        print("与BOSS战斗")
        fLeftClick(bossPos,(5,5))
        boss = True
        return True
    
    if expPos:
        daoPos = fLocateAll(daoBtn,0.8)#战斗图标
        print(daoPos)
        expX = expPos[0]
        if daoPos != None:
            sortList = {} #排序所与需要的字典
            for pos in daoPos:
                diff = expX - pos[0] #计算差值
                if diff != 0:
                    if diff < 0:
                        diff = diff * (-1) #如果为负数，转化为正数
                vl = (pos[0],pos[1],diff)#组装元组
                sortList[diff] = vl
            sortListRes = sorted(sortList.items(), key=lambda asd:asd[0])
            # print(sortListRes[0][1])
            if sortListRes[0][1][2] < 100: #限定左右距离100像素点
                fLeftClick((sortListRes[0][1][0],sortListRes[0][1][1]),(10,8))
                fireNum += 1
                print("找到怪物，开始战斗")
                print("战斗次数：%d" % fireNum)
                
            else:
                print('超出限定距离')
                return False 
            return True
        else:
            return False

def danshua():
    global pullNum #拖动界面次数
    global boss #boss标识
    fScreenShot(0.5)
    winPos = fLocate(tswin)
    if winPos:
        print("战斗胜利")
        for i in range(2):                
            time.sleep(0.2)
            fLeftClick((800 , 320),(100 ,100))

    fuPos = fLocate(tsfu)
    if fuPos:
        time.sleep(1.5)
        fLeftClick((800 , 320),(100 ,100))
        print("点击福蛋")
        if boss:
            time.sleep(4)

    lipinPos = fLocate(lipinFlag)
    if lipinPos:
        print("检测到小纸人礼盒")        
        while lipinPos:
            time.sleep(0.2)            
            print("领取小纸人礼盒")
            fLeftClick(lipinPos,(5,5))
            time.sleep(1)
            fLeftClick((800 , 320),(100 ,50))
            time.sleep(0.2)
            fScreenShot(0.5)
            lipinPos = fLocate(lipinFlag)
        boss = False
        pullNum = 7
        return True

    towSixPos = fLocate(towSixFlag)
    if towSixPos:
        fLeftClick(towSixPos,(10,10))

    tsPos = fLocate(tsBtn)
    if tsPos:
        boss = False
        pullNum = 1
        fLeftClick(tsPos,(10,10))

    yaoPos = fLocate(yaoFlag)
    if yaoPos:
        boss = False
        pullNum = 1

    fbPos = fLocate(fbjmFlag)
    if fbPos and pullNum < 5:
        print("进入副本界面")
        # time.sleep(1)    
        for j in range(2):
            print("查找怪物 %d 次"%(j+1))
            if findexp():
                return True

        fDragMouse((900,300),(50,300),(100,50),25)#探索副本界面滑动
        print("拖动%d次" % pullNum)
        pullNum += 1
    else:
        if fbPos:
            qrPos = fLocate(qrBtn)
            if qrPos:
                fLeftClick(qrPos,(10,6))
                pullNum = 1 #拖动界面次数
                print("确认退出")
            fanhuiPos = fLocate(fanhuiBtn)
            if fanhuiPos:
                fLeftClick(fanhuiPos,(10,6))
                print("退出副本")
                return True
                    
    zbjmPos = fLocate(zbjmFlag)
    if zbjmPos:
        manPos1 = fLocateAll(manFlag,0.8)
        if manPos1 != None:
            if len(manPos1) > 1:
                print("进入换狗粮界面")
                fLeftClick((130,330),(60,60))
                time.sleep(1.5)
                #x:120-330 y:320-460
            else:
                fLeftClick((830,370),(60,60))
                print("准备页面-点击准备")

    fScreenShot(0.5)
    allPos = fLocate(allFlag)
    if allPos:
        fLeftClick(allPos,(5,5))
        time.sleep(0.2)
        fScreenShot(0.5)
        nPos = fLocate(nFlag)
        if nPos:
            fLeftClick(nPos,(1,1))
            time.sleep(0.3)
            findman()#换狗粮

def findman():
    fScreenShot(0.5,True)
    manPos = fLocateAll(manFlag,0.8)
    if manPos :
        if len(manPos) > 1:
            print("开始换狗粮")
            print(len(manPos))
            for pos in manPos:
                if pos[0] < 560:#过滤掉输出位置
                    glPos = findGouliang()
                    fDragMouse(glPos,pos,(20,30),25)
            time.sleep(1.5)
            fLeftClick((830,370),(60,60))
            print("狗粮页面-点击准备1")
        else:
            fLeftClick((830,370),(60,60))
            print("狗粮页面-点击准备2")

def findGouliang():
    fScreenShot(0.5)
    djPos = fLocateAll(dengjiFlag,0.7)
    if djPos and len(djPos) >= 2:
        djx = djPos[1][0] + 15
        djy = djPos[1][1] + 20
        return djx,djy
    else:
        fDragMouse((600,410),(300,410),(30,20),25)#拖动选卡页面
        
        return findGouliang()

#队员
def duiyuan():
    fScreenShot(0.5) #截图
    _publicFun()#调用共用函数

    yaoqingPos = fLocate(yaoqingTip)
    #接受邀请
    if yaoqingPos:
        fLeftClick((int(yaoqingPos[0])+10,int(yaoqingPos[1])+8))
        print("接受邀请")

    dengPos = fLocate(dengFlag)
    bqPos = fLocate(bqFlag)
    if dengPos:
        if bqPos:
            pass
        else:
            fanhuiPos = fLocate(fanhuiBtn)
            if fanhuiPos:
                fLeftClick(fanhuiPos,(10,8))
                print("点击退出")
                for i in range(2):                    
                    fScreenShot(0.5)
                    qrPos = fLocate(qrBtn)
                    if qrPos:
                        fLeftClick(qrPos,(10,8))
                        print("确认退出")

#共用功能
def _publicFun():
    # readyPos = fLocate(readyBtn,0.95)#准备按钮
    # if readyPos:
    #     fLeftClick(readyPos,(10,10))
    #     print("点击准备")

    dAcceptPos = fLocate(dAcceptBtn)#拒绝任何协作
    if dAcceptPos:
        fLeftClick((630,420),(10,8))#拒绝任何协作

    winPos = fLocate(winFlag,0.9)#胜利标识        
    if winPos:
        # win = win + 1
        # print("战斗胜利次数：%d" % win)
        for i in range(2):                
            time.sleep(0.2)
            fLeftClick((800 , 320) ,(100 ,100))

    shibaiPos = fLocate(shibaiFlag)#失败标识
    if shibaiPos:      
        # fair = fair + 1
        # print("战斗失败次数：%d" % fair)       
        time.sleep(1)
        fLeftClick((800 , 320) ,(100 ,100))

    fudanPos = fLocate(fudanFlag)#福蛋标识
    if fudanPos:
        # time.sleep(1)
        print('点击福蛋')
        fLeftClick((800 , 320) ,(100 ,100))
        
# while True:
#     try:
#         start()
#     except:
#         pass
    # start()