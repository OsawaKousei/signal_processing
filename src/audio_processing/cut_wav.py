import wave

import numpy as np
import scipy

wavf = r"C:\Users\kousei\Prox_dev\dev-shikoku\raw_data\normal.wav"
wr = wave.open(wavf, "r")

ch = wr.getnchannels()
width = wr.getsampwidth()
fr = wr.getframerate()
fn = wr.getnframes()

print("Channel: ", ch)
print("Sample width: ", width)
print("Frame Rate: ", fr)
print("Frame num: ", fn)
print("Params: ", wr.getparams())
print("Total time: ", 1.0 * fn / fr)

data = wr.readframes(wr.getnframes())
X = np.frombuffer(data, dtype="int16")

time = 600  # sec
frame = int(ch * fr * time)
start = 0
end = int((fn / fr) / time)

print("Frame: ", frame)
print("Start: ", start)
print("End: ", end)

for i in range(start, end):
    scipy.io.wavfile.write(
        "./normal_{0}.wav".format(i),
        fr,
        X[i * frame : (i + 1) * frame],
    )
