# Jetson Nano Demo

**Hardware:**
- Jetson Nano B01
- RPI Camera v2
- Arduino Uno
- OLED Display SSD1306
- AC to DC Power Supply 5V 4A (Barrel connector Plug 5.5mm x 2.1mm)

**Software:**
- Ubuntu 18.04
- Jet Pack 4.6 image (download link: https://developer.nvidia.com/embedded/l4t/r32_release_v6.1/jeston_nano/jetson-nano-jp46-sd-card-image.zip)
- How to install image on Jetson Nano? (Instructions: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)
- Python 3.6.9 (Jetson Nano Default Version)
- Libraries for inference:
  - jetson.inference (follow provided tutorials to learn more)
  - jetson_uttils (follow provided tutorials to learn more)
- Other libraries
  - serial (for serial communication with Arduino Uno)
  - time

**Tutorials:**
- How to Build the Hello AI Jetson Inference Project in Jetson https://youtu.be/RC_m7-cGw3o
- How to train SSD MOBILENET DRAGON for Custom Object Detection for #jetson #nano https://youtu.be/fZiY7zUk3TU
- Writing your own Python Detectnet Script for Jetson Inference | Nvidia Jetson https://youtu.be/1PbfaaZCo2Y


**Scripts:**
- python script is for jetson (appJetsonArduino.py)
- (ino) c script for Arduino UNO (test3.ino)
