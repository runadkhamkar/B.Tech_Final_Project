from scipy.io import wavfile
import matplotlib.pyplot as plt
a,b=wavfile.read("G:\\platform-tools\\f2.wav")
b=list(b)
b=[i[0] for i in b]
plt.plot(b)
plt.show()