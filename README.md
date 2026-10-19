# MERGED AI FREE STACK

The 100% free, open-source (GitHub) equivalent of the viral "6 tools, 1 system, 0 manual work" setup.
Every component is free, self-hosted, and runs on your own Linux machine. No subscriptions.

## The Mapping

| Paid tool in the post | Role | FREE GitHub equivalent | Repo |
|---|---|---|---|
| **Opus 5.5** | The brain — plans every task | **Ollama** (local Llama 3.1 / Qwen / DeepSeek) + **Open WebUI** (GUI) | `ollama/ollama` · `open-webui/open-webui` |
| **Grok Bot** | Scans X 24/7 for trends | **trend_scan.py** (included — Google Trends + Hacker News + Reddit, no login) or **twscrape** for native X scraping | `vladkens/twscrape` |
| **REA** | Researches any topic in ~4 minutes | **GPT Researcher** — autonomous deep-research agent, runs on your local Ollama models | `assafelovic/gpt-researcher` |
| **Jev** | Turns ideas into action automatically | **AutoGPT** — the original autonomous agent platform | `Significant-Gravitas/AutoGPT` |
| **Dots** | Connects everything into one workflow | **n8n** — visual workflow automation, 400+ integrations, self-hosted | `n8n-io/n8n` |
| **Obsidian** | Memory — nothing lost | **Logseq** (open-source notes, local-first) + **mem0** (memory layer for the AI agents, backed by Qdrant) | `logseq/logseq` · `mem0ai/mem0` |

## Install

See the one-block install in this README on the delivered package, or simply:

```bash
docker compose up -d ollama open-webui n8n qdrant
docker exec brain-ollama ollama pull llama3.1:8b
```

Then open http://localhost:3000 (brain GUI) and http://localhost:5678 (n8n workflows — import `n8n/workflows/merged_ai_night_shift.json`).

## Honest notes

- The "$279 before breakfast / 36x return" claim in the original post is marketing — this stack gives you the same *architecture* at $0/month, not guaranteed revenue.
- Native X scraping via twscrape conflicts with X's Terms of Service; the bundled trend_scan.py uses credential-free public sources instead.
