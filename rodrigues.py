import numpy as np
import matplotlib.pyplot as plt

p = np.array([0,1,0]) #回転させる元の点

n = np.array([1,-1,1])  #回転軸ベクトル
K = np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]]) #回転軸ベクトルnとの外積に対応する歪対称行列

element = 36 #大きい値にすると滑らかな円盤に近づく
step = np.linspace(0,360,element)   #初項0[deg],末項360[deg]のelement[個]の等差配列

x = np.zeros(element)
y = np.zeros(element)   
z = np.zeros(element)   

count = 0
for theta in step:
    R = np.eye(3) + np.sin(np.deg2rad(theta))*K + (1-np.cos(np.deg2rad(theta)))*np.dot(K,K) #ロドリゲスの公式
    m_p = np.dot(p,R) #点にを回転行列をかけて回転
    x[count] = m_p[0]
    y[count] = m_p[1]
    z[count] = m_p[2]
    count+=1

#3次元散布図プロット
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
plt.show()