# Changelog

## 0.4.0 (2026-10-16)
- Uma pasta por validação, com data e hora no nome: relatorio.html, pecas-corrigidas/ e dados.json. Saem auditorias/, revisoes/, reports/ e log.md.
- Nova aba Evolução no portal: achados por validação, conformidade, regras que mais se repetem e lista de todas as validações.
- Relatório individual de cada validação (gerar_portal.py --relatorio).

## 0.3.0 (2026-10-15)
- Repositório público só com o motor: dados de cliente saem do plugin e ficam na pasta Onboarding Clientes (`config/workspace.md`).
- `cliente.json` por cliente com as pastas de referência e as pastas de peças a validar.
- Menu pergunta se é para criar algo novo ou revisar algo pronto.
- Revisões gravadas também em JSON e mostradas no portal junto com as auditorias.
- Portal com a identidade da aunica e assinatura aunica Labs.
- marketplace.json para instalar direto do GitHub.

## 0.2.0 (2026-10-15)
- Funções separadas por tipo de peça, com porta de entrada interativa (onboarding).
- Novas funções: auditar-pasta, portal-cliente, briefing-criacao, revisar-linkedin-executivo, revisar-resposta-sac.
- Método comum em `metodo/` (interação, parecer, leitura de arquivos) e histórico por cliente na pasta do OneDrive.
- Portal HTML de diretrizes com busca e filtros (`scripts/gerar_portal.py`).
- Primeira auditoria de cliente como exemplo.

## 0.1.0 (2026-10-15)
- Primeira versão com validar-peca, diretrizes-cliente e cliente-novo.
