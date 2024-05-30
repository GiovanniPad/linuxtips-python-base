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
