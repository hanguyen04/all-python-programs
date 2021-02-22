from tkinter import*

def submit():
    print("Username",username.get())
    print("Firstname",firstname.get())
    print("Surname",surname.get())
def clear():
    username.delete(0,END)
    firstname.delete(0,END)
    surname.delete(0,END)
    username.focus_set()

root=Tk()
root.geometry("300x240")
root.title("Students Detail")
root.configure(background = "light blue")

#frame to contain the form heading
frame_heading = Frame(root)
frame_heading.grid(row=0,column=0,padx=30,pady=5)
#frame to contain the labels and user's entry 
frame_entry = Frame(root)
frame_entry.grid(row=1,column=0,padx=25,pady=10)

#place the form heading
Label(frame_heading, text = "student details form", font=('Arial',16))\
      .grid(row=0,column=0,padx=0,pady=5)

#place the labels
Label(frame_entry, text="username:")\
      .grid(row=0,column=0,padx=10,pady=5)
Label(frame_entry, text="firstname:")\
      .grid(row=1,column=0,padx=10,pady=10)
Label(frame_entry, text="lastname:")\
      .grid(row=2,column=0,padx=10,pady=10)

#place the text entry file
username = Entry(frame_entry, width = 15, bg ="white")
username.grid(row=0,column=1,padx=5,pady=5)
firstname = Entry(frame_entry, width=15, bg="white")
firstname.grid(row=1,column=1,padx=5,pady=5)
surname = Entry(frame_entry, width=15, bg="white")
surname.grid(row=2,column=1,padx=5,pady=5)

#place the submit and clear
submit_button = Button(root, text="Submit",width=7,command=submit)
submit_button.grid(row=2,column=0,padx=0,pady=5)
clear_button = Button(root, text="Clear",width=7,command=clear)
clear_button.grid(row=2, column=1,padx=0,pady=5) 
    
root.mainloop()
