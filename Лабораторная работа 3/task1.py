def find_index(product_list, target_product):
    if target_product in product_list:
        return product_list.index(target_product)
    return None


print(find_index(['яблоко', 'груша', 'банан', 'апельсин', 'груша'], 'груша'))
print(find_index(['яблоко', 'груша', 'апельсин', 'груша'], 'банан'))
print(find_index(['яблоко', 'груша', 'банан', 'апельсин', 'груша', 'апельсин'], 'апельсин'))
print(find_index([], 'яблоко'))
