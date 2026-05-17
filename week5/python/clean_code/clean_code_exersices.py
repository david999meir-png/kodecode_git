# exersice 1

# original code

def f(l):
    r = []
    for x in l:
        if x[1] >= 18 and x[2] == "active":
            r.append(x[0])
    return r

d = [
    ["Dan", 25, "active"],
    ["Noa", 16, "active"],
    ["Yael", 30, "inactive"],
]

print(f(d))


# clean code

def filter_users(user_list):
    filtered_list = []
    name_, age_, is_active = 0, 1, 2

    for user in user_list:
        if user[age_] >= 18 and user[is_active]:
            filtered_list.append(user[name_])
    return filtered_list

users_group1 = [
    ["Dan", 25, True],
    ["Noa", 16, True],
    ["Yael", 30, False],
]

print(filter_users(users_group1))

# exersice 2

# original code

def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not user_email:
        print("Invalid user")
        return None
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None

    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85

    stock -= quantity

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status


# clean code

def check_user(user_email=None) -> bool:
    return user_email


def check_quantity(quantity: int, stock: int) -> bool:
    return quantity > 0 and quantity < stock


def calculate_price(price: float, quantity: int) -> float:
    total_price = price * quantity
    if quantity >= 10:
        total_price *= 0.9
    elif quantity >= 50:
        total_price *= 0.85
    return total_price


def update_stock(stoke: int, quantity: int) -> int:
    return stoke - quantity


def main(email: str, product_name: str, product_price: float, stock: int, quantity: int):
    email_ = check_user(email)
    if not email:
        print("Invalid user")
        return None
    
    check_quantity_test = check_quantity(quantity, stock)
    if not check_quantity_test:
        print("Invalid quantity")
        return None
    
    order_status = "confirmed"
    total_price = calculate_price(product_price, quantity)
    updated_stock = update_stock(stock, quantity)

    print(f"Order {order_status}: {email_} bought {quantity}x {product_name} for ${total_price}")
    return  email, product_name, quantity, total_price, order_status , updated_stock



    


 
