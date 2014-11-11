import requests
import wordgraph

class Thesaurus():
    def login(self, user, password):
        URL = 'http://app.dictionary.com/login'
        SOURCE = 'header_thes'
        LOGINDEST = 'http://www.thesaurus.com'
        self.session = self.getSession(URL, user, password, SOURCE, LOGINDEST)

    def getSession(self, URL, user, pwd, source, logindest) :
        session = requests.session()
        login_data = { 'source' : source,
                   'logindest' : logindest,
                   'username' : user,
                   'password' : pwd
                   }
        print session.post(URL, data=login_data)
        return session

    def getSynonyms(self, date) :
        URL = 'http://www.thesaurus.com/my-synonyms'
        request = self.session.get(URL)
        graph = wordgraph.get(request.text, date)
        return graph

