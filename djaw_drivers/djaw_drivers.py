﻿# coding:utf-8
# include <sys.stdin>
# include <sys.stdout>
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
import urllib
import urllib3

import file_transport as e_to_j
import driverData
import setting
import json
import sys
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import pytesser3 as pyt3
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.select import Select



# 读取json数据库,获取待处理列表
list_driver_js = []  # 所有待处理的驾驶人数据JS类型
list_driver = []  # 所有待处理的驾驶人数据
driverDatas = []
n = 0  # 计数器
end = 0
start = 0
error = 0
switch_1 = True
error_count = 0
time_clock = 5
b = True
my = setting.setting("ctsz005","123456")
#大型汽车=大型汽车19:29 2018/8/30
#低速车 =？无法提取
#普通摩托车=？无法提取
#轻便摩托车=？无法提取
#拖拉机=？无法提取


#while True:
    
#    if input_num == "1":
#        my.get_and_save_setting()#

#e_to_j.excel_json('driver.xlsx' or 'driver.xls', 'driver.json')
#print("第一步完成！")
#e_to_j.file_to_json_fomat(
#"driver.json", "driver2.json",  list_driver)
## e_to_j.json_to_personDatalist("002.json",list_poor_family_js,list_poor_family,error,start,end,n)
#input("数据转换完成，生成文件完成，程序即将关闭，下次使用请输入2，按任意键退出......")
#sys.exit()

#    elif input_num == "2":
#my.load_setting()
#start = time.time()

e_to_j.json_to_carDatalist(
    "driver2.json", list_driver_js, list_driver, error, start, end, n,1,5000)#读取11767条数据耗时13秒



#1-2753  已以镇级区划录入

#e_to_j.carDatalist_to_json(list_car, 'car2.json')

#input()
#end = time.time()
#print (end-start)
#input()
#start = time.time()
#e_to_j.carDatalist_to_json(list_car, 'car2.json')#写入11767条数据耗时13秒
#end = time.time()
#print (end-start)


#    elif input_num == "3":
#        e_to_j.js_to_xlsx('002.json', 'error.xlsx')
#        # 将002.json中error=true的项提取出来并写入error+datetime.excel
#        input("按任意键退出......")
#        sys.exit()
#    else:
#        print("请重新输入")
## input()

#e_to_j.personDatalist_to_json(list_poor_family, '002.json')

## 初始化---------
## input()
## e_to_j.save_as_json(list_poor_family,'002.json')

## 构造模拟浏览器


chromedriver = my.chromePath

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
driver.implicitly_wait(5)




url = my.url
#----------------------------------------------------------------开始录入驾驶人------------------------------------
driver.get(url)  # 打开网址
driver.maximize_window()  # 窗口最大化

time.sleep(2)


driver.find_element_by_xpath(my.xpath1).send_keys(my.account)  # 输入账号
# time.sleep(1)
driver.find_element_by_xpath(my.xpath2).send_keys(my.password)  # 输入密码
driver.find_element_by_xpath(my.xpathyzmflash).click()  # 点击刷新验证码

yanzhengma = input("请手动输入验证码：")
driver.find_element_by_xpath(my.xpath3).send_keys(yanzhengma)  # 输入验证码
driver.find_element_by_xpath(my.xpath4).click()  # 点击登陆

#yanzhengma = pyt3.image_file_to_string('code.png')[:4]

# 验证码处理
#while b:
#    driver.find_element_by_xpath(
#        my.xpathyzmflash).click()  # 点击刷新验证码
#    time.sleep(1)
#    driver.save_screenshot('screenshot.png')
#    imgelement = driver.find_element_by_id('yzmImage')
#    location = imgelement.location  # 获取验证码x,y轴坐标
#    size = imgelement.size  # 获取验证码的长宽
#    rangle = (int(location['x']), int(location['y']), int(
#        location['x']+size['width']), int(location['y']+size['height']))  # 写成我们需要截取的位置坐标
#    i = Image.open("screenshot.png")  # 打开截图
#    result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
#    result.save('result.png')
#    yanzhengma = pyt3.image_file_to_string('result.png', 'eng').replace(' ','')[:4]
#    print(">%s<" % yanzhengma)
#    driver.find_element_by_xpath(my.xpath3).clear() #清空验证码输入栏
#    driver.find_element_by_xpath(my.xpath3).send_keys(yanzhengma)  # 输入验证码
#    driver.find_element_by_xpath(my.xpath4).click()  # 点击登陆
#    time.sleep(2)

#    input()
    # 登陆成功
    #try:
    #    driver.find_element_by_xpath(
    #        "//div[contains(text(),'验证码不正确,请重新输入验证码')]")
    #    time.sleep(1)
    #    driver.find_element_by_xpath(
    #        "//button[@class = 'swal2-confirm swal2-styled']").click()
    #except:
    #    b = False


# 加载时间过长 异常处理
time.sleep(2)
driver.switch_to_frame('leftFrame') #切换iframe
#driver.find_element_by_xpath(my.xpath102).click() #点击农村驾驶人
time.sleep(1)
driver.find_element_by_xpath(my.xpath5).click()

#js = "document.querySelector('#menutab_2').click()"
#driver.execute_script(js)

#driver.find_element_by_xpath(my.xpath5).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpathjcxxgl).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpath6).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpath26).click()
time.sleep(4)
driver.switch_to.default_content() #恢复默认表单
driver.switch_to_frame('rightFrame') #切换iframe

main_windows=driver.current_window_handle #标记当前窗口为主窗口
driver.find_element_by_xpath(my.xpath9).click()  
time.sleep(1)
all_handles=driver.window_handles#标记所有窗口

#for handle in all_handles:
#    if handle !=main_windows:
#        driver.switch_to_window(handle)#切换到非主窗口
driver.switch_to_window(all_handles[-1])
type_windows =driver.current_window_handle
# "大型汽车", "J7D220", "重型普通货车",  "货运",  "13777761839",  "车溪乡翊武村民委员会8组08046号",  "城头山镇",  "",  "","1" 
#   "大型汽车""J78783","中型自卸货车", "货运", "18573635693","车溪乡万兴村2组02029号",  "城头山镇", "",  "","2"
#list_car=[carData.carData("大型汽车","J78783","中型自卸货车", "货运", "18573635693","车溪乡万兴村2组02029号",  "城头山镇", "",  "","2"),carData.carData("大型汽车","J7D220", "重型普通货车",  "货运",  "13777761839",  "车溪乡翊武村民委员会8组08046号",  "城头山镇",  "",  "","1" )]



# for p1 in list(reversed(list_poor_family[:])):

#try:

for p1 in list_driver:
    #if p1.suoyin.endswith("50"):#每隔50条保存一次
    #        e_to_j.carDatalist_to_json(list_car, 'car.json')
            
    try:
        if (p1.edit == False and p1.error == False): 
            if p1.suoyin.endswith("0"):#每隔10条保存一次
                e_to_j.carDatalist_to_json(list_driver, 'driver2.json')#写入11767条数据耗时13秒
                    
            #WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            #                (By.XPATH, my.xpath11)))
            #//td[@id = 'QY_Code_td']/input
            #if int(p1.suoyin)%2==0:#每隔500条清理一次缓存
            #    type_windows =driver.current_window_handle
            #    #driver.get("chrome://settings/clearBrowserData")
            #    js='window.open("chrome://settings");'
            #    driver.execute_script(js)
                
            #    all_handles = driver.window_handles
            #    print(all_handles)

            #    driver.switch_to_window(all_handles[-1])
                
            #    driver.get("chrome://settings")
            #    time.sleep(2)
                
            #    root1 = driver.find_element_by_tag_name('settings-ui')
            #    shadow_root1 = e_to_j.expand_shadow_element(root1,driver)

            #    root2 = shadow_root1.find_element_by_css_selector('[page-name="设置"]')
            #    shadow_root2 = e_to_j.expand_shadow_element(root2,driver)

            #    root3 = shadow_root2.find_element_by_id('search')
            #    shadow_root3 = e_to_j.expand_shadow_element(root3,driver)

            #    search_button = shadow_root3.find_element_by_id("searchTerm")
            #    search_button.click()

            #    text_area = shadow_root3.find_element_by_id('searchInput')
            #    text_area.send_keys("清除浏览数据")
            #    time.sleep(2)

            #    root0 = shadow_root1.find_element_by_id('main')
            #    shadow_root0_s = e_to_j.expand_shadow_element(root0,driver)


            #    root1_p = shadow_root0_s.find_element_by_css_selector('settings-basic-page')
            #    shadow_root1_p = e_to_j.expand_shadow_element(root1_p,driver)


            #    root1_s = shadow_root1_p.find_element_by_css_selector('settings-privacy-page')
            #    shadow_root1_s = e_to_j.expand_shadow_element(root1_s,driver)

            #    content_settings_div = shadow_root1_s.find_element_by_css_selector('settings-animated-pages')


            #    content_settings = content_settings_div.find_element_by_css_selector('button[id="clearBrowsingDataTrigger"]')
            #    driver.execute_script("arguments[0].click();",content_settings)
            #    time.sleep(2)
            #    root1_q =shadow_root1_s.find_element_by_css_selector('settings-clear-browsing-data-dialog')
            #    shadow_root1_q = e_to_j.expand_shadow_element(root1_q,driver)

            #    setting_button_ele = shadow_root1_q.find_element_by_css_selector('[id="clearBrowsingDataConfirm"]')
            #    driver.execute_script("arguments[0].click();",setting_button_ele)

            #    time.sleep(5)
            #    driver.close()
            #    driver.switch_to_window(type_windows)


    
            time.sleep(1)

            driver.find_element_by_xpath(my.xpath13).clear() #清空
    
            driver.find_element_by_xpath(my.xpath13).send_keys(p1.ID) #输入身份证号
                
            time.sleep(0.5)
            driver.find_element_by_xpath(my.xpath17).click()  # 点击查重
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, my.xpath19)))
            if '勿重复录入' in driver.find_element_by_xpath(my.xpath19).text:
                driver.find_element_by_xpath(my.xpath18).click() #点击确定
                p1.pass_state()
                continue
            else:
                driver.find_element_by_xpath(my.xpath18).click() #点击确定
            time.sleep(1)
            driver.find_element_by_xpath(my.xpath14).click()  # 点击提取
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, my.xpath19)))
            if '未提到该身份证号' in driver.find_element_by_xpath(my.xpath19).text:
                driver.find_element_by_xpath(my.xpath18).click() #点击确定
                p1.show_error_tiqu()
                continue
            else:
                driver.find_element_by_xpath(my.xpath18).click()  # 点击提取后弹窗确定
        
            time.sleep(0.5)
            ele = driver.find_element_by_xpath(my.xpath11)  
            driver.execute_script("arguments[0].focus();",ele)
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, "//a[@attr_name = '%s']"% p1.location)))
            driver.find_element_by_xpath("//a[@attr_name = '%s']"% p1.location).click()  # 点击获取行政区划


            #ele2 = driver.find_element_by_xpath(my.xpath15)
            #driver.execute_script("arguments[0].click();",ele)# 点击提取
        

            time.sleep(0.5)
            driver.find_element_by_xpath(my.xpath22).clear() #清空电话号码输入框
            driver.find_element_by_xpath(my.xpath22).send_keys(p1.phone)
            time.sleep(0.5)
            driver.find_element_by_xpath(my.xpath23).send_keys(p1.date) 
            
            s1 = Select(driver.find_element_by_id("JiaZQX"))
            if s1.first_selected_option.text == "请选择":
                s1.select_by_value("长期")
                
            driver.find_element_by_xpath(my.xpath20).click()#点击保存

            

            
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, my.xpath19)))     
            #time.sleep(1)
            driver.find_element_by_xpath(my.xpath18).click()#点击继续
            p1.show_edit() 
        else :
            p1.pass_state()
    except TimeoutException :
        p1.show_error()
        print("")
        type_windows.close()
        driver.switch_to_window(main_windows)#切换到主窗口
        driver.refresh()
        time.sleep(3)
        driver.switch_to_frame('leftFrame') #切换iframe
        #driver.find_element_by_xpath(my.xpath102).click() #点击农村驾驶人
        time.sleep(1)
        driver.find_element_by_xpath(my.xpath5).click()
    
        #js = "document.querySelector('#menutab_2').click()"
        #driver.execute_script(js)
    
        #driver.find_element_by_xpath(my.xpath5).click()
        time.sleep(1)
        driver.find_element_by_xpath(my.xpathjcxxgl).click()
        time.sleep(1)
        driver.find_element_by_xpath(my.xpath7).click()
        time.sleep(1)
        driver.find_element_by_xpath(my.xpath8).click()
        time.sleep(1)
        driver.switch_to.default_content() #恢复默认表单
        driver.switch_to_frame('rightFrame') #切换iframe
    
        main_windows=driver.current_window_handle #标记当前窗口为主窗口
        driver.find_element_by_xpath(my.xpath9).click()  
        #time.sleep(2)
        all_handles=driver.window_handles#标记所有窗口
        driver.switch_to_window(all_handles[-1])
        type_windows =driver.current_window_handle
        continue
#except :
#    pass

#finally:
#    e_to_j.carDatalist_to_json(list_driver, 'driver2.json')
#    with open("log.txt", 'w', encoding="utf-8") as f:
#        for p1 in list_driver:
#            f.writelines(p1.log+'\n')

#    driver.quit()
