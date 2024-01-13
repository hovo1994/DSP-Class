
# Python program showing  
# Graphical representation of  
# cos() function  
import math 
import numpy as np 
import matplotlib.pyplot as plt  
  
n_continuous = np.linspace(0, 100, 20000) 
n_discrete = np.linspace(0, 100, 100) 
  
cont_cos_w0n = [] 
cont_cos_w0_2pi_n = []
discrete_cos_w0n = [] 
discrete_cos_w0_2pi_n = []

omega = (2 * np.pi / 20) 
omega2 = (2*np.pi / 20) + 2 * np.pi

for i in range(len(n_discrete)): 
    discrete_cos_w0n.append(math.cos(omega * n_discrete[i])) 
    discrete_cos_w0_2pi_n.append(math.cos(omega2 * n_discrete[i]))
    i += 1
  

for i in range(len(n_continuous)): 
    cont_cos_w0n.append(math.cos(omega * n_continuous[i])) 
    cont_cos_w0_2pi_n.append(math.cos(omega2 * n_continuous[i]))
    i += 1

  
fig = plt.figure()
axs = []
axs.append(fig.add_subplot(411))
axs[0].plot(n_continuous, cont_cos_w0n, color = 'red')
axs[0].title.set_text("Continuous cos(w_0n)")
axs.append(fig.add_subplot(412))
axs[1].plot(n_continuous, cont_cos_w0_2pi_n, color = 'green')
axs[1].title.set_text("Continuous cos((w_0 + 2pi)n)")
axs.append(fig.add_subplot(413))
axs[2].plot(n_discrete, discrete_cos_w0n, color = 'red', marker='o')
axs[2].title.set_text("Sampled cos(w_0n)")
axs.append(fig.add_subplot(414))
axs[3].plot(n_discrete, discrete_cos_w0_2pi_n, color = 'green', marker='o')
axs[3].title.set_text("Sampled cos((w_0 + 2pi)n)")
plt.show()  
