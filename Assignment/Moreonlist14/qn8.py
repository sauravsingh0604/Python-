'''

8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.

'''

list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}


for item in list:

   if item in frequency:
      
      frequency[item] += 1
   else:
      
      frequency[item] = 1


print(frequency)