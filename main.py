import sys
import MeCab

tagger = MeCab.Tagger('-Ochasen')

print(tagger.parse(sys.argv[1]))
#fi = open('data.txt', 'r')
#fo = open('output.txt', 'w')

#line = fi.readline()
#while line:
#    result = tagger.parse(line)
#    fo.write(result[1:])
#    line = fi.readline()

#fi.close()
#fo.close()