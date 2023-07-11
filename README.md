# InstaBoostPro_PyAutoGUI
Vamos criar um bot que para curtir o primeiro post da página que o usuário definir. Esta aplicação deve verificar se a postagem mais atual ainda não foi curtida pelo bot. Caso a postagem não tenha sido curtida, ele deve entrar nessa postagem, curtir e comentar algo nela.

***

## Descrição das instruções: 

1.  Solicitar uma página ao usuário.
2. Solicitar nome de usuário.
3.  Solicitar senha.
4.  Abrir o navegador
5.  Navegar até o site https://www.instagram.com
6.  Digitar o nome de usuário.
7.  Digitar a senha.
8.  Apertar no botão de logar.
9.  Clicar em 'not now' para não manter conectado.
10.  Acessar a página que o usuário informou.
11.  Abrir o primeiro post.

SE O POST NÃO TIVER SIDO CURTIDO:
 
     13. Curtir o post
     
     14. Solicitar um comentário ao usuário
         
     15. Digitar o comentário.
     
     16. Informar ao usuário que o programa ficará pausado por 24 horas.
     
     17. Repetir o processo após 24 horas.

CASO O POST JÁ ESTEJA CURTIDO:
     
     13. Informar ao usuário que o post já estava curtido.
     
     14. Informar ao usuário que o programa ficará pausado por 24 horas.
     
     15. Repetir o processo após 24 horas.

***

## Como rodar o projeto?

### Vídeo de apresentação do projeto e primeiros passos:

Assista ao vídeo de funcionamento do projeto  [clicando aqui!](https://www.linkedin.com/feed/update/urn:li:activity:7084661680470667264/) 

Assim que clonar este código, sugire que você crie um ambiente virtual isolando os arquivos que estão no seu computador do diretório do projeto.

### Criando ambiente virtual com Python:

1. Certifique-se que você selecionou a opção **Add to path** quando instalou o Python 3.

2. Estando dentro da pasta do projeto, abra o seu terminal:

3. Caso esteja no Windows, rode o comando abaixo e aguarde a criação:

```
python -m venv nome_do_ambiente_virtual
```
***nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

Caso esteja no Linux ou Mac, rode o comando abaixo e aguarde a criação:

```
python3 -m venv nome_do_ambiente_virtual
```
***nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

4. Ative o ambiente virtual através do seu terminal:

No caso do Windows, rode:
```
nome_do_ambiente_virtual\Scripts\activate
```
***nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

No caso do Linux ou Mac, rode:
```
source nome_do_ambiente_virtual\bin\activate
```
***nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

5. Feito isso, vamos instalar as bibliotecas necessárias através do arquivo **requirements.txt**:

No Windows, estando dentro da pasta do projeto  e com o ambiente virtual ativado, rode:

```
pip install -r requirements.txt
```

No Linux ou MAC, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:
```
pip3 install -r requirements.txt
```

Pronto! Você está apto para rodar o projeto.

### Possíveis problemas:

Primeiramente, entenda que a biblioteca **PyAutoGUI** foi criada para automatizações que dependem do tamanho da sua tela. Em outras palavras, se você utilizar uma tela de tamanho diferente do computador em que a aplicação foi testada, é muito provável que a aplicação quebre. No meu caso, eu dividi a tela no meio, com o editor de texto à esquerda e o navegador, à direita, então, tente fazer o mesmo no seu computador.


Caso você tenha este tipo de problema, olhe código do fonte do programa - **app.py**. Os comandos que dependem do tamanho da sua tela recebem um comentário na sua linha de cima escrito: 

**Depende do tamanho da sua tela.**. Além disso, é possível que o seu navegador padrão não mostre claramente algum item que foi localizado via imagem(print). Se isso acontecer, tente mudar alterar o tamanho da janela do navegador ou tire outros prints e salve-os sobrescrevendo a imagem correspondente na pasta **images**.

