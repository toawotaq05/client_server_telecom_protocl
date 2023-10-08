import numpy as np
"""
Converts the digital signals (bits) into BPSK modulated signals.
Essentially, it will map 0s and 1s to specific phase values (e.g., 0° and 180°).
"""

def bpsk_modulate(bit_sequence, sample_rate=100, carrier_freq=2):
    """
    Modulate a binary sequence using BPSK.

    Args:
    - bit_sequence (str): The binary sequence to be modulated.
    - sample_rate (int): Number of samples per bit.
    - carrier_freq (int): Frequency of the carrier wave.

    Returns:
    - numpy.ndarray: The BPSK modulated signal.
    """
    # Create a time vector for one bit duration
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    
    # Create a base carrier wave
    carrier = 2 * np.pi * carrier_freq * t
    
    # Initialize an empty array for the modulated signal
    modulated_signal = np.array([])
    
    for bit in bit_sequence:
        if bit == '0':
            # For bit=0, phase is 0°
            signal = np.cos(carrier)
        elif bit == '1':
            # For bit=1, phase is 180° (which is π in radians)
            signal = np.cos(carrier + np.pi)
        else:
            raise ValueError(f"Invalid bit: {bit}. Expected 0 or 1.")
        
        # Append the signal for this bit to the modulated signal
        modulated_signal = np.concatenate([modulated_signal, signal])

    return modulated_signal

# For testing purposes:
if __name__ == '__main__':
    test_binary = "0000"
    modulated_signal = bpsk_modulate(test_binary)
    print(f"Modulated Signal for {test_binary}: {modulated_signal}")
    np.save("0000_to_BPSK", modulated_signal)
