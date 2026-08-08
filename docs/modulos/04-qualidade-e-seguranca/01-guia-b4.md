# B4 · Qualidade e segurança

> Mascote da unidade: **Shield**
>
> Fonte de produto: [fontes canônicas](../../fontes.md), verificada em
> 05-08-2026.

## Propósito

Transformar a revisão em uma etapa explícita do trabalho com IA. B4 não ensina
a confiar menos por reflexo; ensina a decidir o que pode ser usado, o que deve
ser conferido, o que precisa de autorização e o que não deve prosseguir.

## Fato documentado, inferência pedagógica e hipótese

**Fato documentado:** a orientação oficial de segurança recomenda revisão
humana antes do uso prático de saídas, com atenção especial a domínios de alto
risco. Ela também recomenda avaliar limitações, testar entradas adversariais e
restringir o uso quando o caso exigir controles adicionais.

**Inferência pedagógica:** uma ficha curta que registra evidência, classificação,
dados e decisão torna a revisão ensinável e auditável. A ficha não garante
correção; ela mostra o que ainda precisa ser confirmado.

**Hipótese a testar no contexto do participante:** a pessoa responsável tem
acesso à fonte primária, competência e autoridade para realizar a revisão
necessária. Se não tiver, a decisão precisa ser escalada ou interrompida.

Fonte: [Safety best practices](https://platform.openai.com/docs/guides/safety-best-practices).

## Matriz de decisão

| Pergunta | Evidência mínima | Decisão possível | Limite |
| --- | --- | --- | --- |
| O que a saída afirma? | Trecho, cálculo, recomendação ou ação identificada. | Classificar antes de usar. | Linguagem convincente não transforma hipótese em fato. |
| O que sustenta isso? | Fonte primária, material de origem, cálculo reproduzível ou lacuna declarada. | Conferir ou suspender. | Uma citação sem leitura não sustenta uma conclusão. |
| Há dados ou impacto relevante? | Tipo de dado, autorização, pessoas afetadas e consequência de erro. | Minimizar, anonimizar, escalar ou não usar. | Não envie segredos, chaves ou dados de terceiros sem base legítima. |
| Quem revisa e por qual critério? | Pessoa responsável, critério de aceitação e próximo passo. | Usar, revisar, escalar ou descartar. | Alto impacto exige revisão humana proporcional ao risco. |

## Roteiro seguro

1. Isole a afirmação, recomendação ou decisão. Não avalie uma resposta inteira
   como se ela fosse um bloco indivisível.
2. Classifique o que é fato documentado, inferência, hipótese ou afirmação sem
   suporte suficiente.
3. Localize a fonte primária ou o material de origem; se não houver, registre a
   lacuna em vez de preenchê-la por suposição.
4. Identifique dados pessoais, sigilo, segredo, autorização limitada e pessoas
   que podem ser afetadas pela ação.
5. Decida explicitamente: usar, revisar, escalar ou não usar. Para alto risco,
   deixe claro quem revisa e o que precisa confirmar.

## O que não fazer

- Não usar uma resposta como prova de que um fato, norma, prazo ou cálculo está
  correto.
- Não omitir a diferença entre fonte, interpretação e hipótese.
- Não inserir senhas, tokens, chaves de API, dados pessoais de terceiros ou
  material confidencial apenas para obter uma resposta mais específica.
- Não delegar ao modelo a decisão final sobre saúde, direito, finanças, emprego,
  disciplina, acesso ou outro resultado de alto impacto.

## Conexão com a próxima etapa

B4 encerra os fundamentos do Nível 1. O laboratório básico reunirá pesquisa,
arquivo e artefato em uma entrega verificável; quem não demonstrar contexto,
evidência e revisão retornará a B2 antes de avançar.
