---
name: revisar-video
description: Revisa vídeo, Reels ou GIF de um cliente (capa, trilha, fechamento, marca, texto e fala) contra as diretrizes dele. Use quando pedirem para revisar, validar ou checar vídeo, reels, shorts, motion, GIF ou animação.
---

# Revisar vídeo e Reels

Antes de tudo, ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md`, `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md` e, para arquivos, `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Seguir os passos de interação: cliente, como a peça chega, contexto. Depois carregar `<workspace>/clientes/<slug>/cliente.json` e `diretrizes/regras.md` (workspace: ver `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`).

## Contexto específico desta função
Perguntar, se não estiver claro:
- Tipo: humanizado (pessoas reais) ou animado.
- Canal e duração.

## Blocos de regra que se aplicam
VID, MAR, IMG, SEL, TXT (legenda e fala), SEN.

## O que checar, nesta ordem
1. Capa: humanizado com a pessoa sorrindo; animado com capa criada.
2. Trilha presente, sem vocal, sem ritmo lento ou acelerado demais.
3. Fechamento com a marca em destaque no centro.
4. Quadros: logo, cores, fotos e selos como em arte.
5. Texto na tela e fala com as regras de escrita.
6. Legenda do post com a função revisar-post.

## Entrega
Parecer no formato de `metodo/parecer.md`. Achados com minuto e segundo, e lista de ajustes para a edição.
Registrar a validação como manda `metodo/parecer.md`: pasta nova em `<workspace>/clientes/<slug>/validacoes/` com `relatorio.html`, `pecas-corrigidas/` (a versão corrigida) e `dados.json`, e atualizar o portal do cliente (função `portal-cliente`).
Fechar com a pergunta de próximo passo.
