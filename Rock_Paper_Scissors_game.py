# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------
#install this

#pip install tkinter
#pip install termcolor
#pip install pyfiglet
from tkinter import *
from random import choice
import os
import termcolor
import pyfiglet
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def main():
  #create windows
  root = Tk()
  #title windows
  root.title("Stone Paper Scissors")
  root.geometry("860x500+300+130")
  root.config(background="#bdbdbd")
  root.resizable(False,False)
  root.iconbitmap("game.ico")
  #اعدادت اللعبه

  def Robot_choice(car):
      if  car == "stone":
          bun_Stone_Robot.place(x=500,y=200)
          vs = Label(root,text="VS",font=('Courier', 25),bg="#bdbdbd")
          vs.place(x=440,y=200)

      elif car == "paper":
          bun_Paper_Robot.place(x=500,y=200)
          vs = Label(root,text="VS",font=('Courier', 25),bg="#bdbdbd")
          vs.place(x=440,y=200)
      elif car == "scissors":
          vs = Label(root,text="VS",font=('Courier', 25),bg="#bdbdbd")
          vs.place(x=440,y=200)
          bun_Scissors_Robot.place(x=500,y=200)

  def get_stone():
    
    def Repeat_Game():
      #اعادة الازار المستخدم
      bun_Stone.place(x=70,y=200)
      bun_Scissors.place(x=70,y=300)
      bun_Paper.place(x=70,y=400)
      #اعادة الازار الكمبيوتر
      bun_Stone_Robot.place(x=700,y=200)
      bun_Scissors_Robot.place(x=700,y=300)
      bun_Paper_Robot.place(x=700,y=400)
      tail.place(x=300,y=10000)
      bun_repeat.place(x=400,y=10000)

    bun_repeat =Button(root,text="اعادة اللعبه",bg="Grey",fg="white",width=14,font=('Courier', 15),height=2,command=Repeat_Game)
    bun_repeat.place(x=350,y=430)
    operation = ["stone", "paper", "scissors"]
    computer = choice(operation)
    bun_Stone.place(x=300,y=200)
    if "stone" == computer:
      Robot_choice(computer)
      tail = Label(root,text="انه تعادل",bg="#bdbdbd",fg="Black",font=('Courier', 35))
      tail.place(x=300,y=300)
    elif computer == "scissors":
      Robot_choice(computer)
      tail = Label(root,text="مبروك لقد فزت بالعبه",bg="#bdbdbd",fg="Black",font=('Courier', 20))
      tail.place(x=300,y=300)
    else:
      Robot_choice(computer)
      tail = Label(root,text="للاسف لقد خسرت اللعبه",bg="#bdbdbd",fg="Black",font=('Courier', 20))
      tail.place(x=300,y=300)

  def get_paper():

    def Repeat_Game():
      #اعادة الازار المستخدم
      bun_Stone.place(x=70,y=200)
      bun_Scissors.place(x=70,y=300)
      bun_Paper.place(x=70,y=400)
      #اعادة الازار الكمبيوتر
      bun_Stone_Robot.place(x=700,y=200)
      bun_Scissors_Robot.place(x=700,y=300)
      bun_Paper_Robot.place(x=700,y=400)
      tail.place(x=300,y=10000)
      bun_repeat.place(x=400,y=10000)

    bun_repeat =Button(root,text="اعادة اللعبه",bg="Grey",fg="white",width=14,font=('Courier', 15),height=2,command=Repeat_Game)
    bun_repeat.place(x=350,y=430)

    operation = ["stone", "paper", "scissors"]
    computer = choice(operation)
    bun_Paper.place(x=300,y=200)
    if "paper" == computer:
      Robot_choice(computer)
      tail = Label(root,text="انه تعادل",bg="#bdbdbd",fg="Black",font=('Courier', 35))
      tail.place(x=300,y=300)
    elif computer == "stone":
      Robot_choice(computer)
      tail = Label(root,text="مبروك لقد فزت بالعبه",bg="#bdbdbd",fg="Black",font=('Courier', 20))
      tail.place(x=300,y=300)
    else:
      Robot_choice(computer)
      tail = Label(root,text="للاسف لقد خسرت اللعبه",bg="#bdbdbd",fg="Black",font=('Courier', 20))
      tail.place(x=300,y=300)

  def get_scissors():

    def Repeat_Game():
      #اعادة الازار المستخدم
      bun_Stone.place(x=70,y=200)
      bun_Scissors.place(x=70,y=300)
      bun_Paper.place(x=70,y=400)
      #اعادة الازار الكمبيوتر
      bun_Stone_Robot.place(x=700,y=200)
      bun_Scissors_Robot.place(x=700,y=300)
      bun_Paper_Robot.place(x=700,y=400)
      tail.place(x=300,y=10000)
      bun_repeat.place(x=400,y=10000)

    bun_repeat =Button(root,text="اعادة اللعبه",bg="Grey",fg="white",width=14,font=('Courier', 15),height=2,command=Repeat_Game)
    bun_repeat.place(x=350,y=430)

    operation = ["stone", "paper", "scissors"]
    computer = choice(operation)
    bun_Scissors.place(x=300,y=200)
    if "scissors" == computer:
      Robot_choice(computer)
      tail = Label(root,text="انه تعادل",bg="#bdbdbd",fg="Black",font=('Courier', 35))
      tail.place(x=300,y=300)
    elif computer == "paper":
      Robot_choice(computer)
      tail = Label(root,text=" مبروك لقد فزت بالعبه",bg="#bdbdbd",fg="Black",font=('Courier', 20))
      tail.place(x=300,y=300)
    else:
      Robot_choice(computer)
      tail = Label(root,text="للاسف لقد خسرت اللعبه",bg="#bdbdbd",fg="Black",font=('Courier', 20))
      tail.place(x=300,y=300)


  game = Label(root,text="لعبه حجر ورق مقص",font=('Courier', 35),bg="#bdbdbd")
  game.pack()
  #اعدادات المستخدم
  you = Label(root,text=  ":  اختر انت اولا",font=('Courier', 25),bg="#bdbdbd")
  you.place(x=70,y=100)
  bun_Stone =Button(root,text="حجر",bg="Grey",fg="white",width=10,font=('Courier', 15),height=2,command=get_stone)
  bun_Stone.place(x=70,y=200)
  bun_Scissors =Button(root,text="مقص",bg="Grey",fg="white",width=10,font=('Courier', 15),height=2,command=get_scissors)
  bun_Scissors.place(x=70,y=300)
  bun_Paper =Button(root,text="ورق",bg="Grey",fg="white",width=10,font=('Courier', 15),height=2,command=get_paper)
  bun_Paper.place(x=70,y=400)
  #اعدادات الكمبيوتر
  Robot = Label(root,text=  ":  اختيار الحاسوب",font=('Courier', 25),bg="#bdbdbd")
  Robot.place(x=500,y=100)
  bun_Stone_Robot =Label(root,text="حجر",bg="Red",fg="white",width=10,font=('Courier', 15),height=2)
  bun_Stone_Robot.place(x=700,y=200)
  bun_Scissors_Robot =Label(root,text="مقص",bg="Red",fg="white",width=10,font=('Courier', 15),height=2)
  bun_Scissors_Robot.place(x=700,y=300)
  bun_Paper_Robot =Label(root,text="ورق",bg="Red",fg="white",width=10,font=('Courier', 15),height=2)
  bun_Paper_Robot.place(x=700,y=400)

  mainloop()

print(termcolor.colored(pyfiglet.figlet_format("@ddos_attack_co"), color="red"))

print(" Go to my Instagram account < @ddos_attack_co > and Fallowed Me \n Enter...", end="")
enter = input("")

main()
