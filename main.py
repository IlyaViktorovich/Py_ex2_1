def read_txt(file_name):

    cook_book = {}
    with open(file_name, encoding="utf-8") as file:
        cook_recipe = []
        #print(type(file)) cook_recipe = []
        for line in file:
            cook_recipe.append(line)
            number_recipe = int(file.readline())
            for numer_ingredients in range(number_recipe):
                res = file.readline().strip().strit(' | ')
                print(res)
                #print(type(file.readline()))
                #print(line_ingredients)
            file.readline()

    #print(cook_recipe)
    #return cook_book

read_txt('recipes.txt')