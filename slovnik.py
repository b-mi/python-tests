slovnik = {}
food = {"ham": "yes", "eggs": "yes", "spam": "no"}
print(food)
food["yoghurt"] = "no"
print(food)

for k, v in food.items():
    print(f"{k} => {v}");

