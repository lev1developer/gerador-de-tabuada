# Gerador de Tabuada

Agora não tem mais desculpa pra dizer que não sabe a tabuadakkkkkkkkkk

## Funcionalidades

- Solicita um número inteiro ao usuário.
- Gera a tabuada de multiplicação desse número.
- Exibe os resultados no terminal.

## Código utilizado

```python
tabuada = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {tabuada}:")

for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")
```

## Conceitos praticados

- `input()`: recebe informações digitadas pelo usuário.
- `int()`: converte o valor recebido para um número inteiro.
- `for`: estrutura de repetição utilizada para executar um bloco de código várias vezes.
- `range()`: define o intervalo de repetição.
- **f-strings**: permitem inserir variáveis diretamente em textos.
- Operadores aritméticos: utilização da multiplicação (`*`).

## Exemplo de execução

```text
Digite um número para ver a tabuada: 7
Tabuada do 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

## 🎯 Objetivo do exercício

Praticar estruturas de repetição com `for` e `range()`, além de trabalhar com entrada de dados, conversão de tipos e operações matemáticas em Python.

---

**Projeto desenvolvido como parte dos meus estudos de Python e lógica de programação.**
