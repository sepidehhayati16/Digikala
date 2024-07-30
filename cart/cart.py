from shop.models import  Product
from decimal import Decimal

class Cart:
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart
    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = product_qty
        self.session.modified = True

    def __len__(self):
        return len(self.cart)


    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def get_total(self):
        product_ids = map(int, self.cart.keys())  # تبدیل کلیدها به اعداد صحیح
        products = Product.objects.filter(id__in=product_ids)

        total = Decimal(0)
        product_dict = {product.id: product for product in products}  # تبدیل لیست محصولات به دیکشنری

        for key, value in self.cart.items():
            product = product_dict.get(int(key))
            if product:
                quantity = Decimal(value)
                if product.is_sale:
                    total += Decimal(product.sale_price) * quantity
                else:
                    total += Decimal(product.price) * quantity

        return total


    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True

        doc = self.cart
        return doc

    def delete(self,product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

