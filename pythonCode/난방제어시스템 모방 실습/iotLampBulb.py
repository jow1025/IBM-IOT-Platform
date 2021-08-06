import wiotp.sdk
from utils import bulb
from gpiozero import RGBLED
led=RGBLED(red=17,green=27,blue=22)
led.off()
# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "vd6jub", "typeId": "vDev", "deviceId": "led"},
    "auth": {"token": "rla1rla1rla1"},
}

led_state = 'off'

def commandProcessor(cmd):
    global led_state
    if cmd.data["d"]["led_state"]:
        data = {}
        if cmd.data["d"]["led_state"] == "on":
            led_state = 'on'
            led.color=(1,0,0)
            bulb.bulbOn()
            data = {"d" : {"led_state" : "on"}}
        else:
            led_state = 'off'
            bulb.bulbOff()
            led.off()
            data = {"d" : {"led_state" : "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

def periodicPublish():
    data = {"d":{"led_state": led_state}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Lamp is " + led_state)
    bulb.after(3000, periodicPublish)

bulb.after(3000, periodicPublish)
bulb.mainloop()
