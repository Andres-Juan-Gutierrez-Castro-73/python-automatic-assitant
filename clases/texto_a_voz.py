#IMPORTAAMOS LAS BIBLIOTECTAS NECESARIAS
import pyttsx3
import datetime

#CLASE QUE SE VA A INSTANCIAR EN EL ARCHIVO MAIN
class texto_a_voz:
    
    #METODO CONSTRUCTOR
    def __init__(self):
        #PROPIEDADES QUE VAMOS A MANIPULAR
        self.velocidad = 150
        self.volumen = 1
    
    #FUNCION QUE PASA EL TEXTO A VOZ
    def voz(self, texto):
        #OBJETO QUE ACCESDE A LOS METODOS DE LA LIBRERIA
        objeto = pyttsx3.init()

        #ESPECIFICACION DE LA VELOCIDAD Y EL VOLUMEN
        objeto.setProperty('rate', self.velocidad)
        objeto.setProperty('volume', self.volumen)

        #CONVERSION DEL TEXTO A VOZ
        objeto.say(texto)

        #REPRODUCCION DEL AUDIO
        objeto.runAndWait()
    
    #FUNCION QUE SALUDA DEPENDIENDO DE LA HORA DEL DIA
    def saludo(self):
        #VARIABLE QUE VA A GUARDAR LA HORA ACTUAL DEL DISPOSITIVO
        hora_actual = datetime.datetime.now().hour
        
        #CREAMOS LA FUNCION MENSAJE
        mensaje = ""

        #CON LA ESTRUCTURA DE CONSTROL IF EVALUAMOS UN RANOG DE HORA
        if (hora_actual >= 6 and hora_actual < 12):
            mensaje = "Buenos dias, espero que estes bien"
            self.voz(mensaje)
        elif (hora_actual >= 12 and hora_actual < 18):
            mensaje = "Buenas tardes, ¿cómo estas?"
            self.voz(mensaje)
        else:
            mensaje = "Buenas noches, espero que tu dia haya ido bien"
            self.voz(mensaje)