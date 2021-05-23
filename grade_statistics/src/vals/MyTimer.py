import time as t


class MyTimer():

    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.prompt = "还没开始运行哦"
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt
    
    __repr__ = __str__

    
    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop停止计时"
        print("开始计时...")

     #计时结束
    def stop(self):
        if not self.begin:
            print("请先调用start计时")
        else:
            self.end = t.localtime()
            self.__calc()
            print("计时结束！")

    #内置函数
    def __calc(self):
        self.prompt = "总共运行了："
        self.lasted = []
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        print(self.prompt)

    #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0
        
if __name__ == "__main__":
    timer = MyTimer()
    timer.start()
    t.sleep(3) # 休眠3秒
    timer.stop()
