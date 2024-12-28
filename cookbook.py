import pprint

cook_book = {}
pp = pprint.PrettyPrinter(indent=1)

# получение словаря со списком блюд в качестве ключа и
# список ингредиентов для его приготовления в качестве значений
with open('reciptes.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        if not line.strip().isdigit() and '|' not in line and line != '\n':
            recipt_name = line.strip()
            if recipt_name not in cook_book:
                cook_book[recipt_name] = []
        elif line.strip().isdigit() and '|' not in line and line != '\n':
            continue
        elif line != '\n':
            ingredient, quantity, measure = line.strip().split("|")
            cook_book[recipt_name].append({'ingredient_name': ingredient.strip(), 'quantity': quantity.strip(), 'measure': measure.strip()})


def get_shop_list_by_dishes(dishes, person_count):
    """
    Функция для формирования словаря с названием ингредиентов и их количества для выбранных блюд.
    :param dishes: Список наименований блюд
    :param person_count: Количество персон
    :return: Словарь со списком ингредиентов
    """
    recipt={}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]

            for ingr in ingredients:
                name_ = ingr['ingredient_name']
                qty = int(ingr['quantity'])
                msr = ingr['measure']

                if name_ not in recipt:
                    recipt[name_] = {'quantity': 0, 'measure': str()}

                recipt[name_]['quantity'] += qty*person_count
                recipt[name_]['measure'] = msr
        else:
            print(f'Блюда {dish} нет в кулинарной книге!\n')
            continue

    return recipt

pp.pprint(cook_book)
print('\n'*3)
pp.pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))