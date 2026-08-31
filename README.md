# TensorTonic RAG from scratch

Retrieval-augmented generation built as a small, readable Python system: chunk, embed, retrieve, ground, evaluate.

This is a **learning / interview-prep** repository, not a production search engine. It exists to make the RAG loop inspectable.

```
Documents
  ↓
Chunking
  ↓
Embeddings
  ↓
Retriever (similarity)
  ↓
Prompt + grounding
  ↓
Generator
  ↓
Evaluation (faithfulness / hit rate — only where tests exist)
```

## Status

Experimental prototype. The layout (`src/`, `pyproject.toml`, `requirements.txt`) is in place so the pipeline can be extended without a framework soup.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run whatever entrypoint lives under `src/` after install. If a script is missing, the repo is still a scaffold — that is documented here rather than hidden.

## What this is not

- Not TensorTonic the company, and not a claim of employment
- Not a benchmark winner
- No API keys belong in this repo

## Related

- [TensorTonic-Solutions](https://github.com/ahmaddroobi99/TensorTonic-Solutions)
- [meridian](https://github.com/ahmaddroobi99/meridian)
