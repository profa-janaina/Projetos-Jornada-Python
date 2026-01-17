import pyautogui
import pandas as pd
import time

# Importar a base de produtos

# Automação
#Tempo de espera entre os comandos pyautogui e link
pyautogui.PAUSE = 0.7
link_sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Abrir o sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link_sistema)
pyautogui.press("enter")

#Esperar site abrir
time.sleep(3)

#Login no sistema
pyautogui.click(x=415, y=375)
pyautogui.write("meu_email@email.com")
pyautogui.press("tab")
pyautogui.write('minhaS&nha123')
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(4)

#Abrir a base de dados
#caminho = r"d:\Users\Janaína\Acesso rápido\Udemy\Curso JS\Python\Projetos Jornada Python - Hashtag\P1 - Automação_Tarefas_e_Bots\produtos.csv"
caminho = r"./P1 - Automação_Tarefas_e_Bots/produtos.csv"
tabela = pd.read_csv(caminho)



#Cadastro produto
# for linha in tabela.index:
#     pyautogui.click(x=411, y=257)
#     print(tabela.loc[linha, "codigo"])
#     pyautogui.write(str(tabela.loc[linha, "codigo"]))
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "marca"]))
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "tipo"]))
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "categoria"]))
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
#     pyautogui.press("tab")
#     pyautogui.write(str(tabela.loc[linha, "custo"]))
#     pyautogui.press("tab")
#     obs = str(tabela.loc[linha, "obs"])
#     if obs != "nan":
#         pyautogui.write(obs)
#     pyautogui.press("tab")

#     pyautogui.press("enter")

#     pyautogui.scroll(5000)