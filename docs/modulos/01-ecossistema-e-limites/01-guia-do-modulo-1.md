# B1 · Ecossistema OpenAI

> Mascote da unidade: **Atlas**
>
> Fontes de produto devem ser conferidas em [fontes canônicas](../../fontes.md)
> no dia de cada aula, pois planos, superfícies e disponibilidade variam.

## Propósito

Construir o vocabulário que evita decisões confusas: uma pessoa não escolhe
“uma IA” de forma abstrata; escolhe uma superfície, um fluxo, uma permissão e
uma forma de revisão para um objetivo concreto.

## Os quatro blocos obrigatórios

| Bloco | Questão que a unidade responde | Limite de decisão |
| --- | --- | --- |
| ChatGPT | Quando uma interface conversacional e suas ferramentas ajudam? | Não presume disponibilidade de um recurso por plano ou região. |
| Codex | Quando o trabalho é uma tarefa em projeto, arquivos ou repositório? | Não substitui revisão de diff, testes e permissões proporcionais. |
| API Platform | Quando é necessário integrar modelos e ferramentas a uma aplicação? | Exige projeto, autenticação, custo, tratamento de erro e observabilidade. |
| Vocabulário | O que muda entre modelo, produto, ferramenta, agente e app? | Os termos não são intercambiáveis. |

## O que está documentado e o que é decisão pedagógica

### Fatos documentados — verificados em 05-08-2026

- A documentação do ChatGPT na web descreve seu uso para pesquisar, analisar e
  criar arquivos. Seus recursos efetivamente disponíveis dependem da conta,
  do plano, da plataforma, da região, do rollout e das políticas aplicáveis.
- O Codex possui superfícies para terminal/CLI, IDE e cloud; a superfície muda
  o contexto de trabalho, mas não elimina a necessidade de revisar alterações
  e validações.
- A API oferece uma interface para integrar modelos a aplicações. A documentação
  de início rápido exige uma chave de API mantida em local seguro, e os SDKs a
  leem a partir do ambiente.

Fontes primárias: [ChatGPT na web](https://learn.chatgpt.com/docs/web.md),
[Codex CLI](https://learn.chatgpt.com/docs/codex/cli.md) e
[Developer quickstart](https://developers.openai.com/api/docs/quickstart.md).

### Inferência pedagógica

Escolher “processo manual” é correto sempre que a ação não pode ser delegada,
os dados excedem o escopo aprovado ou a revisão humana disponível não é capaz
de controlar o impacto. Isso não é uma capacidade de produto; é um critério de
decisão do curso.

## Modelo mental

- **Modelo**: componente que recebe contexto e produz uma resposta.
- **Produto**: experiência pronta para uma pessoa operar, como uma interface.
- **Ferramenta**: capacidade disponível dentro de um produto ou aplicação.
- **Agente**: sistema que usa modelo, instruções, ferramentas e regras para
  avançar uma tarefa.
- **App**: aplicação que integra uma experiência, dados, interface e regras.

Essas definições são pedagógicas. As capacidades concretas devem ser verificadas
na documentação oficial e na conta que será usada.

## Roteiro de decisão inicial

Antes de escolher uma superfície, responda na ordem abaixo:

1. Qual é o objetivo observável e qual artefato deve existir ao final?
2. Há dados sensíveis, segredos ou uma política que proíba esse uso?
3. O trabalho acontece numa conversa, num projeto/repositório ou numa aplicação?
4. Ele precisa ser repetível por software e integrado a outros sistemas?
5. Qual é o impacto de uma resposta ou ação errada?
6. Quem revisará o resultado, o diff ou a decisão antes de agir?

A escolha é provisória: ela pode mudar quando o risco, o contexto ou os
requisitos mudarem. B1 não ensina a redigir prompts (B2), usar ferramentas do
ChatGPT (B3), nem construir uma integração de API (P1 em diante).

## Conexão com a próxima unidade

B1 escolhe a superfície e delimita o problema. B2 ensinará a formular contexto,
instruções, critérios e formatos sem repetir a taxonomia desta unidade.

