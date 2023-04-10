#IMPORTAMOS AL LIBRERIA DE OPENCV
import cv2

#CLASE DE DETECTOR ROSTROS
class detector_rostros:
    #METODO CONSTRUCTOR
    def __init__(self):
        #DEFINICION DE LAS PROPIEDADES
        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    #METODO DE CONTADOR CARAS
    def contador_cara(self):
        #DEFINIMOS LA VARIABLE QUE VA SER EL CONTADOR DE CARAS
        num_faces = 0

        #CICLO PARA ENCENDER LA CAMARA Y MANTENERLA ENCENDIDA
        while True:
            #CAPTURAMOS EL FRAME DEL VIDEO
            ret, frame = self.cap.read()

            #DETECTAMOS LAS CARAS EN EL FRAME
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            #DIBUJAMOS UN RECTANGULO EN LAS CARAS QUE DETECTAMOS
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                num_faces += 1
            
            #MOSTRAMOS EL FRAME CON LAS CARAS DETECTADAS Y LOS RECTANGULOS
            cv2.imshow('frame', frame)

            #DETENEMOS EL CICLO CON LA TECLA Q
            if cv2.waitKey(1) == ord('q'):
                break
        
        #APAGAMOS LA CAMARA Y DESTRUIMOS LAS VENTANAS
        self.cap.release()
        cv2.destroyAllWindows()

        #IPRIMIMOS EL NUMERO DE CARAS DETECTADO
        return num_faces