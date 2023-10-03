import ply.lex as lex

tokens = [
    'SELECT', 'FROM', 'WHERE', 'ID', 'NUMERO', 'OPREL', 'SIGNO'
]

# Definiciones regulares
def t_ws(t):
    r'[ \t\n]+'
    pass

def t_NO_SELECT(t):
    r'\b\d+[Ss][Ee][Ll][Ee][Cc][Tt]\b'
    print(f'Error: Palabra clave no puede comenzar con un numero: {t.value}')
    t.lexer.skip(1)

def t_NO_FROM(t):
    r'\b\d+[Ff][Rr][Oo][Mm]\b'
    print(f'Error: Palabra clave no puede comenzar con un numero: {t.value}')
    t.lexer.skip(1)

def t_NO_WHERE(t):
    r'\b\d+[Ww][Hh][Ee][Rr][Ee]\b'
    print(f'Error: Palabra clave no puede comenzar con un numero: {t.value}')
    t.lexer.skip(1)

def t_SELECT(t):
    r'\b[Ss][Ee][Ll][Ee][Cc][Tt]\b'
    return t

def t_FROM(t):
    r'\b[Ff][Rr][Oo][Mm]\b'
    return t

def t_WHERE(t):
    r'\b[Ww][Hh][Ee][Rr][Ee]\b'
    return t

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.value = instalarID(t.value)
    return t

def t_NO_ID(t):
    r'\b\d+[A-Za-z_][A-Za-z0-9_]*'
    print(f"Error: Identificador no puede comenzar con un numero: {t.value}")
    t.lexer.skip(1)
    
def t_NUMERO(t):
    r'\d+(\.\d+)?(E[+\-]?\d+)?'
    t.value = instalarNum(t.value)  
    return t

def t_OPREL(t):
    r'<=|>=|==|<>|<|>|='
    return t

def t_SIGNO(t):
    r','
    return t

def t_error(t):
    print(f"Error: Simbolo incorrecto '{t.value[0]}'")
    t.lexer.skip(1)

# Tablas de símbolos y constantes numéricas (como diccionarios)
tabla_simbolos = {}
tabla_numeros = {}

# Función para instalar un ID en la tabla de símbolos
def instalarID(id):
    if id in tabla_simbolos:
        return tabla_simbolos[id]
    else:
        nuevo_id = len(tabla_simbolos) + 1
        tabla_simbolos[id] = nuevo_id
        return nuevo_id

# Función para instalar un número en la tabla de constantes numéricas
def instalarNum(numero):
    if numero in tabla_numeros:
        return tabla_numeros[numero]
    else:
        nuevo_numero = len(tabla_numeros) + 1
        tabla_numeros[numero] = nuevo_numero
        return nuevo_numero

lexer = lex.lex()

# Leer desde un archivo .txt
with open('entrada.txt', 'r') as file:
    entrada = file.read()

# Prueba el analizador léxico con el contenido del archivo.txt
lexer.input(entrada)

# Define un diccionario para mapear los tipos de tokens a sus valores
token_values = {
    'SELECT': 'PC: SELECT',
    'FROM': 'PC: FROM',
    'WHERE': 'PC: WHERE',
    'ID': 'ID',
    'NUMERO': 'NUMERO',
    'OPREL': 'OPREL',
    'SIGNO': 'SIGNO'
}
print(entrada)
print('\n--------------------------------')

# Lee los tokens y obtén sus valores
for token in lexer:
    if token.type == 'ID':
        if token.value in tabla_simbolos.values():
            print(f'{token_values[token.type]}: {list(tabla_simbolos.keys())[list(tabla_simbolos.values()).index(token.value)]}')
        else:
            print(f'{token_values[token.type]}: {token.value}')
    elif token.type == 'NUMERO':
        if token.value in tabla_numeros.values():
            print(f'{token_values[token.type]}: {list(tabla_numeros.keys())[list(tabla_numeros.values()).index(token.value)]}')
        else:
            print(f'{token_values[token.type]}: {token.value}')
    elif token.type == 'SIGNO':
        print(f'SIGNO: {token.value}')
    elif token.type == 'OPREL':
        print(f'OPREL: {token.value}')
    else:
        print(token_values[token.type])


print('--------------------------------')
# Imprime tabla de símbolos
print("\nTABLA DE SIMBOLOS:")
for key, value in tabla_simbolos.items():
    print(f"{value}: {key}")
print('--------------------------------')
# Imprime tabla de números
print("\nTABLA DE NUMEROS:")
for key, value in tabla_numeros.items():
    print(f"{value}: {key}")