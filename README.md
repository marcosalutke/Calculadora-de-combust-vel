## Calculadora de Combustível

Este é um projeto pessoal nascido da necessidade real de colocar os gastos do carro na ponta do lápis. Seja para planejar aquela viagem de fim de semana ou apenas para descobrir qual bomba de combustível vai doer menos no bolso no fim do mês, este aplicativo resolve a matemática de forma rápida e visual.

Desenvolvido com foco na simplicidade, este é o MVP (Produto Mínimo Viável) de uma ferramenta de utilidade diária para motoristas.

---

## ✨ Funcionalidades

O aplicativo é dividido em duas frentes principais:

### 1. Calculadora de Viagem 🛣️
Planeje sua rota antes de tirar o carro da garagem:
* **Cálculo de Ida e Volta:** Um clique para dobrar a distância automaticamente.
* **Flexibilidade de Consumo:** Suporta tanto o padrão brasileiro (`km/ℓ`) quanto o padrão internacional (`ℓ / 100 km`).
* **Visão de Custos:** Entrega mastigado o total de litros necessários, o custo exato por quilômetro rodado e o impacto total no bolso.

### 2. Etanol x Gasolina (O Tira-Teima) ⛽
Chegou no posto e ficou na dúvida? 
* Insira o preço do Etanol e da Gasolina.
* O sistema calcula a proporção exata entre os dois.
* Retorna o veredito de qual combustível é a escolha financeira mais inteligente para o abastecimento no momento (baseado na regra padrão de eficiência de 70%).

---

## 🛠️ Tecnologias Utilizadas

A versão atual foi construída de forma enxuta para rodar diretamente no desktop:
* **Python 3:** Lógica de negócio e cálculos matemáticos.
* **Tkinter (ttk):** Construção da Interface Gráfica de Usuário (GUI) nativa e responsiva, sem necessidade de bibliotecas externas pesadas.

---

## 🚀 Como Rodar o Projeto na Sua Máquina

Para testar a calculadora, você só precisa ter o Python instalado no seu computador. Siga os passos abaixo:

**1. Clone este repositório:**
Abra o seu terminal e digite:
```bash
git clone https://github.com/marcosalutke/Calculadora-de-combust-vel
