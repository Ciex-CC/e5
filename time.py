import time  
  
def print_clock(minutes, seconds):  
    print(f"{int(minutes)}:{int(seconds)}")  
    time.sleep(1)  
    print_clock(minutes, seconds)  
  
minutes = int(input("print sce："))  
seconds = int(input("print min："))  
  
print("开始计时！")  
print_clock(minutes, seconds)  
print("时间到！")
