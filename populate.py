from faker import Faker
from random import randint
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
import django
django.setup()


fake = Faker()

#
# def populate(value):
#     for i in range(value):
#         lid = randint(1000, 9999)
#         bname = fake.name()
#         mname = fake.email()
#         faddress = fake.address()
#
#         Laptop_records = Laptop.objects.get_or_create(c_id=fno, name=fname, email_id=femail, address=faddress)


def main():
    no = int(input("Enter the number of records do you want to add :"))
    populate(no)


if __name__ == '__main__':
    main()
