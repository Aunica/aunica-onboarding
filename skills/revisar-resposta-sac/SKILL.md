---
name: revisar-resposta-sac
description: Revisa ou redige resposta a comentário, direct ou mensagem nas redes de um cliente usando o guia de interações (SAC) dele. Use quando pedirem para responder comentário, direct, menção, reclamação, pedido de vaga ou denúncia nas redes do cliente.
---

# Revisar resposta de SAC

Antes de tudo, ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md`, `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md` e, para arquivos, `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Seguir os passos de interação: cliente, como a peça chega, contexto. Depois carregar `<workspace>/clientes/<slug>/cliente.json` e `diretrizes/regras.md` (workspace: ver `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`).

## Contexto específico desta função
Perguntar, se não estiver claro:
- O que a pessoa escreveu (texto exato) e em qual rede.
- Quem é: colaborador, candidato, cliente, fornecedor, outro.

## Blocos de regra que se aplicam
SEN, SAC e TXT.

## O que checar, nesta ordem
1. Identificar o caso no guia de interações do cliente (vaga, processo seletivo, comercial, parceria, denúncia, crise).
2. Usar o modelo aprovado e personalizar com o nome e o que a pessoa disse.
3. Tema sensível: só o texto aprovado; se não houver, encaminhar para a área indicada no guia e não improvisar.
4. Nunca expor dado de colaborador nem informação de serviço de clientes do cliente.
5. Indicar para quem encaminhar internamente, quando o guia mandar.

## Entrega
Parecer no formato de `metodo/parecer.md`. Resposta pronta para colar e, quando for o caso, o encaminhamento interno.
Registrar a validação como manda `metodo/parecer.md`: pasta nova em `<workspace>/clientes/<slug>/validacoes/` com `relatorio.html`, `pecas-corrigidas/` (a versão corrigida) e `dados.json`, e atualizar o portal do cliente (função `portal-cliente`).
Fechar com a pergunta de próximo passo.
