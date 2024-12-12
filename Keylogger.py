import time  # Import time for sleep functionality
import ctypes  # Para usar funciones de la API de Windows

# Función para obtener una tecla simulada
def main():
    # Cargar la biblioteca de Windows para detectar el estado del teclado
    user32 = ctypes.windll.user32
    # Diccionario de las teclas
    asciiTable = {
        "0": "[NUL]", "1": "[LCLICK]", "2": "[RCLICK]", "3": "[ETX]", "4": "[SCROLLCLICK]",
        "5": "[ENQ]", "6": "[ACK]", "7": "[BEL]", "8": "[BACKSPACE]", "9": "[TAB]",
        "10": "[LF]", "11": "[VT]", "12": "[CLEAR]", "13": "[ENTER]", "14": "[SO]", "15": "[SI]",
        "16": "", "17": "[RALT]", "18": "[LALT]", "19": "[PAUSEBREAK]", "20": "[CAPSLOCK]",
        "21": "[NAK]", "22": "[SYN]", "23": "[ETB]", "24": "[CAN]", "25": "[EM]",
        "26": "[SUB]", "27": "[ESC]", "28": "[FS]", "29": "[GS]", "30": "[RS]",
        "31": "[US]", "32": "[SPACE]", "33": "[PAGEUP]", "34": "[PAGEDOWN]", "35": "[END]",
        "36": "[HOME]", "37": "[LEFT]", "38": "[UP]", "39": "[RIGHT]", "40": "[DOWN]",
        "41": ")", "42": "*", "43": "+", "44": "[PRTSC]", "45": "[INSERT]",
        "46": "[DELETE]", "47": "/", "48": "0", "49": "1", "50": "2",
        "51": "3", "52": "4", "53": "5", "54": "6", "55": "7",
        "56": "8", "57": "9", "58": ":", "59": ";", "60": "<",
        "61": "=", "62": ">", "63": "?", "64": "@", "65": "A",
        "66": "B", "67": "C", "68": "D", "69": "E", "70": "F",
        "71": "G", "72": "H", "73": "I", "74": "J", "75": "K",
        "76": "L", "77": "M", "78": "N", "79": "O", "80": "P",
        "81": "Q", "82": "R", "83": "S", "84": "T", "85": "U",
        "86": "V", "87": "W", "88": "X", "89": "Y", "90": "Z",
        "91": "[WIN]", "92": "\\", "93": "]", "94": "^", "95": "_",
        "96": "0", "97": "1", "98": "2", "99": "3", "100": "4",
        "101": "5", "102": "6", "103": "7", "104": "8", "105": "9",
        "106": "*", "107": "+", "108": "l", "109": "-", "110": ".",
        "111": "/", "112": "[F1]", "113": "[F2]", "114": "[F3]", "115": "[F4]",
        "116": "[F5]", "117": "[F6]", "118": "[F7]", "119": "[F8]", "120": "[F9]",
        "121": "[F10]", "122": "[F11]", "123": "[F12]", "124": "|", "125": "}",
        "126": "~", "145": "[SCROOLLOCK]", "144": "[NUMLOCK]", "160": "[LSHIFT]", "161": "[RSHIFT]",
        "162": "[LCTRL]", "163": "[RCTRL]", "190": ".", "191": "/", "188": ",",
        "186": ";", "189": "-", "187": "=", "165": "", "164": "",
        "192": "`", "222": "'", "220": "\\", "219": "[", "221": "]"
    }

    # Diccionario para almacenar el estado de cada tecla (presionada o no)
    keyStates = {}

    while True:
        # Iterar sobre posibles códigos de tecla (0-255)
        for i in range(256):
            # Verificar si la tecla está presionada usando GetAsyncKeyState
            if user32.GetAsyncKeyState(i) & 0x8000:
                # Si la tecla no estaba presionada antes
                if not keyStates.get(i, False):
                    keyStates[i] = True  # Marcarla como presionada
                    key = asciiTable.get(str(i), f"[UNKNOWN {i}]")  # Obtener el nombre legible
                    print(f"Tecla presionada: {key}")  # Imprimir la tecla en lugar de enviarla

            else:
                # Marcar la tecla como no presionada
                keyStates[i] = False

        # Pausa para reducir el uso de CPU
        time.sleep(0.1)

# Ejecutar la función principal
main()
#COmentario de prueba
