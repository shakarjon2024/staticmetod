1
class Shop:
    shop_name = 'Tech Market'

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity


    def total_price(self):
        return f"{self.price} * {self.quantity}"


    @classmethod
    def change_shop_name(cls, new_name):
        cls.shop_name = new_name


    @staticmethod
    def is_valid_price(price):
        return price > 0

product1 = Shop("Laptop", 1000, 2)

print("Do'kon nomi:", Shop.shop_name)
print("Umumiy narx:", product1.total_price())


Shop.change_shop_name("Super Tech")
print("Yangi do'kon nomi:", Shop.shop_name)


print("Narx to'g'rimi?", Shop.is_valid_price(500))
print("Narx to'g'rimi?", Shop.is_valid_price(-10))





# 2
class Student:
    passing_score = 60

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= Student.passing_score

    @classmethod
    def change_passing_score(cls, new_score):
        cls.passing_score = new_score
        print(f"O'tish balli {new_score} ga o'zgartirildi.")

    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

print(Student.is_valid_score(85))
s1 = Student("Ali", 55)
print(s1.is_passed())

Student.change_passing_score(50)
print(s1.is_passed())





# 3
class BankCard:
    bank_name = "AgroBank"

    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Muvaffaqiyatli! Yangi balans: {self.balance}"
        else:
            return "Mablag' yetarli emas!"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank nomi {new_name} ga yangilandi.")

    @staticmethod
    def is_valid_card_number(number):
        return len(str(number)) == 16

# Tekshirish:
card = BankCard(8600123456789012, 100000)
print(card.withdraw(40000)) 
print(BankCard.is_valid_card_number(86001234))
BankCard.change_bank_name("Milliy Bank")
