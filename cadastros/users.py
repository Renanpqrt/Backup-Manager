import customtkinter as ctk
from util import limpar_tela, resource_path
from dados.tabelas import User, session
from PIL import Image
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox


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
    criar_u.place(relx=0.06, rely=0.045, anchor='center')

    excl_img = Image.open(resource_path("imagens/excluir.png"))
    excl_img = CTkImage(light_image=excl_img, size=(35, 35))

    deletar_u = ctk.CTkButton(frame_atual, image=excl_img, text='', fg_color='#08254b', hover_color='#A9A9A9', command=lambda: deletar_user(frame_atual), width=60)
    deletar_u.place(relx=0.155, rely=0.045, anchor='center')


    for i, conta in enumerate(session.query(User).all()):
        label_user = ctk.CTkLabel(frame_contas, text=conta.nome_user.capitalize(), text_color='white')
        label_user.grid(row=i, column=0, pady=5)

    def criar_user(frame_atual):
        limpar_tela(frame_atual)

        titulo_criar = ctk.CTkLabel(frame_atual, text='Criação de usuários', font=('Arial', 25, 'bold'), text_color='white')
        titulo_criar.place(relx=0.5, rely=0.05, anchor='center')

        entry_user = ctk.CTkEntry(frame_atual, placeholder_text='Digite o usuário')
        entry_user.place(relx=0.5, rely=0.3, anchor='center')

        entry_senha = ctk.CTkEntry(frame_atual, placeholder_text='Digite a senha', show='*')
        entry_senha.place(relx=0.5, rely=0.45, anchor='center')

        def salvar(frame_atual):
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
                        abrir_user(janela, frame_atual)


        b_salvar = ctk.CTkButton(frame_atual, text='Criar', fg_color='Green', hover='Green', width=80, command=lambda: salvar(frame_atual))
        b_salvar.place(relx=0.5, rely=0.60, anchor='n')

        
        voltar_imag = Image.open(resource_path("imagens/voltar.png"))
        voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

        voltar_cadastros = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_user(janela, frame_atual), bg_color='#08254b')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    def deletar_user(frame_atual):
        limpar_tela(frame_atual)        

        titulo_del = ctk.CTkLabel(frame_atual, text='Deletar usuário do app', font=('Arial', 20, 'bold'), text_color='white')
        titulo_del.place(relx=0.5, rely=0.05, anchor='center')


        entry_user = ctk.CTkEntry(frame_atual, placeholder_text='Digite o usuário')
        entry_user.place(relx=0.5, rely=0.2, anchor='center')

        senha_adm = ctk.CTkEntry(frame_atual, placeholder_text='Senha de admin', show='*')
        senha_adm.place(relx=0.5, rely=0.35, anchor='center')

        def delete(frame_atual):
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
                        abrir_user(janela, frame_atual)
                else:
                    retorno = CTkMessagebox(icon='cancel', message='Usuário inexistente', title='Exclusão de usuário (Erro)')

        b_excluir = ctk.CTkButton(frame_atual, text='deletar', fg_color='Red', hover='Red', width=80, command=lambda: delete(frame_atual))
        b_excluir.place(relx=0.5, rely=0.50, anchor='center')

        voltar_imag = Image.open(resource_path("imagens/voltar.png"))
        voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

        voltar_cadastros = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_user(janela, frame_atual), bg_color='#08254b')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')