import jetson.inference
import jetson_utils
import serial 
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
arduino.reset_input_buffer()
cmd = 0

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("csi://0")
display = jetson.utils.videoOutput("display://0")

try:
    while display.IsStreaming():
        while True:
            img = camera.Capture()
            detections = net.Detect(img)
            display.Render(img)
            display.SetStatus("OUTPUT")
            
            var = detections
            print()
            
            with arduino as arduino:
                if arduino.isOpen():
                    if len(var) != 0:
                        arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
                        #arduino.write(b'1') #test
                        info = var[0]
                        if info.ClassID == 1: #1 person
                            x = info.Left
                            y = info.Top
                            center = info.Center
                            print(x)
                            #arduino.write(b'0')
                            
                            if x > 400:
                                cmd = "0"
                                arduino.write(b'0')
                            elif x >= 200 and x <= 400:
                                cmd = "1"
                                arduino.write(b'1')
                            elif x < 200:
                                cmd = "2"
                                arduino.write(b'2')
                            
                            #arduino.write(cmd.encode())  
                            
                            print("cmd is ", cmd)  
                            time.sleep(0.1)
                            #data =arduino.readline()
                            #print(data)   
                            
except KeyboardInterrupt:
    print("interupted")



