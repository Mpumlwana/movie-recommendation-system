class PaymentProcessor:
    def process(self):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process(self):
        return "Processing credit card payment"


class PayPalProcessor(PaymentProcessor):
    def process(self):
        return "Processing PayPal payment"