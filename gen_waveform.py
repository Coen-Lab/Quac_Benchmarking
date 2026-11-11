import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

RATE = 500_000                           # must match FileSettings.UpdateFrequency
AMPLITUDE = 5.0                          # must match FileSettings.Amplitude

def volts_to_codes(v):
    return np.clip(np.round((np.asarray(v) + 10) / 20 * 65535), 0, 65535).astype("<u2")
#

if __name__ == "__main__":
    FREQUENCY = 2000.0                       # must match FileSettings.Frequency
    NUMBER_OF_CYCLES = 200                   # number of cycles to generate
    DURATION = NUMBER_OF_CYCLES / FREQUENCY  # duration of the waveform in seconds

    t = np.arange(int(DURATION * RATE)) / RATE         # duration of the waveform in seconds
    # square wave
    v = AMPLITUDE * (signal.square(2 * np.pi * FREQUENCY * t) + 1) / 2
    v[-1] = 0.0                                        # end at 0 V

    print("Duration in us: " + str(int(DURATION * 1e6)))

    volts_to_codes(v).tofile("channel_0_short.bin")
    volts_to_codes(v).tofile("channel_1_short.bin")
    volts_to_codes(v).tofile("channel_2_short.bin")
    volts_to_codes(v).tofile("channel_3_short.bin")

    ## now the long waveforms
    FREQUENCY = 2000.0                       # must match FileSettings.Frequency
    NUMBER_OF_CYCLES = 10000                 # number of cycles to generate
    DURATION = NUMBER_OF_CYCLES / FREQUENCY  # duration of the waveform in seconds

    t = np.arange(int(DURATION * RATE)) / RATE         # duration of the waveform in seconds
    # square wave
    v = AMPLITUDE * (signal.square(2 * np.pi * FREQUENCY * t) + 1) / 2
    v[-1] = 0.0                                        # end at 0 V

    print("Duration in us: " + str(int(DURATION * 1e6)))

    volts_to_codes(v).tofile("channel_0_long.bin")
    volts_to_codes(v).tofile("channel_1_long.bin")
    volts_to_codes(v).tofile("channel_2_long.bin")
    volts_to_codes(v).tofile("channel_3_long.bin")


    ## now the long waveforms
    FREQUENCY = 2000.0                       # must match FileSettings.Frequency
    NUMBER_OF_CYCLES = 10000                 # number of cycles to generate
    DURATION = NUMBER_OF_CYCLES / FREQUENCY  # duration of the waveform in seconds

    t = np.arange(int(DURATION * RATE)) / RATE         # duration of the waveform in seconds
    # sine wave
    v = AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t)  # any waveform you like, in volts
    v[-1] = 0.0                                        # end at 0 V

    print("Duration in us: " + str(int(DURATION * 1e6)))

    volts_to_codes(v).tofile("channel_0_sine.bin")
    volts_to_codes(v).tofile("channel_1_sine.bin")
    volts_to_codes(v).tofile("channel_2_sine.bin")
    volts_to_codes(v).tofile("channel_3_sine.bin")


    # Visualize the waveform
    if 0:
        plt.plot(v)
        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V]")
        plt.title("Generated Waveform")
        plt.grid(True)
        plt.show()
    #
#
