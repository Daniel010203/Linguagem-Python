from sympy import symbols, ForAll, Exists, And, Or, Not

# Definir variáveis
x, y = symbols('x y')

# Predicados
P = symbols('P', integer=True)
Q = symbols('Q', integer=True)

# Fórmulas de lógica de primeira ordem
formula1 = ForAll(x, P(x) >> Q(x))  # Para todo x, se P(x) então Q(x)
formula2 = Exists(x, P(x) & Q(x))  # Existe x tal que P(x) e Q(x)
formula3 = Or(P(x), Not(Q(y)))      # P(x) ou não Q(y)

# Exemplo de avaliação
modelo = {P(1): True, P(2): False, Q(1): True, Q(2): True}

print(f"A fórmula 1 é verdadeira no modelo? {formula1.subs(modelo)}")
print(f"A fórmula 2 é verdadeira no modelo? {formula2.subs(modelo)}")
print(f"A fórmula 3 é verdadeira no modelo? {formula3.subs(modelo)}")

# Neste exemplo, usamos sympypara criar fórmulas de lógica de primeira ordem e avaliá-las em um modelo específico. Observe que as variáveis P​​e Qsão tratadas como predicadas sobre inteiros. Você pode adaptar isso para representar predicados específicos do seu domínio.
#
# Se você estiver trabalhando com lógica de primeira ordem em contextos mais complexos, você pode precisar de bibliotecas mais especializadas ou ferramentas dedicadas. Este exemplo é uma introdução básica usando sympy.