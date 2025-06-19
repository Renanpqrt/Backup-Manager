import customtkinter as ctk
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import A4, A3
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from util import limpar_area_principal
from dados.tabelas import Conta, Conta_dados, session
from tkinter import filedialog
from datetime import date, datetime
import locale
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

def abrir_relatorios(janela, area_principal):
    limpar_area_principal(area_principal)
    
    # Funções para construir os relatórios

    def relat_bkps():
        caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')
        dados = [conta for conta in session.query(Conta).all()]

        if not caminho:
            return
        
        dados_tabela = [["NOME", "EMAIL"]]
        for conta in dados:
            dados_tabela.append([conta.nome.upper(), conta.email.upper()])

        # Coletar data e hora
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
        data = date.today().strftime("%A, ""%d de " "%B de " "%Y").upper()
        hora = datetime.today().strftime("%H:%M:%S")

        # Parametros do relatório
        relatorio = SimpleDocTemplate(caminho, pagesize=A4, topMargin=30, bottomMargin=30)
        elementos = []
        estilo = getSampleStyleSheet()

        # PLR
        plr = Paragraph("PLR MANAGER", estilo['Heading3'].clone('h3_esquerda'))
        elementos.append(plr)

        # Data
        data_pdf = Paragraph(data, estilo["Heading3"].clone('h3_direita', alignment=TA_RIGHT))
        elementos.append(data_pdf)

        elementos.append(Spacer(1, 20))

        # Hora

        hora_pdf = Paragraph(f'Hora: {hora}', estilo["Heading3"].clone('normal_direita', alignment=TA_RIGHT))
        elementos.append(hora_pdf)
        
        elementos.append(Spacer(1, 20))

        # Titulo
        titulo_pdf = Paragraph("Relatório de contas de backup", estilo["Title"])
        elementos.append(titulo_pdf)

        elementos.append(Spacer(1, 20))
        
        # Dados finais da tabela
        dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

        # Criação da tabela
        tabela = Table(dados_tabela, colWidths=[200, 300])
        tabela.setStyle(TableStyle([("ALIGIN", (0, 0), (-1, -1), "LEFT"),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                                    # Dados finais
                                    ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold")
                                     
                                      ]))

        
        elementos.append(tabela)
        elementos.append(Spacer(1, 12))
        
        
        
        relatorio.build(elementos)

    def relat_dados():
        caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')
        dados = [conta for conta in session.query(Conta_dados).all()]

        if not caminho:
            return
        
        dados_tabela = [["NOME", "EMAIL"]]
        for conta in dados:
            dados_tabela.append([conta.nome.upper(), conta.email.upper()])

        # Coletar data e hora
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
        data = date.today().strftime("%A, ""%d de " "%B de " "%Y").upper()
        hora = datetime.today().strftime("%H:%M:%S")

        # Parametros do relatório
        relatorio = SimpleDocTemplate(caminho, pagesize=A4, topMargin=30, bottomMargin=30)
        elementos = []
        estilo = getSampleStyleSheet()

        # PLR
        plr = Paragraph("PLR MANAGER", estilo['Heading3'].clone('h3_esquerda'))
        elementos.append(plr)

        # Data
        data_pdf = Paragraph(data, estilo["Heading3"].clone('h3_direita', alignment=TA_RIGHT))
        elementos.append(data_pdf)

        elementos.append(Spacer(1, 20))

        # Hora

        hora_pdf = Paragraph(f'Hora: {hora}', estilo["Heading3"].clone('normal_direita', alignment=TA_RIGHT))
        elementos.append(hora_pdf)
        
        elementos.append(Spacer(1, 20))

        # Titulo
        titulo_pdf = Paragraph("Relatório de contas de backup", estilo["Title"])
        elementos.append(titulo_pdf)

        elementos.append(Spacer(1, 20))
        
        # Dados finais da tabela
        dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

        # Criação da tabela
        tabela = Table(dados_tabela, colWidths=[200, 300])
        tabela.setStyle(TableStyle([("ALIGIN", (0, 0), (-1, -1), "LEFT"),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                                    # Dados finais
                                    ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold")
                                     
                                      ]))

        
        elementos.append(tabela)
        elementos.append(Spacer(1, 12))
        
        
        
        relatorio.build(elementos)
    
    def relat_bkps_data():
        caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')
        dados = [conta for conta in session.query(Conta).all()]

        if not caminho:
            return
        
        dados_tabela = [["NOME", "EMAIL", "ULTIMO BACKUP", "SEGUNDO BACKUP"]]
        for conta in dados:
            segundo_bkp = conta.segundo_backup if conta.segundo_backup else "--"
            dados_tabela.append([conta.nome.upper(), conta.email.upper(), conta.ultimo_bkp, segundo_bkp])

        # Coletar data e hora
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
        data = date.today().strftime("%A, ""%d de " "%B de " "%Y").upper()
        hora = datetime.today().strftime("%H:%M:%S")

        # Parametros do relatório
        relatorio = SimpleDocTemplate(caminho, pagesize=A3, topMargin=30, bottomMargin=30)
        elementos = []
        estilo = getSampleStyleSheet()

        # PLR
        plr = Paragraph("PLR MANAGER", estilo['Heading3'].clone('h3_esquerda'))
        elementos.append(plr)

        # Data
        data_pdf = Paragraph(data, estilo["Heading3"].clone('h3_direita', alignment=TA_RIGHT))
        elementos.append(data_pdf)

        elementos.append(Spacer(1, 20))

        # Hora

        hora_pdf = Paragraph(f'Hora: {hora}', estilo["Heading3"].clone('normal_direita', alignment=TA_RIGHT))
        elementos.append(hora_pdf)
        
        elementos.append(Spacer(1, 20))

        # Titulo
        titulo_pdf = Paragraph("Relatório de contas de backup por data", estilo["Title"])
        elementos.append(titulo_pdf)

        elementos.append(Spacer(1, 20))
        
        # Dados finais da tabela
        dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

        # Criação da tabela
        tabela = Table(dados_tabela, colWidths=[230, 300, 152, 152])
        tabela.setStyle(TableStyle([("ALIGIN", (0, 0), (-1, -1), "LEFT"),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                                    # Dados finais
                                    ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold")
                                     
                                      ]))

        
        elementos.append(tabela)
        elementos.append(Spacer(1, 12))
        
        
        
        relatorio.build(elementos)

    def relat_dados_data():
        caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')
        dados = [conta for conta in session.query(Conta_dados).all()]

        if not caminho:
            return
        
        dados_tabela = [["NOME", "EMAIL", "ULTIMA ALTERAÇÃO"]]
        for conta in dados:
            dados_tabela.append([conta.nome.upper(), conta.email.upper(), conta.ultimo_bkp])

        # Coletar data e hora
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
        data = date.today().strftime("%A, ""%d de " "%B de " "%Y").upper()
        hora = datetime.today().strftime("%H:%M:%S")

        # Parametros do relatório
        relatorio = SimpleDocTemplate(caminho, pagesize=A4, topMargin=30, bottomMargin=30)
        elementos = []
        estilo = getSampleStyleSheet()

        # PLR
        plr = Paragraph("PLR MANAGER", estilo['Heading3'].clone('h3_esquerda'))
        elementos.append(plr)

        # Data
        data_pdf = Paragraph(data, estilo["Heading3"].clone('h3_direita', alignment=TA_RIGHT))
        elementos.append(data_pdf)

        elementos.append(Spacer(1, 20))

        # Hora

        hora_pdf = Paragraph(f'Hora: {hora}', estilo["Heading3"].clone('normal_direita', alignment=TA_RIGHT))
        elementos.append(hora_pdf)
        
        elementos.append(Spacer(1, 20))

        # Titulo
        titulo_pdf = Paragraph("Relatório de contas de backup por data", estilo["Title"])
        elementos.append(titulo_pdf)

        elementos.append(Spacer(1, 20))
        
        # Dados finais da tabela
        dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

        # Criação da tabela
        tabela = Table(dados_tabela, colWidths=[175, 290, 130])
        tabela.setStyle(TableStyle([("ALIGIN", (0, 0), (-1, -1), "LEFT"),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                                    # Dados finais
                                    ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold")
                                     
                                      ]))

        
        elementos.append(tabela)
        elementos.append(Spacer(1, 12))
        
        
        
        relatorio.build(elementos)
    
    def relat_bkps_atrasados():
        caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('arquivos pdf', '*.pdf')], title='salvar como')
        dados = [conta for conta in session.query(Conta).all() if conta.cor_ultimo_backup in ['red', 'yellow'] and conta.cor_segundo_backup in ['red', 'yellow', '']]

        if not caminho:
            return
        
        dados_tabela = [["NOME", "EMAIL", "ULTIMO BACKUP", "SEGUNDO BACKUP"]]
        for conta in dados:
            segundo_bkp = conta.segundo_backup if conta.segundo_backup else "--"
            dados_tabela.append([conta.nome.upper(), conta.email.upper(), conta.ultimo_bkp, segundo_bkp])

        # Coletar data e hora
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
        data = date.today().strftime("%A, ""%d de " "%B de " "%Y").upper()
        hora = datetime.today().strftime("%H:%M:%S")

        # Parametros do relatório
        relatorio = SimpleDocTemplate(caminho, pagesize=A3, topMargin=30, bottomMargin=30)
        elementos = []
        estilo = getSampleStyleSheet()

        # PLR
        plr = Paragraph("PLR MANAGER", estilo['Heading3'].clone('h3_esquerda'))
        elementos.append(plr)

        # Data
        data_pdf = Paragraph(data, estilo["Heading3"].clone('h3_direita', alignment=TA_RIGHT))
        elementos.append(data_pdf)

        elementos.append(Spacer(1, 20))

        # Hora

        hora_pdf = Paragraph(f'Hora: {hora}', estilo["Heading3"].clone('normal_direita', alignment=TA_RIGHT))
        elementos.append(hora_pdf)
        
        elementos.append(Spacer(1, 20))

        # Titulo
        titulo_pdf = Paragraph("Relatório de contas de backup atrasados", estilo["Title"])
        elementos.append(titulo_pdf)

        elementos.append(Spacer(1, 20))
        
        # Dados finais da tabela
        dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

        # Criação da tabela
        tabela = Table(dados_tabela, colWidths=[230, 300, 152, 152])
        tabela.setStyle(TableStyle([("ALIGIN", (0, 0), (-1, -1), "LEFT"),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                                    # Dados finais
                                    ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold")
                                     
                                      ]))

        
        elementos.append(tabela)
        elementos.append(Spacer(1, 12))
        
        
        
        relatorio.build(elementos)

    def relat_dados_atrasados():
        caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('arquivos pdf', '*.pdf')], title='salvar como')
        dados = [conta for conta in session.query(Conta_dados).all() if conta.cor_ultimo_backup in ['red', 'yellow']]

        if not caminho:
            return
        
        dados_tabela = [["NOME", "EMAIL", "ULTIMO BACKUP"]]
        for conta in dados:
            dados_tabela.append([conta.nome.upper(), conta.email.upper(), conta.ultimo_bkp])

        # Coletar data e hora
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
        data = date.today().strftime("%A, ""%d de " "%B de " "%Y").upper()
        hora = datetime.today().strftime("%H:%M:%S")

        # Parametros do relatório
        relatorio = SimpleDocTemplate(caminho, pagesize=A4, topMargin=30, bottomMargin=30)
        elementos = []
        estilo = getSampleStyleSheet()

        # PLR
        plr = Paragraph("PLR MANAGER", estilo['Heading3'].clone('h3_esquerda'))
        elementos.append(plr)

        # Data
        data_pdf = Paragraph(data, estilo["Heading3"].clone('h3_direita', alignment=TA_RIGHT))
        elementos.append(data_pdf)

        elementos.append(Spacer(1, 20))

        # Hora

        hora_pdf = Paragraph(f'Hora: {hora}', estilo["Heading3"].clone('normal_direita', alignment=TA_RIGHT))
        elementos.append(hora_pdf)
        
        elementos.append(Spacer(1, 20))

        # Titulo
        titulo_pdf = Paragraph("Relatório de contas dados atrasados", estilo["Title"])
        elementos.append(titulo_pdf)

        elementos.append(Spacer(1, 20))
        
        # Dados finais da tabela
        dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

        # Criação da tabela
        tabela = Table(dados_tabela, colWidths=[175, 290, 130])
        tabela.setStyle(TableStyle([("ALIGIN", (0, 0), (-1, -1), "LEFT"),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                                    # Dados finais
                                    ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold")
                                     
                                      ]))

        
        elementos.append(tabela)
        elementos.append(Spacer(1, 12))
        
        
        
        relatorio.build(elementos)

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

            rel_contas = ctk.CTkButton(menu_lateral_bkp, text='Contas BKPs GERAL', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=relat_bkps, text_color='#EAEAEA', corner_radius=10)
            rel_contas.place(relx=0.01, rely=0.2)

            rel_contas_data = ctk.CTkButton(menu_lateral_bkp, text='Contas BKPs DATA', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=relat_bkps_data, text_color='#EAEAEA', corner_radius=10)
            rel_contas_data.place(relx=0.01, rely=0.28)

            rel_contas_atrasados = ctk.CTkButton(menu_lateral_bkp, text='Contas BKPs ATRASADOS', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=relat_bkps_atrasados, text_color='#EAEAEA', corner_radius=10)
            rel_contas_atrasados.place(relx=0.01, rely=0.36)

            fechar_btn = ctk.CTkButton(menu_lateral_bkp, text='Fechar', fg_color='red', hover_color='red', width=60 ,command=lambda: fechar_menu(menu=menu_lateral_bkp))
            fechar_btn.place(relx=0.01, rely=0.95)
            
        else: # Caso o contrario abrir o relatório de dados
            texto_lateral = ctk.CTkLabel(menu_lateral_bkp, text='Relatórios de Dados', text_color='gray')
            texto_lateral.place(relx=0.45, rely=0.08, anchor='center')

            rel_dados = ctk.CTkButton(menu_lateral_bkp, text='Contas Dados GERAL', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=relat_dados, text_color='#EAEAEA', corner_radius=10)
            rel_dados.place(relx=0.01, rely=0.2)

            rel_dados_data = ctk.CTkButton(menu_lateral_bkp, text='Contas Dados DATA', fg_color="#00B4D8", hover_color='#0096C7', width=175, command=relat_dados_data, text_color='#EAEAEA', corner_radius=10)
            rel_dados_data.place(relx=0.01, rely=0.28)

            rel_dados_atrasados = ctk.CTkButton(menu_lateral_bkp, text='Contas Dados ATRASADOS', fg_color="#00B4D8", hover_color='#0096C7', width=170, command=relat_dados_atrasados, text_color='#EAEAEA', corner_radius=10)
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


