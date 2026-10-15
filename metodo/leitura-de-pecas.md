# Como ler cada tipo de arquivo

## Texto
Colado no chat: analisar frase a frase. DOCX: extrair com python-docx ou pandoc.

## Imagem (PNG, JPG, PDF de arte)
- Abrir com Read e olhar a peça.
- Cores: extrair as dominantes com Pillow (`img.convert('RGB').quantize(8)`) e comparar com os HEX do `regras.md`. Cor proibida como destaque ou fundo é bloqueio quando o cliente tiver essa regra.
- Checar logo (versão, tamanho, margem), balão, selo e ano, foto (tipo de imagem proibida, pessoas olhando para frente), texto na arte, poluição visual, pixelização.

## Vídeo
- Quadros com ffmpeg: `ffmpeg -i v.mp4 -vf "select='eq(n,0)+not(mod(n,90))'" -vsync vfr q%03d.png` e o último segundo (`-sseof -1`).
- Capa, abertura, fechamento com a marca centralizada.
- Áudio: `ffprobe` para saber se há trilha; se houver fala, transcrever quando houver ferramenta. Trilha com vocal só dá para afirmar ouvindo ou com a informação do usuário; senão, vai em "Não verificado".

## PPTX
- python-pptx para texto por slide, fontes (`run.font.name`), tamanhos e cores.
- Ordem real dos slides vem de `ppt/presentation.xml` (sldIdLst), não do nome do arquivo `slideN.xml`.
- Para ver o layout, converter com LibreOffice (`soffice --headless --convert-to pdf`) e ler as páginas.

## Arquivos no SharePoint / OneDrive
- Conector Microsoft 365: `sharepoint_folder_search` para achar a pasta, `read_resource` para listar e ler (pptx e docx vêm como texto por página, na ordem de exibição).
- Para fontes, cores e tamanhos: abrir a pasta no navegador e, na própria página do SharePoint, baixar o arquivo por `/_api/web/GetFileByServerRelativePath(decodedurl='...')/$value` e descompactar no navegador (DecompressionStream 'deflate-raw'), extraindo `ppt/slides/*.xml`.
- Nunca criar cópia do arquivo do time em outro lugar para analisar.

## Google Drive
- Conector do Drive: `read_file_content` lê PDF, Docs, Slides e Office.
- Pasta compartilhada que o conector não lista: abrir no navegador; o HTML de `/drive/folders/<id>` traz a listagem em `_DRIVE_ivd`.
- Exemplo visual dentro de PDF (usar / não usar): abrir no visualizador do Drive e olhar a página.

## Canva e Figma
Usar os conectores quando ativos (exportar como imagem e seguir "Imagem").
