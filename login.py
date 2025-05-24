from dados.tabelas import User, session
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from home import abrir_home
from util import limpar_tela, resource_path
from PIL import Image
from customtkinter import CTkImage

def abrir_login(janela, frame_atual):
    limpar_tela(frame_atual)
    janela.geometry('550x500')

    frame_fundo = ctk.CTkFrame(frame_atual, width=600, height=500, fg_color="#ffffff")
    frame_fundo.place(relx=0.5, rely=0.5, anchor='center')

    # Frame da imagem de login
    frame_imagem = ctk.CTkFrame(frame_fundo, width=400, height=500, fg_color='#327bcf')
    frame_imagem.pack(side='left', fill='both')

    fundo_img = Image.open(resource_path("imagens/login.png"))
    fundo_img = CTkImage(light_image=fundo_img, size=(400, 500))
    image_label = ctk.CTkLabel(frame_imagem, text='', image=fundo_img)
    image_label.place(relx=0.5, rely=0.5, anchor='center')

    # Frame do login
    frame_login = ctk.CTkFrame(frame_fundo, width=150, height=500, fg_color="#ffffff", corner_radius=20)
    frame_login.pack(side='right', fill='both', padx=10, pady=10)
    
    titulo_login = ctk.CTkLabel(frame_login, text='Login', font=('Arial Rounded MT Bold', 23), text_color="#0c184c")
    titulo_login.pack(pady=(50, 10))
    
    subtitulo_login = ctk.CTkLabel(frame_login, text='Entre com suas credenciais', font=('Arial', 12), text_color="#333333", wraplength=150, justify="center")
    subtitulo_login.pack(pady=(0, 20))

    entry_user = ctk.CTkEntry(frame_login, placeholder_text='Usuário', fg_color='#e0e0e0', text_color='#0c184c', border_color='#0c184c', corner_radius=10)
    entry_user.pack(pady=10, padx=10, fill='x')

    entry_senha = ctk.CTkEntry(frame_login, placeholder_text='Senha', show="*", fg_color='#e0e0e0', text_color='#0c184c', border_color='#0c184c', corner_radius=10)
    entry_senha.pack(pady=10, padx=10, fill='x')

    def verificar_login():
        usuario = entry_user.get().lower()
        senha = entry_senha.get().lower()

        usuario_banco = session.query(User).filter_by(nome_user=usuario, senha_user=senha).first()

        if usuario_banco:
            abrir_home(janela, frame_atual)
        else:
           retorno = CTkMessagebox(icon='cancel', message='Usuário ou senha incorreto', title='Login incorreto')

    botao = ctk.CTkButton(frame_login, text='Login', width=120, height=35, command=verificar_login, fg_color="#5247e7", hover_color="#3e36af", text_color='#0c184c', corner_radius=20)
    botao.pack(pady=30)

    


