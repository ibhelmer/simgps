import serial
ser = serial.Serial('/dev/pts/4')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'Hej Ib')     # write a string
ser.close()             # close port
