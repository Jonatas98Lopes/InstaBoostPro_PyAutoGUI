import pyautogui, pyperclip, webbrowser
from funcoes import *


# - Solicitar uma página ao usuário.
# nome_pagina = pyautogui.prompt(text='Qual o nome da página?', title='Nome de usuário da página')
# # # - Solicitar nome de usuário.
# email = pyautogui.prompt(text='Qual o email que você usa no Instagram?', title='Endereço de email no Instagram')
# # # - Solicitar senha.
# senha = pyautogui.password(text='Qual a sua senha?', title='Senha de usuário no Instagram', mask='*')

while True:
	# - Abrir o navegador
	# - Navegar até o site https://www.instagram.com
	webbrowser.open('https://www.instagram.com/')
	pausar()
	# - Digitar o nome de usuário
	barra_email = pyautogui.locateCenterOnScreen('./images/BarraEmail.png')
	pyautogui.click(barra_email[0], barra_email[1], duration=0.8)
	pausar()
	digitar_caracteres_especiais(email)
	pausar()
   	# # - Digitar a senha.
	barra_senha = pyautogui.locateCenterOnScreen('./images/BarraSenha.png')
	print(barra_senha)
	# pyautogui.click(barra_senha[0], barra_senha[1], duration=0.8)
	pausar()
	digitar_caracteres_especiais(senha)
	pausar()
	# # - Apertar no botão de logar.
	botao_entrar = pyautogui.locateCenterOnScreen('./images/BotaoEntrar.png')
	print(botao_entrar)
	pyautogui.click(botao_entrar[0], botao_entrar[1], duration=0.8)
	pausar()
	try:
	# 	# - Clicar em 'not now' para não manter conectado.
		x, y = pyautogui.locateCenterOnScreen('./images/NotNow.png')
		pyautogui.click(x=x, y=y, duration=0.8)
		pausar()
	except: pass
	finally:
	# 	# - Acessar a página que o usuário informou.
		webbrowser.open(f'https://www.instagram.com/{nome_pagina}')
		pausar()
	# 	# - Abrir o primeiro post.
		pyautogui.click(x=773, y=662, duration=0.8)
		pausar()
		try:
	# 		# SE O POST NÃO TIVER SIDO CURTIDO:
	# 		# 	- Curtir o post
			x, y = pyautogui.locateCenterOnScreen('./images/Coracao.png')
			pausar()
		except: pass
		else:
			pyautogui.click(x=x, y=y, duration=0.8)
			pausar()
	# 		# 	- Solicitar um comentário ao usuário
			comentario = pyautogui.prompt(text='Insira um comentário no seu post:', title='Comentário no Post')
	# 		# 	- Digitar o comentário
			pyautogui.click(x=932, y=579, duration=0.8)
			pausar()
			pyautogui.click(x=955, y=663, duration=0.8)
			digitar_caracteres_especiais(comentario)
			pausar()
			pyautogui.press("enter")
