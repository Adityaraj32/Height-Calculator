from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Height Calculator")
root.geometry("455x995")

def GetHie():
    if PGender.get() == "Male" or PGender.get() == "male":
        if presentAge.get() == 13 :
            FinHie = presentHieght.get()/88 * 100
        elif presentAge.get() == 8 :
            FinHie = presentHieght.get()/75 * 100
        elif presentAge.get() == 9 :
            FinHie = presentHieght.get()/75 * 100
        elif presentAge.get() == 10 :
            FinHie = presentHieght.get()/78 * 100
        elif presentAge.get() == 11 :
            FinHie = presentHieght.get()/81 * 100
        elif presentAge.get() == 12 :
            FinHie = presentHieght.get()/84 * 100
        elif presentAge.get() == 14 :
            FinHie = presentHieght.get()/92 * 100
        elif presentAge.get() == 15 :
            FinHie = presentHieght.get()/95 * 100
        elif presentAge.get() == 16 :
            FinHie = presentHieght.get()/98 * 100
        elif presentAge.get() == 17 :
            FinHie = presentHieght.get()/99 * 100
        elif presentAge.get() == 18 :
            FinHie = presentHieght.get()/100 * 100
        tkinter.showinfo("Your Height",f"Your Maximum Height is {FinHie}") 
    elif PGender.get() == "Female" or PGender.get() == "female":
        if presentAge.get() == 8 :
            FinHie = presentHieght.get()/77 * 100
        elif presentAge.get() == 9 :
            FinHie = presentHieght.get()/81 * 100
        elif presentAge.get() == 10 :
            FinHie = presentHieght.get()/84 * 100
        elif presentAge.get() == 11 :
            FinHie = presentHieght.get()/88 * 100
        elif presentAge.get() == 12 :
            FinHie = presentHieght.get()/91 * 100
        elif presentAge.get() == 13 :
            FinHie = presentHieght.get()/95 * 100
        elif presentAge.get() == 14 :
            FinHie = presentHieght.get()/98 * 100
        elif presentAge.get() == 15 :
            FinHie = presentHieght.get()/99 * 100
        elif presentAge.get() == 16 :
            FinHie = presentHieght.get()/99.5 * 100
        elif presentAge.get() == 17 :
            FinHie = presentHieght.get()/100 * 100
        elif presentAge.get() == 18 :
            FinHie = presentHieght/100 * 100
        tkinter.showinfo("Your Height",f"Your Maximum Height is {FinHie}") 

Label1 = Label(root, text = "Enter Your Gender")
Label1.grid()
Label1 = Label(root, text = "Enter Your Present Hieght")
Label1.grid()
Label2 = Label(root, text = "Enter Your Present Age")
Label2.grid()

PGender = StringVar()
presentHieght = IntVar()
presentAge = IntVar()
Gender = Entry(root, textvariable = PGender)
Gender.grid(row = 0, column = 1)
PreHie = Entry(root, textvariable = presentHieght)
PreHie.grid(row = 1, column = 1)
PreAge = Entry(root, textvariable = presentAge)
PreAge.grid(row = 2, column = 1)

Button(text = "Submit", command=GetHie).grid()

root.mainloop()
