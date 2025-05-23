import customtkinter as ctk
from dados.tabelas import Conta_dados, session
from datetime import date, timedelta, datetime
from util import b_exportar2, resource_path


def iniciar_backup(frame_atual, janela):
    bkp = ctk.CTkToplevel()
    bkp.geometry('1000x900')
    bkp.configure(fg_color='#111530')
    bkp.wm_attributes('-topmost', 1)
    bkp.title('Backups de dados (Em andamento)')
    
    texto = ctk.CTkLabel(bkp, text='Iniciando Backups (Dados)', text_color='white', font=('Arial', 25))
    texto.place(relx=0.5, rely=0.05, anchor='center')

    export = ctk.CTkButton(bkp, text='Exportar dados', width=80, fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: b_exportar2(frame_atual, janela))
    export.place(relx=0.1, rely=0.05, anchor='center')

    frame_conta = ctk.CTkScrollableFrame(bkp, fg_color='#111530')
    frame_conta.place(relx=0.5, rely=0.55, anchor='center', relwidth=1, relheight=0.95)

    def atualizar_data_hoje(e, id):
        e.configure(fg_color='gray20')
        hoje = date.today().strftime("%d/%m/%Y")
        e.delete(0, 'end')
        e.insert(0, hoje)

        conta_db = session.query(Conta_dados).get(id)
        conta_db.ultimo_bkp = hoje
        session.commit()

    def atualizar_data_ontem(e, id):
        e.configure(fg_color='gray20')
        ontem = (date.today() - timedelta(days=1)).strftime("%d/%m/%Y")

        e.delete(0, 'end')
        e.insert(0, ontem)

        conta_db = session.query(Conta_dados).get(id)
        conta_db.ultimo_bkp = ontem
        session.commit()

    def salvar_ultimobkp(e, id):
        e.configure(fg_color='gray20')
        valor = e.get()

        conta_db = session.query(Conta_dados).get(id)
        conta_db.ultimo_bkp = valor
        session.commit()

    def salvar_obs(e, id):
        e.configure(fg_color='gray20')
        valor = e.get()

        conta_db = session.query(Conta_dados).get(id)
        conta_db.obs = valor
        session.commit()


    for i, conta in enumerate(session.query(Conta_dados).all()):
        label_nome = ctk.CTkLabel(frame_conta, text=conta.nome.capitalize(), text_color='white')
        label_nome.grid(row=i, column=0, padx=5, pady=5)

        label_email = ctk.CTkLabel(frame_conta, text=conta.email, text_color='white')
        label_email.grid(row=i, column=1, padx=10, pady=5)

        entry_ultimobkp = ctk.CTkEntry(frame_conta, width=100)
        entry_ultimobkp.insert(0, conta.ultimo_bkp)
        entry_ultimobkp.grid(row=i, column=2, padx=10, pady=5)
        entry_ultimobkp.bind('<Return>', lambda event, e=entry_ultimobkp, id=conta.id: salvar_ultimobkp(e, id))

        entry_obs = ctk.CTkEntry(frame_conta, width=100)
        entry_obs.insert(0, conta.obs)
        entry_obs.grid(row=i, column=3, padx=10, pady=5)
        entry_obs.bind('<Return>', lambda event, e=entry_obs, id=conta.id: salvar_obs(e, id))

        b_hoje = ctk.CTkButton(frame_conta, text='Hoje', width=80, fg_color='gray20', hover_color='gray20', command=lambda e=entry_ultimobkp, id=conta.id: atualizar_data_hoje(e, id))
        b_hoje.grid(row=i, column=4, padx=10, pady=5)

        b_ontem = ctk.CTkButton(frame_conta, text='Ontem', width=80, fg_color='gray20', hover_color='gray20', command=lambda e=entry_ultimobkp, id=conta.id: atualizar_data_ontem(e, id))
        b_ontem.grid(row=i, column=5, padx=10, pady=5)

        b_verde = ctk.CTkButton(frame_conta, text='✔', width=60, fg_color='gray20', hover_color='gray20', command=lambda e=entry_ultimobkp: e.configure(fg_color='green'))
        b_verde.grid(row=i, column=6, padx=10, pady=5)

        b_amarelo = ctk.CTkButton(frame_conta, text='➖', width=60, fg_color='gray20', hover_color='gray20', command=lambda e=entry_ultimobkp: e.configure(fg_color='yellow'))
        b_amarelo.grid(row=i, column=7, padx=5, pady=5)

        b_vermelho = ctk.CTkButton(frame_conta, text='X', width=60, fg_color='gray20', hover_color='gray20', command=lambda e=entry_ultimobkp: e.configure(fg_color='red'))
        b_vermelho.grid(row=i, column=8, padx=5, pady=5)

