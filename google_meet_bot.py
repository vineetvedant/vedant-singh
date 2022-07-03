from time import sleep
import pyautogui as auto
import schedule
import webbrowser

link =  input("please enter your class link :- ")

time = input("plesee enter your time ") 


def join():
    webbrowser.open_new_tab('https://' + link)
    sleep(15)
    
    auto.hotkey('ctrl','d')
    auto.hotkey('ctrl','e')
    auto.click(1008,445) ##enter your mouse over enter the meeting 

schedule.every().day.at(time).do(join)

while True:
    schedule.run_pending()
    sleep(1)
