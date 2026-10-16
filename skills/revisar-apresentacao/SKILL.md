---
name: revisar-apresentacao
description: Revisa apresentação (PPTX, PDF ou Google Slides) de um cliente slide a slide contra as diretrizes dele. Use quando pedirem para revisar, validar ou checar apresentação, deck, PPT, slides, proposta ou material institucional, seja do cliente ou da aunica para o cliente.
---

# Revisar apresentação

Antes de tudo, ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md`, `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md` e, para arquivos, `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Seguir os passos de interação: cliente, como a peça chega, contexto. Depois carregar `<workspace>/clientes/<slug>/cliente.json` e `diretrizes/regras.md` (workspace: ver `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`).

## Contexto específico desta função
Perguntar, se não estiver claro:
- De quem é o deck: material com a marca do cliente (aplica tudo) ou deck da aunica para o cliente (aplica só o que o deck propõe que o cliente publique ou adote).
- Uso: externo, reunião com o cliente, interno.

## Blocos de regra que se aplicam
PRE, MAR, IMG, SEL, SOL, TXT, SEN.

## O que checar, nesta ordem
1. Ler a ordem real dos slides e extrair texto, fontes, tamanhos e cores por slide.
2. Deck da marca do cliente: layout institucional aprovado, logo, hierarquia de fonte, um só estilo de elemento, ícones, gráficos, fotos, selos, mapa.
3. Deck da aunica para o cliente: checar a copy e as recomendações (o que o cliente vai publicar ou adotar) contra as regras; recomendação que contradiz o manual do cliente é achado.
4. Soluções, mascote e temas sensíveis em qualquer caso.
5. Versões duplicadas na pasta viram nota informativa.

## Entrega
Parecer no formato de `metodo/parecer.md`. Tabela por slide (slide, regra, trecho, problema, como fica).
Registrar a validação como manda `metodo/parecer.md`: pasta nova em `<workspace>/clientes/<slug>/validacoes/` com `relatorio.html`, `pecas-corrigidas/` (a versão corrigida) e `dados.json`, e atualizar o portal do cliente (função `portal-cliente`).
Fechar com a pergunta de próximo passo.
