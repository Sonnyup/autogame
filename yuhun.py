from fun import *
import time
from setting import *

win = 0
fair = 0
#队长
def duizhang():
    fScreenShot(0.7) #截图
    _publicFun()#调用共用函数
    teamPos = fLocate(teamFlag)#组队界面标识
    if teamPos:
        # print('zuduijiemian')
        # print(peopleNum)
        fightPos = fLocate(fightBtn)#开始战斗按钮
        invitePos = fLocateAll(inviteBtn) #邀请按钮--查找全部
        if peopleNum == 2:  #2人开队
            if len(invitePos) == 1:
                fLeftClick(fightPos,(13,8))
                print("2人开始战斗")
        elif peopleNum == 3:
            if invitePos == None:
                fLeftClick(fightPos,(13,8))
                print("3人开始战斗")

    autoPos = fLocate(autoFlag)#自动邀请
    # print(autoPos)    
    if autoPos:
        fLeftClick(autoPos,(5,5))
        print('勾选邀请')

    confirmPos = fLocate(autoConfirm)#默认自动邀请
    if confirmPos:
        fLeftClick(confirmPos ,(5 ,5))
        print('勾选邀请点击确定')

#队员
def duiyuan():

    fScreenShot(0.7) #截图
    autoAcceptPos = fLocate(autoAcceptBtn)#自动接受组队邀请
    if autoAcceptPos:
        fLeftClick(autoAcceptPos , (10, 8))#接受组队邀请
        print("接受自动邀请")
    
    invitePos = fLocate(inviteMsg)#组队邀请    
    if invitePos:
        fLeftClick(invitePos, (10, 8))#接受组队邀请
        print("接受邀请")
    _publicFun()#调用共用函数

#共用功能
def _publicFun():
    global win
    global fair
    readyPos = fLocate(readyBtn,0.95)#准备按钮
    if readyPos:
        fLeftClick(readyPos,(10,10))
        print("点击准备")

    dAcceptPos = fLocate(dAcceptBtn)#拒绝任何协作
    if dAcceptPos:
        fLeftClick((630,420),(10,8))#拒绝任何协作

    winPos = fLocate(winFlag,0.9)#胜利标识        
    if winPos:
        win = win + 1
        print("战斗胜利次数：%d" % win)
        for i in range(4):                
            time.sleep(0.5)
            fLeftClick((800 , 320) ,(100 ,100))

    # failurePos = fLocate(failureFlag)#失败标识
    # if failurePos:      
    #     fair = fair + 1
    #     print("战斗失败次数：%d" % fair)       
    #     time.sleep(1)
    #     fLeftClick((800 , 320) ,(100 ,100))

    fudanPos = fLocate(fudanFlag)#福蛋标识
    if fudanPos:
        # time.sleep(1)
        print('点击福蛋')
        fLeftClick((800 , 320) ,(100 ,100))
