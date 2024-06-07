# Objetivo

Validar a possibilidade de um agente conversacional que fosse capaz de realizar uma escuta empática com uma pessoa, apoiando-a na compreensão de sentimentos e necessidades presentes em situações diversas.

# Plano de Ação

1. Buscar datasets de escuta empática ou de alguma área adjacente, preparar dados.

    - [x] Coletar dados estruturados do Juliano Rigatti.
    - [ ] Pesquisar outros datasets.
    - [ ] Utilizar o GPT para anotar as conversas do ouvido classificando por necessidades atendidas e validar manualmente.

2. Criar dois agentes conversasionais com o GPT para realizar a escuta empática. Um para ser o ouvinte e outro para ser o ouvido.

    - [x] Começar apenas com prompt egnineering, criar prompts para tentar simular utilizando os recursos padrões do gpt-3.5
        - a resposta da prompt 1 ainda é muito longa, precisa de alterações.

    - [ ] Utilizar uma RAG para aprimorar a qualidade de conversação.
    - [ ] Realizar o fine tunning do modelo.

3. Criar uma maneira de avaliar textos produzidos com base aos fornecidos pelos exemplos.

    - [x] Análise manual.
    - [ ] [NLTK Sentimental Analysis](https://www.nltk.org/howto/sentiment.html).

# Ferramentas

- [ ] UI e backend para facilitar o teste, armazenamento e anotação dos dados.