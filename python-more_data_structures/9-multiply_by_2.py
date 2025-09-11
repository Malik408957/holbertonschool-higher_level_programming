#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Yeni dictionary yaradırıq
    new_dict = {}
    # Orijinal dictionary-dəki hər açar-dəyər cütlüyü üçün
    for key, value in a_dictionary.items():
        # Dəyəri 2-yə vurub yeni dictionary-ə əlavə edirik
        new_dict[key] = value * 2
    return new_dict
