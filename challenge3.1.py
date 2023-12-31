def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices

# Example usage:
product_list = ["Apple", "Banana", "Orange", "Banana", "Mango", "Banana"]
target = "Banana"
result = linear_search_product(product_list, target)

if result:
    print(f"The target product '{target}' was found at indices: {result}")
else:
    print(f"The target product '{target}' was not found.")
