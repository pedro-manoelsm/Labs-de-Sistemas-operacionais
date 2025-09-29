import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tarefas', durable=True)
print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')

def callback(ch, method, properties, body):
    mensagem = body.decode()
    print(f" [x] Recebido: {mensagem}")
    time.sleep(2)
    print(" [v] Tarefa concluída")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='tarefas', on_message_callback=callback, auto_ack=False)

channel.start_consuming()







































































































