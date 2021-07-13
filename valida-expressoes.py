def analise_parenteses(expressao):
  pilha = []
  for i in expressao:
    if i == '(':
      pilha.append(i)
    if i == ')':
      tamanho = len(pilha)                     
      if tamanho == 0:
        return False
      pilha.pop(-1)
      
  if len(pilha) == 0:
    return True
  else:
    return False   
  
  
def main():
  while True:
   expressao = input('Digite uma expressão com parênteses (ENTER para terminar):')
   if expressao == '':
     break
   if analise_parenteses(expressao): 
     print(expressao, 'está ok')
   else:
     print(expressao, 'está errado') 
 
main()

