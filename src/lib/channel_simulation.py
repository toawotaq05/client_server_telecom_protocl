import numpy as np

def add_awgn_noise(signal: np.ndarray, snr_db: float) -> np.ndarray:
    """Add AWGN noise to a signal to achieve a given SNR (in dB).
    
    Parameters:
        signal (numpy.ndarray): The original signal
        snr_db (float): The desired signal-to-noise ratio in dB
    
    Returns:
        numpy.ndarray: The signal with added noise
    """
    # Calculate signal power
    sig_power = np.mean(np.abs(signal)**2)
    
    # Calculate noise power based on SNR
    noise_power = sig_power / 10**(snr_db / 10)
    
    # Generate noise
    noise = np.sqrt(noise_power) * np.random.normal(size=signal.shape)
    
    # Add noise to signal
    noisy_signal = signal + noise
    
    return noisy_signal
