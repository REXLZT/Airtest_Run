import tkinter as tk
import time
import threading
from pynput.mouse import Button, Controller

# 创建窗口
root = tk.Tk()
root.title('Mouse Clicker')
root.geometry('250x150')

# 点击次数变量
count = tk.StringVar(value='1')

# 获取鼠标控制器对象
mouse = Controller()

# 开始点击
def start_clicking():
    # 获取点击次数
    clicks = int(count.get())

    # 获取点击位置坐标
    x, y = (int(root.winfo_pointerx()), int(root.winfo_pointery()))

    # 建立线程进行点击操作，防止界面阻塞
    def clicking_thread():
        for i in range(clicks):
            # 移动鼠标到指定位置并模拟点击
            mouse.position = (x, y)
            mouse.click(Button.left)

            # 等待0.2秒以防过快出错
            time.sleep(0.2)

    # 启动线程
    t = threading.Thread(target=clicking_thread)
    t.start()

# 显示界面
count_label = tk.Label(root, text='Click Count:')
count_label.pack(pady=5)

count_entry = tk.Entry(root, textvariable=count)
count_entry.pack(pady=5)

start_button = tk.Button(root, text='Start', command=start_clicking)
start_button.pack(pady=10)

root.mainloop()