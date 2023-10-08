import socket
from src.communication.handshake import server_perform_handshake
from src.log_config import setup_logger
from src.communication.variable_msg_length import variable_message_send

logger = setup_logger(__name__)
logger.debug("This is a debug message.")

def main():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
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
            
            variable_message_send(conn, "How about this?")
            print("Success! Server shutting down.")
            
            

if __name__ == "__main__":
    main()