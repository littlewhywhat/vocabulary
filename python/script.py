import thesaurus
import vocabularydb
from datetime import datetime

def main(date) :
    # Authenticate   
    USER = 'littlewhywhat@gmail.com'
    PWD = 'equilibrium'
    
    th = thesaurus.Thesaurus()
    th.login(USER, PWD)
    wordgraph = th.getSynonyms(date)    
    
    # Get word graph
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

