import sys
import binascii
from Crypto.PublicKey import RSA
from base64 import b64decode

if (False): #len(sys.argv)<7):
    print "\t\n\nArg error: python rsaHastad.py <n0 File> <n1 File> <n2 File> <c0 File> <c1 File> <c2 File> [--decimal/--hex/--b64] [-v/--verbose]\n\n"
    exit()

print "\n"

print "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "\t        RSA Hastad Attack         "
print "\t         JulesDT -- 2016          "
print "\t         License GNU/GPL          "
print "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def find_invpow(x,n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

def parseC(argv, index, verbose):
    import string
    file = open(argv[index],'r')
    cmd = ' '.join(argv)
    fileInput = ''.join(file.readlines()).strip()
    if '--decimal' in cmd:
        if verbose:
            print "##"
            print "##",fileInput
            print "## Considered as decimal input"
            print "##"
        return long(fileInput)
    elif '--hex' in cmd:
        if verbose:
            print "##"
            print "##",fileInput
            print "## Considered as hexadecimal input"
            print "##"
        return long(fileInput,16)
    elif '--b64' in cmd:
        if verbose:
            print "##"
            print "##",fileInput
            print "## Considered as base64 input"
            print "##"
        return long(binascii.hexlify(binascii.a2b_base64(fileInput)),16)
    else:
        try:
            fileInput = long(fileInput)
            if verbose:
                print "##"
                print "##",fileInput
                print "## Guessed as decimal input"
                print "##"
            return long(fileInput)
        except ValueError:
            if all(c in string.hexdigits for c in fileInput):
                if verbose:
                    print "##"
                    print "##",fileInput
                    print "## Guessed as hexadecimal input"
                    print "##"
                return long(fileInput,16)
            else:
                if verbose:
                    print "##"
                    print "##",fileInput
                    print "## Guessed as base64 input"
                    print "##"
                return long(binascii.hexlify(binascii.a2b_base64(fileInput)),16)
            pass

def parseN(argv,index):
    file = open(argv[index],'r')
    fileInput = ''.join(file.readlines()).strip()
    try:
        fileInput = long(fileInput)
        return fileInput
    except ValueError:
        from Crypto.PublicKey import RSA
        return long(RSA.importKey(fileInput).__getattr__('n'))
        pass


if __name__ == '__main__':
    e = 3
    cmd = ' '.join(sys.argv)
    if '-v' in cmd or '--verbose' in cmd:
        verbose = True
    else:
        verbose = False
    n0 = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
    n1 = 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309
    n2 = 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723
    
    c0 = 261345950255088824199206969589297492768083568554363001807292202086148198406074174087599949853526183725967067833548807700003242116447746845440684134251660304329137959138520358243308203606301658523591058739042432952619448086647193337265971245145812964921635172967644877116033878019171669996959913243573262905352
    c1 = 147535246350781145803699087910221608128508531245679654307942476916759248177185257800509654502604804274016979933266589612202725825700391959444409062358822225723990027527297006978244654606302532267233009201147158408744883222082702546984956726569203304884883611514054090179844394974632291986608151788475105033841
    c2 = 633230627388596886579908367739501184580838393691617645602928172655297372011201023715698247545128732683701168969876752613788489811859334308151035580367022645613275345197226463059204068925526462215747374938053085247530963311728051220282203348788536162008752905647387811366287564542709387347113984861614875521973
    n = [n0,n1,n2]
    a = [c0,c1,c2]

    result = (chinese_remainder(n, a))
    resultHex = str(hex(find_invpow(result,3)))[2:-1]
    print ""
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Decoded Hex :\n",resultHex
    print "---------------------------"
    print "As Ascii :\n",resultHex.decode('hex')
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"