import sys
from CalUI import *

class MyApp(QtWidgets.QMainWindow):
        def __init__(resistencia):
            super().__init__()
            resistencia.ui = Ui_MainWindow()
            resistencia.ui.setupUi(resistencia)

            resistencia.colorBandas = {
	    "Negro":0,
	    "Cafe":1,
	    "Rojo":2,
	    "Naranja":3,
	    "Amarillo":4,
	    "Verde":5,
	    "Azul":6,
	    "Violeta":7,
	    "Gris":8,
	    "Blanco":9
	    }

            resistencia.multiplicadorBanda = {
	    "Negro":1,
	    "Cafe":10,
	    "Rojo":100,
	    "Naranja":1000,
	    "Amarillo":10000,
	    "Verde":100000,
	    "Azul":1000000,
	    "Violeta":10000000,
	    "Gris":100000000,
	    "Blanco":1000000000
	    }

            resistencia.toleranciaBanda = {
            "":0,   
            "Negro":1,
	    "Rojo":2,
	    "Dorado":5,
	    "Plateado":10
	    }

            resistencia.valor1 = int(0)
            resistencia.valor2 = int(0)
            resistencia.valor3 = int(0)
            resistencia.valor4 = int(0)
            resistencia.Tolerancia = int(0)

            resistencia.ui.pushButton.clicked.connect(resistencia.obtener_Resultado)

            resistencia.ui.comboBox.addItems(resistencia.colorBandas.keys())
            resistencia.ui.comboBox.currentIndexChanged.connect(resistencia.seleccion1)
            resistencia.ui.comboBox.setCurrentText("Negro")

            resistencia.ui.comboBox_2.addItems(resistencia.colorBandas.keys())
            resistencia.ui.comboBox_2.currentIndexChanged.connect(resistencia.seleccion2)
            resistencia.ui.comboBox_2.setCurrentText("Negro")

            resistencia.ui.comboBox_3.addItems(resistencia.colorBandas.keys())
            resistencia.ui.comboBox_3.currentIndexChanged.connect(resistencia.seleccion3)
            resistencia.ui.comboBox_3.setCurrentText("Negro")

            resistencia.ui.comboBox_4.addItems(resistencia.toleranciaBanda.keys())
            resistencia.ui.comboBox_4.currentIndexChanged.connect(resistencia.seleccion4)
            resistencia.ui.comboBox_4.setCurrentText("Ninguno")

        def seleccion1(resistencia):
            valor1 = resistencia.ui.comboBox.currentText()

            if valor1=="Negro":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(0, 0, 0)")
                resistencia.valor1 = 0

            elif valor1 =="Cafe":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(128, 64, 0)")
                resistencia.valor1 = 1

            elif valor1 =="Rojo":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(255, 0, 0)")
                resistencia.valor1 = 2

            elif valor1 =="Naranja":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(255, 128, 0)")
                resistencia.valor1 = 3

            elif valor1 =="Amarillo":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(255, 255, 0)")
                resistencia.valor1 = 4

            elif valor1 =="Verde":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(0, 143, 57)")
                resistencia.valor1 = 5

            elif valor1 =="Azul":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(0, 71, 171)")
                resistencia.valor1 = 6

            elif valor1 =="Violeta":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(76, 40, 130)")
                resistencia.valor1 = 7

            elif valor1 =="Gris":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(155, 155, 155)")
                resistencia.valor1 = 8

            elif valor1 =="Blanco":
                resistencia.ui.label_8.setStyleSheet("background-color: rgb(255, 255, 255)")
                resistencia.valor1 = 9

        def seleccion2(resistencia):
            valor2 = resistencia.ui.comboBox_2.currentText()

            if valor2=="Negro":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(0, 0, 0)")
                resistencia.valor2 = 0

            elif valor2 =="Cafe":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(128, 64, 0)")
                resistencia.valor2 = 1

            elif valor2 =="Rojo":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(255, 0, 0)")
                resistencia.valor2 = 2

            elif valor2 =="Naranja":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(255, 128, 0)")
                resistencia.valor2 = 3

            elif valor2 =="Amarillo":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(255, 255, 0)")
                resistencia.valor2 = 4

            elif valor2 =="Verde":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(0, 143, 57)")
                resistencia.valor2 = 5

            elif valor2 =="Azul":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(0, 71, 171)")
                resistencia.valor2 = 6

            elif valor2 =="Violeta":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(76, 40, 130)")
                resistencia.valor2 = 7

            elif valor2 =="Gris":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(155, 155, 155)")
                resistencia.valor2 = 8

            elif valor2 =="Blanco":
                resistencia.ui.label_9.setStyleSheet("background-color: rgb(255, 255, 255)")
                resistencia.valor2 = 9

        def seleccion3(resistencia):
            valor3 = resistencia.ui.comboBox_3.currentText()

            if valor3=="Negro":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(0, 0, 0)")
                resistencia.valor3 = 1

            elif valor3 =="Cafe":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(128, 64, 0)")
                resistencia.valor3 = 10

            elif valor3 =="Rojo":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(255, 0, 0)")
                resistencia.valor3 = 100

            elif valor3 =="Naranja":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(255, 128, 0)")
                resistencia.valor3 = 1000

            elif valor3 =="Amarillo":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(255, 255, 0)")
                resistencia.valor3 = 10000

            elif valor3 =="Verde":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(0, 143, 57)")
                resistencia.valor3 = 100000

            elif valor3 =="Azul":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(0, 71, 171)")
                resistencia.valor3 = 1000000

            elif valor3 =="Violeta":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(76, 40, 130)")
                resistencia.valor3 = 10000000

            elif valor3 =="Gris":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(155, 155, 155)")
                resistencia.valor3 = 100000000

            elif valor3 =="Blanco":
                resistencia.ui.label_10.setStyleSheet("background-color: rgb(255, 255, 255)")
                resistencia.valor3 = 1000000000

        def seleccion4(resistencia):
            valor4 = resistencia.ui.comboBox_4.currentText()

            if valor4=="Negro":
                resistencia.ui.label_11.setStyleSheet("background-color: rgb(0, 0, 0)")
                resistencia.valor4 = 0.01
                resistencia.Tolerancia = "±1%"

            elif valor4=="Rojo":
                resistencia.ui.label_11.setStyleSheet("background-color: rgb(255, 0, 0)")
                resistencia.valor4 = 0.02
                resistencia.Tolerancia = "±2%"

            elif valor4 =="Dorado":
                resistencia.ui.label_11.setStyleSheet("background-color: rgb(239, 184, 16)")
                resistencia.valor4 = 0.05
                resistencia.Tolerancia = "±5%"

            elif valor4 =="Plateado":
                resistencia.ui.label_11.setStyleSheet("background-color: rgb(138, 149, 151)")
                resistencia.valor4 = 0.01
                resistencia.Tolerancia = "±10%"

        def obtener_Resultado(resistencia):
            ValorG = str((resistencia.valor1)) + str((resistencia.valor2))
            X = float(resistencia.valor3)
            Y = float(ValorG)

            ValorTT= float("{0:.3f}".format(X*Y))

            resistencia.ui.label_14.setText(str(ValorTT))
            resistencia.ui.label_16.setText(str(resistencia.Tolerancia))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inapp = MyApp()
    inapp.show()
    sys.exit(app.exec_())
