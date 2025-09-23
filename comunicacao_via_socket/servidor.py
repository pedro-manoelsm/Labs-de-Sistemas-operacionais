import threading
import socket

HOST = "127.0.0.1"
PORT = 5000

def cliente(conn, addr):
    print(f"cliente encontrado: {addr}")

    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
            if not msg:
                break
            
            print(f"{addr}, {msg}")

            if msg.lower() == "sair":
                conn.send("conexão encerrada pelo cliente".encode("utf-8"))
                break

            resposta = "Mensagem recebida com sucesso"
            conn.send(resposta.encode("utf-8"))
        except:
            break

    conn.close()
    print(f"Cliente {addr} saiu")

def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()

    print(f"Esperando conexão em {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=cliente,args = (conn, addr))
        thread.start()
        print(f"{threading.active_count()-1} cliente(s) conectado(s)")


if __name__ == "__main__":
    iniciar_servidor()


        
