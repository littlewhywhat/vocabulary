
def parseWords(string) :
    words = []
    results = [string]
    divideElemsBy(',', results)
    divideElemsBy(';', results)
    divideElemsBy(' and ', results)
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
            check = True
            if divider != ';' :
                for result in results :
                    result = result.strip()
                    # print result
                    if ' ' in result:
                        check = False
            if check :
                elems[len(elems) :] = results
            else :
                elems.insert(0, string)
        else :
            elems.insert(0, string)
    # print elems
