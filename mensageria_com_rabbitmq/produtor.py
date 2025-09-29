import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tarefas', durable=True)

mensagens = [
    "Processar pedido 001",
    "Gerar relatório XYZ",
    "Atualizar banco de dados",
    "Enviar email de confirmação"
]

for tarefa in mensagens:
    channel.basic_publish(
        exchange='',
        routing_key='tarefas',
        body=tarefa,
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    print(f" [x] Enviado '{tarefa}'")

connection.close()