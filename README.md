# Weather-Data-on-Camera-Image
Displays Weather Data from Weewx to ip  Camera image
For users of weewx weather monitoring programm i create a python script that displays weather data to a camera image and send the image to ftp or dropbox and i run it on crontab every 2 minutes
Install cumulus realtime from https://github.com/weewx/weewx/wiki/crt

Install python pillow
sudo pip3 install pillow
install dropbox 
sudo pip install dropbox
I also create an empty txt file (meteo.txt) to write the data i want

I named the script meteodata.py and i use this command on crontab to run it over 2 minutes

/2 * * * * python3 /home/pi/Desktop/meteodata.py >/dev/null 2>&1

I am not good in Python but this worked for me ... Just replace the necessary fields with your own

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

##"Draw a text on an Image, saves it"
text=open('/home/pi/meteo.txt').read()
image=Image.open('/home/pi/grab.jpg')
font = ImageFont.truetype("/usr/share/fonts/gentium-basic/GenBkBasR.ttf",34)
draw=ImageDraw.Draw(image)
##draw text
draw.text((10,10), text=text, font=font, fill=(270,280,0))
##save file
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
##send image ftp to your.ftp.sever
filename = "image.jpg"
ftp = FTP("your.ftp.server")
ftp.login("User", "Password")
ftp.cwd("/your/ftp/folder")
myfile = open('/home/pi/grab.jpg', 'rb') 
ftp.storbinary('STOR '+ filename, myfile)
ftp.quit()
