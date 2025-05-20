from dados.tabelas import User, session
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from home import abrir_home
from util import limpar_tela, resource_path
from PIL import Image
from customtkinter import CTkImage

def abrir_login(janela, frame_atual):
    limpar_tela(frame_atual)

    frame_fundo = ctk.CTkFrame(frame_atual, width=600, height=500, fg_color='#0c184c')
    frame_fundo.place(relx=0.5, rely=0.5, anchor='center')

    fundo_img = Image.open(resource_path("imagens/fundo2.png"))
    fundo_img = CTkImage(light_image=fundo_img, size=(600, 500))
    image_label = ctk.CTkLabel(frame_fundo, text='', image=fundo_img)
    image_label.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)
    
    titulo_login = ctk.CTkLabel(frame_fundo, text='Backup Manager', font=('Arial', 25), fg_color='#0A1F56', text_color='Cyan')
    titulo_login.place(relx=0.5, rely=0.0, anchor='n')
    
    entry_user = ctk.CTkEntry(frame_fundo, placeholder_text='Usuário', fg_color='#0d1b2a', bg_color='#0A1F56', text_color='white')
    entry_user.place(relx=0.5, rely=0.25, anchor='center')

    entry_senha = ctk.CTkEntry(frame_fundo, placeholder_text='Senha', show="*", fg_color='#0d1b2a', bg_color='#0A1F56', text_color='white')
    entry_senha.place(relx=0.5, rely=0.35, anchor='center')

    def verificar_login():
        usuario = entry_user.get().lower()
        senha = entry_senha.get().lower()

        usuario_banco = session.query(User).filter_by(nome_user=usuario, senha_user=senha).first()

        if usuario_banco:
            abrir_home(janela, frame_atual)
        else:
           retorno = CTkMessagebox(icon='cancel', message='Usuário ou senha incorreto', title='Login incorreto')

    botao = ctk.CTkButton(frame_fundo, text='Login', width=80, command=verificar_login, fg_color='#0d1b2a', bg_color='#0d1b2a', hover_color='#0d1b2a')
    botao.place(relx=0.5, rely=0.45, anchor='n')

    


