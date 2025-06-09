import customtkinter as ctk
from util import limpar_area_principal, resource_path
from dados.tabelas import User, session
from PIL import Image
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox


def abrir_user(area_principal):
    from cadastros.cadastro import abrir_cadastros
    limpar_area_principal(area_principal)

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastros(area_principal), bg_color='#1E1E1E')
    voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    titulo_cadastro = ctk.CTkLabel(area_principal, text='Usuários', font=('Helvetica', 30, 'bold'), text_color="#EAEAEA", fg_color='#1E1E1E')
    titulo_cadastro.place(relx=0.5, rely=0.05, anchor='center')

    frame_contas = ctk.CTkScrollableFrame(area_principal, width=700, height=500, fg_color='#1E1E1E')
    frame_contas.place(relx=0.5, rely=0.55, anchor='center')

    criar_img = Image.open(resource_path("imagens/adicionar.png"))
    criar_img = CTkImage(light_image=criar_img, size=(35, 35))

    criar_u = ctk.CTkButton(area_principal, image=criar_img, text='', fg_color='#1E1E1E', hover_color='#A9A9A9', command=lambda: criar_user(area_principal), width=60)
    criar_u.place(relx=0.06, rely=0.045, anchor='center')

    excl_img = Image.open(resource_path("imagens/excluir.png"))
    excl_img = CTkImage(light_image=excl_img, size=(35, 35))

    deletar_u = ctk.CTkButton(area_principal, image=excl_img, text='', fg_color='#1E1E1E', hover_color='#A9A9A9', command=lambda: deletar_user(area_principal), width=60)
    deletar_u.place(relx=0.155, rely=0.045, anchor='center')


    for i, conta in enumerate(session.query(User).all()):
        label_user = ctk.CTkLabel(frame_contas, text=conta.nome_user.capitalize(), text_color='#EAEAEA', font=('Helvetica', 15, 'bold'))
        label_user.grid(row=i, column=0, pady=5)

    def criar_user(area_principal):
        limpar_area_principal(area_principal)

        titulo_criar = ctk.CTkLabel(area_principal, text='Criação de usuários', font=('Arial', 30, 'bold'), text_color='#1b4332')
        titulo_criar.place(relx=0.5, rely=0.05, anchor='center')

        entry_user = ctk.CTkEntry(area_principal, placeholder_text='Digite o usuário')
        entry_user.place(relx=0.5, rely=0.3, anchor='center')

        entry_senha = ctk.CTkEntry(area_principal, placeholder_text='Digite a senha', show='*')
        entry_senha.place(relx=0.5, rely=0.45, anchor='center')

        def salvar(area_principal):
            usuario = entry_user.get().lower()
            senha = entry_senha.get().lower()
            usuario_banco = session.query(User).filter_by(nome_user=usuario).first()

            if len(usuario) == 0 or len(senha) == 0:
                retorno = CTkMessagebox(icon='cancel', message='Preencha todos os campos', title='Criação de usuário (Erro)')
            else:
                if usuario_banco:
                    retorno = CTkMessagebox(icon='cancel', message='Nome de usuário ja existente!', title='Criação de usuário (Erro)')
                else:
                    new_user = User(nome_user=usuario, senha_user=senha)
                    session.add(new_user)
                    session.commit()
                    retorno = CTkMessagebox(icon='check', message='Usuário criado com sucesso!', title='Criação de usuário (Sucesso)')
                    if retorno == "OK":
                        abrir_user(area_principal)


        b_salvar = ctk.CTkButton(area_principal, text='Criar', fg_color='Green', hover='Green', width=80, command=lambda: salvar(area_principal))
        b_salvar.place(relx=0.5, rely=0.60, anchor='n')

        
        voltar_imag = Image.open(resource_path("imagens/voltar.png"))
        voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

        voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_user(area_principal), bg_color='#1E1E1E')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    def deletar_user(area_principal):
        limpar_area_principal(area_principal)        

        titulo_del = ctk.CTkLabel(area_principal, text='Deletar usuário do app', font=('Helvetica', 30, 'bold'), text_color='#1b4332')
        titulo_del.place(relx=0.5, rely=0.05, anchor='center')


        entry_user = ctk.CTkEntry(area_principal, placeholder_text='Digite o usuário')
        entry_user.place(relx=0.5, rely=0.2, anchor='center')

        senha_adm = ctk.CTkEntry(area_principal, placeholder_text='Senha de admin', show='*')
        senha_adm.place(relx=0.5, rely=0.35, anchor='center')

        def delete(area_principal):
            usuario = entry_user.get().lower()
            senha_admin = senha_adm.get().lower()
            usuario_banco = session.query(User).filter_by(nome_user=usuario).first()

            if senha_admin != "administrador123":
                retorno = CTkMessagebox(icon='cancel', message='Senha de administrador incorreta!', title='Exclusão de usuario (Erro)')
            else:
                if usuario_banco:
                    session.delete(usuario_banco)
                    session.commit()
                    retorno = CTkMessagebox(icon='check', message='Usuario excluido com sucesso!', title='Exclusão de usuário (Sucesso)')
                    if retorno.get() == "OK":
                        abrir_user(area_principal)
                else:
                    retorno = CTkMessagebox(icon='cancel', message='Usuário inexistente', title='Exclusão de usuário (Erro)')

        b_excluir = ctk.CTkButton(area_principal, text='deletar', fg_color='Red', hover='Red', width=80, command=lambda: delete(area_principal))
        b_excluir.place(relx=0.5, rely=0.50, anchor='center')

        voltar_imag = Image.open(resource_path("imagens/voltar.png"))
        voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

        voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_user(area_principal), bg_color='#1E1E1E')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')