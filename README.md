# Spyware Project with Telegram Bot for Windows  

This project was developed as part of a university cybersecurity assignment to demonstrate how basic programming knowledge can be used to create potentially harmful tools. Specifically, this project is a spyware with communication capabilities through a Telegram bot, designed specifically for the Windows operating system. The goal is to show how quickly and effectively such tools can be developed, even by individuals with basic programming knowledge.

## Project Objective  

The purpose of this project is twofold:  

1. **Demonstrate technical accessibility**: Show how a tool like spyware can be developed by anyone with basic programming skills, highlighting the importance of strengthening system security.  
2. **Analyze security implications**: Provide a controlled environment to understand how such tools work, assess the associated risks, and explore strategies to mitigate these threats.  

## Features  

- **Sensitive Data Capture**: Collects data such as keystrokes, screenshots, and other key system information.  
- **Communication via Telegram**: Uses a Telegram bot to securely send the collected data in real-time to a predefined channel.  
- **Windows Compatibility**: Specifically designed to operate in Windows environments, leveraging system features to run discreetly.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Roger-Valles/SpyWare-With-Telegram-Bot
   ```
  
2. **Set up the Telegram bot token**:  
   - Create a bot on Telegram using BotFather.  
   - Copy your token and paste it into the code in `main_spyware.py` where the bot is initialized.

   <img src="https://github.com/user-attachments/assets/1dd23135-165a-4f01-be67-d1041106f341" width="300" height="500">
   
3. **Copy your ChatID**:  
   Copy your `chat_id="131933xxxx"` and paste it into `keylogger.py`.

4. **Make sure Python is installed**:  
   This project requires Python to run. Ensure you have Python 3.x installed on your system. You can download Python from https://www.python.org/downloads.

5. **Run the build script**:  
   Double-click on `build.bat` to compile the program.

## How to use

Double-click the generated `.exe` file to run the program.

## Errors  
You have to add th Python Scritps PATH to environment variables of windows
1. **Go to the Scripts Python folder and copy this path**
   Can be this:
   ```C:\Users\USER\AppData\Local\Programs\Python\Python312\Scripts```
   Or can be this:
   ```C:\Users\USER\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts```
  
2. **Find Control Panel and search for enviorment variables**:  
   - Once you are there click on PATH variable and add a new line with the path of Scripts Folder
   - ![image](https://github.com/user-attachments/assets/5c7972bf-6f3c-4054-838b-d646477b1d03)
     
3. **If this does not work to you just execute this command**:
     ```C:\Users\USER\AppData\Local\Programs\Python\Python312\Scripts\pyinstaller.exe build.spec```
     Or this one:
     ```C:\Users\USER\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe build.spec```
      
## Disclaimer  

**⚠️ Warning:** This project is for educational purposes and security testing in authorized environments only. Unauthorized use of this tool may be illegal and is prohibited.

