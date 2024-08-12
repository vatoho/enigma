ListZamen = {
    'а':'а',
    'б':'б',
    'в':'в',
    'г':'г',
    'д':'д',
    'е':'е',
    'ё':'ё',
    'ж':'ж',
    'з':'з',
    'и':'и',
    'й':'й',
    'к':'к',
    'л':'л',
    'м':'м',
    'н':'н',
    'о':'о',
    'п':'п',
    'р':'р',
    'с':'с',
    'т':'т',
    'у':'у',
    'ф':'ф',
    'х':'х',
    'ц':'ц',
    'ч':'ч',
    'ш':'ш',
    'щ':'щ',
    'ъ':'ъ',
    'ы':'ы',
    'ь':'ь',
    'э':'э',
    'ю':'ю',
    'я':'я',
    ' ':' '
}


def EnigmaInput():
    InputText = input("Введите текст:")
    result = list(InputText)
    return result


def CommPanel(InputList, ListZamen):
    OutputList = []
    for i in range(len(InputList)):
        InputSymbol = InputList[i]
        OutputList.append(ListZamen[InputSymbol])
    return OutputList


def rotors(InputList):
    


print(CommPanel(EnigmaInput(), ListZamen))