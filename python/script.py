import thesaurus
import wordparser
import vocabularydb

from datetime import datetime

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
        words = wordparser.parseWords(string)
        for word in words :
            synonyms.append(word)

def main(date) :
    # Authenticate   
    USER = 'littlewhywhat@gmail.com'
    PWD = 'equilibrium'
    
    th = thesaurus.Thesaurus()
    th.login(USER, PWD)
    tree = th.getSynonyms()    
    
    # Get word graph
    wordgraph = getWordGraph(tree, date)
    print wordgraph

    # Connect to MySQL
    base = vocabularydb.Database()
    base.open()
    
    print 'was'
    base.storySoFar()
    
    # base.addGraph(wordgraph)

    print 'now'
    base.storySoFar()
    
    print len(wordgraph)
    base.close()

def test() :
    main(datetime(2014,10,1))

