# Sample dictionary
data = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Sort by key
sorted_by_key = dict(sorted(data.items(), key=lambda item: item[0]))
print("Sorted by key:")
print(sorted_by_key)

# Sort by value
sorted_by_value = dict(sorted(data.items(), key=lambda item: item[1]))
print("\nSorted by value:")
print(sorted_by_value)




