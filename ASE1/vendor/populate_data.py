from vendor.models import Category


def populate_categories():
    categories  = ['Home Needs', 'Groceries', 'Fruits/Veg', 'Beverages', 'Dairy', 'Personal care']
    for i in categories:
        c = Category(cat_name=i)
        c.save()
