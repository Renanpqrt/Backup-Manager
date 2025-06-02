from dados.tabelas import User, session
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from home import abrir_home
from util import limpar_tela


def abrir_login(janela, frame_atual):
    limpar_tela(frame_atual)
    janela.configure(fg_color='#111606')
    janela.geometry('720x360')

    #Fundo principal
    frame_fundo = ctk.CTkFrame(frame_atual, width=720, height=320, fg_color="#6f8c3e")
    frame_fundo.pack(expand=True, fill="both", padx=20, pady=20)

    #Fundo esquerdo
    frame_esquerdo = ctk.CTkFrame(frame_fundo, width=280, height=280, fg_color="#111606", corner_radius=15)
    frame_esquerdo.pack(side="left", padx=(20, 10), pady=20, fill="y")

    label_logo = ctk.CTkLabel(frame_esquerdo, text="PLR", font=("Montserrat", 36, "bold"), text_color="#F5F5F5")
    label_logo.place(relx=0.5, rely=0.25, anchor="center")

    label_sublogo = ctk.CTkLabel(frame_esquerdo, text="Manager", font=("Montserrat", 20), text_color="#F5F5F5")
    label_sublogo.place(relx=0.5, rely=0.43, anchor="center")

    label_slogan = ctk.CTkLabel(frame_esquerdo, 
                                text="Gestão de backups\npara o seu negócio", 
                                font=("Montserrat", 13), text_color="#F5F5F5", justify="center")
    label_slogan.place(relx=0.5, rely=0.65, anchor="center")

    #Fundo direito
    frame_direito = ctk.CTkFrame(frame_fundo, width=380, height=280, fg_color="#FFFFFF", corner_radius=15)
    frame_direito.pack(side="right", padx=(10, 20), pady=20, fill="both", expand=True)

    label_login = ctk.CTkLabel(frame_direito, text="Login", font=("Montserrat", 24, "bold"), text_color="#333333")
    label_login.pack(pady=(40, 5))

    label_instrucao = ctk.CTkLabel(frame_direito, 
                                   text="Insira seu usuário e senha para continuar", 
                                   font=("Montserrat", 12), text_color="#666666")
    label_instrucao.pack(pady=(0, 25))

    entry_user = ctk.CTkEntry(frame_direito, placeholder_text='Usuário', fg_color='#e0e0e0', text_color='#0c184c', border_color='#0c184c', corner_radius=10)
    entry_user.pack(pady=10, padx=10, fill='x')

    entry_senha = ctk.CTkEntry(frame_direito, placeholder_text='Senha', show="*", fg_color='#e0e0e0', text_color='#0c184c', border_color='#0c184c', corner_radius=10)
    entry_senha.pack(pady=10, padx=10, fill='x')

    def verificar_login():
        usuario = entry_user.get().lower()
        senha = entry_senha.get().lower()

        usuario_banco = session.query(User).filter_by(nome_user=usuario, senha_user=senha).first()

        if usuario_banco:
            abrir_home(janela, frame_atual)
        else:
           retorno = CTkMessagebox(icon='cancel', message='Usuário ou senha incorreto', title='Login incorreto')

    botao = ctk.CTkButton(frame_direito, text='Login', width=120, height=35, command=verificar_login, fg_color="#5247e7", hover_color="#3e36af", text_color='#0c184c', corner_radius=20)
    botao.pack(padx=5, pady=5)

    


