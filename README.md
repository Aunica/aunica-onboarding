# aunica-onboarding

Plugin de Cowork para onboarding de clientes. Uma iniciativa **aunica Labs**.

Transforma o material de referência de um cliente (manual de marca, guias de conteúdo, políticas) em regras checáveis e coloca essas regras na mão do time para criar e revisar cada peça antes de ir para o cliente.

## Instalar no Cowork

1. Em Plugins, adicionar marketplace pelo GitHub: `Aunica/aunica-onboarding`.
2. Instalar o plugin **aunica-onboarding**.
3. Conectar a pasta **Onboarding Clientes** (onde ficam os dados dos clientes). Ver `config/workspace.md`.

Também dá para instalar pelo arquivo `.plugin` gerado a partir deste repositório.

## O plugin não guarda dados de cliente

Este repositório é público e tem só o motor. Regras, referências, revisões e auditorias de cada cliente ficam na pasta **Onboarding Clientes** da aunica:

```
Onboarding Clientes/clientes/<cliente>/
  cliente.json        onde está o material de referência e onde estão as peças a validar
  diretrizes/         regras.md, personas.md, fontes.md e o portal HTML
  revisoes/  auditorias/  reports/  historico/log.md
```

## Funções

| Função | Quando usar |
|---|---|
| onboarding | Porta de entrada: pergunta o cliente e se é para criar ou revisar. |
| briefing-criacao | Criar algo novo (post, e-mail, artigo, roteiro) ou briefing, já dentro das regras. |
| revisar-post | Legenda, arte e carrossel de rede social. |
| revisar-email-marketing | Assunto, pré-header, corpo e CTA de e-mail ou newsletter. |
| revisar-artigo | Blog, matéria, artigo de LinkedIn. |
| revisar-apresentacao | Deck slide a slide. |
| revisar-arte | Peça estática: post, banner, KV, convite. |
| revisar-video | Vídeo, Reels, GIF. |
| revisar-linkedin-executivo | Título, Sobre, capa, foto e posts de executivos do cliente. |
| revisar-resposta-sac | Comentário, direct e menção nas redes do cliente. |
| auditar-pasta | Varre uma pasta inteira e gera relatório por arquivo e slide. |
| consultar-diretrizes | "Posso usar laranja?", resumo pode e não pode. |
| portal-cliente | Gera ou atualiza a página de diretrizes do cliente. |
| cliente-novo | Cadastra ou atualiza um cliente a partir da pasta de referência. |

## Estrutura do repositório

```
.claude-plugin/         plugin.json e marketplace.json
skills/<função>/        uma pasta por função
metodo/                 como conduzir o usuário, formato do parecer, como ler cada arquivo
config/workspace.md     onde o plugin procura os dados dos clientes
modelo-cliente/         modelo de pasta de cliente novo
scripts/                gerador do portal HTML
assets/                 logos da aunica usados no portal
exemplos/               exemplo fictício de auditoria
```

## Formato das regras

Cada regra é uma linha de tabela em `diretrizes/regras.md` do cliente:

```
| TXT-08 | AJUSTAR | Não usar "sua operação". Usar "seu negócio". |
```

Severidade: BLOQUEIA (não pode publicar), AJUSTAR (corrigir antes de aprovar), CONFIRMAR (precisa de ok do cliente).

## Publicar uma versão

Subir a versão em `.claude-plugin/plugin.json`, registrar no `CHANGELOG.md` e fazer o commit.
