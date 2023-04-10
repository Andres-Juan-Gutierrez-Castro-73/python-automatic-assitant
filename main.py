#IMPORTAMOS LAS CLASE QUE HEMOS CREADO CON LAS FUNCIONALIDADES
from clases.texto_a_voz import texto_a_voz
from clases.detector_rostros import detector_rostros
from clases.reconocimiento_voz import reconocimiento_voz
from clases.excell import excell
from clases.web_scraping import ProductSearcher
from clases.whatsapp import whatsapp

#CREAMOS LAS INTANCIAS DE LAS CLASES
obj_texto_a_voz = texto_a_voz()
obj_detector_rostros = detector_rostros()
obj_reconocimiento_voz = reconocimiento_voz()
obj_excell = excell()
obj_whatsapp = whatsapp()

#<===========INICIO DEL PROGRAMA==========>
#DAMOS LA BIENVENIDA AL USUARIO
obj_texto_a_voz.voz("Hola usuario, bienvenido al programa")

#CREAMOS UNA VARIABLE QUE VA A ALMACENAR EL NUMERO DE ROSTROS DETECTADOS
numero_caras = obj_detector_rostros.contador_cara()

#VALIDAMOS QUE EL NUMERO DE CARAS SEA MAYOR QUE CERO
if(numero_caras > 0):
    #SALUDAMOS DEPENDIENDO DE LA HORA DEL DIA
    obj_texto_a_voz.saludo()

    #CREAMOS UNA VARIABLE CON EL MENU DE OPCIONES
    opciones = ("este es el menu de opciones de la aplicacion:\n" +
                "1. abrir el archivo contactos de excell.\n" +
                "2. mandar mensaje a los contactos del archivo excell contactos.\n" +
                "3. buscar ofertas de tecnologia\n." +
                "4. salir de la aplicacion\n" +
                "Escoge alguna de las opciones")
    
    #LE DECIMOS LAS OPCIONES AL USUARIO
    obj_texto_a_voz.voz(opciones)

    #CREAMOS UNA VARIABLE PARA RECIBIR LA OPCION
    eleccion = obj_reconocimiento_voz.voz_a_texto()
        
    #CREAMOS UNA ESTRUCTURA DE CONTROL CON LAS OPCIONES
    if("opción 1" in eleccion):
        #MOSTRAMOS LAS OPCIONES QUE TIENE EL USUARIO
        obj_texto_a_voz.voz("Escogiste la opcion abrir archivo de excell.\n" +
                                "¿Qué quieres hacer ahora?: \n" +
                                "1. crear \n" +
                                "2. abrir \n" +
                                "3. llenar \n" +
                                "4. eliminar \n")
            
        #LLAMAMOS A LA VARIABLE ELECCION
        eleccion = obj_reconocimiento_voz.voz_a_texto()

        #DEPENDIENDO DE LA ELECCION TOMADA QUE EJECUTE LA ACCION
        if("crear" in eleccion):
            obj_texto_a_voz.voz("Creando archivo contactos.xlsx")
            obj_excell.crear_archivo()
        elif("abrir" in eleccion):
            obj_texto_a_voz.voz("Abriendo archivo contactos.xlsx")
            obj_excell.abrir_archivo()
        elif("llenar" in eleccion):
            obj_texto_a_voz.voz("Llena los datos ahora")
            obj_excell.llenar_archivo()
        elif("eliminar" in eleccion):
            obj_texto_a_voz.voz("Eliminado el archivo contactos.xlsx")
            obj_excell.eliminar_archivo()
        else:
            obj_texto_a_voz.voz("Error al reconocer la voz")

    elif("opción 2" in eleccion):
        obj_texto_a_voz.voz("Enviando mensaje a la lista de contactos de excell")
        obj_whatsapp.enviar_mensajes()
        
    elif("opción 3" in eleccion):
        obj_texto_a_voz.voz("Buscando ofertas de tecnologia")
        
        #DEFINIMOS UN ARREGLO QUE VA A TENER LOS SITIOS WEB QUE SE VAN A BUSCAR
        sitios = ['https://listado.mercadolibre.com.mx/', 'https://www.linio.com.co', 'https://www.alkomprar.com/']
        obj_scraping = ProductSearcher(sitios)
        obj_scraping.search_products('iphone')
        obj_scraping.close_browsers()

    elif("opción 4" in eleccion):
        obj_texto_a_voz.voz("Saliendo el programa, adios.")
    else:
        obj_texto_a_voz.voz("Hubo un error al reconocer tu voz, adios.")
else:
    #MENSAJE DE VOZ EXPLICANDO EL ERROR
    obj_texto_a_voz.voz("Ups, por algun motivo no se a reconocido tu rostro, intenta de nuevo") 