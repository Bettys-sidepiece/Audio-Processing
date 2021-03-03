import numpy as np
import wave   # This module provides a convenient interface to the WAV sound format
import struct # converts string and numbers in bytes and vice versa
from matplotlib import pyplot as plt

freq = 1000 #frequency of the wave
n_samples = 48000 

rate = 48000.0 #Sammplin rate, this is the rate of analogue to digital conversion
amp = 16000 #Amplitude of the signal
file = "sine_test.wav" # Name and file extension of output file

# This line below generates a sine wave 
sin_wave = [np.sin(2*np.pi*freq*n/rate) for n in range(n_samples)]

nframes = n_samples # the number of frames or samples 
comptype="NONE"  # This determines the type of compression a signal should have "NONE" is the only supported type
compname="not compressed" #This defines if a signal is compressed or not 
nchannels=1 # number of channels .i.e 1 mono and  2 stereo
sampwidth=2 #sample width in byte

wav_file = wave.open(file,'wb') #Writes the wave

wav_file.setparams((nchannels, sampwidth, int(rate),nframes,comptype,compname))
for s in sin_wave:
    wav_file.writeframes(struct.pack('h', int(s*amp))) 
    
wav_file.close()

