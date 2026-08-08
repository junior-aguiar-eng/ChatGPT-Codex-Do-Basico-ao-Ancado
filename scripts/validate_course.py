"""Validates basic course metadata consistency."""

from __future__ import annotations

import json
from pathlib import Path

REQUIRED_OUTLINE_KEYS = {
    "id",
    "title",
    "stage",
    "track",
    "outcomes",
    "topics",
    "deliverable",
}
REQUIRED_LAB_KEYS = {
    "module_id",
    "title",
    "instructions",
    "task_types",
    "tool_options",
    "surface_cards",
    "scenarios",
}
REQUIRED_SCENARIO_KEYS = {"id", "title", "context", "risk_hint"}
REQUIRED_SURFACE_KEYS = {"name", "use_when", "boundary", "source"}
REQUIRED_DIAGNOSTIC_KEYS = {
    "module_id",
    "title",
    "purpose",
    "privacy_note",
    "entry_paths",
    "experience_levels",
    "environment_options",
    "care_options",
    "completion_fields",
}
REQUIRED_PREPARATION_KEYS = {
    "module_id",
    "title",
    "purpose",
    "availability_note",
    "official_source",
    "verified_on",
    "account_options",
    "workspace_options",
    "control_options",
    "completion_fields",
}
REQUIRED_B2_LAB_KEYS = {
    "module_id",
    "title",
    "instructions",
    "official_sources",
    "verified_on",
    "components",
    "scenarios",
    "completion_fields",
}
REQUIRED_B2_SCENARIO_KEYS = {"id", "title", "vague_request", "context_hint"}
REQUIRED_B3_LAB_KEYS = {
    "module_id",
    "title",
    "instructions",
    "official_sources",
    "verified_on",
    "availability_note",
    "capability_cards",
    "workflows",
    "completion_fields",
}
REQUIRED_B3_CARD_KEYS = {"name", "use_when", "evidence", "boundary"}
REQUIRED_B3_WORKFLOW_KEYS = {
    "id",
    "title",
    "prompt",
    "input_label",
    "input_placeholder",
    "evidence_label",
    "risk_hint",
}
REQUIRED_B4_LAB_KEYS = {
    "module_id",
    "title",
    "instructions",
    "official_sources",
    "verified_on",
    "safety_note",
    "quality_cards",
    "classification_options",
    "cases",
    "completion_fields",
}
REQUIRED_B4_CARD_KEYS = {"name", "question", "action", "boundary"}
REQUIRED_B4_CASE_KEYS = {
    "id",
    "title",
    "scenario",
    "risk_hint",
    "claim_label",
    "claim_placeholder",
}
REQUIRED_BASIC_CHECKPOINT_KEYS = {
    "module_id",
    "title",
    "instructions",
    "official_sources",
    "verified_on",
    "availability_note",
    "privacy_note",
    "checkpoint_options",
    "checkpoint_criteria",
    "completion_fields",
}
REQUIRED_CHECKPOINT_CRITERION_KEYS = {"id", "title", "question"}
REQUIRED_I1_LAB_KEYS = {
    "module_id",
    "title",
    "instructions",
    "official_sources",
    "verified_on",
    "availability_note",
    "privacy_note",
    "workspace_cards",
    "completion_fields",
}
REQUIRED_I1_CARD_KEYS = {"name", "purpose", "boundary"}
REQUIRED_I2_LAB_KEYS = {
    "module_id",
    "title",
    "instructions",
    "official_sources",
    "verified_on",
    "availability_note",
    "safety_note",
    "workflow_cards",
    "completion_fields",
}
REQUIRED_I2_CARD_KEYS = {"name", "question", "failure"}
REQUIRED_I3_LAB_KEYS = {"module_id", "title", "instructions", "official_sources", "verified_on", "availability_note", "safety_note", "research_cards", "completion_fields"}
REQUIRED_I3_CARD_KEYS = {"name", "use_when", "boundary"}


def validate_module1_lab() -> int:
    lab_path = Path("data/labs/modulo1.json")
    if not lab_path.exists():
        raise SystemExit("modulo1.json lab data not found.")

    lab = json.loads(lab_path.read_text(encoding="utf-8"))
    missing = REQUIRED_LAB_KEYS - set(lab.keys())
    if missing:
        raise SystemExit(f"Module 1 lab missing required keys: {sorted(missing)}")

    if lab["module_id"] != "basic-b1":
        raise SystemExit("Module 1 lab must have module_id='basic-b1'.")

    for key in ("task_types", "tool_options", "scenarios"):
        if not isinstance(lab[key], list) or not lab[key]:
            raise SystemExit(f"Module 1 lab key '{key}' must be a non-empty list.")

    for idx, scenario in enumerate(lab["scenarios"], start=1):
        if not isinstance(scenario, dict):
            raise SystemExit(f"Module 1 scenario #{idx} must be an object.")
        missing = REQUIRED_SCENARIO_KEYS - set(scenario.keys())
        if missing:
            raise SystemExit(
                f"Module 1 scenario #{idx} missing required keys: {sorted(missing)}"
            )

    if len(lab["scenarios"]) != 5:
        raise SystemExit("Module 1 must contain the five canonical B1 scenarios.")

    surface_names = {surface.get("name") for surface in lab["surface_cards"]}
    required_surfaces = {"ChatGPT", "Codex", "API Platform", "Processo manual"}
    if surface_names != required_surfaces:
        raise SystemExit("Module 1 surface cards do not match the B1 decision set.")

    for idx, surface in enumerate(lab["surface_cards"], start=1):
        missing = REQUIRED_SURFACE_KEYS - set(surface.keys())
        if missing:
            raise SystemExit(
                f"Module 1 surface #{idx} missing required keys: {sorted(missing)}"
            )

    return len(lab["scenarios"])


def validate_diagnostic() -> int:
    diagnostic_path = Path("data/diagnostico-inicial.json")
    if not diagnostic_path.exists():
        raise SystemExit("diagnostico-inicial.json data not found.")

    diagnostic = json.loads(diagnostic_path.read_text(encoding="utf-8"))
    missing = REQUIRED_DIAGNOSTIC_KEYS - set(diagnostic.keys())
    if missing:
        raise SystemExit(f"Diagnostic data missing required keys: {sorted(missing)}")

    if diagnostic["module_id"] != "diagnostico":
        raise SystemExit("Diagnostic data must have module_id='diagnostico'.")

    for key in (
        "entry_paths",
        "experience_levels",
        "environment_options",
        "care_options",
        "completion_fields",
    ):
        if not isinstance(diagnostic[key], list) or not diagnostic[key]:
            raise SystemExit(f"Diagnostic key '{key}' must be a non-empty list.")

    required_fields = {
        "objetivo",
        "rota",
        "repertório",
        "ambiente",
        "projeto",
        "cuidados",
        "sucesso",
    }
    if set(diagnostic["completion_fields"]) != required_fields:
        raise SystemExit("Diagnostic completion_fields do not match the required fields.")

    return len(diagnostic["completion_fields"])


def validate_preparation() -> int:
    preparation_path = Path("data/preparacao-do-ambiente.json")
    if not preparation_path.exists():
        raise SystemExit("preparacao-do-ambiente.json data not found.")

    preparation = json.loads(preparation_path.read_text(encoding="utf-8"))
    missing = REQUIRED_PREPARATION_KEYS - set(preparation.keys())
    if missing:
        raise SystemExit(f"Preparation data missing required keys: {sorted(missing)}")

    if preparation["module_id"] != "preparacao":
        raise SystemExit("Preparation data must have module_id='preparacao'.")

    for key in (
        "account_options",
        "workspace_options",
        "control_options",
        "completion_fields",
    ):
        if not isinstance(preparation[key], list) or not preparation[key]:
            raise SystemExit(f"Preparation key '{key}' must be a non-empty list.")

    required_fields = {
        "acesso",
        "disponibilidade",
        "workspace",
        "repositório",
        "dados",
        "revisão",
        "evidência",
    }
    if set(preparation["completion_fields"]) != required_fields:
        raise SystemExit("Preparation completion_fields do not match the required fields.")

    return len(preparation["completion_fields"])


def validate_b2_lab() -> int:
    lab_path = Path("data/fundamentos-interacao-b2.json")
    if not lab_path.exists():
        raise SystemExit("B2 lab data not found.")

    lab = json.loads(lab_path.read_text(encoding="utf-8"))
    missing = REQUIRED_B2_LAB_KEYS - set(lab.keys())
    if missing:
        raise SystemExit(f"B2 lab missing required keys: {sorted(missing)}")
    if lab["module_id"] != "basic-b2":
        raise SystemExit("B2 lab must have module_id='basic-b2'.")
    if len(lab["scenarios"]) != 3:
        raise SystemExit("B2 must contain the three canonical briefing scenarios.")
    for idx, scenario in enumerate(lab["scenarios"], start=1):
        missing = REQUIRED_B2_SCENARIO_KEYS - set(scenario.keys())
        if missing:
            raise SystemExit(f"B2 scenario #{idx} missing keys: {sorted(missing)}")

    required_fields = {
        "objetivo",
        "contexto",
        "instrucoes",
        "restricoes",
        "formato",
        "exemplo",
        "lacuna",
        "critica",
        "refinamento",
    }
    if set(lab["completion_fields"]) != required_fields:
        raise SystemExit("B2 completion_fields do not match the required fields.")
    return len(lab["scenarios"])


def validate_b3_lab() -> int:
    lab_path = Path("data/chatgpt-essencial-b3.json")
    if not lab_path.exists():
        raise SystemExit("B3 lab data not found.")

    lab = json.loads(lab_path.read_text(encoding="utf-8"))
    missing = REQUIRED_B3_LAB_KEYS - set(lab.keys())
    if missing:
        raise SystemExit(f"B3 lab missing required keys: {sorted(missing)}")
    if lab["module_id"] != "basic-b3":
        raise SystemExit("B3 lab must have module_id='basic-b3'.")
    if len(lab["capability_cards"]) != 4:
        raise SystemExit("B3 must contain the four capability cards.")
    if len(lab["workflows"]) != 3:
        raise SystemExit("B3 must contain the three evidence workflows.")
    for idx, card in enumerate(lab["capability_cards"], start=1):
        missing = REQUIRED_B3_CARD_KEYS - set(card.keys())
        if missing:
            raise SystemExit(f"B3 capability card #{idx} missing keys: {sorted(missing)}")
    for idx, workflow in enumerate(lab["workflows"], start=1):
        missing = REQUIRED_B3_WORKFLOW_KEYS - set(workflow.keys())
        if missing:
            raise SystemExit(f"B3 workflow #{idx} missing keys: {sorted(missing)}")

    required_fields = {"intencao", "evidencia", "disponibilidade", "revisao"}
    if set(lab["completion_fields"]) != required_fields:
        raise SystemExit("B3 completion_fields do not match the required fields.")
    return len(lab["workflows"])


def validate_b4_lab() -> int:
    lab_path = Path("data/qualidade-seguranca-b4.json")
    if not lab_path.exists():
        raise SystemExit("B4 lab data not found.")

    lab = json.loads(lab_path.read_text(encoding="utf-8"))
    missing = REQUIRED_B4_LAB_KEYS - set(lab.keys())
    if missing:
        raise SystemExit(f"B4 lab missing required keys: {sorted(missing)}")
    if lab["module_id"] != "basic-b4":
        raise SystemExit("B4 lab must have module_id='basic-b4'.")
    if len(lab["quality_cards"]) != 4:
        raise SystemExit("B4 must contain the four quality and safety cards.")
    if len(lab["cases"]) != 3:
        raise SystemExit("B4 must contain the three review cases.")
    for idx, card in enumerate(lab["quality_cards"], start=1):
        missing = REQUIRED_B4_CARD_KEYS - set(card.keys())
        if missing:
            raise SystemExit(f"B4 quality card #{idx} missing keys: {sorted(missing)}")
    for idx, case in enumerate(lab["cases"], start=1):
        missing = REQUIRED_B4_CASE_KEYS - set(case.keys())
        if missing:
            raise SystemExit(f"B4 case #{idx} missing keys: {sorted(missing)}")

    required_fields = {"afirmacao", "classificacao", "evidencia", "dados", "decisao"}
    if set(lab["completion_fields"]) != required_fields:
        raise SystemExit("B4 completion_fields do not match the required fields.")
    return len(lab["cases"])


def validate_basic_checkpoint() -> int:
    lab_path = Path("data/laboratorio-basico-checkpoint.json")
    if not lab_path.exists():
        raise SystemExit("Basic checkpoint data not found.")
    lab = json.loads(lab_path.read_text(encoding="utf-8"))
    missing = REQUIRED_BASIC_CHECKPOINT_KEYS - set(lab.keys())
    if missing:
        raise SystemExit(f"Basic checkpoint missing required keys: {sorted(missing)}")
    if lab["module_id"] != "basic-checkpoint":
        raise SystemExit("Basic checkpoint must have module_id='basic-checkpoint'.")
    if len(lab["checkpoint_criteria"]) != 4:
        raise SystemExit("Basic checkpoint must contain four canonical criteria.")
    for idx, criterion in enumerate(lab["checkpoint_criteria"], start=1):
        missing = REQUIRED_CHECKPOINT_CRITERION_KEYS - set(criterion.keys())
        if missing:
            raise SystemExit(f"Basic checkpoint criterion #{idx} missing keys: {sorted(missing)}")
    if len(lab["completion_fields"]) != 10:
        raise SystemExit("Basic checkpoint must contain ten delivery fields.")
    return len(lab["checkpoint_criteria"])


def validate_i1_lab() -> int:
    lab_path = Path("data/organizacao-persistente-i1.json")
    if not lab_path.exists():
        raise SystemExit("I1 lab data not found.")
    lab = json.loads(lab_path.read_text(encoding="utf-8"))
    missing = REQUIRED_I1_LAB_KEYS - set(lab.keys())
    if missing:
        raise SystemExit(f"I1 lab missing required keys: {sorted(missing)}")
    if lab["module_id"] != "inter-i1":
        raise SystemExit("I1 lab must have module_id='inter-i1'.")
    if len(lab["workspace_cards"]) != 5:
        raise SystemExit("I1 must contain the five workspace layers.")
    for idx, card in enumerate(lab["workspace_cards"], start=1):
        missing = REQUIRED_I1_CARD_KEYS - set(card.keys())
        if missing:
            raise SystemExit(f"I1 workspace card #{idx} missing keys: {sorted(missing)}")
    if len(lab["completion_fields"]) != 10:
        raise SystemExit("I1 must contain ten workspace completion fields.")
    return len(lab["workspace_cards"])


def validate_i2_lab() -> int:
    lab_path = Path("data/arquitetura-workflows-i2.json")
    if not lab_path.exists():
        raise SystemExit("I2 lab data not found.")
    lab = json.loads(lab_path.read_text(encoding="utf-8"))
    missing = REQUIRED_I2_LAB_KEYS - set(lab.keys())
    if missing:
        raise SystemExit(f"I2 lab missing required keys: {sorted(missing)}")
    if lab["module_id"] != "inter-i2":
        raise SystemExit("I2 lab must have module_id='inter-i2'.")
    if len(lab["workflow_cards"]) != 5:
        raise SystemExit("I2 must contain the five workflow decisions.")
    for idx, card in enumerate(lab["workflow_cards"], start=1):
        missing = REQUIRED_I2_CARD_KEYS - set(card.keys())
        if missing:
            raise SystemExit(f"I2 workflow card #{idx} missing keys: {sorted(missing)}")
    if len(lab["completion_fields"]) != 12:
        raise SystemExit("I2 must contain twelve workflow completion fields.")
    return len(lab["workflow_cards"])


def validate_i3_lab() -> int:
    path = Path("data/pesquisa-fontes-i3.json")
    if not path.exists():
        raise SystemExit("I3 lab data not found.")
    lab = json.loads(path.read_text(encoding="utf-8"))
    missing = REQUIRED_I3_LAB_KEYS - set(lab)
    if missing or lab["module_id"] != "inter-i3":
        raise SystemExit(f"I3 lab invalid or missing keys: {sorted(missing)}")
    if len(lab["research_cards"]) != 5 or len(lab["completion_fields"]) != 12:
        raise SystemExit("I3 must contain five research modes and twelve fields.")
    for idx, card in enumerate(lab["research_cards"], start=1):
        missing = REQUIRED_I3_CARD_KEYS - set(card)
        if missing:
            raise SystemExit(f"I3 research card #{idx} missing keys: {sorted(missing)}")
    return len(lab["research_cards"])


def main() -> None:
    outline = Path("data/course_outline.json")
    if not outline.exists():
        raise SystemExit("course_outline.json not found.")

    payload = json.loads(outline.read_text(encoding="utf-8"))
    modules = payload.get("modules")
    if not isinstance(modules, list) or not modules:
        raise SystemExit("course_outline.json must contain a non-empty modules list.")

    for idx, module in enumerate(modules, start=1):
        if not isinstance(module, dict):
            raise SystemExit(f"Module #{idx} must be an object.")

        missing = REQUIRED_OUTLINE_KEYS - set(module.keys())
        if missing:
            raise SystemExit(f"Module #{idx} missing required keys: {sorted(missing)}")

    expected_units = {
        "diagnostico",
        "preparacao",
        "basic-b1",
        "basic-b2",
        "basic-b3",
        "basic-b4",
        "basic-checkpoint",
        "inter-i1",
        "inter-i9",
        "chat-a1",
        "chat-a4",
        "codex-c1",
        "codex-c7",
        "api-p1",
        "api-p6",
        "integracao-m1",
    }
    present_units = {module["id"] for module in modules}
    missing_units = expected_units - present_units
    if missing_units:
        raise SystemExit(
            f"Course outline is missing canonical units: {sorted(missing_units)}"
        )

    map_path = Path("docs/mapa-do-curso.mmd")
    map_contents = map_path.read_text(encoding="utf-8")
    for marker in ("NÍVEL 1", "NÍVEL 2", "NÍVEL 3A", "NÍVEL 3B", "NÍVEL 3C"):
        if marker not in map_contents:
            raise SystemExit(f"Canonical map is missing marker: {marker}")

    scenario_count = validate_module1_lab()
    diagnostic_field_count = validate_diagnostic()
    preparation_field_count = validate_preparation()
    b2_scenario_count = validate_b2_lab()
    b3_workflow_count = validate_b3_lab()
    b4_case_count = validate_b4_lab()
    basic_checkpoint_count = validate_basic_checkpoint()
    i1_card_count = validate_i1_lab()
    i2_card_count = validate_i2_lab()
    i3_card_count = validate_i3_lab()
    print(
        f"Course outline OK: {len(modules)} modules loaded; "
        f"Module 1 lab OK: {scenario_count} scenarios loaded; "
        f"Diagnostic OK: {diagnostic_field_count} required fields loaded; "
        f"Preparation OK: {preparation_field_count} required fields loaded; "
        f"B2 lab OK: {b2_scenario_count} scenarios loaded; "
        f"B3 lab OK: {b3_workflow_count} workflows loaded; "
        f"B4 lab OK: {b4_case_count} review cases loaded; "
        f"Basic checkpoint OK: {basic_checkpoint_count} criteria loaded; "
        f"I1 lab OK: {i1_card_count} workspace layers loaded; "
        f"I2 lab OK: {i2_card_count} workflow decisions loaded; "
        f"I3 lab OK: {i3_card_count} research modes loaded."
    )


if __name__ == "__main__":
    main()





