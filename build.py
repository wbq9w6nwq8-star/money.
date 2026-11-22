import json
import os

os.makedirs("dist", exist_ok=True)

with open("data/benefits.json", "r", encoding="utf-8") as f:
    benefits = json.load(f)

with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

pages = [
    {
        "filename": "index.html",
        "title": "あなたに合う給付金・減税・お得制度を3秒診断",
        "h1": "あなたに合う給付金・減税・お得制度を3秒診断",
        "desc": "国の給付金・補助金・税制優遇から民間の学割・高還元サービスまで、あなたの属性に合う制度だけを瞬時に抽出します。",
        "initial_state": {"role": "all", "age": "all", "purpose": "all"}
    },
    {
        "filename": "student.html",
        "title": "学生が使える給付金・税制・学割・お得制度まとめ",
        "h1": "学生が使える給付金・税制・お得制度一覧",
        "desc": "学生向け制度、NISA、学割サブスク、高還元クレジットカードなど、在学中に活用したいお得制度を整理。",
        "initial_state": {"role": "student", "age": "all", "purpose": "all"}
    },
    {
        "filename": "employee.html",
        "title": "会社員・公務員が使える補助金・減税・節税制度まとめ",
        "h1": "会社員・公務員が使える補助金・減税制度一覧",
        "desc": "ふるさと納税、教育訓練給付金、NISA、住宅省エネ支援など、給与所得者が確認しておきたい制度を一覧化。",
        "initial_state": {"role": "employee", "age": "all", "purpose": "all"}
    },
    {
        "filename": "freelance.html",
        "title": "フリーランス・個人事業主の補助金・控除まとめ",
        "h1": "フリーランス・個人事業主の補助金・控除一覧",
        "desc": "フリーランス・個人事業主が活用できるリスキリング支援、税制優遇、生活・住宅支援制度を整理。",
        "initial_state": {"role": "freelance", "age": "all", "purpose": "all"}
    }
]

benefits_json_str = json.dumps(benefits, ensure_ascii=False)

for page in pages:
    html = template.replace("{{PAGE_TITLE}}", page["title"])
    html = html.replace("{{H1_TITLE}}", page["h1"])
    html = html.replace("{{PAGE_DESC}}", page["desc"])
    html = html.replace("/*__BENEFITS_JSON__*/ []", benefits_json_str)
    html = html.replace(
        "/*__INITIAL_STATE__*/ { role: 'all', age: 'all', purpose: 'all' }",
        json.dumps(page["initial_state"], ensure_ascii=False)
    )

    out_path = os.path.join("dist", page["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {out_path}")
