# PyShelf: Biblioteca Pessoal
O PyShelf é um sistema de biblioteca pessoal desenvolvido em Python, criado para cadastrar, organizar e acompanhar livros de acordo com diferentes status de leitura.

integrantes: Dennis Alex de Oliveira, Eric Alexander Felix Santos 

Período Diurno

# Explicação Conceitual

## Fila — FIFO (First In, First Out)

A estrutura de fila segue o princípio “o primeiro que entra é o primeiro que sai”. Seu funcionamento pode ser comparado a uma fila de atendimento, onde o primeiro elemento inserido será o primeiro removido.

No Python, utilizamos listas para implementar filas com os métodos .append() para adicionar itens ao final e .pop(0) para remover o primeiro elemento.

Dentro do projeto, a fila é responsável por armazenar os livros cadastrados, mantendo a ordem em que foram adicionados.

### Exemplo de uso em código

```
fila_pendente.append(dict_livro)  # Adiciona ao final da fila
fila_pendente.pop(0) # Remove o primeiro item
```

## Pilha — LIFO (Last In, First Out)

A pilha funciona de forma inversa à fila: o último elemento inserido é o primeiro a ser retirado. Um exemplo simples é uma pilha de pratos.

Em Python, utilizamos .append() para inserir elementos no topo da pilha e .pop() ou reversed() para acessar os itens na ordem inversa.

No sistema, a pilha é utilizada para registrar o histórico de livros lidos, mostrando primeiro os livros adicionados mais recentemente.

### Exemplo de uso em código

```
pilha_lida.append(livro) # Adiciona no topo da pilha
for livro in reversed(pilha_lida): # Exibe do mais recente para o mais antigo (LIFO)
```

## Dicionário

Cada livro é armazenado em formato de dicionário Python, permitindo organizar as informações em pares de chave e valor.

Essa estrutura facilita o acesso aos dados do livro pelo nome de cada atributo, tornando o código mais organizado e legível.

### Exemplo de uso em código

```
livro = {
    'ID:' '1',
    'Título:' 'Jantar Secreto',
    'Autor:' 'Raphael Montes',
    'Ano de Publicação:' '2016',
    'Gênero:' 'Suspense',
    'status': 'A Ler',
    'Prioridade:' 'Alta'
}
# guarda todos os atributos do livro
```

## Lista e Tupla

A lista principal do sistema é utilizada para armazenar todos os livros cadastrados. Por ser mutável, ela permite adicionar e remover elementos durante a execução do programa.

Já as tuplas armazenam informações fixas, como categorias de status e níveis de prioridade. Como são imutáveis, ajudam a evitar alterações acidentais nesses valores.

```
Listas:

livros = []
em_leitura = []

Tuplas:

status = ('A Ler', 'Lendo', 'Lido')
prioridades = ('Baixa', 'Média', 'Alta')
```


## Modularização

O sistema foi organizado em diferentes arquivos .py, separando responsabilidades para facilitar a manutenção e a leitura do código.
```
dados.py
→ Armazena listas, filas, pilhas e constantes do sistema

tarefas.py
→ Contém as funções principais do projeto, como cadastrar e atualizar livros

utils.py
→ Funções auxiliares, validações e elementos visuais do terminal

main.py
→ Arquivo principal responsável pelo menu e execução do sistema
```

# Como Executar o Projeto

Para executar o sistema PyShelf, é necessário ter o Python instalado no computador.

Requisitos

Python 3.10 ou superior
Nenhuma biblioteca externa é necessária

Executando o projeto

Baixe ou clone os arquivos do projeto
Abra o terminal na pasta do projeto
Execute o seguinte comando:

python main.py

Após a execução, o menu principal do sistema será exibido no terminal.

# Funcionalidades Implementadas

O sistema possui funcionalidades para gerenciamento e organização de livros pessoais, utilizando estruturas de dados estudadas em sala.

### Funcionalidades principais:
```
Cadastro de livros contendo:
Título
Autor
Ano de publicação
Gênero
Prioridade

Listagem completa dos livros cadastrados com seus respectivos status

Implementação de fila FIFO para livros “A Ler”, onde os livros mais antigos possuem prioridade

Implementação de pilha LIFO para livros concluídos, exibindo primeiro os livros lidos mais recentemente

Atualização de status dos livros:

A Ler
Lendo
Concluído

Busca de livros por:

Título
Autor
```

### Funcionalidades bônus
```
Filtragem de livros por gênero

Contagem total de livros de acordo com o status:

A Ler
Lendo
Concluído
```

# Dificuldades e Aprendizados

Durante o desenvolvimento do projeto, uma das maiores dificuldades encontradas pelo grupo foi a implementação da busca de livros por título ou autor. Foi necessário trabalhar com percorrimento de listas e comparação de strings para localizar corretamente os livros cadastrados no sistema.

Além disso, organizar as estruturas de dados para que funcionassem em conjunto também exigiu bastante atenção, principalmente no uso correto da fila e da pilha. O projeto ajudou a reforçar os conceitos estudados em sala, como listas, dicionários, filas, pilhas e modularização em Python.

Ao longo do desenvolvimento, o grupo também aprendeu mais sobre organização de código, separação de responsabilidades entre arquivos e construção de menus interativos no terminal. A experiência contribuiu para melhorar a lógica de programação e a compreensão prática das estruturas de dados aplicadas em um sistema funcional.
