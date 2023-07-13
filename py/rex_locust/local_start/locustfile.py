import base64
import logging
from locust import events
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://10.18.3.113:9430"
    USERNAME = "admin"
    PASSWORD = "password"
    
    def on_start(self):
        self.login()

    def login(self):
        credentials = {
            "username": self.USERNAME,
            "password": self.PASSWORD
        }
        response = self.client.post("/login", data=credentials)
        if response.status_code == 200:
            print("登录成功")
        elif response.status_code ==401:
            print("其实是401")
        else:
            print("登录失败")


    @task
    def index(self):
        auth_header = "Basic " + base64.b64encode(f"{self.USERNAME}:{self.PASSWORD}".encode()).decode()
        response = self.client.get("/", headers={"Authorization": auth_header})
        print(response.status_code)
        print(response.content)
        #加了个登录成功之后保存信息，这样后续登录就不会返回401了


    @events.quitting.add_listener
    #加上退出的条件代码
    def _(environment, **kw):
        if environment.stats.total.fail_ratio > 0.01:
            logging.error("Test failed due to failure ratio > 1%")  #超过1%即时请求失败
            environment.process_exit_code = 1
        elif environment.stats.total.avg_response_time > 200:
            logging.error("Test failed due to average response time ratio > 200 ms")    #平均响应时间大于200ms
            environment.process_exit_code = 1
        elif environment.stats.total.get_response_time_percentile(0.95) > 800:
            logging.error("Test failed due to 95th percentile response time > 800 ms")  #响应时间的第 95 个百分位大于 800 毫秒
            environment.process_exit_code = 1
        else:
            environment.process_exit_code = 0
            #有点问题的，回头研究下，咋加了没效果嘞