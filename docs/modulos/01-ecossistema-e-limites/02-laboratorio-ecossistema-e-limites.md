# Laboratório 1 — Decisão de ecossistema com responsabilidade

## Objetivo

Aplicar os critérios do módulo em situações de uso real do projeto:

- reconhecer o tipo de tarefa;
- escolher ferramenta;
- registrar justificativa e risco;
- propor uma revisão humana antes de concluir.

## Materiais

- `docs/modulos/01-ecossistema-e-limites/01-guia-do-modulo-1.md`
- `docs/entregas/01-ecossistema-e-limites/template-entrega-modulo-1.md`
- Painel interativo: selecione o **Módulo 1** em `app/main.py` para preencher
  o laboratório e baixar uma versão inicial da entrega em Markdown.
- Editor de texto (ou o próprio repositório local).

## Cenários

Escolha uma ferramenta para cada cenário e complete a tabela pedida no template.

### Cenário 1 — Planejar estudo de um capítulo

**Contexto:** você precisa resumir 5 páginas de estudo e criar 4 perguntas para revisão amanhã.
**Risco principal:** baixa perda de precisão, risco de “resposta vaga”.
**Ferramenta provável:** ChatGPT (conversa) com critérios de forma (pontos, perguntas e nível).

### Cenário 2 — Ajustar configuração da base de curso no repositório

**Contexto:** deseja padronizar texto em 3 arquivos (`README.md`, `docs/plano-de-entrega.md`, `app/main.py`) com formato específico.
**Risco principal:** editar arquivo errado sem revisão.
**Ferramenta provável:** Codex para alteração rastreável no repositório (e validação após a mudança).

### Cenário 3 — Informar custo/benefício para um colega

**Contexto:** colega quer escolher entre “usar IA para tudo” ou “usar IA apenas para rascunho”, com prazo curto.
**Risco principal:** decisão desalinhada ao risco real de operação.
**Ferramenta provável:** ChatGPT (conversa) com matriz de decisão curta e limites explícitos.

### Cenário 4 — Conteúdo confidencial

**Contexto:** análise de mensagem com dados pessoais e chaves temporárias da equipe.
**Risco principal:** vazamento/uso indevido de dados.
**Ferramenta provável:** avaliação manual + política definida no início (evitar inserir secrets em prompts externos até política de segurança aprovada).

## Atividade passo a passo

1. Copie os 4 cenários para uma planilha curta.
2. Preencha para cada um:
   - classificação (exploração/síntese/edição/decisão)
   - ferramenta principal
   - motivo (máximo 2 frases)
   - principal risco
   - controle de revisão
3. Gere uma versão alternativa para **um** cenário mudando a ferramenta e explique por que a decisão mudou.
4. Identifique um erro comum do grupo (ex.: “usar ferramenta errada por hábito”) e documente prevenção.

## Entregável do laboratório

- 1 tabela completa com os 4 cenários.
- 1 nota de decisão curta:
  - “Quando escolho Codex.”
  - “Quando fico no ChatGPT.”
  - “Quando não uso LLM.”
- 1 linha de melhoria para o próximo módulo.

## Critério de conclusão

O laboratório está concluído quando os quatro cenários tiverem: tipo de tarefa,
ferramenta, justificativa, risco e revisão humana. O painel não aprova respostas
automaticamente: faça a revisão qualitativa em
`03-rubrica-avaliacao-modulo-1.md` antes de marcar o módulo como concluído.
