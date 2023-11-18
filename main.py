class Product:
    def __init__(self, name, quantity, unit_price, gst):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.gst = gst

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity}, Unit Price: {self.unit_price}, GST: {self.gst}%)"

    def calculate_total(self):
        return self.quantity * self.unit_price * (1 + self.gst / 100)

    

leather_wallet = Product("Leather wallet", 2, 1100, 12)
umbrella = Product("Umbrella", 12, 900, 28)
cigarette = Product("Cigarette", 28, 200, 3)
honey = Product("Honey", 3, 100, 2)

basket = {
    "Leather wallet": leather_wallet,
    "Umbrella": umbrella,
    "Cigarette": cigarette,
    "Honey": honey
}

max_gst = 0
max_product = ""
for productname, product in basket.items():
    if product.gst > max_gst:
        max_gst = product.gst
        max_product = productname
print(f"Product with maximum GST: {max_product}")

total_amount = sum(product.calculate_total() for product in basket.values())
print(f"Total amount to be paid: Rs. {total_amount}")
