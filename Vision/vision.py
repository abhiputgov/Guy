import cv2
import sys
##caffe tracker based on GOTURN
tracker = cv2.TrackerGOTURN_create()
##once the tracker is decalred, we start the frame reader
video = cv2.VideoCapture("smapleVideo.mp4")

if not video.isOpened():
    print("Could not open the video")
    sys.exit()
else:
    ok, frame = video.read()
    if not ok:
        print("Could not read the video file")

##boundry conditions:
bbox = (276, 23, 86, 320)

##tracker initaialized
ok = tracker.init(frame, bbox)

while True:
    ##frame reading....
    ok, frame = video.read()
    if not ok:
        break
 
    ##timer count
    timer = cv2.getTickCount() 
    ## tracker get updated here
    ok, bbox = tracker.update(frame) 
    ## calculation the FPS
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer); 
    ##Drawing the bounding box based of the bbox changes
    if ok:
        ##Tracking ongoing
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        ##Tracking? I dont think so
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
    ##Displaying tracker type on frame
    cv2.putText(frame, "GOTURN Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
 
    ##Displaying  FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
 
    ## final result display
    cv2.imshow("Tracking", frame)
  
    ##way to exit the screen --> press ESC
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
