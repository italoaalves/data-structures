# ProjetoED
Repositório do Projeto da disciplina de Estruturas de Dados. Escohemos Pokemons para nosso modelo de dado.

## Como executar este projeto
```console
git clone https://github.com/italoaalves/projeto-ed/
cd projeto-ed

virtualenv env
./env/bin/activate
pip install -r requirements.txt

python app.py
```

## Pokeapi
Utilizamos da API disponivel em [pokeapi](https://pokeapi.co) para preencher o nosso modelo de dados.

## Especificação do projeto
O objetivo deste projeto é implementar as principais estruturas de
dados lineares: Listas, Pilhas e Filas. Devem ser implementadas (pelo menos)
as seguintes classes:
 - Classe No – Representa a informação sendo manipulada nas estruturas lineares;
 - Classe Lista – Classe contendo os principais métodos para a manipulação de uma lista;
 - Classe Pilha - Classe contendo os principais métodos para a manipulação de uma pilha;
 - Classe Fila - Classe contendo os principais métodos para a manipulação de uma fila;
 - Classe Dado – Classe que contém o conteúdo dos nós. Pode ser uma música, livro, série, jogo etc.
 
 ### As classes Lista, Pilha e Fila devem conter os seguintes métodos:
  - Adicionar – Adiciona um elemento em qualquer posição. No caso de Pilhas e Filas, existem regras para a adição de novos elementos;
  - Remover – Remove um elemento de qualquer posição. No caso de Pilhas e Filas, a remoção não pode ocorrer em qualquer posição;
  - Vazio – Retorna verdadeiro se a estrutura estiver vazia e falso caso contrário;
  - Tamanho – Retorna quantos elementos a estrutura possui;
  - Mostrar Elemento – Mostra o valor de um elemento em uma determinada posição. No caso de Pilhas e Filas, esse método só pode apresentar o valor do dado que esta no início da estrutura;
  - Ordenar – Esse método só é possível ser implementado para a lista. O critério de ordenação (música, ano, título do livro) deve ser escolhido pelo grupo;
  - Buscar – Escolher alguma informação da classe Dado para ser buscada. Por exemplo, se seu Dado é um filme, esse método pode fazer uma busca por todos os filmes de um determinado ano. Esse método, assim como o anterior, só deve ser implementado para a lista.
