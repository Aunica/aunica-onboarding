---
name: cliente-novo
description: Cadastra um cliente novo (ou atualiza um existente) a partir da pasta de referência que o cliente mandou (Google Drive, OneDrive, SharePoint) e registra onde ficam as peças que o time vai validar. Use quando entrar cliente novo, quando o cliente mandar ou atualizar material de marca, ou quando mudar a pasta onde o time guarda as peças do cliente.
---

# Cadastrar ou atualizar cliente

## 1. Conversa inicial (AskUserQuestion e campo livre)
- Nome do cliente e slug (minúsculo, sem acento).
- Link da pasta de referência (manual de marca, guias, logos).
- Pastas onde o time guarda as peças desse cliente para validar (SharePoint, OneDrive, Drive), com o tipo de peça de cada uma.
- Outras marcas na pasta entram no escopo? Quem aprova no cliente e qual o contato de marketing.

## 2. Criar a pasta do cliente no workspace
Copiar `${CLAUDE_PLUGIN_ROOT}/modelo-cliente/` para `<workspace>/clientes/<slug>/` e criar `revisoes/`, `auditorias/`, `reports/`, `historico/log.md`. Preencher `cliente.json` com `referencias` e `pecas_para_validar`.

## 3. Mapear e ler a referência
Seguir `${CLAUDE_PLUGIN_ROOT}/metodo/leitura-de-pecas.md`. Separar regra (manual, guias, políticas, SAC, personas) de ativo (logos, fotos, vídeos, mascote, templates). Mostrar o mapa ao usuário antes de ler tudo. Em PDF com exemplo visual, abrir a página e olhar.

## 4. Escrever as diretrizes
Em `<workspace>/clientes/<slug>/diretrizes/`:
- `regras.md`: tabelas por bloco (TXT, POST, CTA, SOL, MAR, IMG, SEL, VID, CAS, PRE, SEN), linhas `| ID | BLOQUEIA/AJUSTAR/CONFIRMAR | regra curta e verificável |`. Boa prática fora do material vira "(recomendação aunica)". Manter o formato: o portal lê as tabelas.
- `personas.md` e `fontes.md` (documento, onde está, o que alimenta, lacunas para perguntar ao cliente).

## 5. Fechar
- Gerar o portal (`portal-cliente`) e registrar no `historico/log.md`.
- Entregar o resumo pode e não pode e as lacunas para levar ao cliente.
- Nada de dados de cliente dentro do plugin nem no GitHub.
- Sem travessão e sem emoji.
