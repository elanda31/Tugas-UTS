import pywhatkit # instal dulu dengan: pip install pywhatkit
import pyautogui # instal dulu dengan: pip install pyautogui
import time      # instal juga dengan: pip install flask
import rsa       # instal dulu dengan pip instal rsa
kuncipublik, kunciprivat = rsa.newkeys(1024)
with open("public.pem","wb") as f:
    f.write(kuncipublik.save_pkcs1("PEM"))
with open("private.pem","wb") as f:
    f.write(kunciprivat.save_pkcs1("PEM"))
nohp = input('Ketik nomor hpwa tujuan, diawali dengan +62 : ')
pesan = input('Ketik pesan yang akan dikirimkan : ')
jam = int(input ('Ketik jam saat kirim (0-24) : '))
menit= int(input('Ketik menit saat kirim (0-59) : '))
pesanchiperrsa=rsa.encrypt(pesan.encode(),kuncipublik)
with open("pesanenkrip.txt","wb") as f:
    f.write(pesanchiperrsa)
pywhatkit.sendwhatmsg(nohp,pesanchiperrsa,jam,menit)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.press('enter')