# Weather-Data-on-Camera-Image
Displays Weather Data from Weewx to ip  Camera image
For users of weewx weather monitoring programm i create a python script that displays weather data to a camera image and send the image to ftp or dropbox and i run it on crontab every 2 minutes
# Install cumulus realtime 
https://github.com/weewx/weewx/wiki/crt
# Install python pillow
sudo pip3 install pillow
# install dropbox 
sudo pip install dropbox

I also create an empty txt file (meteo.txt) to write the data i want

I named the script meteodata.py and i use this command on crontab to run it over 2 minutes

/2 * * * * python3 /home/pi/Desktop/meteodata.py >/dev/null 2>&1

I am not good in Python but this worked for me ... Just open the file meteodata.py.txt to see the code and replace the necessary fields with your own

