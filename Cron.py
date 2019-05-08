import schedule
import time
import requests
import pymongo
import datetime

def job():
    print("I'm working...")
    '''
    user = pymongo.MongoClient(
    'mongodb+srv://mariof:mariof@nickcluster-vb9g8.mongodb.net/ClimaEstados?retryWrites=true')
    db = user.Estados
    collection = db.municipios
    '''
    
    urlEstados = 'http://localhost:3000/hola'
    response = requests.get(urlEstados)
    estados = [ 'Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Coahuila de Zaragoza', 'Colima', 'Chiapas', 'Chihuahua', 'Ciudad de México', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán de Ocampo','Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz de Ignacio de la Llave', 'Yucatán', 'Zacatecas' ]
    

    if response.status_code == 200:
        municipiosJson = response.json()
        for i in range(1):
            # Obtener los municipios de cada estado
            # Municipios de cada estado
            municipios = municipiosJson.get('estados[i]',[])
            
            for municipio in municipios:
                # Mando llamar la API del Clima con municipio que lo obtenemos del JSON de minicipios
                urlClima = 'https://api.apixu.com/v1/current.json?key=9cc0046b008947b5ba351438190201&q=' + municipio
                respuestaClima = requests.get(urlClima)
                # Si es 200 jala
                if respuestaClima.status_code == 200:
                    print('JALO')
                    # Convertir a JSON
                    climaJson = respuestaClima.json()
                    # Obtener cada uno de los elementos que queremos
                    current = climaJson.get('current',[])
                    # Todos los elementos del Current
                    temperatura_c = current.get('temp_c', []),
                    temperatura_f = current.get('temp_f', []),
                    # Accedemos cuando se convierte a vector
                    # nameState = municipios[i]
                    nameState = estados[i]
                    name = municipio
                    # Obtener datos de current.condition
                    condition = current.get('condition',[])
                    icon = condition.get('icon',[])
                    print(temperatura_c)
                    print(temperatura_f)
                    print(nameState)
                    print(name)
                    print(icon)
                    print('//******************************//')
                    api = climaJson.get('location',[])
                    print(api.get('name',[]))
                    print(api.get('country',[]))

                    
                    print('-----------------------------------------------------')
  

            print('-------------------------------------------')
  
    else:
        print('Nanchis')

                    
schedule.every().hour.do(job)

job()
while True:
    schedule.run_pending()
    time.sleep(1)
