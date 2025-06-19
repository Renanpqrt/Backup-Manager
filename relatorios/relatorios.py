import customtkinter as ctk
from util import limpar_area_principal
from relatorios.f_relatorios import relat_bkps, relat_bkps_data, relat_bkps_atrasados, relat_dados, relat_dados_data, relat_dados_atrasados

def abrir_relatorios(janela, area_principal):
    limpar_area_principal(area_principal)
    
    # Titulo da area principal
    label_titulo = ctk.CTkLabel(area_principal, text='Relatórios', font=('Arial', 30, 'bold'), text_color="#EAEAEA")
    label_titulo.pack(anchor='n', pady=10, padx=0.5)

    # Menu lateral dos relatórios de Backup
    menu_lateral_bkp = ctk.CTkFrame(area_principal, width=200, fg_color='#2B2B2B')
    menu_lateral_bkp.place(x=-200, y=0, relheight=1)  # escondido à esquerda

    # Função para fechar o menu
    def fechar_menu(menu):
        x = menu.winfo_x()
        if x > 0:
            menu.place(x=-200, y=0, relheight=1)
        
    # Função para abrir o menu
    def abrir_menu(tipo, menu):
        for widget in menu.winfo_children():
            widget.destroy()
        
        if tipo == 1: # Se for do tipo 1, abrir os relatórios das contas de BKPs

            texto_lateral = ctk.CTkLabel(menu_lateral_bkp, text='Relatórios de BKPs', text_color='gray')
            texto_lateral.place(relx=0.45, rely=0.08, anchor='center')

            rel_contas = ctk.CTkButton(menu_lateral_bkp, text='Contas BKPs - Geral', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=lambda: relat_bkps(janela), text_color='#EAEAEA', corner_radius=10)
            rel_contas.place(relx=0.01, rely=0.2)

            rel_contas_data = ctk.CTkButton(menu_lateral_bkp, text='Contas BKPs - Data', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=lambda: relat_bkps_data(janela), text_color='#EAEAEA', corner_radius=10)
            rel_contas_data.place(relx=0.01, rely=0.28)

            rel_contas_atrasados = ctk.CTkButton(menu_lateral_bkp, text='Contas BKPs - Atrasados', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=lambda: relat_bkps_atrasados(janela), text_color='#EAEAEA', corner_radius=10)
            rel_contas_atrasados.place(relx=0.01, rely=0.36)

            fechar_btn = ctk.CTkButton(menu_lateral_bkp, text='Fechar', fg_color='red', hover_color='red', width=60 ,command=lambda: fechar_menu(menu=menu_lateral_bkp))
            fechar_btn.place(relx=0.01, rely=0.95)
            
        else: # Caso o contrario abrir o relatório de dados
            texto_lateral = ctk.CTkLabel(menu_lateral_bkp, text='Relatórios de Dados', text_color='gray')
            texto_lateral.place(relx=0.45, rely=0.08, anchor='center')

            rel_dados = ctk.CTkButton(menu_lateral_bkp, text='Contas Dados - Geral', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=lambda: relat_dados(janela), text_color='#EAEAEA', corner_radius=10)
            rel_dados.place(relx=0.01, rely=0.2)

            rel_dados_data = ctk.CTkButton(menu_lateral_bkp, text='Contas Dados - Data', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=lambda: relat_dados_data(janela), text_color='#EAEAEA', corner_radius=10)
            rel_dados_data.place(relx=0.01, rely=0.28)

            rel_dados_atrasados = ctk.CTkButton(menu_lateral_bkp, text='Contas Dados - Atrasados', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=lambda: relat_dados_atrasados(janela), text_color='#EAEAEA', corner_radius=10)
            rel_dados_atrasados.place(relx=0.01, rely=0.36)

            fechar_btn = ctk.CTkButton(menu_lateral_bkp, text='Fechar', fg_color='red', hover_color='red', width=60,command=lambda: fechar_menu(menu=menu_lateral_bkp))
            fechar_btn.place(relx=0.01, rely=0.95)


        # Lógica para abrir o menu
        x = menu_lateral_bkp.winfo_x()
        if x < 0:
            menu.place(x=550, y=0, relheight=1)

    # Botão para abrir o menu - BKPs  
    relatorio_de_contas = ctk.CTkButton(area_principal, text='Relatório de contas BKP', fg_color="#00B4D8", hover_color='#0096C7', width=200, 
    command=lambda tipo=1, menu=menu_lateral_bkp: abrir_menu(tipo, menu), text_color='#EAEAEA', corner_radius=10)
    relatorio_de_contas.place(relx=0.015, rely=0.08)

    # Botão para abrir o menu - Dados
    rel_contas_dados = ctk.CTkButton(area_principal, text='Relatório de contas Dados', fg_color="#00B4D8", hover_color='#0096C7', width=200, 
    command=lambda tipo=2, menu=menu_lateral_bkp: abrir_menu(tipo, menu), text_color='#EAEAEA', corner_radius=10)
    rel_contas_dados.place(relx=0.015, rely=0.15)


