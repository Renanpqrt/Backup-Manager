import customtkinter as ctk
from util import limpar_tela, resource_path
from dados.tabelas import Conta, Conta_dados, session
from PIL import Image
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox

def abrir_cadastro_contas(janela, frame_atual):
    from cadastros.cadastro import abrir_cadastros
    limpar_tela(frame_atual)

    titulo = ctk.CTkLabel(frame_atual, text='Cadastros De Contas', font=('Arial', 20, "bold"), fg_color="#08254b", text_color='white')
    titulo.place(relx=0.5, rely=0.05, anchor='center')

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_cadastros = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastros(janela, frame_atual), bg_color='#08254b')
    voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    criar_img = Image.open(resource_path("imagens/adicionar.png"))
    criar_img = CTkImage(light_image=criar_img, size=(35, 35))

    criar_u = ctk.CTkButton(frame_atual, image=criar_img, text='', fg_color='#08254b', hover_color='#A9A9A9', command=lambda: cadastrar_conta(frame_atual), width=60)
    criar_u.place(relx=0.06, rely=0.045, anchor='center')

    excl_img = Image.open(resource_path("imagens/excluir.png"))
    excl_img = CTkImage(light_image=excl_img, size=(35, 35))

    deletar_u = ctk.CTkButton(frame_atual, image=excl_img, text='', fg_color='#08254b', hover_color='#A9A9A9', command=lambda: deletar_contas(frame_atual), width=60)
    deletar_u.place(relx=0.155, rely=0.045, anchor='center')

    tabela = ctk.CTkTabview(master=frame_atual, width=550, height=335, fg_color="#08254b", segmented_button_fg_color="#08254b",
    segmented_button_selected_color="#011125", segmented_button_selected_hover_color="#011125", segmented_button_unselected_color="gray20", segmented_button_unselected_hover_color="gray20")
    
    tabela.place(relx=0.5, rely=0.5, anchor='center')

    tabela.add("Contas")  
    tabela.add("Contas de dados")
    tabela.set("Contas")

    aba_contas = tabela.tab("Contas")
    aba_contas_dados = tabela.tab("Contas de dados")

    frame_contas = ctk.CTkScrollableFrame(aba_contas, width=525, height=335, fg_color='#08254b')
    frame_contas.pack(padx=0, pady=0, fill="both", expand=True)

    frame_dados = ctk.CTkScrollableFrame(aba_contas_dados, width=525, height=335, fg_color='#08254b')
    frame_dados.pack(padx=0, pady=0, fill="both", expand=True)

    for i, conta in enumerate(session.query(Conta).all()):
        label_c = ctk.CTkLabel(frame_contas, text=conta.nome.capitalize(), text_color='white')
        label_c.grid(row=i, column=0, padx=10, pady=5)

    for i, conta in enumerate(session.query(Conta_dados).all()):
        label_c = ctk.CTkLabel(frame_dados, text=conta.nome.capitalize(), text_color='white')
        label_c.grid(row=i, column=0, padx=10, pady=5)
    
    # Cadastros
    def cadastrar_conta(frame_atual):
        limpar_tela(frame_atual)

        titulo_cadastro = ctk.CTkLabel(frame_atual, text='Criação de contas', font=('Arial', 20, 'bold'), text_color='white')
        titulo_cadastro.place(relx=0.5, rely=0.04, anchor='center')

        tabela = ctk.CTkTabview(master=frame_atual, width=550, height=400, fg_color="#08254b", segmented_button_fg_color="#08254b",
    segmented_button_selected_color="#011125", segmented_button_selected_hover_color="#011125", segmented_button_unselected_color="gray20", segmented_button_unselected_hover_color="gray20")
    
        tabela.place(relx=0.5, rely=0.5, anchor='center')

        tabela.add("Contas")  
        tabela.add("Contas de dados")
        tabela.set("Contas")

        voltar_imag = Image.open(resource_path("imagens/voltar.png"))
        voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

        voltar_cadastros = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastro_contas(janela, frame_atual), bg_color='#08254b')
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

        def salvar(frame_atual):
            nome = entry_nome.get().lower()
            email = entry_email.get().lower()
            ultimo_bkp = entry_ultimobkp.get().lower()
            segundo_bkp = entry_segundobkp.get().lower()

            if len(nome) == 0 or len(email) == 0:
                retorno = CTkMessagebox(icon='cancel', message='Preencha todos os campos obrigatórios!', title='Cadastro de conta (Erro)')
            else:
                new_conta = Conta(nome=nome, email=email, ultimo_bkp=ultimo_bkp, segundo_backup=segundo_bkp)
                session.add(new_conta)
                session.commit()
                retorno = CTkMessagebox(icon='check', message='Conta cadastrada com sucesso!', title='Criação de conta (Sucesso)')

                entry_nome.delete(0, 'end')
                entry_email.delete(0, 'end')
                entry_ultimobkp.delete(0, 'end')
                entry_segundobkp.delete(0, 'end')
            
        b_salvar = ctk.CTkButton(tabela.tab('Contas'), text='Cadastrar', fg_color='Green', hover_color='Green', width=80, command=lambda: salvar(frame_atual))
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
        
        def salvar_dados(frame_atual):
            nome = entry_nome_d.get().lower()
            email = entry_email_d.get().lower()
            ultimo_bkp = entry_ultimobkp_d.get().lower()
            obs = entry_obs.get().lower()

            if len(nome) == 0 or len(email) == 0:
                retorno = CTkMessagebox(icon='cancel', message='Preencha todos os campos obrigatórios!', title='Cadastro de conta (Erro)')
            else:
                new_conta = Conta_dados(nome=nome, email=email, ultimo_bkp=ultimo_bkp, obs=obs)
                session.add(new_conta)
                session.commit()
                retorno = CTkMessagebox(icon='check', message='Conta cadastrada com sucesso!', title='Criação de conta (Dados) (Sucesso)')

                entry_nome_d.delete(0, 'end')
                entry_email_d.delete(0, 'end')
                entry_ultimobkp_d.delete(0, 'end')
                entry_obs.delete(0, 'end')
                
        b_salvar = ctk.CTkButton(tabela.tab('Contas de dados'), text='Cadastrar', fg_color='Green', hover_color='Green', width=80, command=lambda: salvar_dados(frame_atual))
        b_salvar.place(relx=0.5, rely=0.67, anchor='center')

    def deletar_contas(frame_atual):
        limpar_tela(frame_atual)

        titulo_cadastro = ctk.CTkLabel(frame_atual, text='Criação de contas', font=('Arial', 20, 'bold'), text_color='white')
        titulo_cadastro.place(relx=0.5, rely=0.04, anchor='center')

        tabela = ctk.CTkTabview(master=frame_atual, width=550, height=400, fg_color="#08254b", segmented_button_fg_color="#08254b",
    segmented_button_selected_color="#011125", segmented_button_selected_hover_color="#011125", segmented_button_unselected_color="gray20", segmented_button_unselected_hover_color="gray20")
    
        tabela.place(relx=0.5, rely=0.5, anchor='center')

        tabela.add("Contas")  
        tabela.add("Contas de dados")
        tabela.set("Contas")

        voltar_imag = Image.open(resource_path("imagens/voltar.png"))
        voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

        voltar_cadastros = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastro_contas(janela, frame_atual), bg_color='#08254b')
        voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

        # deletar contas

        entry_nome = ctk.CTkEntry(tabela.tab('Contas'), placeholder_text='Digite o nome')
        entry_nome.place(relx=0.5, rely=0.1, anchor='center')

        senha_adm = ctk.CTkEntry(tabela.tab('Contas'), placeholder_text='Digite a senha de adm')
        senha_adm.place(relx=0.5, rely=0.23, anchor='center')

        def delete(frame_atual):
            conta = entry_nome.get().lower()
            senha_admin = senha_adm.get().lower()
            conta_banco = session.query(Conta).filter_by(nome=conta).first()

            if senha_admin != "administrador123":
                retorno = CTkMessagebox(icon='cancel', message='Senha de administrador incorreta!', title='Exclusão de contas (Erro)')
            else:
                if conta_banco:
                    session.delete(conta_banco)
                    session.commit()
                    retorno = CTkMessagebox(icon='check', message='Conta excluida com sucesso!', title='Exclusão de contas (Sucesso)')
                    
                    entry_nome.delete(0, 'end')
                    senha_adm.delete(0, 'end')
                else:
                    retorno = CTkMessagebox(icon='cancel', message='Conta inexistente', title='Exclusão de contas (Erro)')
        
        b_deletar = ctk.CTkButton(tabela.tab('Contas'), text='Deletar', fg_color='red', hover_color='red', width=80, command=lambda: delete(frame_atual))
        b_deletar.place(relx=0.5, rely=0.37, anchor='center')

        # Deletar conta dados

        entry_nome_d = ctk.CTkEntry(tabela.tab('Contas de dados'), placeholder_text='Digite o nome')
        entry_nome_d.place(relx=0.5, rely=0.1, anchor='center')

        senha_adm_d = ctk.CTkEntry(tabela.tab('Contas de dados'), placeholder_text='Digite a senha de adm')
        senha_adm_d.place(relx=0.5, rely=0.23, anchor='center')

        def delete(frame_atual):
            conta = entry_nome_d.get().lower()
            senha_admin = senha_adm_d.get().lower()
            conta_banco = session.query(Conta_dados).filter_by(nome=conta).first()

            if senha_admin != "administrador123":
                retorno = CTkMessagebox(icon='cancel', message='Senha de administrador incorreta!', title='Exclusão de contas (Erro)')
            else:
                if conta_banco:
                    session.delete(conta_banco)
                    session.commit()
                    retorno = CTkMessagebox(icon='check', message='Conta excluida com sucesso!', title='Exclusão de contas (Sucesso)')
                    
                    entry_nome_d.delete(0, 'end')
                    senha_adm_d.delete(0, 'end')
                else:
                    retorno = CTkMessagebox(icon='cancel', message='Conta inexistente', title='Exclusão de contas (Erro)')
        
        b_deletar_d = ctk.CTkButton(tabela.tab('Contas de dados'), text='Deletar', fg_color='red', hover_color='red', width=80, command=lambda: delete(frame_atual))
        b_deletar_d.place(relx=0.5, rely=0.37, anchor='center')
