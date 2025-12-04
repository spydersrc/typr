try:
  import os
  import json
  import random 
  import pyautogui 
  import time 
  import string 
  from random import randint
except ImportError as e: 
    print(f"Error importing module: {e}. Installing {e.name}...")
    os.system(f"pip install {e.name}")  
    
import os
import json
import random 
import pyautogui 
import time 
import string 
from random import randint

file =  open("text.txt", "r")  
data = file.read() 
def wpm_delay(wpm):
    return 60 / (wpm * 5)

def auto_type_error(text, whentofix, errorchance, delay):
    s = text.split()
    for word in s: 
        pyautogui.typewrite(word) 
        human_error(whentofix, errorchance) 
        pyautogui.typewrite(' ') 
        time.sleep(float(delay))

def auto_type(text, delay):
    s = text.split()
    for word in s: 
        pyautogui.typewrite(word, interval=float(delay)) 
        pyautogui.typewrite(' ')
        
def human_error(whentofix, errorchance):
    letters = string.ascii_letters + string.digits + string.punctuation + ' ' 
    error_chance = int(errorchance)
    for i in range(1): 
        s = randint(0, 100)
        if s <= error_chance: 
            wrong_char = random.choice(letters) 
            pyautogui.typewrite(wrong_char) 
            time.sleep(float(whentofix)) 
            pyautogui.press('backspace') 
    else: 
        return 


def main(): 
    print("Welcome to Typr with Human Error Simulation!")
    print("Make sure you have a text.txt file in the same directory as this script. It will read from that file your text.")
    fixerror = input("Do you want to simulate human error? (yes/no): ") 
    wpm = input("Enter your typing speed in WPM: ")
    delay = wpm_delay(int(wpm))
    if fixerror == 'yes':
        errorchance = input("Enter human error chance percentage (0-100): ")
        whentofix = input("When to fix errors? Enter time in seconds: ")
        print("Starting to type in 5 seconds... Tab into the application you want to type in ")
        time.sleep(5) 
        auto_type_error(data, whentofix, errorchance, delay)
    else: 
        print("Starting to type in 5 seconds... Tab into the application you want to type in ")
        time.sleep(5) 
        auto_type(data, delay)

main()
