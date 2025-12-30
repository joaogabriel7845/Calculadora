from customtkinter import *
import pygame
import os
import sys

# Função para carregar recursos
def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


root = CTk()
root.title('Calculadora')
root.geometry('400x500')
root.resizable(False, False)

# Criação da janela do customtkinter
janela = CTkFrame(root, fg_color='#0D0D0D', bg_color='black')
janela.pack(fill="both", expand=True)

# Inicialização do PyGame
pygame.mixer.init()

# FUNÇÕES
def calcular():
    try:
        # Obtém a expressão do campo de entrada
        expressao = valores.get().strip()
        
        # Avalia a expressão matemática
        resultado = eval(expressao)

        # Limpa o campo de entrada e insere o resultado
        valores.delete(0, 'end')
        valores.insert(0, f'{resultado}')

    except (NameError, TypeError):
        # Se ocorrer um erro, exibe uma mensagem de erro
        valores.delete(0, 'end')
        valores.insert(0, f'Erro: Expressão inválida')
        
    except ZeroDivisionError:
        valores.delete(0, 'end')
        valores.insert(0, 'Erro: Divisão por zero')


def adicionarNUM(num):
    valores.insert('end', num)


def trocarsinal():
    try:
        valor_atual = valores.get().strip()

        if valor_atual:
            if valor_atual.startswith('-'):
                novo_valor = valor_atual[1:]
            else:
                novo_valor = '-' + valor_atual

            valores.delete(0, 'end')
            valores.insert(0, novo_valor)
        
    except Exception as e:
        print(f'Erro ao trocar o sinal: {e}')
        

def apagarNUM():
    valores.delete(0, 'end')

# Entry
valores = CTkEntry(root, fg_color='#0D0D0D',bg_color='#0D0D0D',width=345, border_color='#0D0D0D',height=50, font=('Inter', 50))
valores.place(x=20, y=30)

# Button
apagar = CTkButton(janela, text='CE', fg_color='#35C2C2', width=70, height=65, font=('Inter', 20, 'bold'), command=apagarNUM)
apagar.place(x=20, y=120)

# Button
trocarsinal = CTkButton(janela, text='+/-', fg_color='#35C2C2', width=160, height=65, font=('Inter', 20, 'bold'), command=trocarsinal)
trocarsinal.place(x=110, y=120)


botoes = [
    ('7', 20, 195), ('8', 110, 195), ('9', 200, 195), ('+', 300, 195),
    ('4', 20, 270), ('5', 110, 270), ('6', 200, 270), ('-', 300, 270),
    ('1', 20, 345), ('2', 110, 345), ('3', 200, 345), ('*', 300, 345),
    ('0', 20, 420), ('/', 300, 120), ('.', 200, 420), ('=', 300, 420)
]

for texto, x, y in botoes:
    if texto == '0':
        CTkButton(janela, text=texto, fg_color='#171718', width=160, height=65, hover_color='gray', font=('Inter', 20, 'bold'), command=lambda t=texto: adicionarNUM(t)).place(x=x, y=y)
    elif texto == '=':
        CTkButton(janela, text=texto, fg_color='#35C2C2', width=70, height=65, font=('Inter', 20, 'bold'), command=calcular).place(x=x, y=y)
    elif texto == '+' or texto == '-' or texto == '*' or texto == '/' or texto == '.':
        CTkButton(janela, text=texto, fg_color='#35C2C2', width=70, height=65, font=('Inter', 20, 'bold'), command=lambda t=texto: adicionarNUM(t)).place(x=x, y=y)
    else:
        CTkButton(janela, text=texto, fg_color='#171718', width=70, height=65, hover_color='gray', font=('Inter', 20, 'bold'), command=lambda t=texto: adicionarNUM(t)).place(x=x, y=y)

# Inicialização da janela
root.mainloop()