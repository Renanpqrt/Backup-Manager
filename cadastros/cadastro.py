import customtkinter as ctk
from util import limpar_tela, resource_path
from PIL import Image
from customtkinter import CTkImage
from cadastros.users import abrir_user

def abrir_cadastros(janela, frame_atual):
    from home import abrir_home
    limpar_tela(frame_atual)

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_home = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_home(janela, frame_atual), bg_color='#08254b')
    voltar_home.place(relx=0.98, rely=0.025, anchor='ne')

    titulo_cadastro = ctk.CTkLabel(frame_atual, text='Cadastros', font=('Helvetica', 25, 'bold'), text_color="#FFFFFF", fg_color='#08254b')
    titulo_cadastro.place(relx=0.5, rely=0.05, anchor='center')

    users_imag = Image.open(resource_path("imagens/users.png"))
    users_imag = CTkImage(light_image=users_imag, size=(40, 40))

    users_b = ctk.CTkButton(frame_atual, image=users_imag, text='', width=60, fg_color='#08254b', hover_color="#A9A9A9", command=lambda: abrir_user(janela, frame_atual), bg_color='#08254b')
    users_b.place(relx=0.07, rely=0.07, anchor='center')