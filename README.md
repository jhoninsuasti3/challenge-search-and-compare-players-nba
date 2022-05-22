# Explicacion del proyecto trabajado y realizado

Se tuvieron las siguientes rutas para abordar el desarrollo del proyecto
* Analisis del requerimiento y su complejidad
* Encontrar las diferencias entre complejidades algortimicas
* Consumir los recursos y aplicar una soluciion optima
* Entregar el resultado en dos alternativas, una solucion sencilla y otra con una propuesta adicional al reto:
    {
        "alternativa1 " : "La ejecucion sencilla de la solicitud con un solo archivo python, utilizando la libreria request y json, en donde se ingresa un valor por consola y se entrega el resultado esperado",

        "alternativa2 " : "Se propone entregar los datos en un API, para la comodidad de visualizacion de los datos, se utilizan recursos como fastapi import, routes, JSONResponse uvicorn",       

        "ambas": " Se utiliza la libreria de test"
    }

# Datos y requerimientos para solucion algoritmica sin API

En el reposotorio enviado encontraras una carpeta 


# Requerimientos para desplegar toda la solucion localmente con API
1. Para probar unicamente la solucion algoritmica -> PYTHON 3 o superior
2. Para desplegar el proyecto localmente debes tener instalado docker


    - Levantar el proyecto -> docker-compose up
    - Luego ir a http://localhost:8000/docs
    - Ejecutar tests, para ejecutar el siguiente comando debe estar en el directorio del proyecto al mismo nivel del archivo docker-compose.yml
    - docker-compose run api_nba_service pytest tests


# Datos para API

Importante se realiza una api con el recurso de fast api con el objetivo de brindar facilidad a la verificacion de la informacion seteada, tener en cuenta los comentarios y las recomendaciones y apuntes que se entregara en esta documentacion.

La api fue desplegada en heroku, Y ESTA DISPONIBLE PARA QUE SE PUEDA CONSUMIR DESDE CUALQUIER LUGAR

1. En la url que se consume en la api se debe tener en cuenta lo siguiente: https://nba-api-challenge.herokuapp.com/api/v1/find_heights_nba/
    a. Puedes probar los datos a traves de cualquier cliente por ejemplo POSTMAN
    b. Ingresar la siguiente url ->
    c. El tipo de metodo es POST
    d. El body es tipo (raw) y se debe enviar con formato tipo json ejemplo
        {
            "height_target": 154
        }
    e. El resultado se entregara en tipo json de los resultados encontrados

# Datos para test

En el directorio test se encuentra un archivo .py se crean test para validar Y/O REALIZAR los test de lo datos que se deben buscar y los que el usuario digitaria.
Se crearon dos funciones adicionales para la validacion de estado del recurso por consumo de API