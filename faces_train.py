import os 
import cv2 as cv
import numpy as np 

people=['Ben Affleck','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

# p=[]
# # for i in os.listdir(r'C:\Users\ABHIRAM NAIDU\Desktop\OpenCV\Resources\Faces\train'):
# #     p.append(i)

# # print(p)
DIR=r'C:\Users\ABHIRAM NAIDU\Desktop\OpenCV\Resources\Faces\train'
haar_cascade=cv.CascadeClassifier('haar_face.xml')
features=[]
labels=[]


def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbours=4)

            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training Done-----')
labels=np.array(labels,dtype='object')

features=np.array(features)

# Train the recognizer on the features list and the labels list 
face_recognizer=cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

np.save('features.npy',features)
np.save('labels.npy',labels)



     