import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()

def createNewWindow():
    newWindow = tk.Toplevel(app)
   
def cadastrarUsuarios():
    janelaUsuarios = tk.Toplevel(app)

    lblNome = tk.Label(janelaUsuarios,text="Informe seu nome:"
    ,font="Times"
    ,bg="white", foreground="black")
    lblNome.place(x=1,y=10)

    entryNome = tk.Entry(janelaUsuarios)
    entryNome.place(x=122,y=13)

    lblSobrenome = tk.Label(janelaUsuarios,text="Informe seu sobrenome:"
    ,font="Times"
    ,bg="white", foreground="black")
    lblSobrenome.place(x=1,y=40)

    entrySobrenome = tk.Entry(janelaUsuarios)
    entrySobrenome.place(x=155,y=44)

    lblDataNascimento = tk.Label(janelaUsuarios,text="Informe sua Data de Nascimento:"
    ,font="Times"
    ,bg="white", foreground="black")
    lblDataNascimento.place(x=1,y=70)

    entryDataNascimento = tk.Entry(janelaUsuarios)
    entryDataNascimento.place(x=213,y=74)

    lblCidade = tk.Label(janelaUsuarios,text="Informe sua cidade:"
    ,font="Times"
    ,bg="white", foreground="black")
    lblCidade.place(x=1,y=100)

    entryNome = tk.Entry(janelaUsuarios)
    entryNome.place(x=129,y=105)

    lblEstado = tk.Label(janelaUsuarios,text="Informe seu estado:"
    ,font="Times"
    ,bg="white", foreground="black")
    lblEstado.place(x=1,y=130)

    entryEstado = tk.Entry(janelaUsuarios)
    entryEstado.place(x=129,y=133)

    


    janelaUsuarios.title("Cadastro de Usuários")
    janelaUsuarios.geometry("800x600")

def cadastrarProdutos():
    janelaProdutos= tk.Toplevel(app)
    janelaProdutos.title("Cadastro de Produtos")
    janelaProdutos.geometry("800x600")

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar Usuários"
            ,command=cadastrarUsuarios)
fileMenu.add_command(label="Cadastrar Produtos"
            ,command=cadastrarProdutos)
menuPrincipal.add_cascade(label="Função"
                        ,menu=fileMenu)

#buttonExample = tk.Button(app,
#                text='Create new window',
#                command=createNewWindow)
#buttonExample.place(x=100,y=50)
app.title("Sistema Tarumã")
app.geometry("800x600")
app.mainloop()
app.destroy()









