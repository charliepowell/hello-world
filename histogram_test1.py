import matplotlib.pyplot as plt 

population_ages = [23, 25, 24, 28, 23, 22, 29, 34, 31, 36, 38, 38, 43, 47, 50, 57, 63, 70, 23, 25, 24, 28, 23,  22, 29, 34, 31, 36, 63, 70, 23, 25, 24, 28, 23,  22, 29, 34, 31, 36, 38, 38, 43, 47, 50, 57, 63, 70, 23, 25, 24, 28, 23,  22, 29, 34, 31, 36, 38, 38, 43, 47, 50, 57, 63, 70, 23, 25, 24, 28, 23,  22, 29, 34, 31, 36, 38, 38, 43, 47, 50, 57, 63, 70, 23, 25, 24, 28, 23,  22, 29, 34, 31, 36, 38, 38, 43, 47, 50, 57, 63, 70, 23, 25, 24, 28, 23,  22, 29, 34, 31, 36, 38, 38, 43, 47, 50, 57, 63, 70, 23, 25, 24, 28, 23,  22, 29, 34, 31, 36, 38, 38, 43, 47, 50, 23, 22, 29, 34, 31, 36, 38, 38, 43, 47, 50, 57, 63, 70]

bins = [20, 25, 30, 35, 40, 50, 60, 80]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.9, color='r')

plt.xlabel("Number of Times per Day I Decide that I'm Bored")
plt.ylabel('Frequency')
plt.title("Productivity Graph")
plt.show()
