# Luis Fernando Koh Avila
# Data 2 B
# My example seeing the incomes from an enterprise during 2019, 2020, 2021
import matplotlib.pyplot as plt

plt.style.use('seaborn-colorblind') # Taking a style for the plot

months_x = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] # X axis with the months
incomes_2019 = [25000,25700,28000,20500,23000,29400,32000,24000,26000,22500,19000,20400] # Incomes during 2019
plt.plot(months_x, incomes_2019, 'c-',marker = 'o', label='2019') # Adding the 2019 incomes as y axis, and adding format

incomes_2020 = [26000,29700,32000,29500,33000,35400,24000,28000,39000,27500,24000,25400] # Incomes during 2020
plt.plot(months_x, incomes_2020, 'k-.',marker = '*', label='2020') # Adding the 2020 incomes as y axis, and adding format

incomes_2021 = [32000,30700,33000,34500,28000,15400,10000,8800,7500,0,0,0] # Incomes during 2021
plt.plot(months_x, incomes_2021, 'b--',marker = 'X', label='2021') # Adding the 2021 incomes as y axis, and adding format

plt.legend() # Showing the legend on the plot
plt.title("Incomes in 2019-2021 period") # Definig a title
plt.xlabel('Year') # Naming the x label
plt.ylabel('Earnings') # Naming the y label
plt.show() # Displaying the plot on screen
