from time import sleep
import pandas
import pyautogui
import pyperclip

# Acessar o drive e fazer o dowloand
pyautogui.PAUSE = 1
pyautogui.click(x=662, y=745, clicks=1)
sleep(10)
pyperclip.copy('https://drive.google.com/drive/u/0/my-drive')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)
pyautogui.click(x=563, y=281, clicks=2)
sleep(3)
pyautogui.click(x=317, y=440, button="right")
sleep(3)
pyautogui.click(x=458, y=438, clicks=1)

# Abrir e analisar o arquivo

tabela = pandas.read_excel(r'C:\Users\pedro\Downloads/Vendas - Dez.xlsx', engine='openpyxl')
faturamente = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
print(faturamente)
print(quantidade)

# Enviar o E-mail

