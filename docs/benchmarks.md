# Evaluation notes

[Project overview](../README.md) | [简体中文](benchmarks.zh-CN.md)

Snapshot: October 14, 2026. These results are reported by the Themis project from completed runs and saved public baseline snapshots.

Comparison positions are limited to the benchmark versions and reference models shown: 12 selected models for Heaven, 11 public fixture models plus Themis for Decision Index 0.3, and 21 saved reference models plus Themis for QUB. Themis results come from local evaluations and have not been registered as official leaderboard entries. Overlap with public evaluation data is recorded in prior training and experiments. Values are displayed to two decimal places; rankings and differences use the underlying unrounded scores.

![Themis benchmark scores and comparison positions](../assets/benchmarks/00-benchmark-overview.png)

## 2. Public evaluation results

| Evaluation | Themis INT8 | Coverage and measurement |
| --- | ---: | --- |
| **Heaven** | **93.07%** | 215 correct answers on the same set of 231 public questions; all requests valid. |
| **Decision Index 0.3** | **70.46** | Public, baseline-corrected index; raw index 77.53; 37 question sets across 5 domains, with 140,178 valid requests. |
| **QUB / jevbench-240** | **82.15 / 100** | Full-suite consistency score; 240 cases, 50 relational checks, and 14,838 outcomes. |

Heaven measures correctness on public tasks. Decision Index uses random-baseline correction and domain weighting. QUB measures consistency across probabilities and related decisions. The comparisons below retain each benchmark's native measurement conventions.

### 2.1 Heaven: the same 231 public questions

![Heaven ranking of 12 selected models on the same 231 tasks](../assets/benchmarks/01-heaven.png)

| Position | Model / mode | Correct | Accuracy |
| ---: | --- | ---: | ---: |
| 1 | **Themis 26B-A4B V1 INT8** | 215 / 231 | **93.07%** |
| 2 | OpenJev (thinking · BF16) | 205 / 231 | 88.74% |
| 3 | djev (thinking) | 202 / 231 | 87.45% |
| 4 | reflex-27b (Qwen3.8-27B) | 201 / 231 | 87.01% |
| 5 | Jev 1.13.0 (TypeSafe AI) | 200 / 231 | 86.58% |
| 5 | SimpleJev (Qwen3.8-27B) | 200 / 231 | 86.58% |
| 7 | LitJev (Qwen3.8-27B) | 199 / 231 | 86.15% |
| 8 | Winnow-12B (Q8) | 198 / 231 | 85.71% |
| 9 | openjev-sglang (Qwen3.6-35B-A3B · SGLang) | 197 / 231 | 85.28% |
| 9 | classifier.dev (fast tier) | 197 / 231 | 85.28% |
| 11 | djev (diffusion-gemma) | 194 / 231 | 83.98% |
| 12 | decider-35b-a3b (Mapika) | 192 / 231 | 83.12% |

On this comparison using identical questions, Themis INT8 answers **15 more questions** correctly than Jev 1.13.0, an advantage of **6.49 percentage points**. It exceeds OpenJev thinking by **4.33 percentage points**. The comparison uses the saved 231-question public snapshot and retains each model's execution mode.

Themis INT8's Heaven macro accuracy is **92.00%**, ECE is **0.02816**, mean Brier score is **0.10814**, and paraphrase consistency is **35 / 36 (97.22%)**.

### 2.2 Decision Index 0.3: public index

![Decision Index 0.3 public-index ranking of 12 compared models](../assets/benchmarks/02-decision-index-0.3.png)

| Position | Model / mode | Public index | Themis INT8 minus baseline |
| ---: | --- | ---: | ---: |
| 1 | **Themis 26B-A4B V1 INT8** | **70.46** | — |
| 2 | Torchcast Decision 27B | 65.10 | +5.36 |
| 3 | Perplexity Decider v1.1 (27B) | 62.25 | +8.21 |
| 4 | Cloudflare clef | 61.71 | +8.75 |
| 5 | Quyet-1.0-Large | 60.79 | +9.67 |
| 6 | Fastino GLiDE (no-thinking · 28B) | 59.06 | +11.40 |
| 7 | Jev | 57.96 | +12.50 |
| 8 | Kev 27B | 56.69 | +13.77 |
| 9 | JPT-9B | 46.96 | +23.50 |
| 10 | JPT-0.8B | 19.37 | +51.09 |
| 11 | Lavoir | 8.85 | +61.61 |
| 12 | Verdict | 1.86 | +68.60 |

Themis INT8's public index exceeds Jev by **12.50 points** and Torchcast Decision 27B by **5.36 points**. This table covers the public portion of Decision Index 0.3. The leaderboard's Full score also includes private evaluations held by its maintainers.

![Themis and Jev compared across five Decision Index domains](../assets/benchmarks/04-decision-index-domains.png)

| Domain | Themis INT8 | Jev | Difference |
| --- | ---: | ---: | ---: |
| Knowledge and reasoning | 64.04 | 53.87 | +10.17 |
| Language understanding | 69.38 | 59.23 | +10.15 |
| Retrieval and classification | 70.71 | 55.42 | +15.29 |
| Tools and automation | **85.86** | 75.09 | +10.77 |
| Arts and human preferences | 61.18 | 39.08 | +22.10 |

Coverage is 100% in all five domains. Jev's domain scores were recalculated from the corresponding public component scores using the native weights. Themis INT8 scores higher in all five domains in this comparison.

### 2.3 QUB: the full jevbench-240 suite

![QUB full-suite ranking of 22 compared models](../assets/benchmarks/03-qub-full.png)

| Position | Model / mode | Full-suite score / 100 | Themis INT8 minus baseline |
| ---: | --- | ---: | ---: |
| 1 | Open-Jev-9B | 83.90 | -1.75 |
| 2 | **Themis 26B-A4B V1 INT8** | **82.15** | — |
| 3 | JevAny-Gemma-4B (pointer) | 79.03 | +3.12 |
| 4 | JevAny-Qwen-4B (direct token) | 78.60 | +3.55 |
| 5 | JevAny-Qwen-4B (pointer) | 78.27 | +3.88 |
| 6 | decider-4b v2.1 | 77.27 | +4.88 |
| 7 | Jebadiah 9B v2 | 76.56 | +5.59 |
| 8 | Von 1.3 | 75.21 | +6.94 |
| 9 | TinyJev-4B | 75.18 | +6.97 |
| 10 | OneJev-4B | 72.91 | +9.24 |
| 11 | RSI-Jev v3.0 2B | 72.10 | +10.05 |
| 12 | JevK5 v0.3 | 72.05 | +10.10 |
| 13 | decider-2b v10 | 71.32 | +10.84 |
| 14 | Kev-4B | 71.20 | +10.95 |
| 15 | jevhome-E | 68.98 | +13.17 |
| 16 | Bespoke-Nimble-9B | 67.87 | +14.28 |
| 17 | CLM v0.1 | 66.53 | +15.63 |
| 18 | jevhome-ettin-1b | 64.79 | +17.36 |
| 19 | Laya (typed-decisions) | 63.10 | +19.05 |
| 20 | OpenThai-SystemOne | 62.11 | +20.04 |
| 21 | Verdict 1.4 | 59.69 | +22.47 |
| 22 | Laya (english) | 57.64 | +24.52 |

The comparison uses saved full-suite results. Open-Jev-9B scores **1.75 points** above Themis INT8; Themis INT8 scores above the remaining models in the table. This result has not been registered as an official leaderboard submission. A corresponding TypeSafe Jev 1.13.0 result is unavailable under this measurement convention.

| QUB dimension | Meaning | Themis INT8 / 100 |
| --- | --- | ---: |
| REP | Consistency under changes in representation | 87.61 |
| BAT | Batching and question isolation | 97.33 |
| MEA | Probability-measure consistency | 58.97 |
| LOG | Consistency with logical constraints | 94.63 |
| CHO | Choice consistency | 72.22 |

The QUB overall score has a **95% bootstrap interval of 81.22–83.04**. The complete run made 10,320 actual calls and returned an empty error list.

### 2.4 Supplementary workflow evaluations

The following results use WorkflowEvals consensus labels and each workflow's native metrics.

| Workflow / metric | Themis INT8 | Jev | Difference |
| --- | ---: | ---: | ---: |
| Invoice processing / exact_actions | 58.67% | 61.78% | -3.11 percentage points |
| Invoice processing / primary_action | 82.00% | 83.11% | -1.11 percentage points |
| Customer service / exact_actions | 73.53% | 75.98% | -2.45 percentage points |
| Security incidents / exact_actions | 55.83% | 61.67% | -5.83 percentage points |
| Agent trajectory observation / primary_action | 63.06% | 71.62% | -8.56 percentage points |

All 705 cases across the four workflows completed execution. Action-matching quality is reported in the table. Jev baselines come from the corresponding public records; Themis INT8 scores lower on these workflow metrics.
