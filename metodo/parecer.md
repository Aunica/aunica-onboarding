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

## Onde guardar (histórico do cliente)
Tudo vai para `<workspace>/clientes/<slug>/` (ver `config/workspace.md`). Sem workspace conectado, entregar no chat e avisar que não ficou no histórico.

- **Revisão**: dois arquivos em `revisoes/` com o mesmo nome `AAAA-MM-DD_<tipo>_<nome-curto>`:
  - `.md` para ler: data, quem pediu, peça (nome e link), veredito, tabela de achados, versão corrigida.
  - `.json` para o portal, no formato de `${CLAUDE_PLUGIN_ROOT}/exemplos/auditoria-exemplo.json` com `"tipo": "revisao"`, `titulo` = nome da peça e um achado por linha da tabela.
- **Auditoria**: `.json` em `auditorias/` no mesmo formato, com `"tipo": "auditoria"`.
- **Histórico**: uma linha em `historico/log.md`: `AAAA-MM-DD | função | peça | veredito | achados (B/A/C/I)`.
- Depois de gravar, atualizar o portal (função `portal-cliente`) para a revisão aparecer na aba Revisões e auditorias.
- Nunca sobrescrever: o nome leva a data.
