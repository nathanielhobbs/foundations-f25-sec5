import random

# each of these choose uniformly at random.
print(f'random number between 0 and 1: {random.random()=}')
print(f'random integer between 0 and 100: {random.randint(0,100)=}')
print(f'random element from list: {random.choice(['a','b','c'])=}')


fair_die = random.choice([1,2,3,4,5,6])
# here is how to choose with a "weighted" die
print(f'{fair_die=}')

weighted_die = random.choices([1,2,3,4,5,6], weights=[1, 1, 1, 1, 1, 10])
print(f'{weighted_die=}')

weighted_die_many = random.choices([1,2,3,4,5,6], weights=[1, 1, 1, 1, 1, 10], k=10)
print(f'{weighted_die_many=}')




token_dict = {
"one": {"fish": 1},
"two": {"fish": 1},
"three": {"fish": 1},
"blue": {"fish": 1},
"fish": {".": 4, "two": 1, "him": 1}
}

word_after_fish = random.choices([".", "two", "him"], weights=[4,1,1])
# this is doing the same thing, but is more general (that's a good thing)
word_after_fish = random.choices(list(token_dict['fish'].keys()), weights=token_dict['fish'].values())

# get the actual word, not the list
word_after_fish = word_after_fish[0]
print(f'{word_after_fish=}')