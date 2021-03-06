import argparse
import re

# Keywords
keywords = ['main','int','float', 'if','else', 'while', 'for', 'read', 'print']

# Regular Expression for Identifiers and Keywords
re_words = '^[a-zA-Z0-9_]*$'
re_alpha = '/^[A-Za-z]+$/'
# Regular Expression for Literals
re_int = '^[0-9]+$'

tokens = {
  "main":   "MAIN",
  "int":    "INT",
  "float":  "FLOAT",
  "if":     "IF",
  "else":   "ELSE",
  "while":  "WHILE",
  "for":    "FOR",
  "read":   "READ",
  "print":  "PRINT",
  "(":      "LBRACKET",
  ")":      "RBRACKET",
  "{":      "LBRACE",
  "}":      "RBRACE",
  ",":      "COMMA",
  ";":      "PCOMMA",
  "=":      "ATTR",
  "==":     "EQ",
  "!=":     "NE",
  "||":     "OR",
  "&&":     "AND",
  "<":      "LT",
  "<=":     "LE",
  ">":      "GT",
  ">=":     "GE",
  "+":      "PLUS",
  "-":      "MINUS",
  "*":      "MULT",
  "/":      "DIV",
  "[":      "LCOL",
  "]":      "RCOL"
  
}

parser = argparse.ArgumentParser()

#-db DATABSE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-i", "--input", help="insert the path and name of a .c file", default="input/teste_attr1.c")
parser.add_argument("-o", "--output", help="insert the name of output file", default="output/output.txt")

args = parser.parse_args()

f = open(args.input, "r")

# file_content = file_content.replace('\n', '')
# list_elements = re.split('([^a-zA-Z0-9._>=<=!=&&||])', file_content)
# list_elements = [c.strip(' ') for c in list_elements]
# list_elements = list(filter(None, list_elements))

buffer = []
state = 0

for line in f:
  line = line.rstrip('\n')
  for char in line:
  
    if state == 0:
      if re.match('^[a-zA-Z]*$', char):
        state = 1
        buffer.append(char)
      elif re.match('^[0-9]+$', char):
        state = 2
        buffer.append(char)
      elif char == '<':
        state = 5
        buffer.append(char)
      elif char == '>':
        state = 6
        buffer.append(char)
      elif char == '=':
        state = 7
        buffer.append(char)
      elif char == '!':
        state = 8
        buffer.append(char)
      elif char == '|':
        state = 9
        buffer.append(char)
      elif char == '&':
        state = 10
        buffer.append(char)
      else:
        buffer.append(char)
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []



    elif state == 1:
      if re.match('^[a-zA-Z0-9_]*$', char):
        buffer.append(char)
      else:
        state = 0
        lexeme = ''.join(buffer)
        idToken = 'ID'
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme] if lexeme in tokens else idToken}')
        buffer = []

    elif state == 2:
      if re.match('^[0-9]+$', char):
        buffer.append(char)
      elif char == '.':
        state = 3
        buffer.append(char)
      else:
        state = 0
        print(f'INTEGER: {buffer}')
        buffer = []
        
    elif state == 3:
      if re.match('^[0-9]+$', char):
        state = 4
        buffer.append(char)
      else:
        print('error')

    elif state == 4:
      if re.match('^[0-9]+$', char):
        buffer.append(char)
      else:
        state = 0
        print(f'FLOAT: {buffer}')
        buffer = []

    elif state == 5:
      if (char == '='):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []
      else:
        state = 0
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []

    elif state == 6:
      if (char == '='):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []
      else:
        state = 0
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []

    elif state == 7:
      if (char == '='):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []
      else:
        state = 0
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []

    elif state == 8:
      if (char == '='):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []
      else:
        print('Error')

    elif state == 9:
      if (char == '|'):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []
      else:
        print('Error')

    elif state == 10:
      if (char == '&'):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        print(f'Lexema: "{lexeme}" Token: {tokens[lexeme]}')
        buffer = []
      else:
        print('Error')


# file_content = f.read()

# print(file_content)
# print(list_elements)

# for element in list_elements:

#   if element[0].isalpha(): 
#     if (re.fullmatch(re_words, element)):
#       if any(keyword == element for keyword in keywords):
#         print(f'PALAVRA: {element} TOKEN: {element.upper()}') 
#       else:
#         print(f'PALAVRA: {element} TOKEN: ID')

#   elif element[0].isnumeric():
#     if (re.fullmatch(re_float, element)):
#         print(f'PALAVRA: {element} TOKEN: FLOAT_CONSTANT') 
#     elif (re.fullmatch(re_int, element)):
#         print(f'PALAVRA: {element} TOKEN: INTEGER_CONSTANT') 
#     else:
#         print(f'PALAVRA: {element} TOKEN: ERROR') 


