""" I am trying to create a function that identifies the characthers that are being repeated (>2)
in a string, and return the characther and the amount of times it has been. """

#Get the string and eliminate the spaces 
string = input("Send your string here: ")
string = string.replace(" ", "")

#
l = []
sequence = []

for i in string:
      if i in l:
            sequence.append(i)
      else:
            l.append(i) 

results = set()
def func(sequence):
      for i in sequence:
            r = sequence.count(i)
            if r > 1:
                  results.add(f"'{i}' appears {r + 1} times")
            else:
                  results.add(f"'{i}' appears twice")
      return results
            
print(func(sequence))

