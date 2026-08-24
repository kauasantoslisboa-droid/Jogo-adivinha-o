import tkinter as tk
import ramdom

#________________
#VARIÁVEIS DO JOGO
#________________

numero_secreto = 0 
tentativas = 0 
limite = 20

#_________________
#JANELA
#_________________

janela = tk.Tk()

janela.title("Jogo de Adivinhação")
janela.geometry("450x500")


#_________________
#TÍTULO
#_________________

titulo = tk.Label(
    janela,
    text="JOGO DE ADIVINHAÇÃO",
)   font=("Arial",20)

titulo.pack(pady=20)


#_______________
#NOME DO JOGADOR
#_______________


texto_nome = tl.Label(
    janela,
    text="Digite seu nome:"
)   

texto_nome.pack()

campo_nome = tk.Entry(
    janela,
    font=("Arial",14)
)

campo_nome.pack(pady=5)


# ____________________________
# DIFICULDADE
# ____________________________

texto_dificuldade = tk.Label(
janela,
text="Escolha a dificuldade:"
)

texto_dificuldade.pack(pady=10)


dificuldade = tk.StringVar()

dificuldade.set("Fácil")


menu_dificuldade = tk.OptionMenu(
janela,
dificuldade,
"Fácil",
"Médio",
"Difícil"
)

menu_dificuldade.pack()


# _____________________________
# CAMPO DO PALPITE
# _____________________________

texto_palpite = tk.Label(
janela,
text="Digite seu palpite:"
)

texto_palpite.pack(pady=15)


campo_palpite = tk.Entry(
janela,
font=("Arial", 16),
justify="center"
)

campo_palpite.pack()


# _____________________________
# RESULTADO
# _____________________________

resultado = tk.Label(
janela,
text="Digite seu nome e clique em INICIAR.",
font=("Arial", 12)
)

resultado.pack(pady=20)


# _____________________________
# FUNÇÃO PARA INICIAR O JOGO
# _____________________________

def iniciar_jogo():

global numero_secreto
global tentativas
global limite

tentativas = 0

nivel = dificuldade.get()

if nivel == "Fácil":
limite = 20

elif nivel == "Médio":
limite = 50

else:
limite = 100

numero_secreto = random.randint(1, limite)

resultado.config(
text="Jogo iniciado!\nAdivinhe um número entre 1 e " + str(limite)
)


# _____________________________
# FUNÇÃO PARA VERIFICAR PALPITE
# _____________________________

def verificar_palpite():

global tentativas

palpite = int(campo_palpite.get())

tentativas = tentativas + 1


if palpite == numero_secreto:

nome = campo_nome.get()

resultado.config(
text="Parabéns, " + nome +
"!\nVocê acertou em " +
str(tentativas) +
" tentativas!"
)


elif palpite < numero_secreto:

resultado.config(
text="O número secreto é MAIOR!"
)


else:

resultado.config(
text="O número secreto é MENOR!"
)


campo_palpite.delete(0, tk.END)


# _____________________
# BOTÕES
# _____________________

botao_iniciar = tk.Button(
janela,
text="INICIAR JOGO",
command=iniciar_jogo
)
# _____________________
# DIFICULDADE
# _____________________

texto_dificuldade = tk.Label(
janela,
text="Escolha a dificuldade:"
)

texto_dificuldade.pack(pady=10)


dificuldade = tk.StringVar()

dificuldade.set("Fácil")


menu_dificuldade = tk.OptionMenu(
janela,
dificuldade,
"Fácil",
"Médio",
"Difícil"
)

menu_dificuldade.pack()


# _____________________
# CAMPO DO PALPITE
# _____________________

texto_palpite = tk.Label(
janela,
text="Digite seu palpite:"
)

texto_palpite.pack(pady=15)


campo_palpite = tk.Entry(
janela,
font=("Arial", 16),
justify="center"
)

campo_palpite.pack()


# _____________________
# RESULTADO
# _____________________

resultado = tk.Label(
janela,
text="Digite seu nome e clique em INICIAR.",
font=("Arial", 12)
)

resultado.pack(pady=20)


# _____________________
# FUNÇÃO PARA INICIAR O JOGO
# _____________________

def iniciar_jogo():

global numero_secreto
global tentativas
global limite

tentativas = 0

nivel = dificuldade.get()

if nivel == "Fácil":
limite = 20

elif nivel == "Médio":
limite = 50

else:
limite = 100

numero_secreto = random.randint(1, limite)

resultado.config(
text="Jogo iniciado!\nAdivinhe um número entre 1 e " + str(limite)
)


# _____________________
# FUNÇÃO PARA VERIFICAR PALPITE
# _____________________

def verificar_palpite():

global tentativas

palpite = int(campo_palpite.get())

tentativas = tentativas + 1


if palpite == numero_secreto:

nome = campo_nome.get()

resultado.config(
text="Parabéns, " + nome +
"!\nVocê acertou em " +
str(tentativas) +
" tentativas!"
)


elif palpite < numero_secreto:

resultado.config(
text="O número secreto é MAIOR!"
)
-----------------------------

else:

resultado.config(
text="O número secreto é MENOR!"
)


campo_palpite.delete(0, tk.END)


# _____________________
# BOTÕES
# _____________________

botao_iniciar = tk.Button(
janela,
text="INICIAR JOGO",
command=iniciar_jogo
)

botao_iniciar.pack(pady=10)


botao_tentar = tk.Button(
janela,
text="TENTAR",
command=verificar_palpite,
font=("Arial", 12)
)

botao_tentar.pack(pady=5)

-----------------------------
# _____________________
# MANTÉM A JANELA ABERTA
# _____________________

janela.mainloop()
botao_iniciar.pack(pady=10)


botao_tentar = tk.Button(
janela,
text="TENTAR",
command=verificar_palpite,
font=("Arial", 12)
)

botao_tentar.pack(pady=5)


# _____________________
# MANTÉM A JANELA ABERTA
# ______________________

janela.mainloop()