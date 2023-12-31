import pyautogui, webbrowser
from funcoes import *


nome_pagina = pyautogui.prompt(text='Qual o nome da página?', title='Nome de usuário da página')

if nome_pagina.find('@') != -1:
    nome_pagina = nome_pagina[1:]
    print(nome_pagina)

email = pyautogui.prompt(text='Qual o email que você usa no Instagram?', title='Endereço de email no Instagram')

senha = pyautogui.password(text='Qual a sua senha?', title='Senha de usuário no Instagram', mask='*') 

comentario = pyautogui.prompt(text='Insira um comentário padrão adicionar à cada nova postagem publicada', title='Comentário no Post')

# O site Será aberto na janela do seu navegadorpadrão.
webbrowser.open('https://www.instagram.com/')
pausar()

while True:    
    
    # Depende do tamanho da sua tela.
    barra_email = pyautogui.locateCenterOnScreen('./images/BarraEmail.png')

    # Depende do tamanho da sua tela.
    barra_senha = pyautogui.locateCenterOnScreen('./images/BarraSenha.png')
    
    # Depende do tamanho da sua tela.
    botao_entrar = pyautogui.locateCenterOnScreen('./images/BotaoEntrar.png')

    
    # Depende do tamanho da sua tela.
    pyautogui.click(x=barra_email[0], y=barra_email[1], duration=1.5)
    pausar()
    digitar_caracteres_especiais(email)
    pausar() 
   
    # Depende do tamanho da sua tela.
    pyautogui.click(x=barra_senha[0], y=barra_senha[1], duration=1.5)
    pausar()
    digitar_caracteres_especiais(senha)
    pausar()
 
    # Depende do tamanho da sua tela.
    pyautogui.click(x=botao_entrar[0], y=botao_entrar[1], duration=1.5)
    pausar()

    try:
        # Depende do tamanho da sua tela.
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

        curtido = True
        try:
            # Depende do tamanho da sua tela.
            botao_curtir = pyautogui.locateCenterOnScreen('./images/Coracao.png')
            pyautogui.click(x=botao_curtir[0], y=botao_curtir[1], duration=1.5)
            pausar()
        except: pass 
        else:
            curtido = False
            
            # Depende do tamanho da sua tela.
            barra_comentario = pyautogui.locateCenterOnScreen('./images/Comentario.png')
            pausar()
            # Depende do tamanho da sua tela.
            pyautogui.click(x=barra_comentario[0], y=barra_comentario[1], duration=1.5)
            pausar()
            pyautogui.press("space")
            pausar()
            digitar_caracteres_especiais(comentario)
            pausar()
            pyautogui.press("enter")
        finally:
            # Depende do tamanho da sua tela.
            pyautogui.doubleClick(x=1268,y=687, duration=1.5, interval=1)
            pausar()

            # Depende do tamanho da sua tela.
            pyautogui.click(x=909,y=184, duration=1.5)
            pausar()

            for i in range(5):
                pyautogui.press("tab")
                pausar()

            pyautogui.press("enter")
        
            if curtido:
                mensagem = 'Última publicação já  estava curtida. O programa será pausado por pelo menos 24 horas.'
            else:
                mensagem = 'Pronto! A última publicação foi curtida e comentada. O programa será pausado por pelo menos 24 horas.'

            informar_fim_do_programa(mensagem)
            parar_temporariamente()