import pyperclip, pyautogui
from time import sleep
from random import randint

def digitar_caracteres_especiais(frase):
	"""
  Essa função nos permite digitar textos com caracteres especiais como: à, á, é, ç...
  
  Ela aceita um único parametro chamado 'frase' onde frase é uma string.
  """
	pyperclip.copy(frase)
	pyautogui.hotkey('ctrl', 'v')
	
def pausar():
	"""
  Faz o programa ficar parado de 2 até 10 segundos. O tempo em que o programa ficará pausado é definido aleatoriamente.
  
  Esta função não aceita parâmetros.
  """
	sleep(randint(2, 10))
	
def repousar():
	"""
  Faz o programa ficar parado de 20 até 30 segundos. O tempo em que o programa ficará pausado é definido aleatoriamente.
  
  Esta função não aceita parâmetros.
  """
	sleep(randint(20, 30))

def parar_temporariamente():
	"""
  Faz o programa ficar parado de 24 até 30 horas. O tempo em que o programa ficará pausado é definido aleatoriamente.
  
  Esta função não aceita parâmetros.
  """
	sleep(randint(86400, 108000))