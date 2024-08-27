shopping_list = {
    "piekarnia": ["chleb","bułki","pączki"],
    "warzywniak": ["marchew","seler","rukola"]
}

print("Lista zakupów:")

for shop,product_list in shopping_list.items():
    product_list_updated = [product.title() for product in product_list]
    print(f"Idę do {shop.title()} i kupuję tam {product_list_updated}.")