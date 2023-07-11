import time

class LazyPerson(object):
    def __init__(self, name):
        self.name = name
        self.watch_tv_func = []  # 将这里改为列表
        self.have_dinner_func = None

    def get_up(self):
        print("%s get up at:%s" % (self.name, time.time()))

    def go_to_sleep(self):
        print("%s go to sleep at:%s" % (self.name, time.time()))

    def register_tv_hook(self, watch_tv_func):
        self.watch_tv_func.append(watch_tv_func)  # 改为用append，将函数添加到列表中

    def register_dinner_hook(self, have_dinner_func):
        self.have_dinner_func = have_dinner_func

    def enjoy_a_lazy_day(self):
        self.get_up()
        time.sleep(3)

        # 这里遍历列表，执行每个函数
        for func in self.watch_tv_func:
            func(self.name)
        time.sleep(3)

        if self.have_dinner_func is not None:
            self.have_dinner_func(self.name)
        else:
            print("nothing to eat at dinner")
        time.sleep(3)

        self.go_to_sleep()

def watch_daydayup(name):
    print("%s : The program ---day day up--- is funny!!!" % name)

def watch_happyfamily(name):
    print("%s : The program ---happy family--- is boring!!!" % name)

def eat_meat(name):
    print("%s : The meat is nice!!!" % name)

def eat_hamburger(name):
    print("%s : The hamburger is not so bad!!!" % name)

if __name__ == "__main__":
    lazy_tom = LazyPerson("Tom")
    lazy_jerry = LazyPerson("Jerry")

    lazy_tom.register_tv_hook(watch_daydayup)
    lazy_tom.register_dinner_hook(eat_meat)
    lazy_jerry.register_tv_hook(watch_happyfamily)
    lazy_jerry.register_tv_hook(eat_meat)  # 注册第二个看电视的函数
    lazy_jerry.register_dinner_hook(eat_hamburger)
    lazy_jerry.enjoy_a_lazy_day()
    #酱紫的话，LazyPerson对象lazy_jerry会在享受一天时，先看happy family，然后看eat meat，最后吃汉堡包。
    #避免了调用同个hook会覆盖掉上一个注册函数的情况