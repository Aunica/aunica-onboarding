---
name: revisar-artigo
description: Revisa artigo de blog, matéria ou texto longo de um cliente contra as diretrizes de conteúdo dele. Use quando pedirem para revisar, validar ou checar artigo, post de blog, matéria, newsletter longa ou conteúdo para o site.
---

# Revisar artigo e blog

Antes de tudo, ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md`, `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md` e, para arquivos, `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Seguir os passos de interação: cliente, como a peça chega, contexto. Depois carregar `<workspace>/clientes/<slug>/cliente.json` e `diretrizes/regras.md` (workspace: ver `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`).

## Contexto específico desta função
Perguntar, se não estiver claro:
- Onde será publicado: blog do cliente, LinkedIn artigo, portal parceiro.
- Se existe palavra-chave alvo de SEO.

## Blocos de regra que se aplicam
TXT, CTA (CTA-05, CTA-06), SOL, SEN, CAS.

## O que checar, nesta ordem
1. Tom e escrita em todo o texto (primeira pessoa, frases curtas, expressões proibidas).
2. Toda informação de outro veículo com fonte citada.
3. Nenhuma marca de terceiro citada sem autorização.
4. CTA de leitura no post que divulga o artigo; dentro do blog, CTA para WhatsApp.
5. Soluções na escrita e ordem oficiais.
6. SEO: se o cliente não tiver regra escrita, dar só sugestões, sem reprovar.

## Entrega
Parecer no formato de `metodo/parecer.md`. Lista de ajustes por parágrafo e o texto corrigido, quando a pessoa pedir.
Gravar a revisão em `<workspace>/clientes/<slug>/revisoes/` (um .md para ler e um .json para o portal, formato em `metodo/parecer.md`), acrescentar uma linha em `historico/log.md` e atualizar o portal do cliente (função `portal-cliente`).
Fechar com a pergunta de próximo passo.
