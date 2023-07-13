import base64
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