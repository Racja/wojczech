with open("tekst_du.txt", 'r', encoding='utf8') as in_file:
    text_to_change = in_file.read()
    in_file.close()
words_to_change_list = {
            " i": " i_dz",
            " oraz": " i",
            " i_dz": " oraz",
            " nigdy": " prawie nigdy",
            " dlaczego": " czemu"}

for word in words_to_change_list:
    text_to_change = text_to_change.replace(word, words_to_change_list[word])

with open("wynik_zamiany.txt", "w") as o_file:
    o_file.write(text_to_change)
    o_file.close()
