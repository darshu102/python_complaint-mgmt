from tkinter import *
root = Tk()

text = Text(root,bg='light blue')
text.grid(row=0,column=0,columnspan=2)

e = Entry(root,width=80)
e.grid(row=1,column=0)

class chatbott:

    def send():
        
        send = "You:"+ e.get()
        text.insert(END,"\n" + send)
        
        if(e.get()=='hi'):
            text.insert(END, "\n" + "Bot: hello, how can i help you?")
        elif(e.get()=='hello'):
            text.insert(END, "\n" + "Bot: hi")
        elif (e.get() == 'how are you?'):
            text.insert(END, "\n" + "Bot: i'm fine and you?")
        elif (e.get() == "i'm fine too"):
            text.insert(END, "\n" + "Bot: nice to hear that")
        else:
            text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
        
        

    send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)

root.title('CHATBOT')
