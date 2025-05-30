import customtkinter as ctk
from dados.tabelas import User, Conta, session, Conta_dados
from CTkMessagebox import CTkMessagebox
from PIL import Image
from customtkinter import CTkImage
import pandas as pd
from tkinter import filedialog
from datetime import datetime, timedelta
import openpyxl
from openpyxl.styles import PatternFill, Border, Side
from openpyxl.utils import get_column_letter
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def limpar_tela(frame_atual):
    
    for widget in frame_atual.winfo_children():
        widget.destroy()

def deletar_conta(frame_atual):
    deletar = ctk.CTkToplevel()
    deletar.geometry('350x400')
    deletar.wm_attributes('-topmost', 1)
    deletar.overrideredirect(True)
    deletar.configure(fg_color="#6679F8")

    barra = ctk.CTkFrame(deletar, height=30, fg_color='gray20')
    barra.pack(fill='x')

    x_imag = Image.open(resource_path('imagens/x.png'))
    x_imag = CTkImage(light_image=x_imag, size=(30, 30))

    b_voltar = ctk.CTkButton(barra, text='', image=x_imag, fg_color='transparent', hover_color='gray20', width=60, command=lambda: deletar.destroy())
    b_voltar.pack(side='right')

    d_imag = Image.open(resource_path('imagens/detalhe.png'))
    d_imag = CTkImage(light_image=d_imag, size=(30, 30))

    b_fake = ctk.CTkButton(barra, image=d_imag, text='', fg_color='transparent', hover_color='gray20', width=60, state='disabled')
    b_fake.pack(side='left')

    titulo_del = ctk.CTkLabel(deletar, text='Deletar conta do app', font=('Arial', 15), text_color='white')
    titulo_del.place(relx=0.5, rely=0.15, anchor='n')

    text_barra = ctk.CTkLabel(barra, text='Exclusão de contas', text_color='white')
    text_barra.pack(side='left', padx=5, pady=0)

    entry_conta = ctk.CTkEntry(deletar, placeholder_text='Digite a conta')
    entry_conta.place(relx=0.5, rely=0.3, anchor='n')

    senha_adm = ctk.CTkEntry(deletar, placeholder_text='Senha de admin', show='*')
    senha_adm.place(relx=0.5, rely=0.40, anchor='n')

    def delete(frame_atual):
        conta = entry_conta.get().lower()
        senha_admin = senha_adm.get().lower()
        conta_banco = session.query(Conta).filter_by(nome=conta).first()

        if senha_admin != "administrador123":
            retorno = CTkMessagebox(icon='cancel', message='Senha de administrador incorreta!', title='Exclusão de contas (Erro)')
        else:
            if conta_banco:
                session.delete(conta_banco)
                session.commit()
                retorno = CTkMessagebox(icon='check', message='Conta excluida com sucesso!', title='Exclusão de contas (Sucesso)')
                if retorno.get() == "OK":
                    deletar.destroy()
            else:
                retorno = CTkMessagebox(icon='cancel', message='Conta inexistente', title='Exclusão de contas (Erro)')
                if retorno.get() == "OK":
                    deletar.destroy()

    b_excluir = ctk.CTkButton(deletar, text='deletar', fg_color='Red', hover='Red', width=80, command=lambda: delete(frame_atual))
    b_excluir.place(relx=0.5, rely=0.55, anchor='n')

def deletar_conta_dados(frame_atual):
    deletar = ctk.CTkToplevel()
    deletar.geometry('350x400')
    deletar.wm_attributes('-topmost', 1)
    deletar.overrideredirect(True)
    deletar.configure(fg_color="#6679F8")

    barra = ctk.CTkFrame(deletar, height=30, fg_color='gray20')
    barra.pack(fill='x')

    x_imag = Image.open(resource_path('imagens/x.png'))
    x_imag = CTkImage(light_image=x_imag, size=(30, 30))

    b_voltar = ctk.CTkButton(barra, text='', image=x_imag, fg_color='transparent', hover_color='gray20', width=60, command=lambda: deletar.destroy())
    b_voltar.pack(side='right')

    d_imag = Image.open(resource_path('imagens/detalhe.png'))
    d_imag = CTkImage(light_image=d_imag, size=(30, 30))

    b_fake = ctk.CTkButton(barra, image=d_imag, text='', fg_color='transparent', hover_color='gray20', width=60, state='disabled')
    b_fake.pack(side='left')

    titulo_del = ctk.CTkLabel(deletar, text='Deletar conta de dados', font=('Arial', 15), text_color='white')
    titulo_del.place(relx=0.5, rely=0.15, anchor='n')

    text_barra = ctk.CTkLabel(barra, text='Exclusão de contas (Dados)', text_color='white')
    text_barra.pack(side='left', padx=5, pady=0)

    entry_conta = ctk.CTkEntry(deletar, placeholder_text='Digite a conta')
    entry_conta.place(relx=0.5, rely=0.3, anchor='n')

    senha_adm = ctk.CTkEntry(deletar, placeholder_text='Senha de admin', show='*')
    senha_adm.place(relx=0.5, rely=0.40, anchor='n')

    def delete(frame_atual):
        conta = entry_conta.get().lower()
        senha_admin = senha_adm.get().lower()
        conta_banco = session.query(Conta_dados).filter_by(nome=conta).first()

        if senha_admin != "administrador123":
            retorno = CTkMessagebox(icon='cancel', message='Senha de administrador incorreta!', title='Exclusão de contas (Erro)')
        else:
            if conta_banco:
                session.delete(conta_banco)
                session.commit()
                retorno = CTkMessagebox(icon='check', message='Conta excluida com sucesso!', title='Exclusão de contas (Sucesso)')
                if retorno.get() == "OK":
                    deletar.destroy()
            else:
                retorno = CTkMessagebox(icon='cancel', message='Conta inexistente', title='Exclusão de contas (Erro)')
                if retorno.get() == "OK":
                    deletar.destroy()

    b_excluir = ctk.CTkButton(deletar, text='deletar', fg_color='Red', hover='Red', width=80, command=lambda: delete(frame_atual))
    b_excluir.place(relx=0.5, rely=0.55, anchor='n')

def coletar_dados(frame_atual, janela):
    contas = session.query(Conta).all()

    dados = []

    for dado in contas:
        dados.append({
            'Nome': dado.nome,
            'Email': dado.email,
            'Último Backup': dado.ultimo_bkp,
            'Segundo Backup': dado.segundo_backup if dado.segundo_backup else ''
        })
    
    return pd.DataFrame(dados)


def exportar_para_excel(df, frame_atual, janela):
    cores_status = {
        'verde': 'FF008000',   
        'amarelo': 'FFFFFF00', 
        'vermelho': 'FFFF0000' 
    }

    borda_preta = Border(
        left=Side(style='thin', color='000000'),
        right=Side(style='thin', color='000000'),
        top=Side(style='thin', color='000000'),
        bottom=Side(style='thin', color='000000')
    )

    caminho = filedialog.asksaveasfilename(parent=janela, defaultextension=".xlsx",
                                          filetypes=[("Arquivos Excel", "*.xlsx")],
                                          title="Salvar como")

    if caminho:
        with pd.ExcelWriter(caminho, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Backup')
            planilha = writer.sheets['Backup']

            
            tamanhos_colunas = {
                'Nome': 40,
                'Email': 45,
                'Ultimo Backup': 35,
                'Segundo Backup': 35
            }

            
            for idx, col in enumerate(df.columns, 1):
                col_letter = get_column_letter(idx)
                largura = tamanhos_colunas.get(col, 20)
                planilha.column_dimensions[col_letter].width = largura

            
            num_linhas = df.shape[0] + 1  
            num_colunas = df.shape[1]

            for row in range(1, num_linhas + 1):  
                for col in range(1, num_colunas + 1):
                    celula = planilha.cell(row=row, column=col)
                    celula.border = borda_preta

            col_index = df.columns.get_loc("Último Backup") + 1

            hoje = datetime.today().date()
            ontem = hoje - timedelta(days=1)

            
            for i, data_str in enumerate(df['Último Backup'], start=2):
                try:
                    data_backup = datetime.strptime(data_str, '%d/%m/%Y').date()
                    dias_atras = (hoje - data_backup).days

                    if data_backup == hoje or data_backup == ontem:
                        cor = cores_status['verde']
                    elif 2 <= dias_atras <= 3:
                        cor = cores_status['amarelo']
                    elif dias_atras > 3:
                        cor = cores_status['vermelho']
                    else:
                        cor = 'FFFFFFFF'  
                except Exception:
                    cor = 'FFFFFFFF'  

                celula = planilha.cell(row=i, column=col_index)
                fill = PatternFill(start_color=cor, end_color=cor, fill_type='solid')
                celula.fill = fill
                celula.border = borda_preta


def b_exportar(frame_atual, janela):
    df = coletar_dados(frame_atual, janela)
    exportar_para_excel(df, frame_atual, janela)

def coletar_dados2(frame_atual, janela):
    contas = session.query(Conta_dados).all()

    dados = []

    for dado in contas:
        dados.append({
            'Nome': dado.nome,
            'Email': dado.email,
            'Último Backup': dado.ultimo_bkp,
            'OBS': dado.obs
        })
    
    return pd.DataFrame(dados)

def b_exportar2(frame_atual, janela):
    df = coletar_dados2(frame_atual, janela)
    exportar_para_excel(df, frame_atual, janela)