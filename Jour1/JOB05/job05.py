import string


def listAlphabet():
    return list(string.ascii_letters)

alphabet_list = listAlphabet()
alphabet_list.reverse()

print(alphabet_list)