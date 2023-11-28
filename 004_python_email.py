# Módulo SMTPLIB
"""
Esse módulo define um objeto de sessão do cliente SMTP que pode ser usado
a fim de enviar e-mail para qualquer máquina da internet com um serviço de
processamento SMTP ou ESMTP. O exemplo a seguir vai permitir que você envie
um e-mail a partir do servidor SMTP do Gmail.
"""
# Import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# O código seguinte mostra a criação da mensagem com o corpo e seus parâmetros:
# Criação de um Objeto de mensagem.
msg = MIMEMultipart() # Objeto.
texto = "Estou enviando um e-mail com Python" # Corpo mensagem em uma string.

# Parametros
senha = "sua senha"
msg['From'] = "Seu e-mail"
msg['To'] = "E-mail de destino"
msg['Subject'] = "Assunto"

# Criação do corpo  da mensagem
msg.attach(MIMEText(texto, 'plain'))

# Passos necessários para o próprio envio
# Criação do Servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.startlls()   # <--- Tem algo errado nessa linha.

# Login na conta de envio
server.login(msg['From'], senha)

#Envio da mensagem
server.sendmail(msg['From'], msg['To', msg.as_string])

# Encerramento do servidor
server.quiet()

print('Mensagem enviada com sucesso')