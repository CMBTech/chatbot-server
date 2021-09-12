"""command line utility to create a new category"""
from app.models.category import Category


def create_category():
    name = 'socials-platforms'
    new_category = Category.find_first(**{'name': name})
    if new_category:
        print(f'Category {name} already in use')
        return

    new_category = Category(name=name)
    new_category.save()
    print("Category added successfuly is ", name)


