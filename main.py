class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0
        self.is_gift_wrapped = False

    def calculate_total(self):
        return self.quantity * self.price

    def apply_discount(self, total_quantity):
        if self.quantity > 10:
            discount_percentage = 0.05 if self.quantity <= 20 else 0.1
            return self.calculate_total() * discount_percentage
        return 0

    def apply_tiered_discount(self, total_quantity):
        if total_quantity > 30 and self.quantity > 15:
            discounted_quantity = self.quantity - 15
            return self.calculate_total(discounted_quantity) * 0.5
        return 0


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.subtotal = 0

    def add_product(self, product):
        self.products.append(product)
        self.subtotal += product.calculate_total()

    def apply_discount(self):
        total_quantity = sum(product.quantity for product in self.products)
        discounts = {
            'flat_10_discount': 10 if self.subtotal > 200 else 0,
            'bulk_5_discount': max(product.apply_discount(total_quantity) for product in self.products),
            'bulk_10_discount': 10 if total_quantity > 20 else 0,
            'tiered_50_discount': max(product.apply_tiered_discount(total_quantity) for product in self.products),
        }
        best_discount = max(discounts, key=discounts.get)
        return best_discount, discounts[best_discount]


def main():
    product_a = Product("Product A", 20)
    product_b = Product("Product B", 40)
    product_c = Product("Product C", 50)

    cart = ShoppingCart()

    for product in [product_a, product_b, product_c]:
        product.quantity = int(input(f"Enter quantity for {product.name}: "))
        product.is_gift_wrapped = input(f"Is {product.name} wrapped as a gift? (yes/no): ").lower() == 'yes'
        cart.add_product(product)

    discount_name, discount_amount = cart.apply_discount()

    shipping_fee = (sum(product.quantity for product in cart.products) // 10) * 5
    gift_wrap_fee = sum(1 for product in cart.products if product.is_gift_wrapped)

    total = cart.subtotal - discount_amount + shipping_fee + gift_wrap_fee

    # Output details
    for product in cart.products:
        print(f"{product.name}: Quantity: {product.quantity}, Total: ${product.calculate_total()}")

    print(f"\nSubtotal: ${cart.subtotal}")
    print(f"Discount Applied: {discount_name}, Amount: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"\nTotal: ${total}")


if __name__ == "__main__":
    main()
