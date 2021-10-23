import mmap

#converts hex offset to be readable for mmap
def cnvt(j):
    a = int(j, 16)
    return(a)

# adjusts values that use 2 hex memory locations
def two_hex(dest_a, dest_b, value):
    if value <= 255: #checks if the value is less than or equal to 255
        hexd = hex(value)
        hexd = hex(value).replace('x', '') # Since Hex values on python come out
        if len(hexd) == 1:                 # as '0x####' we remove the x and
            hexd = '000'+hexd              # adjust the values as 4 digits
        elif len(hexd) == 2:
            hexd = '00' + hexd

    elif value > 255: #checks if greater than 255
        hexd = hex(value).replace('x', '')
        if len(hexd) == 4:
            pass
        elif len(hexd) == 5:
            hexd = hexd.replace('0','',1)

    splitter = []                       # this splits the 4 digit hex to 2
    for index in range(0,len(hexd),2):  # seperate Hex Values
        splitter.append(hexd[index:index+2])
    m[dest_a] = cnvt(splitter[1]) #first slot
    m[dest_b] = cnvt(splitter[0]) #second slot


# edits the values of characters.
def char_adj(Str, Dex, Int, HPa, HPb, HMa, HMb, EXa, EXb, talk):
    global hpv, hmv, exv, hmv
    if talk == 'c' or talk == 'C': # values modified by user
        cst = int(input('Strength Val (255 Max)\n'))      # Str
        cdx = int(input('Dexterity Val (255 Max)\n'))     # Dex
        cit = int(input('Intelligence Val (255 Max)\n'))  # Int
        hpv = int(input('Health Val (999 Max)\n'))        # HP
        hmv = int(input('Max Health Val (999 Max)\n'))    # MH
        exv = int(input('Experience Val (999 Max)\n'))    # Int
    else:
        print('Max Values Set\n') # default modified values (Maxed)
        cst = 99   # Str
        cdx = 99   # Dex
        cit = 99   # Int
        hpv = 999  # HP
        hmv = 999  # HM
        exv = 9999 # exp
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[Str] = cst  # 63
    m[Dex] = cdx  # 63
    m[Int] = cit  # 63
    two_hex(HPa, HPb, hpv)
    two_hex(HMa, HMb, hmv)
    two_hex(EXa, EXa, exv)
    m.flush()


def item_adj(talk): #todo make the values editable for user
    if talk == 'y' or talk == 'Y': #values modified by user
        mga = int(input('How Many Magic Axes (255 Max)\n'))     # Magic_Axe
        blb = int(input('How Many Black Badge (255 Max)\n'))    # Black_badge
        skk = int(input('How Many Skull Keys (255 Max)\n'))     # Skull_Keys
        mgc = int(input('How Many Magic Carpets (255 Max)\n'))  # Magic_Carpet
        gem = int(input('How Many Gems (255 Max)\n'))           # gems
        key = int(input('How Many Keys (255 Max)\n'))           # key
        gld = int(input('How Much gold (9999 Max)\n'))          # gold
    else:
        print('\nDefault modified values set.')# default modified values (Maxed)
        mga = 10
        blb = 1
        skk = 100
        mgc = 2
        gem = 100
        key = 100
        gld = 9999
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    two_hex(cnvt('204'),cnvt('205'),gld)
    m[cnvt('206')] = key  # keys
    m[cnvt('207')] = gem  # gems
    m[cnvt('20a')] = mgc  # Magic_Carpet
    m[cnvt('20b')] = skk  # Skull_Keys
    m[cnvt('218')] = blb  # Black_badge
    m[cnvt('240')] = mga  # Magic_Axe
    m.flush()

# Program Main Start

print('   ULTIMA V SAVE EDITOR ')
print('\nThis tool can max the stats of all characters within the game save file creator.\n!!! Make sure this python file '
      'is in the same directory as the INIT.GAM file or SAVED.GAM in order to work properly. !!!\nyou will be able to '
      'edit some values as well.')

input('\nPress Enter to continue...')

file_type = input('Would you like to modify the (I)NIT file to make all your save games have the modified values?\nor '
                  'your (S)AVED file which just modifies the current save file? (I/S): ')
if file_type == 'i' or file_type == 'I':
    f = open('INIT.GAM', 'a+b')
elif file_type == 's' or file_type ==  'S':
    f = open('SAVED.GAM', 'a+b')

print('\n~~~ Character Stat Modifier ~~~\n')

m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
#print(m[:15]) # prints the lines from 0 to 15
char_inp = input('Would you like to modify Character Stats? (Y/N): ')
if char_inp == 'y' or char_inp == 'Y':
    cstm = input('Would you like to (m)ax the stats? or (c)ustomize individually? (m/c): ')
    print('\n mainChar:')
    char_adj(cnvt('0e'),cnvt('0f'), cnvt('10'), cnvt('12'), cnvt('13'), cnvt('14'), cnvt('15'), cnvt('16'), cnvt('17'),cstm)
    print('Shamino:')
    char_adj(cnvt('2e'),cnvt('2f'), cnvt('30'), cnvt('32'), cnvt('33'), cnvt('34'), cnvt('35'), cnvt('36'), cnvt('37'),cstm)
    print('Iolo:')
    char_adj(cnvt('4e'),cnvt('4f'), cnvt('50'), cnvt('52'), cnvt('53'), cnvt('54'), cnvt('55'), cnvt('56'), cnvt('57'),cstm)
    print('Mariah:')
    char_adj(cnvt('6e'),cnvt('6f'), cnvt('70'), cnvt('72'), cnvt('73'), cnvt('74'), cnvt('75'), cnvt('76'), cnvt('77'),cstm)
    print('Geoffrey:')
    char_adj(cnvt('8e'),cnvt('8f'), cnvt('90'), cnvt('92'), cnvt('93'), cnvt('94'), cnvt('95'), cnvt('96'), cnvt('97'),cstm)
    print('Jaana:')
    char_adj(cnvt('Ae'),cnvt('Af'), cnvt('B0'), cnvt('B2'), cnvt('B3'), cnvt('B4'), cnvt('B5'), cnvt('B6'), cnvt('B7'),cstm)
    print('Julia:')
    char_adj(cnvt('Ce'),cnvt('Cf'), cnvt('D0'), cnvt('D2'), cnvt('D3'), cnvt('D4'), cnvt('D5'), cnvt('D6'), cnvt('D7'),cstm)
    print('Dupre:')
    char_adj(cnvt('Ee'),cnvt('Ef'), cnvt('F0'), cnvt('F2'), cnvt('F3'), cnvt('F4'), cnvt('F5'), cnvt('F6'), cnvt('F7'),cstm)

    print('Katrina:')
    char_adj(cnvt('10e'),cnvt('10f'), cnvt('110'), cnvt('112'), cnvt('113'), cnvt('114'), cnvt('115'), cnvt('116'), cnvt('117'),cstm)
    print('Sentri:')
    char_adj(cnvt('12e'),cnvt('12f'), cnvt('130'), cnvt('132'), cnvt('133'), cnvt('134'), cnvt('135'), cnvt('136'), cnvt('137'),cstm)
    print('Gwenno:')
    char_adj(cnvt('14e'),cnvt('14f'), cnvt('150'), cnvt('152'), cnvt('153'), cnvt('154'), cnvt('155'), cnvt('156'), cnvt('157'),cstm)
    print('Johne:')
    char_adj(cnvt('16e'),cnvt('16f'), cnvt('170'), cnvt('172'), cnvt('173'), cnvt('174'), cnvt('175'), cnvt('176'), cnvt('177'),cstm)
    print('Gorn:')
    char_adj(cnvt('18e'),cnvt('18f'), cnvt('190'), cnvt('192'), cnvt('193'), cnvt('194'), cnvt('195'), cnvt('196'), cnvt('197'),cstm)
    print('Maxwell:')
    char_adj(cnvt('1Ae'),cnvt('1Af'), cnvt('1B0'), cnvt('1B2'), cnvt('1B3'), cnvt('1B4'), cnvt('1B5'), cnvt('1B6'), cnvt('1B7'),cstm)
    print('Toshi:')
    char_adj(cnvt('1Ce'),cnvt('1Cf'), cnvt('1D0'), cnvt('1D2'), cnvt('1D3'), cnvt('1D4'), cnvt('1D5'), cnvt('1D6'), cnvt('1D7'),cstm)
    print('Saduj:')
    char_adj(cnvt('1Ee'),cnvt('1Ef'), cnvt('1F0'), cnvt('1F2'), cnvt('1F3'), cnvt('1F4'), cnvt('1F5'), cnvt('1F6'), cnvt('1F7'),cstm)
    print('\nAll Characters have been modified')
else:
    print('\nSkipped.')
    pass

print('\n~~~ Item quantity Modifier ~~~')
item_inp = input('Would you like to modify the quantity of items? (y/n): ')
if item_inp == 'y' or item_inp == 'Y':
    choice = input('\nWould you like to customize the values individually? (y/n): \n')
    item_adj(choice)
    print('\nItem Quantities have been modified.')
else:
    print('\nskipped.')


m.flush()
m.close()
f.close()


if char_inp == 'exit':
    print('\n\n\n°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø')
    print('  User@Admin:~$ Sudo rm -r /*  ')
    print('°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø')
