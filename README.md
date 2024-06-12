# Linuxtips - Python Base

## Dia 1 - Introdução a programação e ao Python

### Linguagens de Programação

- **Input** -> entrada, envia dados/instruções para a unidade computacional, exemplo: teclado.
- **Output** -> saída, maneira como a informação é disponibiliza, exemplo: monitor.

O computador por ser um dispositivo eletrônico, só entende a linguagem binária (0 e 1).

- 0 significa desligado.
- 1 significa ligado.

Padronização de como as informações são enviadas, feita através dos bits, cada bit representa 0 ou 1. Existindo uma sequência de 8 bits (byte), 16 bits...

Cada byte possui uma "mensagem", exigindo um cálculo na base 2, binária, chegando num número final.

- 10011011 = 155
- Letra "A" = 65 = 1000001

Linguagem de programação é uma abstração, ao olho humano é mais fácil de escrever, tendo um entendimendo melhor. No final o código é convertido para a base binária.

- **Linguagem de baixo nível** -> Assembly
- **Linguagem de médio nível** -> C, é convertida para uma linguagem de baixo nível.
- **Linguagem de alto nível** -> Python, contertida para a linguagem de médio nível.
  - **Linguagens compiladas** -> escreve o programa, e o programa precisa estar todo correto do ínicio ao fim, em pacote, o erro vai ser detectado na execução do programa já compilado.
  - **Linguagens interpretadas** -> significa que cada comando(linha) pode ser interpretado individualmente. O Python é interpretado.

No compilado se tiver um erro em qualquer lugar do código, a compilação vai falhar, e no interpretado uma linha pode funcionar e depois pode ocorrer um erro, por exemplo, no final do programa.

No código compilado, para cada sistema operacional, necessitará de um programa compilado separadamente, enquanto que o interpretado é multiplataforma, podendo o mesmo programa ser executado em diferentes sistemas operacionais.

### Como está organizada a plataforma Python

Componentes da Plataforma Python

Python é um conjunto de coisas.

- **PLR Python Language Reference** -> toda especificação, um documento de design formal da linguagem Python. A partir desse documento é possível criar uma implementação de um programa.

Implementações Python

- **IronPython** -> Python rodando no .NET.
- **Jython** -> Python rodando na Máquina Virtual do Java
- **PyPy** -> implementação do Python reescrito em Python para ficar mais rápido.
- **Stackless** Python -> galho do CPython que suporta multi-threading.
- **MicroPython** -> Python reduzido, rodando em micro controladores, dispositivos embarcados.

**CPython** -> implementação oficial. Escrito usando a Linguagem C

O CPython possui um ecossistema em torno dele, tudo em torno da linguagem Python.

- Comunidades
- PSF -> Python Software Foundation, fundacão que protege a marca Python e possui um código de conduta, também há empresas que se afiliam a fundação.
- APyB -> Fundação Python Brasil.
- Pacotes e ferramentas -> programas Pythons que podem ser reutilizados. E ferramentas para instalar bibliotecas, etc.
- PyPI -> Python Package Index.

### Instalação do Python e preparação do ambiente

- Replit
- Gitpod
- Micro
- Terminator

Comandos Python a partir do terminal

- `python -c "1"` -> não retorna nada, pois não foi instruído como utilizar o número 1, ele entende mas ele não sabe o que fazer, é um valor literal.
- `python -c "print(1)"` -> ele imprime o número 1, pois o interpretador foi instruído a fazer essa ação.
- `python -c "print('giovanni'.upper())"` -> imprime "GIOVANNI" pois a função `upper()` coloca todos os caracteres em maiúsculo.
- `python -m site` -> executa um módulo do Python já pré-definido. Mostra como o Python que está sendo utilizado que está instalado.
- `python -m turtledemo` -> interface gráfica feita em tk com exemplos de jogos e animações
- `python -V` -> mostra a versão do Python.
- `python -VV` -> mostra a versão e a data da última compilação do Python.
- `python --help` -> ajuda do Python.
- `python` -> terminal interativo do Python, é o interpretador padrão. Sempre mostra o output.

<hr>

- **REPL** -> Read Eval Print Loop.

### Introdução ao git e seu primeiro script Python

- **Script** -> é um arquivo de comandos encadeados independente.
- **Sintaxe** -> ordem e regras que as palavras e os comandos devem ser escritos.

**Comentários** -> são ignorados pelo interpretador. Alguns comentários colocados na frente do código podem ser interpretados por algumas ferramentas.

- **Shebang** -> característica do sistema Unix/Linux, é um comentário especial, sempre presente na primeira linha do script, ele serve para identificar qual é o interpretador e a versão do Python que vai ser usada para executar o script.
  - `which python` -> caminho do Python

Um ambiente é um "local" que está preparado para executar o script ou programa Python, que possui acesso ao interpretador e ele tem acesso a informações específicas do ambiente/sistema.

Um ambiente é formado de um shell e as variáveis de ambiente, a maioria dos programas são desenvolvidos orientados a ambiente.

Ao utilizar o SHEBANG apontando para o ambiente, todas as variáveis de ambiente serão fornecidas para o Python. Ao especificar o Python no SHEBANG não será necessário especificar o Python ao executar, pode escrever apenas `./arquivo.py`.

### Criando um programa que lê variáveis de ambiente

- É recomendável seguir um guia de estilo para escrever códigos Python. O pep8.
- Para terminal é legal manter 80 colunas de caracteres por linha. Utilizar apenas até a coluna 79, quebrando para a linha de baixo.
- Também é necessário colocar no script/programa são os metadados, que são informações que necessariamente não fazem parte do programa, mas podem serem usadas para informações adicionais. Normalmente são adicionais após o comentário de bloco de explicação do script no início do programa.

`__` -> underline duplos podem ser chamado de Dunder.

O Python executa todo o conteúdo do arquivo mesmo não estando dentro de uma função `main()`.

- Usar snake case ao escrever nomes de variáveis, mas também existe o padrão Pascal Case.
- **Built-in** -> funções, bibliotecas ou ferramentas já implementadas no Python.
- **Biblioteca padrão** -> não está incluso no Python, precisa ser importada, mas já instalada junto com o pacote do Python.

**Fatiamento** -> forma de cortar um texto, exemplo: `string[:5]`, no exemplo, só é retornada os 5 primeiros caracteres da string.

Existe outra maneira de cortar uma string, quebrando a string a partir de um caractere, usando a função `split(caractere)`.

- `unset variavel` -> apaga uma variável de ambiente.
- `export variavel` -> altera o valor de uma variável de ambiente.
- `LANG=pt_BR python3 hello.py` -> exporta uma variável de ambiente diretamente ao executar um script Python, sobrescrevendo o valor padrão do sistema operacional.

### Tipos de Instruções: Expressions, Statements, Assignment

- **Expressão/Expression** -> instrução que espera um valor de retorno. Ex: `1+1`.
- **Declaração/Statement** -> instrução que prepara o interpretador para uma determinada tarefa mas não retorna valor. Ex: `if, else, def, for`.
- **Atribuição/Assignment** -> instrução que pega o retorno de uma expressão e processa o seu valor com intuito de armazenar. Ex: `soma = 40 + 2, soma += 3, soma -= 3`.

**Protocolos** -> o que o objeto é capaz de fazer.

O interpretador executa a linha sempre da esquerda para direita.

Precedência de operadores aritméticos (PEMDAS)

1. Parênteses.
2. Exponenciação e Raízes.
3. Multiplicação
4. Divisão.
5. Adição.
6. Subtração.

Precedência de operadores do Python

- 7(alto): exponenciação `**`.
- 6: multiplicação `*`.
- 5: adição `+,-`.
- 4: relacional `==,!=,<=,>=,>,<`.
- 3: lógico `not`.
- 2: lógico `and`.
- 1(baixo): lógico `or`.

### Blocos de código e identação

- Python não usa chaves para delimitar os blocos de código, ele usa 4 espaços em branco de identação(recuo) obrigatório.
- Os dois pontos (:) indica que a partir começa um bloco de código.
- Existem blocos condicionais e blocos de repetição.
- Para cada bloco de código aninhado, soma-se 4 espaços em branco, aumentando o recuo.
- É recomendável não passar de 3 a 4 níveis de identação.

### Ambientes virtuais e a ferramenta iPython

- O ambiente é aonde o programa/script vai ser executado.
- Para garantir que o programa/script rode corretamente e igualmente em todos os computadores se faz necessário a criação de um ambiente virtual.

É uma boa prática é criar um ambiente virtual do Python para todo projeto, evitando que danifique o sistema operacional, por conta de conflitos, separando todo o ambiente do projeto do ambiente real do computador.

- `python3 -m venv nome_do_ambiente` -> comando para criar um ambiente virtual utilizando a versão 3 do Python, uma conversão para nome de um ambiente é `.venv`, pois arquivos/pastas que utilizam "." antes do nome normalmente são ocultos e não aparecem no sistema de arquivo do SO.
- `source .venv/bin/activate` -> comando para ativar o ambiente virtual no Linux.

Não há necessidade de mandar a pasta do ambiente virtual para o repositório git.

- `python3 -m pip` -> módulo do Python destinado a instalação de pacotes.
- `python3 -m pip install ipython` -> instala a biblioteca iPython, um interpretador interativo melhorado de Python.
- `python3 -m pip install --upgrade pip` -> atualiza o pip para a última versão, recomendado sempre executar ao criar um novo ambiente virtual.

Ao usar `%time` no iPython antes de qualquer código, é mostrado o tempo de execução utilizado, além dos recursos computacionais.

## Dia 2 - Tipos de Dados e Protocolos

### A importância dos tipos de dados e o tipo inteiro

- Ao realizar uma operação de atribuição, o interpretador do Python realiza uma operação de inferência de tipo, para saber a maneira e o local correto de armazenar a informação na memória.

Tipo de dado também pode ser chamado de classe de dado ou categoria de dado.

O interpretador do Python converte um número inteiro para uma sequência de bits para armazená-los na memória.

- `bin(numero_inteiro)` -> retorna o valor em binário de qualquer número inteiro. Tudo que começa com `0b` no Python indica um número binário.

Na memória do computador, o identificador(nome da variável) está apontando para uma sequência de bits. Ao solicitar um dado da memória, o Python o converte para o contexto da aplicação, isso é realizado através do tipo de dado.

No caso de letras ou strings, cada letra é convertida para um número inteiro, depois converte novamente para binário e então é armazenado o valor binário na memória.

**Exemplo**

Como é realizado o armazenamento da operação de atribuição `numero = 65`.

- Em seguida, o interpretador vai identificar, através da inferência de tipos, qual o tipo daquele dado, neste caso, um inteiro(int).
- Depois, o interpretador cria um "envelope" e atribui a um espaço na memória RAM, numa posição qualquer.
- E dentro desse "envelope" o Python armazena o número inteiro "65" convertido para binário, que é "1000001".
- Finaliza colocando nesse "envelope" uma etiqueta contendo o nome da variável em questão, no caso "numero".

Ao solicitar essa variável `numero`, o interpretador Python vai buscar na memória o local que possui o identificador "numero" e ao ver que aquele valor é do tipo inteiro, o interpretador vai converter o número binário para um número inteiro e por fim, exibir na tela(output).

<hr>

- `id(variavel)` -> retorna o número, que é a posição em que se encontra aquela variável na memória RAM. Esses valores são aleatórios e não sequenciais.
- `type(variavel)` -> retorna qual o tipo do valor armazenado em uma variável qualquer.

Um objeto é um conjunto composto por um endereço de memória, um tipo, um valor e um identificador(nome da variável). Todo objeto possui as mesmas características.

Dado é o valor armazenado na memória, e é através do tipo de dado que esse dado é transformado em uma informação para ser compreendida.

Os tipos de dados são divididos em duas categorias: primários e compostos

#### Tipos de dados primários(Scalar Types)

- São tipos de dados que servem para representar apenas um único valor.

Um desses tipos de dado é o Tipo Inteiro(Integer), que é uma classe definida no código fonte do Python que juntamente do valor traz todo o comportamento específico dessa classe.

Não é necessário explicitamente dizer ao Python qual o tipo de objeto a guardar na memória, pois o interpretador faz isso dinamicamente.

- `int(valor)` -> força o tipo de um determinado valor para inteiro.
- `dir(tipo_de_dado)` -> retorna uma lista contendo todos os métodos e protocolos de um determinado tipo de dado, eles determinam quais operações que aquele objeto pode realizar.

**Métodos públicos**

- Qualquer método que não possui dunder, são chamados de métodos públicos.

**Protocolos**

- Já os protocolos(métodos que possuem dunder), determinam as operações e ações que o tipo de dado pode realizar, normalmente, não são utilizados. Tudo no Python vai funcionar através desses protocolos, que são vários.
- Existem protocolos que exigem apenas um método dunder, enquanto há protocolos que exigem mais de um método dunder para funcionar.

**Exemplos**

***Método Dunder Add***

Quando um objeto implementa o método `__add__()`, ele implementa o protocolo addible, significa que o objeto é capaz de receber adição de outros números.

- `numero + 1` = `numero.__add__(1)`

***Método Dunder Eq***

Implementa o método `__eq__()`, que implementa o protocolo equal, significa que o objeto pode realizar operações de comparações.

- `numero == 65` = `numero.__eq__(65)`

### Tipos Float, Bool, NoneType

Os tipos Float, Bool, NoneType são tipos primitivos.

**Tipo Float**

- É um número que além do número inteiro, possui uma parte fracionada, Float de ponto flutuante. Representa frações.
- É a presença de um ponto no número que faz com o Python trate como Float.
- Podem ser negativos ou positivos.

```python
valor = 2.0
type(valor) # float
valor.is_integer() # true

valor = 2
type(valor) # int
```

- Para representar valores monetários, o ideal é utilizar o tipo Decimal (ou Currency). Pois a precisão do tipo Decimal é maior do que a do tipo Float.

**Tipo Boolean**

- Pode ter apenas o valor True (Verdade) ou o valor False (Falso).
- Representado pelo nome `bool`.
- O número 0 é igual a False e o número 1 é igual a True.
- Expressões lógicas sempre retornam um booleano.
- O `if` só funciona com valores booleanos.
- Texto vazio é considerado como o valor 0 (False).
- Para o interpretador do Python todo valor numérico, diferente de 0, é True.

**Tipo NoneType**

- Apenas possui uma opção de valor, `None`, que significa nulo ou ausência de valor.
- No Python, todo objeto (variável) deve ser inicializado, sempre contendo um valor.
- Pode ser usado para inicializar uma variável que ainda não se sabe o valor, posteriormente, essa variável pode ter seu valor mudado.

**Singleton** -> objetos que podem ser criados uma única vez durante toda a execução do código.

Toda variável None terá a mesma posição na memória, independente da quantidade de variáveis com o valor `None` atribuído.

- Em alguns casos, funções irão retornar um valor `None`. Isso ocorre pois toda função, por ser uma expressão, deve retornar um valor.

### Textos, Caracteres, Encoding e Strings

- Tipos de dados que fica entre os tipos primário e os tipos compostos.

**String**

- Representa uma cadeia de caracteres.
- Objeto representado pela classe `str`.
- Criado usando aspas duplas ou aspas simples.

Textos com mais de um caractere são chamados de Bytearrays ou String. Cada caractere no texto é convertido para um byte e armazenado na memória, formando uma cadeia de bytes.

**Tabela ASCII**

- O interpretador do Python usa uma tabela padrão ASCII para converter um número inteiro em um caractere específico.
- Limitada, pois só possui os caracteres americanos.
- Por limitação de memória possui apenas 127 valores (caracteres).
- Os primeiros 33 caracteres são chamados de caracteres de controle.

**Tabela Unicode**

- Uma tabela única extendida que possuem muitos caracteres, além de emojis. Melhoria da Tabela ASCII.
- O interpretador do Python já converte automaticamente qualquer valor hexadecimal da Tabela Unicode ao usar a função `print()`.
- É um consórcio mundial de várias empresas.

**UTF-8**

- Tabela Unicode que em cada posição consegue armazenar 8 bits.
- Existem alguns caracteres da Tabela Unicode que ocupam mais de 8 bits.

**Serialização**

Conversão de um objeto Unicode em uma representação em texto em hexadecimal. Ideal utilizar para trafegar pela rede ou armazenar caracteres Unicode em servidores ou banco de dados que não suportam Unicode.

- `variavel.encode("utf-8")` -> converte para uma string que tem uma sequência hexadecimal que representa um caractere especial da Unicode.
- `variavel.decode("utf-8")` -> converte da sequência hexadecimal para o caractere especial da Unicode.
- `bytes(variavel, "utf-8")` -> retorna a representação em bytes do valor de uma variável, o segundo parâmetro informa qual a tabela que o interpretador vai utilizar para buscar esses valores.
- `string[numero]` -> fatiamento, fatia a string em várias formas. Também é possivel selecionar um intervalo de caracteres da string, usando `[inicio:fim]`.
- `len(variavel)` -> retorna o número de itens dentro de um objeto que pode armazenar outros objetos, pode ser usado em uma string para retornar a quantidade de caracteres.

É possível concatenar apenas textos usando o caractere `+`, exemplo: `"Giovanni" + "Padilha"`.

Também é possível multiplicar textos, `"Giovanni" * 2` = `"GiovanniGiovanni"`.

Strings são percorríveis, podendo percorrer cada caractere como se a string fosse uma lista contendo caracteres.

- `next(variavel_iteravel)` -> retorna o próximo objeto de um objeto iterável.
- `string.upper()` -> retorna toda a string em maiúsculo.
- `string.lower()` -> retorna toda a string em minúsculo.
- `string.capitalize()` -> coloca a primeira letra da primeira palavra da string em maiúsculo.
- `string.title()` -> coloca a primeira letra de todas as palavras da string em maiúsculo.
- `string.split(caractere)` -> separa a string em uma lista, cortando com base em um caractere especificado.
- `string.startswith(caractere)` -> verifica se a string começa com o caractere especificado, retornando True ou False.

Esses métodos podem ser usados em cadeia. Por exemplo: `string.upper().split()`.

Strings podem ser comparadas, de acordo com o valor daquele caractere na tabela Unicode ou ASCII.

- `sorted(string)` -> retorna uma lista de caracteres em ordem alfabética.
- `reversed(string)` -> retorna um objeto do tipo reversed (pode ser convertido para uma lista) com os caracteres começando do fim.

Os dois métodos acima apenas funcionam pois o objeto `str` implementa o protocolo dunder `__eq__`.

As strings estão entre os objetos primários e compostos pois, uma string armazena semânticamente um único valor, porém internamente, o Python grava uma sequência de caracteres a partir dessa string.

### Formatação de Textos

#### Concatenação

- É possível concatenar várias strings, ex: `'Giovanni' + 'Padilha' = 'Giovanni Padilha'`.
- O operador `+` apenas concatena string com string, para concatenar outros tipos de dados com strigs se utiliza o operador `,`, ou então converter a variável para string usando `str()`. Isso ocorre pois o Python é de tipagem forte.

#### Interpolação

- Define a mensagem (string) antes, criando um template.
- Nesse template, terá os placeholders que é o local que vai ser substituído na string por um valor de uma variável. Esses placeholders são definidos usando o operador de `%` seguido de uma letra, ex: `%s`.
  - `%s` indica um placeholder para strings.
  - `%d` indica um placeholder para integers. Para indicar a quantidade de dígitos `%03d`.
  - `%f` indica um placeholder para floats. Para indicar quantas casas decimais mostrar `%.2f`.

Para substituir esses placeholders por valores de variáveis utiliza: `template % (variavel_1, variavel_2, ...)`.

Útil para usar na biblioteca `logging`.

**Parâmetros Nomeados**

- Atribui um nome para o placeholder, usado em textos muito grande.
- Sintaxe: `%(nome)s`

Para atribuir valores a esses placeholders se usa um dicionário `template % {'nome':'Giovanni', chave: valor, ...}`.

#### String Format

- Método `str.format()`.
- New style, forma mais recente de formatar textos no Python3.
- Em vez de utilizar `%`, utiliza `{}`.
- Para formatar segue o mesmo padrão da Interpolação, a diferença é que vem `:` antes da especificação.

Útil para mensagens longas, como e-mails.

*Exemplo*

```python
msg = "Olá, {} você é o player n {:03d} e você tem {:.2f} pontos"

msg.format("Giovanni", 2, 987.3)
```

**Extras**

- Centraliza textos `{:^10}.format("Giovanni")`, o número 10 é o tamanho do espaço, centraliza em 10 caracteres.
- Alinha a esquerda `{:<10}.format("Giovanni")`.
- Alinha a direita `{:>10}.format("Giovanni")`.
- Preenche os espaços em branco com um caractere especificado `{:#^10}.format("Giovanni")`, preenche com `#`.
- Corta uma string `{:^10.3}.format("Giovanni")`, usando em valores floats imprime uma representação abreviada.

**Chaves Nomeadas**

- Atribui nome as chaves, ex: `{pontos:.2f}`.

Substituindo os placeholders nomeados `str.format(nome_variavel=valor, ...)`

#### f-strings

- A partir do Python3, nova sintaxe de aplicar `str.format`.
- Sintaxe simplificada: `f"Olá, {nome}"`
- Obrigatório aplicar um nome para os placeholders. E cade placeholder se refere a uma variável existente, se não existir a variável, retorna erro.

Uso geral, qualquer tipo de mensagem.

#### Emojis

Há duas formas de imprimir emojis no Python.

- A primeira forma é através do código unicode do emoji. Utiliza `\U000` antes do código do emoji.
- A segunda forma é substituir o `\U` pelo nome do emoji usando `\N{nome_emoji}`.

### Tipos de Dados Compostos e Tuplas

- Capaz de armazenar (como um contâiner) mais de um único valor, até mesmo diferentes tipos de dados.

#### Sequência

- Um único objeto na memória, que possui um nome.
- Dentro desse objeto sequência, terá posições que vão referenciar aos objetos contidos dentro desse contâiner. Cada objeto dentro de um contâiner vai ser armazenado na memória separadamente, da mesma forma que uma variável individual, tendo sua posição, tipo de dado e valor.

#### Tuplas (Tuple)

- Cria uma sequência de objetos heterogêneos.
- Cada objeto é separado por vírgulo, e os objetos como um todo são armazenados dentro de uma Tupla.

<hr>

- `tuple.count(valor)` -> retorna a quantidade de vezes que um determinado valor é encontrado dentro de uma Tupla.

A Tupla pode ser subscrita, ex: acessando o último valor da tupla `tuple[-1]`. As Tuplas são acessados pelo índice, começando por 0, ao usar índices negativos o acesso é feito do inverso. É o fatiamento, ex: `tuple[indice_inicial:indice_final]`

- Também pode ser iterada.
- É opcional o uso de parênteses ao realizar a atribuição, apenas as vírgulas são obrigatórios, é a partir delas que vai ser inferido o tipo de dado Tuple.
- A Tupla é imutável, a partir de sua criação, ela não pode ser alterada.

**Desempacotamento de Tupla**

- Desempacota uma Tupla em várias variáveis separadas, ao mesmo tempo.

*Ex:*

```python
pontos = 2, 1, 99

x, y, z = pontos

# x = 2
# y = 1
# z = 99
```

- Para ignorar valores, basta usar o operador `*_` no local da variável em questão.
- Também podem ser desempacotados o primeiro valor e o último elemento, ex: `primeiro, *_, ultimo = valores`.
- `len(objeto)` -> retorna o tamanho apenas de sequências materializadas.

### Listas

- Objeto "padrão" no Python para sequências.
- Podem ser comparadas com arrays ou vetores, com diferenças!
- Uma lista é declarada usando `[]` (preferível) ou `list()`.
- Pode ser criada vazia, pois é um objeto mutável, pode ser alterada após ser criada.
- Todas as operações com Tuplas também é possível fazer com uma Lista.
- É permitido somar Listas uma com a outra. E o resultado dessa soma é uma outra Lista com a junção dos objetos das duas Listas.

<hr>

- `list.append(valor)` -> adiciona um objeto ao final de uma lista.
- `list.insert(posicao, valor)` -> adiciona um objeto em uma posição (índice) específico.
- `list.remove(valor)` -> remove o primeiro valor encontrado na lista, mesmo que haja dois valores iguais.
- `list.extend(list)` -> extende uma Lista com outra Lista, sem criar um objeto novo. Funciona igual com o operador `+=`.
- `list.count(valor)` -> retorna quantas vezes aparece um valor dentro de uma lista.
- `list.pop()` -> remove o último valor da lista.

Possível usar `in` em Listas, retornando True se achar ou False se não encontrar, ex: `valor in list`. Em alguns objetos ele é lento!