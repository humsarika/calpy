from tkinter import *
root = Tk()
root.title("Calpy")
e1=Entry(root,width=16,justify="right",font="Arial 25",bd=7,bg="cadet blue")
e1.grid(row=0,column=0,columnspan=4)

def cal(button):
    e1.insert(16,button)

def result(r):
    e1.delete(0,END)
    e1.insert(16,r)

def button_C(e):
    e1.delete(0,END)

def button_D(e):
    txt=e1.get()[:-1]
    e1.delete (0,END)
    e1.insert(0,txt)

b7 = Button(root,text="7",command=lambda:cal("7"),width=5,height=2,font="Arial 16",bd=3)
b7.grid(row=1,column=0)
b8 = Button(root,text="8",command=lambda:cal("8"),width=5,height=2,font="Arial 16",bd=3)
b8.grid(row=1,column=1)
b9 = Button(root,text="9",command=lambda:cal("9"),width=5,height=2,font="Arial 16",bd=3)
b9.grid(row=1,column=2)
bC = Button(root,text="C",command=lambda:button_C(e1.get()),width=5,height=2,fg="red",font="Arial 16",bd=3)
bC.grid(row=1,column=3)

b4 = Button(root,text="4",command=lambda:cal("4"),width=5,height=2,font="Arial 16",bd=3)
b4.grid(row=2,column=0)
b5 = Button(root,text="5",command=lambda:cal("5"),width=5,height=2,font="Arial 16",bd=3)
b5.grid(row=2,column=1)
b6 = Button(root,text="6",command=lambda:cal("6"),width=5,height=2,font="Arial 16",bd=3)
b6.grid(row=2,column=2)
b_mul = Button(root,text="*",command=lambda:cal("*"),width=5,height=2,font="Arial 16",bd=3)
b_mul.grid(row=2,column=3)

b1 = Button(root,text="1",command=lambda:cal("1"),width=5,height=2,font="Arial 16",bd=3)
b1.grid(row=3,column=0)
b2 = Button(root,text="2",command=lambda:cal("2"),width=5,height=2,font="Arial 16",bd=3)
b2.grid(row=3,column=1)
b3 = Button(root,text="3",command=lambda:cal("3"),width=5,height=2,font="Arial 16",bd=3)
b3.grid(row=3,column=2)
b_add = Button(root,text="+",command=lambda:cal("+"),width=5,height=2,font="Arial 16",bd=3)
b_add.grid(row=3,column=3)
b_zero = Button(root,text=".",command=lambda:cal("."),width=5,height=2,font="Arial 16",bd=3)
b_zero.grid(row=4,column=0)
b_point = Button(root,text="0",command=lambda:cal("0"),width=5,height=2,font="Arial 16",bd=3)
b_point.grid(row=4,column=1)
b_sub = Button(root,text="-",command=lambda:cal("-"),width=5,height=2,font="Arial 16",bd=3)
b_sub.grid(row=4,column=2)
b_equal = Button(root,text="=",command=lambda:result(eval(e1.get())),width=5,height=2,fg="blue",font="Arial 16",bd=3)
b_equal.grid(row=4,column=3)
b_left_p = Button(root,text="(",command=lambda:cal("("),width=5,height=2,font="Arial 16",bd=3)
b_left_p.grid(row=5,column=0)
b_right_p = Button(root,text=")",command=lambda:cal(")"),width=5,height=2,font="Arial 16",bd=3)
b_right_p.grid(row=5,column=1)
b_modulo = Button(root,text="/",command=lambda:cal("/"),width=5,height=2,font="Arial 16",bd=3)
b_modulo.grid(row=5,column=2)
b_d = Button(root,text="D",command=lambda:button_D(e1.get()),width=5,height=2,fg="orange",font="Arial 16",bd=3)
b_d.grid(row=5,column=3)

root.mainloop()
