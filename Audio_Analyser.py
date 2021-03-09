import pyaudio
import matplotlib.pyplot as plt
import numpy as np

CHUNK = 1024*4  # Number of data points per sample
Format = pyaudio.paInt16  # 16 bit audio
channel = 1  # mono
sampling_rate = 44100

# create an object from the pyaudio class
p = pyaudio.PyAudio()

stream = p.open(
    format=Format, channels=channel,
    rate=sampling_rate, input=True,
    frames_per_buffer=CHUNK
)

# Generate the plot
fig, ax = plt.subplots(figsize=(14, 6))
x = np.arange(0, 2 * CHUNK, 2)
ax.set_ylim(-500, 500)
ax.set_ylabel("Volume")
ax.set_xlim(0, CHUNK)
ax.set_xlabel("Samples")
line, = ax.plot(x, np.random.rand(CHUNK))

while True:
    data = stream.read(CHUNK)
    data_arr = np.frombuffer(data, np.int16)
    line.set_ydata(data_arr)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.001)


