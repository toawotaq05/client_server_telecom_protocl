import numpy as np
from ..signal import (
    modulator, signal_generator, demodulator, signal_decoder
)
from socket import socket

from src.log_config import setup_logger
logger = setup_logger(__name__)

def receive_and_decode_message(s: socket, recv_window: int = 8**7) -> str:
    data = s.recv(recv_window)
    logger.debug("Listened for %s data.", len(data))
    
    received_signal = np.frombuffer(data, dtype=np.float64)
    # logger.debug("received Signal: %s", received_signal)
    logger.debug("received Signal Length: %d", len(received_signal))
    
    
    demodulated_data = demodulator.bpsk_demodulate(received_signal)
    logger.debug("Demodulated Data: %s", demodulated_data)
    logger.debug("Demodulated Data Length: %d", len(demodulated_data))
    
    logger.debug("final message recieved: %s", signal_decoder.binary_to_string(demodulated_data))

    return signal_decoder.binary_to_string(demodulated_data)

def encode_and_send_message(s: socket, message: str) -> None:
    logger.debug("Message to be sent: %s", message)
    binary_data = signal_generator.string_to_binary(message)  # Assuming you have this function available
    logger.debug("Message to binary data: %s", binary_data)
    logger.debug("binary length: %d", len(binary_data))
    
    modulated_data = modulator.bpsk_modulate(binary_data)
    logger.debug("binary data modulated to length: %d", len(modulated_data))
    logger.debug("binary data (tobytes) modulated to length: %d", len(modulated_data.tobytes()))

    s.sendall(modulated_data.tobytes())