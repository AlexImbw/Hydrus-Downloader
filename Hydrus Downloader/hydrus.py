import yt_dlp
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askdirectory

pasta_local = ("")
root = Tk()
root.title("Hydrus Downloader") #Nome da janela
imagem = tk.PhotoImage(file="hydra.png") #Carrega a imagem no tk
imagem2 = tk.Label(root, image=imagem).grid(columnspan=4, row=0) #Mostra a imagem no Frame
frm = ttk.Frame(root, padding=100)
frm.grid()
url = ('')
def onclick(): #função pegar dados da Entry
    url = chave.get() #Os dados da Entry precisam ir para uma segunda variavel para dai então serem tratados.
    print(url)
    # Configurações para o yt-dlp
    ydl_opts = {}

# Criação do objeto yt-dlp
    ydl = yt_dlp.YoutubeDL(ydl_opts)

    
    # Inicia o download do vídeo
    try:
        ydl.download([url])
        print("Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# ttk.Label(text="DOWNLOAD CONCLUÍDO!").grid(columnspan=4, row=5)

Label(frm, text="---== COLE O LINK AQUI ==---").grid(columnspan=4, row=0)
chave = Entry(frm, width=50)
chave.grid(column=0, row=1)
Button(frm, text="Download", command=onclick).grid(column=0, row=3)

root.mainloop()
