---
name: onboarding
description: Porta de entrada do plugin de onboarding de clientes da aunica. Use quando alguém chamar o plugin sem dizer o que quer, perguntar o que dá para fazer, ou não souber qual função usar. Pergunta o cliente, se é para criar algo novo ou revisar algo pronto, e encaminha para a função certa.
---

# Onboarding de clientes: menu

1. Ler `${CLAUDE_PLUGIN_ROOT}/metodo/interacao.md` e fazer os passos 0 e 1 (workspace e cliente).
2. Perguntar "O que você quer fazer?":
   - Criar algo novo (post, e-mail, artigo, roteiro, briefing) → `briefing-criacao`
   - Revisar algo pronto → próxima pergunta
   - Auditar uma pasta de materiais → `auditar-pasta` (oferecer as pastas de `pecas_para_validar`)
   - Outra coisa → consultar regras (`consultar-diretrizes`), abrir portal (`portal-cliente`), cliente novo ou atualizar referências (`cliente-novo`)
3. Revisar: perguntar o tipo
   - Post de rede social → `revisar-post`
   - E-mail marketing → `revisar-email-marketing`
   - Artigo ou blog → `revisar-artigo`
   - Apresentação → `revisar-apresentacao`
   (campo livre: arte → `revisar-arte`; vídeo → `revisar-video`; LinkedIn de executivo → `revisar-linkedin-executivo`; comentário ou direct → `revisar-resposta-sac`)
4. Ler o `SKILL.md` da função escolhida em `${CLAUDE_PLUGIN_ROOT}/skills/<função>/` e seguir sem repetir perguntas já respondidas.
