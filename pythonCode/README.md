python 코드 해설

1. iotlaptop.py : laptop이나 PC에 설치하여 cpu/memory 사용량을 IBM IOT Platform에 주기적으로 보고 하는 샘플 프로그램
2. iotSwitch.py : {"d": {"switch": "on | off"}} 의 이벤트를 IBM IOT Platform에 전송하는 텍스트 기반의 샘플 프로그램
3. iotLamp.py : IBM IOT Platform에 연결하여 platform으로 부터, {"d": {"lamp": "on | off"}} 명령을 받아 lamp 상태를 조작하여 텍스트로 표시하는 샘플 프로그램
4. iotSwitchButton.py : 텍스트 기반인 iotSwitch의 GUI 버전으 샘플 프로그램
5. iotLamp.Bulb.py : 텍스트 기반인 iotLamp의 GUI 버전의 샘플 프로그램
6. iotLampPi.py : iotLamp를 Raspberry Pi에서 돌리는 샘플 프로그램. GPIO 15번에 릴레이를 설치하여 실습
7. iotLampMananged.py : IBM IOT Platform에서 제공하는 IOT Device의 원격 재시동등 관리 기능을 보여주는 샘플.


testButton.py 는 utils 및에 있는 buttonSwitch.py를 사용하는 프로그램의 예시를 보인다.
