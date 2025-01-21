import pytest
from services.email import send_email_to

# Testes de emails
def test_send_email_to_with_valid_email():
    """
    Teste de envio com email correto
    """
    resultado = send_email_to("example@gmail.com", "testContent")
    
    assert resultado == True
    
def test_send_email_to_with_no_email():
    """
    Teste de envio sem emails definidos
    """
    with pytest.raises(ValueError):
        send_email_to("", "testContent")
        
def test_send_email_to_with_invalid_email():
    """
    Teste de envio com email inválido
    """
    with pytest.raises(ValueError):
        send_email_to("examplegmailcom", "testContent")

def test_send_email_to_with_more_than_one_valid_email():
    """
    Teste de envio com mais de um email, sendo todos válidos
    """
    resultado = send_email_to("example@gmail.com,example1@gmail.com,example2@gmail.com", "testContent")
    
    assert resultado == True

def test_send_email_to_with_more_than_one_invalid_email():
    """
    Teste de envio com mais de um email, sendo um deles invalido
    """
    with pytest.raises(ValueError):
        send_email_to("example@gmail.com,example1@gmail.com,examplegmailcom", "testContent")


# Testes de conteúdo
def test_send_email_to_with_no_content():
    """
    Teste de envio sem conteúdo
    """
    with pytest.raises(ValueError):
        send_email_to("example@gmail.com", "")