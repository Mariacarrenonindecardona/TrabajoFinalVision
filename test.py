import os
import time
import cv2
from picamera2 import Picamera2

def stream_video():
    picam = Picamera2()
    picam.preview_configuration.main.size = (1280, 720)
    picam.preview_configuration.main.format = "RGB888"
    picam.preview_configuration.align()
    picam.configure("preview")
    picam.start()

    last_saved_time = 0 
    save_interval = 2 

    while True:
        frame = picam.capture_array()
        cv2.imshow("picam", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('p'):
            current_time = time.time()
            if current_time - last_saved_time >= save_interval:
                last_saved_time = current_time  
                output_folder = "../data"
                img_name = f"Foto_{int(current_time)}.png"  
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                cv2.imwrite(os.path.join(output_folder, img_name), frame)
                print(f"Foto guardada como {img_name}")
            else:
                print("Espere antes de guardar otra foto.")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    stream_video()
