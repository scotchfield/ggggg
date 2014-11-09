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
    return '{0}.'.format( st )

def getName():
    obj = []
    for i in range( random.randint( 2, 3 ) ):
        obj.append( getWord().capitalize() )
    return ' '.join( obj )

def getParagraph( bib_count ):
    st = getSentence()
    for i in range( random.randint( 0, 8 ) ):
        s = getSentence()
        if bib_count > 0 and random.randint( 1, 20 ) == 1:
            s = '{0} \\cite{{g{1}}}.'.format( s[:-1],
                                              random.randint( 1, bib_count ) )
        elif bib_count > 0 and random.randint( 1, 25 ) == 1:
            s = '{0} \\footnote{{{1}}}.'.format( s[:-1], getSentence() )
        st = '{0}  {1}'.format( st, s )

    return '{0}\n\n'.format( st )

def getSection( bib_count ):
    st = '\section{{{0}}}\n\n{1}'.format( getWord(),
                                          getParagraph( bib_count ) )
    for i in range( random.randint( 12, 22 ) ):
        st = '{0}{1}'.format( st, getParagraph( bib_count ) )
    if random.randint( 1, 2 ) == 1:
        st = '{0}\n\n{1}'.format( st, getFigure() )
    return st

def getEmail():
    return '{0}@{1}.ggg'.format( getWord(), getWord() )

def getAuthors():
    obj = []
    for i in range( random.randint( 1, 3 ) ):
        obj.append( '''\IEEEauthorblockN{{{0}}}
\IEEEauthorblockA{{{1}\\\\
{2}\\\\
{3}\\\\
{4}}}
'''.format( getName(), getName(), getName(), getName(), getEmail() ) )
    return '\n\\and\n'.join( obj )

def getFigure():
    g = []
    for i in range( random.randint( 1, 8 ) ):
        g.append( getWord().capitalize() )
    st = '''\\begin{{figure}}[tb]
\\centering
\\huge
{0}
\\caption{{{1}}}
\\end{{figure}}'''.format('\\\\\n'.join( g ), getParagraph( 0 ).strip() )
    return st

def getBibliography():
    n = random.randint( 12, 25 )
    st = '\\begin{thebibliography}{9}'
    for i in range( n ):
        st = '{0}\n\n\\bibitem{{g{1}}} {2}, \\emph{{{3}}}, {4}, {5}, {6}.'.format(
                 st, i, getName(), getSentence()[:-1], getName(),
                 getWord().capitalize(), getWord().capitalize() )
    st = '{0}\n\n\\end{{thebibliography}}\n'.format( st )
    return ( st, n )

def getPaper():
    bib = getBibliography()
    st = '''
\\documentclass[conference]{{IEEEtran}}
\\begin{{document}}
\\title{{{0}}}
\\author{{
{1}
}}
\\maketitle
\\renewcommand{{\\refname}}{{Gggggggggg}}
\\renewcommand{{\\abstractname}}{{Gggggggg}}
\\renewcommand{{\\figurename}}{{G.}}
\\begin{{abstract}}
{2}
\\end{{abstract}}
'''.format( getSentence()[:-1], getAuthors(), getParagraph( 0 ) )
    for i in range( 8, 11 ):
        st = '{0}\n\n{1}'.format( st, getSection( bib[ 1 ] ) )
    st = '{0}\n\n{1}'.format( st, bib[ 0 ] )
    return '{0}\n\n\\end{{document}}'.format( st )

print( getPaper() )
