# Formato do parecer e onde guardar

## Veredito
- **BLOQUEADO**: qualquer regra BLOQUEIA violada.
- **APROVADO COM AJUSTES**: só violações AJUSTAR.
- **APROVADO**: nada a corrigir.
Itens CONFIRMAR não mudam o veredito, mas viram pendências com o cliente.

## Estrutura da resposta
1. **Veredito** em uma linha, com a contagem (ex.: "Aprovado com ajustes: 3 ajustes, 1 pendência com o cliente").
2. **O que mudar**, tabela curta:

| Regra | Onde | Problema | Como fica |
|---|---|---|---|

   "Onde" é o trecho exato, o slide, o segundo do vídeo ou a área da arte.
3. **Pendências com o cliente** (autorização de imagem, ok de cliente novo, selo vigente, versão alternativa de logo).
4. **Versão corrigida** pronta para colar, quando a peça for texto. Para visual, lista para o designer em ordem de prioridade.
5. **Não verificado**: o que não deu para checar e por quê.
6. **Sugestões** (opcional e separado): coisas que melhoram a peça mas não estão nas regras.

## Regras de conduta
- Sempre citar o ID da regra.
- Não inventar regra. O que não está no `regras.md` vai em Sugestões.
- Regra marcada "(recomendação aunica)" aparece identificada assim.
- Copy proposta para o cliente publicar segue todas as regras. Análise interna (benchmark, diagnóstico) só recebe nota informativa quando cita algo que não pode ir para publicação.

## Onde guardar (uma pasta por validação)
Tudo vai para `<workspace>/clientes/<slug>/validacoes/` (ver `config/workspace.md`). Sem workspace conectado, entregar no chat e avisar que não ficou registrado.

Cada vez que alguém valida (uma peça ou uma pasta inteira), criar uma pasta nova:

```
validacoes/AAAA-MM-DD HHhMM - <o que foi validado>/
  relatorio.html       o relatório para abrir com duplo clique
  pecas-corrigidas/    textos corrigidos prontos para usar (um .md por peça, ou correcoes.md com antes e depois)
  dados.json           o que o portal lê
```

- Data e hora no fuso de Brasília. Nome curto e claro no assunto: "Post SmartForecast", "Apresentações outubro".
- `dados.json` no formato de `${CLAUDE_PLUGIN_ROOT}/exemplos/validacao-exemplo.json`: `tipo` (revisao ou auditoria), `data`, `hora`, `solicitante`, `titulo`, `pecas_total`, `pecas_aprovadas` (peças sem nenhum BLOQUEIA, AJUSTAR ou CONFIRMAR) e um item em `achados` por linha da tabela.
- Gerar o relatório: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/gerar_portal.py <workspace>/clientes/<slug> --relatorio "<pasta da validação>"`.
- Depois atualizar o portal (função `portal-cliente`): a validação entra na aba Validações e na aba Evolução.
- Nunca sobrescrever uma validação: cada uma tem sua pasta com data e hora.
