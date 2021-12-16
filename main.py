
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
  dict = {}
  for key in cook_book:
    for name_cook in dishes:
      if key == name_cook:
        for key2 in cook_book[key]:
          doct = {}
          for key3 in key2:
            if key3 == 'ingredient_name':
              name_ing = key2[key3]
            elif key3 == 'measure':
              meas = key2[key3]
              doct["measure"] = meas
              doct['quantity'] = quant
            elif key3 == 'quantity':
              quant = key2[key3]*person_count
          dict[name_ing] = doct
  return dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2 ))
