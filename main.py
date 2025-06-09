from dados import tabelas
import customtkinter as ctk
from login import abrir_login
from util import resource_path

def inciar_app():
    app = ctk.CTk()
    app.title('PLR Manager')
    app.geometry('900x600')
    app.resizable(False, False)
    app._set_appearance_mode('dark')
    app.iconbitmap(resource_path("imagens/BKP.ico"))
   
    frame_principal = ctk.CTkFrame(app, fg_color='#1E1E1E')
    frame_principal.pack(fill="both", expand=True)

    abrir_login(app, frame_principal)
    app.mainloop()

inciar_app()