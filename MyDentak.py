import tkinter as tk #GUI(Graphical User Interface)の作成

# 電卓の表示形式
h_gamen = tk.Tk()
h_gamen.title("calculator")
h_hyouji = tk.Label(h_gamen, fg="red", bg="yellow") 
h_hyouji.grid(row=0, column=0, columnspan=3, sticky=tk.W)
def Num_hyouji(h_event):
    h_num_button = h_event.widget.cget("text")
    h_keta_hyouji = h_hyouji.cget("text") 
    h_hyouji["text"] = h_keta_hyouji + h_num_button

# リセットボタンの動作
def all_clear(h_event):
    h_hyouji["text"] = ""

# 例外処理
def calculate(h_event):
    try:
        h_keisan = h_hyouji.cget("text")
        h_hyouji["text"] = str(eval(h_keisan))
    except:
        h_hyouji["text"] = "ERROR!"

# 数字、小数点ボタンの設定
for j in range(3):
    for i in range(3):
        h_button = tk.Button(h_gamen, text=str(7+i-3*j), width=10)
        h_button.grid(row=j+1, column=i)
        h_button.bind("<ButtonPress>", Num_hyouji)

h_button = tk.Button(h_gamen, text="0")
h_button.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E) #W+Eで左右いっぱい
h_button.bind("<ButtonPress>", Num_hyouji)

h_button = tk.Button(h_gamen, text=".", width=10)
h_button.grid(row=4, column=2,)
h_button.bind("<ButtonPress>", Num_hyouji)

# 演算子ボタンの設定
h_enzanshi = ["+", "-", "*", "/"]
for i in range(len(h_enzanshi)):
    h_button = tk.Button(h_gamen, text=h_enzanshi[i], width=5)
    h_button.grid(row=1+i, column=3)
    h_button.bind("<ButtonPress>", Num_hyouji)

h_button = tk.Button(h_gamen, text="=", width=5)
h_button.grid(row=5, column=3)
h_button.bind("<ButtonPress>", calculate)

# リセットボタンの設定
h_button = tk.Button(h_gamen, text="All Clear")
h_button.grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E)
h_button.bind("<ButtonPress>", all_clear)

h_gamen.mainloop()
