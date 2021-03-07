from token_csmall import tokens
from tabulate import tabulate
import argparse
import re

# Argumentos da linha de comandos: -i [arquivo de entrada .c] -o [arquivo de saida contendo os tokens]
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="insert the path and name of a .c file (DEFAULT: 'input/teste_attr1.c')", default="input/teste_attr1.c")
parser.add_argument("-o", "--output", help="insert the path and name of output file (DEFAULT: 'output/output.txt')", default="output/output.txt")
args = parser.parse_args()

f_in = open(args.input, "r") # Le arquivo de entrada

token_list = [] # Lista de tokens identificados 
buffer = [] # Buffer que forma o lexema
state = 0 # Estado inicial do automato
line_count = 1 

for line in f_in: # Percorre todas as linhas do arquivo de entrada
  line = line.rstrip('\n')
  char_count = 0

  while (char_count < len(line)): # Percorre todos os caracteres da linha
    char = line[char_count]

    if state == 0:
      if char.isalpha():
        state = 1
        buffer.append(char)
      elif char.isnumeric():
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
      elif char == ' ':
        pass
      else:
        buffer.append(char)
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer

    elif state == 1:
      if re.match('^[a-zA-Z0-9_]*$', char):
        buffer.append(char)
      else:
        char_count -= 1
        state = 0
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme] if lexeme in tokens else "ID", lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer

    elif state == 2:
      if char.isnumeric():
        buffer.append(char)
      elif char == '.':
        state = 3
        buffer.append(char)
      else:
        char_count -= 1
        state = 0
        lexeme = ''.join(buffer)
        token_list.append(['INTEGER_CONST', lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer
        
    elif state == 3:
      if char.isnumeric():
        state = 4
        buffer.append(char)
      else:
        print(f'Falha no estado {state}: produção não aceita pelo analisador léxico da linguagem Csmall.')

    elif state == 4:
      if char.isnumeric():
        buffer.append(char)
      else:
        char_count -= 1
        state = 0
        lexeme = ''.join(buffer)
        token_list.append(['FLOAT_CONST', lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer

    elif state == 5:
      if (char == '='):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer
      else:
        char_count -= 1
        state = 0
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer

    elif state == 6:
      if (char == '='):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer
      else:
        char_count -= 1
        state = 0
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer

    elif state == 7:
      if (char == '='):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer
      else:
        char_count -= 1
        state = 0
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer

    elif state == 8:
      if (char == '='):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer
      else:
        print(f'Falha no estado {state}: produção não aceita pelo analisador léxico da linguagem Csmall.')

    elif state == 9:
      if (char == '|'):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer
      else:
        print(f'Falha no estado {state}: produção não aceita pelo analisador léxico da linguagem Csmall.')

    elif state == 10:
      if (char == '&'):
        state = 0
        buffer.append(char)
        lexeme = ''.join(buffer)
        token_list.append([tokens[lexeme], lexeme, line_count]) # Adiciona o token à lista de tokens identificados
        buffer = [] # Limpa o buffer
      else:
        print(f'Falha no estado {state}: produção não aceita pelo analisador léxico da linguagem Csmall.')
    
    char_count += 1
  line_count += 1

# Ultimo token refere ao fim do arquivo -> EOF
token_list.append(['EOF', '', line_count])

# Escreve no arquivo de saida os tokens identificados na produção
f_out = open(args.output, "w")
f_out.write(tabulate(token_list, headers=['Token', 'Lexema', 'Linha']))
f_out.close()

f_in.close()

