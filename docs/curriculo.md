# Currículo por módulo — evolução do básico ao avançado

## Princípio de desenho do curso

O curso é modular, progressivo e em cadeia causal:

- nenhum módulo depende de habilidade não apresentada antes;
- não há repetição de conteúdo entre módulos;
- cada módulo tem:
  1) base conceitual mínima;
  2) prática guiada;
  3) entrega verificável;
  4) critério de transição para o próximo módulo.

O formato será lúdico para jovens adultos: linguagem de missão, checkpoints,
simulações, erros reais e revisão de risco.

## Mapa consolidado de dependências

1. `Diagnóstico e missão inicial`
   → define metas pessoais e cria a base técnica do ambiente.
2. `Módulo 1 — Ecossistema e limites de LLM`
3. `Módulo 2 — Comunicação eficiente com ChatGPT`
4. `Módulo 3 — Qualidade, evidência e validação`
5. `Módulo 4 — Segurança, privacidade e governança`
6. `Módulo 5 — Git, rastreabilidade e trabalho orientado a evidência`
7. `Módulo 6 — Codex para engenharia de tarefas`
8. `Módulo 7 — Integração de ferramentas e automações`
9. `Módulo 8 — Projeto final integrado (Nível avançado)`

Cada etapa só avança quando a anterior está comprovada por evidência no repositório.

## Trilha por módulo

| Etapa | Resultados de aprendizagem | Escopo delimitado | Entrega mínima |
| --- | --- | --- | --- |
| Diagnóstico e missão inicial | Mapear objetivos, repertório prévio e contexto de uso. | Onboarding, metas, estrutura da trilha, configuração inicial e plano pessoal. | Formulário de diagnóstico + checklist de ambiente funcional. |
| Módulo 1 — Ecossistema e limites de LLM | Explicar diferenças entre modelos, planos, modos de uso e custo básico. | Conceito de funcionamento, alcance e limites de modelos. Sem entrar em tuning/extensão avançada ainda. | Página de comparação entre cenários com justificativa de escolha do recurso. |
| Módulo 2 — Comunicação eficiente com ChatGPT | Construir prompts com contexto, papel, formato e critérios de saída. | Técnicas de interação e engenharia de conversa; sem introduzir ainda automações. | Laboratório de reescrita, síntese e instrução de procedimento com evidência de saída correta. |
| Módulo 3 — Qualidade, evidência e validação | Diferenciar fato documentado, inferência e hipótese. | Fontes oficiais, revisão de consistência e detecção de alucinação controlada. | Relatório curto com 3 exemplos de validação de resposta. |
| Módulo 4 — Segurança, privacidade e governança | Aplicar limites de compartilhamento e checagem de risco. | Threat model, dados sensíveis, viés, fallback e plano de contenção. | Matriz de risco aplicada a 2 cenários reais de uso. |
| Módulo 5 — Git, rastreabilidade e trabalho orientado a evidência | Versionar tarefas e decisões com histórico auditável. | Regras de commit, revisão, logs de decisão e documentação. | Mini projeto com branch, commits, revisão e changelog de evidência. |
| Módulo 6 — Codex para engenharia de tarefas | Traduzir objetivo funcional em instrução executável com verificação. | Uso de Codex em tarefas reais de edição, busca de contexto e revisão. Sem entrar ainda em integração API pesada. | Mudança ponta a ponta com evidência de entrada, edição e checagem. |
| Módulo 7 — Integração de ferramentas e automações | Orquestrar apps e fluxo com automações simples e controláveis. | Ligação de fontes, scripts e APIs em um mini fluxo funcional. | Protótipo de automação com logs de execução e critério de rollback. |
| Módulo 8 — Projeto final integrado | Unificar módulos 1 a 7 em solução completa e explicável. | Entrega final com documentação, custo estimado, limitações e plano de manutenção. | Projeto final com banca de validação, evidência e plano de evolução. |

## Regras de não sobreposição

- 1 e 2: não misturam técnica de validação com validação prática.
- 2 e 3: não repetem conceitos de prompting na discussão de evidência.
- 3 e 4: não confundem consistência factual com segurança de operação.
- 5 e 6: Git e rastreabilidade aparecem antes da automação de mudanças no código.
- 6 e 7: Codex é a base de engenharia; integração é aplicação orquestrada.

## Método de profundidade pedagógica

- Não é enciclopédico: cada módulo aprofunda só o que será usado no próprio módulo e no próximo.
- Não é superficial: todo módulo tem uma entrega verificável e um mini erro proposital para depuração.
- Cada laboratório tem:
  - objetivo mensurável,
  - dados/inputs,
  - critérios de conclusão,
  - revisão de falha frequente,
  - uma versão “melhor prática”.

## Conexão com o mapa visual

As fases 1 a 4 do mapa (`diagnóstico`, `fundamentos` e `laboratório básico`) continuam válidas.
As fases 5 a 8 consolidam a trilha de `workflow`, `specialização` e `projeto final`.
