"""Validates basic course metadata consistency."""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_OUTLINE_KEYS = {"id", "title", "outcomes", "deliverable"}
REQUIRED_LAB_KEYS = {
    "module_id",
    "title",
    "instructions",
    "task_types",
    "tool_options",
    "scenarios",
}
REQUIRED_SCENARIO_KEYS = {"id", "title", "context", "risk_hint"}


def validate_module1_lab() -> int:
    lab_path = Path("data/labs/modulo1.json")
    if not lab_path.exists():
        raise SystemExit("modulo1.json lab data not found.")

    lab = json.loads(lab_path.read_text(encoding="utf-8"))
    missing = REQUIRED_LAB_KEYS - set(lab.keys())
    if missing:
        raise SystemExit(f"Module 1 lab missing required keys: {sorted(missing)}")

    if lab["module_id"] != "modulo1":
        raise SystemExit("Module 1 lab must have module_id='modulo1'.")

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

    return len(lab["scenarios"])


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

    scenario_count = validate_module1_lab()
    print(
        f"Course outline OK: {len(modules)} modules loaded; "
        f"Module 1 lab OK: {scenario_count} scenarios loaded."
    )


if __name__ == "__main__":
    main()
