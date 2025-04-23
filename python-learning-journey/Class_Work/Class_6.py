# # Revision of previous all 5 class

# pip install request
import requests 


####  List / Mutable /Chaangeable
# list ma square bracket ata hain []
months:list=['January','Febuary','March','April','May','June','July','August']
months[0]='December' # list ko change karne ka tareeqa
print(months)

# methods of list
# slice
print(months[0:3])

# is ma -1 ko count nahi kara ga  ar negative indexing -1 sa shuru hoti  ha 0 sa nahi
print(months[-3:-1])

# is ma end ma kuch bhi aya ga wo include ho jaya ga 
print(months[3:])






#####  Tuples / Immutable / Unchangeable 

# tuple ko change nahi kar sakte hain yani immutable hoti hain
# tuple ma round bracket ata hain ()
# 0 sa start hota ha indexing same hoti ha tuple ar list ki
numbers : tuple = (12, 15, 93, -21,  27, 57)
print(numbers[0])
# numbers[0] = 100 # ye error de ga kyun ke tuple ko change nahi kar sakte hain

# method of tuples
print(numbers[0:3])


teacher : tuple[str] = ('Ali', 'Ahmed', 'Sara', 'Tariq')
print(teacher)
print(type(teacher)) #<class 'tuple'>
print(teacher[0:2])


# tuple to list conversion 
tuple_to_list = list (teacher)
print(tuple_to_list)
print(type(tuple_to_list)) #<class 'list'>

# adding elem to list
print(tuple_to_list.append('Sie Ameen'))
print(tuple_to_list)

# Converting the list back to tuple
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)
print(type(list_to_tuple))




###    Dictionary


# dictionary ma key value pair hota hain yani key ki value kya hai
# for structured data we used dictionary
#  {} used hota hain

student_info = {
    'roll_no' : 428816,
    'name' : 'Ali Ahmed',
    'courses' : [
        'Docker', 'FastAPI', 'OpenAI Agents'
        ], 
    'assignments':{
        'assignOne':'completed',
        'assignmentTwo':'Inprogress'
        }
}
print(student_info)
print(student_info['courses'])
print(student_info['name'])
print(student_info['courses'][2]) # OpenAI Agents
print(student_info['courses'][-1]) # OpenAI Agents
print(student_info['assignments']['assignmentTwo']) # Nesting ki ha



###### for Loops
for abcd in student_info.values():
    print(abcd) # jitni bhi dictionary ki values ho gi wo print ho jaya gi

for keys, value in student_info.items():
    print(keys, value)

for i in range (1,10):
    print(i)


#  try cath tab use hota ha jab server pa request krni hota ha yani ka api chalani ho
try:
  req = requests.get("https://jsonplaceholder.typicode.com/posts")
  print(req.json())
except Exception as e:
  print(e)
  print("Error agya bhai saab")
else:
  print("Yahha tak pohnch gya") 


  
try:
    url = requests.get("https://jsonplaceholder.typicode.com/posts")
    res = url.json()
    # exception in easy word we call error
except Exception as e :
    print(e)
else:
    print("Yahan error ha")
finally:
    print("Request ended")


####  Sets 