import os
import matplotlib.image as mpimg
import numpy as np

path = '/home/sandynote/Downloads/F slot/Term project 2020/Dataset_Question1'

folders = [];
for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r, folder));

folders = sorted(folders, key=lambda x: int(x.split('/')[-1]));

exps_image = np.zeros((15,64*64,10));
for i in range(15):
    f = folders[i];
    m = 0;
    for filename in os.listdir(f):
        img = mpimg.imread(os.path.join(f, filename));
        exps_image[i,:,m:(m+1)] = img.reshape(64*64,1);
        m += 1
        
#sub_images = np.zeros((64*64,15));
#for k in range(15):
#    X = exps_image[k,:,:];
#    u = np.mean(X, axis=0);
#    s = np.std(X, axis=0);
#    for l in range(10):
#        X[:,l] = (X[:,l] - u[l])/s[l];
#    X_norm = X;
#    covX = np.cov(X_norm.T, bias=True);
#    D, V = np.linalg.eig(covX);
#    sub_images[:,k:k+1] = np.dot(X_norm,V[:,0:1]);
    
    
count = 0;
#for i in range(15):
#    for j in range (10):
#        matchM = exps_image[i,:,j];
#        dist = np.zeros((1,15));
#        for k in range(15):
#            dist[0,k] = np.linalg.norm(sub_images[:,k] - matchM);
#        I = np.argmin(dist);
#        if I == i:
#            count += 1;



sub_images = np.zeros((64*64,15));
for k in range(15):
    X = exps_image[k,:,:];
    u = np.mean(X, axis=0);
    s = np.std(X, axis=0);
    for l in range(10):
        X[:,l] = (X[:,l] - u[l])/s[l];
    X_norm = X;
    covX = np.cov(X_norm.T, bias=True);
    D, V = np.linalg.eig(covX)
    per_var = (sum(D[0:1])/sum(D))*100
    print(per_var)
    sub_images[:,k:k+1] = np.dot(X_norm,V[:,0:1]);

for j in range (10):
        matchM = exps_image[0,:,j];
        print(matchM)
        dist = np.zeros((1,15));
        for k in range(15):
            dist[0,k] = np.linalg.norm(sub_images[:,k] - matchM);  
        I = np.argmin(dist);
        print(I)
        if I == 0:
            count += 1;





print(count)
print(str((count/10)*100))


    









    
        

    





