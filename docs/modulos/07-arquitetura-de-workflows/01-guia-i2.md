# I2 · Arquitetura de workflows

## Objetivo

Projetar um fluxo repetível, verificável e corrigível antes de automatizá-lo. O
participante deve conseguir explicar como cada entrada vira uma saída, qual
ferramenta atua em cada etapa, onde a qualidade é verificada e como o processo
é retomado após uma falha.

## Workflow não é uma lista de tarefas

Uma lista informa o que fazer. Uma arquitetura de workflow também define:

- entradas necessárias e sua qualidade mínima;
- transformação e ferramenta de cada etapa;
- saída esperada e formato;
- gate que autoriza a passagem à etapa seguinte;
- responsável pela decisão ou revisão;
- tratamento de erro, ponto de parada e caminho de correção;
- registro das decisões e da versão produzida.

## Comece pela definição de pronto

A documentação oficial da OpenAI, verificada em 08-08-2026, recomenda que
trabalhos de várias etapas declarem resultado, restrições e verificação. Em
Goal mode, o próprio objetivo funciona como critério de conclusão; em outras
superfícies, esses elementos devem estar no pedido e no plano.
[Long-running work](https://learn.chatgpt.com/docs/long-running-work).

Para I2, a definição de pronto deve permitir uma decisão objetiva: aprovado,
reprovado ou bloqueado por evidência ausente. “Parece bom” não é gate.

## Decomposição com contratos

Divida o processo quando houver mudança de ferramenta, responsável, formato,
risco ou critério de aceite. Para cada etapa, escreva um pequeno contrato:

| Elemento | Pergunta |
| --- | --- |
| Entrada | O que precisa existir e em qual estado? |
| Transformação | O que acontece sem ocultar decisões humanas? |
| Ferramenta | Por que esta superfície é necessária e autorizada? |
| Saída | Qual artefato, formato e localização serão produzidos? |
| Gate | Qual evidência permite avançar? |
| Falha | Quando parar, corrigir, repetir ou escalar? |

Uma etapa não deve aceitar como entrada uma saída que ainda não passou pelo
gate anterior.

## Ferramenta adequada

Escolha a ferramenta pelo contrato, não pela novidade. Chat pode servir para
formular ou revisar; arquivos podem sustentar análise; uma planilha pode ser a
fonte de cálculo; código pode validar regras repetíveis; processo manual pode
ser superior quando há alto impacto ou baixa frequência. Permissão e
necessidade vêm antes da automação.

ChatGPT Work e controles de tarefas prolongadas podem variar por plano,
workspace, superfície, região, permissões e rollout. O método de I2 continua
válido quando a execução é manual.

## Gates próximos da causa

Valide cedo. Um gate deve indicar:

1. o objeto verificado;
2. o método ou evidência;
3. o resultado esperado;
4. quem decide;
5. a ação quando falha.

Testes, conferência de fonte, reconciliação de totais, revisão de formato e
aprovação humana são gates diferentes. Um não substitui o outro.

## Registro e versão

Ao final de cada execução, registre entrada usada, versão do fluxo, decisões,
exceções, validações, artefatos gerados e próximo passo. Mudança de regra exige
nova versão; correção silenciosa impede reprodução e auditoria.

## Limites e conexão com I3

I2 desenha o fluxo e pode indicar que uma etapa precisa pesquisar. A técnica de
busca, Deep Research, comparação de fontes e síntese rastreável pertence a I3 e
não é antecipada aqui.
