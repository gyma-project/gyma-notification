
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='notify')


content = "dinizrobert2002gmail.com,flechotonshabbos@gmail.com;conteudo do relatório"

channel.basic_publish(exchange='', routing_key='notify', body=content)
print(" [x] Sent 'data'")

connection.close()