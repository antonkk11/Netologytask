def getdictionary(file):
    with open(file) as f:
        data = f.read()

    data = data.splitlines()
    numbers = [0]
    indices = [i for i, x in enumerate(data) if x == '']
    numbers = numbers + indices
    numbers.append(len(data))
    dictionary = {}

    for n in range(len(numbers) - 1):
        ingredients = []
        if n == 0:
            set_recipe = data[numbers[n]:numbers[n+1]]
        else:
            set_recipe = data[numbers[n]+1:numbers[n+1]]

        for number in range(2,len(set_recipe)):
            temporary_set = set_recipe[number].split(' | ')
            temporary = {'ingredient_name': temporary_set[0],
                         'quantity': int(temporary_set[1]), 'measure': temporary_set[2]}
            ingredients.append(temporary)

        dictionary.setdefault(set_recipe[0], ingredients)
    return dictionary

# cookbook = getdictionary('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    for dish in dishes:
        for ingredient in cookbook[dish]:
            if ingredient['ingredient_name'] not in ingredients_dict.keys():
                temporary_dict = {'measure': ingredient['measure'],
                                  'quantity': ingredient['quantity'] * person_count}
                ingredients_dict.setdefault(ingredient['ingredient_name'], temporary_dict)
            else:
                name = ingredient['ingredient_name']
                previous_quantity = ingredients_dict[name]['quantity']
                temporary_dict = {'measure': ingredient['measure'],
                                  'quantity': ingredient['quantity'] * person_count + previous_quantity}
                ingredients_dict[name] = temporary_dict

    return ingredients_dict

# dishes = ['Омлет', 'Фахитос']
# ingredients = get_shop_list_by_dishes(dishes, 4)
#
name_files = ['1.txt', '2.txt', '3.txt']

def append_file(set_files):
    file_dict = {}
    set_length = []
    for file_name in set_files:
        with open(file_name) as f:
            data = f.read()
            q_string =len(data.splitlines())
            set_length.append(q_string)
            temporary_dict = {'name': file_name, 'data': data}
            file_dict.setdefault(q_string, temporary_dict)
    with open('result.txt', 'w') as f:
        for length in sorted(set_length):
            f.write(file_dict[length]['name']+ '\n')
            f.write(str(length) + '\n')
            f.write(file_dict[length]['data']+ '\n')
            f.write('\n')

append_file(name_files)






