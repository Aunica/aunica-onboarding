---
name: consultar-diretrizes
description: Responde o que pode e o que não pode na comunicação de um cliente (tom, CTA, cores, logo, fotos, mascote, selos, vídeo, temas sensíveis) com a regra citada. Use quando perguntarem se pode usar algo, como escreve um nome, qual cor ou fonte usar, ou pedirem o resumo das diretrizes de um cliente.
---

# Consultar diretrizes

1. Workspace e cliente (método de interação, passos 0 e 1) e ler `<workspace>/clientes/<slug>/diretrizes/regras.md`.
2. Pergunta pontual: responder em uma ou duas frases com o ID da regra e a alternativa permitida.
3. Resumo: blocos NÃO PODE, PRECISA DE OK e DEVE TER, no máximo 12 itens cada, priorizando BLOQUEIA. Oferecer o portal do cliente (função `portal-cliente`) para busca com filtros.
4. Se a resposta não estiver nas regras, dizer isso e sugerir confirmar com o contato de marketing do cliente (campo `contato_marketing`). Registrar a dúvida em `fontes.md` como lacuna na próxima atualização.
