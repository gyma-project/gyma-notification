#!/usr/bin/env python
import json
import pika, sys, os

from services.email import send_email_to

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notify')

    def callback(ch, method, properties, body):
        
        print(f" [x] Received {body}")
        
        
        # Decodificar de bytes para string
        decoded_body = body.decode('utf-8')

        # Dividir a string
        email_list_to_send, content = decoded_body.split(";")
        
        # Dividir emails para array
        
        
        print("")
        print("Realizando envio para a lista de emails:")
        print(email_list_to_send)
        print("Conteúdo a ser enviado:", content)
        print("")
        
        send_email_to(email_list_to_send, content)

    channel.basic_consume(queue='notify', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def run_rabbit():
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            
            
run_rabbit()