import tkinter as tk #GUI(Graphical User Interface)の作成

h_gamen = tk.Tk()
h_gamen.title("calculator")
h_hyouji = tk.Label(h_gamen, fg="red", bg="yellow") #これだけでは、ラベルがどこに配置するかの指示がない！
h_hyouji.grid(row=0, column=0, columnspan=3, sticky=tk.W) #grid()によって、0行目0列目に表示の支持を与える, columnspanによって幅を決定, stickyで寄せ
def Num_hyouji(h_event):
    h_num_button = h_event.widget.cget("text")
    h_keta_hyouji = h_hyouji.cget("text") # 現在表示されている（複数桁の）数値を再取得、下のコードで新たに起きたイベントを後ろにくっつける
    h_hyouji["text"] = h_keta_hyouji + h_num_button #これらの変数はtextとして取得されている→足し算ではなくテキストの追加　ex. a = "1", b = "2", print(a+b)

def all_clear(h_event):
    h_hyouji["text"] = ""

def calculate(h_event):
    try:
        h_keisan = h_hyouji.cget("text")
        h_hyouji["text"] = str(eval(h_keisan))
    except:
        h_hyouji["text"] = "ERROR!"

for j in range(3):
    for i in range(3):
        h_button = tk.Button(h_gamen, text=str(7+i-3*j), width=10) #電卓において、同じコードを作って他の数字ボタンを作るのは長くなる→for文を使う
        h_button.grid(row=j+1, column=i)
        h_button.bind("<ButtonPress>", Num_hyouji)

h_button = tk.Button(h_gamen, text="0")
h_button.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E) #W+Eで左右いっぱい
h_button.bind("<ButtonPress>", Num_hyouji)

h_button = tk.Button(h_gamen, text=".", width=10)
h_button.grid(row=4, column=2,)
h_button.bind("<ButtonPress>", Num_hyouji)

h_enzanshi = ["+", "-", "*", "/"]
for i in range(len(h_enzanshi)): #lenは繰り返し実行、今回は演算子が4種類→o、1、2、3
    h_button = tk.Button(h_gamen, text=h_enzanshi[i], width=5)
    h_button.grid(row=1+i, column=3)
    h_button.bind("<ButtonPress>", Num_hyouji)


h_button = tk.Button(h_gamen, text="All Clear")
h_button.grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E)
h_button.bind("<ButtonPress>", all_clear)

h_button = tk.Button(h_gamen, text="=", width=5)
h_button.grid(row=5, column=3)
h_button.bind("<ButtonPress>", calculate)

h_gamen.mainloop() #ループさせないと、一瞬現れた後のウィンドウが維持されない