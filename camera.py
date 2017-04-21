from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/git/foosbot/videos/video1.mp4')
sleep(5)
camera.stop_recording()
camera.stop_preview()
