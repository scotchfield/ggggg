import random

def getWord():
    return 'g' * random.randint( 1, 12 )

def getShortSentence():
    st = getWord().capitalize()
    for i in range( random.randint( 1, 2 ) ):
        st = '{0} {1}'.format( st, getWord() )
    return st

def getSentence():
    st = getWord().capitalize()
    for i in range( random.randint( 1, 15 ) ):
        st = '{0} {1}'.format( st, getWord() )
    if random.randint( 1, 20 ) == 1:
        st = '"{0}."'.format( st )
    else:
        st = '{0}.'.format( st )
    return st

def getName():
    obj = []
    for i in range( random.randint( 2, 3 ) ):
        obj.append( getWord().capitalize() )
    return ' '.join( obj )

def getParagraph():
    st = getSentence()
    for i in range( random.randint( 0, 13 ) ):
        s = getSentence()
        st = '{0} {1}'.format( st, s )

    return '{0}\n\n'.format( st )

def getChapter( chapter ):
    st = '{0}.\n\n{1}'.format( chapter, getParagraph() )
    for i in range( random.randint( 12, 45 ) ):
        st = '{0}{1}'.format( st, getParagraph() )
    return st

def getBookObj( chapters ):
    obj = []
    for i in range( chapters ):
        obj.append( getChapter( i + 1 ) )
    return obj

def getBook( chapters ):
    book_obj = getBookObj( chapters )
    return "\n\n".join( book_obj )

print( getBook( 50 ) )
