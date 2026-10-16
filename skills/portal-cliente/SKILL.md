---
name: portal-cliente
description: Gera ou atualiza o portal HTML de diretrizes de um cliente, com logo da aunica, busca, filtros por severidade, tipo de peça e bloco, resumo pode e não pode e todas as validações e a evolução do time. Use quando pedirem a página das diretrizes, o portal do cliente, um link para o time consultar, ou depois de qualquer validação.
---

# Portal do cliente

1. Workspace e cliente (método de interação, passos 0 e 1).
2. Rodar `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/gerar_portal.py <workspace>/clientes/<slug> <workspace>/clientes/<slug>/diretrizes/portal-<slug>.html --standalone`. Esse arquivo abre direto do OneDrive com duplo clique.
3. Rodar de novo sem `--standalone` para uma saída temporária e publicar como página (Artifact). Se já existir página do cliente (link em `diretrizes/link-portal.txt`), atualizar a mesma para não mudar o endereço; senão, publicar e gravar o link nesse arquivo.
4. Lembrar que a página publicada é privada até ser compartilhada com o time.
