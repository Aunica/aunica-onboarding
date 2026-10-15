---
name: revisar-arte
description: Revisa peça visual estática (arte de post, banner, KV, capa, convite, peça de evento) de um cliente contra as regras de marca dele. Use quando mandarem uma imagem, arte, banner, KV, peça ou layout para checar se está dentro da marca.
---

# Revisar arte e peça visual

Antes de tudo, ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md`, `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md` e, para arquivos, `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Seguir os passos de interação: cliente, como a peça chega, contexto. Depois carregar `<workspace>/clientes/<slug>/cliente.json` e `diretrizes/regras.md` (workspace: ver `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`).

## Contexto específico desta função
Perguntar, se não estiver claro:
- Onde a peça vai rodar (feed, LinkedIn, banner de site, impresso, evento).
- Tipo de conteúdo (institucional, engajamento, evento, prêmio, novo cliente, ação interna, data comemorativa).

## Blocos de regra que se aplicam
MAR, IMG, SEL, SOL, POST-05, e TXT para o texto da arte.

## O que checar, nesta ordem
1. Logo ou balão conforme o tipo de conteúdo, versão oficial, tamanho mínimo, arejamento, sem distorção.
2. Cores dominantes contra a paleta (medir, não estimar).
3. Fonte da marca.
4. Foto: tipo permitido, pessoas olhando para frente, sem estereótipo, autorização quando for colaborador ou diretor.
5. Selo GPTW: só no tipo de conteúdo certo, ano vigente, removido quando há logo de parceiro.
6. Margens de segurança do canal e poluição visual.
7. Texto da arte com as regras de escrita.

## Entrega
Parecer no formato de `metodo/parecer.md`. Lista de ajustes para o designer em ordem de prioridade, com a área da peça em cada item.
Gravar a revisão em `<workspace>/clientes/<slug>/revisoes/` (um .md para ler e um .json para o portal, formato em `metodo/parecer.md`), acrescentar uma linha em `historico/log.md` e atualizar o portal do cliente (função `portal-cliente`).
Fechar com a pergunta de próximo passo.
