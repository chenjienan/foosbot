import io
import picamera
import config


camera = picamera.PiCamera(framerate=config.framerate)
stream = picamera.PiCameraCircularIO(camera, seconds=15)
camera.start_recording(stream, format='h264')
try:
    while True:
        # Keep recording for 5 seconds and only then write the stream to disk
        camera.wait_recording(1)
        stream.copy_to(config.video_path)
finally:
    camera.stop_recording()
