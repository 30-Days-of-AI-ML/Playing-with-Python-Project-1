from mathparse import mathparse

exp1 = mathparse.parse('4 + 4')
exp2 = mathparse.parse('four thousand two hundred one plus five hundred', language='ENG')
exp3 = mathparse.parse('thirty minus twenty', language='ENG')
exp4 = mathparse.parse('one thousand two hundred four divided by one hundred', language='ENG')

print(exp1)
print(exp2)
print(exp3)
print(exp4)
