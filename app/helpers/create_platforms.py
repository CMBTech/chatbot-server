"""command line utility to create a new platform"""
from app.models.platform import Platform


def create_platform(name,url,category_id):
    new_platform = Platform.find_first(**{'name': name})
    if new_platform:
        print(f'name {name} already in use')
        return

    new_platform = Platform(name=name, url=url, category_id=category_id)
    new_platform.save()
    print("Platform added successfuly is ", name)


