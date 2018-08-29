# -*- coding:utf-8 -*-
import json
import codecs
class setting():
    """w"""
    def __init__(self,account,password):
        self.url = "http://hnnc.122.gov.cn/view/frame/login.html"
        self.account = account
        self.password = password
        self.chromePath = u'C:/Program Files (x86)/Google/Chrome/Application/chromedriver'
        self.xpath1 = "//input[@name = 'username']"#帐号输入框体
        self.xpath2 = "//input[@name = 'password']"#密码输入框体
        self.xpath3 = "//input[@name = 'captcha']"#验证码输入框体
        self.xpath4 = "//div[@class='loginbtn']"#首页登陆按钮
        self.xpathcaptcha = "//img[@id='yzmImage']" #验证码图片元素
        self.xpathyzmflash = "//a[@id = 'refresh_yzm']" #验证码刷新
        self.xpath5 = "//div[@id = 'menutab_2']"#系统菜单按钮
        self.xpathjcxxgl ="//li[@id = 'tree_M1002']" #基础信息管理菜单
        self.xpath6 = "//a[@id ='menu_M4701']"#农村驾驶人菜单
        self.xpath26 = "//li[@id ='tree_M4702']/a"#农村驾驶人菜单=>资料录入
        self.xpath7 = "//a[@id ='menu_M2201']"#农村机动车菜单
        self.xpath8 = "//li[@id ='tree_M2202']/a"#农村机动车菜单=>资料录入
        self.xpath101 = "//li[@attr_id='M4702']"#  农村驾驶人录入
        self.xpath102 =  "//li[@attr_shortcutname='机动车资料录入']"# 农村机动车驾驶



        self.xpath9 = "//li[@id ='btn_add']"#添加按钮
        self.xpath10 = "//a[@attr_name = '大庙村']" #城头山镇按钮
        self.xpathjiahao = "//img[@code='000430007027008']"#城头山镇前加号按钮
        self.xpath12 = "//a[@attr_name = '城头山镇']" #各村级按钮
        self.xpath11 = "//input[@id = 'QY_Code']" #行政区划openselect
        self.xpathHPZL = "//select[@id = 'HPZL']" #号牌种类select
        self.xpathCLLB = "//select[@id = 'CheLLB']" #车辆类别select
        self.xpathSYXZ = "//select[@id = 'ShiYXZ']" #使用性质select

        self.xpath13 = "//input[@id = 'SFZH']" #身份证号输入框体
        self.xpathHPHM = "//input[@id = 'CPname']" #号牌号码输入框体

        self.xpath14 = "//a[@class = 'addsJSR bluebutton']"#驾驶人提取按钮
        self.xpath17 = "//a[@class = 'addsfzh bluebutton']"#驾驶人查重按钮
        self.xpath16 = "//a[@class = 'addCPname bluebutton ']"#机动车查重按钮
        self.xpath15 = "//a[@class = 'addCXJDC bluebutton ']"#机动车提取按钮
        self.xpath18 = "//a[@class = 'button button_ok']" #提取成功后弹窗确定按钮
        self.xpath19 = "//div[@class='SysMsgMain']/div" #提取成功后弹窗内容元素

        self.xpath20 = "//a[@id = 'save']" #二页面保存按钮
        self.xpath21 = "//a[@id = 'Close']" #二页面关闭按钮
        self.xpath22 = "//input[@id ='Mobile']" #驾驶人手机号码输入页面
        self.xpath23 = "//input[@id = 'tjsj']" #统计时间输入框  格式xxxx-xx-xx
        self.xpath24 = "//input[@id = 'DoTime']" #摸底时间输入框  格式xxxx-xx-xx
        self.xpath25 = "//input[@id = 'IsKY_0']" #是否客运车辆 否 radio按钮
        self.xpath28 = "//div[@class = 'SysMsgMain']/div[2]" #添加完成后继续
        self.xpath27 = "//div[@class = 'SysMsgMain']/div" #添加完成后关闭



        self.xpath201="//a[@attr_name = '湖南省']"#定位湖南省
        self.xpath2011="//img[@code='000430']" #定位湖南省 前的+号
        self.xpath2012="//img[@code='000430007']" #定位常德市 前的+号
        self.xpath2013="//img[@code='000430007027']" #定位澧县 前的+号

        self.xpath202="//a[@attr_name = '常德市']"#定位常德市
        self.xpath203="//a[@attr_name = '澧县']"#定位澧县
        self.xpath204="//a[@attr_name = '城头山镇']"#定位湖南省

        #未提到该身份证号【43072419871022163X】对应的农村驾驶人信息！ 提取失败提示信息

        #该身份证号【432424197205235011】【已】被【常德市澧县城头山镇翊武村】录入，请与【常德市澧县城头山镇翊武村】联系，勿重复录入。 查重反馈


        
    
    def load_setting(self):
        with open('setting.json','r',encoding = 'utf-8') as f:
            list_f = json.load(f)
            self.account = list_f['account']
            self.password = list_f['password']
        print("已从'setting.json'加载帐号密码")

    def get_and_save_setting(self):
        account = input("请输入帐号")
        password = input("请输入密码")
        dict_j = {'account':account,'password':password}
        j_file = str(json.dumps(dict_j, ensure_ascii=False))
        with codecs.open('setting.json','w', encoding='utf-8', errors ='ignore') as f:
            f.write(j_file)
        print("已将账号和密码，保存至目录下的setting.json，可用记事本打开自行编辑，下次运行将自动读取已存配置")
