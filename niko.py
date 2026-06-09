import tkinter as tk
from tkinter import messagebox

# Função para calcular
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida!")

# Função para adicionar texto ao campo
def adicionar_texto(texto):
    entrada.insert(tk.END, texto)

# Função para limpar
def limpar():
    entrada.delete(0, tk.END)

# Criando janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Campo de entrada
entrada = tk.Entry(janela, width=25, font=("Arial", 16))
entrada.grid(row=0, column=0, columnspan=4)

# Botões
botoes = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        tk.Button(janela, text=texto, width=5, height=2, command=calcular).grid(row=linha, column=coluna)
    else:
        tk.Button(janela, text=texto, width=5, height=2, command=lambda t=texto: adicionar_texto(t)).grid(row=linha, column=coluna)

# Botão de limpar
tk.Button(janela, text="C", width=5, height=2, command=limpar).grid(row=5, column=0, columnspan=4)

# Executar janela
janela.mainloop()