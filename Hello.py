'''
Created on Nov 18, 2013

@author: jordan
'''
from cgi import escape

def hello(): 
    """ return hello world """
    return "hello world"

assert hello() == "hello world"


def palindrome(string):
    for i in range( len(string)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

assert palindrome("hellolleh") == True
assert palindrome("string") == False

def html_table(t):
    s = """<table border="1">\n"""
    for row in t:
        s+="""<tr>\n"""
        for entry in row:
            s+="""<td>""" + escape(str(entry)) + """</td>\n"""
        s+="""</tr>\n"""
    s += """</table>"""
    return s


mul = []

for r in range(0, 10):
    col = []
    for c in range(0, 10):
        col.append(c * r)
    mul.append(col)


text = ""
for r in range(0, 10):
    for c in range(0, 10):
        text += '\t' + str(mul[r][c])
    text += "\n"

# print(text)

table1 = [[1,2,3],[4,5,6]]
print(html_table(mul))
f = open('table.html', 'w')
f.write(html_table(mul))
print"ok"