#print function
#max value
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))

#len function
# a=[1,2,3,4,5,6]
# print(len(a))

# function
# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif") 

#multiple function
# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev") 

#multiplication2 function
# def add_numbers(number1, number2):
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = "134"
# name = "Rinki"
# add_numbers(num_x, name) 

#argument 
def icecream(*flavours):
 for flavour in flavours:
  print("i love"+flavour)

icecream("chocolate", "butterscotch","vanilla","strawberry") 

#default
def attendance(name,status="absent"):
    print(name,"is",status," today")

attendance("kartik","present")
attendance("sonu")
attendance("vishal","present")
attendance("umesh") 