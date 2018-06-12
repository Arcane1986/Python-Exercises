contacts_dict = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}
def sort_contacts(contacts_dict):
  new_list=[]
  contacts_dict_copy=contacts_dict.copy()
  for name,data in contacts_dict_copy.items():
    (phone,email)=data
    new_list.append((name,phone,email))
  new_list.sort(key = lambda name:name[0])
  return new_list

print(sort_contacts(contacts_dict))