#!/usr/bin/python3
import sys
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont
import dropbox
import ftplib
from ftplib import FTP

meteo = open('/home/weewx/realtime.txt').read()
data = meteo.split()
print(data[0],'|',data[1],'|','Baro:', data[10],'hPa'' |',' Temp:',data[2],'C' ' |',' Hum:', data[3],'%' ' |','Rain:',data[9],'mm''|','Rain Rate:',data[8],'mm/h''|','Wind:',data[5],'km/h','at' ,data[11])
with open('/home/pi/meteo.txt', 'w') as f:   
    print(data[0],'|',data[1],'|','Baro:', data[10],'hPa'' |','Temp:',data[2],'C' ' |','Hum:', data[3],'%' '|','Rain:',data[9],'mm''|','Rain Rate:',data[8],'mm/h''|','Wind:',data[5],'km/h','at' ,data[11], file=f)  
    
subprocess.call('ffmpeg -rtsp_transport tcp -i rtsp://admin:password@your.camera.ip:34567/user=admin_password=password_channel=1_stream=0.sdp -q:v 1 -y -v quiet /home/pi/grab.jpg', shell=True)

#"Draw a text on an Image, saves it"
text=open('/home/pi/meteo.txt').read()
image=Image.open('/home/pi/grab.jpg')
font = ImageFont.truetype("/usr/share/fonts/gentium-basic/GenBkBasR.ttf",34)
draw=ImageDraw.Draw(image)
# draw text
draw.text((10,10), text=text, font=font, fill=(270,280,0))
# save file
image.save('/home/pi/image.jpg')
#send to Drpbox
app_key = 'your app_key'
app_secret = 'your app_secret'
access_token = 'your_access_token'
file_from = '/home/pi/image.jpg'  
file_to = '/your_dropbox_folder/image.jpg'      
def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode("overwrite") )
upload_file(file_from,file_to)
#send image ftp to your.ftp.sever
filename = "image.jpg"
ftp = FTP("your.ftp.server")
ftp.login("User", "Password")
ftp.cwd("/your/ftp/folder")
myfile = open('/home/pi/grab.jpg', 'rb') 
ftp.storbinary('STOR '+ filename, myfile)
ftp.quit()
