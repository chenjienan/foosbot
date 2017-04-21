import io
import picamera
import config
import thread

camera_recording = True
camera = picamera.PiCamera(framerate=config.framerate)
stream = picamera.PiCameraCircularIO(camera, seconds=config.record_time)

def is_recording():
    try:
        return camera_recording
    except NameError:
        return False

def start_recording():
    camera_recording = True
    thread.start_new_thread(recording_thread, ())

def recording_thread():
    camera.start_recording(stream, format='h264')
    try:
        while is_recording():
            # Keep recording for 5 seconds and only then write the stream to disk
            camera.wait_recording(1)
            stream.copy_to(config.video_path)
    finally:
        camera.stop_recording()

def stop_recording():
    if is_recording():
        camera_recording = False
        camera.stop_recording()
