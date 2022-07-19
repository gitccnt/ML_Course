students = {'Ivan'  : 5.00,
            'Alex'  : 3.50,
            'Maria' : 5.50,
            'Georgy': 5.00}

for key, val in students.items():
    if val > 4.00:
        print(key,f'{val:.2f}')


text = '''
       apple and banana one apple one banana
       a red apple and a green apple
       '''

print('\n')
print('\n')


words_list = text.split()
new_set = set(sorted(words_list, key=len, reverse=False))

for x in new_set:
    print(x,words_list.count(x))
 
test = {'Ivan'  : 5.00,
        'Alex'  : 3.50,
        'Maria' : 5.50,
        'Georgy': 5.00}
