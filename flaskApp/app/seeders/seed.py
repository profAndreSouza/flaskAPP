from flaskApp.app.models.user import User
from flaskApp.app import db
from faker import Faker

class Seeder:
    def __init__(self):
        self.fake = Faker()

    def run(self):
        if User.query.first():
            print("Dados já existem, pulando seed.")
            return

        print("Inserindo dados mockados...")
        users = []

        for _ in range(5):
            name = self.fake.first_name().lower()
            username = f"{name}{self.fake.random_int(100, 999)}"
            email = f"{username}@example.com"

            user = User(
                username=username,
                email=email
            )
            user.password = "123456"
            users.append(user)

        db.session.add_all(users)
        db.session.commit()
        print("Dados mockados inseridos.")
        print(users)
