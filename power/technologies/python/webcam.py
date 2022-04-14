import cv2

# "pip list" to check packages installed.

# Define a video capture object.
vid = cv2.VideoCapture(0)

# Define a tracker.
# tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.legacy.TrackerCSRT_create() # Takes a lot of power, but more accurate.
ret, frame = vid.read()
bbox = cv2.selectROI("This is the window title", frame, False)
tracker.init(frame, bbox)
  
def drawBox(frame, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    # Recentangle.
    cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (86,170,255), 3, 1)
    cv2.putText(frame, "Looks like a bitch!", (75,75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)


while(True):
    # Timer.
    timer = cv2.getTickCount()
    # Capture the video frame.
    ret, frame = vid.read()
    ret, bbox = tracker.update(frame)
    # Is it tracking?
    if ret:
        drawBox(frame, bbox)
    else:
        cv2.putText(frame, "Lost", (75,75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    # FPS.
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(frame, str(int(fps)), (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    # Display the resulting frame.
    cv2.imshow("This is the window title", frame)    
    # The 'q' button is set as the quitting button you may use any desired button of your choice.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object.
vid.release()
# Destroy all the windows.
cv2.destroyAllWindows()