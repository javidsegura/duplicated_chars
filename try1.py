""" I am trying to create a function that identifies the characthers that are being repeated (>2)
in a string, and return the characther and the amount of times it has been. """

string = input("Send your string here: ")
string = string.replace(" ", "") #Get the string and eliminate the spaces 

sequence = []
duplicated = [] 
results = set() # Make sure results are not repeated for every duplicated i

for i in string:
      if i in duplicated: #Originally duplicated starts empty
            sequence.append(i)  # Add non-duplicated chars 
      else:
            duplicated.append(i) # Add duplicated chars

def func(sequence):
      for i in sequence: #Check within the duplicated list
            r = sequence.count(i) #Count how many times a single character appears
            if r > 1:
                  results.add(f"'{i}' appears {r + 1} times") 
            else:
                  results.add(f"'{i}' appears twice")
      return results
            
print(func(sequence))

