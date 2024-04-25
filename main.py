import tkinter as tk
from tkinter import Frame,LEFT,Entry
from tkinter import *

#insert entry
def insert_digit(digit):
    entry.insert(END,f"{digit}")
    
#clear entry
def clear_entry():
    entry.delete(0, tk.END)

#функция для выражений
def count_result():
    text = entry.get()
    result = 0

    if '+' in text:
        splitted_text = text.split('+')
        first = round(float(splitted_text[0]),2)
        second = round(float(splitted_text[1]),2)
        result = round((first + second),2)


    elif '-' in text:
        splitted_text = text.split('-')
        first = round(float(splitted_text[0]),2)
        second = round(float(splitted_text[1]),2)
        result = round((first - second),2)

    elif 'X' in text:
        splitted_text = text.split('X')
        first = round(float(splitted_text[0]),2)
        second = round(float(splitted_text[1]),2)
        result = round((first * second),2)

    elif '/' in text:
        splitted_text = text.split('/')
        first = round(float(splitted_text[0]),2)
        second = round(float(splitted_text[1]),2)
        result = round((first / second),2)
    else:
        result = text
    clear_entry()
    entry.insert(0,result)



#Окно
root = tk.Tk()
root.geometry("240x370")
root.config(bg='gray')
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack()



w = tk.Label(root,text="Calculator")
w.pack(side="top")



#поле ввода 
entry = tk.Entry(root)
entry.configure(font=("Courier",15))
entry.pack(ipadx=120,ipady=10)


#кнопки числа
button0 = tk.Button(root, text="0",command=lambda: insert_digit('0'))
button0.place(x=0,y=250,width=60,height=60)
button1 = tk.Button(root, text="1",command=lambda: insert_digit('1')).place(x=0,y=190,width=60,height=60)
button2 = tk.Button(root, text="2",command=lambda: insert_digit('2')).place(x=60,y=190,width=60,height=60)
button3 = tk.Button(root, text="3",command=lambda: insert_digit('3')).place(x=120,y=190,width=60,height=60)



button4 = tk.Button(root, text="4",command=lambda: insert_digit('4')).place(x=0,y=130,width=60,height=60)
button5 = tk.Button(root, text="5",command=lambda: insert_digit('5')).place(x=60,y=130,width=60,height=60)
button6 = tk.Button(root, text="6",command=lambda: insert_digit('6')).place(x=120,y=130,width=60,height=60)



button7 = tk.Button(root, text="7",command=lambda: insert_digit('7')).place(x=0,y=70,width=60,height=60)
button8 = tk.Button(root, text="8",command=lambda: insert_digit('8')).place(x=60,y=70,width=60,height=60)
button9 = tk.Button(root, text="9",command=lambda: insert_digit('9')).place(x=120,y=70,width=60,height=60)



#кнопки (спец символы)
button_comm = tk.Button(root, text=",",command=lambda: insert_digit('.')).place(x=60,y=250,width=60,height=60)
button_result = tk.Button(root, text="=",command=count_result).place(x=120,y=250,width=60,height=60)
button9 = tk.Button(root, text="+",command=lambda: insert_digit('+')).place(x=180,y=250,width=60,height=60)
button9 = tk.Button(root, text="-",command=lambda: insert_digit('-')).place(x=180,y=190,width=60,height=60)
button9 = tk.Button(root, text="X",command=lambda: insert_digit('X')).place(x=180,y=130,width=60,height=60)
button9 = tk.Button(root, text="/",command=lambda: insert_digit('/')).place(x=180,y=70,width=60,height=60)
button_clear = tk.Button(root, text="AC",command=clear_entry).place(x=0,y=310,width=240,height=60)



root.mainloop()
