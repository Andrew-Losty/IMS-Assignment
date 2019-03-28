# Load CSV using Pandas
import pandas as pd
data = pd.read_csv("coastguard-16k-psnr.log", sep=" ",  header=None)

#Print dimensions of dataframe
print("The shape of the dataset is", data.shape , "rows, columns.")

#Print first 2 rows of dataframe
Print(data.head(2))

#Print size of dataframe
print("The size of the dataset is: ", data.size)


#Print the maximum values found in each column of MSE/PSNR Datafile 
ColmaxValues = data.max()
print('Maximum value in each MSE/PSNR column is: ')
print(ColmaxValues)


The iloc function was used to provide access to a single column for analysis.
# Rows: data.iloc[0] # first row of frame  data.iloc[1] # second row of frame 
# Columns: data.iloc[:,0] # first column of frame data.iloc[:,1] # second column of frame 
#Print the maximum and minimum values found a selected column in each column of MSE/PSNR Datafile 
print ("The maximum PSNR value for the file is:" )
print (data.iloc[:,5].max())
print ("The minimum PSNR value for the file is:" )
print (data.iloc[:,5].min())


The mean and median values were calculated ( note text was removed from data tables).
print ("The mean PSNR value for the file is:" )
print (data.iloc[:,5].mean())
print ("The median PSNR value for the file is:" )
print (data.iloc[:,5].median())

