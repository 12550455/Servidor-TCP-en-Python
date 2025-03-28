import socket

HOST = '127.0.0.1'
PORT = 5000

def iniciar_cliente():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))
        print(f"[CLIENTE] Conectado en la direccion y puerto {HOST}:{PORT}")

        while True:
            mensaje = input("Escribe un mensaje o escribe 'DESCONEXION' para salir: ")
            cliente.sendall(mensaje.encode())

            if mensaje.strip().upper() == "DESCONEXION":
                print("[CLIENTE] Has sido desconectado del servidor.")
                break

            respuesta = cliente.recv(1024).decode()
            print(f"[CLIENTE] Respuesta del servidor: {respuesta}")

if __name__ == "__main__":
    iniciar_cliente()