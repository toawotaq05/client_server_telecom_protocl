import unittest
import numpy as np
from src.signal.modulator import bpsk_modulate
from src.signal.demodulator import bpsk_demodulate

class TestModulationDemodulationIntegration(unittest.TestCase):

    def test_integration_modulation_demodulation(self):
        # Original binary string
        original_data = "1010101001010101"

        # Use modulator to modulate the original binary string
        modulated_signal = bpsk_modulate(original_data)

        # Simulate a "received" signal (in a real scenario, this would be received over a network or some channel)
        received_signal = np.copy(modulated_signal)

        # Use demodulator to demodulate the received signal
        demodulated_data = bpsk_demodulate(received_signal)

        # Assert that the demodulated data is the same as the original data
        self.assertEqual(original_data, demodulated_data)

if __name__ == "__main__":
    unittest.main()
