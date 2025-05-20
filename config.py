import customtkinter as ctk
from util import limpar_tela, criar_user, deletar_user, cadastrar_conta, deletar_conta, resource_path, cadastrar_conta_dados, deletar_conta_dados
from PIL import Image
from customtkinter import CTkImage


def abrir_config(janela, frame_atual):
    from home import abrir_home
    limpar_tela(frame_atual)
    
    fundo = Image.open(resource_path("imagens/fundo1.png"))
    fundo = CTkImage(light_image=fundo, size=(600, 100))

    image_label = ctk.CTkLabel(frame_atual, text='', image=fundo)
    image_label.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.2)

    titulo_config = ctk.CTkLabel(frame_atual, text='Configurações', font=('Helvetica', 24), text_color='white')
    titulo_config.pack(anchor='n', pady=10, padx=0.5)

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_home = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='transparent', hover_color='#A9A9A9', text='', command=lambda: abrir_home(janela, frame_atual))
    voltar_home.place(relx=0.98, rely=0.025, anchor='ne')

    b_criar_user = ctk.CTkButton(frame_atual, text='Criar usuários', text_color='#fffafa', width=90, fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: criar_user(frame_atual))
    b_criar_user.place(relx=0.01, rely=0.2)

    b_deletar_user = ctk.CTkButton(frame_atual, text='Deletar usuários', text_color='#fffafa', width=90, fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: deletar_user(frame_atual))
    b_deletar_user.place(relx=0.01, rely=0.3)

    b_cadastrar_conta = ctk.CTkButton(frame_atual, text='Cadastrar conta', text_color='#fffafa', width=90, fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: cadastrar_conta(frame_atual))
    b_cadastrar_conta.place(relx=0.01, rely=0.4)

    b_deletar_conta = ctk.CTkButton(frame_atual, text='Deletar contas', text_color='#fffafa', width=90, fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: deletar_conta(frame_atual))
    b_deletar_conta.place(relx=0.01, rely=0.5)

    b_cadastrar_dados = ctk.CTkButton(frame_atual, text='Cadastrar contas (Dados)', text_color='#fffafa', width=90, fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: cadastrar_conta_dados(frame_atual))
    b_cadastrar_dados.place(relx=0.01, rely=0.5)

    b_deletar_dados = ctk.CTkButton(frame_atual, text='deletar contas (Dados)', text_color='#fffafa', width=90, fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: deletar_conta_dados(frame_atual))
    b_deletar_dados.place(relx=0.01, rely=0.6)