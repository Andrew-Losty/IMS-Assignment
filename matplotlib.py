import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("coastguard-16k-psnr-mod.log", sep=" ",  header=None, )
print("The PSNR for 300 frame file coastguard-16k-psnr-mod.log is:")
plt.plot (data.iloc[:,5])

data = pd.read_csv("coastguard-128k-psnr-mod.log", sep=" ",  header=None, )
print("The PSNR for 300 frame file coastguard-128k-psnr-mod.log is:")
plt.plot (data.iloc[:,5])

data = pd.read_csv("coastguard-512k-psnr-mod.log", sep=" ",  header=None, )
print("The PSNR for 300 frame file coastguard-512k-psnr-mod.log is:")
plt.plot (data.iloc[:,5])

data = pd.read_csv("coastguard-1024k-psnr-mod.log", sep=" ",  header=None, )
print("The PSNR for 300 frame file coastguard-1028k-psnr-mod.log is:")
plt.plot (data.iloc[:,5])

data = pd.read_csv("coastguard-2048k-psnr-mod.log", sep=" ",  header=None, )
print("The PSNR for 300 frame file coastguard-2048k-psnr-mod.log is:")
plt.plot (data.iloc[:,5])

