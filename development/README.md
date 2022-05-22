# Explicacion del proyecto trabajado y realizado

Se tuvieron las siguientes rutas para abordar el desarrollo del proyecto

# Requerimientos para desplegar toda la solucion
1. Para probar unicamente la solucion algoritmica -> PYTHON 3 o superior
2. Para desplegar el proyecto localmente debes tener instalado docker


    - levantar el proyecto -> docker-compose up
    - luego ir a http://localhost:8000/docs

    - ejecutar tests, para ejecutar el siguiente comando debe estar en el directorio del proyecto al mismo nivel del archivo docker-compose.yml
    - docker-compose run api_nba_service pytest tests

# Datos para programa simple

En el reposotorio enviado encontraras una carpeta 

# Datos para API

1. En la url que se consume en la api se debe tener en cuenta lo siguiente:
    a. Puedes probar los datos a traves de cualquier cliente por ejemplo POSTMAN
    b. Ingresar la siguiente url ->
    c. El tipo de metodo es POST
    d. El body es tipo (raw) y se debe enviar con formato tipo json ejemplo
        {
            "height_target": 154
        }
    e. El resultado se entregara en tipo json de los resultados encontrados

# Datos para test
