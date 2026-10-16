---
name: revisar-email-marketing
description: Revisa e-mail marketing ou newsletter de um cliente (assunto, pré-header, corpo, CTA e peças) contra as diretrizes dele. Use quando pedirem para revisar, validar ou checar e-mail marketing, newsletter, disparo, régua ou template de e-mail.
---

# Revisar e-mail marketing

Antes de tudo, ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md`, `${CLAUDE_PLUGIN_ROOT}/metodo/parecer.md` e, para arquivos, `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Seguir os passos de interação: cliente, como a peça chega, contexto. Depois carregar `<workspace>/clientes/<slug>/cliente.json` e `diretrizes/regras.md` (workspace: ver `${CLAUDE_PLUGIN_ROOT}/config/workspace.md`).

## Contexto específico desta função
Perguntar, se não estiver claro:
- Tipo: newsletter, disparo de campanha, convite de evento, comunicado.
- Ferramenta de envio, se souber (ex.: RD Station).

## Blocos de regra que se aplicam
TXT, CTA, SOL, SEN, MAR, IMG, SEL (SEL-06: QR Code só em e-mail), CAS.

## O que checar, nesta ordem
1. Assunto e pré-header: objetivos, sem expressões proibidas, sem promessa que o corpo não cumpre.
2. Corpo: primeira pessoa do plural, frases curtas, "seu negócio" e não "sua operação".
3. CTA: principal para WhatsApp quando for conversão; texto do botão coerente com o destino.
4. Soluções e mascote com a escrita oficial.
5. Peças visuais: logo, cores, foto, selo do ano vigente.
6. Dados citados com fonte.
7. Temas sensíveis fora do conteúdo.

## Entrega
Parecer no formato de `metodo/parecer.md`. Assunto, pré-header e corpo corrigidos prontos para colar, e lista de ajustes visuais.
Registrar a validação como manda `metodo/parecer.md`: pasta nova em `<workspace>/clientes/<slug>/validacoes/` com `relatorio.html`, `pecas-corrigidas/` (a versão corrigida) e `dados.json`, e atualizar o portal do cliente (função `portal-cliente`).
Fechar com a pergunta de próximo passo.
