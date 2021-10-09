from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='UTF8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
contacts_dict = {}
key_contact = contacts_list.pop(0)
for contact in contacts_list:
    FIO = [x.strip() for x in ' '.join(contact[:3]).split(' ', 2)]
    new_contact = FIO + contact[3:]
    key = ' '.join(FIO[:2])
    contacts_dict.setdefault(key, {i: None for i in key_contact})
    for index, value in enumerate(new_contact):
        if value and not contacts_dict[key][key_contact[index]]:
            contacts_dict[key][key_contact[index]] = value
        elif value and contacts_dict[key][key_contact[index]] != value:
            contacts_dict[key][key_contact[index]] += f';{value}'
    pattern = r'(\+7|8)?\s*\(?(\d+)\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})((\s*)\(?(доб\.)\s*(\d+)\)?)?'
    subst = r'+7(\2)\3-\4-\5\7\8\9'
    contacts_dict[key]['phone'] = re.sub(pattern, subst, contacts_dict[key]['phone'])
new_contacts_list = [key_contact]
for value in contacts_dict.values():
    new_contacts_list += [[value[i] for i in key_contact]]
pprint(new_contacts_list)
with open("phonebook.csv", "w", encoding='UTF8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
