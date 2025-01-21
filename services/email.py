import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from utils.email_validate import email_validate_list
import os

# Configurações do servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_user = os.getenv('EMAIL_USER')
email_password = os.getenv('EMAIL_APP_KEY')

# Função para enviar e-mails
def send_email_to(email_list, content):
    print("Entrando na função de envio de e-mail...")
    
    if not (email_validate_list(email_list)):
        print("Erro, lista contém emails inválidos")
        return
    
    
    print("\nProcessando envio para emails:", email_list)
    # Criando a mensagem
    messageEmail = MIMEMultipart()
    messageEmail["From"] = email_user
    messageEmail["To"] = email_list
    messageEmail["Subject"] = "Relatório"

    # Adicionando o corpo do e-mail
    messageEmail.attach(MIMEText(content, "plain"))

    try:
        with smtplib.SMTP_SSL(smtp_server, 465, timeout=30) as server:
            server.login(email_user, email_password)
            server.sendmail(email_user, email_list, messageEmail.as_string())


        print("Enviado - OK")
    
    except smtplib.SMTPException as e:
        print(f"Erro - {e}")
    
    except Exception as e:
        print(f"Erro - {e}")

    finally:
        print("Envio finalizado!")
