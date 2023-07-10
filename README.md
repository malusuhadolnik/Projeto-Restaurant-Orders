# Projeto-Restaurant-Orders

# Sobre
Neste projeto foram desenvolvidos testes, classes e funções em Python para a implementação de um cardápio de restaurante. O intuito foi construir uma ferramenta para que pudesse gerar cardápios considerando possíveis restrições alimentares, utilizando como base o antigo arquivo csv de gestão do estabelecimento.

##  Arquivos desenvolvidos

1. No arquivo  tests/ingredient/test_ingredient.py:
- Desenvolvimento de testes para a classe Ingredient, implementada previamente.

2. No arquivo tests/dish/test_dish.py:
- Desenvolvimento de testes para a classe Dish, implementada previamente.

3. No arquivo src/services/menu_data.py:
- Implementa a classe MenuData, que recebe como parâmetro o caminho para o arquivo csv no parâmetro source_path, faz sua leitura e, baseado em seu conteúdo, faz as devidas instanciações de pratos e ingredientes.

4. No arquivo src/services/menu_builder.py
- Implementa o método get_main_menu dentro da classe MenuBuilder, que tem como parâmetro opcional uma restrição que deve ser levada em conta na hora de gerar o cardápio.
- O método retorna uma lista de dicionários que contenham as chaves dish_name, ingredients, price e restrictions que se referem, respectivamente, ao nome do prato, ingredientes que o compõem, seu preço no cardápio e restrições daquele mesmo prato.


Os demais arquivos foram desenvolvidos pelo time da Trybe.

## Habilidades exercitadas
- Praticar o conceito de hashmaps através das estruturas de dados Dict e Set do Python;
- Praticar os conhecimentos de testes de software;
- Praticar os conhecimentos de orientação a objetos.

## Tecnologias usadas
Python
