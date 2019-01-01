import configparser

#读写配置文件
class configs():

    def __init__(self):
        self.path = 'config.ini'
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path)

    #获取配置字典
    def getConfigDict(self,sectionName):   
        clist = self.cf.items(sectionName)
        return dict(clist)

    #获取单个配置的值
    def getOneConfigValue(self,sk):        
        return self.cf.get(sk[0],sk[1])

    #更新单个配置
    def setConfigValue(self,skv):
        self.cf.set(skv[0],skv[1],skv[2])
        self.cf.write(open(self.path,'w'))

    # def getConfigDisc(sectionName):
    #     configs = {}
    #     path = 'config.ini'
    #     cf = configparser.ConfigParser()
    #     cf.read(path)
    #     clist = cf.items(sectionName)
    #     for c in clist:
    #         configs[c[0]] = c[1]

# c = configs()
# s = c.getConfigDict('setting')
# print(s)
# y = c.getConfigDict('yuhun')
# print(y)

# s = c.getConfigDict('setting')
# print(s)
# print(c.getOneConfigValue(('setting','type')))