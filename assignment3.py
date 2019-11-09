#data structures assignment
persons = [
    {
        'name':'bob',
        'age': 18,
        'hobbies':['baseball','football']
    },
    {
        'name':'julia',
        'age':44,
        'hoobies':['book','cooking']
    }
]

person_names = [person['name'] for person in persons]
print(persons)
print(person_names)

are_older = all([person['age'] > 20 for person in persons ])
print(are_older)

#persons_copy = persons[:]
persons_copy = [person.copy() for person in persons]

persons_copy[0]['name'] = 'Max'

print(persons_copy[0]['name'])
print(persons[0]['name'])

p1, p2, p3 = persons
print(p1)
print(p2)
print(p3)


