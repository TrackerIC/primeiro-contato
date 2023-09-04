import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Oculta a janela principal, se desejar

# Defina os argumentos para personalizar a caixa de diálogo
file_path = filedialog.askopenfilename(
    initialdir="/",
    title="Selecione a Planilha",
    filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")],
    defaultextension=".txt"
)

# Verifique se um arquivo foi selecionado
if file_path:
    print("Arquivo selecionado:", file_path)
else:
    print("Nenhum arquivo selecionado.")
