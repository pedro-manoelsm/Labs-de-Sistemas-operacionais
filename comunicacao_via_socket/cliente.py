import socket

HOST = "127.0.0.1"
PORT = 5000

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    print("Conectado ao servidor")

    while True:
        msg = input("Insira sua mensagem")
        cliente.send(msg.encode("utf-8"))
        resposta = cliente.recv(1024).decode("utf-8")
        print("Servidor", resposta)

        if msg == "sair":
            break

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()