contacts_dict = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}
def sort_contacts(contacts_dict):
  dict_copy=contacts_dict.copy()
  new_list= list(dict_copy)
  new_dict = new_list.sort()
  return new_dict

print(sort_contacts(contacts_dict))