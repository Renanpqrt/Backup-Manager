from dados.tabelas import User, session
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from home import abrir_home
from util import limpar_tela
from datetime import date, datetime
import locale
versao = '1.1.2'

def abrir_login(janela, frame_atual):
    limpar_tela(frame_atual)
    janela.configure(fg_color='#2B2B2B')
    janela.geometry('900x550')

    # Frame esquerdo
    left_frame = ctk.CTkFrame(frame_atual, width=400, fg_color="#2B2B2B")
    left_frame.pack(side="left", fill="both", expand=True)

    # Texto no painel esquerdo
    welcome_label = ctk.CTkLabel(left_frame, text="🔒 PLR Manager", font=("Arial", 24, "bold"), text_color="#EEEEEE")
    welcome_label.place(relx=0.5, rely=0.3, anchor="center")

    info_label = ctk.CTkLabel(left_frame, text="Organize, controle e acesse com facilidade", font=("Arial", 14), text_color="#EEEEEE", wraplength=300, justify="center")
    info_label.place(relx=0.5, rely=0.4, anchor="center")

    # Datas no painel esquerdo
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
    except locale.Error:
        locale.setlocale(locale.LC_TIME, '')
    
    hora = datetime.today().strftime("%H:%M")
    data = date.today().strftime("%a, %d de %b")

    hora_label = ctk.CTkLabel(left_frame, text=hora, text_color="#EEEEEE", font=("Arial", 15))
    hora_label.place(relx=0.9, rely=0.8, anchor='center')

    data_label = ctk.CTkLabel(left_frame, text=data.title(), font=("Arial", 16), text_color="#EEEEEE")
    data_label.place(relx=0.15, rely=0.08, anchor='center')

    # Atualizar o relogio

    def atualizar_relogio():
        nova_hora = datetime.now().strftime("%H:%M")
        hora_label.configure(text=nova_hora)
        hora_label.after(1000, atualizar_relogio)

    # Mostrar senha

    def mostrar_senha():
        if variavelCheckBox.get() == 1:
            entry_senha.configure(show='')
        else:
            entry_senha.configure(show='*')

    # Frame direito - login
    right_frame = ctk.CTkFrame(frame_atual, fg_color="#1E1E1E")
    right_frame.pack(side="right", fill="both", expand=True)

    # Título
    login_label = ctk.CTkLabel(right_frame, text="Login", font=("Arial", 28, "bold"), text_color='gray')
    login_label.pack(pady=(60, 10))

   # Subtítulo
    subtitle = ctk.CTkLabel(right_frame, text="Acesse sua conta", font=("Arial", 16), text_color="gray")
    subtitle.pack(pady=(0, 30))

    # Entrada - Usuário
    entry_user = ctk.CTkEntry(right_frame, placeholder_text="Usuário", width=300)
    entry_user.pack(pady=10)

    # Entrada - Senha
    entry_senha = ctk.CTkEntry(right_frame, placeholder_text="Senha", show="*", width=300)
    entry_senha.pack(pady=10)

    # Mostrar senha

    variavelCheckBox = ctk.IntVar()

    checkBox_senha = ctk.CTkCheckBox(right_frame, command=mostrar_senha, variable=variavelCheckBox, text='Mostrar senha', text_color='#ffffff', hover_color='gray20', fg_color='gray20')
    checkBox_senha.pack(pady=10)

    def verificar_login():
        usuario = entry_user.get().lower()
        senha = entry_senha.get().lower()

        usuario_banco = session.query(User).filter_by(nome_user=usuario, senha_user=senha).first()

        if usuario_banco:
            abrir_home(janela, frame_atual)
        else:
           retorno = CTkMessagebox(icon='cancel', message='Usuário ou senha incorreto', title='Login incorreto', 
        bg_color='#2B2B2B', fg_color='#2B2B2B', text_color='#EEEEEE', border_color='#2B2B2B', title_color='#EEEEEE', button_color="#00B4D8", button_hover_color='#0096C7', header=True)

    # Botão
    btn_login = ctk.CTkButton(right_frame, text="Entrar", command=verificar_login, width=200, fg_color="#00B4D8", hover_color="#0096C7")
    btn_login.pack(pady=30)

    # Esqueci a senha
    esqueci_b = ctk.CTkButton(right_frame, text="Esqueci a senha", font=("Arial", 12), text_color="gray", fg_color="#1E1E1E", hover_color="#1E1E1E",
                command=lambda: CTkMessagebox(title='Esqueceu a senha?', message='Também não sei a sua senha', bg_color='#2B2B2B', 
                fg_color='#2B2B2B', text_color='#EEEEEE', border_color='#2B2B2B', title_color='#EEEEEE', button_color="#00B4D8", button_hover_color='#0096C7', header=True))
    
    esqueci_b.pack()

    label_versao = ctk.CTkLabel(right_frame, text=versao, font=("Arial", 12), text_color="gray")
    label_versao.pack(pady=50)
    
    # Chamando a função pra atualizar o relogio
    atualizar_relogio()


