def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices
products = ['ball', 'bat', 'net', 'ball', 'pin']
target_product = 'ball'
result = linear_search_product(products, target_product)
print(result)