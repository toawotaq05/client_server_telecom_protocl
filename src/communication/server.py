import socket
from src.communication.handshake import server_perform_handshake
from src.communication.variable_msg_length import variable_message_send

def main():
    HOST = '127.0.0.1'
    PORT = 65432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    s.bind((HOST, PORT))
    s.listen()
    
    with s:
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by: {addr}")

            # Perform handshake
            if server_perform_handshake(conn):
                print("Handshake successful!")
                # Continue with the rest of your server logic here
            else:
                print("Handshake unsuccessful!")
            
            message = "Variable length message you cannot predict?"
            print("sending out message: ", message)
            variable_message_send(conn, message)
            print("Success! Server shutting down.")
            
            

if __name__ == "__main__":
    main()