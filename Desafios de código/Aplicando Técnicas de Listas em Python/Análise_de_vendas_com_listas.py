def analise_vendas(vendas):
    # Calcula o total de vendas e a média mensal
    total_vendas = sum(vendas) # Aqui definimos que o total de vendas é equivalente a soma (sum) de vendas
    media_vendas = total_vendas / len(vendas) # Aqui calculamos a média de vendas, sendo a média o total dividido pela quantidade de vendas. O (len) é usado para fazer essa contagem da quantidade de vendas
    
    return f"{total_vendas}, {media_vendas:.2f}" # O retorno define que a saída será os valores equivalentes ao total_vendas e media_vendas

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input() 
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(','))) # O entrada.split divide a string entrada em uma lista de strings, separando os valores por vírgula. O map(int, ...) aplica a função int a cada elemento dessa lista, convertendo cada string em um inteiro. O list(...) coverte o objeto map resultante em uma lista de inteiros. A lista é atribuida à variável vendas.
    
    return vendas

# Executa a função principal
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
