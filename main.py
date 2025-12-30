import cv2
import time
print("The camera is starting up...")
selected_camera = 2
cap = cv2.VideoCapture(selected_camera, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("No stream.")
    exit()
print(f"Camera ({selected_camera}) is active! Press 'q'for exit.")
while True:
    ret, frame = cap.read()
    if not ret:
        continue
# Finding the center.
    height, width = frame.shape[:2]
    cx = width // 2
    cy = height // 2
# Determining 200*200 pixel area.
    x1 = cx - 100
    y1 = cy - 100
    x2 = cx + 100
    y2 = cy + 100
# Cropping this 200*200 region.
    roi = frame[y1:y2, x1:x2] #region of interest
# Converting this piece to gray.
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
# Format change to paste the  gray image back.
    roi_gray_bgr = cv2.cvtColor(roi_gray, cv2.COLOR_GRAY2BGR)
# Putting the image back its old position.     
    frame[y1:y2, x1:x2] = roi_gray_bgr
# A green rectangle shows where we cut.
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2) # Red rectangle.
# We put a text "filter:gray " on the leftmost corner of the image. 
    cv2.putText(frame, "filter: gray", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 0), 2)  
# Showing the last window.
    cv2.imshow('Final:', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()