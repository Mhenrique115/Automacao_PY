import pyautogui 
from time import sleep

with open(r'D:\Projetos\Automação com py\codigos_clientes.txt','r') as file:
    for linha in file:
        cliente = linha.strip()
        pyautogui.click(117,463, duration=2)  
        pyautogui.write(cliente)  
        # pyautogui.click(197,401, duration=2)
        pyautogui.click(265,774, duration=2)
        pyautogui.click(131,465, duration=2)
        sleep(5)
        