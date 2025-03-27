import os 
import smtplib
from email.message import EmailMessage 

#Meus dados para login no email(poderia ser feito ocultando a senha!)

EMAIL_ADDRESS = "xxxxxxxxxxx"
EMAIL_PASSWORD = "xxxxxxxxxxxxxx"
#Caminho do meu anexo usando string bruta
ANEXO = r'C:\Users\djmat\Desktop\SADIG.xlsx'

#Mensagem sendo feita em HTML.
MENSAGEM = """
<!DOCTYPE html>
<html>
<body>
    <p>Bom dia Amanda.</p>
    <p>Tudo bem? </p>
    <p>Segue arquivo em anexo.</p>
    <p>Atenciosamente,<br>
    <img src="https://mouragro.com.br/sign/txxxxxxxxxxxxxxxxxxr.png" alt="Assinatura" style="max-width: 40%; height: auto;">
</body>
</html>
"""

#Corpo do meu e-mail e para quem vai ser enviado.
msg = EmailMessage()
msg['Subject'] = 'Arquivo Sadig'
msg['From'] = EMAIL_ADDRESS
msg['To'] = "xxxxxxxxxxxxxxxx"
msg.set_content('Este e-mail requer um cliente que suporte HTML.')  # Texto simples para clientes que não suportam HTML
msg.add_alternative(MENSAGEM, subtype='html')

with open(ANEXO, 'rb') as arquivo:
    msg.add_attachment(arquivo.read(), maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=os.path.basename(ANEXO))


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
