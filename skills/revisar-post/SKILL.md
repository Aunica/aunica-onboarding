---
name: revisar-post
description: Revisa post de rede social (legenda, arte e carrossel) de um cliente contra as diretrizes dele e devolve veredito, correções e a legenda pronta. Use quando pedirem para revisar, validar ou checar um post, legenda, carrossel, stories ou publicação de LinkedIn, Instagram ou Facebook da marca.
---

# Revisar post de rede social

Antes de tudo, ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md`, `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md` e, para arquivos, `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Seguir os passos de interação: cliente, como a peça chega, contexto. Depois carregar `<workspace>/clientes/<slug>/cliente.json` e `diretrizes/regras.md` (workspace: ver `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`).

## Contexto específico desta função
Perguntar, se não estiver claro:
- Rede e formato: LinkedIn da marca, Instagram feed, carrossel, stories, Facebook.
- Só legenda, só arte, ou os dois.

## Blocos de regra que se aplicam
TXT, POST, CTA, SOL, CAS, SEN; com arte também MAR, IMG, SEL; carrossel também POST-04, POST-05, CTA-04.

## O que checar, nesta ordem
1. Estrutura: no máximo 3 parágrafos (impacto, contexto, CTA).
2. Hashtag institucional certa para o tema e assinatura padrão no fim.
3. CTA permitido para o canal; carrossel com 1 CTA na última imagem.
4. Expressões proibidas, primeira pessoa, frases que começam com "Nos", frase de soma quebrada.
5. Soluções: escrita e ordem; SmartForecast com IA.
6. Cliente novo, case ou prêmio: autorização e agradecimentos.
7. Arte: logo ou balão conforme o tipo de conteúdo, cores, margem de 80px, selo GPTW só onde cabe e do ano vigente, foto permitida.
8. Horário sugerido de publicação quando a pessoa informar.

## Entrega
Parecer no formato de `metodo/parecer.md`. Legenda corrigida pronta para colar, com assinatura e hashtags. Para a arte, lista de ajustes para o designer.
Registrar a validação como manda `metodo/parecer.md`: pasta nova em `<workspace>/clientes/<slug>/validacoes/` com `relatorio.html`, `pecas-corrigidas/` (a versão corrigida) e `dados.json`, e atualizar o portal do cliente (função `portal-cliente`).
Fechar com a pergunta de próximo passo.
