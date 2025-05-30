import customtkinter as ctk
from util import limpar_tela, resource_path
from PIL import Image
from customtkinter import CTkImage


def abrir_config(janela, frame_atual):
    from home import abrir_home
    limpar_tela(frame_atual)
    
    titulo_config = ctk.CTkLabel(frame_atual, text='Configurações', font=('Helvetica', 24), text_color='white', fg_color='#08254b')
    titulo_config.pack(anchor='n', pady=10, padx=0.5)

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_home = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_home(janela, frame_atual), bg_color='#08254b')
    voltar_home.place(relx=0.98, rely=0.025, anchor='ne')
