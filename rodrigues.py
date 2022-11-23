import numpy as np
import matplotlib.pyplot as plt

p = np.array([0,1,0])

n = np.array([1,-1,1])
K = np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])

element = 360
step = np.linspace(0,360,element)

x = np.zeros(element)
y = np.zeros(element)
z = np.zeros(element)

count = 0
for theta in step:
    R = np.eye(3) + np.sin(np.deg2rad(theta))*K + (1-np.cos(np.deg2rad(theta)))*np.dot(K,K)
    m_p = np.dot(p,R)
    x[count] = m_p[0]
    y[count] = m_p[1]
    z[count] = m_p[2]
    count+=1

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
plt.show()