import json
head_dict_together = {}
head_dict_separately = {}
lst_of_words_together = list()
json_lst = list()
lst_of_words_separately = list()


for one_two in range(1, 3):
    with open(f"ws{one_two}.txt", encoding="utf-8") as file:
        lst_of_words_together.extend([w[0:one_two] + "_" + w.rstrip(",\n")[one_two:] for i in file for w in i.split(", ")])
head_dict_together.update({0: lst_of_words_together}) # 1 - раздельно 0 - слитно

with open("bd.json", "w", encoding="utf-8") as file:
    json_lst.append(head_dict_together)
    json.dump(json_lst, file, ensure_ascii=False, indent=2)

with open("wr.txt", encoding="utf-8") as file:
    lst_of_words_separately.extend([w.split()[0] + "_" + w.rstrip(",\n").split()[1] for i in file for w in i.split(", ")])
head_dict_separately.update({1: lst_of_words_separately})
with open("bd.json", "w", encoding="utf-8") as file:
    json_lst.append(head_dict_separately)
    json.dump(json_lst, file, ensure_ascii=False, indent=2)
