# Módulo 1 — Ecossistema e limites de LLM

> Mascote do módulo: **Atlas**
> Tom: técnico, limpo, com missão de decisão.

## Objetivo de aprendizagem

Ao final do módulo, você deverá conseguir:

- Identificar em quais cenários **usar ou não** um LLM para resolver uma tarefa.
- Distinguir “o que a ferramenta faz” do “como a ferramenta deve ser supervisionada”.
- Escolher uma estratégia inicial (ChatGPT/Codex/sem LLM) com justificativa curta e rastreável.

## Missão de treino (roteiro)

Você é operador de uma célula de produtividade do curso. Recebe três demandas reais e precisa decidir o caminho técnico mais seguro e eficiente para cada uma.

1. **Entradas não triviais** aparecem no início de qualquer pedido (texto, código, regras, risco, prazo).
2. **Cada decisão precisa de critério**, não de achismo.
3. **Escolha de ferramenta ≠ sucesso automático**: toda decisão precisa de revisão humana no fim.

## O que esse módulo cobre

- Ecossistema prático de uso do ChatGPT e do Codex em contexto de curso/produto.
- Tipos de tarefas e limites comuns dos modelos de linguagem.
- Risco de ferramenta inadequada (ex.: ambiguidade, privacidade, precisão técnica).
- Critérios de custo de tempo/risco antes de executar.

## O que esse módulo não cobre (e propositalmente fica para frente)

- Engenharia de prompt avançada fina (`Módulo 2`).
- Validação factual profunda com protocolo de prova (`Módulo 3`).
- Segurança operacional e plano de resposta a incidente (`Módulo 4`).
- Otimização de automações, API e fluxos avançados (`Módulo 7`).

## Matriz de decisão — versão inicial

Antes de enviar qualquer pedido, responda:

1. O objetivo é **exploração**, **síntese**, **edição local** ou **decisão operacional**?
2. O conteúdo é **sensível** (dados pessoais, segredos, chaves, credenciais)?
3. Você precisa de:
   - saída criativa
   - resposta argumentativa
   - edição segura de arquivo real
4. Existe risco de erro com impacto real (financeiro, jurídico, pessoal)?

### Regra prática de escolha

Use esta régua para iniciar:

- **ChatGPT (conversa)**: ideal para pesquisa exploratória, síntese, redação e discussão de estratégia.
- **Codex (execução local/repo)**: ideal quando há um artefato versionado, mudança rastreável e necessidade de executar ação no projeto.
- **Sem LLM**: ideal para tarefas repetitivas, checagens objetivas e decisões já conhecidas.

## Limites operacionais que você deve assumir desde já

- Toda resposta de IA pode conter incerteza.
- Modelos seguem o contexto que recebem; instruções fracas geram saída fraca.
- Ambiguidade no pedido vira ambiguidade no resultado.
- Não substitui revisão humana em decisões com impacto.
- Recursos, planos e recursos disponíveis mudam com região, conta e período; atualize a escolha por contexto.

## Entrega mínima do módulo (prévia)

No seu registro de entrega, você deve apresentar:

- uma comparação de 3 cenários reais com ferramenta escolhida
- justificativa objetiva (1–3 linhas por cenário)
- risco principal de cada escolha e como mitigar

> Referência de navegação: entregue em `docs/entregas/01-ecossistema-e-limites/template-entrega-modulo-1.md`.
