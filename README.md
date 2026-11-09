# 🧮 Calculadora Matemática em Python

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Versão](https://img.shields.io/badge/Versão-3.0-blue)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Projeto](https://img.shields.io/badge/Projeto-Educacional-informational)
![Interface](https://img.shields.io/badge/Interface-Terminal-purple)

## 📖 Sobre o projeto

A **Calculadora Matemática** é uma aplicação desenvolvida em **Python 3**, com o objetivo de realizar operações aritméticas básicas de maneira simples, interativa e acessível.

O programa permite realizar adição, subtração, multiplicação e divisão, oferecendo instruções claras para cada operação e verificando as informações digitadas pelo usuário.

Seu principal diferencial é o **tratamento de entradas inválidas**: quando uma informação incorreta é inserida, o sistema explica o problema, orienta como resolvê-lo e solicita uma nova entrada, sem perder as informações válidas fornecidas anteriormente.

O projeto foi desenvolvido para praticar lógica de programação, estruturas condicionais, estruturas de repetição, funções e tratamento de exceções.

## ⚙️ Funcionalidades

- Realização das quatro operações matemáticas básicas.
- Menu explicativo com exemplos de cada operação.
- Seleção de operações utilizando apenas símbolos matemáticos.
- Aceitação de números positivos, negativos e decimais.
- Reconhecimento de vírgula e ponto como separadores decimais.
- Validação das operações selecionadas.
- Identificação de campos vazios e entradas não numéricas.
- Mensagens explicativas para orientar o usuário.
- Repetição automática da entrada quando um valor inválido é informado.
- Bloqueio de divisões por zero.
- Rejeição de valores infinitos e `NaN`.
- Identificação de resultados não finitos.
- Tratamento de exceções durante a execução.
- Encerramento controlado por interrupção do usuário.
- Exibição organizada do resultado final.

## ➕ Operações disponíveis

O programa utiliza somente quatro símbolos para selecionar as operações.

| Símbolo | Operação | Exemplo |
|:---:|---|---|
| `+` | Adição | 10 + 5 = 15 |
| `-` | Subtração | 10 - 5 = 5 |
| `*` | Multiplicação | 10 × 5 = 50 |
| `/` | Divisão | 10 ÷ 5 = 2 |

O usuário deve informar exclusivamente o símbolo correspondente à operação desejada.

Por exemplo, para realizar uma multiplicação, deve digitar `*`, e não a palavra `multiplicação`.

## 🖥️ Como funciona o programa?

### 1. Seleção da operação

Ao iniciar, o sistema apresenta um menu explicativo:

```text
====================================
       CALCULADORA MATEMÁTICA
====================================

Escolha uma das operações abaixo:

+ = ADIÇÃO: soma dois números.
- = SUBTRAÇÃO: subtrai o segundo número do primeiro.
* = MULTIPLICAÇÃO: multiplica dois números.
/ = DIVISÃO: divide o primeiro número pelo segundo.

ATENÇÃO: digite somente o símbolo da operação desejada.
```

O usuário seleciona uma das quatro operações.

Caso informe uma opção inválida, o programa explica quais símbolos são aceitos e solicita uma nova escolha.

### 2. Entrada dos números

Após selecionar a operação, o programa solicita dois valores numéricos.

Exemplo:

```text
Digite o primeiro número: 10
Digite o segundo número: 5
```

São aceitos valores como:

- `10` — número inteiro positivo.
- `-5` — número negativo.
- `2.5` — número decimal com ponto.
- `2,5` — número decimal com vírgula.
- `0` — zero, exceto como divisor.

Se o usuário digitar uma informação inválida, o sistema solicita novamente apenas o valor incorreto.

### 3. Exibição do resultado

Após validar as entradas e realizar o cálculo, o programa apresenta:

```text
====================================
           RESULTADO FINAL
====================================

Primeiro número: 10.0
Operação: +
Segundo número: 5.0
Resultado: 15.0

Cálculo concluído com sucesso!
```

## 🛡️ Sistema de validação de dados

A versão 3.0 possui verificações para evitar erros comuns durante a utilização.

| Situação | Comportamento do programa |
|---|---|
| Operação inválida | Explica os símbolos permitidos e solicita outra operação |
| Campo numérico vazio | Solicita um número válido |
| Letras no lugar de números | Apresenta orientação e repete a entrada |
| Número decimal com vírgula | Converte a vírgula em ponto |
| Divisão por zero | Explica o erro matemático e solicita outro divisor |
| Entrada `NaN` | Rejeita o valor |
| Entrada `Infinity` | Rejeita o valor |
| Número fora do intervalo finito de `float` | Rejeita a entrada |
| Resultado não finito | Solicita outro segundo número |
| Interrupção com `Ctrl+C` | Encerra o programa com uma mensagem |

### Exemplo: operação inválida

```text
Digite a operação (+, -, * ou /): soma

ERRO: operação inválida!
Você deve digitar apenas um destes símbolos:
+ para adição
- para subtração
* para multiplicação
/ para divisão
Tente novamente.
```

O programa permanece na seleção da operação até receber uma opção válida.

### Exemplo: divisão por zero

```text
Digite a operação (+, -, * ou /): /
Digite o primeiro número: 10
Digite o segundo número: 0

ERRO MATEMÁTICO: divisão por zero não é permitida.
O segundo número precisa ser diferente de zero.
Exemplos válidos: 1, 2, -5 ou 0,5.
```

Nesse caso, o sistema mantém a operação e o primeiro número, solicitando novamente apenas o divisor.

### Exemplo: entrada não numérica

```text
Digite o primeiro número: abc

ERRO: você não informou um número válido.
Digite apenas números, como 10, -5 ou 2,5.
Não utilize letras ou símbolos matemáticos neste campo.
```

O usuário recebe instruções para corrigir a informação antes de prosseguir.

## 🧠 Conceitos de programação aplicados

| Conceito | Aplicação |
|---|---|
| Variáveis | Armazenamento das operações e dos números |
| Funções | Organização da validação e dos cálculos |
| `input()` | Recebimento de informações |
| `float()` | Conversão de valores numéricos |
| `while True` | Repetição de entradas até serem válidas |
| `if`, `elif`, `else` | Seleção de operações e validações |
| `try` e `except` | Tratamento de exceções |
| `return` | Retorno de valores das funções |
| `continue` | Repetição de uma entrada inválida |
| `break` | Encerramento de um laço após entrada válida |
| `.strip()` | Remoção de espaços nas extremidades |
| `.replace()` | Conversão de vírgula decimal em ponto |
| `math.isfinite()` | Verificação de valores numéricos finitos |
| `SystemExit` | Encerramento controlado do programa |

## 🧩 Estrutura do código

O programa possui duas funções principais.

### `ler_numero(mensagem, divisor=False)`

Responsável por receber e validar os números informados pelo usuário.

Essa função:

- Solicita a entrada numérica.
- Converte o texto para `float`.
- Verifica se o valor é finito.
- Rejeita entradas inválidas.
- Impede zero como divisor quando necessário.
- Repete a solicitação até receber um valor válido.

### `calcular(numero1, numero2, operacao)`

Responsável por realizar a operação matemática selecionada.

Essa função:

- Identifica a operação desejada.
- Executa o cálculo correspondente.
- Trata exceções de cálculo.
- Verifica se o resultado é finito.
- Retorna o resultado válido ou `None` quando não é possível representá-lo adequadamente.

## 📁 Estrutura do projeto

```text
Calculadora-Matem-tica/
│
├── calculadora.py
│
└── README.md
```

**`calculadora.py`**

Arquivo principal, contendo o menu, as funções, as validações e os cálculos matemáticos.

**`README.md`**

Documentação com instruções de utilização, funcionalidades e informações técnicas.

## 🛠️ Tecnologias utilizadas

**Python 3**

Linguagem utilizada para implementar a lógica matemática e a interação pelo terminal.

**Biblioteca `math`**

Biblioteca padrão do Python utilizada para verificar se números e resultados são finitos.

O projeto não necessita de bibliotecas externas.

## 🚀 Como executar

### Pré-requisitos

Ter o Python 3 instalado no computador.

### Passo 1 — Clonar o repositório

```bash
git clone https://github.com/nunes39-cmyk/Calculadora-Matem-tica.git
```

### Passo 2 — Acessar o diretório

```bash
cd Calculadora-Matem-tica
```

### Passo 3 — Executar o programa

```bash
python calculadora.py
```

Em sistemas que utilizam o comando `python3`:

```bash
python3 calculadora.py
```

Também é possível executar o código em compiladores online com suporte a Python.

## ⚠️ Limitações técnicas

O projeto utiliza o tipo numérico `float`, que possui limitações de precisão e representação.

Por exemplo:

```python
0.1 + 0.2
```

Pode produzir:

```text
0.30000000000000004
```

Esse comportamento ocorre devido à representação binária de números decimais em ponto flutuante.

Além disso, valores extremamente pequenos podem ser arredondados para zero.

A calculadora realiza verificações para impedir resultados não finitos, mas não oferece precisão decimal arbitrária nem elimina todas as limitações do tipo `float`.

Para aplicações financeiras ou cálculos que exigem precisão decimal específica, seria recomendável utilizar o módulo `decimal` do Python.

## 🔮 Possíveis melhorias futuras

- [ ] Permitir vários cálculos na mesma execução.
- [ ] Adicionar um menu para reiniciar ou encerrar.
- [ ] Implementar histórico de operações.
- [ ] Melhorar a apresentação de resultados decimais.
- [ ] Implementar cálculos com `Decimal`.
- [ ] Criar testes automatizados.
- [ ] Desenvolver uma interface gráfica.
- [ ] Adicionar novas operações matemáticas.

## 🎯 Objetivo do projeto

O objetivo principal é desenvolver conhecimentos fundamentais em Python e lógica de programação por meio da construção de uma aplicação funcional.

A versão 3.0 busca aprimorar especialmente três aspectos:

**Usabilidade:** fornecer instruções claras para o usuário.

**Validação:** identificar entradas inválidas e permitir sua correção.

**Confiabilidade:** tratar erros comuns e evitar operações matemáticas indefinidas.

O projeto também registra a evolução do aprendizado em programação, desde uma calculadora básica até uma versão com funções, validações e tratamento de exceções.

## 👨‍💻 Autor

**Miguel Nunes Ribeiro**

Estudante de Análise e Desenvolvimento de Sistemas.

GitHub: [@nunes39-cmyk](https://github.com/nunes39-cmyk)

---

⭐ Projeto desenvolvido para fins educacionais, prática de lógica de programação em Python e construção de portfólio.
