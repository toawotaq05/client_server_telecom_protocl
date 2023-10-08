import socket
from src.communication.handshake import client_initiate_handshake
from src.communication.variable_msg_length import variable_message_recv

def main():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        # Initiate handshake
        if client_initiate_handshake(s):
            print("Handshake successful!")
            # Continue with the rest of your client logic here
        else:
            print("Handshake unsuccessful!")
            
            
        final_message_recieved = variable_message_recv(s)
        print("final_message_recieved: ", final_message_recieved)
        print("Success! Client shutting down.")
        
        

if __name__ == "__main__":
    main()
