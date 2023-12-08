import datetime  
  
def print_date():  
    now = datetime.datetime.now()  
    print(now.strftime("%Y-%m-%d"))  
  
print("当前日期：")  
print_date()
