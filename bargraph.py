import numpy as np
import matplotlib.pyplot as plt
data = {'Python':50, 'C++':21, 'Java':39, 'PHP':8, 'Kotlin':15}
Languages = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(Languages, values, color ='g', width = 0.5)
plt.xlabel("Computer Languages")
plt.ylabel("Popularity in Numbers")
plt.title("Determining the Most popular Language right now")
plt.show()