__author__ = "Sigfrido Soria"
__date__ = "14-mar-2023 21:10:00"

import platform
import threading
import serial

# Raspberry PI 5
import gpiod

sistema = platform.system()
plataforma = platform.uname()

if sistema == "Windows":
    print('Estamos en Windows')
elif sistema == 'Linux':
    print('Estamos en Linux')
    if plataforma.node == "raspberrypi":
        print('Es una raspberry')

        # Raspberry PI 4
        import RPi.GPIO as GPIO






class Controladora:
    def __init__(self):

        print('Iniciando la controladora')

        self.DI_00 = None
        self.DI_01 = None
        self.DI_02 = None
        self.DI_03 = None
        self.DI_04 = None
        self.DI_05 = None
        self.DI_06 = None
        self.DI_07 = None

        self.DO_00 = None
        self.DO_01 = None
        self.DO_02 = None
        self.DO_03 = None
        self.DO_04 = None
        self.DO_05 = None
        self.DO_06 = None
        self.DO_07 = None

        self.DO_08 = None
        self.DO_09 = None
        self.DO_10 = None
        self.DO_11 = None
        self.DO_12 = None
        self.DO_13 = None
        self.DO_14 = None
        self.DO_15 = None

        # Entradas Digitales
        self.X_00 = False
        self.X_01 = False
        self.X_02 = False
        self.X_03 = False
        self.X_04 = False
        self.X_05 = False
        self.X_06 = False
        self.X_07 = False

        # Salidas digitales
        self.Y_00 = False
        self.Y_01 = False
        self.Y_02 = False
        self.Y_03 = False

        self.Y_04 = False
        self.Y_05 = False
        self.Y_06 = False
        self.Y_07 = False

        self.Y_08 = False
        self.Y_09 = False
        self.Y_10 = False
        self.Y_11 = False

        self.Y_12 = False
        self.Y_13 = False
        self.Y_14 = False
        self.Y_15 = False

        self.instruccionLeida = ""
        self.instruccionEscrita = ""

        self.estado = False

        if plataforma.node == "raspberrypi":
            self.configurarSenales()

            tarea1 = threading.Thread(target=self.run)
            tarea1.start()

    def activarPin(self, direccion, valor):
        if plataforma.node == "raspberrypi":

            if direccion == 0:
                self.Y_00 = valor

            if direccion == 1:
                self.Y_01 = valor

            if direccion == 2:
                self.Y_02 = valor

            if direccion == 3:
                self.Y_03 = valor

    def configurarSenales(self):


        # --------------  Entradas
        # Botones

        DI_00 = 18
        DI_01 = 23
        DI_02 = 24
        DI_03 = 25

        # Sensores

        DI_04 = 8
        DI_05 = 7
        DI_06 = 1
        DI_07 = 12

        # --------------  Salidas
        # Lamparas
        DO_00 = 4      
        DO_01 = 17
        DO_02 = 27
        DO_03 = 22
        DO_04 = 10

        # Motor de Corriente directa
        DO_05 = 9
        DO_06 = 11

        # Motor de CD con PWM
        DO_07 = 0
        DO_08 = 5

        # Motor a pasos
        DO_09 = 6
        DO_10 = 13
        DO_11 = 19
        DO_12 = 26

        # Motor Trifasico
        DO_13 = 16
        DO_14 = 20
        DO_15 = 21



        chip = gpiod.Chip('gpiochip4')

        
        self.DI_00 = chip.get_line(DI_00)
        self.DI_01 = chip.get_line(DI_01)
        self.DI_02 = chip.get_line(DI_02)
        self.DI_03 = chip.get_line(DI_03)


        self.DO_00 = chip.get_line(DO_00)
        self.DO_01 = chip.get_line(DO_01)
        self.DO_02 = chip.get_line(DO_02)
        self.DO_03 = chip.get_line(DO_03)


        self.DI_00.request(consumer="DI_00", type=gpiod.LINE_REQ_DIR_IN)
        self.DI_01.request(consumer="DI_01", type=gpiod.LINE_REQ_DIR_IN)
        self.DI_02.request(consumer="DI_02", type=gpiod.LINE_REQ_DIR_IN)
        self.DI_03.request(consumer="DI_03", type=gpiod.LINE_REQ_DIR_IN)


        self.DO_00.request(consumer="DO_00", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_01.request(consumer="DO_01", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_02.request(consumer="DO_02", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_03.request(consumer="DO_03", type=gpiod.LINE_REQ_DIR_OUT)

        # self.DI_00.release()
        # self.DO_00.release()


        # GPIO.setmode(GPIO.BCM)
        # GPIO.setwarnings(False)


        # # Entradas
        # GPIO.setup(self.DI_00, GPIO.IN)
        # GPIO.setup(self.DI_01, GPIO.IN)
        # GPIO.setup(self.DI_02, GPIO.IN)
        # GPIO.setup(self.DI_03, GPIO.IN)

        # GPIO.setup(self.DI_04, GPIO.IN)
        # GPIO.setup(self.DI_05, GPIO.IN)
        # GPIO.setup(self.DI_06, GPIO.IN)
        # GPIO.setup(self.DI_07, GPIO.IN)

        # # Salidas
        # GPIO.setup(self.DO_00, GPIO.OUT)
        # GPIO.setup(self.DO_01, GPIO.OUT)
        # GPIO.setup(self.DO_02, GPIO.OUT)
        # GPIO.setup(self.DO_03, GPIO.OUT)

        # GPIO.setup(self.DO_04, GPIO.OUT)
        # GPIO.setup(self.DO_05, GPIO.OUT)
        # GPIO.setup(self.DO_06, GPIO.OUT)
        # GPIO.setup(self.DO_07, GPIO.OUT)

        # GPIO.setup(self.DO_08, GPIO.OUT)
        # GPIO.setup(self.DO_09, GPIO.OUT)
        # GPIO.setup(self.DO_10, GPIO.OUT)
        # GPIO.setup(self.DO_11, GPIO.OUT)

        # GPIO.setup(self.DO_12, GPIO.OUT)
        # GPIO.setup(self.DO_13, GPIO.OUT)
        # GPIO.setup(self.DO_14, GPIO.OUT)
        # GPIO.setup(self.DO_15, GPIO.IN)

        # configurar puerto serie

    def run(self):
        self.estado = True
        while self.estado:
            self.leerYEscribirPines()
            # recibirDatos()

    def leerYEscribirPines(self):


        # Entradas digitales
           
        self.X_00 = self.DI_00.get_value()
        self.X_01 = self.DI_01.get_value()
        self.X_02 = self.DI_02.get_value()
        self.X_03 = self.DI_03.get_value()
       

        # self.X_00 = GPIO.input(self.DI_00)
        # self.X_01 = GPIO.input(self.DI_01)
        # self.X_02 = GPIO.input(self.DI_02)
        # self.X_03 = GPIO.input(self.DI_03)
        # self.X_04 = GPIO.input(self.DI_04)
        # self.X_05 = GPIO.input(self.DI_05)
        # self.X_06 = GPIO.input(self.DI_06)
        # self.X_07 = GPIO.input(self.DI_07)

        # Salidas digitales
       
        self.DO_00.set_value(self.Y_00)
        self.DO_01.set_value(self.Y_01)
        self.DO_02.set_value(self.Y_02)
        self.DO_03.set_value(self.Y_03)


        # GPIO.output(self.DO_00, self.Y_00)
        # GPIO.output(self.DO_01, self.Y_01)
        # GPIO.output(self.DO_02, self.Y_02)
        # GPIO.output(self.DO_03, self.Y_03)
        # GPIO.output(self.DO_04, self.Y_04)
        # GPIO.output(self.DO_05, self.Y_05)
        # GPIO.output(self.DO_06, self.Y_06)
        # GPIO.output(self.DO_07, self.Y_07)

        # GPIO.output(self.DO_08, self.Y_08)
        # GPIO.output(self.DO_09, self.Y_09)
        # GPIO.output(self.DO_10, self.Y_10)
        # GPIO.output(self.DO_11, self.Y_11)
        # GPIO.output(self.DO_12, self.Y_12)
        # GPIO.output(self.DO_13, self.Y_13)
        # GPIO.output(self.DO_14, self.Y_14)
        # GPIO.output(self.DO_15, self.Y_15)
        #
        # GPIO.output(self.DO_16, self.Y_16)
        # GPIO.output(self.DO_17, self.Y_17)
        # GPIO.output(self.DO_18, self.Y_18)
        # GPIO.output(self.DO_19, self.Y_19)
        # GPIO.output(self.DO_20, self.Y_20)
        # GPIO.output(self.DO_21, self.Y_21)
        # GPIO.output(self.DO_22, self.Y_22)
        # GPIO.output(self.DO_23, self.Y_23)

    def recibirDatos(self):
        # self.instruccionLeida = serial.read(50)
        pass

    def transmitirDatos(self, instruccion):
        serial.write(50)


def main():
    controladora = Controladora()


if __name__ == "__main__":
    main()
