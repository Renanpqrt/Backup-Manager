from dados import tabelas
import customtkinter as ctk
from login import abrir_login
from util import resource_path

def inciar_app():
    app = ctk.CTk()
    app.title('Gerenciamento de Backups')
    app.geometry('600x500')
    app.resizable(False, False)
    app._set_appearance_mode('dark')
    app.iconbitmap(resource_path("imagens/BKP.ico"))


    frame_principal = ctk.CTkFrame(app, fg_color='#111530')
    frame_principal.pack(fill="both", expand=True)

    abrir_login(app, frame_principal)
    app.mainloop()

inciar_app()