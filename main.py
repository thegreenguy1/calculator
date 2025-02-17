import tkinter as tk
from functools import  partial

app = tk.Tk()
app.config(bg="#87CEEB")
app.title("Calculator")
app.geometry("300x300")


app.resizable(False,False)
icon = tk.PhotoImage(file="icon.png")
app.iconphoto(True,icon)

calculations = tk.StringVar()
calculations.set("")

input = tk.Entry(app,textvariable=calculations,font=("",15),bg="#007FFF",fg="#032B44")
input.place(x=15,y=0)
def changex_view():
    if len(calculations.get()) > 10:
        input.xview_moveto(1)

def calculate():
    try:
        calculations.set(eval(calculations.get()))
    except SyntaxError:
        if calculations.get() == "":
            ...
        else:
            calculations.set("Math Error")
    except ZeroDivisionError:
        calculations.set("Math Error")
    except NameError:
        calculations.set("")
    input.icursor(len(calculations.get()))
def show(num):
    calculations.set(calculations.get()+num)
def clear():
    calculations.set("")
def dele():
    calc = calculations.get()
    calc = [i for i in calc]

    try:
        calc.pop()
        calculations.set("".join(calc))
    except IndexError:
        ...

listofkeys = ["7","8","9","*","4","5","6","-","1","2","3","+","0",".","/"]

x= 0
y = 50
for i in listofkeys:
    button = tk.Button(text=f"{i}",bg="#4169e1",border=("5px","black"),command=partial(show,i),width=1,height=1,font=("Consolas",15),activebackground="#a1c1f2")
    if x> 150:
        x = 0
        y += 50
    x += 50
    button.place(x=x ,y=y)
    if i in ["*","/","+","-"]:
        button.config(fg="#eded65")
    if i == '0':
        x = 100
        button.place(x=x,y=y)

solve = tk.Button(text="=", bg="#4169e1", border=("5px", "black"), command=calculate,width=10)
solve.place(x=50, y=250)
cler =tk.Button(text="C",bg="#4169e1", border=("5px", "black"),width=1,height=1,font=("Consolas",15),activebackground="#a1c1f2")
cler.place(x=50,y=200)
delete = tk.Button(text="x",bg="#4169e1", border=("5px", "black"),width=5,command=dele,activebackground="#a1c1f2",fg="red")
delete.place(x=170,y=250)

if "__main__" == __name__:
    changex_view()
    app.mainloop()
