"""RAG from Scratch — TensorTonic project solution.

Six primitives, no LangChain, no vector-DB vendor:

1. chunking   — split documents into retrieval-aware chunks
2. embeddings — represent text as searchable vectors (TF-IDF from scratch)
3. retrieve   — dense / BM25 / hybrid top-k
4. context    — assemble grounded context with citation slots
5. citations  — validate that an answer's citations sit in retrieved evidence
6. evaluate   — recall@k, MRR, nDCG, citation faithfulness
"""

from .types import (
    Document,
    Chunk,
    RetrievedChunk,
    GroundedContext,
    CitationCheck,
    RAGAnswer,
    EvalCase,
    RetrievalMetrics,
)
from .chunking import RecursiveCharacterSplitter, split_documents
from .embeddings import TfidfEmbedder
from .bm25 import BM25Index
from .retrieve import Retriever, HybridRetriever
from .context import build_grounded_context
from .generate import generate_grounded_answer
from .citations import validate_citations
from .evaluate import evaluate_retrieval, evaluate_citations
from .pipeline import RAGPipeline

__all__ = [
    "Document",
    "Chunk",
    "RetrievedChunk",
    "GroundedContext",
    "CitationCheck",
    "RAGAnswer",
    "EvalCase",
    "RetrievalMetrics",
    "RecursiveCharacterSplitter",
    "split_documents",
    "TfidfEmbedder",
    "BM25Index",
    "Retriever",
    "HybridRetriever",
    "build_grounded_context",
    "generate_grounded_answer",
    "validate_citations",
    "evaluate_retrieval",
    "evaluate_citations",
    "RAGPipeline",
]

__version__ = "1.0.0"
