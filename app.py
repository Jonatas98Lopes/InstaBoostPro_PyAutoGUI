import pyautogui, pyperclip, webbrowser
from funcoes import *



nome_pagina = pyautogui.prompt(text='Qual o nome da página?', title='Nome de usuário da página')

email = pyautogui.prompt(text='Qual o email que você usa no Instagram?', title='Endereço de email no Instagram')

senha = pyautogui.password(text='Qual a sua senha?', title='Senha de usuário no Instagram', mask='*') 

while True:
	
	# O site Será aberto na janela do seu navegadorpadrão.
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
	except: 
		pausar()
	finally:
		webbrowser.open(f'https://www.instagram.com/{nome_pagina}')
		pausar()
		
		# Depende do tamanho da sua tela.
		pyautogui.click(x=1197,y=286, duration=1.5)
		pausar()

		# Depende do tamanho da sua tela.
		pyautogui.scroll(-470)
		pausar()
  
		# Depende do tamanho da sua tela.
		pyautogui.click(x=801, y=292, duration=1.5)
		pausar()

		try:
			botao_curtir = pyautogui.locateCenterOnScreen('./images/Coracao.png')
			pyautogui.click(x=botao_curtir[0], y=botao_curtir[1], duration=1.5)
			pausar()
		except: 
			pyautogui.alert(text='Última publicação já  estava curtida. O programa será pausado por pelo menos 24 horas.', title='Informação', button='Ok')
		else:
			comentario = pyautogui.prompt(text='Insira um comentário no seu post:', title='Comentário no Post')


		
			barra_comentario = pyautogui.locateCenterOnScreen('./images/Comentario.png')
			pausar()
			pyautogui.click(x=barra_comentario[0], y=barra_comentario[1], duration=1.5)
			pausar()
			pyautogui.press("space")
			pausar()
			digitar_caracteres_especiais(comentario)
			pausar()
			pyautogui.press("enter")
			pyautogui.alert(text='Pronto! A última publicação foi curtida e comentada. O programa será pausado por pelo menos 24 horas.', title='Informação', button='Ok')
		finally:
			parar_temporariamente()
