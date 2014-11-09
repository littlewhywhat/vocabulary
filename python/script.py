import MySQLdb
import requests
from datetime import datetime
from lxml import html

def getSession(URL, user, pwd, source, logindest) :
    session = requests.session()
    login_data = { 'source' : source,
               'logindest' : logindest,
               'username' : user,
               'password' : pwd
               }
    print session.post(URL, data=login_data)
    return session

def getWordGraph(tree, date) :
    graph = {}
    for headword in tree.xpath('//div[@class="headword"]') :
        header = headword.xpath('.//h2')[0]
        datestr = header.get('data-update')
        headdate = datetime.strptime(datestr, '%Y-%m-%d %X')
        if (headdate > date) :
          word = getFromHeader(header)
          synonyms = []
          for ul in headword.xpath('.//ul') :
            appendFromUL(ul, synonyms)
          contents = headword.xpath('.//div[@class="content"]')
          appendFromContent(contents, synonyms)
          graph[word] = synonyms
    return graph

def getFromHeader(header) :
    return header.xpath('.//a')[0].text.strip()

def appendFromUL(ul, synonyms) :
    for synonym in ul.xpath('.//li/a') :
        synonyms.append(synonym.text.strip())

def appendFromContent(contents, synonyms) :
    for content in contents :
        string = content.xpath('.//strong')[0].text.strip()
        words = parseWords(string)
        for word in words :
            synonyms.append(word)

def storySoFar(cur) :
    cur.execute('SELECT * FROM a ORDER BY id DESC LIMIT 5')
    for row in cur.fetchall() :
       print row
    cur.execute('SELECT * FROM words ORDER BY id DESC LIMIT 5')
    for row in cur.fetchall() :
       print row

def addGraphToDB(db, cur, wordgraph) :
    try:
        for word, synonyms in wordgraph.items() :
            for synonym in synonyms :
                 cur.callproc('insertAWW', (word, synonym, 0 , 0))
        db.commit()
    except:
        db.rollback

def main(date) :
    # Authenticate
    URL = 'http://app.dictionary.com/login'
    USER = 'littlewhywhat@gmail.com'
    PWD = 'equilibrium'
    SOURCE = 'header_thes'
    LOGINDEST = 'http://www.thesaurus.com'
    session = getSession(URL, USER, PWD, SOURCE, LOGINDEST)
    
    # Access a page that requires you to be logged in
    request = session.get('http://www.thesaurus.com/my-synonyms')
    tree = html.fromstring(request.text)
    
    # Get word graph
    wordgraph = getWordGraph(tree, date)
    
    # Connect to MySQL
    HOST = '127.0.0.1'
    USER = 'root'
    PWD = 'vocabulary'
    DB = 'vocabulary'
    
    db = MySQLdb.connect(host=HOST, user=USER, passwd=PWD, db=DB)
    cur = db.cursor()
    
    print 'was'
    storySoFar(cur)
    
    addGraphToDB(db, cur, wordgraph)
    
    print 'now'
    storySoFar(cur)

    # print wordgraph['brisk']
    # print wordgraph['combustible']
    # print wordgraph['augment']
    # print wordgraph['analyze']
    print len(wordgraph)
    cur.close()
    db.close()

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

def test() :
    main(datetime(2014,0,0))

