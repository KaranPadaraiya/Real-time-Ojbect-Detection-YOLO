import cv2
import numpy as np


network = cv2.dnn.readNet('yolov3.weights', 'yolo.cfg')

classes = []
with open("coco.names", "r") as f:
    classes = f.read().splitlines()

cap = cv2.VideoCapture('Test.mp4')
# cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_PLAIN

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))

while True:
    _, img = cap.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
    network.setInput(blob)
    output_layers_names = network.getUnconnectedOutLayersNames()
    layerOutputs = network.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.2:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    ind = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

    if len(ind)>0:
        print(len(ind))
        if len(ind)<=45:
            for i in ind.flatten():
                print(len(ind))
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = str(round(confidences[i]*100,2))+ "%"
                color = [0,0,255]
                cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
                cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (0,0,255), 2)
        elif len(ind)> 45:
            for i in ind:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = str(round(confidences[i]*100,2))+ "%"
                color = [0,255,0]
                cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
                cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (0,255,0), 2)
    img = cv2.resize(img,(640,480))
    cv2.imshow('Image', img)
    out.write(img)
    key = cv2.waitKey(1)
    if key== ord("q"):
        break


cap.release()
out.relase()
cv2.destroyAllWindows()
