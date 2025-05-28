import customtkinter as ctk
from util import limpar_tela, resource_path
from dados.tabelas import Conta, Conta_dados, session
from PIL import Image
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox

def abrir_cadastro_contas(janela, frame_atual):
    from cadastros.cadastro import abrir_cadastros
    limpar_tela(frame_atual)

    titulo = ctk.CTkLabel(frame_atual, text='Cadastros De Contas', font=('Arial', 20, "bold"), fg_color="#08254b", text_color='white')
    titulo.place(relx=0.5, rely=0.05, anchor='center')

    voltar_imag = Image.open(resource_path("imagens/voltar.png"))
    voltar_imag = CTkImage(light_image=voltar_imag, size=(30, 30))

    voltar_cadastros = ctk.CTkButton(frame_atual, image=voltar_imag, width=80, fg_color='#08254b', hover_color='#A9A9A9', text='', command=lambda: abrir_cadastros(janela, frame_atual), bg_color='#08254b')
    voltar_cadastros.place(relx=0.98, rely=0.025, anchor='ne')

    tabela = ctk.CTkTabview(master=frame_atual, width=550, height=350, fg_color="#08254b", segmented_button_fg_color="#08254b",
    segmented_button_selected_color="#011125", segmented_button_selected_hover_color="#011125", segmented_button_unselected_color="gray20", segmented_button_unselected_hover_color="gray20")
    
    tabela.place(relx=0.5, rely=0.5, anchor='center')

    tabela.add("Contas")  
    tabela.add("Contas de dados")
    tabela.set("Contas")

    aba_contas = tabela.tab("Contas")
    aba_contas_dados = tabela.tab("Contas de dados")

    frame_contas = ctk.CTkScrollableFrame(aba_contas, width=550, height=350, fg_color='#08254b')
    frame_contas.pack(padx=0, pady=0, fill="both", expand=True)

    for i, conta in enumerate(session.query(Conta).all()):
        label_c = ctk.CTkLabel(frame_contas, text=conta.nome.capitalize(), text_color='white')
        label_c.grid(row=i, column=0, padx=10, pady=5)

   