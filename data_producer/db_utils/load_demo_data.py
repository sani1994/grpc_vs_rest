from db_helper import UserDB,User

DATA_SIZE = 10000


def creat_demo_data():
    User().create_table()
    for idx in range(DATA_SIZE):
        data = {
            "name": f"user {idx}",
            "username": f"user_{idx}",
            "phone_number": "01521202936",
            "email": f"user_{idx}@email.com"
        }
        UserDB().add_user(**data)


if __name__ == "__main__":
    creat_demo_data()
