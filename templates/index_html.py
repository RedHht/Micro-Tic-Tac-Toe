# Autogenerated file
def render(TEAM):
    yield """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Ta-Te-Ti Jugador 1</title>
    <style>
        .boton """
    yield """{
            width: 100px;
            height: 100px;
            margin: 5px;
        }
        #caja """
    yield """{
            position: fixed; /* or absolute */
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
    </style>
</head>
<body>
<div id=\"caja\">
    <a><button id=\"boton0\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <a><button id=\"boton1\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <a><button id=\"boton2\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <br>
    <a><button id=\"boton3\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <a><button id=\"boton4\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <a><button id=\"boton5\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <br>
    <a><button id=\"boton6\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <a><button id=\"boton7\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <a><button id=\"boton8\" class=\"boton\" style=\"background-color: white;\"></button></a>
    <br>
    """
    if TEAM == "R":
        yield """    <span>Estas jugando como el jugador: <span style=\"color: red;\">Rojo</span></span>
    """
    elif TEAM == "G":
        yield """    <span>Estas jugando como el jugador: <span style=\"color: green;\">Verde</span></span>
    """
    yield """</div>
<script type=\"text/javascript\">
    function getCurrentHost () """
    yield """{
        return window.location.host
    }

    function getCurrentURL () """
    yield """{
        return window.location.href
    }
    
    const url = getCurrentURL()
    const host = getCurrentHost()
    
        // Crear una instancia de WebSocket
    var ws = new WebSocket(\"ws://\" + host + \"/ws\");

    // Definir una función para manejar los mensajes entrantes
    ws.onmessage = function(event) """
    yield """{
      // Obtener el mensaje como un objeto JSON
      var data = JSON.parse(event.data);
      
      console.log(event.data)

      // Verificar el tipo de mensaje y realizar la acción correspondiente
      switch (data.type) """
    yield """{
        case \"color\":
          // Cambiar el color de fondo de un elemento con el color enviado
          document.getElementById(data.id).style.backgroundColor = data.value;
          break;
        case \"alert\":
          // Mostrar una alerta con el mensaje enviado
          alert(data.message);
          break;
        default:
          // Ignorar los mensajes de otros tipos
          console.log(\"Mensaje desconocido: \" + data.type);
      }
    };


    """
    for i in range(9):
        yield """    
    
    const button"""
        yield str(i)
        yield """ = document.getElementById('boton"""
        yield str(i)
        yield """');

    button"""
        yield str(i)
        yield """.addEventListener('click', async _ => """
        yield """{
        try """
        yield """{
            const response = await fetch(\"http://\" + host + \"/move?m="""
        yield str(TEAM)
        yield str(i)
        yield """\", """
        yield """{
                method: 'post',
                body: """
        yield """{
                    // Your body
                }
            });
            console.log('Completed!', response);
        } catch(err) """
        yield """{
            console.error(`Error: $"""
        yield """{err}`);
        }
    });
    
    """
    yield """    
</script>
</body>
</html>"""
