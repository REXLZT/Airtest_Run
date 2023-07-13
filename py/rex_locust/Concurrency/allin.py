from locust import task, HttpUser, constant_pacing
from locust import between, constant, tag
from locust import events
from locust.runners import MasterRunner
import csv
import time
import json
from json import JSONDecodeError
from loguru import logger
 
 
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    if not isinstance(environment.runner, MasterRunner):
        print("Beginning test setup")
    else:
        print("Started test from Master node")
 
 
@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    if not isinstance(environment.runner, MasterRunner):
        print("Cleaning up test data")
    else:
        print("Stopped test from Master node")
 
 
# 请求完成后，触发监听器：定义了输出响应的相关内容，这个可以放到locufile文件里面
@events.request.add_listener
def my_request_handler(request_type, name, response_time, response_length, response,
                       context, exception, start_time, url, **kwargs):
    if exception:
        print(f"Request to {name} failed with exception {exception}")
    else:
        print(f"request_type ： {request_type}")
        print(f"response_time ： {response_time}")
        print(f"response_length ： {response_length}")
        print(f"context ： {context}")
        print(f"start_time ： {start_time}")
        print(f"url ： {url}")
        print(f"Successfully made a request to: {name}")
        print(f"The response ： {response.text}")
 
 
class User1(HttpUser):
    weight = 1  # user1类被执行的概率是25%，user2类被执行的概率是4分之3
    host = "https://xxx.com"  # 要加载的url的前缀
    wait_time = between(2, 5)  # 每个用户结束，等待2-5秒
    # wait_time = constant(3)  # 每个用户操作完成后，等待3秒
    # wait_time = constant_pacing(10)  # 强制只等待10秒，优先级大于@task标记方法自定义的的sleep(20)
    # wait_time = constant_throughput(0.1)  # pacing的反例，这个还是等待10秒，1/值(0.1) = 10
 
    def on_start(self):
        """
        每个user启动前调用on_start方法
        这是获取用户特定测试数据的好地方。每个用户执行一次
        如果不希望记录请求，可以将self.client.<method>替换为request请求
        """
        headers = {"Content-Type": "application/json"}
        self.client.headers = headers  # 这里设置的headers将给分发给每个任务的headers，避免重复去写,高级起来了
        time.sleep(1)   #其实可以不用的
 
    @tag("smoke", "tag2")  # 执行被smoke标记的任务：--tags smoke，执行没有被tag2标记的：--exclude-tags tag2/--exclude-tags tag2 smoke
    @task(1)  # 执行脚本时，只会运行被task标记的方法作为一个测试点，其他方法都是辅助任务的
    def test_login1(self):
        # 读取csv中的用户名、密码
        file = open("../data/user/userdata_1000.csv", "r")
        table = csv.reader(file)
        for i in table:
            # 参数化登录的入参
            data = json.dumps({"account": "18741341234"})
        headers = {"Content-Type": "application/json"}
        r = self.client.post("/api/login", data=data, headers=headers)
            # self.client继承了request.session，所以不用传cookie，传登录，直接请求即可
        with r as response:  # 断言响应的内容
                try:
                    if response.status_code != 200:
                        logger.info("Did not get expected value in greeting")
                except JSONDecodeError:
                    response.failure("Response could not be decoded as JSON")  # 如果是json格式问题，抛出自己定义的异常
                except KeyError:
                    response.failure("Response did not contain expected key 'greeting'")  # 执行失败，抛出异常

        def log_failure(self,msg):
            #再加个报错打印吧
            self.client.logger.info(msg)
            r.failure(msg)
        
    @tag("smoke1")
    @tag("smoke")
    @task(3)  # 有4分之3的几率执行下面这个任务
    def test_login2(self):
        data = json.dumps({"account": "18741341234"})
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/api/login", data=data, headers=headers)
        # locust自带标准断言
        with response as res:
            try:
                if res.status_code != 200:
                    res.failure("脚本返回的code不是200")
            except JSONDecodeError:
                res.failure("Response could not be decoded as JSON")
        time.sleep(1)
        # self.environment.runner.quit()  # to stop the runner from a task method
 
    def on_stop(self):
        """
        每个user运行结束后调用on_start方法
        清理测试数据等：
        （1）调用接口清理测试数据、（2）数据库清理测试数据
        """
        data = json.dumps({"account": "18741341234"})
        headers = {"Content-Type": "application/json"}
        self.client.post("/api/login", data=data, headers=headers)
        time.sleep(1)
 
    # tasks = {test_login1: 3, test_login2: 1}  # 任务权重的第二种选择：执行1的概率是2的3倍
    # tasks = [test_login1, test_login2]  # 任务权重的第三种选择：随机执行列表里面的任务
 
 
class User2(HttpUser):
    """
    登录
    """
    weight = 4
    last_wait_time = 0
    host = "https://xxx.com"
    wait_time = constant(1)
 
    def on_start(self):
        data = json.dumps({"account": "18741341234"})
        headers = {"Content-Type": "application/json"}
        self.user_specific_testdata = self.client.post("/api/login", data=data, headers=headers)
        time.sleep(1)
        self.tfjiao = "jiaotengfei"  # 在on start方法中定义了self.tfjiao属性，所以下面可直接调用
 
    @tag("tag2")
    @task
    def test_login3(self):
        print(self.tfjiao)
        self.last_wait_time += 1  #
        data = json.dumps({"account": "18741341234"})
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/api/login", data=data, headers=headers)
        assert response.status_code == 200
 
    @tag("smoke")
    @task
    def test_login4(self):
        self.last_wait_time += 1  #
        data = json.dumps({"account": "18741341234"})
        headers = {"Content-Type": "application/json"}
        r = self.client.post("/api/login", data=data, headers=headers)
 
    def on_stop(self):
        data = json.dumps({"account": "18741341234"})
        headers = {"Content-Type": "application/json"}
        self.client.post("/api/login", data=data, headers=headers)
        time.sleep(1)