# Como conduzir o usuário (vale para todas as funções)

O plugin é operado por gente do time, não por especialista em marca. Cada função conduz a conversa em passos curtos, com perguntas de múltipla escolha (AskUserQuestion), e nunca começa a trabalhar com dúvida sobre cliente ou tarefa.

## Passo 0. Achar o workspace
Seguir `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`: localizar a pasta conectada `Onboarding Clientes`. Sem ela, pedir para conectar e parar.

## Passo 1. Qual cliente
1. Listar as pastas em `<workspace>/clientes/`.
2. Se o pedido já disser o cliente, confirmar só se houver ambiguidade.
3. Senão, perguntar "Para qual cliente?", uma opção por cliente. Cliente que não existe: oferecer a função `cliente-novo`.
4. Ler `clientes/<slug>/cliente.json` (onde está a referência e onde estão as peças a validar) e `diretrizes/regras.md`. Respeitar `fora_de_escopo`.

## Passo 2. Criar ou revisar
Se o pedido não deixar claro, perguntar:
- **Criar algo novo**: a pessoa ainda não tem a peça. Vai para `briefing-criacao`, que escreve ou orienta já dentro das regras e passa pelo checklist antes de entregar.
- **Revisar algo pronto**: a pessoa tem o texto, arquivo ou link. Vai para a função `revisar-*` do tipo da peça.
- **Auditar uma pasta inteira**: vai para `auditar-pasta`.
- **Tirar uma dúvida**: vai para `consultar-diretrizes`.

Pistas: "escreve", "cria", "monta", "faz um post sobre" é criar. "Revisa", "confere", "pode publicar?", "está dentro?", texto colado ou arquivo anexado é revisar.

## Passo 3. Como a peça chega (revisão)
Perguntar só o que faltar, numa pergunta só:
- Texto colado no chat
- Arquivo anexado
- Link
- Uma das pastas de `pecas_para_validar` do `cliente.json` (mostrar os nomes como opções)

## Passo 4. Contexto que muda a régua
No máximo duas perguntas: canal e formato; rascunho ou versão final.

## Passo 5. Executar e devolver
Seguir `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md`.

## Passo 6. Próximo passo
Fechar com múltipla escolha: aplicar as correções e devolver a versão final; revisar outra peça; gerar briefing para o designer; encerrar.

## Tom
Português, frases curtas, sem travessão e sem emoji. Mostrar o resultado, não o método. Dizer o que não deu para checar.
