import customtkinter as ctk
from dados.tabelas import Conta, session
from util import limpar_tela, resource_path
from PIL import Image
from customtkinter import CTkImage
from bkp.iniciar_backups import iniciar_backup

def abrir_backups(janela, frame_atual):
    limpar_tela(frame_atual)
    from home import abrir_home
    
    fundo = Image.open(resource_path("imagens/fundo1.png"))
    fundo = CTkImage(light_image=fundo, size=(550, 100))

    image_label = ctk.CTkLabel(frame_atual, text='', image=fundo)
    image_label.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.2)

    titulo_backups = ctk.CTkLabel(frame_atual, text='Lista de Contas', font=('Helvetica', 24), text_color='white')
    titulo_backups.pack(anchor='n', pady=10, padx=0.5)

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_home = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='transparent', hover_color='#A9A9A9', text='', command=lambda: abrir_home(janela, frame_atual))
    voltar_home.place(relx=0.98, rely=0.025, anchor='ne')

    iniciar = ctk.CTkButton(frame_atual, text='Iniciar Backups', fg_color='#0d1b2a', hover_color='#0d1b2a', width=80, command=lambda: iniciar_backup(frame_atual, janela))
    iniciar.place(relx=0.025, rely=0.02)

    frame_contas = ctk.CTkScrollableFrame(frame_atual, width=520, height=425, fg_color='#111530')
    frame_contas.place(relx=0.5, rely=0.55, anchor='center')

    for i, conta in enumerate(session.query(Conta).all()):
        label_nome = ctk.CTkLabel(frame_contas, text=conta.nome.capitalize(), text_color='white')
        label_nome.grid(row=i, column=0, padx=5, pady=5)

        label_email = ctk.CTkLabel(frame_contas, text=conta.email, text_color='white')
        label_email.grid(row=i, column=1, padx=10, pady=5)
