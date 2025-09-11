#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Yeni list yaradırıq
    new_list = []
    # Orijinal listin hər elementini gəzirik
    for element in my_list:
        # Əgər element axtarılan elementdirsə, əvəz edirik
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
