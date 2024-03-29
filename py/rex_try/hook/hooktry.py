import time

class LazyPerson(object):
    #构造函数，初始化
    def __init__(self, name):
        self.name = name
        self.watch_tv_func = None
        self.have_dinner_func = None

    def get_up(self):
        print("%s get up at:%s" % (self.name, time.time()))

    def go_to_sleep(self):
        print("%s go to sleep at:%s" % (self.name, time.time()))

    def register_tv_hook(public, watch_tv_func):
        public.watch_tv_func = watch_tv_func
        #注册个示例方法

    def register_dinner_hook(self, have_dinner_func):
        self.have_dinner_func = have_dinner_func

    def enjoy_a_lazy_day(self):

        # get up
        self.get_up()
        time.sleep(3)
        # watch tv
        # check the watch_tv_func(hooked or unhooked)
        # hooked
        if self.watch_tv_func is not None:
            self.watch_tv_func(self.name)
        # unhooked
        else:
            print("no tv to watch")
        time.sleep(3)
        # have dinner
        # check the have_dinner_func(hooked or unhooked)
        # hooked
        if self.have_dinner_func is not None:
            self.have_dinner_func(self.name)
        # unhooked
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
    # register hook
    lazy_tom.register_tv_hook(watch_daydayup)
    lazy_tom.register_dinner_hook(eat_meat)
    lazy_jerry.register_tv_hook(watch_happyfamily)
    lazy_jerry.register_dinner_hook(eat_hamburger)
    lazy_jerry.register_tv_hook(eat_meat)
    #两次调用是会覆盖掉前一次注册的函数，如果想要的话，得将LazyPerson改为列表的，详情将hooktry_double_try
    # enjoy a day
    # lazy_tom.enjoy_a_lazy_day()
    lazy_jerry.enjoy_a_lazy_day()

