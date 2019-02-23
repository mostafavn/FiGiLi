import random, sys, os
try:
    import pyfiglet
except ImportError:
    fig = input('You Need to Install pyfiglet Library. Continue?[Y/N]: ')
    if fig == 'Y' or fig == 'y' or fig == '':
        os.system('pip install pyfiglet')
    else:
        sys.exit()
try:
    from colored import fg, attr
except ImportError:
    col = input('You Need to Install colored Library. Continue?[Y/N]: ')
    if col == 'Y' or col == 'y' or col == '':
        os.system('pip install colored')
    else:
        sys.exit()

os.system('clear')

if sys.argv[-1] != sys.argv[0]:
    text = sys.argv[1]
else:
    text = input('%s%s Enter Your Text: %s%s'%(fg('white'), attr('bold'), attr('reset'), fg('light_slate_grey')))

font = input('%s%s Enter Your font [prees ENTER to random font]: %s%s'%(fg('white'), attr('bold'), attr('reset'), fg('light_slate_grey')))

os.system('clear')

if font == '':
    randFont = ['3-d','3x5','5lineoblique','acrobatic','alligator','alligator2','alphabet','avatar','banner','banner3-D','banner3',' banner4','barbwire','basic','bell','big','bigchief','binary','bubble','bulbhead','calgphy2','caligraphy','catwalk','chunky','coinstak','colossal','compute','contessa','contrast','cosmic','cosmike','cricket','cyberlarge','cybermedium','cybersmall','digital','doh','doom','dotmatrix','drpepper','eftichess','eftifont','eftipiti','eftirobot','eftitalic','eftiwall','eftiwater','epic','fender','fourtops','fuzzy','goofy','gothic','graffiti','hollywood','invita','isometric1','isometric2','isometric3','isometric4','italic','ivrit','jazmine',' jerusalem','katakana','kban','larry3d','lcd','lean','letters','linux','lockergnome','madrid','marquee','maxfour','mike','mini',' mirror','mnemonic','morse','moscow','nancyj-fancy','nancyj-underlined','nancyj','nipples','ntgreek','o8','ogre','pawp',' peaks','pebbles','pepper','poison','puffy','pyramid','rectangles','relief','relief2','rev','roman','rot13','rounded','rowancap','rozzo','runic','runyc','sblood','script','serifcap','shadow','short','slant','slide','slscript','small','smisome1','smkeyboard','smscript','smshadow','smslant','smtengwar','speed','stampatello','standard','starwars','stellar','stop','straight','tanja','tengwar','term','thick','thin','threepoint','ticks','ticksslant','tinker-toy','tombstone','trek','tsalagi','twopoint','univers','usaflag','weird']
    result = pyfiglet.figlet_format(text, font='{}'.format(random.choice(randFont)))
    print('%s %s'%(fg('light_cyan_1'), result))
else:
    result = pyfiglet.figlet_format(text, font='{}'.format(font))
    print('%s %s'%(fg('light_cyan_1'), result))
