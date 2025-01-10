import logging

def registro_errores(mensaje):
    logging.basicConfig(
        filename="errors.log",
        level=logging.ERROR,
        format="%(asctime)s - %(message)s"
    )
    
    logging.error(mensaje)

def get_key(codigo_tecla, mayuscula=False, alt_gr=False):
    
    teclas_especiales = {
        0x01: "BOTON IZQUIERDO DEL RATON",
        0x02: "BOTON DERECHO DEL RATON",
        0x08: "RETROCESO",
        0x09: "TABULADOR",
        0x0D: "ENTER",
        0x1B: "ESC",
        0x20: "ESPACIO",
        0x2C: "IMPRIMIR PANTALLA",
        0x2E: "SUPRIMIR",
        0x25: "FLECHA IZQUIERDA",
        0x27: "FLECHA DERECHA",
        0x26: "FLECHA ARRIBA",
        0x28: "FLECHA ABAJO",
        0x70: "F1",
        0x71: "F2",
        0x72: "F3",
        0x73: "F4",
        0x74: "F5",
        0x75: "F6",
        0x76: "F7",
        0x77: "F8",
        0x78: "F9",
        0x79: "F10",
        0x7A: "F11",
        0x7B: "F12",
        0xBA: "Ñ",  
        0xDB: "¿",  
        0xDD: "CORCHETE DERECHO",
        0xDC: "BARRA INVERTIDA",
        0xDE: "COMILLA SIMPLE",
        0xBF: "Ç",  
        0xA1: "¡",  
        0xBC: ",",   
        0xBE: ".",   
        0xBD: "-",
        0xBB: "+",    
    }

    
    combinaciones_alt_gr = {
        0x32: "@",  
        0x33: "#",  
        0x34: "~",  
        0x35: "€",  
        0x6C: "|",  
    }

    combinaciones_shift = {
        0xBC: ";",  
        0xBE: ":",  
        0xBD: "_",  
        0x30: "=",  
        0x31: "!",  
        0x32: '"',   
        0x33: "#",   
        0x34: "$",   
        0x35: "%",   
        0x36: "&",   
        0x37: "/",   
        0x38: "(",   
        0x39: ")",   
    }

    if alt_gr:
        if codigo_tecla in combinaciones_alt_gr:
            return f"ALT GR + {chr(codigo_tecla)} ({combinaciones_alt_gr[codigo_tecla]})"
        else:
            return f"ALT GR + UNKNOWN_KEY_{codigo_tecla} (N/A)"

    if mayuscula:
        if codigo_tecla in combinaciones_shift:
            return f"SHIFT + {chr(codigo_tecla)} ({combinaciones_shift[codigo_tecla]})"
        else:
            if 0x41 <= codigo_tecla <= 0x5A:
                letra = chr(codigo_tecla).upper()
                return f"LETRA MAYÚSCULA {letra} ({letra})"
    
    if 0x30 <= codigo_tecla <= 0x39:
        numero = chr(codigo_tecla)
        if mayuscula and codigo_tecla in combinaciones_shift:
            return f"SHIFT + NUMERO {combinaciones_shift[codigo_tecla]} ({combinaciones_shift[codigo_tecla]})"
        return f"NUMERO {numero} ({numero})"

    if 0x60 <= codigo_tecla <= 0x69:
        numero_teclado_numerico = chr(codigo_tecla - 0x30)  
        return f"NUMERO TECLADO NUMERICO {numero_teclado_numerico} ({numero_teclado_numerico})"
    
    if codigo_tecla in teclas_especiales:
        return f"{teclas_especiales[codigo_tecla]} ({chr(codigo_tecla) if codigo_tecla < 256 else 'N/A'})"
    
    return f"UNKNOWN_KEY_{codigo_tecla} (N/A)"
