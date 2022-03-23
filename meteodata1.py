#!/usr/bin/python3
import sys
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps
import dropbox
import ftplib
from ftplib import FTP

meteo = open('/home/weewx/realtime.txt').read()
data = meteo.split()
print(data[0],'|',data[1],'|','Baro:', data[10],'hPa'' |',' Temp:',data[2],'C' ' |',' Hum:', data[3],'%' ' |','Rain:',data[9],'mm''|','Rain Rate:',data[8],'mm/h''|','Wind:',data[5],'km/h','at' ,data[11])
with open('/home/pi/meteo.txt', 'w') as f:   
    print(data[0],'|',data[1],'|','Baro:', data[10],'hPa'' |','Temp:',data[2],'C' ' |','Hum:', data[3],'%' '|','Rain:',data[9],'mm''|','Rain Rate:',data[8],'mm/h''|','Wind:',data[5],'km/h','at' ,data[11], file=f)  # Python 3.x
    
subprocess.call('ffmpeg -rtsp_transport tcp -i rtsp://admin:freeze07@192.168.1.8:34567/user=admin_password=freeze07_channel=1_stream=0.sdp -q:v 1 -y -v quiet /home/pi/grab.jpg', shell=True)

#"Draw a text on an Image, saves it"
text=open('/home/pi/meteo.txt').read()
image=Image.open('/home/pi/grab.jpg')
font = ImageFont.truetype("/usr/share/fonts/gentium-basic/GenBkBasR.ttf",34)
draw=ImageDraw.Draw(image)
#draw backround text
draw.rectangle((1920,0 ,0,45), fill='#09189c')
# draw text
draw.text((10,2), text=text, font=font, fill=(255,255,255, 255))
# save file
image.save('/home/pi/image.jpg')
#os.chmod('/home/pi/image.jpg', 777)
#send file to Dropbox
app_key = 'your apikey'
app_secret = 'your secret'
access_token = 'yoyr access'
file_from = '/home/pi/image.jpg'  
file_to = '/yours'      
def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode("overwrite") )
upload_file(file_from,file_to)
#send image ftp to Northmeteo
filename = "image.jpg"
ftp = FTP("your_ftp.com")
ftp.login("user", "password")
ftp.cwd("/your_ftp_folder")
myfile = open('/home/pi/grab.jpg', 'rb') 
ftp.storbinary('STOR '+ filename, myfile)
ftp.quit()

