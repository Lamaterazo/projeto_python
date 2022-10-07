from tkinter import *
janela = Tk()
janela["bg"] = "white"
app = Frame(janela)
app.grid()

def escrever():
    print("O meu nome é:", entryNome.get()
    , "e minha idade é:", entryIdade.get())
    
labelMsg = Label(janela,text="Qual seu nome?:"
    ,font="Times"
    ,bg="white",foreground="black")
labelMsg.place(x=1,y=1)

entryNome = Entry(janela)
entryNome.place(x=109,y=1)

Labelmsg = Label(janela,text="Qual sua idade?:",font="Times",bg="white",foreground="black")
Labelmsg.place(x=1,y=22)

entryIdade = Entry(janela)
entryIdade.place(x=109,y=22)

btnFalarNome = Button(janela,width=20,text="Clicar", command=escrever)
btnFalarNome.place(x=100,y=42)

title="Sistema Tarumã"
janela.title(title)
janela.geometry("800x400")
janela.resizable(False,False)
janela.mainloop()
janela.destroy()
