#!/usr/bin/env python3
"""校验 Claude Code 插件市场结构。

检查项：
1. .claude-plugin/marketplace.json 存在且为合法 JSON，含必填字段。
2. 每个 plugin 条目的 source 目录存在，且含 .claude-plugin/plugin.json（合法 JSON、name 与条目一致）。
3. 每个插件 skills/<name>/SKILL.md 存在，且 frontmatter 含 name + description。

无三方依赖，可本地直接运行：python3 scripts/validate-marketplace.py
任一检查失败则以非 0 退出，便于 CI 阻断。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        err(f"缺少文件：{path.relative_to(ROOT)}")
    except json.JSONDecodeError as e:
        err(f"JSON 不合法：{path.relative_to(ROOT)} — {e}")
    return None


def check_skill_frontmatter(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        err(f"SKILL.md 缺少 YAML frontmatter：{skill_md.relative_to(ROOT)}")
        return
    fm = m.group(1)
    for field in ("name", "description"):
        if not re.search(rf"^{field}\s*:", fm, re.MULTILINE):
            err(f"SKILL.md frontmatter 缺少 {field}：{skill_md.relative_to(ROOT)}")


def main() -> int:
    mkt_path = ROOT / ".claude-plugin" / "marketplace.json"
    mkt = load_json(mkt_path)
    if mkt is None:
        return fail()

    for field in ("name", "description", "owner", "plugins"):
        if field not in mkt:
            err(f"marketplace.json 缺少必填字段：{field}")
    if not isinstance(mkt.get("plugins"), list) or not mkt["plugins"]:
        err("marketplace.json 的 plugins 必须是非空数组")
        return fail()

    for entry in mkt["plugins"]:
        name = entry.get("name", "<未命名>")
        for field in ("name", "description", "source"):
            if field not in entry:
                err(f"插件条目 [{name}] 缺少字段：{field}")
        src = entry.get("source")
        if not isinstance(src, str):
            continue  # 仅支持本仓库相对路径 source 的结构校验
        plugin_dir = (ROOT / src).resolve()
        if not plugin_dir.is_dir():
            err(f"插件 [{name}] 的 source 目录不存在：{src}")
            continue

        pj_path = plugin_dir / ".claude-plugin" / "plugin.json"
        pj = load_json(pj_path)
        if pj is not None:
            if pj.get("name") != entry.get("name"):
                err(f"插件 [{name}] 的 plugin.json name='{pj.get('name')}' 与市场条目 name='{entry.get('name')}' 不一致")

        skills_dir = plugin_dir / "skills"
        skill_mds = list(skills_dir.glob("*/SKILL.md")) if skills_dir.is_dir() else []
        if not skill_mds:
            err(f"插件 [{name}] 未找到任何 skills/<name>/SKILL.md")
        for skill_md in skill_mds:
            check_skill_frontmatter(skill_md)

    return fail()


def fail() -> int:
    if errors:
        print("插件市场校验失败：", file=sys.stderr)
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr)
        return 1
    print("✓ 插件市场结构校验通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
