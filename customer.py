# create a customer class
class Customer:
    def __init__(self, customer_name, email, payment_method):
        self.customer_name = customer_name
        self.email = email
        self.payment_method = payment_method
    def __str__(self) -> str:
        return f'Name: {self.customer_name}'
