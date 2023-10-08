import socket
from src.lib.communications import encode_and_send_message, receive_and_decode_message

def server_perform_handshake(conn: socket) -> bool:
    # Receive SYN
    # data = conn.recv(1024).decode('utf-8')
    data = receive_and_decode_message(conn)
    if data == "SYN":
        # Send SYN-ACK
        # conn.sendall("SYN-ACK".encode('utf-8'))
        encode_and_send_message(conn, "SYN-ACK")
        # Wait for ACK
        # data = conn.recv(1024).decode('utf-8')
        data = receive_and_decode_message(conn)
        if data == "ACK":
            return True
    return False

def client_initiate_handshake(s: socket) -> bool:
    import time

    # Send SYN
    encode_and_send_message(s, "SYN")

    # Wait for SYN-ACK
    data = receive_and_decode_message(s)
    if data == "SYN-ACK":
        # Introducing a slight delay before ACK for clarity in demonstration
        time.sleep(1)
        # Send ACK
        encode_and_send_message(s, "ACK")
        return True

    return False
