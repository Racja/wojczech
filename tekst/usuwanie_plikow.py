with open("tekst_du.txt", 'r', encoding='utf8') as in_file:
    text_to_delete = in_file.read()
    in_file.close()
word__delete_list = [" się", " i", " oraz", " nigdy", " dlaczego"]

for word in word__delete_list:
    text_to_delete = text_to_delete.replace(word, "")

with open("wynik_usuwania.txt", "w") as o_file:
    o_file.write(text_to_delete)
    o_file.close()
