
import socket
import pyaudio
import wave
 
#record
CHUNK = 1024
FORMAT = pyaudio.paInt16 #8bit
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
 
HOST = ''    # The remote host
PORT = 50007              # The same port as used by the server
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
 
p = pyaudio.PyAudio()
 
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
 
#print("*recording")
 
 
 
for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
 data  = stream.read(CHUNK)
 
 s.sendall(data)
 
#print("*done recording")
 
stream.stop_stream()
stream.close()
p.terminate()
s.close()
 
