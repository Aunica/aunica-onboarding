#!/usr/bin/env python3
"""Gera o portal de diretrizes de um cliente (HTML de um arquivo só).

Uso:
  python3 gerar_portal.py <pasta_do_cliente> <saida.html> [--standalone]
  python3 gerar_portal.py <pasta_do_cliente> --relatorio "<pasta da validação>"

<pasta_do_cliente> é a pasta do cliente no OneDrive, por exemplo
"Onboarding Clientes/clientes/<cliente>". Ela precisa ter:
  diretrizes/regras.md      (obrigatório)
  diretrizes/personas.md    (opcional)
  validacoes/<AAAA-MM-DD HHhMM - assunto>/dados.json   (uma pasta por validação)

--relatorio gera o relatorio.html dentro da pasta da validação informada.

--standalone gera documento completo (doctype, head, body) para abrir direto
do OneDrive. Sem a flag, gera o corpo pronto para publicar como página.
"""
import base64, datetime, html, json, pathlib, re, sys
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent.parent

TIPOS = {
    "TXT": ["Post", "E-mail", "Artigo", "Apresentação", "SAC"],
    "POST": ["Post"],
    "CTA": ["Post", "E-mail", "Artigo"],
    "SOL": ["Post", "E-mail", "Artigo", "Apresentação", "Arte", "Vídeo"],
    "MAR": ["Arte", "Post", "Vídeo", "Apresentação", "E-mail"],
    "IMG": ["Arte", "Post", "Vídeo", "Apresentação", "E-mail"],
    "SEL": ["Arte", "Post", "Vídeo", "Apresentação"],
    "VID": ["Vídeo"],
    "CAS": ["Post", "Artigo"],
    "PRE": ["Apresentação"],
    "SEN": ["Post", "E-mail", "Artigo", "SAC", "Apresentação"],
}


def frontmatter(txt):
    fm = {}
    m = re.match(r"---\n(.*?)\n---", txt, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    return fm


def regras(txt):
    out, bloco = [], ""
    for line in txt.splitlines():
        h = re.match(r"^##\s+\d+\.\s+(.*)", line)
        if h:
            bloco = h.group(1).strip()
            continue
        r = re.match(r"^\|\s*([A-Z]{2,5}-\d{2})\s*\|\s*(BLOQUEIA|AJUSTAR|CONFIRMAR)\s*\|\s*(.+?)\s*\|\s*$", line)
        if r:
            rid, sev, texto = r.groups()
            out.append({"id": rid, "sev": sev, "bloco": bloco, "texto": texto.replace("**", ""),
                        "tipos": TIPOS.get(rid.split("-")[0], []),
                        "aunica": "(recomendação aunica)" in texto})
    return out


def fluxo(txt):
    m = re.search(r"## 12\. Fluxo de aprovação\n(.*)", txt, re.S)
    return [l[2:].strip() for l in m.group(1).splitlines() if l.startswith("- ")] if m else []


def data_uri(name):
    p = ROOT / "assets" / name
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode() if p.exists() else ""


def carregar_validacoes(cdir, com_link):
    regs = []
    vdir = cdir / "validacoes"
    for f in sorted(vdir.glob("*/dados.json")) if vdir.exists() else []:
        try:
            a = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("ignorado (JSON inválido):", f)
            continue
        a["_pasta"] = f.parent.name
        if com_link:
            a["_link"] = "../validacoes/" + "/".join(quote(p) for p in (f.parent.name, "relatorio.html"))
        regs.append(a)
    regs.sort(key=lambda a: a.get("data", "") + a.get("hora", ""), reverse=True)
    return regs


def montar(cdir, regs, modo, standalone):
    d = cdir / "diretrizes"
    rtxt = (d / "regras.md").read_text(encoding="utf-8")
    fm = frontmatter(rtxt)
    pers = (d / "personas.md").read_text(encoding="utf-8") if (d / "personas.md").exists() else ""
    data = {"cliente": fm.get("cliente", cdir.name), "fm": fm, "regras": regras(rtxt), "fluxo": fluxo(rtxt),
            "personas": pers, "auditorias": regs, "gerado": datetime.date.today().isoformat(), "modo": modo}
    tpl = (ROOT / "scripts" / "portal_template.html").read_text(encoding="utf-8")
    page = (tpl.replace("__CLIENTE__", html.escape(data["cliente"]))
               .replace("__LOGO_LIGHT__", data_uri("aunica-light.png"))
               .replace("__LOGO_DARK__", data_uri("aunica-dark.png"))
               .replace("__LOGO_LABS__", data_uri("aunica-labs.png"))
               .replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    if standalone:
        page = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                + page.replace("<!--BODY-->", "</head><body>") + "</body></html>")
    else:
        page = page.replace("<!--BODY-->", "")
    return page, data


def main():
    args = sys.argv[1:]
    cdir = pathlib.Path(args[0])
    if "--relatorio" in args:
        vpasta = pathlib.Path(args[args.index("--relatorio") + 1])
        a = json.loads((vpasta / "dados.json").read_text(encoding="utf-8"))
        page, data = montar(cdir, [a], "relatorio", True)
        (vpasta / "relatorio.html").write_text(page, encoding="utf-8")
        print(vpasta / "relatorio.html", "|", len(a.get("achados", [])), "achados")
        return
    standalone = "--standalone" in args
    out = pathlib.Path([a for a in args[1:] if not a.startswith("--")][0])
    regs = carregar_validacoes(cdir, standalone)
    page, data = montar(cdir, regs, "portal", standalone)
    out.write_text(page, encoding="utf-8")
    print(f"{out} | {len(data['regras'])} regras | {len(regs)} validações")


if __name__ == "__main__":
    main()
