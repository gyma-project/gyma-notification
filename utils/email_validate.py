import re

def email_validate_list(lista_emails):
    lista_emails = lista_emails.split(",")
    
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return all(re.match(padrao_email, email) for email in lista_emails)