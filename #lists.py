#lists allow to save data of different types
numbers = [1,2,3,4]
print(list)
print(type(numbers))
tasks = ['do the dishes', 'play videogames']
types = ['types list', True, 'hola']

#add new element
numbers.append(5) #at the end of the list
numbers.insert(3, 'new number') #insert at the position 3
print(numbers.index('new number'))
numbers.remove('new number') #delete an specific value
numbers.pop() #delete last item of the list
numbers.pop(0) #delete an specific item of the list
numbers.reverse()
print(numbers)
print(numbers + tasks)

numbers = [1,3,5,7,2]
numbers.sort()




