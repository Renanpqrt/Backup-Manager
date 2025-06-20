# PLR Manager 📋💾

Aplicativo desktop para gerenciamento de contas e controle de datas de backup, desenvolvido com **Python** e **CustomTkinter**.

## 📌 Funcionalidades

- 📄 **Lista de Contas:**  
Visualize todas as contas cadastradas com informações como:  
✅ Nome  
✅ E-mail  
✅ Última Alteração  
✅ Segundo Backup  

- 🎨 **Status Visual por Cores:**  
A coluna "Última Alteração" muda de cor conforme o status da conta:  
🟩 Verde → Alterado Hoje, Ontem 
🟨 Amarelo → Alterado Anteontem  
🟥 Vermelho → Não alterado recentemente  
⬜ Branco → Sem alteração registrada  

- 🕒 **Atualização de Datas:**  
Possibilidade de atualizar o campo "Última Alteração" de forma:  
✅ Manual  
✅ Para a Data Atual  
✅ Para a Data de Ontem  

- 🚀 **Gerenciador de Backups:**  
Toplevel dedicada para iniciar e controlar o processo de backup das contas.

- 📤 **Exportação:**  
  Exporte os dados das contas para um arquivo `.xlsx`.

- 📝 **Geração de Relatórios em PDF:**  
Crie relatórios detalhados das contas em formato PDF, com formatação personalizada.


## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **CustomTkinter** (para a interface gráfica)
- **SQLAlchemy** (ORM para gerenciamento do banco de dados)
- **SQLite** (banco de dados local)

## 📂 Estrutura do Projeto (simplificada)

