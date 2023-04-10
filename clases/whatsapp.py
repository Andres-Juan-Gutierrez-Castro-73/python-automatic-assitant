from selenium import webdriver
import time
import pandas as pd

class whatsapp:
    #METODO CONSTRUCTOR
    def __init__(self):
        #DEFINIMOS LAS PROPIEDADES
        self.driver = webdriver.Chrome("static/chromedriver.exe")
    
    #METODO PARA ENVIAR MENSAJES
    def enviar_mensajes(self):
        self.driver.get("https://web.whatsapp.com/")

        #ESPERAMOS A QUE EL USUARIO ESCANEE EL CODIGO QR Y PRESIONE ENTER
        input("Escanea el QR y presiona enter para continuar:   ")

        #LEEMOS LOS DATOS DEL ARCHIVO DE EXCELL
        data = pd.read_excel('static/contactos.xlsx')
        
        #ITERMAOS SOBRE LOS DATOS Y ENVIAMOS LOS MENSAJES
        for i, row in data.iterrows():
            numero = row['Telefono']
            mensaje = "Mañana no tendremos clase"
            url = f'https://web.whatsapp.com/send?phone={numero}&text={mensaje}'
            self.driver.get(url)
            time.sleep(5)
            boton_enviar = self.driver.find_element_by_xpath('//span[@data-testid="send"]')
            boton_enviar.click()

#w = whatsapp()
#w.enviar_mensajes()
