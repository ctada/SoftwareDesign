""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/media/celine/6E86D54986D513071/Users/cta/Downloads/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')

if not cap.isOpened(): 
	cap.open()

while(True):
	ret, frame = cap.read()  # Capture frame-by-frame
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20)) # find faces
	
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel) # blurs rectangular face boundary, degree of blurriness determined by kernel
		#cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255)) # Draw bounding rectangle around detected faces
		
		# draw face
		# left eye
		cv2.circle(frame[y:y+h,x:x+w,:], (int(float(w)/4), int(float(h)/3)), 20, (255,255,255), -1) # eyeball center, radius in pixels, color = white, -1 = fill
		cv2.circle(frame[y:y+h,x:x+w,:], (int(float(w)/4), int(float(h)/3)), 7, (0,0,0), -1) # pupil center, radius in pixels, color= black, -1 = fill
		# right eye
		cv2.circle(frame[y:y+h,x:x+w,:], (int(float(3*w)/4), int(float(h)/3)), 20, (255,255,255), -1) # eyeball center, radius in pixels, color = white, -1 = fill
		cv2.circle(frame[y:y+h,x:x+w,:], (int(float(3*w)/4), int(float(h)/3)), 7, (0,0,0), -1) # pupil center, radius in pixels, color= black, -1 = fill
		# smile
		cv2.ellipse(frame[y:y+h,x:x+w,:], (int(float(w)/2), int(float(7.5*h)/10)), (50, 25), 0, 30, 150, (0,0,0), 2) #center, axes, angle, startAngle, endAngle, color, line thickness

	# Display the resulting frame, filter first if desired (gray filter removed here)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
# To close, click video frame and press 'q'
cap.release()
cv2.destroyAllWindows()

