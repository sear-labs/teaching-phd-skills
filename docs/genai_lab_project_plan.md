# GenAI Lab Curriculum & Research Project

Plan and key lessons from project design discussion.

## The Four-Phase Plan

### Phase 1 — Train a small model from scratch
Students build a SmolLM2-style small language model (50M–150M params, ~500M–1B tokens), using CS336 / HF Smol Course material to teach the mechanics: tokenizer vocabulary-size trade-offs, data-mixture decisions, sequence-length vs. batch-size trade-offs, deduplication and data hygiene.

**Datasets to draw on:**
- Knowledge/general text: FineWeb-Edu or DCLM, Wikipedia, Cosmopedia (synthetic textbooks)
- Math/science: FineMath, InfiMM-WebMath
- Code: Stack-Edu / deduplicated Stack-v2, filtered StackOverflow
- Extra language capability: FineWeb2 (1,000+ languages) or CulturaX (167 languages)
- Instruction-following layer: SmolTalk-style SFT set

**Teaching note:** a toy model at this scale will have real knowledge gaps and will hallucinate. That's expected — worth framing explicitly as a lesson about scale vs. capability, not a defect to chase away with better curation.

### Phase 2 — Compare RAG, fine-tuning, and continual pretraining on the same base model
Build three variants against the same lab-knowledge target so students can compare directly:
1. **RAG** — retrieval at query time, no weight changes, instantly updatable, bounded by retrieval quality.
2. **Fine-tuned RAG** — same retrieval setup, but the model is tuned to use retrieved context better (a behavior/format fix, not a knowledge fix).
3. **Continual pretraining** — further next-token training on lab-specific raw text; bakes knowledge into weights, permanent but stale the moment it stops, real compute cost, risks catastrophic forgetting.

This is the exercise that makes the "continual pretraining is basically RAG" confusion concrete — one keeps information external and swappable, the other bakes it in internally.

### Phase 3 — Tool-use loop
Build the orchestrator/tool pattern and have students *measure* it, not just build it.
- **Default pattern**: one model, deterministic tools (grep/search/calculator), one context window, iterative reason → act → observe loop.
- **Subagent pattern**: a genuinely separate model instance (can be a smaller/cheaper model) spawned for a bounded task, own context window, returns a condensed result to the orchestrating model — the closer match to "tool-purpose model feeding a general model."
- **Cost to measure**: multi-agent/subagent orchestration runs roughly 4–7x the tokens of a single-agent session. Have students quantify accuracy gain against that overhead.
- **Model choice matters**: Qwen3 (including small sizes) currently leads open-weight native tool-calling reliability; Gemma's tool-calling is a prompt-based workaround and measurably weaker. Evaluate with BFCL (Berkeley Function Calling Leaderboard), not general QA accuracy.
- **What trains tool-use competence**: SFT on trajectory data (reasoning → tool call → tool result → next action), not Q&A pairs — a different target than what improves RAG-answer quality.

### Phase 4 — Build the actual lab model
After the training exercise, students move to the real deliverable: the largest open-weight model the lab's hardware can run, continuously tuned for lab-specific tasks.

## Key Lessons Learned

### 1. From-scratch training is a validated teaching approach
SmolLM2, Phi, and similar small models prove the recipe works, and it's what CS336 and HF's Smol Course already teach. Note: CS336's actual assignment structure combines tokenizer + architecture + optimizer into Assignment 1, then Systems (A2), Scaling (A3), Data (A4), Alignment/RL (A5) — worth getting right before it goes into course materials.

### 2. "Open-weight" ≠ "open-data"
- Fully open (data recipe published): SmolLM2, OLMo, Pythia.
- Open-weight only (training data undisclosed or partial): Llama 3/3.2/3.3, Qwen2.5/3, Gemma. Qwen increasingly bootstraps by having earlier specialist models (Qwen2.5-Math, Qwen2.5-Coder) generate synthetic data that gets folded into the next general model.
- The student from-scratch recipe overlaps in *kind*, not in scale, with what the frontier labs use.

### 3. RAG, fine-tuning, and continual pretraining are three different mechanisms

| | Changes weights? | Update speed | Relative cost |
|---|---|---|---|
| RAG | No | Instant | Cheap per query |
| Fine-tuning | Yes (behavior/format) | Slow | Moderate |
| Continual pretraining | Yes (knowledge) | Slow, real compute | Highest, risks forgetting |

### 4. Tools beat RAG for exact/structured lookup — Anthropic's own history, not just intuition
Early Claude Code used vector-embedding RAG and dropped it for agentic grep/glob/file-read search because it "outperformed everything, by a lot" (Boris Cherny, Anthropic). Cursor, Windsurf, Cline, and Sourcegraph converged on the same pattern since. The real skill split is four separable pieces: (1) knowing *when* to call a tool, (2) formulating the right query, (3) executing the call correctly, (4) synthesizing the result. Small models are usually fine at #4 and weak at #1–3.

### 5. Why small models specifically struggle with "when" to call a tool
Research on qwen2.5:3b/7b found the dominant failure mode at small scale is *omission* (~89% of errors at 3B) — the model doesn't recognize a tool call is needed and just answers with a plausible guess. That's a general-judgment gap, not a formatting bug, and general judgment is exactly what's scarcest in a small parameter budget — the same tension as the vocabulary-size-vs-attention-capacity trade-off in small-model design.

### 6. Why tool-calling-first small models aren't the obvious default
- Compounding error: at 95% per-step reliability, a 10-step tool chain completes ~60% of the time; at 90%, ~35%. Small models start with lower per-step reliability, so this hits them hardest.
- Not a new idea (ReAct 2022, Toolformer 2023) — it needed base models with enough judgment, benchmarks (BFCL, 2024) to measure the skill, and stable tool infrastructure (MCP, late 2024) to mature.
- Safe execution environments (sandboxing, permissions, prompt-injection defense) are a separate, slower engineering problem from raw model capability.
- Not every task benefits — over-triggering tool use is its own failure mode alongside under-triggering.

### 7. Subagents vs. plain tool calls
Tools (grep, bash, calculators) are deterministic programs, not other models — the default agent loop is one model calling programs and reasoning about results. Subagents are genuinely separate model instances (can be routed to a cheaper model for bounded work), spawned for isolated tasks, returning a condensed summary — the closer match to a "tool-purpose model feeding a general model" idea, and a real, currently-used pattern (mirrored in Windsurf's SWE-grep and Chroma's Context-1 specialized retrieval models). Not free: roughly 4–7x the token cost of single-agent sessions.

### 8. Job-market reality for curriculum weighting
An analysis of 900+ "AI Engineer" postings found ~90% are about applying/adapting existing models (RAG, fine-tuning, agents, evals) rather than pretraining from scratch. Within the adaptation bucket, fine-tuning specifically is the scarcer, higher-paid skill; RAG alone is now table stakes. Implication: from-scratch training builds intuition, but the employable skill for most students is the adaptation layer — weight the program accordingly.

### 9. Reasons to run your own model beyond privacy/cost
- **Provider dependency risk** — real precedent: Claude Fable/Mythos access was suspended in June 2026 over export-control compliance and restored weeks later, entirely outside any user's control.
- **Reproducibility** — API models drift or get deprecated; a self-hosted checkpoint is frozen, which matters for replicable academic results.
- **Funding-source data-handling requirements** — DOD/DOE/USDA-funded work can carry data residency or processing constraints a third-party API doesn't cleanly satisfy.
- **Deep customization** — architecture changes, custom training objectives, hardware-specific quantization, interpretability work: none possible through an API.
- **The research is the deliverable** — "how to build/optimize a domain-specific small model under real resource constraints" is itself a fundable research question, and the compute/energy cost of local training vs. API inference sits directly in an energy-systems-optimization wheelhouse.
- **No rate limits** for real-time or bulk workloads — relevant if the model ever sits in a live loop against lab equipment or processes large batch jobs.

## Open Questions for the Lab — Recommendations

### Target corpus size for the Phase 2 continual-pretraining comparison?
**Recommendation: ~100–200M tokens, padded with adjacent public literature.** The domain-adaptive pretraining literature puts the floor for a clean CPT signal at roughly 100M tokens — a 7.26M-token domain corpus in one study was explicitly called "well below the recommended threshold," with CPT expected to underperform simple fine-tuning at that scale. A financial-domain study on 1–3B models saw most of the gain within the first 200M tokens, diminishing returns after. The lab's own proprietary documents (papers, proposals, reports) almost certainly don't reach 100M tokens alone — pad with adjacent public critical-minerals/battery/energy-systems literature to get into range. Running lean and proprietary-only is a legitimate alternative, but frame the likely "CPT underperforms RAG at this scale" outcome as the lesson, not a failed experiment.

### Which open-weight model for Phase 4, and does lab hardware support it?
**Recommendation: stay in the Qwen3 family, sized to whatever the confirmed GPU specs support.** UTA HPC cluster and COSMOS Center access are noted, but exact GPU count/VRAM should be confirmed before locking this in — it's the real gating factor. Tiers:
- Single 24GB consumer GPU (RTX 3090/4090): **Qwen3-30B-A3B** — MoE, only ~3B params active per token (fast), but needs all 30B expert weights resident (~17.5GB with QLoRA) — near-32B quality at 3B-active speed. Sweet spot for a typical lab budget.
- 8–16GB GPU: **Qwen3-8B** dense — comfortable ceiling for both inference and fine-tuning.
- Multi-GPU HPC nodes (A100/H100-class, 40–80GB/card): **Qwen3-32B** dense or newer Qwen3.5 line becomes realistic.

Staying in the Qwen3 family across Phases 3–4 means the tool-calling work from Phase 3 transfers directly rather than needing re-validation on a different model's tool-calling quirks.

### Repurpose a tool-calling specialist or custom-train for Phase 3?
**Recommendation: repurpose, then light LoRA fine-tune on the lab's own tool schema — don't custom-train from zero.** Tool-calling competence is a mature, well-benchmarked skill (BFCL); the specialists (xLAM-2-1B, Granite 4.1 3B, Qwen3.5-4B) already do it well, so rebuilding that trajectory-SFT pipeline from scratch spends time better used on the domain-adaptation work in Phases 1–2. Good fine-tuning target: wrap the lab's actual computational tools — PROMMIS, IDAES/Pyomo, GREET, the NREL Materials Flow tool — as callable functions and fine-tune the specialist on that schema, tying Phase 3 directly to the lab's DOE-funded work instead of a generic toy tool set.
