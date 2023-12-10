import datetime  
  
def print_date():  
    now = datetime.datetime.now()  
    print(now.strftime("%Y-%m-%d"))  
  
print("nowdate:")  
print_date()
