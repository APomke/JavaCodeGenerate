# 每个单词首字母大小
def word_first_letter_size(s):
    string = ""
    for i in s.split("_"):
        string += "".join(i.title())
    return string
