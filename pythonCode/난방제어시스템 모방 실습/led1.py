from gpiozero import RGBLED
import wiotp.sdk
from time import sleep

led=RGBLED(red=17,green=27,blue=22)
led.off()
# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "aua984", "typeId": "vDev", "deviceId": "led2"},
    "auth": {"token": "password"},
}

led_state = 'off'

def commandProcessor(cmd):
    global led_state
    if cmd.data["d"]["led_state"]:
        data = {}
        if cmd.data["d"]["led_state"] == "on":
            led_state = 'on'
            led.color=(1,0,0)
            print("Lamp is On")
            data = {"d" : {"led_state" : "on"}}
        else:
            led_state = 'off'
            led.off()
            print("Lamp is Off")
            data = {"d" : {"led_state" : "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)
        
deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

def periodicPublish():
    data = {"d":{"led_state": led_state}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Lamp is " + led_state)

while True:
    periodicPublish()
    sleep(10)
