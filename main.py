import tkinter as tk

# janelas config

janela = tk.Tk()
janela.geometry("480x300")
janela.title("Ocicle")

# buttons/textos
texto = tk.Label(janela, text=f"Ola, bem vindo! ao Ocicle, digite seu nome:")
texto.pack()

entrada_texto = tk.Entry(janela)
entrada_texto.pack()

def botão_apertado():
    nome = entrada_texto.get()
    texto['text'] = f"olá {nome}"

tk.Button(janela, text="button", command=botão_apertado).pack()

# Executador

janela.mainloop()
