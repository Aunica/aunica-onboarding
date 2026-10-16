---
name: revisar-linkedin-executivo
description: Revisa perfil e posts de LinkedIn de executivos de um cliente (título, Sobre, capa, foto e posts) contra as diretrizes da marca. Use quando pedirem para revisar perfil, headline, Sobre, capa, foto ou post de LinkedIn de CEO, diretor ou executivo do cliente.
---

# Revisar LinkedIn de executivo

Antes de tudo, ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md`, `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md` e, para arquivos, `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Seguir os passos de interação: cliente, como a peça chega, contexto. Depois carregar `<workspace>/clientes/<slug>/cliente.json` e `diretrizes/regras.md` (workspace: ver `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`).

## Contexto específico desta função
Perguntar, se não estiver claro:
- Qual executivo e cargo confirmado.
- O que revisar: perfil, posts, ou os dois.

## Blocos de regra que se aplicam
TXT, SOL, SEN, IMG-06, SEL, e POST e CTA quando o post for da marca.

## O que checar, nesta ordem
1. Post de executivo é em primeira pessoa do singular; as regras de escrita e as expressões proibidas valem do mesmo jeito.
2. Hashtag institucional: só exigir se o cliente tiver regra para perfil de executivo; senão, pendência CONFIRMAR.
3. Soluções e números da empresa com a escrita e dados oficiais.
4. Foto e capa: mudança precisa de validação do executivo; CEO passa pelo marketing do cliente.
5. Nenhum concorrente citado, nenhum tema sensível.

## Entrega
Parecer no formato de `metodo/parecer.md`. Título, Sobre e posts corrigidos prontos para colar.
Registrar a validação como manda `metodo/parecer.md`: pasta nova em `<workspace>/clientes/<slug>/validacoes/` com `relatorio.html`, `pecas-corrigidas/` (a versão corrigida) e `dados.json`, e atualizar o portal do cliente (função `portal-cliente`).
Fechar com a pergunta de próximo passo.
