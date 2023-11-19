# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set or a string) (or a custom condition)


people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
# for person in people:
#     print(f'Current Person is {person}')



# Break (out of loop) - Starts around (1:01:01): https://youtu.be/JJmcL1N2KQs?si=DG6E2oUns6iylP4j&t=3661
for person in people: 
    if person == 'Sara':
        break
    print(f'Break Loop Person es: {person}')


# Continue (here, skip over Sara)
for person in people: 
    if person == 'Sara':
        continue
    print(f'Continue Loop Person is: {person}')


# Range
for i in range(len(people)):
    # print(people[i])
    print(f'Range Loop Person is: {people[i]}')

# Custom Range: here print numbers 0 to 10:
for i in range(0, 11):
    print(f'Number: {i}')



# While loops execute a set of statements as long as a condition is true.
# Started (1:04:13): https://youtu.be/JJmcL1N2KQs?si=eJ8wQb6kziIPo0MD&t=3853
count = 0
while count <= 10:
    print(f'Count in while loop is: {count}')
    count += 1

