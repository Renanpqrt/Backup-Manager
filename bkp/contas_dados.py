import customtkinter as ctk
from dados.tabelas import Conta_dados, session
from util import limpar_area_principal, resource_path
from bkp.iniciar_backups_dados import iniciar_backup

def backup_dados(janela, area_principal):
    limpar_area_principal(area_principal)

    titulo_backups = ctk.CTkLabel(area_principal, text='Contas de Dados', font=('Helvetica', 30, 'bold'), text_color='#1b4332')
    titulo_backups.pack(anchor='n', pady=10, padx=0.5)

    iniciar = ctk.CTkButton(area_principal, text='Iniciar Backups', fg_color='#111606', hover_color='#111606', width=80, command=lambda: iniciar_backup(janela),
    text_color="#aede3c", corner_radius=12)
    iniciar.place(relx=0.025, rely=0.02)

    frame_contas = ctk.CTkScrollableFrame(area_principal, width=700, height=425, fg_color='#799b2a')
    frame_contas.place(relx=0.5, rely=0.55, anchor='center')

    for i, conta in enumerate(session.query(Conta_dados).all()):
        label_nome = ctk.CTkLabel(frame_contas, text=conta.nome.capitalize(), text_color='#222c0c', font=('Helvetica', 15, 'bold'))
        label_nome.grid(row=i, column=0, padx=5, pady=5)

        label_email = ctk.CTkLabel(frame_contas, text=conta.email, text_color='#222c0c', font=('Helvetica', 15, 'bold'))
        label_email.grid(row=i, column=1, padx=10, pady=5)