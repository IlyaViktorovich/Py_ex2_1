def read_txt(file_name):
    cook_book = {}
    cook_list = []
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            cook_name = line.strip()
            cook_list.append(cook_name)
            number_recipe = int(file.readline().strip())
            ingrid = []
            for numer_ingredients in range(number_recipe):
                res = file.readline().strip().split(' | ')
                dich = {}
                dich['ingredient_name'] = res[0]
                dich['quantity'] = res[1]
                dich['measure'] = res[2]
                ingrid.append(dich)
            cook_book[cook_name] = ingrid
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
  dict = {}
  cook_book = read_txt('recipes.txt')
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
              quant = int(key2[key3])*person_count
          dict[name_ing] = doct
  return dict

#result = read_txt('recipes.txt')

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2 ))