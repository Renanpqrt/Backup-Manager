import customtkinter as ctk
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
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
    dados = [conta for conta in session.query(Conta).all()]

    label_titulo = ctk.CTkLabel(area_principal, text='Relatórios', font=('Arial', 30, 'bold'), text_color="#1b4332")
    label_titulo.pack(anchor='n', pady=10, padx=0.5)

    def relat_contas():
        caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')

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

    rel_contas = ctk.CTkButton(area_principal, text='Contas de Backup', fg_color="#111606", hover_color='#111606', width=80, command=relat_contas, 
    text_color='#aede3c', corner_radius=12)
    rel_contas.place(relx=0.015, rely=0.08)
