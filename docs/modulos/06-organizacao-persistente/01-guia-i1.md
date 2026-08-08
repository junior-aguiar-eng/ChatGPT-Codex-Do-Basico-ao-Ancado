# I1 · Organização persistente

## Objetivo

Organizar conhecimento e contexto de trabalho para que uma atividade possa ser
interrompida, retomada e revisada sem depender da lembrança de uma pessoa ou de
um único histórico de chat.

## O que é persistência neste módulo

Persistência não significa guardar tudo. Significa saber qual é a fonte de
verdade, onde ficam as regras obrigatórias, quais materiais sustentam o trabalho
e como reconstruir o estado atual.

Segundo a documentação oficial da OpenAI verificada em 08-08-2026, Projects
podem reunir chats, arquivos, fontes e instruções relacionadas. Chats separados
mantêm resultados distintos, enquanto o projeto preserva contexto
compartilhado. Um Project do ChatGPT não acessa automaticamente uma pasta local;
as fontes precisam ser enviadas ou conectadas. [Projects and
chats](https://learn.chatgpt.com/docs/projects).

## Cinco camadas que não devem ser confundidas

1. **Workspace:** contêiner do objetivo, dos chats e das fontes relacionadas.
2. **Instruções do projeto:** regras obrigatórias, critérios e limites.
3. **Memória:** camada auxiliar para preferências e contexto útil.
4. **Fontes:** arquivos e referências com origem, versão e autorização.
5. **Checkpoint:** resumo canônico do estado, das decisões e das pendências.

A documentação oficial distingue memória de orientação obrigatória: memórias
podem carregar contexto útil, mas regras que sempre devem valer pertencem às
instruções ou à documentação versionada. [Personalize
ChatGPT](https://learn.chatgpt.com/docs/personalize) e
[Memories](https://learn.chatgpt.com/docs/customization/memories).

## Library e reutilização

Neste curso, “Library” é tratada funcionalmente como acesso e reutilização de
arquivos disponíveis na conta. Ela não será pressuposta. Quando a interface ou
o recurso não estiver disponível, mantenha um inventário manual com nome,
origem, finalidade, data, versão, autorização e localização do arquivo.

Reutilizar não é copiar sem revisão: confira se o material continua atual, se a
autorização cobre o novo uso e se uma versão posterior o substituiu.

## Gestão de contexto

Um bom checkpoint responde, sem reler todo o histórico:

- qual é o objetivo e o que está fora do escopo;
- quais instruções são obrigatórias;
- quais fontes são canônicas e em que versão;
- o que já foi decidido e com qual evidência;
- quais pendências permanecem;
- qual é a próxima ação reproduzível.

## Limites

Projects, memórias, fontes conectadas e inventários podem depender de plano,
conta, workspace, plataforma, região, permissões e rollout. Memória pode estar
desativada ou incompleta. Não armazene segredos nela nem presuma que contexto
lembrado seja evidência atual.

## Conexão com I2

I1 entrega o workspace recuperável. I2 usará essa base para decompor o trabalho
em entradas, etapas, saídas, validações e versões; não antecipe a arquitetura do
workflow neste módulo.
