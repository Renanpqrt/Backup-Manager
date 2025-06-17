import customtkinter as ctk
from util import limpar_tela, limpar_area_principal
from bkp.contas_backup import iniciar_backup
from bkp.contas_dados import iniciar_backup_d
from cadastros.cadastro import abrir_cadastros
from dashboard import dashboard
from relatorios import abrir_relatorios

def criar_menu_lateral(janela, area_principal, frame_atual):
    from login import abrir_login, versao

    menu_lateral = ctk.CTkFrame(frame_atual, width=200, fg_color="#2B2B2B")
    menu_lateral.pack(side="left", fill="y")

    logo_label = ctk.CTkLabel(menu_lateral, text="PLR Manager", font=ctk.CTkFont(size=24, weight="bold"), text_color="#EAEAEA")
    logo_label.pack(pady=30)

    btn_dashboard = ctk.CTkButton(menu_lateral, text="Dashboard", command=lambda: dashboard(area_principal), fg_color="#00B4D8", hover_color="#0096C7", corner_radius=8, height=40)
    btn_dashboard.pack(pady=8, padx=15, fill="x")

    btn_cadastro = ctk.CTkButton(menu_lateral, text="Cadastros", command=lambda: abrir_cadastros(area_principal), fg_color="#00B4D8", hover_color="#0096C7", corner_radius=8, height=40)
    btn_cadastro.pack(pady=8, padx=15, fill="x")

    btn_bkp = ctk.CTkButton(menu_lateral, text="Iniciar BKPs", command=lambda: iniciar_backup(janela), fg_color="#00B4D8", hover_color="#0096C7", corner_radius=8, height=40)
    btn_bkp.pack(pady=8, padx=15, fill="x")

    btn_bkp_dados = ctk.CTkButton(menu_lateral, text="Iniciar BKPs de Dados", command=lambda: iniciar_backup_d(janela), fg_color="#00B4D8", hover_color="#0096C7", corner_radius=8, height=40)
    btn_bkp_dados.pack(pady=8, padx=15, fill="x")

    btn_relatorios = ctk.CTkButton(menu_lateral, text="Relatórios", command=lambda: abrir_relatorios(janela, area_principal), fg_color="#00B4D8", hover_color="#0096C7", corner_radius=8, height=40)
    btn_relatorios.pack(pady=8, padx=15, fill="x")

    btn_bloquear = ctk.CTkButton(menu_lateral, text="Bloquear", command=lambda: abrir_login(janela, frame_atual), fg_color="#00B4D8", hover_color="#0096C7", corner_radius=8, height=40)
    btn_bloquear.pack(pady=8, padx=15, fill="x")

    label_versao = ctk.CTkLabel(menu_lateral, text=versao, text_color="#EAEAEA")
    label_versao.place(relx=0.5, rely=0.9, anchor='center')

def criar_area_principal(area_principal):
    area_principal = ctk.CTkFrame(area_principal, fg_color="#1E1E1E")
    area_principal.pack(side="right", fill="both", expand=True)

    dashboard(area_principal)


def abrir_home(janela, frame_atual):
    limpar_tela(frame_atual)
    janela.geometry('900x600')
     
    area_principal = ctk.CTkFrame(frame_atual, fg_color="#1E1E1E")
    area_principal.pack(side="right", fill="both", expand=True)

    criar_menu_lateral(janela, area_principal, frame_atual)
    criar_area_principal(area_principal)
