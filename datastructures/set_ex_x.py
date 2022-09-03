dry_fruits = {'dates','almond','walnut','cashew'}
fruits = {'mango','banana','apple','pomegrenate'}

all_fruits = dry_fruits | fruits

print(all_fruits)
print(fruits)
print(dry_fruits)

ans = dry_fruits.isdisjoint(fruits)
print(ans)

ans = dry_fruits.issubset(all_fruits)
print("dry fruit is subset of all fruits:", ans)

ans = fruits.issuperset({'apple','banana'})
print("fruits is superset of {apple, banana}:", ans)