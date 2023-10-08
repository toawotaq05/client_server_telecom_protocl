"""
Converts the received BPSK signal back into digital signals (bits).
"""

import numpy as np

def bpsk_demodulate(received_signal: np.array, sample_rate=100, carrier_freq=2) -> str:
    """
    Demodulate a BPSK modulated signal.

    Args:
    - received_signal (numpy.ndarray): The BPSK modulated signal to be demodulated.
    - sample_rate (int): Number of samples per bit.
    - carrier_freq (int): Frequency of the carrier wave.

    Returns:
    - str: The demodulated binary sequence.
    """

    # Create a time vector for one bit duration
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    
    # Create a reference carrier wave
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    
    # Number of bits in the received signal
    num_bits = len(received_signal) // sample_rate

    # Initialize an empty string to store the demodulated bits
    demodulated_bits = ""
    
    for i in range(num_bits):
        # Extract the current bit's samples from the received signal
        current_samples = received_signal[i*sample_rate: (i+1)*sample_rate]
        
        # Multiply the samples with the reference carrier
        product = current_samples * carrier
        
        # Integrate the product over the bit duration (i.e., summing is a form of integration in discrete-time signals)
        result = np.sum(product)
        
        # Determine the bit based on the sign of the result
        if result > 0:
            demodulated_bits += '0'
        else:
            demodulated_bits += '1'

    return demodulated_bits
