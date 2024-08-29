shopping_list = {
    "piekarnia": ["chleb","bułki","pączki"],
    "warzywniak": ["marchew","seler","rukola"]
}

print("Lista zakupów:")
sum_of_products=0

for shop,product_list in shopping_list.items():
    product_list_updated = [product.title() for product in product_list]
    sum_of_products=sum_of_products+len(product_list)
    print(f"Idę do {shop.title()} i kupuję tam {product_list_updated}.")

print(f"W sumie kupuję {sum_of_products} produktów.")
print()
print("Cześć Maciek!")
print("Robię zmiany numer 2")