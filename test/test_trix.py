from rdflib.graph import ConjunctiveGraph
import unittest


class TriXTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAperture(self): 

        g=ConjunctiveGraph()

        g.parse("test/trix/aperture.trix",format="trix")

        c=list(g.contexts())

        #print list(g.contexts())
        t=sum(map(lambda x: len(g.get_context(x)),g.contexts()))

        self.assertEquals(t,24)
        self.assertEquals(len(c),4)
        
        #print "Parsed %d triples"%t

    testAperture.known_issue = True

    def testSpec(self): 

        g=ConjunctiveGraph()
        
        g.parse("test/trix/nokia_example.trix",format="trix")
        
        #print "Parsed %d triples"%len(g)
        

if __name__=='__main__':
    unittest.main()
                          