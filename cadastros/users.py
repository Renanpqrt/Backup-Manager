import customtkinter as ctk
from util import limpar_tela, resource_path, criar_user, deletar_user
from dados.tabelas import User, session
from PIL import Image
from customtkinter import CTkImage


def abrir_user(janela, frame_atual):
    from cadastros.cadastro import abrir_cadastros
    limpar_tela(frame_atual)

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_cadastros = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastros(janela, frame_atual), bg_color='#08254b')
    voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    titulo_cadastro = ctk.CTkLabel(frame_atual, text='Usuários', font=('Helvetica', 25, 'bold'), text_color="#FFFFFF", fg_color='#08254b')
    titulo_cadastro.place(relx=0.5, rely=0.05, anchor='center')

    frame_contas = ctk.CTkScrollableFrame(frame_atual, width=520, height=325, fg_color='#08254b')
    frame_contas.place(relx=0.5, rely=0.55, anchor='center')

    criar_img = Image.open(resource_path("imagens/adicionar.png"))
    criar_img = CTkImage(light_image=criar_img, size=(35, 35))

    criar_u = ctk.CTkButton(frame_atual, image=criar_img, text='', fg_color='#08254b', hover_color='#A9A9A9', command=lambda: criar_user(frame_atual), width=60)
    criar_u.place(relx=0.06, rely=0.072, anchor='center')


    for i, conta in enumerate(session.query(User).all()):
        label_user = ctk.CTkLabel(frame_contas, text=conta.nome_user.capitalize(), text_color='white')
        label_user.grid(row=i, column=0, pady=5)