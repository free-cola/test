import os
import subprocess
import pickle
import sys
import requests

# Hardcoded API Key (Mala práctica)
API_KEY = "12345-SECRET-API-KEY"

def insecure_command_execution(user_input: str) -> None:
    # Vulnerabilidad: Inyección de comandos
    os.system("ping -c 1 " + user_input)

def insecure_subprocess(user_input: str) -> None:
    # Vulnerabilidad: Subproceso inseguro
    subprocess.call("ls " + user_input, shell=True)

def insecure_pickle_loading(pickle_data: bytes) -> None:
    # Vulnerabilidad: Deserialización insegura
    obj = pickle.loads(pickle_data)
    print(obj)

def insecure_eval(user_input: str) -> None:
    # Vulnerabilidad: Uso de eval con entrada de usuario
    eval(user_input)

def download_file(url: str) -> None:
    # Vulnerabilidad: No validamos la URL
    response = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)

def insecure_file_read(file_path: str) -> None:
    # Vulnerabilidad: Lectura de archivo sin validación
    with open(file_path, "r") as f:
        print(f.read())

def main() -> None:
    user_input = input("Enter a command: ")
    insecure_command_execution(user_input)
    insecure_subprocess(user_input)
    insecure_eval(user_input)
    insecure_file_read(user_input)
    url = input("Enter a URL to download: ")
    download_file(url)
    
    # Datos maliciosos de prueba para pickle
    malicious_pickle = b"cos\nsystem\n(S'echo vulnerable'\ntR."
    insecure_pickle_loading(malicious_pickle)

if __name__ == "__main__":
    main()
