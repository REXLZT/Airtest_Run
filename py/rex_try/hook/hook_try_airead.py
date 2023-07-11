import time
class LazyPerson(object):
    def __init__(self, name):   # 构造函数，初始化懒人的名字和他的日常活动函数
        self.name = name
        self.watch_tv_func = None
        self.have_dinner_func = None
    def get_up(self):   # 懒人起床的方法
        print("%s get up at:%s" % (self.name, time.time()))
    def go_to_sleep(self):  # 懒人睡觉的方法
        print("%s go to sleep at:%s" % (self.name, time.time()))
    def register_tv_hook(self, watch_tv_func):  # 注册看电视的活动函数
        self.watch_tv_func = watch_tv_func
    def register_dinner_hook(self, have_dinner_func):  # 注册吃饭的活动函数
        self.have_dinner_func = have_dinner_func
    def enjoy_a_lazy_day(self):   # 懒人享受一天的方法
        self.get_up()  # 起床
        time.sleep(3)
        if self.watch_tv_func is not None:  # 如果已经注册了看电视的活动函数
            self.watch_tv_func(self.name)  # 看电视
        else:
            print("no tv to watch")  # 没有注册看电视的活动函数，输出提示信息                                                                                                                                                                       
        time.sleep(3)
        if self.have_dinner_func is not None:  # 如果已经注册了吃饭的活动函数
            self.have_dinner_func(self.name)  # 吃饭
        else:
            print("nothing to eat at dinner")  # 没有注册吃饭的活动函数，输出提示信息
        time.sleep(3)
        self.go_to_sleep()  # 睡觉
# 定义各种活动函数
def watch_daydayup(name):
    print("%s : The program ---day day up--- is funny!!!" % name)
def watch_happyfamily(name):
    print("%s : The program ---happy family--- is boring!!!" % name)
def eat_meat(name):
    print("%s : The meat is nice!!!" % name)
def eat_hamburger(name):
    print("%s : The hamburger is not so bad!!!" % name)
if __name__ == "__main__":
    lazy_tom = LazyPerson("Tom")  # 创建Tom对象
    lazy_jerry = LazyPerson("Jerry")  # 创建Jerry对象
    # 为Tom和Jerry注册他们的活动函数
    lazy_tom.register_tv_hook(watch_daydayup)
    lazy_tom.register_dinner_hook(eat_meat)
    lazy_jerry.register_tv_hook(watch_happyfamily)
    lazy_jerry.register_dinner_hook(eat_hamburger)
    # 让Tom和Jerry享受他们的一天
    lazy_tom.enjoy_a_lazy_day()
    lazy_jerry.enjoy_a_lazy_day()
