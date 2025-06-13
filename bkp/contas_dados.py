import customtkinter as ctk
from dados.tabelas import Conta_dados, session
from util import limpar_area_principal, b_exportar2, importar_ultima_alteracao
from datetime import date, timedelta, datetime

# Toplevel dos backups
def iniciar_backup_d(janela):
    bkp = ctk.CTkToplevel()
    bkp.geometry('1000x900')
    bkp.configure(fg_color='#1E1E1E')
    bkp.wm_attributes('-topmost', 1)
    bkp.after(100, lambda: bkp.wm_attributes('-topmost', 0))
    bkp.title('Backups de Dados')
    entry_ultimos_bkp = {}  # chave: conta.id, valor: CTkEntry

    # Funções

    def resetar_cores():
        conta_db = session.query(Conta_dados).all()
        for conta in conta_db:
            conta.cor_ultimo_backup = 'white'
        session.commit()

        for conta in conta_db:
            entry = entry_ultimos_bkp.get(conta.id)
            if entry:
                entry.configure(fg_color='white')

    def atualizar_data_hoje(e, id):
        e.configure(fg_color='white')
        hoje = date.today().strftime("%d/%m/%Y")
        e.delete(0, 'end')
        e.insert(0, hoje)

        conta_db = session.query(Conta_dados).get(id)
        conta_db.ultimo_bkp = hoje
        session.commit()

    def atualizar_data_ontem(e, id):
        e.configure(fg_color='white')
        ontem = (date.today() - timedelta(days=1)).strftime("%d/%m/%Y")

        e.delete(0, 'end')
        e.insert(0, ontem)

        conta_db = session.query(Conta_dados).get(id)
        conta_db.ultimo_bkp = ontem
        session.commit()

    def salvar_ultimobkp(e, id):
        e.configure(fg_color='white')
        valor = e.get()

        conta_db = session.query(Conta_dados).get(id)
        conta_db.ultimo_bkp = valor
        session.commit()

    def salvar_obs(e, id):
        e.configure(fg_color='white')
        valor = e.get()

        conta_db = session.query(Conta_dados).get(id)
        conta_db.obs = valor
        session.commit()

    def verde(e, id):
        e.configure(fg_color='green')

        conta_db = session.query(Conta_dados).get(id)
        conta_db.cor_ultimo_backup = 'green'
        session.commit()

    def amarelo(e, id):
        e.configure(fg_color='yellow')

        conta_db = session.query(Conta_dados).get(id)
        conta_db.cor_ultimo_backup = 'yellow'
        session.commit()

    def vermelho(e, id):
        e.configure(fg_color='red')

        conta_db = session.query(Conta_dados).get(id)
        conta_db.cor_ultimo_backup = 'red'
        session.commit()

    def copiar_para_clipboard(event, label):
        conteudo = label.cget('text')
        label.clipboard_clear()
        label.clipboard_append(conteudo)
        label.update()

    # Labels e Buttons
    texto = ctk.CTkLabel(bkp, text='Iniciando Backups (Dados)', text_color='#EAEAEA', font=('Helvetica', 30, 'bold'))
    texto.place(relx=0.5, rely=0.05, anchor='center')

    export = ctk.CTkButton(bkp, text='Exportar dados', width=80, fg_color='#00B4D8', hover_color='#0096C7', command=lambda: b_exportar2(janela))
    export.place(relx=0.1, rely=0.05, anchor='center')

    importar = ctk.CTkButton(bkp, text='Importar dados', width=80, fg_color='#00B4D8', hover_color='#0096C7', command=lambda: importar_ultima_alteracao())
    importar.place(relx=0.75, rely=0.05)

    resetar_cor = ctk.CTkButton(bkp, text='Resetar cores', width=80, fg_color='#00B4D8', hover_color='#0096C7', command=resetar_cores)
    resetar_cor.place(relx=0.25, rely=0.05, anchor='center')
    
    # Frame dos BKPs
    frame_conta = ctk.CTkScrollableFrame(bkp, fg_color='#1E1E1E')
    frame_conta.place(relx=0.5, rely=0.55, anchor='center', relwidth=1, relheight=0.90)

    # Area dos BKPs
    for i, conta in enumerate(session.query(Conta_dados).all()):
        label_nome = ctk.CTkLabel(frame_conta, text=conta.nome.capitalize(), text_color='gray', font=('Helvetica', 17, 'bold'))
        label_nome.grid(row=i, column=0, padx=5, pady=5)

        label_email = ctk.CTkLabel(frame_conta, text=conta.email, text_color='gray', font=('Helvetica', 17, 'bold'))
        label_email.grid(row=i, column=1, padx=10, pady=5)
        label_email.bind("<Button-1>", lambda event, lbl=label_email: copiar_para_clipboard(event, lbl))

        entry_ultimobkp = ctk.CTkEntry(frame_conta, width=100, fg_color=conta.cor_ultimo_backup, text_color='black')
        entry_ultimobkp.insert(0, conta.ultimo_bkp)
        entry_ultimobkp.grid(row=i, column=2, padx=10, pady=5)
        entry_ultimobkp.bind('<Return>', lambda event, e=entry_ultimobkp, id=conta.id: salvar_ultimobkp(e, id))
        entry_ultimos_bkp[conta.id] = entry_ultimobkp 

        entry_obs = ctk.CTkEntry(frame_conta, width=100, fg_color='#EAEAEA', text_color='black')
        entry_obs.insert(0, conta.obs)
        entry_obs.grid(row=i, column=3, padx=10, pady=5)
        entry_obs.bind('<Return>', lambda event, e=entry_obs, id=conta.id: salvar_obs(e, id))

        b_hoje = ctk.CTkButton(frame_conta, text='Hoje', width=80, fg_color='#00B4D8', hover_color='#0096C7', command=lambda e=entry_ultimobkp, id=conta.id: atualizar_data_hoje(e, id))
        b_hoje.grid(row=i, column=4, padx=10, pady=5)

        b_ontem = ctk.CTkButton(frame_conta, text='Ontem', width=80, fg_color='#00B4D8', hover_color='#0096C7', command=lambda e=entry_ultimobkp, id=conta.id: atualizar_data_ontem(e, id))
        b_ontem.grid(row=i, column=5, padx=10, pady=5)

        b_verde = ctk.CTkButton(frame_conta, text='✔', width=60, fg_color='#00B4D8', hover_color='#0096C7', command=lambda e=entry_ultimobkp, id=conta.id: verde(e, id))
        b_verde.grid(row=i, column=6, padx=10, pady=5)

        b_amarelo = ctk.CTkButton(frame_conta, text='➖', width=60, fg_color='#00B4D8', hover_color='#0096C7', command=lambda e=entry_ultimobkp, id=conta.id: amarelo(e, id))
        b_amarelo.grid(row=i, column=7, padx=5, pady=5)

        b_vermelho = ctk.CTkButton(frame_conta, text='X', width=60, fg_color='#00B4D8', hover_color='#0096C7', command=lambda e=entry_ultimobkp, id=conta.id: vermelho(e, id))
        b_vermelho.grid(row=i, column=8, padx=5, pady=5)

