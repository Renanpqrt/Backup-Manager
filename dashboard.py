import customtkinter as ctk
from util import limpar_area_principal
from dados.tabelas import Conta_dados, Conta, User, session

def dashboard(area_principal):
    limpar_area_principal(area_principal)

    # Consulta no banco de dados
    contas = [conta for conta in session.query(Conta).all()]
    contas_dados = [conta for conta in session.query(Conta_dados).all()]
    usuarios = [usuario for usuario in session.query(User).all()]

    # Variaveis para os cards
    contas_atrasadas = len([conta for conta in contas if conta.cor_ultimo_backup in ('red', 'yellow') or conta.cor_segundo_backup in ('red', 'yellow')])

    dados_atrasados = len([conta for conta in contas_dados if conta.cor_ultimo_backup in ('red', 'yellow')])
    
    contas_sem_cor = len([conta for conta in contas if conta.cor_ultimo_backup not in ('red', 'yellow', 'green') or conta.cor_segundo_backup not in ('red', 'yellow', 'green', '')])

    contas_em_dia = [conta for conta in contas if conta.cor_ultimo_backup == 'green' and conta.cor_segundo_backup in ('green', '')]
    
    try:
        label_porcentagem = (len(contas_em_dia) / len(contas)) * 100
    except ZeroDivisionError:
        label_porcentagem = 0

    # header
    header = ctk.CTkLabel(area_principal, text="Dashboard", font=ctk.CTkFont(size=30, weight="bold"), text_color="#EAEAEA")
    header.pack(pady=20)

    card_frame = ctk.CTkFrame(area_principal, fg_color="#2B2B2B", corner_radius=10)
    card_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Card 1
    card1 = ctk.CTkFrame(card_frame, fg_color="#00B4D8", corner_radius=12)
    card1.grid(row=0, column=0, padx=20, pady=30, sticky="nsew")

    label_title1 = ctk.CTkLabel(card1, text='Contas Backup', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title1.pack(padx=20, pady=(20, 5))

    label_value1 = ctk.CTkLabel(card1, text=len(contas), font=ctk.CTkFont(size=30, weight="bold"), text_color="white")
    label_value1.pack(padx=20, pady=(0, 20))


    # Card 2
    card2 = ctk.CTkFrame(card_frame, fg_color="#00B4D8", corner_radius=12)
    card2.grid(row=0, column=1, padx=20, pady=30, sticky="nsew")

    label_title2 = ctk.CTkLabel(card2, text='Contas Dados', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title2.pack(padx=20, pady=(20, 5))

    label_value2 = ctk.CTkLabel(card2, text=len(contas_dados), font=ctk.CTkFont(size=30, weight="bold"), text_color="white")
    label_value2.pack(padx=20, pady=(0, 20))

    # Card 3
    card3 = ctk.CTkFrame(card_frame, fg_color="#00B4D8", corner_radius=12)
    card3.grid(row=0, column=2, padx=20, pady=30, sticky="nsew")

    label_title3 = ctk.CTkLabel(card3, text='Backups atrasados', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title3.pack(padx=20, pady=(20, 5))

    label_value3 = ctk.CTkLabel(card3, text=contas_atrasadas, font=ctk.CTkFont(size=30, weight="bold"), text_color=("#B11E1E" if contas_atrasadas > 0 else 'white'))
    label_value3.pack(padx=20, pady=(0, 20))

    # Card 4
    card4 = ctk.CTkFrame(card_frame, fg_color="#00B4D8", corner_radius=12)
    card4.grid(row=1, column=0, padx=20, pady=30, sticky="nsew")

    label_title4 = ctk.CTkLabel(card4, text='Dados atrasados', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title4.pack(padx=20, pady=(20, 5))

    label_value4 = ctk.CTkLabel(card4, text=dados_atrasados, font=ctk.CTkFont(size=30, weight="bold"), text_color=('#B11E1E' if dados_atrasados > 0 else 'white'))
    label_value4.pack(padx=20, pady=(0, 20))

    card_frame.grid_columnconfigure((0, 1, 2), weight=1)

    # Card5
    
    card5 = ctk.CTkFrame(card_frame, fg_color="#00B4D8", corner_radius=12)
    card5.grid(row=1, column=1, padx=20, pady=30, sticky="nsew")

    label_title5 = ctk.CTkLabel(card5, text='Backups em dia (%)', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title5.pack(padx=20, pady=(20, 5))

    label_value5 = ctk.CTkLabel(card5, text=(f'{label_porcentagem:.1f}%'), font=ctk.CTkFont(size=30, weight="bold"), text_color=('green' if int(label_porcentagem) > 0 else 'white'))
    label_value5.pack(padx=20, pady=(0, 20))

    # Card 6

    card6 = ctk.CTkFrame(card_frame, fg_color="#00B4D8", corner_radius=12)
    card6.grid(row=1, column=2, padx=20, pady=30, sticky="nsew")

    label_title6 = ctk.CTkLabel(card6, text='Contas sem status', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title6.pack(padx=20, pady=(20, 5))

    label_value6 = ctk.CTkLabel(card6, text=contas_sem_cor, font=ctk.CTkFont(size=30, weight="bold"), text_color='white')
    label_value6.pack(padx=20, pady=(0, 20))