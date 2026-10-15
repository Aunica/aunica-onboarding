---
name: auditar-pasta
description: Varre uma pasta de materiais já produzidos para um cliente (SharePoint, OneDrive, Google Drive ou pasta local) e gera relatório por arquivo e slide ou peça com o que está fora das diretrizes, com link para cada arquivo. Use quando pedirem para auditar, varrer, revisar uma pasta inteira, checar o que o time já produziu ou gerar relatório de conformidade.
---

# Auditar pasta de materiais

1. Ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md` e `metodo/leitura-de-pecas.md`. Perguntar o cliente e qual pasta auditar, oferecendo as de `pecas_para_validar` do `cliente.json` (ou um link novo, que depois entra no `cliente.json`).
2. Perguntar com AskUserQuestion:
   - Incluir subpastas? (sim / não)
   - De quem são as peças: marca do cliente, decks da aunica para o cliente, ou misturado.
3. Listar todos os arquivos e mostrar ao usuário quantos são por tipo antes de começar. Ignorar duplicatas em PDF de arquivo que já existe em PPTX.
4. Para cada arquivo, extrair por slide ou página: texto, fontes, tamanhos, cores e quantidade de imagens. Usar a ordem real dos slides.
5. Passada automática (todos os arquivos): expressões proibidas, escrita e ordem de soluções, mascote, hashtags, CTA, temas sensíveis, concorrentes, selo, fontes e cores fora da paleta (só quando a peça é da marca do cliente).
6. Passada de leitura (obrigatória): ler na íntegra os slides com copy proposta (posts prontos, legendas, títulos, Sobre) e com recomendações. Achado bom é recomendação que contradiz o manual do cliente.
7. Classificar cada achado: severidade (BLOQUEIA, AJUSTAR, CONFIRMAR, INFO) e natureza (Copy, Recomendação, Análise, Conteúdo, Arquivo). Concorrente em benchmark interno é INFO, não erro.
8. Gravar o JSON no formato de `${CLAUDE_PLUGIN_ROOT}/exemplos/auditoria-exemplo.json` (`"tipo": "auditoria"`) em `<workspace>/clientes/<slug>/auditorias/AAAA-MM-DD_<assunto>.json`.
9. Atualizar o portal com a função `portal-cliente`.
10. Linha no `historico/log.md`. Responder com: total de arquivos, contagem por severidade, os 3 a 5 achados que mais importam, e link do portal.
