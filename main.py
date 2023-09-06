from tkinter import *
from tkinter import Tk

#Definindo as cores do programa
cor1 = '#1a1c3b' #azul escuro
cor2 = '#8f92ba' #azul claro
cor3 = '#d9292f' #vermelho claro
cor4 = '#ffffff' # branco
cor5 = '#12142b' #azul mais escuro

#Criando a janela do programa
janela = Tk()
janela.title('Calculadora')
janela.geometry('277x440')
janela.minsize(277, 440)
janela.maxsize(277, 440)
janela.config(bg = cor1)

#Variável "todos valores"
todos_valores = ''

#Criando função para entrada dos valores
def entrada_valores(e):
    global todos_valores

    todos_valores += str(e)

    #Imprimindo os valores na tela
    valorLabel.config(text=todos_valores)


def resultado_calculo():
    global todos_valores

    resultado = eval(todos_valores)

    resultadoLabel.config(text=str(resultado))
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

#Função para limpar a tela
def limpar_tela():
    global todos_valores

    todos_valores = ""
    valor_texto.set("")

    valorLabel.config(text = '')
    resultadoLabel.config(text='')
    

#Criando os frames
frame_display = Frame(janela, width = 277, height = 90, bg = cor1)
frame_display.grid(row = 0, column = 0)

frame_body = Frame(janela, width = 277, height = 390, bg = cor1)
frame_body.grid(row = 1, column = 0)


#Criando label para os valores
valor_texto = StringVar()

valorLabel = Label(frame_display, text = '', width = 26, height = 2, bg = cor5, fg = cor4, padx = 7, relief = FLAT, anchor = "e", justify = RIGHT, font=('Tahoma 14'))
valorLabel.place(x = 0, y = -10)

resultadoLabel = Label(frame_display, text = '', wraplength=260, width = 16, height = 2, bg = cor1, fg = cor4, padx = 8.5, relief = FLAT, anchor = "e", justify = RIGHT, font=('Tahoma 22'))
resultadoLabel.place(x = 0, y = 30)


#Criando os botões da primeira linha
btn_1 = Button(frame_body, command = limpar_tela, text = 'C', width = 6, height = 3, bg = cor2, fg = cor3, font=('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_1.place(x = 0, y = 0)

btn_2 = Button(frame_body, command = lambda: entrada_valores('%'), text = '%', width = 6, height= 3, bg = cor2, fg = cor3, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_2.place(x = 70, y = 0)

btn_3 = Button(frame_body, command = lambda: entrada_valores('/'), text = '/', width = 6, height= 3, bg = cor2, fg = cor3, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_3.place(x = 140, y = 0)

btn_4 = Button(frame_body, command = lambda: entrada_valores('*'), text = '*', width = 6, height= 3, bg = cor2, fg = cor3, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_4.place(x = 210, y = 0)

#Criando os botões da segunda linha
btn_5 = Button(frame_body, command = lambda: entrada_valores('7'), text = '7', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_5.place(x = 0, y = 70)

btn_6 = Button(frame_body, command = lambda: entrada_valores('8'), text = '8', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_6.place(x = 70, y = 70)

btn_7 = Button(frame_body, command = lambda: entrada_valores('9'), text = '9', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_7.place(x = 140, y = 70)

btn_8 = Button(frame_body, command = lambda: entrada_valores('-'), text = '-', width = 6, height= 3, bg = cor2, fg = cor3, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_8.place(x = 210, y = 70)

#Criando os botões da terceira linha
btn_8 = Button(frame_body, command = lambda: entrada_valores('4'), text = '4', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_8.place(x = 0, y = 140)

btn_10 = Button(frame_body, command = lambda: entrada_valores('5'), text = '5', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_10.place(x = 70, y = 140)

btn_11 = Button(frame_body, command = lambda: entrada_valores('6'), text = '6', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_11.place(x = 140, y = 140)

btn_12 = Button(frame_body, command = lambda: entrada_valores('+'), text = '+', width = 6, height= 3, bg = cor2, fg = cor3, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_12.place(x = 210, y = 140)

#Criando os botões da quarta linha
btn_13 = Button(frame_body, command = lambda: entrada_valores('1'), text = '1', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_13.place(x = 0, y = 210)

btn_13 = Button(frame_body, command = lambda: entrada_valores('2'), text = '2', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_13.place(x = 70, y = 210)

btn_14 = Button(frame_body, command = lambda: entrada_valores('3'), text = '3', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_14.place(x = 140, y = 210)

btn_15 = Button(frame_body, command = resultado_calculo, text = '=', width = 6, height= 7, bg = cor3, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_15.place(x = 210, y = 210)

#Criando os botões da quinta linha
btn_16 = Button(frame_body, command = lambda: entrada_valores('0'), text = '0', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_16.place(x = 0, y = 280)

btn_17 = Button(frame_body, command = lambda: entrada_valores('.'), text = '.', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_17.place(x = 70, y = 280)

btn_18 = Button(frame_body, command = lambda: entrada_valores('<'), text = '<', width = 6, height= 3, bg = cor1, fg = cor4, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_18.place(x = 140, y = 280)

janela.mainloop()