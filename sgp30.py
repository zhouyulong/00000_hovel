# _*_ coding: utf-8 _*_
# @Time     : 2022/8/29 09:12
# @Author   : Raina Loong
# @File     : sgp30.py


import time
import board
import busio
import adafruit_sgp30


class SGP30_Raina():
    # celsius单位为摄氏度, relative_humidity相对湿度
    def __init__(self,celsius, relatie_humidity):
        i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        # Create library object on our I2C port
        sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

        print("SGP30 serial #", [hex(i) for i in sgp30.serial])

        sgp30.set_iaq_baseline(0x8973, 0x8AAE)
        sgp30.set_iaq_relative_humidity(celsius=celsius, relative_humidity=relatie_humidity)
        self.baseline_eCO2 = sgp30.baseline_eCO2
        self.baseline_TVOC = sgp30.baseline_TVOC
        # sgp30.eCO2 单位 ppm
        # sgp30.TVOC 单位 ppb
        self.eCO2 = sgp30.eCO2
        self.TVOC = sgp30.TVOC
        self.sgp30 = sgp30

    def get_eCO2_TVOC(self) -> tuple:
        # 单位变换公式: 1 ppb == 4.5 μg/m³
        self.eCO2 = self.sgp30.eCO2
        self.TVOC = self.sgp30.TVOC
        return self.eCO2, float(self.TVOC)


sgp30_raina = SGP30_Raina()
while True:
    print(sgp30_raina.get_eCO2_TVOC())
    time.sleep(2)


# elapsed_sec = 0

# while True:
#     # print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC*4.5))
#     print(f'eCO2 = {sgp30.eCO2:.4f} ppm \t TVOC = {sgp30.TVOC*4.5/1000:.4f} mg/m³')
#     time.sleep(1)
#     elapsed_sec += 1
#     if elapsed_sec > 10:
#         elapsed_sec = 0
#         print(
#             "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
#             % (sgp30.baseline_eCO2, sgp30.baseline_TVOC)
#         )