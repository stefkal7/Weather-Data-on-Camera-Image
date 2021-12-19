# Weather-Data-on-Camera-Image
Displays Weather Data to a Camera image
for users of weewx weather monitoring programm. I create a python script that capture an image from rtsp stream of an Ip  camera then draw the weather data and send the image to ftp or dropbox and i run it on crontab every 2 minutes
# Install cumulus realtime 
https://github.com/weewx/weewx/wiki/crt
# Install python pillow
sudo pip3 install pillow
# Install dropbox 
sudo pip install dropbox
# How to run
Because realtime.txt file has al lot of info(data) i created an empty txt file (I named it 'meteo.txt') to write the data i want

I named the script meteodata.py and i use this command on crontab to run it over 2 minutes

/2 * * * * python3 /home/pi/Desktop/meteodata.py >/dev/null 2>&1

I am not good in Python but this worked for me ... Just open the file meteodata.py.txt to see the code and replace the necessary fields with your own(rtsp stream may be different to models of ip cameras and check and replace  the paths of files realtime.txt , meteo.txt etc)

Check my page to see the result https://tagarades-weather.epizy.com
