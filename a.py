import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://www.instagram.com')
sleep(5)

email = pyautogui.locateCenterOnScreen('./images/BarraEmail.png')
print(email)

senha = pyautogui.locateCenterOnScreen('./images/BarraSenha.png')
print(senha)

entrar = pyautogui.locateCenterOnScreen('./images/BotaoEntrar.png')
print(entrar)




