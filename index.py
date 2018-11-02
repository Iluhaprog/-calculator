from tkinter import *

window = Tk()
window.title("Калькулятор")
window.minsize(212, 300)

str_var = StringVar()
str_var2 = StringVar()

text_field = Entry(width=210, font="Arial 10", bg="#fff", 
                   textvariable=str_var, foreground="#000")
text_field.place(x=1.5, y=1.5)

text_field2 = Entry(width=210, font="Arial 10", bg="#fff", 
                   textvariable=str_var2, foreground="#000")
text_field2.place(x=1.5, y=23.5)

# COMMANDS FOR BUTTONS
# 0
def null():
    st = text_field.get() + "0"
    str_var.set(st)
# 1
def one():
    st = text_field.get() + "1"
    str_var.set(st)
# 2
def two():
    st = text_field.get() + "2"
    str_var.set(st)
# 3
def three():
    st = text_field.get() + "3"
    str_var.set(st)
# 4
def four():
    st = text_field.get() + "4"
    str_var.set(st)
# 5
def five():
    st = text_field.get() + "5"
    str_var.set(st)
# 6
def six():
    st = text_field.get() + "6"
    str_var.set(st)
# 7
def seven():
    st = text_field.get() + "7"
    str_var.set(st)
# 8
def eight():
    st = text_field.get() + "8"
    str_var.set(st)
# 9
def nine():
    st = text_field.get() + "9"
    str_var.set(st)
# plus
def plus():
    st = text_field.get() + "+"
    str_var.set(st)
# minus
def minus():
    st = text_field.get() + "-"
    str_var.set(st)
# multiply
def multiply():
    st = text_field.get() + "*"
    str_var.set(st)
# divide
def divide():
    st = text_field.get() + "/"
    str_var.set(st)
    
# answer or equals
def equals():
    st = text_field.get() + " "
    str_var.set(st)
    text=list(text_field.get())
    numbers = []
    actions = []
    number = ""

    for i in text:
        if ((i != "/") and (i != "+") and (i != "-") 
                      and (i != "*") and (i != " ")):
            number += i
        else:
            actions.append(str(i))
            numbers.append(int(number))
            number = ""
    answer = 0
    len_actions = len(actions)

    i = 0
    while i < len_actions:
        if actions[i] == "*":
            print(i)
            answer = numbers[i] * numbers[i + 1]
            numbers.remove(numbers[i])
            numbers.remove(numbers[i])
            numbers.insert(0, answer)
            actions.remove(actions[i])
            len_actions -= 1 
            i -= 1
        elif actions[i] == "/":
            print(i)
            answer = numbers[i] / numbers[i + 1]
            numbers.remove(numbers[i])
            numbers.remove(numbers[i])
            numbers.insert(0, answer)
            actions.remove(actions[i])
            len_actions -= 1 
            i -= 1
        print(*actions)
        print(*numbers)
        i += 1

    j = 0
    while j < len_actions:

        if actions[j] == "+":
            print(j)
            answer = numbers[j] + numbers[j + 1]
            numbers.remove(numbers[j])
            numbers.remove(numbers[j])
            numbers.insert(0, answer)
            actions.remove(actions[j])
            len_actions -= 1 
            j -= 1
        elif actions[j] == "-":
            print(j)
            answer = numbers[j] - numbers[j + 1]
            numbers.remove(numbers[j])
            numbers.remove(numbers[j])
            numbers.insert(0, answer)
            actions.remove(actions[j])
            len_actions -= 1 
            j -= 1

        print(*actions)
        print(*numbers)
        j += 1
            

    
    str_var2.set(answer)

# BUTTONS
# 0
button0 = Button(width=10, text="0", command=null)
button0.place(x=1.5, y=140)
# equals
button1 = Button(width=3, text="=", command=equals)
button1.place(x=110, y=140)
# divide
button1 = Button(width=3, text="/", command=divide)
button1.place(x=161, y=140)
# 1
button1 = Button(width=3, text="1", command=one)
button1.place(x=1.5, y=110)
# 2
button2 = Button(width=3, text="2", command=two)
button2.place(x=58, y=110)
# 3
button3 = Button(width=3, text="3", command=three)
button3.place(x=110, y=110)
# multiply
button_multiply = Button(width=3, text="*", command=multiply)
button_multiply.place(x=161, y=110)
# 4
button4 = Button(width=3, text="4", command=four)
button4.place(x=1.5, y=79.5)
# 5
button5 = Button(width=3, text="5", command=five)
button5.place(x=58, y=79.5)
# 6
button6 = Button(width=3, text="6", command=six)
button6.place(x=110, y=79.5)
# minus
button_minus = Button(width=3, text="-", command=minus)
button_minus.place(x=161, y=79.5)
# 7
button7 = Button(width=3, text="7", command=seven)
button7.place(x=1.5, y=50.5)
# 8
button8 = Button(width=3, text="8", command=eight)
button8.place(x=58, y=50.5)
# 9
button9 = Button(width=3, text="9", command=nine)
button9.place(x=110, y=50.5)
# plus
button_plus = Button(width=3, text="+", command=plus)
button_plus.place(x=161, y=50.5)

window.mainloop()