from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy.signal import butter
from scipy.signal import lfilter
import numpy as np

def getWav(path):
	rate, native_data = read(path)
	data = native_data / ((2**16)/2)
	return rate, data
	
def saveWav(name, rate, data):
	name = name + '.wav'
	write(name, rate, data)
	return
	
def Equalizer(flow, fhigh, source, title):
	rate, data = getWav(source)
	data = np.float32(data)
	nyq = rate / 2
	if(flow > 0):
		b, a = butter(1, flow/nyq, 'lowpass')
		filteredlow = lfilter(b, a, data)
	else:
		filteredlow = 0
	if(fhigh > 0):
		b, a = butter(1, fhigh/nyq, 'highpass')
		filteredhigh = lfilter(b, a, data)
	else:
		filteredhigh = 0
	filteredsound = filteredlow + filteredhigh
	filteredsound = np.float32(filteredsound)
	saveWav(title, rate, filteredsound)
	return
	
if __name__ == "__main__":
	print('Equalizer script')