# ChatGPT e Codex — do Básico ao Avançado

Curso completo para iniciantes, do básico ao avançado.

Repositório canônico de um curso prático para operar, supervisionar e construir
com ChatGPT, Codex e a plataforma de APIs da OpenAI.

> Status: arquitetura canônica versionada. O curso será publicado por unidade,
> laboratório e trilha, preservando integralmente o mapa aprovado.

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
- [Direção visual](docs/identidade-visual.md)
- [Como começar](docs/inicio-do-curso.md)
- [Currículo e mapa de aprendizagem](docs/curriculo.md)
- [Mapa visual](docs/mapa-do-curso.mmd)
- [Plano de entrega](docs/plano-de-entrega.md)
- [Fontes canônicas](docs/fontes.md)

## Regra de arquitetura

O [mapa canônico](docs/mapa-do-curso.mmd) define toda a engenharia pedagógica.
Não compactamos, fundimos, removemos ou reorganizamos unidades e trilhas sem
autorização expressa do responsável pelo curso.

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

1. Diagnóstico inicial e preparação do ambiente.
2. Nível 1 completo: B1 a B4 e laboratório básico.
3. Nível 2 completo: I1 a I9 e laboratório intermediário.
4. Trilhas avançadas independentes: 3A, 3B e 3C.
5. Integração, projeto final e banca de validação.

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
uv run --with-requirements requirements.txt streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0
```

Requisito de base: o projeto e interativo, versionado e com validacao automatica.
