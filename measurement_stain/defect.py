from ultralytics import YOLO
import cv2
import numpy
from scipy.spatial import distance as dist
modela = YOLO(r'models/yolov8n.pt')  # pretrained YOLOv8n model
modelb = YOLO(r'models/yolov8x-pose-p6.pt')  # pretrained YOLOv8n model
  
#'http://192.168.103.200:4747/video'
# Run batched inference on a list of images
url='http://192.168.252.174:4747/video'

cap=cv2.VideoCapture(url)
while True:
    ret,frame=cap.read()
    img=frame.copy()
    # Load a model
    resultsa = modela(frame, stream=True)  # return a generator of Results objects
    resultsb = modelb(frame, stream=True)  # return a generator of Results objects
    i=0

    # Process results generator
    for resulta,resultb in zip(resultsa,resultsb):
        #boxes = resulta.boxes.xyxy.cpu().numpy()
        #print(boxes)  # Boxes object for bounding box outputs
        keypoints_b = resultb.keypoints.xy.cpu().numpy()  # Keypoints object for pose outputs
        keypoints_b=keypoints_b.tolist()
        try:
            left_shoulder = keypoints_b[0][5]  # Index 5 is the left shoulder
            right_shoulder = keypoints_b[0][6] 
            torso_l=keypoints_b[0][11]
            torso_r=keypoints_b[0][12]
            left_shoulder=(int(left_shoulder[0]),int(left_shoulder[1])) 
            right_shoulder=(int(right_shoulder[0]),int(right_shoulder[1]))
            torso_l=(int(torso_l[0]),int(torso_l[1]))
            torso_r=(int(torso_r[0]),int(torso_r[1]))

            cv2.circle(img, left_shoulder, 5, (0, 255, 0), -1)
            cv2.circle(img, right_shoulder, 5, (0, 255, 0), -1)
            cv2.line(img, left_shoulder, right_shoulder, (255, 0, 0), 2)
            cv2.line(img, left_shoulder, torso_l, (255, 0, 0), 2)
            cv2.line(img, right_shoulder, torso_r, (255, 0, 0), 2)
            cv2.line(img, torso_r, torso_l, (255, 0, 0), 2)

            cv2.circle(img, torso_l, 5, (0, 255, 0), -1)
            cv2.circle(img, torso_r, 5, (0, 255, 0), -1)            
            distance_shoulders = dist.euclidean(left_shoulder,right_shoulder)
            distance_torso= dist.euclidean(torso_l,torso_r)
            distance_length_l=dist.euclidean(left_shoulder,torso_l)
            distance_length_r=dist.euclidean(right_shoulder,torso_r)

            cv2.putText(img, str(11*400.45/distance_shoulders), ((left_shoulder[0] + right_shoulder[0]) // 2, (left_shoulder[1] + right_shoulder[1]) // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(img, str(11*400.45/distance_shoulders), ((torso_r[0] + torso_l[0]) // 2, (torso_l[1] + torso_r[1]) // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(img, str(11*400.45/distance_length_r), ((left_shoulder[0] + torso_l[0]) // 2, (left_shoulder[1] + torso_l[1]) // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(img, str(11*400.45/distance_length_r), ((right_shoulder[0] + torso_r[0]) // 2, (right_shoulder[1] + torso_r[1]) // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        except:
            pass
        """ for box in boxes:
            x1, y1, x2, y2 = box.astype(int)
            try:
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            except:
                pass """# Index 6 is the right shoulder
       
        
        cv2.imshow('frame',img) 
        cv2.waitKey(1)
       






       ###print(11*400.45/distance_shoulders)