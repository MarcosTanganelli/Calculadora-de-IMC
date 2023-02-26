import tkinter as tk
from tkinter import ttk

def getInput ():
    #Essa função é chamada quando o botão é clicado
    userInput = float(entry.get())
    userInput1 = float(entry1.get())
    IMC = float(userInput / (userInput1/100 * userInput1/100))
    getClassificacao(IMC)
    label1.config(text="Seu IMC é: " + str(IMC))

def getClassificacao (imc):
    # Essa função é chamada para mudar cor das linhas
    if imc <= 18.5:
        table.item("I001", tags=("blue",))
    elif (18.5 < imc and imc < 24.99):
        table.item("I002", tags=("green",))
    elif (25 < imc and imc < 29.99):
        table.item("I003", tags=("orange",))
    else:
        table.item("I004", tags=("red",))





root = tk.Tk()  # cria uma janela
# adiciona um rótulo à janela
label = tk.Label(root, text="Calculadora de IMC")
label.pack()#função que adiciona label na tela
root.title("IMC")  # define o título da janela
root.geometry("400x300")  # define o tamanho da janela







# obtém as dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calcula a posição da janela no centro da tela
x = (screen_width / 2) - (400 / 2)
y = (screen_height / 2) - (300 / 2)

# define a posição da janela
root.geometry("+%d+%d" % (x, y))

instruction = tk.Label(root,  text="Digite seu peso:")#instruções do entrada
instruction.pack()


validate_int = root.register(lambda s: s.isdigit()) # função para validar entrada numérica
entry = tk.Entry(root, validate="key", validatecommand=(validate_int, '%S')) # não deixa escrever caracters sem ser numero
entry.pack()


instruction1 = tk.Label(root,  text="Digite sua altura:")
instruction1.pack()


entry1 = tk.Entry(root, validate="key", validatecommand=(validate_int, '%S'))
entry1.pack()


button = tk.Button(root, text="Enviar", command=getInput)#adiciona o botao enviar chamando funcao getinput, para obter valores inseridos
button.pack()

label1 = tk.Label(root)#label que será modificado no final da fução getinput para mostrar o imc
label1.pack()

table = ttk.Treeview(root, columns=('IMC', 'Classificação'), show='headings', height=4)#adiciona a tabela, mostrando apenas 4 linhas

#inserindo as colunas
table.heading('IMC', text='IMC')
table.heading('Classificação', text='Classificação')

#inserindo valroes
table.insert('', 'end', text="1", values=('Menor que 18,5', 'Baixo peso'))
table.insert('', 'end', text="2",  values=('De 18,5 e 24,99', 'Normal'))
table.insert('', 'end', text="3", values=('De 25 a 29,99', 'Sobrepeso'))
table.insert('', 'end', text="4", values=('Maior que 30', 'Obesidade'))


# define o tamanho das colunas
table.column('IMC', width=100)
table.column('Classificação', width=90)



table.pack()

#Definindo o as cores e seus nomes
#I001
style = ttk.Style()
table.tag_configure("blue", background="blue")
table.tag_configure("green", background="green")
table.tag_configure("orange", background="orange")
table.tag_configure("red", background="red")








root.mainloop()  # inicia o loop de eventos da janela