import customtkinter as ctk
from util import limpar_area_principal, resource_path
from PIL import Image
from customtkinter import CTkImage
from cadastros.users import abrir_user
from cadastros.contas import abrir_cadastro_contas

def abrir_cadastros(area_principal):
    from home import abrir_home
    limpar_area_principal(area_principal)

    titulo_cadastro = ctk.CTkLabel(area_principal, text='Cadastros', font=('Helvetica', 30, 'bold'), text_color="#1b4332", fg_color='#799b2a')
    titulo_cadastro.place(relx=0.5, rely=0.05, anchor='center')

    users_imag = Image.open(resource_path("imagens/users.png"))
    users_imag = CTkImage(light_image=users_imag, size=(40, 40))

    users_b = ctk.CTkButton(area_principal, image=users_imag, text='', width=60, fg_color='#799b2a', hover_color="#A9A9A9", command=lambda: abrir_user(area_principal), bg_color='#799b2a')
    users_b.place(relx=0.07, rely=0.07, anchor='center')

    conta_imag = Image.open(resource_path("imagens/cadastro.png"))
    conta_imag = CTkImage(light_image=conta_imag, size=(40, 40))

    contas_b = ctk.CTkButton(area_principal, image=conta_imag, text='', width=60, fg_color='#799b2a', hover_color="#A9A9A9", command=lambda: abrir_cadastro_contas(area_principal), bg_color='#799b2a')
    contas_b.place(relx=0.07, rely=0.2, anchor='center')