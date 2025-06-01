import customtkinter as ctk
from util import limpar_area_principal

def dashboard(area_principal):
    limpar_area_principal(area_principal)

    header = ctk.CTkLabel(area_principal, text="Dashboard", font=ctk.CTkFont(size=30, weight="bold"), text_color="#1b4332")
    header.pack(pady=20)

    card_frame = ctk.CTkFrame(area_principal, fg_color="white", corner_radius=10)
    card_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Card 1
    card1 = ctk.CTkFrame(card_frame, fg_color="#52796f", corner_radius=12)
    card1.grid(row=0, column=0, padx=20, pady=30, sticky="nsew")

    label_title1 = ctk.CTkLabel(card1, text='Contas Backup', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title1.pack(padx=20, pady=(20, 5))

    label_value1 = ctk.CTkLabel(card1, text='50', font=ctk.CTkFont(size=30, weight="bold"), text_color="white")
    label_value1.pack(padx=20, pady=(0, 20))


    # Card 2
    card2 = ctk.CTkFrame(card_frame, fg_color="#52796f", corner_radius=12)
    card2.grid(row=0, column=1, padx=20, pady=30, sticky="nsew")

    label_title2 = ctk.CTkLabel(card2, text='Contas Dados', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title2.pack(padx=20, pady=(20, 5))

    label_value2 = ctk.CTkLabel(card2, text='5', font=ctk.CTkFont(size=30, weight="bold"), text_color="white")
    label_value2.pack(padx=20, pady=(0, 20))


    # Card 3
    card3 = ctk.CTkFrame(card_frame, fg_color="#52796f", corner_radius=12)
    card3.grid(row=0, column=2, padx=20, pady=30, sticky="nsew")

    label_title3 = ctk.CTkLabel(card3, text='Usuários', font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
    label_title3.pack(padx=20, pady=(20, 5))

    label_value3 = ctk.CTkLabel(card3, text='3', font=ctk.CTkFont(size=30, weight="bold"), text_color="white")
    label_value3.pack(padx=20, pady=(0, 20))


    
    card_frame.grid_columnconfigure((0, 1, 2), weight=1)