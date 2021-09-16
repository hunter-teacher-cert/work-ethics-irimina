#function definitions.

#find all names with a given phone number and return the list of names
def findNames(contacts,number):
  nameList=[];
  for name in contacts:
    if contacts[name]==number:
      nameList.append(name)
  return nameList

#print alphabetical list of all dict items
def printAll(contacts):
  print("All names and numbers: ")
  for key in sorted(contacts):
    print(key, contacts[key])

# end of function definitions


# name/phone number pairs program
phoneContacts= {"Sam":2123448444, "Stan":2122554488,"Ana":9173457766, "Emma":9178879095, "Olivia":2334448484, "Bob":9146769988, "Novak":2129873241, "Alex":2364048484, "Sebastian":2122554488, "Leyla":9173457766, "Mitt":9146873242}


# check is Mitt is in the list of phone contacts, program shows the number of the last instance of Mitt
if "Mitt" in phoneContacts:
  print("Mitt's number is", phoneContacts["Mitt"])
else:
  print("Not found in the phone list")

#get and print a list of a contact with a given number
nameList=findNames(phoneContacts,9146873242)
print("Name for 914-687-3242:", end="")
for name in nameList:
  print(name,end=" ")
print()

print(" ")
printAll(phoneContacts)

'''
Resources:
https://docs.python.org/3/howto/sorting.html
'''
