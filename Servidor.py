import socket

HOST = '127.0.0.1'
PORT = 5000

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT))
        servidor.listen()
        print(f"[SERVIDOR] Conectado en {HOST}:{PORT}")

        while True:
            conexion, direccion = servidor.accept()
            with conexion:
                print(f"[SERVIDOR] Conexión establecida desde {direccion}")
                while True:
                    datos = conexion.recv(1024).decode()
                    if not datos:
                        break

                    print(f"[SERVIDOR] Mensaje recibido: {datos}")
                    
                    if datos.strip().upper() == "DESCONEXION":
                        print(f"[SERVIDOR] Cliente {direccion} desconectado.")
                        break
                    else:
                        respuesta = datos.upper()
                        conexion.sendall(respuesta.encode())

if __name__ == "__main__":
    iniciar_servidor()