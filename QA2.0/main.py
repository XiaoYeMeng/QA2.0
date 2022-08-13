import tkinter as tk
import dict as dt
from tkinter import messagebox

window = tk.Tk()
window.title('選擇題')
window.geometry('600x600')

i = 0


# 座標
def ready_to_start():
    # 檢查 et_name 是否為int
    try:
        int(et_name.get())
    except ValueError:
        messagebox.showerror('error', '請輸入學號')
    else:
        # Label 學號座標
        lb_name.place(x=200, y=0)
        # Label 題號標題座標
        lb_number_title.place(x=100, y=50)
        # Label 題號座標
        lb_number.place(x=200, y=50)
        # Label 秒數標題座標
        lb_count_title.place(x=300, y=50)
        # Label 秒數座標
        lb_count.place(x=450, y=50)
        # Label 題目標題座標
        lb_que_title.place(x=100, y=100)
        # Label 題目座標
        lb_que.place(x=200, y=100)
        # Label 答案 A 標題座標
        lb_a_title.place(x=110, y=206)
        # Label 答案 A 座標
        bt_a.place(x=200, y=200)
        # Label 答案 B 標題座標
        lb_b_title.place(x=110, y=256)
        # Label 答案 B 座標
        bt_b.place(x=200, y=250)
        # Label 答案 C 標題座標
        lb_c_title.place(x=110, y=306)
        # Label 答案 C 座標
        bt_c.place(x=200, y=300)
        # Label 答案 D 標題座標
        lb_d_title.place(x=110, y=356)
        # Label 答案 D 標題
        bt_d.place(x=200, y=350)
        # Button 開始座標
        bt_start.place(x=200, y=450)
        # Button 重新開始座標
        bt_ui_update.place(x=200, y=500)
        # Label 分數標題座標
        lb_point_title.place(x=100, y=150)
        # Label 分數座標
        lb_point.place(x=200, y=150)
        # Label 答案結果座標
        lb_point_result.place(x=200, y=400)
        # Button 隱藏準備考試座標
        bt_ready_to_start.place_forget()
        # Label 得到考生學號
        lb_name['text'] = et_name.get()


# 解除鎖定答案按鈕
def normal():
    bt_a['state'] = tk.NORMAL
    bt_b['state'] = tk.NORMAL
    bt_c['state'] = tk.NORMAL
    bt_d['state'] = tk.NORMAL


# 鎖定答案按鈕
def disable():
    bt_a['state'] = tk.DISABLED
    bt_b['state'] = tk.DISABLED
    bt_c['state'] = tk.DISABLED
    bt_d['state'] = tk.DISABLED


# show題目
def topic():
    global i
    if lb_number['text'] == 10:
        lb_number['text'] = ''
        lb_que['text'] = ''
        bt_a['text'] = 'A'
        bt_b['text'] = 'B'
        bt_c['text'] = 'C'
        bt_d['text'] = 'D'
        lb_point_result['text'] = '做題結束 , 總分為 ' + str(lb_point['text'])
        disable()
    else:
        lb_que['text'] = dt.topic_random[i]['topic_que']
        bt_a['text'] = dt.topic_random[i]['topic_a']
        bt_b['text'] = dt.topic_random[i]['topic_b']
        bt_c['text'] = dt.topic_random[i]['topic_c']
        bt_d['text'] = dt.topic_random[i]['topic_d']
        i += 1
        lb_number['text'] = i
        lb_count['text'] = 10


# 倒數做題秒數
def countdown():
    print('count')
    if lb_number['text'] == '':
        lb_count['text'] = ''

    elif lb_count['text'] > 0:
        lb_count['text'] -= 1
        window.after(1000, countdown)

    elif lb_count['text'] == 0:
        lb_point_result['text'] = '時間到 , 分數 -5 '
        topic()
        window.after(1000, countdown)


# 開始
def start():
    normal()
    topic()
    countdown()
    bt_start.place_forget()


# 檢查答案
def check(r):
    if r == dt.topic_random[i-1]['topic_ans']:
        lb_point_result['text'] = '答對 , 分數 +10 '
        lb_point['text'] += 10
        topic()
    else:
        lb_point_result['text'] = '答錯 , 分數 -5 '
        lb_point['text'] -= 5
        topic()


# Label 學號標題
lb_name_title = tk.Label(window, text='學號 : ', font=('Time new roman', 18))
# Entry 輸入學號
et_name = tk.Entry(window, width=9, font=('Time new roman', 18))
# Label 學號
lb_name = tk.Label(window, text='', width=9, font=('Time new roman', 18))
# Label 題號標題
lb_number_title = tk.Label(window, text='題號 : ', font=('Time new roman', 18))
# Label 題號
lb_number = tk.Label(window, text='', font=('Time new roman', 18))
# Label 秒數標題
lb_count_title = tk.Label(window, text='剩餘秒數 : ', font=('Time new roman', 18))
# Label 秒數
lb_count = tk.Label(window, text='', font=('Time new roman', 18))
# Label 題目標題
lb_que_title = tk.Label(window, text='題目 : ', font=('Time new roman', 18))
# Label 題目
lb_que = tk.Label(window, text='', width=18, font=('Time new roman', 18))
# Label 答案 A 標題
lb_a_title = tk.Label(window, text='(A)', font=('Time new roman', 18))
# Button 答案 A
bt_a = tk.Button(window, text='A', width=9, command=lambda: check(bt_a['text']), font=('Time new roman', 18))
# Label 答案 B 標題
lb_b_title = tk.Label(window, text='(B)', font=('Time new roman', 18))
# Button 答案 B
bt_b = tk.Button(window, text='B', width=9, command=lambda: check(bt_b['text']), font=('Time new roman', 18))
# Label 答案 C 標題
lb_c_title = tk.Label(window, text='(C)', font=('Time new roman', 18))
# Button 答案 C
bt_c = tk.Button(window, text='C', command=lambda: check(bt_c['text']), width=9, font=('Time new roman', 18))
# Label 答案 D 標題
lb_d_title = tk.Label(window, text='(D)', font=('Time new roman', 18))
# Button 答案 D
bt_d = tk.Button(window, text='D', width=9, command=lambda: check(bt_d['text']), font=('Time new roman', 18))
# Button 開始
bt_start = tk.Button(window, text='start', width=9, command=start, font=('Time new roman', 18))
# Button 重新開始
bt_ui_update = tk.Button(window, text='restart', width=9, font=('Time new roman', 18))
# Button 準備考試
bt_ready_to_start = tk.Button(window, text='準備考試', width=9, command=ready_to_start, font=('Time new roman', 18))
# Label 分數標題
lb_point_title = tk.Label(window, text='分數 : ', font=('Time new roman', 18))
# Label 分數
lb_point = tk.Label(window, text=0, font=('Time new roman', 18))
# Label 答案結果
lb_point_result = tk.Label(window, text='', font=('Time new roman', 18))

# Label 學號標題座標
lb_name_title.place(x=100, y=0)
# Entry 輸入學號座標
et_name.place(x=200, y=0)
# Button 準備考試座標
bt_ready_to_start.place(x=200, y=400)

# 未開始前鎖定答案按鈕
bt_a['state'] = tk.DISABLED
bt_b['state'] = tk.DISABLED
bt_c['state'] = tk.DISABLED
bt_d['state'] = tk.DISABLED

window.mainloop()
