#Adicionando bibliotecas.
from tkinter import *

#Configurando a interface gráfica.
janela=Tk()
janela.title('Tela De Cadastro.')
janela.geometry('600x400')
janela.configure(background='#d3d3d3')

#Adicionando a apresentação.
apresentação = Label(janela, text='Projeto 001 - Start Code.', width=30)
apresentação.grid(column=0, row=0, padx=190, pady=10)

#Adicionando as caixas de entrada.
username = Label(janela, text='Email', width=21)
username.grid(column=0, row=1, padx=30, pady=30)
entrada1 = Entry(janela, width=25)
entrada1.grid(column=0, row=2)

senha = Label(janela, text='Senha', width=21)
senha.grid(column=0, row=3, padx=30, pady=30)
astsenha = StringVar
entrada2 = Entry(janela, textvariable = astsenha, show='*', width=25)
entrada2.grid(column=0, row=4)

#Adicionando o botão.
botão = Button(janela, text='Entrar', width=30)
botão.grid(column=0, row=5, pady=50)

janela.mainloop()