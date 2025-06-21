from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import A4, A3
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from dados.tabelas import Conta, Conta_dados, session
from tkinter import filedialog
from datetime import date, datetime
import locale
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

try:
    locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')

def coletar_data():
    data = date.today().strftime("%A, ""%d de " "%B de " "%Y").upper()
    hora = datetime.today().strftime("%H:%M:%S")

    return data, hora

def cabeçalho_padrao():
    elementos = []
    data, hora = coletar_data()
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

    return elementos

def relat_bkps(janela):
    caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')
    dados = [conta for conta in session.query(Conta).all()]

    if not caminho:
        return
    
    dados_tabela = [["NOME", "EMAIL"]]
    for conta in dados:
        dados_tabela.append([conta.nome.upper(), conta.email.upper()])

    # Parametros do relatório
    relatorio = SimpleDocTemplate(caminho, pagesize=A4, topMargin=30, bottomMargin=30)
    elementos = []
    estilo = getSampleStyleSheet()

    elementos.extend(cabeçalho_padrao())

    # Titulo
    titulo_pdf = Paragraph("Relatório de contas de backup", estilo["Title"])
    elementos.append(titulo_pdf)

    elementos.append(Spacer(1, 20))
    
    # Dados finais da tabela
    dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

    # Criação da tabela
    tabela = Table(dados_tabela, colWidths=[250, 300])
    tabela.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "LEFT"),
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

def relat_dados(janela):
    caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')
    dados = [conta for conta in session.query(Conta_dados).all()]

    if not caminho:
        return
    
    dados_tabela = [["NOME", "EMAIL"]]
    for conta in dados:
        dados_tabela.append([conta.nome.upper(), conta.email.upper()])

    # Parametros do relatório
    relatorio = SimpleDocTemplate(caminho, pagesize=A4, topMargin=30, bottomMargin=30)
    elementos = []
    estilo = getSampleStyleSheet()

    elementos.extend(cabeçalho_padrao())

    # Titulo
    titulo_pdf = Paragraph("Relatório de contas de dados", estilo["Title"])
    elementos.append(titulo_pdf)

    elementos.append(Spacer(1, 20))
    
    # Dados finais da tabela
    dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

    # Criação da tabela
    tabela = Table(dados_tabela, colWidths=[200, 300])
    tabela.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "LEFT"),
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

def relat_bkps_data(janela):
    caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')
    dados = [conta for conta in session.query(Conta).all()]

    if not caminho:
        return
    
    dados_tabela = [["NOME", "EMAIL", "ULTIMO BACKUP", "SEGUNDO BACKUP"]]
    for conta in dados:
        segundo_bkp = conta.segundo_backup if conta.segundo_backup else "--"
        dados_tabela.append([conta.nome.upper(), conta.email.upper(), conta.ultimo_bkp, segundo_bkp])

    # Parametros do relatório
    relatorio = SimpleDocTemplate(caminho, pagesize=A3, topMargin=30, bottomMargin=30)
    elementos = []
    estilo = getSampleStyleSheet()

    elementos.extend(cabeçalho_padrao())

    # Titulo
    titulo_pdf = Paragraph("Relatório de contas de backup por data", estilo["Title"])
    elementos.append(titulo_pdf)

    elementos.append(Spacer(1, 20))
    
    # Dados finais da tabela
    dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

    # Criação da tabela
    tabela = Table(dados_tabela, colWidths=[230, 300, 152, 152])
    estilos = TableStyle([("ALIGN", (0, 0), (-1, -1), "LEFT"),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('FONTSIZE', (0, 0), (-1, -1), 10),
                                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                                # Dados finais
                                ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold")
                                    ])

    for linha, conta in enumerate(dados, start=1):
        
        if conta.cor_ultimo_backup == 'red':
            estilos.add('BACKGROUND', (2, linha), (2, linha), colors.red)
        elif conta.cor_ultimo_backup == 'yellow':
            estilos.add('BACKGROUND', (2, linha), (2, linha), colors.yellow)
        elif conta.cor_ultimo_backup == 'green':
            estilos.add('BACKGROUND', (2, linha), (2, linha), colors.green)
        else:
            estilos.add('BACKGROUND', (2, linha), (2, linha), colors.white)
        
        if conta.cor_segundo_backup == 'red':
            estilos.add('BACKGROUND', (3, linha), (3, linha), colors.red)
        elif conta.cor_segundo_backup == 'yellow':
            estilos.add('BACKGROUND', (3, linha), (3, linha), colors.yellow)
        elif conta.cor_segundo_backup == 'green':
            estilos.add('BACKGROUND', (3, linha), (3, linha), colors.green)
        else:
            estilos.add('BACKGROUND', (3, linha), (3, linha), colors.white)


    tabela.setStyle(estilos)
    elementos.append(tabela)
    elementos.append(Spacer(1, 12))
    
    
    
    relatorio.build(elementos)

def relat_dados_data(janela):
    caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('Arquivos Pdf', '*.pdf')], title='Salvar como')
    dados = [conta for conta in session.query(Conta_dados).all()]

    if not caminho:
        return
    
    dados_tabela = [["NOME", "EMAIL", "ULTIMA ALTERAÇÃO"]]
    for conta in dados:
        dados_tabela.append([conta.nome.upper(), conta.email.upper(), conta.ultimo_bkp])

    # Parametros do relatório
    relatorio = SimpleDocTemplate(caminho, pagesize=A4, topMargin=30, bottomMargin=30)
    elementos = []
    estilo = getSampleStyleSheet()

    elementos.extend(cabeçalho_padrao())

    # Titulo
    titulo_pdf = Paragraph("Relatório de contas de backup por data", estilo["Title"])
    elementos.append(titulo_pdf)

    elementos.append(Spacer(1, 20))
    
    # Dados finais da tabela
    dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

    # Criação da tabela
    tabela = Table(dados_tabela, colWidths=[175, 290, 130])
    estilos = TableStyle([("ALIGN", (0, 0), (-1, -1), "LEFT"),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('FONTSIZE', (0, 0), (-1, -1), 10),
                                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                                # Dados finais
                                ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold")
                                ])

    for linha, conta in enumerate(dados, start=1):

        if conta.cor_ultimo_backup == 'red':
            estilos.add('BACKGROUND', (2, linha), (2, linha), colors.red)
        elif conta.cor_ultimo_backup == 'yellow':
            estilos.add('BACKGROUND', (2, linha), (2, linha), colors.yellow)
        elif conta.cor_ultimo_backup == 'green':
            estilos.add('BACKGROUND', (2, linha), (2, linha), colors.green)
        else:
            estilos.add('BACKGROUND', (2, linha), (2, linha), colors.white)

    tabela.setStyle(estilos)
    elementos.append(tabela)
    elementos.append(Spacer(1, 12))
    
    
    
    relatorio.build(elementos)

def relat_bkps_atrasados(janela):
    caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('arquivos pdf', '*.pdf')], title='salvar como')
    dados = [conta for conta in session.query(Conta).all() if conta.cor_ultimo_backup in ['red', 'yellow'] and conta.cor_segundo_backup in ['red', 'yellow', '']]

    if not caminho:
        return
    
    dados_tabela = [["NOME", "EMAIL", "ULTIMO BACKUP", "SEGUNDO BACKUP"]]
    for conta in dados:
        segundo_bkp = conta.segundo_backup if conta.segundo_backup else "--"
        dados_tabela.append([conta.nome.upper(), conta.email.upper(), conta.ultimo_bkp, segundo_bkp])

    # Parametros do relatório
    relatorio = SimpleDocTemplate(caminho, pagesize=A3, topMargin=30, bottomMargin=30)
    elementos = []
    estilo = getSampleStyleSheet()

    elementos.extend(cabeçalho_padrao())

    # Titulo
    titulo_pdf = Paragraph("Relatório de contas de backup atrasados", estilo["Title"])
    elementos.append(titulo_pdf)

    elementos.append(Spacer(1, 20))
    
    # Dados finais da tabela
    dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

    # Criação da tabela
    tabela = Table(dados_tabela, colWidths=[230, 300, 152, 152])
    tabela.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "LEFT"),
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

def relat_dados_atrasados(janela):
    caminho = filedialog.asksaveasfilename(parent=janela, defaultextension='.pdf', filetypes=[('arquivos pdf', '*.pdf')], title='salvar como')
    dados = [conta for conta in session.query(Conta_dados).all() if conta.cor_ultimo_backup in ['red', 'yellow']]

    if not caminho:
        return
    
    dados_tabela = [["NOME", "EMAIL", "ULTIMO BACKUP"]]
    for conta in dados:
        dados_tabela.append([conta.nome.upper(), conta.email.upper(), conta.ultimo_bkp])

    # Parametros do relatório
    relatorio = SimpleDocTemplate(caminho, pagesize=A4, topMargin=30, bottomMargin=30)
    elementos = []
    estilo = getSampleStyleSheet()

    elementos.extend(cabeçalho_padrao())
    
    # Titulo
    titulo_pdf = Paragraph("Relatório de contas dados atrasados", estilo["Title"])
    elementos.append(titulo_pdf)

    elementos.append(Spacer(1, 20))
    
    # Dados finais da tabela
    dados_tabela.append(["Totais:", f"Contas >> {len(dados)}"])

    # Criação da tabela
    tabela = Table(dados_tabela, colWidths=[175, 290, 130])
    tabela.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "LEFT"),
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