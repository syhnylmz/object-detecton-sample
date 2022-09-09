import cv2
a = int(input("Set your camera, ex.(0,1): "))
class camera():
    def __init__(self, setcam):
        self.setcam=setcam
    def openCamera(self):
        cap = cv2.VideoCapture(self.setcam)
        if cap.isOpened():
            print(f"Camera {self.setcam} opened.")
            while True:
                ret, frame = cap.read()
                if cv2.waitKey(1) & 0xFF==ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
        else:
            print(f"Camera {self.setcam} is not opened.")
camera1=camera(a)
camera1.openCamera()