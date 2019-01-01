import yuhun
import tansuo
# import md5
# from configs import configs

# path = 'config.ini'
# m = md5.get_file_md5(path)
# conf = configs()
# stype = conf.getOneConfigValue(('setting','type'))

# def starts():
    # global stype
    # print(stype)
    # if m != md5.get_file_md5(path):
    #     conf = configs()
    #     stype = conf.getOneConfigValue(('setting','type'))
    # time.sleep(1)

# while 1:
#     starts()

def start():
    while True:
        print('1.御魂觉醒')
        print('2.探索')
        inputA = input('请选择游戏模式')
        if inputA.isdigit():
            inputA = int(inputA)
            if inputA == 1:
                break
            elif inputA == 2:
                break
                # print('功能暂未实现！请选择其它模式')
            else:
                print('输入错误，请重新选择！')
        else:
            print('请输入数字！')

    while True:        
        # if inputA == 1:
        print('1.队长')
        print('2.队员')
        inputB = input('请选择角色：')
        if inputB.isdigit():
            inputB = int(inputB)
            if inputB == 1:
                if inputA == 1:
                    print('御魂觉醒“队长”程序启动完毕！')
                    while True:
                        try:
                            yuhun.duizhang()
                        except:
                            pass
                    break
                elif inputA == 2:
                    print('功能暂未实现！请选择其它模式')
            elif inputB == 2:
                if inputA == 1:
                    print('御魂觉醒“队员”程序启动完毕！')
                    while True:
                        try:                            
                            yuhun.duiyuan()
                        except:
                            pass
                    break
                elif inputA == 2:
                    print('探索“队员”程序启动完毕！')
                    while True:
                        try:                            
                            tansuo.duiyuan()
                        except:
                            pass
                    break
            elif inputB == 3:
                if inputA == 2:
                    print('探索“单刷”程序启动完毕！')
                    while True:
                        try:                            
                            tansuo.danshua()
                        except:
                            pass
                    break
            else:
                print('输入错误，请重新选择！')
        else:
            print('请输入数字！')

start()#开始