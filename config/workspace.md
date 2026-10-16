# Onde ficam os dados dos clientes (workspace)

O plugin não guarda dados de cliente. Regras, referências, revisões e auditorias ficam numa pasta da aunica chamada **Onboarding Clientes**, que cada pessoa conecta no Cowork.

## Local atual
- OneDrive da aunica: `Onboarding Clientes` (pasta do Ricardo, compartilhada com o time).
- Recomendado para o time: mover para uma biblioteca do SharePoint (ex.: site Operações) e cada pessoa sincronizar e conectar no Cowork.

## Estrutura esperada
```
Onboarding Clientes/
  clientes/<slug>/
    cliente.json          onde está o material de referência e onde estão as peças a validar
    diretrizes/           regras.md, personas.md, fontes.md, portal-<slug>.html
    validacoes/           uma pasta por validação: "AAAA-MM-DD HHhMM - assunto/" com relatorio.html, pecas-corrigidas/ e dados.json
    criacoes/             peças e briefings criados pelo plugin, um arquivo por pedido
```

## Como o plugin acha a pasta
1. Procurar entre as pastas conectadas uma chamada `Onboarding Clientes` (ou que tenha a subpasta `clientes/`).
2. Se não houver, pedir para a pessoa conectar a pasta no Cowork (botão de adicionar pasta) e parar até ela conectar.
3. Nunca criar dados de cliente fora dessa pasta.
