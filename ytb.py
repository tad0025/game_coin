from requests import get
url='https://ghichu.vn/share/c7890ec70'
while True:
    dl=get(url).text.split('readonly>')[1].split('<')[0]
    if dl=='onl':break

from selenium import webdriver
from time import sleep
from pyautogui import click
import threading
from shutil import rmtree,copytree

def open_youtube(l):
    rmtree(r'D:\NSTD\golike'+'\\'+str(l))
    copytree(r'D:\NSTD'+'\\'+str(l), r'D:\NSTD\golike'+'\\'+str(l))

    options = webdriver.ChromeOptions()
    options.add_argument(r'--user-data-dir=D:\NSTD\golike'+'\\'+str(l))
    options.add_argument('--app=https://cryptochampion.game/launcher/')

    driver = webdriver.Chrome(options=options)
    x = l * 200
    y = 0
    driver.set_window_rect(x, y, 200, 350)

    input()

# Bắt đầu
threads = [];n=4
for l in range(n):
    threads.append(threading.Thread(target=open_youtube, args=(l,)))
for t in threads: t.start()
#for t in threads: t.join()
input()
sleep(20)
while True:
     for l in range(0,n):
        click(150+215*l,310)
        sleep(0.5)
     sleep(6)

     for l in range(0,n):
        click(75+215*l,243)
        sleep(0.5)

     for l in range(0,n):
        click(135+215*l,223)
        sleep(0.5)
     sleep(20)

     for l in range(0,n):
        click(100+215*l,283)
        sleep(0.5)
     sleep(6)
