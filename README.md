# ChatGPT e Codex — do Básico ao Avançado

Curso completo para iniciantes, do básico ao avançado.

Repositório canônico de um curso prático para operar, supervisionar e construir
com ChatGPT, Codex e a plataforma de APIs da OpenAI.

> Status: fundação do projeto. O currículo será transformado em módulos,
> laboratórios, materiais e critérios de avaliação versionados.

## Objetivo

Levar o participante de uma operação segura e criteriosa das ferramentas até a
concepção de fluxos profissionais, projetos de software e aplicações com agentes.

O curso prioriza entendimento antes de automação, práticas reproduzíveis e
auditáveis, segurança, privacidade, supervisão humana e fontes rastreáveis.

## Percursos

1. **Fundamentos** — ecossistema OpenAI, interação, qualidade e segurança.
2. **Workflows e Codex** — organização, pesquisa, artefatos, Git e engenharia.
3. **Especializações avançadas** — ChatGPT, Codex, API Platform, agentes e apps.
4. **Projeto final integrado** — avaliação de qualidade, rastreabilidade,
   segurança, reprodutibilidade, manutenção e viabilidade.

## Organização

- [Visão do produto](docs/visao-do-produto.md)
- [Currículo e mapa de aprendizagem](docs/curriculo.md)
- [Mapa visual](docs/mapa-do-curso.mmd)
- [Plano de entrega](docs/plano-de-entrega.md)
- [Fontes canônicas](docs/fontes.md)

## Módulo em produção

O **Módulo 1 — Ecossistema e limites de LLM** já possui guia, laboratório,
rubrica, template de entrega e uma versão interativa no painel Streamlit:

- [Guia do Módulo 1](docs/modulos/01-ecossistema-e-limites/01-guia-do-modulo-1.md)
- [Laboratório 1](docs/modulos/01-ecossistema-e-limites/02-laboratorio-ecossistema-e-limites.md)
- [Rubrica de avaliação](docs/modulos/01-ecossistema-e-limites/03-rubrica-avaliacao-modulo-1.md)
- [Template da entrega](docs/entregas/01-ecossistema-e-limites/template-entrega-modulo-1.md)

## Princípios editoriais

- Recursos, planos, disponibilidade e interfaces podem variar por conta,
  região, sistema operacional e permissões.
- Afirmações sobre produtos da OpenAI precisam apontar para documentação
  oficial e data de verificação.
- Cada laboratório deve declarar objetivo, pré-requisitos, procedimento,
  evidências esperadas, limites e critérios de conclusão.
- O repositório é a fonte de verdade: mudanças relevantes seguem branch,
  revisão e histórico no GitHub.

## Próximo marco

Publicar em ordem modular:

1. Diagnóstico inicial e missão.
2. Módulo 1 — Ecossistema e limites de LLM.
3. Módulo 2 — Comunicação eficiente com ChatGPT.
4. Módulo 3 — Qualidade, evidência e validação.
5. Módulo 4 — Segurança, privacidade e governança.
6. Módulo 5 — Git, rastreabilidade e trabalho orientado a evidência.
7. Módulo 6 — Codex para engenharia de tarefas.
8. Módulo 7 — Integração de ferramentas e automações.
9. Módulo 8 — Projeto final integrado.

## Como o curso estara sendo forjado

Este projeto sera construído como um produto GitHub-first:

- Conteudo editorial em Markdown (`docs/`) e dados em arquivos versionados (`data/`).
- Aplicacao interativa em Python 3.14 com Streamlit (`app/main.py`).
- Ambiente padrao no GitHub Codespaces via `.devcontainer/devcontainer.json`.
- Gerenciamento de ambientes Python com `uv` (e `requirements*.txt`).
- Automacao de qualidade em GitHub Actions (`.github/workflows/course-ci.yml`).
- Node + npm mantidos no Codespace para ferramentas auxiliares quando preciso (`node` 24 e `npm` 12).

Comando rapido local no Codespace:

```bash
python -m streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0
```

Requisito de base: o projeto e interativo, versionado e com validacao automatica.
