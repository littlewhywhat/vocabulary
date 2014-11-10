
def parseWords(string) :
    words = []
    results = [string]
    divideElemsBy(';', results)
    divideElemsByAND_COMA(results)
    length = len(results)
    for result in results :
        result = result.strip()
        if ' ' not in result and len(result) != 0  :
            words.append(result)
    return words 

def divideElemsBy(divider, elems) :
    length = len(elems)
    for i in range(0, length) :
        string = elems.pop()
        if divider in string :
            results = string.split(divider)
            for result in results :
                elems.insert(0, result)
        else :
            elems.insert(0, string)
            
def divideElemsByAND_COMA(elems) :
    length = len(elems)
    for i in range(0, length) :
        results = [elems.pop()]
        check = True
        divideElemsBy(',', results)
        divideElemsBy(' and ', results)
        for result in results :
            result = result.strip()
            if ' ' in result :
                check = False
        if check :
            for result in results :
                    elems.insert(0, result)
