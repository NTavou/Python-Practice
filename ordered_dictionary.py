from operator import itemgetter
from collections import OrderedDict

countr_popul = OrderedDict()

countr_popul['India'] = 1309340000
countr_popul['China'] = 1380460000
countr_popul['USA'] = 325164000
countr_popul['Brazil'] = 206839000
countr_popul['Indonesia'] = 260581000

sorted_countr_popul = sorted(countr_popul.items(), key=itemgetter(1))

print sorted_countr_popul

print sorted_countr_popul[::-1]






