import numpy as np
import matplotlib.pyplot as plt
import struct
import wave

freq = 1000
noisy_freq = 369.994
n_samples = 48000

sam_rate = 48000.0

file = "sine_with_noise(G_minor).wav"

sine_wave = [np.sin(2*np.pi*freq*n/sam_rate) for n in range(n_samples)]
sine_noise = [np.sin(2*np.pi*noisy_freq*n/sam_rate) for n in range(n_samples)]

sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

combine_signal = sine_noise+sine_wave

nframes = n_samples # the number of frames or samples 
comptype="NONE"  # This determines the type of compression a signal should have "NONE" is the only supported type
compname="not compressed" #This defines if a signal is compressed or not 
nchannels=1 # number of channels .i.e 1 mono and  2 stereo
sampwidth=2 #sample width in byte
"""
wav_file = wave.open(file,'wb') #Writes the wave
wav_file.setparams((nchannels, sampwidth, int(sam_rate),nframes,comptype,compname))
for s in combine_signal:
    wav_file.writeframes(struct.pack('h', int(s*1000))) 
wav_file.close()
"""
data_fft = np.fft.fft(combine_signal)
freq = (np.abs(data_fft[:len(data_fft)]))

plt.plot(freq)
plt.title("Sine and G_minor")
plt.xlim(0, 1200)
plt.show()
