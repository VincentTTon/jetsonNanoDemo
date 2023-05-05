import serial 
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
arduino.reset_input_buffer()

while True:
    
    #Varibales DirectionL, DirectionR, gimbalPan, gimbalTilt, LauncherMRight, LauncherMLeft, hopper, ChannelSent
    #represented with a list inputsArduino
    inputsArduino = [1, 2, 3, 4, 5, 6, 7, 8] 
    
    #Converts int values to string
    strInputs = [str(input) for input in inputsArduino]

        
    #Sends each value from the strInputs list
    for j in strInputs:
        arduino.write(j.encode('utf-8'))
        
        #tests sending data from Jetson to Arduion
        print(strInputs)
        
        #Receives data from Arduino and prints in terminal
        receivedData = arduino.readline().decode().strip()
        print("\n\nI received from Arduino: ", receivedData, "\n\n")
        time.sleep(0.01)

