import pyautogui
from time import sleep
import os
import smtplib
from email.message import EmailMessage

# 1 - Clicar e digitar (usuario?) e depois clicar em enter
pyautogui.click(1484, 967, duration=0.5)
pyautogui.write('Escrevendo algo aleatorio')
pyautogui.click(1874, 966, duration=0.5)

print("Arquivo gerado com sucesso.")

# Aguardar um momento para garantir que a primeira parte termine
sleep(2)  # Ajuste o tempo conforme necessário

# 2 - Enviar e-mail
EMAIL_ADDRESS = "xxxxxxxx@email.com"
EMAIL_PASSWORD = "umasenhamutopotente"  # Considere usar um método mais seguro para armazenar a senha
ANEXO = r'C:\Users\djmat\Desktop\SADIG.xlsx'

MENSAGEM = """
<!DOCTYPE html>
<html>
<body>
    <p>Bom dia Amanda.</p>
    <p>Tudo bem? </p>
    <p>Segue arquivo em anexo.</p>
    <p>Atenciosamente,<br>
    <img src="https://mouragro.com.br/sign/xxxxxxxxxxxxxx.png" alt="Assinatura" style="max-width: 40%; height: auto;">
</body>
</html>
"""

# Corpo do e-mail
msg = EmailMessage()
msg['Subject'] = 'Arquivo Sadig'
msg['From'] = EMAIL_ADDRESS
msg['To'] = "xxxxxxxxxxxxxxxxxxx@gmail.com"
msg.set_content('Este e-mail requer um cliente que suporte HTML.')
msg.add_alternative(MENSAGEM, subtype='html')

# Anexar o arquivo
with open(ANEXO, 'rb') as arquivo:
    msg.add_attachment(arquivo.read(), maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=os.path.basename(ANEXO))

# Enviar o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
print("Email enviado com sucesso.")