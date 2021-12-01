
# REFERENCE -> PROFESSOR

import tkinter as tk
import tkinter.ttk as ttk  # for ComboBox!!!!

def submit_command():
    print('pressed submit')

root=tk.Tk()
root.title('Quizz screen')
width, height =800,1000  # Set the width and height
screen_width = root.winfo_screenwidth()  # Get the screen width
screen_height = root.winfo_screenheight()  # Get the screen height
x_cord = int((screen_width / 2) - (width / 2))
y_cord = int((screen_height / 2) - (height / 2))
root.geometry("{}x{}+{}+{}".format(width,
                                   height,
                                   x_cord,
                                   y_cord))


mainFrame=tk.Frame(root,bg='gray')
mainFrame.grid(row=0,column=0,sticky=tk.NSEW,padx=10,pady=10)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

#upperFrame
upperFrame=tk.Frame(mainFrame,bg='red')
upperFrame.grid(row=0,column=0,sticky=tk.NSEW,padx=10,pady=10)
mainFrame.rowconfigure(0,weight=1)
mainFrame.columnconfigure(0,weight=1)

module_label= tk.Label(upperFrame,text='Module :')
module_label.grid(row=0,column=0,sticky=tk.EW,padx=10,pady=10)
upperFrame.rowconfigure(0,weight=1)
upperFrame.columnconfigure(0,weight=1)

module_names=['COMP1811','COMP1812','COMP1813']
module_combox=ttk.Combobox(upperFrame,state='readonly',values=module_names)
module_combox.grid(row=0,column=1,sticky=tk.EW,padx=10,pady=10)
upperFrame.rowconfigure(0,weight=1)
upperFrame.columnconfigure(1,weight=1)

#middleFrame
middleFrame=tk.Frame(mainFrame,bg='green')
middleFrame.grid(row=1,column=0,sticky=tk.NSEW,padx=10,pady=10)
mainFrame.rowconfigure(1,weight=4)
mainFrame.columnconfigure(0,weight=1)

for i in range(5):
    questionFrame = tk.Frame(middleFrame, bg='white')
    questionFrame.grid(row=i, column=0, sticky=tk.NSEW, padx=10, pady=10)
    middleFrame.rowconfigure(i, weight=6)
    middleFrame.columnconfigure(0, weight=1)


    questionHeader = tk.Label(questionFrame,text='Question '+str(i))
    questionHeader.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)
    questionFrame.rowconfigure(0, weight=1)
    questionFrame.columnconfigure(0, weight=1)

    for i in range(1,4):
        var=tk.IntVar()
        answer_radio_button = tk.Radiobutton(questionFrame, text='Question ' + str(i),
                                             var=var,value=i)
        answer_radio_button.grid(row=i, column=0, sticky=tk.NSEW)
        questionFrame.rowconfigure(i, weight=1)
        questionFrame.columnconfigure(0, weight=1)

#lowerFrame
lowerFrame=tk.Frame(mainFrame,bg='brown')
lowerFrame.grid(row=2,column=0,padx=10,pady=10,sticky=tk.NSEW)
mainFrame.rowconfigure(2,weight=1)
mainFrame.columnconfigure(0,weight=1)

resset_button=tk.Button(lowerFrame, text="reset")
resset_button.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)
lowerFrame.rowconfigure(0,weight=1)
lowerFrame.columnconfigure(0,weight=1)

submit_button=tk.Button(lowerFrame, text="submit",command=submit_command)
submit_button.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)
lowerFrame.rowconfigure(0,weight=1)
lowerFrame.columnconfigure(1,weight=1)


root.mainloop()