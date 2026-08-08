from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = Path(__file__).resolve().parents[1] / "app" / "main.py"
APP_TIMEOUT_SECONDS = 10


def run_app(module_id: str) -> AppTest:
    app = AppTest.from_file(APP_PATH)
    app.run(timeout=APP_TIMEOUT_SECONDS)
    app.selectbox[0].set_value(module_id)
    app.run(timeout=APP_TIMEOUT_SECONDS)
    assert not app.exception
    return app


def assert_download_available(app: AppTest, success_message: str) -> None:
    assert any(success_message in item.value for item in app.success)
    assert len(app.get("download_button")) == 1


def test_diagnostic_completion_exports_markdown() -> None:
    app = run_app("diagnostico")
    app.text_area[0].set_value("Aprender a operar o curso com autonomia.")
    app.selectbox[1].set_value("Trabalho intelectual: usar ChatGPT com mÃ©todo")
    app.selectbox[2].set_value("Estou comeÃ§ando agora")
    app.multiselect[0].set_value(["Ambiente em nuvem"])
    app.text_area[1].set_value("Uma rotina de estudos verificÃ¡vel.")
    app.multiselect[1].set_value(["Prazo ou impacto operacional"])
    app.text_area[2].set_value("Revisar antes de compartilhar.")
    app.text_area[3].set_value("Entregar uma atividade revisada.")
    app.checkbox[0].set_value(True)
    app.run()

    assert_download_available(app, "DiagnÃ³stico concluÃ­do")


def test_preparation_completion_exports_markdown() -> None:
    app = run_app("preparacao")
    app.selectbox[1].set_value("Conta pessoal, com acesso confirmado")
    app.text_area[0].set_value("PÃ¡gina da conta e configuraÃ§Ãµes do workspace.")
    app.multiselect[0].set_value(["GitHub Codespaces"])
    app.text_area[1].set_value("RepositÃ³rio GitHub do curso com pull requests.")
    app.text_area[2].set_value("Exemplos pÃºblicos e dados anonimizados.")
    app.text_area[3].set_value("Segredos, tokens e dados pessoais de terceiros.")
    app.multiselect[1].set_value(["NÃ£o compartilhar senhas, chaves de API ou tokens"])
    app.text_area[4].set_value("Revisar o diff e os testes antes do merge.")
    app.text_input[0].set_value("docs/entregas/00-entrada/preparacao-do-ambiente.md")
    app.checkbox[0].set_value(True)
    app.run()

    assert_download_available(app, "PreparaÃ§Ã£o concluÃ­da")


def test_b1_completion_exports_markdown() -> None:
    app = run_app("basic-b1")
    tools = [
        "ChatGPT (interface)",
        "Codex (projeto ou repositÃ³rio)",
        "Sem LLM / processo manual",
        "Sem LLM / processo manual",
        "API Platform (aplicaÃ§Ã£o)",
    ]
    task_types = [
        "sÃ­ntese",
        "ediÃ§Ã£o local",
        "decisÃ£o operacional",
        "decisÃ£o operacional",
        "integraÃ§Ã£o de aplicaÃ§Ã£o",
    ]

    for index, task_type in enumerate(task_types):
        app.selectbox[1 + index * 2].set_value(task_type)
        app.selectbox[2 + index * 2].set_value(tools[index])
        alternative = (
            "Codex (projeto ou repositÃ³rio)"
            if tools[index] == "ChatGPT (interface)"
            else "ChatGPT (interface)"
        )
        app.multiselect[index].set_value([alternative])
        app.text_area[index].set_value("Escolha alinhada ao objetivo e ao contexto.")
        app.text_input[index].set_value("Evitar impacto sem validaÃ§Ã£o.")
        app.text_input[5 + index].set_value("RevisÃ£o humana antes da conclusÃ£o.")
    app.run()

    assert_download_available(app, "Checkpoint preenchido")


def test_b2_completion_exports_markdown() -> None:
    app = run_app("basic-b2")
    assert len(app.text_area) == 24
    assert len(app.text_input) == 3

    for field in app.text_area:
        field.set_value("Componente explÃ­cito e revisÃ¡vel.")
    for field in app.text_input:
        field.set_value("Tabela concisa em portuguÃªs.")
    app.run()

    assert_download_available(app, "Briefings completos")


def test_b3_completion_exports_markdown() -> None:
    app = run_app("basic-b3")
    assert len(app.text_area) == 9
    assert len(app.text_input) == 3

    for field in app.text_area:
        field.set_value("Registro autorizado, rastreÃ¡vel e revisado.")
    for field in app.text_input:
        field.set_value("DisponÃ­vel nesta plataforma; alternativa registrada.")
    app.checkbox[0].set_value(True)
    app.run(timeout=APP_TIMEOUT_SECONDS)

    assert_download_available(app, "Entrega multimodal registrada")


def test_b4_completion_exports_markdown() -> None:
    app = run_app("basic-b4")
    assert len(app.text_area) == 9
    assert len(app.text_input) == 3

    for index in range(3):
        app.selectbox[1 + index].set_value("Fato documentado")
    for field in app.text_area:
        field.set_value("Registro verificÃ¡vel, sem dados sensÃ­veis e com limite explÃ­cito.")
    for field in app.text_input:
        field.set_value("Revisar fonte primÃ¡ria antes de usar ou publicar.")
    app.checkbox[0].set_value(True)
    app.run(timeout=APP_TIMEOUT_SECONDS)

    assert_download_available(app, "RelatÃ³rio de qualidade e seguranÃ§a concluÃ­do")


def test_basic_checkpoint_advances_when_all_criteria_are_consolidated() -> None:
    app = run_app("basic-checkpoint")
    assert len(app.text_area) == 10
    assert len(app.text_input) == 4

    for field in app.text_area:
        field.set_value("EvidÃªncia especÃ­fica, autorizada e verificÃ¡vel.")
    for index in range(4):
        app.selectbox[1 + index].set_value("Consolidada â€” demonstrei com evidÃªncia")
    for field in app.text_input:
        field.set_value("Campo e fonte identificados na entrega.")
    app.run(timeout=APP_TIMEOUT_SECONDS)

    assert_download_available(app, "AvanÃ§ar a I1")


def test_basic_checkpoint_routes_to_b2_when_a_criterion_is_incomplete() -> None:
    app = run_app("basic-checkpoint")
    for field in app.text_area:
        field.set_value("EvidÃªncia especÃ­fica, autorizada e verificÃ¡vel.")
    for index in range(4):
        status = (
            "Em desenvolvimento â€” a evidÃªncia ficou incompleta"
            if index == 0
            else "Consolidada â€” demonstrei com evidÃªncia"
        )
        app.selectbox[1 + index].set_value(status)
    for field in app.text_input:
        field.set_value("Campo e fonte identificados na entrega.")
    app.run(timeout=APP_TIMEOUT_SECONDS)

    assert any("Retornar a B2" in item.value for item in app.warning)
    assert len(app.get("download_button")) == 1


def test_i1_completion_exports_recoverable_workspace() -> None:
    app = run_app("inter-i1")
    assert len(app.text_area) == 10

    for field in app.text_area:
        field.set_value("Registro durÃ¡vel, autorizado, versionado e recuperÃ¡vel.")
    app.checkbox[0].set_value(True)
    app.run(timeout=APP_TIMEOUT_SECONDS)

    assert_download_available(app, "Workspace recuperÃ¡vel concluÃ­do")


def test_i2_completion_exports_documented_workflow() -> None:
    app = run_app("inter-i2")
    assert len(app.text_area) == 12

    for field in app.text_area:
        field.set_value("Contrato explÃ­cito, autorizado, verificÃ¡vel e corrigÃ­vel.")
    app.checkbox[0].set_value(True)
    app.run(timeout=APP_TIMEOUT_SECONDS)

    assert_download_available(app, "Workflow documentado e simulado")


def test_i3_completion_exports_cited_report() -> None:
    app = run_app("inter-i3")
    assert len(app.text_area) == 12
    for field in app.text_area:
        field.set_value("EvidÃªncia lida, datada, comparada e rastreÃ¡vel.")
    app.checkbox[0].set_value(True)
    app.run(timeout=APP_TIMEOUT_SECONDS)
    assert_download_available(app, "RelatÃ³rio citado concluÃ­do")



def test_i4_completion_exports_artifact_output() -> None:
    app = run_app("inter-i4")
    assert len(app.text_area) == 15
    for field in app.text_area:
        field.set_value("Rastreabilidade, consistÃªncia e revisÃ£o humana concluÃ­das antes da publicaÃ§Ã£o.")
    app.checkbox[0].set_value(True)
    app.run(timeout=APP_TIMEOUT_SECONDS)
    assert_download_available(app, "Artefato revisado e rastreÃ¡vel")


def test_i5_completion_exports_functional_customization() -> None:
    app = run_app("inter-i5")
    assert len(app.text_area) == 16
    for field in app.text_area:
        field.set_value("Objetivo e contexto, restriÃ§Ãµes, plano de testes e rollback registrados.")
    app.checkbox[0].set_value(True)
    app.run(timeout=APP_TIMEOUT_SECONDS)
    assert_download_available(app, "PersonalizaÃ§Ã£o testada e registrada")
