# django-review
from charactercreator.models import *
from armory.models import *
# How many total Characters are there - 302
# SQL
SELECT COUNT(*) FROM charactercreator_character
# ORM
Get All Characters
    charactors = Character.objects.all()
    len(charactors) = 302

    # OR
    Character.objects.count()

# How many of each specific subclass?
# Cleric : 75
# SQL
SELECT COUNT(*) FROM charactercreator_cleric

# ORM
Get All Cleric Characters
    clerics = Cleric.objects.all()
    len(cleric) = 75

    # OR
    Cleric.objects.count()

# Mage: 108
# SQL
SELECT COUNT(*) FROM charactercreator_mage

# ORM
Get All Mage Characters
    mage = Mage.objects.all()
    len(mage) = 108

    # OR
    Mage.objects.count()

# Thief: 51
# SQL
SELECT COUNT(*) FROM charactercreator_thief

# ORM
Get All Thief Characters
    thief = Fighter.objects.all()
    len(thief) = 51

    # OR
    Thief.objects.count()

# Fighter: 68
# SQL
SELECT COUNT(*) FROM charactercreator_fighter

# ORM
Get All Fighter Characters
    fighter = Fighter.objects.all()
    len(fighter) = 68

    # OR
    Fighter.objects.count()

# necromancer: 11
# SQL
SELECT COUNT(*) FROM charactercreator_necromancer

# ORM
Get All Necromancer Characters
    necromancer = Necromancer.objects.all()
    len(necromancer) = 11

    # OR
    necromancer.objects.count()

# How many total Items - 174
# SQL
SELECT COUNT(*) FROM armory_item

# ORM
Get items
    items = Item.objects.all()
    len(Item) = 174

    # OR
    Item.objects.count()

# How many of the Items are weapons - 37
# SQL
SELECT COUNT(*) FROM armory_weapon

# ORM
Get Weapons
    weapons = Weapons.objects.all()
    len(weapons) = 37

    # OR
    Weapons.objects.count()

# How many are not - (174 - 37) - 137
# SQL
SELECT COUNT(*) FROM armory_item WHERE item_id < 138

# ORM
Get Not Weapons
    item - weapons = 137

    # OR
    Item.objects.filter(weapon=None).count()

# On average, how many Items does each Character have?
# SQL

# 898

# ORM
Get Average Item
    character = Character.objects.all()

    count = 0
    for char in character:
        count += char.inventory.count()

    avg item = count / items = 2.97 or 3

    # OR
    Character.objects.annotate(num_items=models.Count(
        'inventory')).aggregate(models.Avg('num_items'))

# On average, how many Weapons does each character have?

# ORM
Get Average Weapon
    count = 0
    for char in character:
        # needs to be checked ???
        count += char.inventory.count() - char.inventoryfilter(weapon=None).count()
    avg count / charactors

    # OR
    Character.objects.annotate(num_items=models.Count('inventory__weapon')).aggregate(models.Avg('num_items'))
