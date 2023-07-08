import pyautogui, pyperclip, webbrowser
from funcoes import *



nome_pagina = pyautogui.prompt(text='Qual o nome da página?', title='Nome de usuário da página')

email = pyautogui.prompt(text='Qual o email que você usa no Instagram?', title='Endereço de email no Instagram')

senha = pyautogui.password(text='Qual a sua senha?', title='Senha de usuário no Instagram', mask='*')

while True:
	
	webbrowser.open('https://www.instagram.com/')
	pausar()
	
	barra_email = pyautogui.locateCenterOnScreen('./images/BarraEmail.png')
	barra_senha = pyautogui.locateCenterOnScreen('./images/BarraSenha.png')
	botao_entrar = pyautogui.locateCenterOnScreen('./images/BotaoEntrar.png')

	pyautogui.click(x=barra_email[0], y=barra_email[1], duration=1.5)
	pausar()
	digitar_caracteres_especiais(email)
	pausar() 
   
	pyautogui.click(x=barra_senha[0], y=barra_senha[1], duration=1.5)
	pausar()
	digitar_caracteres_especiais(senha)
	pausar()
 
	pyautogui.click(x=botao_entrar[0], y=botao_entrar[1], duration=1.5)
	pausar()

	try:
		botao_not_now = pyautogui.locateCenterOnScreen('./images/NotNow.png')
		pyautogui.click(x=botao_not_now[0], y=botao_not_now[1], duration=1.5)
		pausar()
	except: pass
	finally:
		webbrowser.open(f'https://www.instagram.com/{nome_pagina}')
		pausar()
  
		pyautogui.click(x=773, y=662, duration=1.5)
		pausar()

		try:
			botao_curtir = pyautogui.locateCenterOnScreen('./images/Coracao.png')
			pyautogui.click(x=botao_curtir[0], y=botao_curtir[1], duration=1.5)
			pausar()
		except: 
			pyautogui.alert(text='Última publicação já  estava curtida. O programa será pausado por pelo menos 24 horas.', title='Informação', button='Ok')
		else:
			comentario = pyautogui.prompt(text='Insira um comentário no seu post:', title='Comentário no Post')

			pyautogui.click(x=932, y=579, duration=1.5)
			pausar()
			pyautogui.click(x=955, y=663, duration=1.5)
			digitar_caracteres_especiais(comentario)
			pausar()
			pyautogui.press("enter")
		finally:
			pyautogui.alert(text='Pronto! A última publicação foi curtida e comentada. O programa será pausado por pelo menos 24 horas.', title='Informação', button='Ok')
			parar_temporariamente()
