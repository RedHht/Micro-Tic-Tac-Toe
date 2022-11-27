rojo = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ta-Te-Ti Jugador 1</title>
    <style>
        .boton {
            width: 100px;
            height: 100px;
            margin: 5px;
        }
        #caja {
            position: fixed; /* or absolute */
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
    </style>
</head>
<body>
    <div id="caja">
        <a><button id="boton1" class="boton"></button></a>
        <a><button id="boton2" class="boton"></button></a>
        <a><button id="boton3" class="boton"></button></a>
        <br>
        <a><button id="boton4" class="boton"></button></a>
        <a><button id="boton5" class="boton"></button></a>
        <a><button id="boton6" class="boton"></button></a>
        <br>
        <a><button id="boton7" class="boton"></button></a>
        <a><button id="boton8" class="boton"></button></a>
        <a><button id="boton9" class="boton"></button></a>
        <br>
        <span>Estas jugando como el jugador: <span style="color: red;">Rojo</span></span>
    </div>
        <script type="text/javascript">
        function getCurrentHost () {
          return window.location.host
        }

        function getCurrentURL () {
          return window.location.href
        }

        const button = document.getElementById('boton1');
        const url = getCurrentURL()
        const host = getCurrentHost()

        webSocket = new WebSocket("ws://192.168.1.41/socket");

        webSocket.onmessage = (event) => {
            console.log(event.data)
            switch (event.data) {
                case 'R1':
                    document.getElementById("boton1").style.backgroundColor = "red";
                    break;
                case 'V1':
                    document.getElementById("boton1").style.backgroundColor = "green";
                    break;
                case 'R2':
                    document.getElementById("boton2").style.backgroundColor = "red";
                    break;
                case 'V2':
                    document.getElementById("boton2").style.backgroundColor = "green";
                    break;
                case 'R3':
                    document.getElementById("boton3").style.backgroundColor = "red";
                    break;
                case 'V3':
                    document.getElementById("boton3").style.backgroundColor = "green";
                    break;
                case 'R4':
                    document.getElementById("boton4").style.backgroundColor = "red";
                    break;
                case 'V4':
                    document.getElementById("boton4").style.backgroundColor = "green";
                    break;
                case 'R5':
                    document.getElementById("boton5").style.backgroundColor = "red";
                    break;
                case 'V5':
                    document.getElementById("boton5").style.backgroundColor = "green";
                    break;
                case 'R6':
                    document.getElementById("boton6").style.backgroundColor = "red";
                    break;
                case 'V6':
                    document.getElementById("boton6").style.backgroundColor = "green";
                    break;
                case 'R7':
                    document.getElementById("boton7").style.backgroundColor = "red";
                    break;
                case 'V7':
                    document.getElementById("boton7").style.backgroundColor = "green";
                    break;
                case 'R8':
                    document.getElementById("boton8").style.backgroundColor = "red";
                    break;
                case 'V8':
                    document.getElementById("boton8").style.backgroundColor = "green";
                    break;
                case 'R9':
                    document.getElementById("boton9").style.backgroundColor = "red";
                    break;
                case 'V9':
                    document.getElementById("boton9").style.backgroundColor = "green";
                    break;
                default:
                    console.log(`El ws envio un mensaje desconocido.`);
                }

        }

        button.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=1", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });     
        const button2 = document.getElementById('boton2');

        button2.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=2", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button3 = document.getElementById('boton3');

        button3.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=3", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });
        const button4 = document.getElementById('boton4');

        button4.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=4", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });    
        const button5 = document.getElementById('boton5');

        button5.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=5", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button6 = document.getElementById('boton6');

        button6.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=6", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button7 = document.getElementById('boton7');

        button7.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=7", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button8 = document.getElementById('boton8');

        button8.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=8", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button9 = document.getElementById('boton9');

        button9.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=9", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
    </script>
</body>
</html>'''

verde = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ta-Te-Ti Jugador 2</title>
    <style>
        .boton {
            width: 100px;
            height: 100px;
            margin: 5px;
        }
        #caja {
            position: fixed; /* or absolute */
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
    </style>
</head>
<body>
    <div id="caja">
        <a><button id="boton1" class="boton"></button></a>
        <a><button id="boton2" class="boton"></button></a>
        <a><button id="boton3" class="boton"></button></a>
        <br>
        <a><button id="boton4" class="boton"></button></a>
        <a><button id="boton5" class="boton"></button></a>
        <a><button id="boton6" class="boton"></button></a>
        <br>
        <a><button id="boton7" class="boton"></button></a>
        <a><button id="boton8" class="boton"></button></a>
        <a><button id="boton9" class="boton"></button></a>
        <br>
        <span>Estas jugando como el jugador: <span style="color: green;">Verde</span></span>
    </div>
        <script type="text/javascript">
        function getCurrentHost () {
          return window.location.host
        }

        function getCurrentURL () {
          return window.location.href
        }

        const button = document.getElementById('boton1');
        const url = getCurrentURL()
        const host = getCurrentHost()

        webSocket = new WebSocket("ws://192.168.1.41/socket");

        webSocket.onmessage = (event) => {
            console.log(event.data)
            switch (event.data) {
                case 'R1':
                    document.getElementById("boton1").style.backgroundColor = "red";
                    break;
                case 'V1':
                    document.getElementById("boton1").style.backgroundColor = "green";
                    break;
                case 'R2':
                    document.getElementById("boton2").style.backgroundColor = "red";
                    break;
                case 'V2':
                    document.getElementById("boton2").style.backgroundColor = "green";
                    break;
                case 'R3':
                    document.getElementById("boton3").style.backgroundColor = "red";
                    break;
                case 'V3':
                    document.getElementById("boton3").style.backgroundColor = "green";
                    break;
                case 'R4':
                    document.getElementById("boton4").style.backgroundColor = "red";
                    break;
                case 'V4':
                    document.getElementById("boton4").style.backgroundColor = "green";
                    break;
                case 'R5':
                    document.getElementById("boton5").style.backgroundColor = "red";
                    break;
                case 'V5':
                    document.getElementById("boton5").style.backgroundColor = "green";
                    break;
                case 'R6':
                    document.getElementById("boton6").style.backgroundColor = "red";
                    break;
                case 'V6':
                    document.getElementById("boton6").style.backgroundColor = "green";
                    break;
                case 'R7':
                    document.getElementById("boton7").style.backgroundColor = "red";
                    break;
                case 'V7':
                    document.getElementById("boton7").style.backgroundColor = "green";
                    break;
                case 'R8':
                    document.getElementById("boton8").style.backgroundColor = "red";
                    break;
                case 'V8':
                    document.getElementById("boton8").style.backgroundColor = "green";
                    break;
                case 'R9':
                    document.getElementById("boton9").style.backgroundColor = "red";
                    break;
                case 'V9':
                    document.getElementById("boton9").style.backgroundColor = "green";
                    break;
                default:
                    console.log(`El ws envio un mensaje desconocido.`);
                }

        }

        button.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=1", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });     
        const button2 = document.getElementById('boton2');

        button2.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=2", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button3 = document.getElementById('boton3');

        button3.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=3", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });
        const button4 = document.getElementById('boton4');

        button4.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=4", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });    
        const button5 = document.getElementById('boton5');

        button5.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=5", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button6 = document.getElementById('boton6');

        button6.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=6", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button7 = document.getElementById('boton7');

        button7.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=7", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button8 = document.getElementById('boton8');

        button8.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=8", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
        const button9 = document.getElementById('boton9');

        button9.addEventListener('click', async _ => {
        try {     
            const response = await fetch(url + "mover?m=9", {
            method: 'post',
            body: {
                // Your body
            }
            });
            console.log('Completed!', response);
        } catch(err) {
            console.error(`Error: ${err}`);
        }
        });  
    </script>
</body>
</html>'''