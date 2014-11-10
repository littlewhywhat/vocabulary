import unittest
import wordparser

class TestParseWords(unittest.TestCase):

    def setUp(self):
        self.SPACE = ' '
        self.AND = ' and '
        self.COMMA = ', '
        self.SEMICOLON = '; '
        self.ADD = 'add'
        self.STRONG = 'strong'
        self.SECURE = 'secure'
        self.LAND = 'land'
    def test_ONEWORD(self):
        print "\n"
        print "test_ONEWORD"
        
        string = self.ADD
        check = [self.ADD]
        self.check(string, check)
    # each divider
    def test_AND(self):
        print "\n"
        print "test_AND"
        
        string = self.ADD + self.AND + self.STRONG
        check = [self.ADD, self.STRONG]
        self.check(string, check)
        string += self.AND + self.SECURE
        check.append(self.SECURE)
        self.check(string, check)
    def test_COMMA(self):
        print "\n"
        print "test_COMMA"
        
        string = self.ADD + self.COMMA + self.STRONG
        check = [self.ADD, self.STRONG]
        self.check(string, check)
        string += self.COMMA + self.SECURE
        check.append(self.SECURE)
        self.check(string, check)
    def test_SEMICOLON(self):
        print "\n"
        print "test_SEMICOLON"
        
        string = self.ADD + self.SEMICOLON + self.STRONG
        check = [self.ADD, self.STRONG]
        self.check(string, check)
        string += self.SEMICOLON + self.SECURE
        check.append(self.SECURE)
        self.check(string, check)
    # each combination of dividers
    def test_AND_COMMA(self):
        print "\n"
        print "test_AND_COMMA"
        
        string = self.ADD + self.AND + self.STRONG
        string += self.COMMA + self.SECURE
        check = [self.ADD, self.STRONG, self.SECURE]
        self.check(string, check)
    def test_AND_SEMICOLON(self):
        print "\n"
        print "test_AND_SEMICOLON"
        
        string = self.ADD + self.AND + self.STRONG
        string += self.SEMICOLON + self.SECURE
        check = [self.ADD, self.STRONG, self.SECURE]
        self.check(string, check)
    def test_COMMA_SEMICOLON(self):
        print "\n"
        print "test_COMMA_SEMICOLON"
        
        string = self.ADD + self.COMMA + self.STRONG
        string += self.SEMICOLON + self.SECURE
        check = [self.ADD, self.STRONG, self.SECURE]
        self.check(string, check)
    def test_COMMA_SEMICOLON_AND(self):
        print "\n"
        print "test_COMMA_SEMICOLON_AND"
        
        string = self.ADD + self.COMMA + self.STRONG
        string += self.SEMICOLON + self.SECURE
        string += self.AND + self.LAND
        check = [self.ADD, self.STRONG, self.SECURE, self.LAND]
        self.check(string, check)
    # each divider with space
    def test_SEMICOLON_SPACE(self):
        print "\n"
        print "test_SEMICOLON_SPACE"
        
        string = self.ADD + self.SPACE + self.STRONG
        string += self.SEMICOLON + self.SECURE
        check = [self.SECURE]
        self.check(string, check)
    def test_COMA_SPACE(self):
        print "\n"
        print "test_COMMA_SPACE"

        string = self.ADD + self.SPACE + self.STRONG
        string += self.COMMA + self.SECURE
        check = []
        self.check(string, check)
    def test_AND_SPACE(self):
        print "\n"
        print "test_AND_SPACE"
        
        string = self.ADD + self.SPACE + self.STRONG
        string += self.AND + self.SECURE
        check = []
        self.check(string, check)
    # each combination of dividers with space
    def test_AND_COMMA_SPACE(self):
        print "\n"
        print "test_AND_COMMA_SPACE"
        
        string = self.ADD + self.SPACE + self.LAND 
        string += self.AND + self.STRONG
        string += self.COMMA + self.SECURE
        check = []
        self.check(string, check)
        string = self.ADD + self.AND + self.STRONG
        string += self.COMMA + self.SECURE
        string += self.SPACE + self.LAND 
        check = []
        self.check(string, check)
    def test_AND_SEMICOLON_SPACE(self):
        print "\n"
        print "test_AND_SEMICOLON_SPACE"
        
        string = self.ADD + self.SPACE + self.LAND 
        string += self.AND + self.STRONG
        string += self.SEMICOLON + self.SECURE
        check = [self.SECURE]
        self.check(string, check)
        string = self.ADD + self.AND + self.STRONG
        string += self.SEMICOLON + self.SECURE
        string += self.SPACE + self.LAND 
        check = [self.ADD, self.STRONG]
        self.check(string, check)
    def test_COMMA_SEMICOLON_SPACE(self):
        print "\n"
        print "test_COMMA_SEMICOLON_SPACE"
        
        string = self.ADD + self.SPACE + self.LAND 
        string += self.COMMA + self.STRONG
        string += self.SEMICOLON + self.SECURE
        check = [self.SECURE]
        self.check(string, check)
        string = self.ADD + self.COMMA + self.STRONG
        string += self.SEMICOLON + self.SECURE
        string += self.SPACE + self.LAND 
        check = [self.ADD, self.STRONG]
        self.check(string, check)
    def test_COMMA_SEMICOLON_AND_SPACE(self):
        print "\n"
        print "test_COMMA_SEMICOLON_AND_SPACE"
        
        string = self.ADD + self.COMMA + self.STRONG
        string += self.SPACE + self.LAND 
        string += self.SEMICOLON + self.SECURE
        string += self.AND + self.LAND
        check = [self.SECURE, self.LAND]
        self.check(string, check)
        string = self.ADD + self.COMMA + self.STRONG
        string += self.SEMICOLON + self.SECURE
        string += self.SPACE + self.LAND 
        string += self.AND + self.LAND
        check = [self.ADD, self.STRONG]
        self.check(string, check)

    def check(self, string, check):
        results = wordparser.parseWords(string)
        print string , check , results
        self.assertEquals(len(results), len(check))
        for result in results :
            self.assertEquals(True, result in check)

if __name__ == '__main__':
    unittest.main()