import numpy as np
# Use Numpy scientific computing module – as variable np
filename = 'coastguard-16k-psnr.txt'
#Import all data types as strings
data = np.loadtxt(filename, delimiter=' ',dtype=str)

#Print first two row of the MSE/PSNR data file this is to provide initial view of the data
print(data[:2])

#To view the shape of the MSE/PSNR Datafile – can be huge – need to determine data table size
print("The shape of the Datafile:", filename, "is rows, columns", data.shape)
The shape of the Datafile: coastguard-16k-psnr.log is rows, columns (300, 10)

#To view the size of the MSE/PSNR Datafile in bytes
print("The size of the Datafile: ", filename , "is", data.size)

#To print all the entries in the " psnr_avg:" column
print("The MSE/PSNR Datafile-psnr_avg:", filename , "is" , data[:,-5] )

Print (np.min( data[:,-5] ))

#To view the entire Datafile
#print(data)
