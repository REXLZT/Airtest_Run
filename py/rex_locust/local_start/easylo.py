from locust import HttpUser, task, between

class MyUser(HttpUser):
    host = "http://10.18.3.113:9340"
    wait_time = between(1, 2)  # 用户执行任务之间等待的时间，单位为秒

    @task  # 使用@task装饰器来标记一个任务
    def my_task(self):
        self.client.get("/")  # 执行GET请求
