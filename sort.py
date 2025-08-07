# Selection Sort to sort favorite foods by name length

def selection_sort_by_length(food_list):
    n = len(food_list)
    for i in range(n):
        # Assume the current item is the minimum
        min_index = i
        for j in range(i + 1, n):
            if len(food_list[j]) < len(food_list[min_index]):
                min_index = j
        # Swap the found minimum with the current item
        food_list[i], food_list[min_index] = food_list[min_index], food_list[i]
    return food_list


# My favorite foods
favorite_foods = ["Biryani", "Pizza", "Masala Dosa", "Burger", "Pani puri", "mandhi", "meals"]


sorted_foods = selection_sort_by_length(favorite_foods)


print("Favorite foods sorted by name length (short to long):")
for food in sorted_foods:
    print(food)

