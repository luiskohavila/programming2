# Replic of Professor's Juan Vasquez plot

import matplotlib.pyplot as plt
import pandas as pd

df_wktime1 = pd.read_csv('wktime.T001.his',delimiter=' ',header=None) # Opening the file wktime.T001 and read it as Data Frame
plt.plot(df_wktime1[0], df_wktime1[1], color = 'r', label = 'Time 1') # Defining the x and y axis and assign name to the label

df_wktime4 = pd.read_csv('wktime.T004.his',delimiter=' ',header=None) # Opening the file wktime.T004 and read it as Data Frame
plt.plot(df_wktime4[0], df_wktime4[1], color = 'b', label = 'Time 4') # Defining the x and y axis and assign name to the label

plt.xlabel('Wealth') # Naming the x label
plt.ylabel('Probability') # Naming the y label
plt.title('Probability Distribution') # Putting title to the plot
plt.legend() # Plotting legends
plt.xscale("log") # Setting the scale to be logarithmic
plt.yscale("log") # Setting the scale to be logarithmic
plt.xlim((0.000001, 100.0)) # Defining the x limits that will be shown
plt.ylim((0.000001, 100000.0)) # Defining the y limits that will be shown
plt.tight_layout() # Adjusting subplot params
plt.show() # Displaying on screen
