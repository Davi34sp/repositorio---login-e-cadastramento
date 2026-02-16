import tkinter as tk
#conta primordial
contas = [
    ("admpimentolas", "123💀💀"), #senha imposivel 🥶🥶
           ]

def createaccount():
    #novo usuario e senha
    newusuario = input("qual é o nome do seu usuario? ")
    newsenha = input("qual vai ser a senha do seu usuario? ")
    #adicionando a "contas"
    contas.append((newusuario, newsenha))
    print("conta criada👍")
createaccount()



#config da janela👍

janela = tk.Tk()
janela.geometry("400x300")
janela.title("login")

tk.Label(janela, text="Usuario").pack() #texto

usuario_entry = tk.Entry(janela) #entry
usuario_entry.pack() #.pack

tk.Label(janela, text="Senha").pack() #texto

senha_entry = tk.Entry(janela) #entry
senha_entry.pack()
menssagem = tk.Label(janela, text="Bem vindo")

def login(): #fuction de login
    usario = usuario_entry.get()
    senha = senha_entry.get()
    if (usario, senha) in contas:
        print('pode entrar')
        menssagem["text"] = "Seja bem-vindo!"
        menssagem.pack()
    else:
        print('credenciais erradas!')
        menssagem["text"] = "Opps!, aparentente as credenciais estão erradas!"
        menssagem.pack()

tk.Button(janela, text="Login", command=login).pack() #button/ login

#Executor
janela.mainloop()
