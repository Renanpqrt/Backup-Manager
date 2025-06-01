import customtkinter as ctk
from util import limpar_tela, limpar_area_principal
from bkp.lista_contas import abrir_backups
from bkp.contas_dados import backup_dados
from cadastros.cadastro import abrir_cadastros

def criar_menu_lateral(janela, area_principal, frame_atual):
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


def dashboard(area_principal):
    limpar_area_principal(area_principal)

    header = ctk.CTkLabel(area_principal, text="Dashboard", font=ctk.CTkFont(size=30, weight="bold"), text_color="#1b4332")
    header.pack(pady=20)

    card_frame = ctk.CTkFrame(area_principal, fg_color="white", corner_radius=10)
    card_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Card 1
    card1 = ctk.CTkFrame(card_frame, fg_color="#52796f", corner_radius=12)
    card1.grid(row=0, column=0, padx=20, pady=30, sticky="nsew")

    label_title1 = ctk.CTkLabel(card1, text='Usuários', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title1.pack(padx=20, pady=(20, 5))

    label_value1 = ctk.CTkLabel(card1, text='10', font=ctk.CTkFont(size=30, weight="bold"), text_color="white")
    label_value1.pack(padx=20, pady=(0, 20))


    # Card 2
    card2 = ctk.CTkFrame(card_frame, fg_color="#52796f", corner_radius=12)
    card2.grid(row=0, column=1, padx=20, pady=30, sticky="nsew")

    label_title2 = ctk.CTkLabel(card2, text='Backups', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title2.pack(padx=20, pady=(20, 5))

    label_value2 = ctk.CTkLabel(card2, text='2', font=ctk.CTkFont(size=30, weight="bold"), text_color="white")
    label_value2.pack(padx=20, pady=(0, 20))


    # Card 3
    card3 = ctk.CTkFrame(card_frame, fg_color="#52796f", corner_radius=12)
    card3.grid(row=0, column=2, padx=20, pady=30, sticky="nsew")

    label_title3 = ctk.CTkLabel(card3, text='Pendentes', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title3.pack(padx=20, pady=(20, 5))

    label_value3 = ctk.CTkLabel(card3, text='5', font=ctk.CTkFont(size=30, weight="bold"), text_color="white")
    label_value3.pack(padx=20, pady=(0, 20))


    
    card_frame.grid_columnconfigure((0, 1, 2), weight=1)


def criar_area_principal(area_principal):
    area_principal = ctk.CTkFrame(area_principal, fg_color="#799b2a")
    area_principal.pack(side="right", fill="both", expand=True)

    dashboard(area_principal)


def abrir_home(janela, frame_atual):
    from login import abrir_login
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
