
"""
/**
 * @author  Behrad Pourhadi
 * @email   behradp32@gmail.com
 * @ide     Visual Studio Code
 * @brief   pyArduino (.py)
 * @explanation   Using the ardCd library, the pulse width of the PWM mode is changed on the Arduino Nano (Pin 9). 
*/
"""

from serial import Serial
import time

arduino = Serial(port= 'COM9' ,baudrate = 9600, timeout = 2)

time.sleep(2)

pwm = 0
base_cmd = "pwm .9 = "
base_cmd_num = 2
it = 0
dir = False

while(it < base_cmd_num):
    data = arduino.readline()
    print(data)
    it += 1

arduino.write(b'pwmfre .9 = 120')
data = arduino.readline()
print(data)
if(data != b'OK\r\n'):
    usercmd = input('terminate? yes(y) / no(any key): ')
    if usercmd == 'y':
        exit()

while(True):
    if(dir == False):
        pwm += 5
        if pwm > 100:
            pwm = 100
            dir = True
    else:
        pwm -= 5
        if pwm < 0:
            pwm = 0
            dir = False

    pwmstr = str(pwm)
    cmd = base_cmd + pwmstr
    arduino.write(bytes(cmd, 'UTF-8'))
    data = arduino.readline()
    if(data != b'OK\r\n'):
        print(data)
        usercmd = input('terminate? yes(y) / no(any key): ')
        if usercmd == 'y':
            exit()

    time.sleep(0.1)
