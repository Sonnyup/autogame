'''
配置文件
'''
import md5
from configs import configs

#分辨率：960x540
#查找的图片
dAcceptBtn = 'image/jujue.bmp' #拒绝协作
teamFlag = 'image/xzdw.bmp' #组队界面标识
fightBtn = 'image/kszd.bmp' #开始战斗按钮
inviteBtn = 'image/yq.bmp' #组队界面邀请按钮
readyBtn = 'image/zb.bmp' #准备按钮
winFlag = 'image/win.bmp'#胜利标识-御魂觉醒
shibaiFlag = 'image/shibai.bmp'#失败标识-御魂觉醒
fudanFlag = 'image/hun.bmp'#福蛋标识
autoFlag = 'image/auto.bmp'#自动邀请勾选框-御魂觉醒
autoConfirm = 'image/autook.bmp'#默认邀请-确认按钮
autoAcceptBtn = 'image/zdjs.bmp' #组队邀请-自动接受
inviteMsg = 'image/yqtip.bmp' #邀请提示
tsBtn = 'image/tsbtn.bmp' #探索
tsFlag = 'image/tsflag.bmp' #探索
fxFlag = 'image/faxian.bmp' #发现妖怪
shibaiFlag = 'image/shibai.bmp' #失败标识
yaoqingTip = "image/yqtip.bmp" #邀请提示
dengFlag = 'image/deng.bmp' #灯标识
bqFlag = 'image/bq.bmp'#表情标识
fanhuiBtn = 'image/fanhui.bmp'#返回按钮
qrBtn = 'image/qr.bmp'#确认按钮
exp = ['image/exp1.bmp','image/exp2.bmp','image/exp3.bmp','image/exp4.bmp','image/exp5.bmp','image/exp6.bmp','image/exp7.bmp','image/exp8.bmp','image/exp9.bmp','image/exp10.bmp']
zbjmFlag = 'image/zbjm.bmp'
manFlag = 'image/man.bmp'
allFlag = 'image/all.bmp'
nFlag = 'image/n.bmp'
dengjiFlag = 'image/dengji.bmp'


lipinBtn = 'image/lipin.bmp' #礼品
dianBtn = 'image/dian.bmp' #点
dian2Btn = 'image/dian2.bmp' #点2
dian3Btn = 'image/dian3.bmp' #点3
chachaBtn = 'image/chacha.bmp' #关闭
kuaijinBtn = 'image/kuaijin.bmp' #快进
renyiBtn = 'image/renyi.bmp' #点击任意位置
tiaoguoBtn = 'image/tiaoguo.bmp' #跳过
yanBtn = 'image/yan.bmp' #眼
daoBtn = 'image/dao.bmp' #刀
daoBtn2 = 'image/dao2.bmp' #刀
bossBtn = 'image/boss.bmp' #boss
wenhaoBtn = 'image/wenhao.bmp' #问号
beijingBtn = 'image/beijing.bmp' #背景
jieshouBtn = 'image/jieshou.bmp' #接受
jiaoxueFlag = 'image/jiaoxue.bmp' #教学标识
hdjlBtn = 'image/hdjl.bmp' #获得奖励标识
tswin = 'image/tswin.bmp' #探索胜利
tsfu = 'image/tsfu.bmp' #探索福蛋
lipinFlag = 'image/lipin.bmp' #小纸人礼盒
towSixFlag = 'image/26.bmp'
yaoFlag = 'image/yao.bmp'
fbjmFlag = 'image/fbjm.bmp'

#########妖气##########
zuduiBtn = 'image/yaoqi/zudui.bmp'
yqfyBtn = 'image/yaoqi/yqfy.bmp' #妖气封印按钮
yqfyTip = 'image/yaoqi/yqfy2.bmp'
rhfBtn = 'image/yaoqi/rhf.bmp' #日和坊
yqfyrhfTip = 'image/yaoqi/yqfyrhf.bmp'
xswBtn = 'image/yaoqi/xsw.bmp' #小松丸
yqfyxswTip = 'image/yaoqi/yqfyxsw.bmp'
zdppBtn= 'image/yaoqi/zdpp.bmp' #自动匹配
chaBtn= 'image/yaoqi/cha.bmp' #拒绝协作
jrBtn = 'image/yaoqi/jr.bmp' #加入
sxBtn = 'image/yaoqi/sx.bmp' #刷新

yaoqiName = '日和坊'
if yaoqiName == '日和坊':
    yqBtnImg = rhfBtn
    yqTipImg = yqfyrhfTip
elif yaoqiName == '小松丸':
    yqBtnImg = xswBtn
    yqTipImg = yqfyxswTip

#参数设置
peopleNum = 2 #御魂觉醒 参战人数

fileMd5 = md5.get_file_md5() #生成配置文件MD5
conf = configs() #读取配置类
publicConf = conf.getConfigDictInt('publicuse')#公用配置参数
yhConf = conf.getConfigDictInt('yuhun') #御魂配置参数
jxConf = conf.getConfigDictInt('juexing')#觉醒参数
tsConf = conf.getConfigDictInt('tansuo')#探索参数