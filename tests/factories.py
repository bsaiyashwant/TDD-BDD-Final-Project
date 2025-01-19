from faker import Faker
fake = Faker()

def create_fake_product():
    return {
        "name": fake.word(),
        "category": fake.word(),
        "price": round(fake.random_number(digits=3), 2),
        "availability": fake.boolean()
    }
