import json
from html import escape
from pathlib import Path
from typing import Any

import streamlit as st

BASE_DIR = Path(__file__).resolve().parents[1]
OUTLINE_PATH = BASE_DIR / "data" / "course_outline.json"
MODULE1_LAB_PATH = BASE_DIR / "data" / "labs" / "modulo1.json"
DIAGNOSTIC_PATH = BASE_DIR / "data" / "diagnostico-inicial.json"
PREPARATION_PATH = BASE_DIR / "data" / "preparacao-do-ambiente.json"
B2_LAB_PATH = BASE_DIR / "data" / "fundamentos-interacao-b2.json"
B3_LAB_PATH = BASE_DIR / "data" / "chatgpt-essencial-b3.json"
B4_LAB_PATH = BASE_DIR / "data" / "qualidade-seguranca-b4.json"
BASIC_CHECKPOINT_PATH = BASE_DIR / "data" / "laboratorio-basico-checkpoint.json"
I1_LAB_PATH = BASE_DIR / "data" / "organizacao-persistente-i1.json"
I2_LAB_PATH = BASE_DIR / "data" / "arquitetura-workflows-i2.json"
I3_LAB_PATH = BASE_DIR / "data" / "pesquisa-fontes-i3.json"
I4_LAB_PATH = BASE_DIR / "data" / "producao-artefatos-i4.json"
I5_LAB_PATH = BASE_DIR / "data" / "personalizacao-funcional-i5.json"


@st.cache_data
def load_course() -> dict[str, Any]:
    return json.loads(OUTLINE_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_b1_lab() -> dict[str, Any]:
    return json.loads(MODULE1_LAB_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_diagnostic() -> dict[str, Any]:
    return json.loads(DIAGNOSTIC_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_preparation() -> dict[str, Any]:
    return json.loads(PREPARATION_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_b2_lab() -> dict[str, Any]:
    return json.loads(B2_LAB_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_b3_lab() -> dict[str, Any]:
    return json.loads(B3_LAB_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_b4_lab() -> dict[str, Any]:
    return json.loads(B4_LAB_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_basic_checkpoint() -> dict[str, Any]:
    return json.loads(BASIC_CHECKPOINT_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_i1_lab() -> dict[str, Any]:
    return json.loads(I1_LAB_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_i2_lab() -> dict[str, Any]:
    return json.loads(I2_LAB_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_i3_lab() -> dict[str, Any]:
    return json.loads(I3_LAB_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_i4_lab() -> dict[str, Any]:
    return json.loads(I4_LAB_PATH.read_text(encoding="utf-8"))


@st.cache_data
def load_i5_lab() -> dict[str, Any]:
    return json.loads(I5_LAB_PATH.read_text(encoding="utf-8"))


def progress_state(modules: list[dict[str, Any]]) -> dict[str, str]:
    progress = st.session_state.setdefault("module_progress", {})
    for module in modules:
        progress.setdefault(module["id"], "pending")
    return progress


def log_event(message: str) -> None:
    events = st.session_state.setdefault("course_events", [])
    events.append(message)
    st.session_state["course_events"] = events[-24:]


def set_focus(module_id: str) -> None:
    st.session_state["focused_module"] = module_id


def status_label(status: str) -> str:
    return {"done": "concluída", "active": "em curso"}.get(status, "planejada")


def status_tone(status: str) -> str:
    return {"done": "is-done", "active": "is-active"}.get(status, "is-pending")


def build_pet_svg(pet: str, color: str, glow: str, index: int) -> str:
    return f"""
    <svg class="pet-svg" viewBox="0 0 120 120" aria-label="Mini pet {escape(pet)}" role="img">
      <defs>
        <radialGradient id="halo-{index}" cx="50%" cy="48%" r="58%">
          <stop offset="0%" stop-color="{escape(glow)}" stop-opacity=".52" />
          <stop offset="100%" stop-color="{escape(glow)}" stop-opacity="0" />
        </radialGradient>
      </defs>
      <circle cx="60" cy="60" r="58" fill="url(#halo-{index})" />
      <rect x="22" y="27" width="76" height="68" rx="22" fill="#09152d" stroke="#67d8ff" stroke-width="2" />
      <rect x="29" y="35" width="62" height="48" rx="14" fill="#0d2344" />
      <rect x="46" y="17" width="28" height="13" rx="6.5" fill="#136da0" />
      <circle cx="47" cy="57" r="7" fill="{escape(color)}" />
      <circle cx="73" cy="57" r="7" fill="{escape(color)}" />
      <circle cx="47" cy="57" r="2.5" fill="#031022" />
      <circle cx="73" cy="57" r="2.5" fill="#031022" />
      <path d="M48 70 Q60 79 72 70" fill="none" stroke="#dff7ff" stroke-width="3" stroke-linecap="round" />
      <path d="M22 79 h-12 M98 79 h12" stroke="#67d8ff" stroke-width="3" stroke-linecap="round" />
      <text x="60" y="110" text-anchor="middle" fill="#bceeff" font-size="11" font-family="ui-monospace, monospace">{escape(pet)}</text>
    </svg>
    """


def build_terminal_preview(module_count: int) -> str:
    return f"""
    <div class="terminal-shell">
      <div class="terminal-bar"><span class="dot red"></span><span class="dot amber"></span><span class="dot green"></span><code>course@codex:~/trilha</code></div>
      <div class="terminal-body">
        <p><span class="prompt">~ $</span> iniciar percurso --objetivo="autonomia"</p>
        <p class="terminal-title">◈ COURSE SYSTEM</p>
        <p>01. mapear ponto de partida</p>
        <p>02. preparar ambiente seguro</p>
        <p>03. explorar o ecossistema</p>
        <p>04. construir com evidência</p>
        <p class="terminal-ok">✓ mapa canônico carregado</p>
        <p class="terminal-ok">✓ {module_count} unidades disponíveis</p>
        <p><span class="prompt">~ $</span><span class="cursor">_</span></p>
      </div>
    </div>
    """


def build_syllabus_cards(modules: list[dict[str, Any]], progress: dict[str, str]) -> str:
    cards = []
    for position, module in enumerate(modules, start=1):
        status = progress[module["id"]]
        cards.append(
            f"""
            <article class="syllabus-card {status_tone(status)}">
              <div class="syllabus-number">{position:02d}</div>
              <div>
                <span class="syllabus-stage">{escape(module["stage"])}</span>
                <h4>{escape(module["title"])}</h4>
                <p>{escape(module["deliverable"])}</p>
              </div>
            </article>
            """
        )
    return "<div class='syllabus-grid'>" + "".join(cards) + "</div>"


def build_b1_delivery(answers: list[dict[str, str]]) -> str:
    rows = "\n".join(
        "| {title} | {task_type} | {tool} | {alternatives} | {reason} | {risk} | {review} |".format(
            **answer
        )
        for answer in answers
    )
    return f"""# Entrega — B1: Ecossistema OpenAI

> Gerado no laboratório interativo. Revise com a rubrica antes de enviar.

## Decisão de superfície por cenário

| Cenário | Tipo de tarefa | Superfície escolhida | Alternativas descartadas | Justificativa | Risco principal | Revisão humana |
| --- | --- | --- | --- | --- | --- | --- |
{rows}

## Conclusão de risco

- Decido com LLM para:
- Não decido com LLM quando:
- Sempre reviso:
"""


def build_diagnostic_delivery(answers: dict[str, Any]) -> str:
    environments = ", ".join(answers["environments"])
    care_points = ", ".join(answers["care_points"])
    return f"""# Diagnóstico inicial

> Registro gerado no curso. Revise antes de guardar ou compartilhar.

## Objetivo

{answers["goal"]}

## Rota de entrada predominante

{answers["entry_path"]}

## Repertório atual

{answers["experience"]}

## Ambiente disponível

{environments}

## Projeto de referência

{answers["project"]}

## Cuidados desde o início

Pontos de atenção: {care_points}

Controle inicial: {answers["control"]}

## Critério pessoal de sucesso

{answers["success"]}

## Próxima unidade

Use este registro na Preparação do ambiente. Não inclua senhas, chaves de API,
dados pessoais de terceiros ou conteúdo sigiloso ao compartilhá-lo.
"""


def render_diagnostic() -> None:
    diagnostic = load_diagnostic()
    st.markdown("<div class='section-kicker'>UNIDADE ATIVA // ENTRADA</div>", unsafe_allow_html=True)
    st.subheader(str(diagnostic["title"]))
    st.caption(str(diagnostic["purpose"]))
    st.info(str(diagnostic["privacy_note"]))

    goal = st.text_area(
        "1. Qual resultado você quer alcançar com este curso?",
        key="diagnostic-goal",
        placeholder="Ex.: construir um fluxo confiável para revisar documentos antes de publicá-los.",
    ).strip()
    entry_path = st.selectbox(
        "2. Qual rota descreve sua prioridade atual?",
        options=["Selecione..."] + list(diagnostic["entry_paths"]),
        key="diagnostic-entry-path",
    )
    experience = st.selectbox(
        "3. Como você descreve seu repertório atual?",
        options=["Selecione..."] + list(diagnostic["experience_levels"]),
        key="diagnostic-experience",
    )
    environments = st.multiselect(
        "4. Em quais ambientes você realmente consegue trabalhar hoje?",
        options=list(diagnostic["environment_options"]),
        key="diagnostic-environments",
        placeholder="Selecione um ou mais ambientes.",
    )
    project = st.text_area(
        "5. Que projeto, problema ou rotina você quer melhorar?",
        key="diagnostic-project",
        placeholder="Descreva sem incluir conteúdo confidencial ou dados de terceiros.",
    ).strip()
    care_points = st.multiselect(
        "6. O que exige cuidado desde o início?",
        options=list(diagnostic["care_options"]),
        key="diagnostic-care-points",
        placeholder="Selecione os pontos relevantes.",
    )
    control = st.text_area(
        "Qual controle inicial você aplicará?",
        key="diagnostic-control",
        placeholder="Ex.: remover identificadores e revisar a saída antes de qualquer envio.",
    ).strip()
    success = st.text_area(
        "7. Como você saberá que o curso foi útil para você?",
        key="diagnostic-success",
        placeholder="Defina uma evidência observável de progresso.",
    ).strip()
    safe_data_confirmed = st.checkbox(
        "Confirmo que não registrei senhas, chaves de API, dados pessoais de terceiros ou conteúdo sigiloso.",
        key="diagnostic-safe-data",
    )

    answers: dict[str, Any] = {
        "goal": goal,
        "entry_path": "" if entry_path == "Selecione..." else entry_path,
        "experience": "" if experience == "Selecione..." else experience,
        "environments": environments,
        "project": project,
        "care_points": care_points,
        "control": control,
        "success": success,
    }
    completed = sum(
        (
            bool(answers["goal"]),
            bool(answers["entry_path"]),
            bool(answers["experience"]),
            bool(answers["environments"]),
            bool(answers["project"]),
            bool(answers["care_points"] and answers["control"]),
            bool(answers["success"]),
        )
    )
    st.progress(completed / len(diagnostic["completion_fields"]))
    st.caption(f"{completed}/{len(diagnostic['completion_fields'])} critérios de conclusão preenchidos")

    if completed == len(diagnostic["completion_fields"]):
        if safe_data_confirmed:
            st.success("Diagnóstico concluído. Use a entrega na Preparação do ambiente.")
            st.download_button(
                "Baixar diagnóstico em Markdown",
                data=build_diagnostic_delivery(answers),
                file_name="diagnostico-inicial.md",
                mime="text/markdown",
            )
        else:
            st.warning("Antes de gerar a entrega, confirme a proteção dos dados registrados.")


def build_preparation_delivery(answers: dict[str, Any]) -> str:
    workspaces = ", ".join(answers["workspaces"])
    controls = ", ".join(answers["controls"])
    return f"""# Preparação do ambiente

> Registro gerado no curso. Revise antes de guardar ou compartilhar.

## Acesso e disponibilidade

Conta ou workspace: {answers["account"]}

Onde conferi plano, permissões e disponibilidade: {answers["availability"]}

## Ambiente escolhido

{workspaces}

## Repositório e espaço de trabalho

{answers["repository"]}

## Política pessoal de dados

Pode compartilhar: {answers["allowed_data"]}

Não pode compartilhar: {answers["restricted_data"]}

## Controles e revisão

Controles selecionados: {controls}

Revisão antes de ação com impacto: {answers["review"]}

## Evidência de conclusão

{answers["evidence"]}

## Próxima unidade

Iniciar B1 · Ecossistema OpenAI. Confirme novamente qualquer recurso que dependa
de conta, plano, plataforma, região, rollout ou configurações do workspace.
"""


def render_preparation() -> None:
    preparation = load_preparation()
    st.markdown("<div class='section-kicker'>UNIDADE ATIVA // ENTRADA</div>", unsafe_allow_html=True)
    st.subheader(str(preparation["title"]))
    st.caption(str(preparation["purpose"]))
    st.warning(str(preparation["availability_note"]))
    st.caption(
        f"Fonte oficial verificada em {preparation['verified_on']}: "
        f"{preparation['official_source']}"
    )

    account = st.selectbox(
        "1. Qual é seu ponto de acesso atual?",
        options=["Selecione..."] + list(preparation["account_options"]),
        key="preparation-account",
    )
    availability = st.text_area(
        "2. Onde você conferiu plano, permissões e disponibilidade?",
        key="preparation-availability",
        placeholder="Ex.: página da conta, configuração do workspace ou orientação do administrador.",
    ).strip()
    workspaces = st.multiselect(
        "3. Quais ambientes você usará nesta etapa?",
        options=list(preparation["workspace_options"]),
        key="preparation-workspaces",
        placeholder="Selecione apenas os ambientes disponíveis para você.",
    )
    repository = st.text_area(
        "4. Qual repositório, pasta de exercícios ou fluxo de revisão você usará?",
        key="preparation-repository",
        placeholder="Ex.: repositório GitHub do curso e pull requests para mudanças técnicas.",
    ).strip()
    allowed_data = st.text_area(
        "5. Que tipo de informação pode entrar no seu ambiente de estudo?",
        key="preparation-allowed-data",
        placeholder="Ex.: exemplos fictícios, material público ou dados anonimizados.",
    ).strip()
    restricted_data = st.text_area(
        "O que não pode ser compartilhado?",
        key="preparation-restricted-data",
        placeholder="Nunca inclua senhas, chaves de API, tokens, conteúdo sigiloso ou dados pessoais de terceiros.",
    ).strip()
    controls = st.multiselect(
        "6. Quais controles você adotará desde agora?",
        options=list(preparation["control_options"]),
        key="preparation-controls",
        placeholder="Selecione um ou mais controles.",
    )
    review = st.text_area(
        "Como você revisará uma ação antes de publicar ou executar?",
        key="preparation-review",
        placeholder="Descreva a pessoa, critério ou etapa de revisão.",
    ).strip()
    evidence = st.text_input(
        "7. Onde ficará o registro desta preparação?",
        key="preparation-evidence",
        placeholder="Ex.: arquivo Markdown, issue, projeto ou pasta de estudo.",
    ).strip()
    safe_data_confirmed = st.checkbox(
        "Confirmo que não registrei senhas, chaves de API, tokens ou dados pessoais de terceiros.",
        key="preparation-safe-data",
    )

    answers: dict[str, Any] = {
        "account": "" if account == "Selecione..." else account,
        "availability": availability,
        "workspaces": workspaces,
        "repository": repository,
        "allowed_data": allowed_data,
        "restricted_data": restricted_data,
        "controls": controls,
        "review": review,
        "evidence": evidence,
    }
    completed = sum(
        (
            bool(answers["account"]),
            bool(answers["availability"]),
            bool(answers["workspaces"]),
            bool(answers["repository"]),
            bool(answers["allowed_data"] and answers["restricted_data"]),
            bool(answers["controls"] and answers["review"]),
            bool(answers["evidence"]),
        )
    )
    st.progress(completed / len(preparation["completion_fields"]))
    st.caption(f"{completed}/{len(preparation['completion_fields'])} critérios de conclusão preenchidos")

    if completed == len(preparation["completion_fields"]):
        if safe_data_confirmed:
            st.success("Preparação concluída. O próximo passo é B1 · Ecossistema OpenAI.")
            st.download_button(
                "Baixar preparação em Markdown",
                data=build_preparation_delivery(answers),
                file_name="preparacao-do-ambiente.md",
                mime="text/markdown",
            )
        else:
            st.warning("Antes de gerar a entrega, confirme a proteção dos dados registrados.")


def render_b1_lab() -> None:
    lab = load_b1_lab()
    st.markdown("<div class='section-kicker'>LABORATÓRIO ATIVO // B1</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))

    answers: list[dict[str, str]] = []
    scenarios = lab["scenarios"]
    task_types = lab["task_types"]
    tool_options = lab["tool_options"]

    st.markdown("**Radar de superfícies**")
    surface_columns = st.columns(len(lab["surface_cards"]), gap="small")
    for column, surface in zip(surface_columns, lab["surface_cards"]):
        with column:
            st.markdown(
                f"<div class='surface-card'><strong>{escape(surface['name'])}</strong>"
                f"<p>{escape(surface['use_when'])}</p>"
                f"<small>Limite: {escape(surface['boundary'])}</small></div>",
                unsafe_allow_html=True,
            )
    st.caption("Fatos de produto foram verificados em 05-08-2026; disponibilidade e controles podem variar.")

    for position, scenario in enumerate(scenarios, start=1):
        scenario_id = scenario["id"]
        with st.expander(f"{position:02d} · {scenario['title']}", expanded=position == 1):
            st.markdown(f"**Contexto** — {scenario['context']}")
            st.caption(f"Radar de risco: {scenario['risk_hint']}")
            task_type = st.selectbox(
                "Tipo de tarefa",
                options=["Selecione..."] + task_types,
                key=f"b1-type-{scenario_id}",
            )
            tool = st.selectbox(
                "Superfície escolhida",
                options=["Selecione..."] + tool_options,
                key=f"b1-tool-{scenario_id}",
            )
            alternatives = st.multiselect(
                "Alternativas descartadas",
                options=tool_options,
                key=f"b1-alternatives-{scenario_id}",
                placeholder="Registre ao menos uma alternativa que não atende tão bem ao cenário.",
            )
            reason = st.text_area(
                "Justificativa",
                key=f"b1-reason-{scenario_id}",
                placeholder="Explique a escolha pelo objetivo e pelo contexto.",
            ).strip()
            risk = st.text_input(
                "Risco principal",
                key=f"b1-risk-{scenario_id}",
                placeholder="Qual erro ou impacto precisa ser evitado?",
            ).strip()
            review = st.text_input(
                "Revisão humana",
                key=f"b1-review-{scenario_id}",
                placeholder="Descreva a checagem antes da conclusão.",
            ).strip()
            answers.append(
                {
                    "title": str(scenario["title"]),
                    "task_type": task_type if task_type != "Selecione..." else "",
                    "tool": tool if tool != "Selecione..." else "",
                    "alternatives": ", ".join(alternatives),
                    "reason": reason,
                    "risk": risk,
                    "review": review,
                }
            )

    completed = sum(
        all(
            answer[key]
            for key in ("task_type", "tool", "alternatives", "reason", "risk", "review")
        )
        for answer in answers
    )
    st.progress(completed / len(answers))
    st.caption(f"{completed}/{len(answers)} cenários concluídos")

    if completed == len(answers):
        st.success("Checkpoint preenchido. Revise a rubrica antes de concluir B1.")
        st.download_button(
            "Baixar entrega em Markdown",
            data=build_b1_delivery(answers),
            file_name="entrega-b1-ecossistema-openai.md",
            mime="text/markdown",
        )


def build_b2_delivery(answers: list[dict[str, str]]) -> str:
    sections = []
    for answer in answers:
        sections.append(
            f"""## {answer['title']}

**Pedido vago:** {answer['vague_request']}

- Objetivo observável: {answer['objective']}
- Contexto e insumos: {answer['context']}
- Instruções: {answer['instructions']}
- Restrições e critérios: {answer['constraints']}
- Formato de saída: {answer['format']}
- Exemplo ou justificativa de ausência: {answer['example']}
- Histórico, anexo ou lacuna de contexto: {answer['gap']}
- Crítica da primeira saída: {answer['critique']}
- Próximo refinamento: {answer['refinement']}"""
        )
    return "# Entrega — B2: Fundamentos de interação\n\n" + "\n\n".join(sections)


def render_b2_lab() -> None:
    lab = load_b2_lab()
    st.markdown("<div class='section-kicker'>OFICINA ATIVA // B2</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.info(
        "Método: tornar explícitos objetivo, contexto e critérios. "
        "O formulário não confirma fatos nem substitui revisão humana."
    )
    st.markdown("**Componentes que cada briefing deve tornar visíveis**")
    st.markdown(
        "<div class='component-line'>"
        + "".join(f"<span>{escape(component)}</span>" for component in lab["components"])
        + "</div>",
        unsafe_allow_html=True,
    )

    answers: list[dict[str, str]] = []
    for position, scenario in enumerate(lab["scenarios"], start=1):
        scenario_id = scenario["id"]
        with st.expander(f"{position:02d} · {scenario['title']}", expanded=position == 1):
            st.markdown(f"**Pedido vago** — {scenario['vague_request']}")
            st.caption(f"Pista de contexto: {scenario['context_hint']}")
            objective = st.text_area(
                "1. Objetivo observável",
                key=f"b2-objective-{scenario_id}",
                placeholder="Que resultado deve existir ao final e para quem?",
            ).strip()
            context = st.text_area(
                "2. Contexto e insumos",
                key=f"b2-context-{scenario_id}",
                placeholder="Quais fatos, materiais ou condições podem ser usados?",
            ).strip()
            instructions = st.text_area(
                "3. Instruções de execução",
                key=f"b2-instructions-{scenario_id}",
                placeholder="Descreva a transformação esperada com verbos claros.",
            ).strip()
            constraints = st.text_area(
                "4. Restrições e critérios",
                key=f"b2-constraints-{scenario_id}",
                placeholder="O que evitar e como reconhecer uma resposta aceitável?",
            ).strip()
            output_format = st.text_input(
                "5. Formato de saída",
                key=f"b2-format-{scenario_id}",
                placeholder="Ex.: tabela com três colunas, até 200 palavras, em português.",
            ).strip()
            example = st.text_area(
                "6. Exemplo ou justificativa de ausência",
                key=f"b2-example-{scenario_id}",
                placeholder="Inclua um exemplo coerente ou diga por que ele não é necessário.",
            ).strip()
            gap = st.text_area(
                "7. Histórico, anexo ou lacuna de contexto",
                key=f"b2-gap-{scenario_id}",
                placeholder="O que ainda não foi fornecido e não pode ser presumido?",
            ).strip()
            critique = st.text_area(
                "8. Crítica da primeira saída",
                key=f"b2-critique-{scenario_id}",
                placeholder="Que evidência, critério ou trecho você verificará na primeira resposta?",
            ).strip()
            refinement = st.text_area(
                "Próximo refinamento",
                key=f"b2-refinement-{scenario_id}",
                placeholder="Escreva o próximo pedido que corrigirá a falha encontrada.",
            ).strip()
            answers.append(
                {
                    "title": str(scenario["title"]),
                    "vague_request": str(scenario["vague_request"]),
                    "objective": objective,
                    "context": context,
                    "instructions": instructions,
                    "constraints": constraints,
                    "format": output_format,
                    "example": example,
                    "gap": gap,
                    "critique": critique,
                    "refinement": refinement,
                }
            )

    required_keys = ("objective", "context", "instructions", "constraints", "format", "example", "gap", "critique", "refinement")
    completed = sum(all(answer[key] for key in required_keys) for answer in answers)
    st.progress(completed / len(answers))
    st.caption(f"{completed}/{len(answers)} briefings completos")
    if completed == len(answers):
        st.success("Briefings completos. Execute um, critique a primeira saída e salve a versão refinada.")
        st.download_button(
            "Baixar entrega B2 em Markdown",
            data=build_b2_delivery(answers),
            file_name="entrega-b2-fundamentos-interacao.md",
            mime="text/markdown",
        )


def build_b3_delivery(answers: list[dict[str, str]]) -> str:
    sections = []
    for answer in answers:
        sections.append(
            f"""## {answer['title']}

- Intenção e material usado: {answer['intencao']}
- Evidência rastreável: {answer['evidencia']}
- Disponibilidade ou alternativa: {answer['disponibilidade']}
- Revisão humana: {answer['revisao']}"""
        )
    return "# Entrega — B3: ChatGPT essencial\n\n" + "\n\n".join(sections)


def render_b3_lab() -> None:
    lab = load_b3_lab()
    st.markdown("<div class='section-kicker'>LABORATÓRIO ATIVO // B3</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.warning(str(lab["availability_note"]))

    st.markdown("**Mapa de recursos e evidências**")
    card_columns = st.columns(2, gap="small")
    for column, capability in zip(card_columns * 2, lab["capability_cards"]):
        with column:
            st.markdown(
                f"<div class='surface-card'><strong>{escape(capability['name'])}</strong>"
                f"<p>{escape(capability['use_when'])}</p>"
                f"<small>Evidência: {escape(capability['evidence'])}<br>Limite: {escape(capability['boundary'])}</small></div>",
                unsafe_allow_html=True,
            )

    answers: list[dict[str, str]] = []
    for position, workflow in enumerate(lab["workflows"], start=1):
        workflow_id = workflow["id"]
        with st.expander(f"{position:02d} · {workflow['title']}", expanded=position == 1):
            st.markdown(f"**Roteiro** — {workflow['prompt']}")
            st.caption(f"Ponto de atenção: {workflow['risk_hint']}")
            intention = st.text_area(
                str(workflow["input_label"]),
                key=f"b3-intention-{workflow_id}",
                placeholder=str(workflow["input_placeholder"]),
            ).strip()
            evidence = st.text_area(
                str(workflow["evidence_label"]),
                key=f"b3-evidence-{workflow_id}",
                placeholder="Registre referências específicas, sem inserir material sensível.",
            ).strip()
            availability = st.text_input(
                "Disponibilidade, permissão ou alternativa usada",
                key=f"b3-availability-{workflow_id}",
                placeholder="Ex.: disponível no navegador; microfone autorizado; ou alternativa manual adotada.",
            ).strip()
            review = st.text_area(
                "Revisão humana antes de usar ou compartilhar",
                key=f"b3-review-{workflow_id}",
                placeholder="O que você conferiu no material, nas fontes ou na versão final?",
            ).strip()
            answers.append(
                {
                    "title": str(workflow["title"]),
                    "intencao": intention,
                    "evidencia": evidence,
                    "disponibilidade": availability,
                    "revisao": review,
                }
            )

    required_keys = ("intencao", "evidencia", "disponibilidade", "revisao")
    completed = sum(all(answer[key] for key in required_keys) for answer in answers)
    st.progress(completed / len(answers))
    st.caption(f"{completed}/{len(answers)} registros multimodais completos")
    safe_data_confirmed = st.checkbox(
        "Confirmo que usei apenas fontes e materiais autorizados e que revisei a entrega antes de compartilhá-la.",
        key="b3-safe-data",
    )
    if completed == len(answers):
        if safe_data_confirmed:
            st.success("Entrega multimodal registrada. Revise a rubrica antes de concluir B3.")
            st.download_button(
                "Baixar entrega B3 em Markdown",
                data=build_b3_delivery(answers),
                file_name="entrega-b3-chatgpt-essencial.md",
                mime="text/markdown",
            )
        else:
            st.warning("Antes de gerar a entrega, confirme que os materiais e a revisão estão autorizados.")


def build_b4_delivery(assessments: list[dict[str, str]]) -> str:
    sections = []
    for assessment in assessments:
        sections.append(
            f"""## {assessment['title']}

- Afirmação, proposta ou saída: {assessment['afirmacao']}
- Classificação: {assessment['classificacao']}
- Evidência ou lacuna: {assessment['evidencia']}
- Dados, privacidade e impacto: {assessment['dados']}
- Decisão e revisão humana: {assessment['decisao']}"""
        )
    return "# Entrega — B4: Qualidade e segurança\n\n" + "\n\n".join(sections)


def render_b4_lab() -> None:
    lab = load_b4_lab()
    st.markdown("<div class='section-kicker'>LABORATÓRIO ATIVO // B4</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.warning(str(lab["safety_note"]))
    st.caption(f"Fonte oficial verificada em {lab['verified_on']}: {lab['official_sources'][0]}")

    st.markdown("**Checklist antes de usar, publicar ou executar**")
    card_columns = st.columns(2, gap="small")
    for column, control in zip(card_columns * 2, lab["quality_cards"]):
        with column:
            st.markdown(
                f"<div class='surface-card'><strong>{escape(control['name'])}</strong>"
                f"<p>{escape(control['question'])}</p>"
                f"<small>Ação: {escape(control['action'])}<br>Limite: {escape(control['boundary'])}</small></div>",
                unsafe_allow_html=True,
            )

    assessments: list[dict[str, str]] = []
    for position, case in enumerate(lab["cases"], start=1):
        case_id = case["id"]
        with st.expander(f"{position:02d} · {case['title']}", expanded=position == 1):
            st.markdown(f"**Cenário** — {case['scenario']}")
            st.caption(f"Risco principal: {case['risk_hint']}")
            claim = st.text_area(
                str(case["claim_label"]),
                key=f"b4-claim-{case_id}",
                placeholder=str(case["claim_placeholder"]),
            ).strip()
            classification = st.selectbox(
                "Classificação da afirmação ou proposta",
                options=["Selecione..."] + list(lab["classification_options"]),
                key=f"b4-classification-{case_id}",
            )
            evidence = st.text_area(
                "Evidência, fonte primária ou lacuna de confirmação",
                key=f"b4-evidence-{case_id}",
                placeholder="Registre o que sustenta a conclusão ou o que ainda precisa ser conferido.",
            ).strip()
            data = st.text_area(
                "Dados, privacidade e impacto de usar esta saída",
                key=f"b4-data-{case_id}",
                placeholder="Indique dados sensíveis, autorização, minimização ou por que não há dados envolvidos.",
            ).strip()
            decision = st.text_input(
                "Decisão e revisão humana necessária",
                key=f"b4-decision-{case_id}",
                placeholder="Ex.: não publicar; conferir fonte primária; submeter à pessoa responsável.",
            ).strip()
            assessments.append(
                {
                    "title": str(case["title"]),
                    "afirmacao": claim,
                    "classificacao": "" if classification == "Selecione..." else classification,
                    "evidencia": evidence,
                    "dados": data,
                    "decisao": decision,
                }
            )

    required_keys = ("afirmacao", "classificacao", "evidencia", "dados", "decisao")
    completed = sum(all(assessment[key] for key in required_keys) for assessment in assessments)
    st.progress(completed / len(assessments))
    st.caption(f"{completed}/{len(assessments)} decisões de qualidade e segurança completas")
    safe_review_confirmed = st.checkbox(
        "Confirmo que não usei dados sensíveis sem autorização e que nenhuma decisão de alto impacto será tomada sem revisão humana adequada.",
        key="b4-safe-review",
    )
    if completed == len(assessments):
        if safe_review_confirmed:
            st.success("Relatório de qualidade e segurança concluído. Revise a rubrica antes de encerrar B4.")
            st.download_button(
                "Baixar relatório B4 em Markdown",
                data=build_b4_delivery(assessments),
                file_name="relatorio-b4-qualidade-seguranca.md",
                mime="text/markdown",
            )
        else:
            st.warning("Antes de gerar a entrega, confirme os limites de dados e a revisão humana.")


def build_basic_checkpoint_delivery(
    answers: dict[str, str], assessments: list[dict[str, str]], decision: str
) -> str:
    checkpoint_rows = "\n".join(
        f"| {item['title']} | {item['status']} | {item['evidence']} |"
        for item in assessments
    )
    return f"""# Entrega — Laboratório básico

## Pergunta e briefing

{answers['pergunta']}

## Arquivo analisado

- **Identificação e autorização:** {answers['arquivo']}
- **Extrato relevante:** {answers['extrato']}
- **Limites do material:** {answers['limites']}

## Pesquisa externa

- **Estratégia de pesquisa:** {answers['pesquisa']}
- **Fontes consultadas:** {answers['fontes']}

## Síntese verificável

{answers['sintese']}

## Classificação das conclusões

{answers['classificacao']}

## Revisão final

{answers['verificacao']}

## Entrega final

{answers['entrega']}

## Checkpoint

| Critério | Estado | Evidência |
| --- | --- | --- |
{checkpoint_rows}

**Decisão:** {decision}
"""


def render_basic_checkpoint() -> None:
    lab = load_basic_checkpoint()
    st.markdown("<div class='section-kicker'>MARCO DE NÍVEL // CHECKPOINT BÁSICO</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.warning(str(lab["availability_note"]))
    st.info(str(lab["privacy_note"]))

    labels = {
        "pergunta": "Pergunta e briefing completo",
        "arquivo": "Identificação do arquivo e autorização de uso",
        "extrato": "Trecho, dado ou estrutura extraída do arquivo",
        "limites": "Data, autoria, escopo e limites do arquivo",
        "pesquisa": "Estratégia e termos da pesquisa externa",
        "fontes": "Fontes consultadas, com título, responsável, data e endereço",
        "sintese": "Síntese que liga conclusões às evidências",
        "classificacao": "Fatos documentados, inferências e hipóteses ou lacunas",
        "verificacao": "Revisão de atualidade, consistência, privacidade e impacto",
        "entrega": "Entrega final pronta para conferência por outra pessoa",
    }
    answers: dict[str, str] = {}
    for key in lab["completion_fields"]:
        answers[key] = st.text_area(labels[key], key=f"basic-lab-{key}").strip()

    st.markdown("**Autoavaliação baseada na evidência produzida**")
    assessments: list[dict[str, str]] = []
    consolidated_label = str(lab["checkpoint_options"][0])
    for criterion in lab["checkpoint_criteria"]:
        criterion_id = criterion["id"]
        with st.expander(str(criterion["title"]), expanded=True):
            st.caption(str(criterion["question"]))
            status = st.selectbox(
                "Estado demonstrado",
                options=["Selecione..."] + list(lab["checkpoint_options"]),
                key=f"basic-checkpoint-status-{criterion_id}",
            )
            evidence = st.text_input(
                "Evidência específica na entrega",
                key=f"basic-checkpoint-evidence-{criterion_id}",
                placeholder="Aponte o campo, a fonte ou o trecho que demonstra o critério.",
            ).strip()
            assessments.append(
                {
                    "title": str(criterion["title"]),
                    "status": "" if status == "Selecione..." else status,
                    "evidence": evidence,
                }
            )

    fields_complete = all(answers.values())
    checkpoint_complete = all(item["status"] and item["evidence"] for item in assessments)
    completed_count = sum(bool(value) for value in answers.values())
    st.progress(completed_count / len(answers))
    st.caption(f"{completed_count}/{len(answers)} campos da entrega completos")

    if fields_complete and checkpoint_complete:
        consolidated = all(item["status"] == consolidated_label for item in assessments)
        if consolidated:
            decision = "Avançar a I1 — quatro competências básicas consolidadas."
            st.success(decision)
        else:
            decision = "Retornar a B2 — ao menos uma competência precisa ser reconstruída e reaplicada."
            st.warning(decision)
        st.download_button(
            "Baixar laboratório e checkpoint em Markdown",
            data=build_basic_checkpoint_delivery(answers, assessments, decision),
            file_name="entrega-laboratorio-basico-checkpoint.md",
            mime="text/markdown",
        )
    elif fields_complete:
        st.warning("Complete os quatro estados do checkpoint e a evidência de cada critério.")


def build_i1_delivery(answers: dict[str, str]) -> str:
    return f"""# Entrega — I1: Organização persistente

## Objetivo e fronteira

- **Objetivo e resultado:** {answers['objetivo']}
- **Fora do escopo:** {answers['fronteira']}

## Fontes e arquivos

{answers['fontes']}

## Instruções obrigatórias

{answers['instrucoes']}

## Memória auxiliar

{answers['memoria']}

## Estrutura do workspace

- **Chats, pastas, arquivos e resumos:** {answers['estrutura']}
- **Nomenclatura:** {answers['nomenclatura']}

## Versionamento

{answers['versionamento']}

## Checkpoint de recuperação

{answers['recuperacao']}

## Teste de retomada

{answers['evidencia']}
"""


def render_i1_lab() -> None:
    lab = load_i1_lab()
    st.markdown("<div class='section-kicker'>WORKSPACE ATIVO // I1</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.warning(str(lab["availability_note"]))
    st.info(str(lab["privacy_note"]))

    st.markdown("**Camadas do workspace recuperável**")
    card_columns = st.columns(2, gap="small")
    for index, card in enumerate(lab["workspace_cards"]):
        with card_columns[index % 2]:
            st.markdown(
                f"<div class='surface-card'><strong>{escape(card['name'])}</strong>"
                f"<p>{escape(card['purpose'])}</p>"
                f"<small>Limite: {escape(card['boundary'])}</small></div>",
                unsafe_allow_html=True,
            )

    labels = {
        "objetivo": "Objetivo e resultado esperado do workspace",
        "fronteira": "Fora do escopo e limites de uso",
        "fontes": "Inventário de fontes: origem, versão, autorização e finalidade",
        "instrucoes": "Instruções obrigatórias e critérios de qualidade",
        "memoria": "O que pode ser memória auxiliar e o que deve ficar documentado",
        "estrutura": "Estrutura de chats, pastas, arquivos e resumos",
        "nomenclatura": "Convenção de nomes e localização da fonte de verdade",
        "versionamento": "Regra para versões, substituições e decisões revogadas",
        "recuperacao": "Checkpoint: estado, decisões, pendências e próxima ação",
        "evidencia": "Evidência do teste de retomada e correções realizadas",
    }
    answers: dict[str, str] = {}
    for key in lab["completion_fields"]:
        answers[key] = st.text_area(labels[key], key=f"i1-{key}").strip()

    completed_count = sum(bool(value) for value in answers.values())
    st.progress(completed_count / len(answers))
    st.caption(f"{completed_count}/{len(answers)} componentes do workspace registrados")
    safe_context_confirmed = st.checkbox(
        "Confirmo que usei apenas materiais autorizados, mantive regras obrigatórias fora da dependência exclusiva de memória e executei o teste de retomada.",
        key="i1-safe-context",
    )
    if completed_count == len(answers):
        if safe_context_confirmed:
            st.success("Workspace recuperável concluído. Revise a rubrica antes de avançar a I2.")
            st.download_button(
                "Baixar entrega I1 em Markdown",
                data=build_i1_delivery(answers),
                file_name="entrega-i1-organizacao-persistente.md",
                mime="text/markdown",
            )
        else:
            st.warning("Confirme autorização dos materiais, orientação durável e teste de retomada.")


def build_i2_delivery(answers: dict[str, str]) -> str:
    return f"""# Entrega — I2: Arquitetura de workflows

## Resultado e definição de pronto

- **Resultado:** {answers['resultado']}
- **Restrições:** {answers['restricoes']}

## Entradas

{answers['entradas']}

## Etapas

{answers['etapas']}

## Ferramentas e permissões

{answers['ferramentas']}

## Saídas e formatos

{answers['saidas']}

## Gates de validação

{answers['validacoes']}

## Parada, correção e retomada

- **Pontos de parada:** {answers['parada']}
- **Caminho de correção:** {answers['correcao']}

## Responsáveis

{answers['responsaveis']}

## Registro

- **Decisões e exceções:** {answers['decisoes']}
- **Versão, artefatos e próxima ação:** {answers['versao']}
"""


def render_i2_lab() -> None:
    lab = load_i2_lab()
    st.markdown("<div class='section-kicker'>WORKFLOW ATIVO // I2</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.warning(str(lab["availability_note"]))
    st.info(str(lab["safety_note"]))

    st.markdown("**Cinco decisões de arquitetura**")
    card_columns = st.columns(2, gap="small")
    for index, card in enumerate(lab["workflow_cards"]):
        with card_columns[index % 2]:
            st.markdown(
                f"<div class='surface-card'><strong>{escape(card['name'])}</strong>"
                f"<p>{escape(card['question'])}</p>"
                f"<small>Falha típica: {escape(card['failure'])}</small></div>",
                unsafe_allow_html=True,
            )

    labels = {
        "resultado": "Resultado final e definição verificável de pronto",
        "restricoes": "Restrições, permissões e fronteiras",
        "entradas": "Entradas: origem, formato, autorização e qualidade mínima",
        "etapas": "Etapas numeradas com entrada, transformação e dependências",
        "ferramentas": "Ferramenta de cada etapa e justificativa",
        "saidas": "Saídas, formato, localização e consumidor seguinte",
        "validacoes": "Gates: evidência, resultado esperado, decisor e ação se falhar",
        "parada": "Pontos de parada e condições de bloqueio",
        "correcao": "Correção, repetição, escalonamento e retomada",
        "responsaveis": "Responsáveis por executar, revisar e aprovar",
        "decisoes": "Log de decisões, exceções e evidências",
        "versao": "Versão do fluxo, artefatos gerados e próxima ação",
    }
    answers: dict[str, str] = {}
    for key in lab["completion_fields"]:
        answers[key] = st.text_area(labels[key], key=f"i2-{key}").strip()

    completed_count = sum(bool(value) for value in answers.values())
    st.progress(completed_count / len(answers))
    st.caption(f"{completed_count}/{len(answers)} contratos do workflow registrados")
    simulation_confirmed = st.checkbox(
        "Confirmo que simulei um caso normal e uma falha, sem executar ação externa, e corrigi o fluxo quando uma etapa não pôde ser validada.",
        key="i2-simulation",
    )
    if completed_count == len(answers):
        if simulation_confirmed:
            st.success("Workflow documentado e simulado. Revise a rubrica antes de avançar a I3.")
            st.download_button(
                "Baixar entrega I2 em Markdown",
                data=build_i2_delivery(answers),
                file_name="entrega-i2-arquitetura-workflows.md",
                mime="text/markdown",
            )
        else:
            st.warning("Execute a simulação de caso normal e falha antes de concluir I2.")


def build_i3_delivery(answers: dict[str, str]) -> str:
    return f"""# Entrega — I3: Pesquisa e fontes

## Pergunta, escopo e modalidade

- **Pergunta:** {answers['pergunta']}
- **Escopo:** {answers['escopo']}
- **Modalidade:** {answers['modalidade']}

## Consultas e fontes

- **Consultas e critérios:** {answers['consultas']}
- **Fontes consultadas:** {answers['fontes']}

## Matriz de fontes

{answers['matriz']}

## Atualidade e conflitos

- **Controle de atualidade:** {answers['atualidade']}
- **Conflitos:** {answers['conflitos']}

## Síntese e citações

{answers['sintese']}

{answers['citacoes']}

## Lacunas e revisão

- **Lacunas e inferências:** {answers['lacunas']}
- **Revisão final:** {answers['revisao']}
"""


def render_i3_lab() -> None:
    lab = load_i3_lab()
    st.markdown("<div class='section-kicker'>PESQUISA ATIVA // I3</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.warning(str(lab["availability_note"]))
    st.info(str(lab["safety_note"]))
    columns = st.columns(2, gap="small")
    for index, card in enumerate(lab["research_cards"]):
        with columns[index % 2]:
            st.markdown(
                f"<div class='surface-card'><strong>{escape(card['name'])}</strong>"
                f"<p>{escape(card['use_when'])}</p>"
                f"<small>Limite: {escape(card['boundary'])}</small></div>",
                unsafe_allow_html=True,
            )
    labels = {
        "pergunta": "Pergunta pesquisável",
        "escopo": "Escopo, período e exclusões",
        "modalidade": "Modalidade escolhida e justificativa",
        "consultas": "Consultas e critérios de inclusão ou exclusão",
        "fontes": "Fontes: título, responsável, endereço, tipo e datas",
        "matriz": "Matriz: tese, versão, autoridade, limites e conflito",
        "atualidade": "Controle de publicação, fato, consulta e vigência",
        "conflitos": "Divergências e resolução ou pendência",
        "sintese": "Síntese com fatos, inferências e dissensos",
        "citacoes": "Mapa de afirmações e respectivas citações",
        "lacunas": "Lacunas, hipóteses e confirmações pendentes",
        "revisao": "Revisão de rastreabilidade, privacidade e segurança",
    }
    answers = {
        key: st.text_area(labels[key], key=f"i3-{key}").strip()
        for key in lab["completion_fields"]
    }
    completed_count = sum(bool(value) for value in answers.values())
    st.progress(completed_count / len(answers))
    st.caption(f"{completed_count}/{len(answers)} componentes da pesquisa registrados")
    review_confirmed = st.checkbox(
        "Confirmo que li as fontes usadas, tratei resultados web como não confiáveis e revisei atualidade, conflitos, dados e citações.",
        key="i3-review",
    )
    if completed_count == len(answers):
        if review_confirmed:
            st.success("Relatório citado concluído. Revise a rubrica antes de avançar a I4.")
            st.download_button(
                "Baixar entrega I3 em Markdown",
                data=build_i3_delivery(answers),
                file_name="entrega-i3-pesquisa-fontes.md",
                mime="text/markdown",
            )
        else:
            st.warning("Confirme a leitura e a revisão das fontes antes de concluir I3.")


def build_i4_delivery(answers: dict[str, str]) -> str:
    return f"""# Entrega â€” I4: Produção de artefatos

## Objetivo, público e formato

- Objetivo: {answers['objetivo']}
- Público: {answers['publico']}
- Formato escolhido: {answers['formato']}
- Ferramenta e local: {answers['ferramenta']}

## Conteúdo e estrutura

- Mensagem principal: {answers['resumo']}
- Estrutura e nomenclatura: {answers['estrutura']}
- Fontes, inputs e rastreabilidade: {answers['fontes']}

## Qualidade e consistência

- Forma e linguagem: {answers['forma']}
- Consistência texto-dado-visual: {answers['consistencia']}

## Revisão e risco

- Revisão humana e controles: {answers['revisao']}
- Riscos e limites: {answers['riscos']}
- Correção e nova versão: {answers['correcao']}

## Publicação e fechamento

- Armazenamento e acesso: {answers['armazenamento']}
- Critério de aceitação: {answers['aceitacao']}
- Próximo passo: {answers['proximo']}
"""


def render_i4_lab() -> None:
    lab = load_i4_lab()
    st.markdown("<div class='section-kicker'>ARTEFATOS DIGITAIS // I4</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.warning(str(lab["availability_note"]))
    st.info(str(lab["safety_note"]))

    columns = st.columns(2, gap="small")
    for index, card in enumerate(lab["artifact_cards"]):
        with columns[index % 2]:
            st.markdown(
                f"<div class='surface-card'><strong>{escape(card['name'])}</strong>"
                f"<p>{escape(card['description'])}</p>"
                f"<small>Limite: {escape(card['boundary'])}</small></div>",
                unsafe_allow_html=True,
            )

    labels = {
        "objetivo": "Objetivo e decisão de produção",
        "publico": "Público, contexto e impacto do artefato",
        "formato": "Formato, extensão e padrão de entrega",
        "ferramenta": "Ferramenta escolhida e justificativa",
        "resumo": "Mensagem principal e resumo executivo",
        "estrutura": "Seções, nomenclatura e organização interna",
        "fontes": "Fontes/inputs: origem, autorização, validade e limites",
        "forma": "Critérios de forma, linguagem e consistência visual",
        "consistencia": "Conferência entre texto, dado, cálculo e anexo",
        "revisao": "Revisão humana e evidência de aceite",
        "riscos": "Riscos de erro, distorção, dados sensíveis ou ambiguidade",
        "correcao": "Plano de correção, log e responsável",
        "armazenamento": "Local, controle de versão e método de compartilhamento",
        "aceitacao": "Critério objetivo para concluir a unidade",
        "proximo": "Próximo passo e ponto de continuidade",
    }
    answers = {
        key: st.text_area(labels[key], key=f"i4-{key}").strip()
        for key in lab["completion_fields"]
    }
    completed_count = sum(bool(value) for value in answers.values())
    st.progress(completed_count / len(answers))
    st.caption(f"{completed_count}/{len(answers)} componentes do artefato registrados")

    review_confirmed = st.checkbox(
        "Confirmo que revisei o artefato em ciclo humano e alinhei risco, consistência e forma antes da conclusão.",
        key="i4-review",
    )
    if completed_count == len(answers):
        if review_confirmed:
            st.success("Artefato revisado e rastreável. Revise a rubrica antes de avançar a I5.")
            st.download_button(
                "Baixar entrega I4 em Markdown",
                data=build_i4_delivery(answers),
                file_name="entrega-i4-producao-artefatos.md",
                mime="text/markdown",
            )
        else:
            st.warning("Finalize a revisão e a validação de risco antes de concluir I4.")


def build_i5_delivery(answers: dict[str, str]) -> str:
    return f"""# Entrega â€” I5: Personalização funcional

## Objetivo e escopo

- Objetivo: {answers['objetivo']}
- Público: {answers['publico']}
- Escopo e limite: {answers['escopo']}
- Critério de sucesso: {answers['aceite']}

## Prompt e conhecimento

- Prompt base: {answers['prompt_fundamental']}
- Perfil de resposta: {answers['perfil_resposta']}
- Mecanismo de início: {answers['mecanismo_inicio']}
- Arquivos/entrada: {answers['arquivos_entrada']}
- Restrições: {answers['restricoes']}
- Conhecimento por arquivos: {answers['conhecimentos']}

## Capacidades e integração

- Capacidades habilitadas: {answers['capacidades']}
- Integrações: {answers['integracoes']}

## Testes e operação

- Testes realizados: {answers['testes']}
- Falha e correções: {answers['falhas_e_correcoes']}
- Versionamento: {answers['versionamento']}
- Compartilhamento: {answers['compartilhamento']}
"""


def render_i5_lab() -> None:
    lab = load_i5_lab()
    st.markdown("<div class='section-kicker'>PERSONALIZAÇÃO FUNCIONAL // I5</div>", unsafe_allow_html=True)
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.warning(str(lab["availability_note"]))
    st.info(str(lab["safety_note"]))

    columns = st.columns(2, gap="small")
    for index, card in enumerate(lab["customization_cards"]):
        with columns[index % 2]:
            st.markdown(
                f"<div class='surface-card'><strong>{escape(card['name'])}</strong>"
                f"<p>{escape(card['description'])}</p>"
                f"<small>Limite: {escape(card['boundary'])}</small></div>",
                unsafe_allow_html=True,
            )

    labels = {
        "objetivo": "Objetivo funcional e valor esperado",
        "publico": "Público e superfície de uso",
        "escopo": "Escopo funcional, contexto e fronteiras",
        "prompt_fundamental": "Prompt-base e comportamento central",
        "perfil_resposta": "Perfil de resposta: tom, evidência e estrutura",
        "mecanismo_inicio": "Início, gatilho e entrada esperada",
        "arquivos_entrada": "Arquivos, fontes e critérios de atualização",
        "restricoes": "Restrições e riscos declarados",
        "conhecimentos": "Conhecimentos persistentes e controle de validade",
        "capacidades": "Capacidades habilitadas e justificativa de uso",
        "integracoes": "Integrações/Apps: escopo e pré-condições",
        "testes": "Plano e resultados de testes (caso feliz e falha)",
        "falhas_e_correcoes": "Falhas, impacto e plano de correção",
        "versionamento": "Versão, rollback e trilha de decisão",
        "compartilhamento": "Critérios de compartilhamento e retenção",
        "aceite": "Critério objetivo de aceite",
    }
    answers = {
        key: st.text_area(labels[key], key=f"i5-{key}").strip()
        for key in lab["completion_fields"]
    }
    completed_count = sum(bool(value) for value in answers.values())
    st.progress(completed_count / len(answers))
    st.caption(f"{completed_count}/{len(answers)} componentes da personalização registrados")

    review_confirmed = st.checkbox(
        "Confirmo que testei o comportamento em cenário feliz e falha, revisei controle de risco e registrei rollback quando necessário.",
        key="i5-review",
    )
    if completed_count == len(answers):
        if review_confirmed:
            st.success("Personalização testada e registrada. Revise a rubrica antes de avançar a I6.")
            st.download_button(
                "Baixar entrega I5 em Markdown",
                data=build_i5_delivery(answers),
                file_name="entrega-i5-personalizacao-funcional.md",
                mime="text/markdown",
            )
        else:
            st.warning("Conclua testes, risco e rollback antes de finalizar I5.")


st.set_page_config(
    page_title="Codex // Curso Completo",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      :root {
        --ink: #f3f8ff;
        --muted: #a9b7d2;
        --surface: #0a1228;
        --surface-2: #0e1934;
        --line: rgba(103, 216, 255, .22);
        --cyan: #67d8ff;
        --blue: #4d80ff;
        --violet: #9f8cff;
        --green: #64e2a7;
      }
      .stApp {
        background:
          radial-gradient(circle at 76% 13%, rgba(63, 123, 255, .23), transparent 27rem),
          radial-gradient(circle at 17% 20%, rgba(56, 217, 255, .12), transparent 22rem),
          #030817;
        color: var(--ink);
      }
      .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
        opacity: .48;
        background-image:
          linear-gradient(rgba(119, 175, 255, .08) 1px, transparent 1px),
          linear-gradient(90deg, rgba(119, 175, 255, .08) 1px, transparent 1px);
        background-size: 58px 58px;
        mask-image: linear-gradient(to bottom, black 0%, transparent 80%);
      }
      .block-container { position: relative; z-index: 1; max-width: 1320px; padding-top: 2.2rem; padding-bottom: 5rem; }
      header, [data-testid="stHeader"] { background: transparent; }
      h1, h2, h3, h4, p, label, .stMarkdown { color: var(--ink); }
      h1 { letter-spacing: -.055em; font-size: clamp(3.1rem, 6.1vw, 6.7rem) !important; line-height: .91; margin: .25rem 0 1.3rem; }
      h2, h3 { letter-spacing: -.03em; }
      .eyebrow, .section-kicker { color: var(--cyan); font: 700 .78rem/1 ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing: .13em; }
      .hero-copy { padding: 3rem 0 1.8rem; max-width: 670px; }
      .hero-copy h1 .neon { color: var(--cyan); text-shadow: 0 0 32px rgba(103,216,255,.32); }
      .hero-copy p { color: var(--muted); font-size: 1.22rem; line-height: 1.58; max-width: 620px; }
      .route-line { display: flex; flex-wrap: wrap; gap: .5rem; margin: 1.5rem 0; }
      .route-line span, .chip { border: 1px solid var(--line); background: rgba(13, 34, 68, .72); color: #c5efff; border-radius: 999px; padding: .36rem .72rem; font: 600 .75rem/1 ui-monospace, monospace; }
      .terminal-shell { margin: 3.6rem 0 1.5rem; border: 1px solid rgba(103,216,255,.28); border-radius: 22px; overflow: hidden; background: linear-gradient(145deg, rgba(15,29,52,.96), rgba(4,10,22,.97)); box-shadow: 0 22px 70px rgba(0,0,0,.38), 0 0 42px rgba(71,125,255,.18); transform: perspective(1100px) rotateY(-3deg) rotateX(1deg); }
      .terminal-bar { display:flex; gap:7px; align-items:center; padding: .85rem 1rem; background: rgba(1,5,12,.68); border-bottom: 1px solid var(--line); }
      .terminal-bar code { color: #8294b6; margin-left: auto; margin-right: auto; font-size: .72rem; }
      .dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }.red { background:#ff6f91; }.amber { background:#ffca6a; }.green { background:#64e2a7; }
      .terminal-body { padding: 1.55rem 1.65rem 1.2rem; font: .88rem/1.68 ui-monospace, SFMono-Regular, Menlo, monospace; color:#c4d7ed; min-height: 275px; }
      .terminal-body p { margin:.18rem 0; color:#b7c5d8; }.terminal-title{ color:var(--cyan) !important; font-weight:700; margin-top:1rem !important; }.prompt { color:#7eabff; }.terminal-ok { color:var(--green) !important; }.cursor { color:var(--cyan); animation: blink 1s step-end infinite; }@keyframes blink{50%{opacity:0}}
      .hero-note { color: var(--muted); font-size: .85rem; margin-top: .8rem; }
      .stButton > button, .stDownloadButton > button { width:100%; min-height: 3.25rem; border: 1px solid rgba(132,224,255,.52); border-radius: 13px; background: linear-gradient(100deg, #4c83ff, #55d4f7); color: #03101f; font-weight: 800; box-shadow: 0 8px 28px rgba(65,146,255,.28); }
      .stButton > button:hover, .stDownloadButton > button:hover { border-color:#e8fbff; background:linear-gradient(100deg,#79a7ff,#79ecff); color:#020914; }
      .stat-card, .story-card, .focus-card { border: 1px solid var(--line); background: linear-gradient(145deg, rgba(13,28,56,.88), rgba(5,13,30,.82)); border-radius: 18px; }
      .stat-card { padding: 1.15rem 1.2rem; min-height: 112px; }.stat-card span { color:var(--muted); font-size:.82rem; }.stat-card strong { display:block; color:var(--cyan); font-size:1.8rem; margin:.32rem 0; }.stat-card small{color:#cdd9ea;}
      .story-card { padding: 1.65rem; min-height: 100%; }.story-card p { color:var(--muted); font-size:1.03rem; line-height:1.6; }.story-card strong { color:var(--ink); }
      .mini-terminal { border:1px solid var(--line); border-radius:14px; background:#050b19; padding:1rem; font: .82rem/1.75 ui-monospace,monospace; color:#b5c8dc; margin-top:1.2rem; }.mini-terminal em{color:var(--green);font-style:normal;}.mini-terminal b{color:var(--cyan);}
      .focus-card { padding:1.3rem; margin:.45rem 0 1.2rem; }.focus-card h4{margin:.7rem 0 .5rem;}.focus-card p{color:var(--muted); line-height:1.55;}.pet-wrap{max-width:112px;}.surface-card{height:100%;border:1px solid var(--line);border-radius:13px;background:rgba(8,18,41,.84);padding:1rem}.surface-card strong{color:var(--cyan);font:800 .82rem/1 ui-monospace,monospace}.surface-card p{color:var(--ink);font-size:.9rem;line-height:1.42;margin:.7rem 0}.surface-card small{color:var(--muted);font-size:.77rem;line-height:1.3}.component-line{display:flex;flex-wrap:wrap;gap:.5rem;margin:.75rem 0 1.3rem}.component-line span{border:1px solid var(--line);border-radius:10px;background:rgba(9,23,49,.82);color:#c5efff;padding:.45rem .62rem;font:.72rem/1.2 ui-monospace,monospace}
      .syllabus-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:.8rem; margin:1.2rem 0 2.6rem; }.syllabus-card{display:grid;grid-template-columns:52px 1fr;gap:1rem;align-items:start;padding:1.05rem 1.12rem;border:1px solid var(--line);background:rgba(8,18,41,.84);border-radius:14px;min-height:105px;}.syllabus-card:hover{border-color:rgba(103,216,255,.7);background:rgba(15,34,69,.9);}.syllabus-number{color:var(--cyan);font:800 1.05rem/1 ui-monospace,monospace;padding-top:.15rem;}.syllabus-stage{color:#93a7c8;font:600 .66rem/1 ui-monospace,monospace;text-transform:uppercase;letter-spacing:.08em;}.syllabus-card h4{font-size:1rem;margin:.4rem 0 .3rem;letter-spacing:-.01em;}.syllabus-card p{color:var(--muted);font-size:.82rem;line-height:1.35;margin:0;}.syllabus-card.is-active{border-color:rgba(103,216,255,.75);box-shadow:inset 3px 0 var(--cyan);}.syllabus-card.is-done{border-color:rgba(100,226,167,.55);}.syllabus-card.is-done .syllabus-number{color:var(--green);}
      div[data-testid="stSelectbox"] label, div[data-testid="stTextInput"] label, div[data-testid="stTextArea"] label { color:#dceeff !important; font-weight:700; }.stSelectbox > div > div, .stTextInput input, .stTextArea textarea { background:rgba(5,14,32,.84) !important; border-color:rgba(103,216,255,.28) !important; color:#eff8ff !important; border-radius:11px !important; }.stExpander{border:1px solid var(--line) !important;background:rgba(9,21,46,.78) !important;border-radius:13px !important;}.stProgress > div > div > div{background:linear-gradient(90deg,var(--blue),var(--cyan)) !important;}.stAlert{background:rgba(15,35,68,.78) !important;border:1px solid var(--line) !important;color:var(--ink) !important;}.stDivider{border-color:var(--line) !important;}
      @media (max-width: 800px) { .block-container{padding-left:1rem;padding-right:1rem;}.terminal-shell{transform:none;margin-top:1rem;}.syllabus-grid{grid-template-columns:1fr;}h1{font-size:3.2rem !important;}.hero-copy{padding-top:1.4rem;} }
    </style>
    """,
    unsafe_allow_html=True,
)

course = load_course()
modules: list[dict[str, Any]] = course.get("modules", [])
if not modules:
    st.error("O catálogo do curso está vazio.")
    st.stop()

module_by_id = {module["id"]: module for module in modules}
if "focused_module" not in st.session_state:
    st.session_state["focused_module"] = "diagnostico"
progress = progress_state(modules)
done_count = sum(status == "done" for status in progress.values())

hero_left, hero_right = st.columns([1.03, 0.97], gap="large")
with hero_left:
    st.markdown(
        f"""
        <section class="hero-copy">
          <div class="eyebrow">CODEX // CURSO COMPLETO</div>
          <h1>Da primeira pergunta à <span class="neon">arquitetura</span> de sistemas com IA.</h1>
          <p>Uma trilha prática, profunda e verificável para operar ChatGPT, Codex, APIs, agentes e integrações — com autonomia, método e segurança.</p>
          <div class="route-line"><span>{len(modules)} unidades</span><span>3 trilhas avançadas</span><span>projeto final integrado</span></div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Iniciar pelo diagnóstico", key="hero-start"):
        set_focus("diagnostico")
        log_event("Diagnóstico inicial selecionado.")
        st.rerun()
    st.markdown("<div class='hero-note'>Comece pelo seu contexto. A tecnologia entra depois, com propósito.</div>", unsafe_allow_html=True)
with hero_right:
    st.markdown(build_terminal_preview(len(modules)), unsafe_allow_html=True)

stats = st.columns(3, gap="medium")
stats_data = [
    (f"{len(modules):02d}", "unidades explícitas", "do diagnóstico ao projeto final"),
    ("03", "trilhas avançadas", "ChatGPT, Codex e API Platform"),
    ("06", "critérios de banca", "qualidade, risco, custo e manutenção"),
]
for column, (number, label, detail) in zip(stats, stats_data):
    with column:
        st.markdown(
            f"<div class='stat-card'><span>{label}</span><strong>{number}</strong><small>{detail}</small></div>",
            unsafe_allow_html=True,
        )

st.divider()
story_left, story_right = st.columns([0.92, 1.08], gap="large")
with story_left:
    st.markdown(
        """
        <div class="story-card">
          <div class="section-kicker">COMO O CURSO FUNCIONA</div>
          <div class="mini-terminal"><b>~/curso</b><br>├── diagnóstico<br>├── fundamentos<br>├── workflows<br>├── especializações<br>└── <em>projeto-final</em></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with story_right:
    st.markdown(
        """
        <div class="story-card">
          <div class="section-kicker">PROGRESSÃO REAL</div>
          <h2>Você não recebe uma coleção de dicas.</h2>
          <p>Cada unidade tem posição no mapa, pré-requisito, prática, evidência e critério de conclusão. O curso começa pelo seu objetivo, passa por fundamentos comuns e abre especializações sem esconder a complexidade.</p>
          <p><strong>O mapa canônico é a fonte de verdade.</strong> A interface apenas torna essa trilha navegável, visual e interativa.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()
st.markdown("<div class='section-kicker'>EMENTA CANÔNICA</div>", unsafe_allow_html=True)
st.header("Toda a trilha, sem atalhos")
st.caption("Cada card representa uma unidade explícita do mapa aprovado.")
st.markdown(build_syllabus_cards(modules, progress), unsafe_allow_html=True)

st.markdown("<div class='section-kicker'>SALA DE OPERAÇÕES</div>", unsafe_allow_html=True)
st.header("Escolha a unidade em foco")
selected_id = st.selectbox(
    "Unidade",
    options=list(module_by_id),
    format_func=lambda module_id: f"{module_by_id[module_id]['stage']} · {module_by_id[module_id]['title']}",
    key="focused_module",
)
selected = module_by_id[selected_id]
selected_status = progress[selected_id]

detail_col, control_col = st.columns([1.7, 0.85], gap="large")
with detail_col:
    st.markdown(
        f"""
        <section class="focus-card">
          <div class="pet-wrap">{build_pet_svg(selected['pet'], selected['accent'], selected['glow'], modules.index(selected) + 1)}</div>
          <div class="chip">{escape(selected['stage'])} // {escape(selected['track'])}</div>
          <h4>{escape(selected['title'])}</h4>
          <p>{escape(selected['outcomes'][0])}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("**Escopo desta unidade**")
    for topic in selected.get("topics", []):
        st.markdown(f"- {topic}")
    st.markdown("**Entrega verificável**")
    st.info(selected["deliverable"])

with control_col:
    st.markdown("<div class='section-kicker'>CHECKPOINT</div>", unsafe_allow_html=True)
    st.markdown(f"**Estado atual:** {status_label(selected_status)}")
    if st.button("Marcar como em curso", key=f"start-{selected_id}"):
        progress[selected_id] = "active"
        log_event(f"{selected_id} iniciado.")
        st.rerun()
    if st.button("Marcar como concluída", key=f"done-{selected_id}"):
        progress[selected_id] = "done"
        log_event(f"{selected_id} concluído.")
        st.rerun()
    if st.button("Reiniciar checkpoint", key=f"reset-{selected_id}"):
        progress[selected_id] = "pending"
        log_event(f"{selected_id} reiniciado.")
        st.rerun()

if selected_id == "diagnostico":
    st.divider()
    render_diagnostic()

if selected_id == "preparacao":
    st.divider()
    render_preparation()

if selected_id == "basic-b1":
    st.divider()
    render_b1_lab()

if selected_id == "basic-b2":
    st.divider()
    render_b2_lab()

if selected_id == "basic-b3":
    st.divider()
    render_b3_lab()

if selected_id == "basic-b4":
    st.divider()
    render_b4_lab()

if selected_id == "basic-checkpoint":
    st.divider()
    render_basic_checkpoint()

if selected_id == "inter-i1":
    st.divider()
    render_i1_lab()

if selected_id == "inter-i2":
    st.divider()
    render_i2_lab()

if selected_id == "inter-i3":
    st.divider()
    render_i3_lab()

if selected_id == "inter-i4":
    st.divider()
    render_i4_lab()

if selected_id == "inter-i5":
    st.divider()
    render_i5_lab()

with st.expander("Log de navegação", expanded=False):
    log_lines = "\n".join(st.session_state.get("course_events", [])) or "Nenhum evento nesta sessão."
    st.code(log_lines, language="text")




