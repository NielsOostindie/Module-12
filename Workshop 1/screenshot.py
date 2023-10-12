import pyautogui #importeer data package pyautogui

myScreenshot = pyautogui.screenshot() #zorg dat pyautogui je scherm mag zien en een foto maken
myScreenshot.save('screenshot.png') #sla het bestand op met de naam screenshot