import numpy as np
import cv2


def useWebcam():
  cap = cv2.VideoCapture(0)
  while(True):
      # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

def useLocalFile(filename):
  cap = cv2.VideoCapture(filename)

  while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()
  
useWebcam()