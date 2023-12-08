import time  
  
def print_clock(minutes, seconds):  
    print(f"{int(minutes)}:{int(seconds)}")  
    time.sleep(1)  
    print_clock(minutes, seconds)  
  
minutes = int(input("请输入分钟数："))  
seconds = int(input("请输入秒数："))  
  
print("开始计时！")  
print_clock(minutes, seconds)  
print("时间到！")
