import customtkinter as ctk
from util import limpar_tela, resource_path
from config import abrir_config
from PIL import Image
from customtkinter import CTkImage
from bkp.lista_contas import abrir_backups
from bkp.contas_dados import backup_dados

def abrir_home(janela, frame_atual):
    from login import abrir_login
    limpar_tela(frame_atual)
    janela.configure(fg_color='#08254b')

    fundo = Image.open(resource_path("imagens/home.png"))
    fundo = CTkImage(light_image=fundo, size=(550, 500))

    image_label = ctk.CTkLabel(frame_atual, text='', image=fundo)
    image_label.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)

    titulo_home = ctk.CTkLabel(frame_atual, text='Backup Manager (Home)', font=('Helvetica', 22), fg_color='#08254b', text_color='white')
    titulo_home.pack(anchor='n', pady=10, padx=0.5)

    engrenagem_img = Image.open(resource_path("imagens/engrenagem.png"))
    engrenagem_img = CTkImage(light_image=engrenagem_img, size=(30, 30))

    botao_config = ctk.CTkButton(frame_atual, image=engrenagem_img, text='', fg_color='#08254b', hover_color='#A9A9A9', width=60, command=lambda: abrir_config(janela, frame_atual), bg_color='#08254b')
    botao_config.place(relx=0.97, rely=0.02, anchor='ne')

    sair_img = Image.open(resource_path("imagens/logoff.png"))
    sair_img = CTkImage(light_image=sair_img, size=(30, 30))

    logoff = ctk.CTkButton(frame_atual, image=sair_img, text='', width=60, fg_color='#08254b', hover_color='#A9A9A9', command=lambda: abrir_login(janela, frame_atual), bg_color='#08254b')
    logoff.place(relx=0.025, rely=0.02)

    fzr_bkp = ctk.CTkButton(frame_atual, text='Backups', fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: abrir_backups(janela, frame_atual), width=120,
                             height=32, corner_radius=5, bg_color='#08254b')
    fzr_bkp.place(relx=0.5, rely=0.3, anchor='n')

    fzr_bkp_dados = ctk.CTkButton(frame_atual, text='Contas De Dados', fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: backup_dados(janela, frame_atual), width=120, 
                                  height=30, corner_radius=5, bg_color='#08254b')
    fzr_bkp_dados.place(relx=0.5, rely=0.4, anchor='n')

