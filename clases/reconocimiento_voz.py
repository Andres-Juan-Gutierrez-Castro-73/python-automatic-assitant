#IMPORTAMOS LA LIBRERIA SPEECH REGNITION
import speech_recognition as sr

#CREACION DE LA CLASE
class reconocimiento_voz:
    #METODO CONSTRUCTOR
    def __init__(self):
        #PROPIEDAD PARA RECONOCER LA VOZ
        self.reconocer = sr.Recognizer()
    
    #METODO PARA PASAR EL AUDIO A TEXTO
    def voz_a_texto(self):
        #UTILIZAMOS EL MICROFONO
        with sr.Microphone() as source:
            print("Di algo!")
            # Escucha para capturar el audio
            audio = self.reconocer.listen(source)
        
        #RETORNAMOS EL TEXTO Y VEMOS SI HAY ALGUN ERROR
        try:
            # Usa Google Speech Recognition para obtener el texto
            texto = self.reconocer.recognize_google(audio, language="es-ES")
            return texto
        except sr.UnknownValueError:
            print("Lo siento, no pude entender lo que dijiste")
        except sr.RequestError as e:
            print("Error al solicitar los resultados de Google Speech Recognition; {0}".format(e))