import json
from pathlib import Path
from typing import Dict

import streamlit as st

BASE_DIR = Path(__file__).resolve().parents[1]
OUTLINE_PATH = BASE_DIR / "data" / "course_outline.json"
MODULE1_LAB_PATH = BASE_DIR / "data" / "labs" / "modulo1.json"


@st.cache_data
def load_outline() -> list[dict[str, object]]:
    payload = json.loads(OUTLINE_PATH.read_text(encoding="utf-8"))
    return payload.get("modules", [])


@st.cache_data
def load_module1_lab() -> dict[str, object]:
    return json.loads(MODULE1_LAB_PATH.read_text(encoding="utf-8"))


def load_progress() -> Dict[str, str]:
    if "module_progress" not in st.session_state:
        st.session_state["module_progress"] = {}
    return st.session_state["module_progress"]


def log_event(message: str) -> None:
    history = st.session_state.setdefault("course_events", [])
    history.append(message)
    st.session_state["course_events"] = history[-30:]


def status_text(status: str) -> str:
    if status == "done":
        return "concluido"
    if status == "active":
        return "em andamento"
    return "pendente"


def status_badge(status: str) -> str:
    if status == "done":
        return "[OK]"
    if status == "active":
        return "[RUN]"
    return "[ ]"


def build_module1_delivery(answers: list[dict[str, str]]) -> str:
    rows = "\n".join(
        "| {title} | {task_type} | {tool} | {reason} | {risk} | {review} |".format(
            **answer
        )
        for answer in answers
    )
    return f"""# Entrega — Módulo 1: Ecossistema e limites de LLM

> Gerado no laboratório interativo. Revise com a rubrica antes de enviar.

## Decisão de ferramenta por cenário

| Cenário | Tipo de tarefa | Ferramenta escolhida | Justificativa | Risco principal | Revisão humana |
| --- | --- | --- | --- | --- | --- |
{rows}

## Conclusão de risco

- Decido com LLM para:
- Não decido com LLM quando:
- Sempre reviso:
"""


def render_module1_lab() -> None:
    lab = load_module1_lab()
    st.divider()
    st.subheader(str(lab["title"]))
    st.caption(str(lab["instructions"]))
    st.info(
        "Checkpoint Atlas: complete a decisão, o risco e a revisão humana. "
        "A rubrica avalia a qualidade; este painel apenas organiza a missão."
    )

    answers: list[dict[str, str]] = []
    scenarios = lab["scenarios"]
    task_types = lab["task_types"]
    tool_options = lab["tool_options"]

    for position, scenario in enumerate(scenarios, start=1):
        scenario_id = scenario["id"]
        with st.expander(f"{position}. {scenario['title']}", expanded=position == 1):
            st.markdown(f"**Contexto:** {scenario['context']}")
            st.caption(f"Radar de risco: {scenario['risk_hint']}")
            task_type = st.selectbox(
                "Tipo de tarefa",
                options=["Selecione..."] + task_types,
                key=f"m1-type-{scenario_id}",
            )
            tool = st.selectbox(
                "Ferramenta escolhida",
                options=["Selecione..."] + tool_options,
                key=f"m1-tool-{scenario_id}",
            )
            reason = st.text_area(
                "Justificativa (até 2 frases)",
                key=f"m1-reason-{scenario_id}",
                placeholder="Explique a escolha com base no objetivo e no contexto.",
            ).strip()
            risk = st.text_input(
                "Risco principal",
                key=f"m1-risk-{scenario_id}",
                placeholder="Qual erro ou impacto precisa ser evitado?",
            ).strip()
            review = st.text_input(
                "Como será feita a revisão humana?",
                key=f"m1-review-{scenario_id}",
                placeholder="Descreva a checagem antes de considerar a tarefa concluída.",
            ).strip()
            answers.append(
                {
                    "title": str(scenario["title"]),
                    "task_type": task_type if task_type != "Selecione..." else "",
                    "tool": tool if tool != "Selecione..." else "",
                    "reason": reason,
                    "risk": risk,
                    "review": review,
                }
            )

    completed = sum(all(answer[key] for key in ("task_type", "tool", "reason", "risk", "review")) for answer in answers)
    st.progress(completed / len(answers))
    st.caption(f"{completed}/{len(answers)} cenários completos")

    if completed == len(answers):
        delivery = build_module1_delivery(answers)
        st.success("Missão preenchida. Faça a leitura final com a rubrica antes de concluir o módulo.")
        st.download_button(
            "Baixar entrega em Markdown",
            data=delivery,
            file_name="entrega-modulo-1.md",
            mime="text/markdown",
        )
    else:
        st.warning("Complete todos os campos para liberar a entrega em Markdown.")


def build_pet_svg(pet: str, color: str, glow: str, idx: int) -> str:
    eye_offset = 32
    blink = ""
    if idx % 2 == 0:
        blink = "0s"
    return f"""
    <svg width=\"92\" height=\"92\" viewBox=\"0 0 92 92\" aria-label=\"pet-{pet}\" role=\"img\">
      <defs>
        <radialGradient id=\"glow-{pet}\" cx=\"50%\" cy=\"50%\" r=\"50%\">
          <stop offset=\"0%\" stop-color=\"{glow}\" stop-opacity=\"0.35\" />
          <stop offset=\"70%\" stop-color=\"{glow}\" stop-opacity=\"0\" />
        </radialGradient>
      </defs>
      <circle cx=\"46\" cy=\"46\" r=\"44\" fill=\"url(#glow-{pet})\" />
      <rect x=\"11\" y=\"15\" width=\"70\" height=\"62\" rx=\"18\" fill=\"#0f2f52\" stroke=\"#7fd0ff\" stroke-width=\"2\" />
      <rect x=\"16\" y=\"22\" width=\"60\" height=\"48\" rx=\"12\" fill=\"#102f55\" />
      <rect x=\"26\" y=\"8\" width=\"40\" height=\"14\" rx=\"7\" fill=\"#0f4c8a\" />
      <rect x=\"29\" y=\"11\" width=\"34\" height=\"8\" rx=\"4\" fill=\"#8ad4ff\" />
      <circle cx=\"34\" cy=\"47\" r=\"5\" fill=\"{color}\" />
      <circle cx=\"58\" cy=\"47\" r=\"5\" fill=\"{color}\" />
      <circle cx=\"34\" cy=\"47\" r=\"2.3\" fill=\"#081a30\" />
      <circle cx=\"58\" cy=\"47\" r=\"2.3\" fill=\"#081a30\" />
      <rect x=\"38\" y=\"56\" width=\"16\" height=\"10\" rx=\"5\" fill=\"#d6ecff\" />
      <rect x=\"22\" y=\"63\" width=\"48\" height=\"4\" rx=\"2\" fill=\"#7ec5f5\" />
      <rect x=\"40\" y=\"66\" width=\"12\" height=\"8\" rx=\"2\" fill=\"#8ad4ff\" />
      <line x1=\"28\" y1=\"24\" x2=\"36\" y2=\"24\" stroke=\"#d6ecff\" stroke-width=\"2\" />
      <line x1=\"56\" y1=\"24\" x2=\"64\" y2=\"24\" stroke=\"#d6ecff\" stroke-width=\"2\" />
      <rect x=\"12\" y=\"65\" width=\"24\" height=\"4\" rx=\"2\" fill=\"#7ec5f5\" opacity=\"0.6\" />
      <rect x=\"56\" y=\"65\" width=\"24\" height=\"4\" rx=\"2\" fill=\"#7ec5f5\" opacity=\"0.6\" />
      <text x=\"46\" y=\"86\" text-anchor=\"middle\" font-size=\"8\" fill=\"#b8e5ff\" font-family=\"Arial, sans-serif\">{pet}</text>
    </svg>
    """


st.set_page_config(page_title="NEXUS Course Ops", page_icon="🛰️", layout="wide")

st.markdown(
    """
    <style>
      .stApp {
        background: radial-gradient(circle at 20% 20%, #0f2f52 0%, #071a2f 35%, #040f1a 100%);
      }
      .hero {
        border: 1px solid #2f6fa5;
        background: linear-gradient(135deg, #0b2a4a, #143d66);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
      }
      .hero h1, .hero p {
        color: #e3f4ff;
      }
      .hero span {
        color: #9ee0ff;
        font-size: 1rem;
      }
      .module-card {
        border: 1px solid #2f6fa5;
        border-radius: 14px;
        padding: 14px;
        margin-bottom: 12px;
        background: linear-gradient(145deg, rgba(15, 67, 109, 0.78), rgba(14, 44, 77, 0.64));
      }
      .small-chip {
        display: inline-block;
        padding: 4px 10px;
        margin: 2px 6px 2px 0;
        border-radius: 999px;
        border: 1px solid #2f6fa5;
        color: #b8e5ff;
        background: rgba(12, 62, 110, 0.55);
        font-size: 0.8rem;
      }
      .status {
        font-weight: 700;
        color: #9ee0ff;
      }
      .section {
        color: #cde9ff;
      }
      .pet-card {
        border: 1px solid #2f6fa5;
        border-radius: 12px;
        padding: 8px;
        margin-bottom: 10px;
        display: inline-block;
        background: linear-gradient(155deg, rgba(8, 36, 67, 0.85), rgba(15, 52, 88, 0.75));
      }
    </style>
    """,
    unsafe_allow_html=True,
)


modules = load_outline()
if not modules:
    st.error("Modulo de dados vazio. Ajuste data/course_outline.json.")
    st.stop()

progress = load_progress()
for module in modules:
    progress.setdefault(module["id"], "pending")

done_count = sum(1 for state in progress.values() if state == "done")
total_count = len(modules)
progress_ratio = 0 if not total_count else done_count / total_count

st.markdown(
    """
    <div class="hero">
      <span>NEXUS COURSE OPS</span>
      <h1>Interface do curso ChatGPT e Codex</h1>
      <p>Clean, azulada, tecnica e com marca visual de mini pet por modulo.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([2, 1], gap="large")
with left:
    st.markdown("<span class='section'>Progresso da trilha</span>", unsafe_allow_html=True)
    st.progress(progress_ratio)
    st.caption(f"{done_count}/{total_count} modulos concluídos")
with right:
    st.markdown("<span class='section'>Terminal de start</span>", unsafe_allow_html=True)
    st.code("python -m streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0")

st.divider()
st.subheader("Painel de modulos")

title_to_module = {m["title"]: m for m in modules}
titles = list(title_to_module.keys())
selected_title = st.radio("Foco atual", options=titles, horizontal=False)
selected = title_to_module[selected_title]

selected_pet = selected.get("pet", "Nexus")
selected_color = selected.get("accent", "#6ec5ff")
selected_glow = selected.get("glow", "#2fb2ff")

detail_col, action_col = st.columns([2, 1], gap="large")
with detail_col:
    st.markdown(
        f"""
        <div class='module-card'>
          <div class='pet-card'>{build_pet_svg(selected_pet, selected_color, selected_glow, done_count)}</div>
          <div>
            <span class='small-chip'>id: {selected.get('id')}</span>
            <span class='small-chip'>nivel: {selected.get('level')}</span>
            <span class='small-chip'>status: {status_text(progress[selected['id']])}</span>
          </div>
          <h4 style='color:#cde9ff;'>{selected.get('title')}</h4>
          <p class='status'>{selected.get('mission')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("**Resultados esperados**")
    for outcome in selected["outcomes"]:
        st.markdown(f"- {outcome}")
    st.markdown("**Entrega principal**")
    st.info(selected["deliverable"])

with action_col:
    st.markdown("<span class='section'>Controle de execucao</span>", unsafe_allow_html=True)
    if st.button("Iniciar modulo", key=f"start-{selected['id']}"):
        progress[selected["id"]] = "active"
        log_event(f"{selected['id']} iniciado.")
        st.rerun()
    if st.button("Concluir modulo", key=f"done-{selected['id']}"):
        progress[selected["id"]] = "done"
        log_event(f"{selected['id']} concluido.")
        st.rerun()
    if st.button("Reset modulo", key=f"reset-{selected['id']}"):
        progress[selected["id"]] = "pending"
        log_event(f"{selected['id']} resetado.")
        st.rerun()

if selected["id"] == "modulo1":
    render_module1_lab()

for idx, module in enumerate(modules, start=1):
    state = progress.get(module["id"], "pending")
    badge = status_badge(state)
    st.markdown(
        f"<span class='status'>{badge}</span> {idx}. {module.get('pet', 'Nexus')}  ·  {module['title']}",
        unsafe_allow_html=True,
    )
    with st.expander("Detalhes do modulo", expanded=False):
        cols = st.columns([1, 3])
        with cols[0]:
            st.markdown(
                f"<div class='pet-card'>{build_pet_svg(module.get('pet','Nexus'), module.get('accent','#6ec5ff'), module.get('glow','#2fb2ff'), idx)}</div>",
                unsafe_allow_html=True,
            )
        with cols[1]:
            st.markdown(f"**Status:** {status_text(state)}")
            st.markdown(module.get("mission", ""))
            for item in module["outcomes"]:
                st.markdown(f"- {item}")

st.divider()
with st.expander("Nerd log", expanded=False):
    log_lines = "\n".join(st.session_state.get("course_events", [])) or "Ainda sem eventos."
    st.code(log_lines, language="text")
