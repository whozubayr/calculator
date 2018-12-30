from Tkinter import *

global var
var = '0'
def print0():
   global var
   if var == '0':
      var = '0'
   else:
      var += '0'
   num1.set(var)

def print1():
   global var
   if var == '0':
      var = '1'
   else:
      var += '1'
   num1.set(var)

def print2():
   global var
   if var == '0':
      var = '2'
   else:
      var += '2'
   num1.set(var)


def print3():
   global var
   if var == '0':
      var = '3'
   else:
      var += '3'
   num1.set(var)

def print4():
   global var
   if var == '0':
      var = '4'
   else:
      var += '4'
   num1.set(var)

def print5():
   global var
   if var == '0':
      var = '5'
   else:
      var += '5'
   num1.set(var)




def print6():
   global var
   if var == '0':
      var = '6'
   else:
      var += '6'
   num1.set(var)

def print7():
   global var
   if var == '0':
      var = '7'
   else:
      var += '7'
   num1.set(var)

def print8():
   global var
   if var == '0':
      var = '8'
   else:
      var += '8'
   num1.set(var)


def print9():
   global var
   if var == '0':
      var = '9'
   else:
      var += '9'
   num1.set(var)

def printp():
   global var
   if var == '0':
      var = '+'
   else:
      var += '+'
   num1.set(var)

def printmi():
   global var
   if var == '0':
      var = '-'
   else:
      var += '-'
   num1.set(var)

def printd():
   global var
   if var == '0':
      var = '/'
   else:
      var += '/'
   num1.set(var)

def printm():
   global var
   if var == '0':
      var = '*'
   else:
      var += '*'
   num1.set(var)

def clear():
   txtDisplay.delete(0,END)
   global var
   var = '0'
   return 
def equal():
   global var
   var = eval(var)
   var = str(var)
   num1.set(var)
   var = '0'
   

root = Tk()
root.resizable(0, 0)

frame = Frame(root)
frame.pack()
root.title('CALCULATOR')

num1 = StringVar()
topframe = Frame(root)
topframe.pack(side = TOP)

txtDisplay = Entry(frame,textvariable=num1,justify=RIGHT,bd=20,insertwidth=1,font = 30)
txtDisplay.pack(side = TOP)

button1 = Button(topframe,padx = 16,pady =16,bd = 8,text='1',fg='black',command=print1)
button1.pack(side = LEFT)

button2 = Button(topframe,padx = 16,pady =16,bd = 8,text='2',fg='black',command=print2)
button2.pack(side = LEFT)

button3 = Button(topframe,padx = 16,pady =16,bd = 8,text='3',fg='black',command=print3)
button3.pack(side = LEFT)

button4 = Button(topframe,padx = 16,pady =16,bd = 8,text='4',fg='black',command=print4)
button4.pack(side = LEFT)

frame1 = Frame(root)
frame1.pack(side = TOP)

button1 = Button(frame1,padx = 16,pady =16,bd = 8,text='5',fg='black',command=print5)
button1.pack(side = LEFT)

button2 = Button(frame1,padx = 16,pady =16,bd = 8,text='6',fg='black',command=print6)
button2.pack(side = LEFT)

button3 = Button(frame1,padx = 16,pady =16,bd = 8,text='7',fg='black',command=print7)
button3.pack(side = LEFT)

button4 = Button(frame1,padx = 16,pady =16,bd = 8,text='8',fg='black',command=print8)
button4.pack(side = LEFT)


frame2 = Frame(root)
frame2.pack(side = TOP)

button1 = Button(frame2,padx = 16,pady =16,bd = 8,text='9',fg='black',command=print9)
button1.pack(side = LEFT)

button2 = Button(frame2,padx = 16,pady =16,bd = 8,text='0',fg='black',command=print0)
button2.pack(side = LEFT)

button3 = Button(frame2,padx = 16,pady =16,bd = 8,text='+',fg='black',command=printp)
button3.pack(side = LEFT)

button4 = Button(frame2,padx = 16,pady =16,bd = 8,text='-',fg='black',command=printmi)
button4.pack(side = LEFT)

frame3 = Frame(root)
frame3.pack(side = TOP)

button1 = Button(frame3,padx = 16,pady =16,bd = 8,text='C',fg='black',command = clear)
button1.pack(side = LEFT)

button2 = Button(frame3,padx = 16,pady =16,bd = 8,text='*',fg='black',command=printm)
button2.pack(side = LEFT)

button3 = Button(frame3,padx = 16,pady =16,bd = 8,text='/',fg='black',command=printd)
button3.pack(side = LEFT)

button4 = Button(frame3,padx = 16,pady =16,bd = 8,text='=',fg='black',command=equal)
button4.pack(side = LEFT)

root.mainloop( )

