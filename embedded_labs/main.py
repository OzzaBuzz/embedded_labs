from gpiozero import LED, LightSensor, Button, Buzzer
from signal import pause
from time import sleep
import time

led3 = LED(26)
led2 = LED(19)
led1 = LED(13)
led4 = LED(6)
ldr = LightSensor(21)
button = Button(20)

global current_state = "ready"

def ledAllOn():
   # while True:
        led1.on()
        led2.on()
        led3.on()
        led4.on()

def ledLDR():
   # while True:
        led1.on()
        led2.off()
        led3.off()
        led4.on()


def ledSequence():
   # while True:
        led1.on()
        sleep(0.1)
        led1.off()
        sleep(0.1)
        led2.on()
        sleep(0.1)
        led2.off()
        sleep(0.1)
        led3.on()
        sleep(0.1)
        led3.off()
        sleep(0.1)
        led4.on()
        sleep(0.1)
        led4.off()
        sleep(0.1)

def ldr_sense():
    if ldr.light_detected:
        ledAllOn()
    else:
        ledLDR()
    
def button_check():
    button.hold_time = 2;
    if button.is_held:
        current_state = "surveillence"

def surveillence_check():
    ledSequence()
    #print("Press Button for 2 secs to enter Surveillence Mode")
    
def state_ready():
    ldr_sense()
    button_check()

def state_surveillence():
    ledSequence()

if __name__ == "__main__":
    while True:
        if(current_state == "ready"):
            state_ready()
        elif(current_state == "surveillence"):
            state_surveillence()