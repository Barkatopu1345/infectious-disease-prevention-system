import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

def maskMain():
    capture = cv2.VideoCapture(0)
    haar_data = cv2.CascadeClassifier('data.xml')
    data= []
    with_mask=np.load('with_mask.npy')
    without_mask = np.load('without_mask.npy')
    w_mask = with_mask.reshape(200,((50*50*3)+75))
    wt_mask = without_mask.reshape(200,50*50*3)
    x = np.r_[with_mask,without_mask]
    labels = np.zeros(x.shape[0])
    labels[200:] = 1.0
    names= {0: 'Mask', 1: 'No Mask'}
    x_train, x_test, y_train, y_test = train_test_split(x,labels,test_size=0.20, )
    pca= PCA(n_components=3)
    nsamples, nx, ny,nz = x_train.shape
    d2_x_train = x_train.reshape((nsamples,nx*ny*nz))
    d2_x_train = pca.fit_transform(d2_x_train)
    svm = SVC()
    svm.fit(d2_x_train,y_train)
    nsamples, nx, ny,nz = x_test.shape
    d2_x_test = x_test.reshape((nsamples,nx*ny*nz))
    d2_x_test = pca.transform(d2_x_test)
    y_pred = svm.predict(d2_x_test)

    while True:
        flag, img = capture.read()
        #img = cv2.imread('self.jpg')
        if flag:
            faces = haar_data.detectMultiScale(img)
            for x,y,w,h in faces:

                face = img[y:y+h, x: x+w, ]
                face = cv2.resize(face,(50,50))
                face = face.reshape(1,-1)
                face = pca.transform(face)
                #pred = svm.predict(face)
                n = 'No mask'
                n = names[int(svm.predict(face))]
                A= (x, y + h + 50)
                if(n=='Mask'):
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
                    cv2.putText(img, n, (A), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
                    cv2.putText(img, n , (A), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
                print(n)
            cv2.imshow('result',img)
            if cv2.waitKey(2) == 27 or len(data)>=200:
                break
    capture.release()
    cv2.destroyAllWindows()

# Problem : we have 3parts .. 1. nose 2. mouth 3. chin .... if we can'f find out any one then we say you are waring mask. otherwise our program will say that we are not waring mask.
# we have to set up this program on high light. otherwise it will give some error on low light.