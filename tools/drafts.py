#!/usr/bin/env python3
"""Keyless drafting helper for the author-agent-skills-pack.

Calls any OpenAI-compatible endpoint (Ollama's REST API, LM Studio,
llama.cpp server, vLLM, and hosted equivalents). Designed local-first:

* the default base URL is a local Ollama server (http://127.0.0.1:11434/v1)
* no API key is required or stored; the api_key config field stays empty
  unless a server specifically needs a bearer token (that would be a token
  the author keeps in a file outside this repo, or a dummy like "ollama")
* standard-library only: no third-party packages

Usage
    python3 tools/drafts.py init
    python3 tools/drafts.py models
    python3 tools/drafts.py draft --dry-run --system "plain, warm" "Hi"
    python3 tools/drafts.py draft --prompt-file notes.md --stream
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.error
import urllib.request
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent
DEFAULT_CONFIG = ROOT / "drafting-config.json"
VERSION = "1.0.0"

DEFAULT_CONFIG_TEXT = json.dumps(
    {
        "base_url": "http://127.0.0.1:11434/v1",
        "model": "llama3.1",
        "timeout_seconds": 120,
        "api_key": "",
    },
    indent=2,
) + "\n"


def load_config(path: pathlib.Path) -> dict[str, Any]:
    if not path.is_file():
        sys.exit(
            f"Config file not found: {path}\n"
            f"Run `python3 {pathlib.Path(__file__).name} init --config {path}` "
            f"first, or use --show-config."
        )
    cfg = json.loads(path.read_text(encoding="utf-8"))
    missing = {"base_url", "model"} - cfg.keys()
    if missing:
        sys.exit(
            f"Missing required field(s) in {path}: {', '.join(sorted(missing))}\n"
            f"Run `init` to write the default config."
        )
    return cfg


def auth_header(cfg: dict[str, Any]) -> dict[str, str]:
    """Header for OpenAI-compatible endpoints. Ollama ignores auth, but some
    clients require a bearer string; use the config value if present, else
    the conventional dummy. Never secret material in this repo."""
    return {"Authorization": "Bearer " + (cfg.get("api_key") or "ollama")}


def post_json(cfg: dict[str, Any], endpoint: str, payload: dict) -> dict:
    base = cfg["base_url"].rstrip("/") + endpoint
    req = urllib.request.Request(
        base,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **auth_header(cfg)},
        method="POST",
    )
    timeout = int(cfg.get("timeout_seconds") or 120)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        detail = err.read()[:300].decode("utf-8", "replace")
        sys.exit(f"HTTP {err.code} from {base}: {detail}")
    except urllib.error.URLError as err:
        sys.exit(
            f"Could not reach {base} ({err.reason}).\n"
            f"Start your local server first, e.g. `ollama serve`. "
            f"Or use --dry-run to preview the payload without a server."
        )
    return json.loads(body)


def stream_completion(cfg: dict[str, Any], payload: dict) -> str:
    """Stream a chat completion, printing tokens as they arrive."""
    base = cfg["base_url"].rstrip("/") + "/chat/completions"
    req = urllib.request.Request(
        base,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **auth_header(cfg)},
        method="POST",
    )
    timeout = int(cfg.get("timeout_seconds") or 120)
    pieces: list[str] = []
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            for raw in resp:
                line = raw.decode("utf-8", "replace").strip()
                if not line.startswith("data:"):
                    continue
                chunk = line[len("data:"):].strip()
                if chunk == "[DONE]":
                    break
                try:
                    piece = json.loads(chunk)["choices"][0]["delta"].get("content") or ""
                except (KeyError, ValueError, IndexError):
                    piece = ""
                pieces.append(piece)
                print(piece, end="", flush=True)
    except urllib.error.HTTPError as err:
        detail = err.read()[:300].decode("utf-8", "replace")
        sys.exit(f"HTTP {err.code} from {base}: {detail}")
    except urllib.error.URLError as err:
        sys.exit(f"Could not reach {base} ({err.reason}). See --dry-run.")
    print()
    return "".join(pieces)


def cmd_models(args: argparse.Namespace, cfg: dict[str, Any]) -> None:
    base = cfg["base_url"].rstrip("/") + "/models"
    req = urllib.request.Request(base, headers=auth_header(cfg))
    try:
        with urllib.request.urlopen(req, timeout=int(cfg.get("timeout_seconds") or 120)) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as err:
        sys.exit(f"Could not reach {base} ({err.reason}). Is your server running?")
    for item in data.get("data", []):
        print(item.get("id", "<unknown>"))


def cmd_draft(args: argparse.Namespace, cfg: dict[str, Any]) -> None:
    prompt = args.prompt_file.read_text(encoding="utf-8") if args.prompt_file else args.prompt
    if not prompt:
        sys.exit("Give a prompt on the command line or via --prompt-file <file>.")
    messages: list[dict[str, str]] = []
    if args.system:
        messages.append({"role": "system", "content": args.system})
    messages.append({"role": "user", "content": prompt})
    payload: dict[str, Any] = {"model": cfg["model"], "messages": messages, "stream": bool(args.stream)}

    if args.dry_run:
        print(f"DRY-RUN — nothing was sent to {cfg['base_url']}. Payload:")
        print(json.dumps(payload, indent=2))
        return

    if args.stream:
        stream_completion(cfg, payload)
        return
    result = post_json(cfg, "/chat/completions", payload)
    try:
        print(result["choices"][0]["message"]["content"])
    except (KeyError, IndexError, TypeError) as err:
        sys.exit(f"Unexpected response shape from server ({err}):\n{json.dumps(result)[:500]}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Draft with a local/OpenAI-compatible model. No API keys required.",
        epilog="Default config: tools/drafting-config.json (points at Ollama). "
        "Nothing is sent anywhere unless you run a non-dry-run draft command.",
    )
    parser.add_argument("--version", action="store_true", help="print version and exit")
    parser.add_argument("--show-config", action="store_true", help="print the expected config shape and exit")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="config JSON path")

    sub = parser.add_subparsers(dest="cmd", required=False)

    p_init = sub.add_parser("init", help="write a default (Ollama) config file")
    p_init.add_argument("--config", default=str(DEFAULT_CONFIG))
    p_init.set_defaults(func=None)

    sub.add_parser("models", help="list model IDs offered by the server")

    p_draft = sub.add_parser("draft", help="draft text")
    p_draft.add_argument("prompt", nargs="?", default=None)
    p_draft.add_argument("--prompt-file", type=pathlib.Path, default=None)
    p_draft.add_argument("--system", default=None, help="style guidance, e.g. 'plain, warm, beginner-safe'")
    p_draft.add_argument("--stream", action="store_true")
    p_draft.add_argument("--dry-run", action="store_true", help="print the payload without sending anything")

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.version:
        print(f"drafts.py {VERSION} (author-agent-skills-pack)")
        return
    if args.show_config:
        print(DEFAULT_CONFIG_TEXT, end="")
        return
    if args.cmd is None:
        parser.print_help()
        return
    if args.cmd == "init":
        path = pathlib.Path(args.config)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(DEFAULT_CONFIG_TEXT, encoding="utf-8")
        print(f"wrote {path}")
        return

    cfg = load_config(pathlib.Path(args.config))
    if args.cmd == "models":
        cmd_models(args, cfg)
    elif args.cmd == "draft":
        cmd_draft(args, cfg)


if __name__ == "__main__":
    main()
