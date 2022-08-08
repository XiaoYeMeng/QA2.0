import tkinter as tk
import dict as dt

window = tk.Tk()
window.title('選擇題')
window.geometry('600x500')


def start():
    # 名字位置
    lb_name_title = tk.Label(window, text='考生 : ', font=('Time new roman', 18))
    lb_name_title.place(x=100, y=0)
    lb_name = tk.Label(window, text=et_name.get(), width=18, font=('Time new roman', 18))
    lb_name.place(x=200, y=0)
    # 題號位置
    lb_number_title = tk.Label(window, text='題號 : ', font=('Time new roman', 18))
    lb_number_title.place(x=100, y=50)
    lb_number = tk.Label(window, text='', font=('Time new roman', 18))
    lb_number.place(x=200, y=50)
    # 秒數位置
    lb_count = tk.Label(window, text='剩餘秒數 : ', font=('Time new roman', 18))
    lb_count.place(x=300, y=50)
    lb_sec = tk.Label(window, text=int(10), font=('Time new roman', 18))
    lb_sec.place(x=450, y=50)
    # 題目位置
    lb_que_title = tk.Label(window, text='題目 : ', font=('Time new roman', 18))
    lb_que_title.place(x=100, y=100)
    lb_que = tk.Label(window, text='', width=18, font=('Time new roman', 18))
    lb_que.place(x=200, y=100)
    # 答案 A 位置
    lb_a_title = tk.Label(window, text='(A)', font=('Time new roman', 18))
    lb_a_title.place(x=110, y=156)
    bt_a = tk.Button(window, text='A', width=9, font=('Time new roman', 18))
    bt_a.place(x=200, y=150)
    # 答案 B 位置
    lb_b_title = tk.Label(window, text='(B)', font=('Time new roman', 18))
    lb_b_title.place(x=110, y=206)
    bt_b = tk.Button(window, text='B', width=9, font=('Time new roman', 18))
    bt_b.place(x=200, y=200)
    # 答案 C 位置
    lb_c_title = tk.Label(window, text='(C)', font=('Time new roman', 18))
    lb_c_title.place(x=110, y=256)
    bt_c = tk.Button(window, text='C', width=9, font=('Time new roman', 18))
    bt_c.place(x=200, y=250)
    # 答案 D 位置
    lb_d_title = tk.Label(window, text='(D)', font=('Time new roman', 18))
    lb_d_title.place(x=110, y=306)
    bt_d = tk.Button(window, text='D', width=9, font=('Time new roman', 18))
    bt_d.place(x=200, y=300)
    # 重新開始位置
    bt_ui_update = tk.Button(window, text='restart', width=9, font=('Time new roman', 18))
    bt_ui_update.place(x=200, y=450)
    # 隱藏 start 位置
    bt_start.place_forget()


et_name = tk.Entry(window, width=18, font=('Time new roman', 18))
et_name.place(x=200, y=0)
bt_start = tk.Button(window, text='start', width=9, command=start, font=('Time new roman', 18))
bt_start.place(x=200, y=400)

window.mainloop()
