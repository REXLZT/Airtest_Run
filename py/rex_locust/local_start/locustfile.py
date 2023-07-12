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
        else:
            print("登录失败")

    @task
    def index(self):
        self.client.get("/")
