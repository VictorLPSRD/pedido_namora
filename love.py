
import customtkinter as tk # Criação da interface e dos elementos dela
from tkinter import messagebox 
import random# é utilizada nesse código para gerar números aleatórios
# que são usados ​​para posicionar o botão na janela de forma aleatória quando ele é clicado.

tela = tk.CTk()#Configuração da janela principal ate a linha 9:
tela.title("LOVE")
tela.configure(background="pink")
tela.geometry("650x400+350+50") 

def mover_button(event):# Dentro dessa função, geramos coordenadas xey aleatórias para posicionar o botão dentro da janela
    x = random.randint(0, tela.winfo_width() - button_1.winfo_width())
    y = random.randint(0, tela.winfo_height() - button_1.winfo_height())
    button_1.place(x=x, y=y)

def accepted():# função para gera uma messagem .
    messagebox.showinfo(" aiiiii"," aiii Vitinho apelâo")

margin =tk.CTkCanvas(tela,bg='#ffc8dd',width=600, height=100, relief="ridge")
margin.place(x=30, y=125)# Ele (ctkcanvas)  serve como um espaço em branco com uma borda em relevo.

text_id =tk.CTkLabel(tela, text="QUE NAMORA COMIGO ?",text_color="black",font=("impact",20),bg_color='#ffc8dd')
text_id.place(x=250, y=150)# label criação do textos  na interface usei 6 vezes da linha 22 a 41 .

emoji1 =tk.CTkLabel(tela, text="😍",text_color="#ffc8dd",font=("impact",60))
emoji1.place(x=150, y=30)

emoji2 =tk.CTkLabel(tela, text="💕",text_color="#ffc8dd",font=("impact",90))
emoji2.place(x=290, y=5)

emoji3 =tk.CTkLabel(tela, text="🥰",text_color="#ffc8dd",font=("impact",60))
emoji3.place(x=450, y=30)


emoji =tk.CTkLabel(tela, text="😍",text_color="#ffc8dd",font=("impact",60))
emoji.place(x=150, y=250)

emoji =tk.CTkLabel(tela, text="💕",text_color="#ffc8dd",font=("impact",90))
emoji.place(x=290, y=250)

emoji =tk.CTkLabel(tela, text="🥰",text_color="#ffc8dd",font=("impact",60))
emoji.place(x=450, y=250)

button_1 =tk.CTkButton(tela, text="Não",hover_color='dark red',fg_color='red',font=("impact",14),border_width=4,border_color='#ffc8dd')
button_1.place(x=350, y=190) # criação do botão
button_1.bind("<Button-1>", mover_button)# O método bind()é usado para associar um evento a um manipulador de eventos que mover 
                                        #Nesse caso, estamos associando o evento <Button-1>, que representa o clique do botão esquerdo do mouse, à função mover_button.
                                        # # Isso significa que quando o botão 1 for clicado, a função mover_buttonserá chamada.

button_2 =tk.CTkButton(tela, text="Sim",hover_color='dark red',fg_color='red',font=("impact",14),border_width=4, border_color='#ffc8dd',command=accepted)
button_2.place(x=200, y=190)# criação do botão chamando a função accepted que vai trazer a mensagem .

tela.mainloop()# Executa o loop principal da aplicação
