from datetime import datetime
class driverData():
    """储存待录入驾驶人资料"""
    def __init__(self,suoyin,name,ID,region,zjcx1,zjcx2,phone,address,location,edit = False,error = False,log=""):
        self.suoyin = suoyin
        self.name = name
        self.ID = ID    
        self.region = region
        self.zjcx1 = zjcx1
        self.zjcx2 = zjcx2
        self.phone = phone
        self.address = address
        self.location = location 
        self.edit = edit        
        self.error = error
        self.log=log
        self.date = "2018-08-15"
        


    def show_error_tiqu(self):
        self.add_error_tiqu()
        self.error = True
        self.print_log()
    
    def show_edit(self):
        self.edit = True
        self.add_log_finish()
        self.print_log()



    def end(self):
        self.edit = True        
        self.print_log()

    def add_log_finish(self):
        self.log = "完成，%s,%s,%s,%s,%s 已录入系统。"% (datetime.now(),self.suoyin,self.name,self.ID,self.address)  
        
    def add_error_log(self):
        self.log = "错误，%s,%s,%s,%s,%s 录入异常。"% (datetime.now(),self.suoyin,self.name,self.ID,self.address) 
    
    def add_error_tiqu(self):
        self.log = "错误，%s,%s,%s,%s,%s 录入异常。"% (datetime.now(),self.suoyin,self.name,self.ID,self.address)


    def show_error(self):
        self.error = True
        self.add_error_log()
        self.print_log()


    def add_pass_state(self):
        self.log = "提示：%s,%s,%s,%s状态为已录入，跳过..."% (datetime.now(),self.suoyin,self.name,self.ID)

    def print_log(self):
        print(self.log)

    def pass_state(self):
        self.edit = True
        self.add_pass_state()
        self.print_log()