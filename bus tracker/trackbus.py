import pyautogui as pg
import webbrowser as wb
import time

wb.open("http://track.roztrack.com/modern/#/login",1)
time.sleep(10)
#pg.displayMousePosition()
pg.moveTo(679,203)
pg.click()
pg.moveTo(679,260)
time.sleep(1)
pg.click()
time.sleep(1)
pg.moveTo(679,326)
time.sleep(1)
pg.click()
