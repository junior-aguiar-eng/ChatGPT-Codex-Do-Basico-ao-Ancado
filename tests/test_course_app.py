from streamlit.testing.v1 import AppTest


APP_PATH = "app/main.py"
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
    app.selectbox[1].set_value("Trabalho intelectual: usar ChatGPT com método")
    app.selectbox[2].set_value("Estou começando agora")
    app.multiselect[0].set_value(["Ambiente em nuvem"])
    app.text_area[1].set_value("Uma rotina de estudos verificável.")
    app.multiselect[1].set_value(["Prazo ou impacto operacional"])
    app.text_area[2].set_value("Revisar antes de compartilhar.")
    app.text_area[3].set_value("Entregar uma atividade revisada.")
    app.checkbox[0].set_value(True)
    app.run()

    assert_download_available(app, "Diagnóstico concluído")


def test_preparation_completion_exports_markdown() -> None:
    app = run_app("preparacao")
    app.selectbox[1].set_value("Conta pessoal, com acesso confirmado")
    app.text_area[0].set_value("Página da conta e configurações do workspace.")
    app.multiselect[0].set_value(["GitHub Codespaces"])
    app.text_area[1].set_value("Repositório GitHub do curso com pull requests.")
    app.text_area[2].set_value("Exemplos públicos e dados anonimizados.")
    app.text_area[3].set_value("Segredos, tokens e dados pessoais de terceiros.")
    app.multiselect[1].set_value(["Não compartilhar senhas, chaves de API ou tokens"])
    app.text_area[4].set_value("Revisar o diff e os testes antes do merge.")
    app.text_input[0].set_value("docs/entregas/00-entrada/preparacao-do-ambiente.md")
    app.checkbox[0].set_value(True)
    app.run()

    assert_download_available(app, "Preparação concluída")


def test_b1_completion_exports_markdown() -> None:
    app = run_app("basic-b1")
    tools = [
        "ChatGPT (interface)",
        "Codex (projeto ou repositório)",
        "Sem LLM / processo manual",
        "Sem LLM / processo manual",
        "API Platform (aplicação)",
    ]
    task_types = [
        "síntese",
        "edição local",
        "decisão operacional",
        "decisão operacional",
        "integração de aplicação",
    ]

    for index, task_type in enumerate(task_types):
        app.selectbox[1 + index * 2].set_value(task_type)
        app.selectbox[2 + index * 2].set_value(tools[index])
        alternative = (
            "Codex (projeto ou repositório)"
            if tools[index] == "ChatGPT (interface)"
            else "ChatGPT (interface)"
        )
        app.multiselect[index].set_value([alternative])
        app.text_area[index].set_value("Escolha alinhada ao objetivo e ao contexto.")
        app.text_input[index].set_value("Evitar impacto sem validação.")
        app.text_input[5 + index].set_value("Revisão humana antes da conclusão.")
    app.run()

    assert_download_available(app, "Checkpoint preenchido")


def test_b2_completion_exports_markdown() -> None:
    app = run_app("basic-b2")
    assert len(app.text_area) == 24
    assert len(app.text_input) == 3

    for field in app.text_area:
        field.set_value("Componente explícito e revisável.")
    for field in app.text_input:
        field.set_value("Tabela concisa em português.")
    app.run()

    assert_download_available(app, "Briefings completos")

