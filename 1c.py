import tkinter.filedialog
from tkinter import *
import tkinter.ttk as ttk
import operator
import random


operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


root = Tk()
root.title("Math Flash Cards")
root.geometry('1024x768')

msg = StringVar()
msg2= StringVar()
msg3= StringVar()
msg4= StringVar()

rightAnswer1 = IntVar()
rightAnswer2 = IntVar()
rightAnswer3 = IntVar()
rightAnswer4 = IntVar()


nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')
tab0 = Text(root)
tab1 = Text(root)
tab2 = Text(root)
tab3 = Text(root)
tab4 = Text(root)

nb.add(tab0, text='Welcome')
nb.add(tab1, text='Level 1')
nb.add(tab2, text='Level 2')
nb.add(tab3, text='Level 3')
nb.add(tab4, text='Level 4')

r1_oper = random.choice(list(operatorlookup))
r1a = random.randint(1,3)
r1b = random.randint(1,3)
msg.set(f'{r1a} {r1_oper} {r1b}')
rightAnswer1.set(eval(f'{r1a} {r1_oper} {r1b}'))

r2_oper = random.choice(list(operatorlookup))
r2a = random.randint(1,6)
r2b = random.randint(1,6)
msg2.set(f'{r2a} {r2_oper} {r2b}')
rightAnswer2.set(eval(f'{r2a} {r2_oper} {r2b}'))


r3_oper = random.choice(list(operatorlookup))
r3a = random.randint(1,9)
r3b = random.randint(1,9)
msg3.set(f'{r3a} {r3_oper} {r3b}')
rightAnswer3.set(eval(f'{r3a} {r3_oper} {r3b}'))

r4_oper = random.choice(list(operatorlookup))
r4a = random.randint(1,12)
r4b = random.randint(1,12)
msg4.set(f'{r4a} {r4_oper} {r4b}')
rightAnswer4.set(eval(f'{r4a} {r4_oper} {r4b}'))

 
# Create a Label
a = Label(tab1, text=msg, textvariable=msg).pack()

# Create an Entry widget
entry1 = Entry(tab1, width=25)
entry1.pack(pady=20)

#refresh():
def refresh1():
    tab1.counter = 0
    L1['text'] = 'Refreshed, Attempts: ' + str(0)
    r1_oper = random.choice(list(operatorlookup))
    r1a = random.randint(1,3)
    r1b = random.randint(1,3)
    rightAnswer1.set(eval(f'{r1a} {r1_oper} {r1b}'))
    a = Label(tab1, text=f'{r1a} {r1_oper} {r1b}').pack()
    
b2 = Button(tab1, text="New Problem", command=refresh1).pack()
   
tab1.counter = 0

def clicked1():
    if eval(entry1.get()) == int(rightAnswer1.get()):
      print1 = Label(tab1, text="Correct Answer!")
      print1.pack()
      tab1.counter = 0
      entry1.delete(0, END)

    else: 
        print1 = Label(tab1, text="Wrong Answer, please try again")
        print1.pack()
        entry1.delete(0, END)
    tab1.counter += 1
    L1['text'] = 'Attempts: ' + str(tab1.counter)

b1 = Button(tab1, text="Submit", command=clicked1)
b1.pack()

L1 = Label(tab1, text="No clicks yet.")
L1.pack()

# Create a Label
a2 = Label(tab2, text=msg2, textvariable=msg2).pack()

# Create an Entry widget
entry2 = Entry(tab2, width=25)
entry2.pack(pady=20)

#refresh():
def refresh2():
    tab2.counter = 0
    L2['text'] = 'Refreshed, Attempts: ' + str(0)
    r2_oper = random.choice(list(operatorlookup))
    r2a = random.randint(1,6)
    r2b = random.randint(1,6)
    msg2.set(f'{r2a} {r2_oper} {r2b}')
    rightAnswer2.set(eval(f'{r2a} {r2_oper} {r2b}'))
    a2 = Label(tab2, text=f'{r2a} {r2_oper} {r2b}').pack()
    
b3 = Button(tab2, text="New Problem", command=refresh2).pack()
   
tab2.counter = 0
print(((entry2.get())), type(rightAnswer2.get()))

def clicked2():
    if eval(entry2.get()) == int(rightAnswer2.get()):
      print2 = Label(tab2, text="Correct Answer!")
      print2.pack()
      tab2.counter = 0
      entry2.delete(0, END)

    else: 
        print2 = Label(tab2, text="Wrong Answer, please try again")
        print2.pack()
        entry2.delete(0, END)
    tab2.counter += 1
    L2['text'] = 'Attempts: ' + str(tab2.counter)

b4 = Button(tab2, text="Submit", command=clicked2)
b4.pack()

L2 = Label(tab2, text="No clicks yet.")
L2.pack()

# Create a Label%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Create a Label
a3 = Label(tab3, text=msg3, textvariable=msg3).pack()

# Create an Entry widget
entry3 = Entry(tab3, width=25)
entry3.pack(pady=20)

#refresh():
def refresh3():
    tab3.counter = 0
    L3['text'] = 'Refreshed, Attempts: ' + str(0)
    r3_oper = random.choice(list(operatorlookup))
    r3a = random.randint(1,9)
    r3b = random.randint(1,9)
    msg3.set(f'{r3a} {r3_oper} {r3b}')
    rightAnswer3.set(eval(f'{r3a} {r3_oper} {r3b}'))
    a3 = Label(tab3, text=f'{r3a} {r3_oper} {r3b}').pack()
    
b5 = Button(tab3, text="New Problem", command=refresh3).pack()
   
tab3.counter = 0

def clicked3():
    if eval(entry3.get()) == int(rightAnswer3.get()):
      print3 = Label(tab3, text="Correct Answer!")
      print3.pack()
      tab3.counter = 0
      entry3.delete(0, END)

    else: 
        print3 = Label(tab3, text="Wrong Answer, please try again")
        print3.pack()
        entry3.delete(0, END)
    tab3.counter += 1
    L3['text'] = 'Attempts: ' + str(tab3.counter)

b6 = Button(tab3, text="Submit", command=clicked3)
b6.pack()

L3 = Label(tab3, text="No clicks yet.")
L3.pack()

# Create a Label
a4 = Label(tab4, text=msg4, textvariable=msg4).pack()

# Create an Entry widget
entry4 = Entry(tab4, width=25)
entry4.pack(pady=20)

#refresh():
def refresh4():
    tab4.counter = 0
    L4['text'] = 'Refreshed, Attempts: ' + str(0)
    r4_oper = random.choice(list(operatorlookup))
    r4a = random.randint(1,12)
    r4b = random.randint(1,12)
    rightAnswer4.set(eval(f'{r4a} {r4_oper} {r4b}'))
    a4 = Label(tab4, text=f'{r4a} {r4_oper} {r4b}').pack()
    
b7 = Button(tab4, text="New Problem", command=refresh4).pack()
   
tab4.counter = 0

def clicked4():
    if eval(entry4.get()) == int(rightAnswer4.get()):
      print4 = Label(tab4, text="Correct Answer!")
      print4.pack()
      tab4.counter = 0
      entry4.delete(0, END)

    else: 
        print4 = Label(tab4, text="Wrong Answer, please try again")
        print4.pack()
        entry4.delete(0, END)
    tab4.counter += 1
    L4['text'] = 'Attempts: ' + str(tab4.counter)

b8 = Button(tab4, text="Submit", command=clicked4)
b8.pack()

L4 = Label(tab4, text="No clicks yet.")
L4.pack()

root.mainloop()
