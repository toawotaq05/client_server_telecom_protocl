import numpy as np
# from ..signal import (
#     modulator, signal_generator, demodulator, signal_decoder
# )
from src.lib.communications import encode_and_send_message, receive_and_decode_message
from socket import socket
from src.log_config import setup_logger
logger = setup_logger(__name__)

HEADER_START = "LEN"
HEADER_END = "END"
HEADER_LENGTH = 5

def variable_message_send(s: socket, message: str):
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    length = len(message)
    header = f"{HEADER_START}{length:0{HEADER_LENGTH}}{HEADER_END}"

    # Send header
    try:
        encode_and_send_message(s, header)
        logger.debug("Header sent: %s", header)
    except Exception as e:
        logger.error("Failed to send header: %s", e)
        return False

    # Send message
    try:
        encode_and_send_message(s, message)
        logger.debug("Message sent: %s", message)
        return True
    except Exception as e:
        logger.error("Failed to send message: %s", e)
        return False
    
def variable_message_recv(s: socket) -> str:
    try:
        rcvd_header = receive_and_decode_message(s)
        logger.debug("Received header: %s", rcvd_header)
    except Exception as e:
        logger.error("Failed to receive header: %s", e)
        return None

    if len(rcvd_header) != HEADER_LENGTH + len(HEADER_START) + len(HEADER_END):
        logger.error("Received header has an incorrect length")
        return None

    if not (rcvd_header.startswith(HEADER_START) and rcvd_header.endswith(HEADER_END)):
        logger.error("Received header format is incorrect")
        return None

    rcvd_header_length_str = rcvd_header[len(HEADER_START):len(HEADER_START) + HEADER_LENGTH]
    if not rcvd_header_length_str.isdigit():
        logger.error("Received header does not contain a valid length")
        return None

    rcvd_header_length = int(rcvd_header_length_str)
    logger.debug("recieved header length (int): %d", rcvd_header_length)
    rcvd_message_window_length = rcvd_header_length * 8**2 * 100

    try:
        rcvd_msg = receive_and_decode_message(s, rcvd_message_window_length)
        logger.debug("Received msg: %s", rcvd_msg)
        return rcvd_msg
    except Exception as e:
        logger.error("Failed to receive message: %s", e)
        return None