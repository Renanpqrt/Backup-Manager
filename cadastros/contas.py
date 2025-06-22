import customtkinter as ctk
from util import limpar_area_principal, resource_path, msgbox
from dados.tabelas import Conta, Conta_dados, session
from PIL import Image
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox

senha_exclusão = 'admin123'

def abrir_cadastro_contas(area_principal):
    from cadastros.cadastro import abrir_cadastros
    limpar_area_principal(area_principal)

    titulo = ctk.CTkLabel(area_principal, text='Cadastros De Contas', font=('Helvetica', 30, "bold"), fg_color="#1E1E1E", text_color='#EAEAEA')
    titulo.place(relx=0.5, rely=0.05, anchor='center')

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastros(area_principal), bg_color='#1E1E1E')
    voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    criar_contas = ctk.CTkButton(area_principal, text='Novo', fg_color="#00CA0A", hover_color='#00CA0A', command=lambda: cadastrar_conta(area_principal), width=60, text_color='black')
    criar_contas.place(relx=0.05, rely=0.95, anchor='center')

    alterar_contas = ctk.CTkButton(area_principal, text='Alterar', fg_color="#ffee00", hover_color="#ffee00", width=60, text_color='black', command=lambda: alterar_conta(area_principal))
    alterar_contas.place(relx=0.14, rely=0.95, anchor='center')

    deletar_contas = ctk.CTkButton(area_principal, text='Deletar', fg_color="#fa0000", hover_color="#fa0000", width=60, text_color='black', command=lambda: deletar_conta(area_principal))
    deletar_contas.place(relx=0.23, rely=0.95, anchor='center')

    tabela = ctk.CTkTabview(master=area_principal, width=700, height=400, fg_color="#1E1E1E", segmented_button_fg_color="#1E1E1E",
    segmented_button_selected_color="#011125", segmented_button_selected_hover_color="#011125", segmented_button_unselected_color="gray20", segmented_button_unselected_hover_color="gray20")
    
    tabela.place(relx=0.5, rely=0.5, anchor='center')

    tabela.add("Contas")  
    tabela.add("Contas de dados")
    tabela.set("Contas")

    aba_contas = tabela.tab("Contas")
    aba_contas_dados = tabela.tab("Contas de dados")

    frame_contas = ctk.CTkScrollableFrame(aba_contas, width=700, height=400, fg_color='#1E1E1E')
    frame_contas.pack(padx=0, pady=0, fill="both", expand=True)

    frame_dados = ctk.CTkScrollableFrame(aba_contas_dados, width=700, height=400, fg_color='#1E1E1E')
    frame_dados.pack(padx=0, pady=0, fill="both", expand=True)

    checkbox_vars_contas = []
    checkbox_widgets_contas = []

    checkbox_vars_dados = []
    checkbox_widgets_dados = []


    def on_checkbox_click(clicked_var, group_vars):
        for var in group_vars:
            if var != clicked_var:
                var.set(False)

    for i, conta in enumerate(session.query(Conta).all()):
        label_c = ctk.CTkLabel(frame_contas, text=conta.nome.capitalize(), text_color='#EAEAEA', font=('Helvetica', 15, 'bold'))
        label_c.grid(row=i, column=1, padx=10, pady=5)

        label_e = ctk.CTkLabel(frame_contas, text=conta.email.capitalize(), text_color="#EAEAEA", font=('Helvetica', 15, 'bold'))
        label_e.grid(row=i, column=2, padx=10, pady=5)

        var = ctk.BooleanVar()
        selecionar = ctk.CTkCheckBox(frame_contas, variable=var, command=lambda v=var: on_checkbox_click(v, checkbox_vars_contas), hover_color='gray20', fg_color='gray20', text='')
        selecionar.grid(row=i, column=0, padx=5, pady=5)
        checkbox_vars_contas.append(var)
        checkbox_widgets_contas.append(conta)

    for i, conta in enumerate(session.query(Conta_dados).all()):
        label_c = ctk.CTkLabel(frame_dados, text=conta.nome.capitalize(), text_color='#EAEAEA', font=('Helvetica', 15, 'bold'))
        label_c.grid(row=i, column=1, padx=10, pady=5)

        label_e = ctk.CTkLabel(frame_dados, text=conta.email.capitalize(), text_color="#EAEAEA", font=('Helvetica', 15, 'bold'))
        label_e.grid(row=i, column=2, padx=10, pady=5)

        var = ctk.BooleanVar()
        selecionar = ctk.CTkCheckBox(frame_dados, variable=var, command=lambda v=var: on_checkbox_click(v, checkbox_vars_dados), hover_color='gray20', fg_color='gray20')
        selecionar.grid(row=i, column=0, padx=5, pady=5)
        checkbox_vars_dados.append(var)
        checkbox_widgets_dados.append(conta)

    # Cadastros
    def cadastrar_conta(area_principal):
        limpar_area_principal(area_principal)

        titulo_cadastro = ctk.CTkLabel(area_principal, text='Criação de contas', font=('Helvetica', 30, 'bold'), text_color='#EAEAEA')
        titulo_cadastro.place(relx=0.5, rely=0.04, anchor='center')

        tabela = ctk.CTkTabview(master=area_principal, width=550, height=400, fg_color="#1E1E1E", segmented_button_fg_color="#1E1E1E",
    segmented_button_selected_color="#011125", segmented_button_selected_hover_color="#011125", segmented_button_unselected_color="gray20", segmented_button_unselected_hover_color="gray20")
    
        tabela.place(relx=0.5, rely=0.5, anchor='center')

        tabela.add("Contas")  
        tabela.add("Contas de dados")
        tabela.set("Contas")

        voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastro_contas(area_principal), bg_color='#1E1E1E')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

        # Cadastro de contas
        entry_nome = ctk.CTkEntry(tabela.tab('Contas'), placeholder_text='Digite o nome')
        entry_nome.place(relx=0.5, rely=0.1, anchor='center')

        entry_email = ctk.CTkEntry(tabela.tab('Contas'), placeholder_text='Digite o email')
        entry_email.place(relx=0.5, rely=0.23, anchor='center')

        entry_ultimobkp = ctk.CTkEntry(tabela.tab('Contas'), placeholder_text='Data do ultimo BKP')
        entry_ultimobkp.place(relx=0.5, rely=0.37, anchor='center')

        entry_segundobkp = ctk.CTkEntry(tabela.tab('Contas'), placeholder_text='Digite segundo BKP')
        entry_segundobkp.place(relx=0.5, rely=0.52, anchor='center')

        def salvar():
            nome = entry_nome.get().lower()
            email = entry_email.get().lower()
            ultimo_bkp = entry_ultimobkp.get().lower()
            segundo_bkp = entry_segundobkp.get().lower()

            if len(nome) == 0 or len(email) == 0:
                retorno = msgbox(message='PREENCHA TODOS OS CAMPOS OBRIGATÓRIOS!', title='INCONSISTÊNCIA')
            else:
                new_conta = Conta(nome=nome, email=email, ultimo_bkp=ultimo_bkp, segundo_backup=segundo_bkp)
                session.add(new_conta)
                session.commit()
                retorno = msgbox(icon='check', message='Conta cadastrada com sucesso!', title='Criação de conta (Sucesso)')

                entry_nome.delete(0, 'end')
                entry_email.delete(0, 'end')
                entry_ultimobkp.delete(0, 'end')
                entry_segundobkp.delete(0, 'end')
            
        b_salvar = ctk.CTkButton(tabela.tab('Contas'), text='Cadastrar', fg_color='Green', hover_color='Green', width=80, command=salvar)
        b_salvar.place(relx=0.5, rely=0.67, anchor='center')

        # Cadastro de contas de dados
        entry_nome_d = ctk.CTkEntry(tabela.tab('Contas de dados'), placeholder_text='Digite o nome')
        entry_nome_d.place(relx=0.5, rely=0.1, anchor='center')

        entry_email_d = ctk.CTkEntry(tabela.tab('Contas de dados'), placeholder_text='Digite o email')
        entry_email_d.place(relx=0.5, rely=0.23, anchor='center')

        entry_ultimobkp_d = ctk.CTkEntry(tabela.tab('Contas de dados'), placeholder_text='Data do ultimo BKP')
        entry_ultimobkp_d.place(relx=0.5, rely=0.37, anchor='center')

        entry_obs = ctk.CTkEntry(tabela.tab('Contas de dados'), placeholder_text='Digite a observação')
        entry_obs.place(relx=0.5, rely=0.52, anchor='center')
        
        def salvar_dados():
            nome = entry_nome_d.get().lower()
            email = entry_email_d.get().lower()
            ultimo_bkp = entry_ultimobkp_d.get().lower()
            obs = entry_obs.get().lower()

            if len(nome) == 0 or len(email) == 0:
                retorno = msgbox(title="INCONSISTÊNCIA", message='PREENCHA TODOS OS CAMPOS OBRIGATÓRIOS!')
            else:
                new_conta = Conta_dados(nome=nome, email=email, ultimo_bkp=ultimo_bkp, obs=obs)
                session.add(new_conta)
                session.commit()
                retorno = msgbox(icon='check', message='Conta cadastrada com sucesso!', title='Criação de conta (Dados) (Sucesso)')

                entry_nome_d.delete(0, 'end')
                entry_email_d.delete(0, 'end')
                entry_ultimobkp_d.delete(0, 'end')
                entry_obs.delete(0, 'end')
                
        b_salvar = ctk.CTkButton(tabela.tab('Contas de dados'), text='Cadastrar', fg_color='Green', hover_color='Green', width=80, command=lambda: salvar_dados())
        b_salvar.place(relx=0.5, rely=0.67, anchor='center')

    def alterar_conta(area_principal):
        selecionados_contas = [(var, conta) for var, conta in zip(checkbox_vars_contas, checkbox_widgets_contas) if var.get()]
        selecionados_dados = [(var, conta) for var, conta in zip(checkbox_vars_dados, checkbox_widgets_dados) if var.get()]

        if len(selecionados_contas) == 0 and len(selecionados_dados) == 0:
            retorno = msgbox(title='INCONSISTÊNCIA', message='SELECIONE UMA CONTA PARA ALTERAR')
            return

        if len(selecionados_contas) > 0:
            _, conta = selecionados_contas[0]
        else:
            _, conta = selecionados_dados[0]

        limpar_area_principal(area_principal)

        voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastro_contas(area_principal), bg_color='#1E1E1E')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

        titulo_cadastro = ctk.CTkLabel(area_principal, text='Alteração de contas', font=('Helvetica', 30, 'bold'), text_color='#EAEAEA')
        titulo_cadastro.place(relx=0.5, rely=0.04, anchor='center')

        # Mini cabeçalho
        id_header = ctk.CTkLabel(area_principal, text=conta.id, font=('Helvetica', 20, 'bold'), text_color="#C0C0C0")
        id_header.place(relx=0.1, rely=0.15, anchor='center')

        nome_header = ctk.CTkLabel(area_principal, text=conta.nome.capitalize(), font=('Helvetica', 20, 'bold'), text_color='#C0C0C0')
        nome_header.place(relx=0.5, rely=0.15, anchor='center')

        # Entry das contas
        entry_nome = ctk.CTkEntry(area_principal, placeholder_text='Digite o nome', width=500)
        entry_nome.place(relx=0.5, rely=0.33, anchor='center')
        entry_nome.insert(0, conta.nome)

        entry_email = ctk.CTkEntry(area_principal, placeholder_text='Digite o email', width=500)
        entry_email.place(relx=0.5, rely=0.43, anchor='center')
        entry_email.insert(0, conta.email)

        def salvar_alteraçao(area_principal):
            nome_novo = entry_nome.get().lower()
            email_novo = entry_email.get().lower()

            if len(nome_novo) == 0 or len(email_novo) == 0:
                retorno = msgbox(title='INCONSISTÊNCIA', message='PREENCHA TODOS OS CAMPOS')
            else:
                conta.nome = nome_novo
                conta.email = email_novo 
                session.commit()

                abrir_cadastro_contas(area_principal)

        b_salvar = ctk.CTkButton(area_principal, text='Salvar', fg_color="green", hover_color="green", command=lambda: salvar_alteraçao(area_principal))
        b_salvar.place(relx=0.5, rely=0.53, anchor='center')

    def deletar_conta(area_principal):
        selecionados_contas = [(var, conta) for var, conta in zip(checkbox_vars_contas, checkbox_widgets_contas) if var.get()]
        selecionados_dados = [(var, conta) for var, conta in zip(checkbox_vars_dados, checkbox_widgets_dados) if var.get()]

        if len(selecionados_contas) == 0 and len(selecionados_dados) == 0:
            retorno = msgbox(title='INCONSISTÊNCIA', message='SELECIONE UMA CONTA PARA DELETAR!')
            return

        if len(selecionados_contas) > 0:
            _, conta = selecionados_contas[0]
        else:
            _, conta = selecionados_dados[0]

        limpar_area_principal(area_principal)

        voltar_cadastros = ctk.CTkButton(area_principal, image=voltar_imag, width=80, fg_color='#1E1E1E', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastro_contas(area_principal), bg_color='#1E1E1E')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

        titulo_cadastro = ctk.CTkLabel(area_principal, text='Exclusão de conta', font=('Helvetica', 30, 'bold'), text_color='#EAEAEA')
        titulo_cadastro.place(relx=0.5, rely=0.04, anchor='center')

        id_header = ctk.CTkLabel(area_principal, text=conta.id, font=('Helvetica', 20, 'bold'), text_color="#C0C0C0")
        id_header.place(relx=0.1, rely=0.15, anchor='center')

        nome_header = ctk.CTkLabel(area_principal, text=conta.nome.capitalize(), font=('Helvetica', 20, 'bold'), text_color='#C0C0C0')
        nome_header.place(relx=0.5, rely=0.15, anchor='center')

        entry_adm = ctk.CTkEntry(area_principal, placeholder_text='Digite a senha de administrador', width=500, show='*')
        entry_adm.place(relx=0.5, rely=0.33, anchor='center')

        def confirmar_delecao():
            senha = entry_adm.get()
            if senha != senha_exclusão:
                retorno = msgbox(title='ERRO', message='Senha incorreta!')
                return
            session.delete(conta)
            session.commit()
            abrir_cadastro_contas(area_principal)
            retorno = msgbox(icon='check', title='Sucesso', message='Conta deletada com sucesso!')

        b_deletar = ctk.CTkButton(area_principal, text='Deletar', fg_color="red", hover_color="red", command=confirmar_delecao)
        b_deletar.place(relx=0.5, rely=0.43, anchor='center')

