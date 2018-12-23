import yuhun

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
                print('功能暂未实现！请选择其它模式')
            else:
                print('输入错误，请重新选择！')
        else:
            print('请输入数字！')

    while True:        
        if inputA == 1:
            print('1.队长')
            print('2.队员')
            inputB = input('请选择角色：')
            if inputB.isdigit():
                inputB = int(inputB)
                if inputB == 1:
                    print('程序启动完毕！')
                    while True:
                        try:
                            yuhun.duizhang()
                        except:
                            pass
                    break
                elif inputB == 2:
                    print('程序启动完毕！')
                    while True:
                        try:                            
                            yuhun.duiyuan()
                        except:
                            pass
                    break
                else:
                    print('输入错误，请重新选择！')
            else:
                print('请输入数字！')

start()#开始