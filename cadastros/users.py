import customtkinter as ctk
from util import limpar_area_principal, resource_path, msgbox
from dados.tabelas import User, session
from PIL import Image
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox

senha_exclusão = 'admin123'

def abrir_user(area_principal):
    from cadastros.cadastro import abrir_cadastros
    limpar_area_principal(area_principal)

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastros(area_principal), bg_color='#1E1E1E')
    voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    titulo_cadastro = ctk.CTkLabel(area_principal, text='Usuários', font=('Helvetica', 30, 'bold'), text_color="#EAEAEA", fg_color='#1E1E1E')
    titulo_cadastro.place(relx=0.5, rely=0.05, anchor='center')

    criar_usuarios = ctk.CTkButton(area_principal, text='Novo', fg_color="#00CA0A", hover_color='#00CA0A', command=lambda: criar_user(area_principal), width=60, text_color='black')
    criar_usuarios.place(relx=0.05, rely=0.95, anchor='center')

    alterar_usuarios = ctk.CTkButton(area_principal, text='Alterar', fg_color="#ffee00", hover_color="#ffee00", width=60, text_color='black', command=lambda: alterar_user(area_principal))
    alterar_usuarios.place(relx=0.14, rely=0.95, anchor='center')

    deletar_usuarios = ctk.CTkButton(area_principal, text='Deletar', fg_color="#fa0000", hover_color="#fa0000", width=60, text_color='black', command=lambda: deletar_user(area_principal))
    deletar_usuarios.place(relx=0.23, rely=0.95, anchor='center')

    frame_contas = ctk.CTkScrollableFrame(area_principal, width=700, height=400, fg_color='#1E1E1E')
    frame_contas.place(relx=0.5, rely=0.55, anchor='center')

    checkbox_vars = []
    checkbox_widgets = []


    def on_checkbox_click(clicked_var):
        for var in checkbox_vars:
            if var != clicked_var:
                var.set(False)

    for i, user in enumerate(session.query(User).all()):
        label_user = ctk.CTkLabel(frame_contas, text=user.nome_user.capitalize(), text_color='#EAEAEA', font=('Helvetica', 15, 'bold'))
        label_user.grid(row=i, column=1, pady=5)
        var = ctk.BooleanVar()
        selecionar = ctk.CTkCheckBox(frame_contas, variable=var, command=lambda v=var: on_checkbox_click(v), hover_color='gray20', fg_color='gray20', text='')
        selecionar.grid(row=i, column=0, padx=5, pady=5)
        checkbox_vars.append(var)
        checkbox_widgets.append(user)

    def criar_user(area_principal):
        limpar_area_principal(area_principal)

        titulo_criar = ctk.CTkLabel(area_principal, text='Criação de usuários', font=('Arial', 30, 'bold'), text_color='#EAEAEA')
        titulo_criar.place(relx=0.5, rely=0.05, anchor='center')

        entry_user = ctk.CTkEntry(area_principal, placeholder_text='Digite o usuário', width=500)
        entry_user.place(relx=0.5, rely=0.3, anchor='center')

        entry_senha = ctk.CTkEntry(area_principal, placeholder_text='Digite a senha', show='*', width=500)
        entry_senha.place(relx=0.5, rely=0.45, anchor='center')

        def salvar(area_principal):
            usuario = entry_user.get().lower()
            senha = entry_senha.get().lower()
            usuario_banco = session.query(User).filter_by(nome_user=usuario).first()

            if len(usuario) == 0 or len(senha) == 0:
                retorno = CTkMessagebox(icon='cancel', message='Preencha todos os campos', title='Criação de usuário (Erro)')
            else:
                if usuario_banco:
                    retorno = msgbox(icon='cancel', message='USUÁRIO JA EXISTENTE!', title='Criação de usuário (Erro)')
                else:
                    new_user = User(nome_user=usuario, senha_user=senha)
                    session.add(new_user)
                    session.commit()
                    abrir_user(area_principal)
                    retorno = msgbox(icon='check', message='USUÁRIO CADASTRADO COM SUCESSO!', title='Criação de usuário (Sucesso)')


        b_salvar = ctk.CTkButton(area_principal, text='Criar', fg_color='Green', hover='Green', width=80, command=lambda: salvar(area_principal))
        b_salvar.place(relx=0.5, rely=0.60, anchor='n')

        voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_user(area_principal), bg_color='#1E1E1E')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    def alterar_user(area_principal):
        selecionado = [(var, user) for var, user in zip(checkbox_vars, checkbox_widgets) if var.get() == True]

        if len(selecionado) == 0:
            retorno = msgbox(title="INCONSISTÊNCIA", message='SELECIONE UM USUÁRIO PARA ALTERAR')
        else:
            limpar_area_principal(area_principal)
            user_selecionado = selecionado[0][1]

            titulo_alterar = ctk.CTkLabel(area_principal, text='Alterar usuário', font=('Helvetica', 30, 'bold'), text_color='#EAEAEA')
            titulo_alterar.place(relx=0.5, rely=0.05, anchor='center')
            
            voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_user(area_principal), bg_color='#1E1E1E')
            voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

            # Mini cabeçalho
            id_header = ctk.CTkLabel(area_principal, text=user_selecionado.id, font=('Helvetica', 20, 'bold'), text_color="#C0C0C0")
            id_header.place(relx=0.1, rely=0.15, anchor='center')

            user_header = ctk.CTkLabel(area_principal, text=user_selecionado.nome_user.capitalize(), font=('Helvetica', 20, 'bold'), text_color='#C0C0C0')
            user_header.place(relx=0.5, rely=0.15, anchor='center')

            # Entrys
            entry_user = ctk.CTkEntry(area_principal, placeholder_text='Digite o nome de usuário', width=500)
            entry_user.place(relx=0.5, rely=0.33, anchor='center')
            entry_user.insert(0, user_selecionado.nome_user)

            entry_senha = ctk.CTkEntry(area_principal, placeholder_text='Digite a senha do usuário', width=500, show='*')
            entry_senha.place(relx=0.5, rely=0.43, anchor='center')
            entry_senha.insert(0, user_selecionado.senha_user)

            def salvar_alteraçao(area_principal):
                nome_novo = entry_user.get().lower()
                senha_nova = entry_senha.get().lower()

                if len(nome_novo) == 0 or len(senha_nova) == 0:
                    retorno = msgbox(title='INCONSISTÊNCIA', message='PREENCHA TODOS OS CAMPOS')
                else:
                    user_selecionado.nome_user = nome_novo
                    user_selecionado.senha_user = senha_nova 
                    session.commit()

                    abrir_user(area_principal)
                    retorno = msgbox(title="ALTERAÇÃO", message="USUÁRIO ALTERADO COM SUCESSO!", icon='check')

        b_salvar = ctk.CTkButton(area_principal, text='Salvar', fg_color="green", hover_color="green", command=lambda: salvar_alteraçao(area_principal))
        b_salvar.place(relx=0.5, rely=0.53, anchor='center')

    def deletar_user(area_principal):   
        selecionado = [(var, user) for var, user in zip(checkbox_vars, checkbox_widgets) if var.get() == True]
        
        if len(selecionado) == 0:
            retorno = msgbox(title='INCONSISTÊNCIA', message='SELECIONE UM USUÁRIO PARA DELETAR')
        else:
            limpar_area_principal(area_principal)     
            user_selecionado = selecionado[0][1]
            titulo_del = ctk.CTkLabel(area_principal, text='Deletar usuário do app', font=('Helvetica', 30, 'bold'), text_color='#EAEAEA')
            titulo_del.place(relx=0.5, rely=0.05, anchor='center')

            # Mini cabeçalho
            id_header = ctk.CTkLabel(area_principal, text=user_selecionado.id, font=('Helvetica', 20, 'bold'), text_color="#C0C0C0")
            id_header.place(relx=0.1, rely=0.15, anchor='center')

            user_header = ctk.CTkLabel(area_principal, text=user_selecionado.nome_user.capitalize(), font=('Helvetica', 20, 'bold'), text_color='#C0C0C0')
            user_header.place(relx=0.5, rely=0.15, anchor='center')

            # Entry da senha
            senha_adm = ctk.CTkEntry(area_principal, placeholder_text='Senha de admin', show='*', width=500)
            senha_adm.place(relx=0.5, rely=0.35, anchor='center')

            def delete(area_principal):
                senha_admin = senha_adm.get().lower()

                if senha_admin != senha_exclusão:
                    retorno = CTkMessagebox(icon='cancel', message='Senha de administrador incorreta!', title='Exclusão de usuario (Erro)')
                else:
                    session.delete(user_selecionado)
                    session.commit()
                    abrir_user(area_principal)
                    retorno = msgbox(title='Exclusão de usuários', message="USUÁRIO EXCLUIDO COM SUCESSO", icon='check')
        
            b_excluir = ctk.CTkButton(area_principal, text='deletar', fg_color='Red', hover='Red', width=80, command=lambda: delete(area_principal))
            b_excluir.place(relx=0.5, rely=0.50, anchor='center')

            voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_user(area_principal), bg_color='#1E1E1E')
            voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')