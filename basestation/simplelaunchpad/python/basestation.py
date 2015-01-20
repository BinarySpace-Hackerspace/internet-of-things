import dweepy
import serial

ser = serial.Serial("COM167", 9600)

while True:
    message = ser.readline()
    dweepy.dweet_for('binaryspace-iot', {'Temperature': message[6:] })
