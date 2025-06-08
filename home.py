import customtkinter as ctk
from util import limpar_tela, limpar_area_principal
from bkp.contas_backup import abrir_backups
from bkp.contas_dados import backup_dados
from cadastros.cadastro import abrir_cadastros
from dashboard import dashboard
from relatorios import abrir_relatorios

def criar_menu_lateral(janela, area_principal, frame_atual):
    from login import abrir_login

    menu_lateral = ctk.CTkFrame(frame_atual, width=200, fg_color="#111606")
    menu_lateral.pack(side="left", fill="y")

    logo_label = ctk.CTkLabel(menu_lateral, text="PLR Manager", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    logo_label.pack(pady=30)

    btn_dashboard = ctk.CTkButton(menu_lateral, text="Dashboard", command=lambda: dashboard(area_principal), fg_color="#799b2a", hover_color="#52796f", corner_radius=8, height=40)
    btn_dashboard.pack(pady=8, padx=15, fill="x")

    btn_cadastro = ctk.CTkButton(menu_lateral, text="Cadastros", command=lambda: abrir_cadastros(area_principal), fg_color="#799b2a", hover_color="#52796f", corner_radius=8, height=40)
    btn_cadastro.pack(pady=8, padx=15, fill="x")

    btn_bkp = ctk.CTkButton(menu_lateral, text="Backups", command=lambda: abrir_backups(janela, area_principal), fg_color="#799b2a", hover_color="#52796f", corner_radius=8, height=40)
    btn_bkp.pack(pady=8, padx=15, fill="x")

    btn_bkp_dados = ctk.CTkButton(menu_lateral, text="Backups de Dados", command=lambda: backup_dados(janela, area_principal), fg_color="#799b2a", hover_color="#52796f", corner_radius=8, height=40)
    btn_bkp_dados.pack(pady=8, padx=15, fill="x")

    btn_relatorios = ctk.CTkButton(menu_lateral, text="Relatórios", command=lambda: abrir_relatorios(janela, area_principal), fg_color="#799b2a", hover_color="#52796f", corner_radius=8, height=40)
    btn_relatorios.pack(pady=8, padx=15, fill="x")

    btn_bloquear = ctk.CTkButton(menu_lateral, text="Bloquear", command=lambda: abrir_login(janela, frame_atual), fg_color="#799b2a", hover_color="#52796f", corner_radius=8, height=40)
    btn_bloquear.pack(pady=8, padx=15, fill="x")


def criar_area_principal(area_principal):
    area_principal = ctk.CTkFrame(area_principal, fg_color="#799b2a")
    area_principal.pack(side="right", fill="both", expand=True)

    dashboard(area_principal)


def abrir_home(janela, frame_atual):
    limpar_tela(frame_atual)
    janela.geometry('900x600')
     
    fzr_bkp = ctk.CTkButton(frame_atual, text='Backups', fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: abrir_backups(janela, frame_atual), width=120,
                             height=32, corner_radius=5, bg_color='#08254b')
    fzr_bkp.place(relx=0.5, rely=0.3, anchor='n')

    fzr_bkp_dados = ctk.CTkButton(frame_atual, text='Contas De Dados', fg_color='#0d1b2a', hover_color='#0d1b2a', command=lambda: backup_dados(janela, frame_atual), width=120, 
                                  height=30, corner_radius=5, bg_color='#08254b')
    fzr_bkp_dados.place(relx=0.5, rely=0.4, anchor='n')

    area_principal = ctk.CTkFrame(frame_atual, fg_color="#799b2a")
    area_principal.pack(side="right", fill="both", expand=True)

    criar_menu_lateral(janela, area_principal, frame_atual)
    criar_area_principal(area_principal)
