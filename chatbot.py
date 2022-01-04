from tkinter import *


class chatbott:

    def __init__(self):

        self.root = Tk()
        self.root.title('CHATBOT')

        e = Entry(self.root,width=80)

        send = "You:"+ e.get()
        
        text = Text(self.root,bg='light blue')

        text.grid(row=0,column=0,columnspan=2)
        text.insert(END,"\n" + send)
        
        if(e.get()=='hi'):
            text.insert(END, "\n" + "Bot: hello")
        elif(e.get()=='hello'):
            text.insert(END, "\n" + "Bot: hi")
        elif (e.get() == 'how are you?'):
            text.insert(END, "\n" + "Bot: i'm fine and you?")
        elif (e.get() == "i'm fine too"):
            text.insert(END, "\n" + "Bot: nice to hear that")
        else:
            text.insert(END, "\n" + "Bot: Sorry I didnt get it.")

        
        send = Button(self.root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
        e.grid(row=1,column=0)
        self.root.mainloop()