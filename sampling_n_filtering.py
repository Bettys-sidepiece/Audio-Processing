"This program is intended to sample and filter a simple audio file"

import numpy as np
import struct as st
import wave
import matplotlib.pyplot as plt

frame_rate = 48000.0 #Audio frame rate
infile_1 = "sine_with_noise(G_minor).wav"
infile_2 = "sine_with_noise(500hz).wav"

num_samples = 48000 #Number of samples
index = 0

#This block opens and samples the wav file
wav_file_1 = wave.open(infile_1,'rb')
data_1 = wav_file_1.readframes(num_samples)
wav_file_1.close()

wav_file_2 = wave.open(infile_2,'rb')
data_2 = wav_file_2.readframes(num_samples)
wav_file_2.close

#unpack the data
data_1 = st.unpack('{n}h'.format(n = num_samples),data_1)
data_2 = st.unpack('{n}h'.format(n = num_samples),data_2)

#convert to usable data for plotting
data_1 = np.array(data_1)
data_2 = np.array(data_2)

#convert to frequency domain for analysis and filtering
data1_fft = np.fft.fft(data_1)
data2_fft =np.fft.fft(data_2)

#convert complex numbers to real components only
freq1 = np.abs(data1_fft[:len(data1_fft)])
freq2 = np.abs(data2_fft[:len(data2_fft)])

#plot the waves
plt.figure(1)
plt.subplots_adjust(hspace=1.5)
plt.subplot(4,1,1)
plt.title("sine_wave_with_noise(G_minor).wav")
plt.plot(data_1[:400])
plt.subplot(4,1,2)
plt.title("Frequency Spectrum of 'sine_wave_with_noise(G_minor).wav'")
plt.plot(freq1)
plt.xlim(0,1200)

plt.subplot(4,1,3)
plt.title("sine_wave_with_noise(500Hz).wav")
plt.plot(data_2[:400])
plt.subplot(4,1,4)
plt.title("Frequency Spectrum of 'sine_wave_with_noise(500Hz).wav'")
plt.plot(freq2)
plt.xlim(0,1200)

#High Pass Filter (Filtering out the noise)
filtered_freq1 = [f if (950 < index < 1050 and f > 1) else 0 for index, f in enumerate(freq1)]
filtered_data1 = np.fft.ifft(filtered_freq1[:len(filtered_freq1)])
filtered_data1_list = np.array(filtered_data1)

#Filtering for the noise
noise_1 = [	f if (200 < index < 500 and f > 1) else 0 for index, f in enumerate(freq1)]
filtered_noise1 = np.fft.ifft(noise_1[:len(noise_1)])
filtered_noise1_data = np.array(filtered_noise1)

#High Pass Filter (Filtering out the noise)
filtered_freq2 = [f if (950 < index < 1050 and f > 1) else 0 for index, f in enumerate(freq2)]
filtered_data2 = np.fft.ifft(filtered_freq1[:len(filtered_freq2)])


#Filtering for the noise
noise_2 = [	f if (200 < index < 500 and f > 1) else 0 for index, f in enumerate(freq2)]
filtered_noise2 = np.fft.ifft(noise_1[:len(noise_2)]) 

plt.figure(2)

plt.subplots_adjust(hspace=.9)
plt.subplot(4,1,1)
plt.title("Filtered Sine Wave")
plt.plot(filtered_data1[:400])
plt.subplot(4,1,2)
plt.title("Filtered Frequency Spectrum")
plt.plot(filtered_freq1)
plt.xlim(0,1200)

plt.subplot(4,1,3)
plt.title("Filtered Out Noise")
plt.plot(filtered_noise1[:400])
plt.subplot(4,1,4)
plt.title("Frequency spectrum of Filtered Noise")
plt.plot(noise_1)
plt.xlim(0,1200)
plt.show()

file = "Filtered_Sine.wav"
file_1 = "Filtered_noise(Gminor).wav"


#Now that the signals have been filtered you, two audio files are generated to listen to the noise and filtered signal

nframes = num_samples # the number of frames or samples 
comptype="NONE"  # This determines the type of compression a signal should have "NONE" is the only supported type
compname="not compressed" #This defines if a signal is compressed or not 
nchannels=1 # number of channels .i.e 1 mono and  2 stereo
sampwidth=2 #sample width in byte

#Write the filtered signal into the project folder
wav1 = wave.open(file,'wb') 
wav1.setparams((nchannels, sampwidth, int(48000.0),nframes,comptype,compname))

for s in filtered_data1_list:
    wav1.writeframes(st.pack('h', int(s*10)))
wav1.close()

#Write the filtered noise into the the project folder

wav = wave.open(file_1,'wb')
wav.setparams((nchannels, sampwidth, int(48000.0),nframes,comptype,compname))

for s in filtered_noise1_data:
    wav.writeframes(st.pack('h',int(s*1)))
wav.close()