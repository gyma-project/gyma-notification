import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from DTOs.MessageDTO import MessageDTO
from dotenv import load_dotenv
import os

# Configurações do servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_user = os.getenv('EMAIL_USER')
email_password = os.getenv('EMAIL_APP_KEY')

# Função para enviar e-mails
def send_email_to(message: MessageDTO):
    print("Entrando na função de envio de e-mail...")
    
    # Criando a mensagem
    messageEmail = MIMEMultipart()
    messageEmail["From"] = email_user
    messageEmail["To"] = message.receiverEmail
    messageEmail["Subject"] = message.title

    # Adicionando o corpo do e-mail
    messageEmail.attach(MIMEText(message.description, "plain"))

    try:
        with smtplib.SMTP_SSL(smtp_server, 465, timeout=30) as server:
            print("Conectando ao servidor SMTP via SSL...")
            server.login(email_user, email_password)
            server.sendmail(email_user, message.receiverEmail, messageEmail.as_string())


        print("E-mail enviado com sucesso!")
        return "E-mail enviado com sucesso!"
    
    except smtplib.SMTPException as e:
        print(f"Erro SMTP: {e}")
        return f"Erro ao enviar o e-mail: {e}"
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return f"Erro ao enviar o e-mail: {e}"

    finally:
        print("Função de envio de e-mail finalizada.")
