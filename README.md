# TruthfulQA PHI‑3.5 Mini Fine‑Tuning with Unsloth

Fine‑tuning Microsoft’s **PHI‑3.5 Mini** language model on the **TruthfulQA** MCQs to curb hallucinations—especially for **multiple‑choice question (MCQ) answering**.

> After fine‑tuning, accuracy jumped from \~zero to **≈ 91 %** and response perplexity fell to **≈ 1.78**.

---

## At a Glance

|                              | Before Fine‑Tuning | After Fine‑Tuning |
| ---------------------------- | ------------------ | ----------------- |
| **Accuracy**                 | 0.00 %                  | **90.85 %**       |
| **Precision**                | 0.00 %                  | **90.90 %**       |
| **Recall**                   | 0.00 %                  | **90.85 %**       |
| **F1‑Score**                 | 0.00 %                  | **90.66 %**       |
| **Avg. Response Perplexity** | 4.03                  | **1.78**          |
| **Avg. Corpus Perplexity**   | 4.68                  | **2.27**          |

*(Evaluated on TruthfulQA MC test split; see the notebook for details.)*

the predictions before finetuning had some correct answers but very little compared to the whole validation data.

---

## 🗂️ Repository Structure

```
truthfulQA_phi/
├── final_phi_unsloth_finetuning.ipynb   <- **Working notebook (run this!)**
├── *.ipynb                              <- Exploratory / hallucinated notebooks (kept for exploring different approaches)
└── README.md                            <- You are here
```

---

## Quick Start (Google Colab)

1. **Open** [`final_phi_unsloth_finetuning.ipynb`](final_phi_unsloth_finetuning.ipynb) in Colab (GPU runtime recommended).
2. **Run all cells**, **skipping** any cell that is commented out.
3. The notebook:

   1. Installs dependencies (Unsloth, Transformers, Bits‑and‑Bytes, etc.).
   2. Downloads & preprocesses **TruthfulQA** into a tabular form with columns:

      ```text
      Type | Category | Question | Best Answer | Options
      ```
   3. Applies prompt template:

      * **Alpaca‑style Prompt (Modified)** – delivers the best results (≈ 91 % accuracy)
   4. Fine‑tunes PHI‑3.5 Mini via **LoRA** using **Unsloth**.
   5. Evaluates & prints metrics shown above.

---

## Environment & Dependencies

* **Python 3.10** (Colab default)
* **unsloth** ≥ 0.3.0
* **transformers** ≥ 4.41.0
* **datasets** ≥ 2.19.0
* **bitsandbytes**, **peft**, **accelerate**, **trl**, **torch** ≥ 2.3.0

> The install cell in the notebook does the required

---

## 🔍 Dataset & Prompts

| Column        | Description                     |
| ------------- | ------------------------------- |
| `Type`        | Question type (e.g., Adversarial, non adversarial) |
| `Category`    | TruthfulQA topic domain (e.g., Misconceptions, Conspiracies)         |
| `Question`    | Natural‑language question       |
| `Best Answer` | Ground‑truth answer text        |
| `Options`     | semi-colon‑separated MC options      |

Two prompt templates are experimented with:

1. **Φ‑3.5 Prompt (Medium)** – vanilla system / user messages (eval loss 0.78)
2. **Modified Alpaca Prompt** – instruction‑style with explicit "<|user|>", "<|end|>", and "<|assistant|>" sections → **highest accuracy**. (eval loss 0.66)

---

## 📈 Results

| Metric                    | Value            |
| ------------------------- | ---------------- |
| Response Perplexity       | **1.779 ± 0.01** |
| Accuracy                  | **90.85 %**      |
| Precision                 | **90.90 %**      |
| Recall                    | **90.85 %**      |
| F1‑Score                  | **90.66 %**      |
| Average Corpus Perplexity | **2.27**         |

*See notebook for full evaluation script and confusion matrix.*

> **Note:** Base PHI‑3.5‑Mini has \~3.8 B parameters; LoRA adds \~1 % trainable params.

---

## 📜 License & Attribution

### Code

Released under the **MIT License** – see [`LICENSE`](LICENSE).

### Model

* **PHI‑3.5 Mini** © Microsoft, licensed under [MIT license](https://github.com/microsoft/phi-3-mini/blob/main/LICENSE) (check upstream for exact terms).
* **Unsloth** © Unsloth authors, Apache‑2.0.

### Dataset

* **TruthfulQA** © OpenAI, released under a CC BY 4.0 license.

> Respect each upstream license when distributing checkpoints.

---

## Preprint

A detailed write‑up is available:

* **arXiv:** [https://arxiv.org/abs/2501.01588](https://arxiv.org/abs/2501.01588)
* **Qeios:** [https://www.qeios.com/read/Z95X8O](https://www.qeios.com/read/Z95X8O)

*(Draft in progress; links will be updated when the final version is published.)*

---

## Acknowledgements

* Microsoft & the PHI team for open‑sourcing PHI‑3.5 Mini.
* The **Unsloth** developers for streamlined fine‑tuning.
* The creators of **TruthfulQA** for the benchmark.
* Google Colab for free GPU resources.

---

## Citation

If you use this work, please cite the preprint (see above) **and** the original TruthfulQA & PHI papers.

```
@misc{truthfulqa_phi,
  title        = {(WHY-PHI) Fine-Tuning PHI-3 for Multiple-Choice Question Answering: Methodology, Results, and Challenges},
  author       = {Hisham, Mohamed},
  howpublished = {GitHub},
  year         = {2025},
  note         = {\url{https://github.com/MohamedHisham20/truthfulQA_phi}}
}
```

---

## Contributing

Issues and pull requests are welcome! Please open an issue to discuss major changes first.

---

## Contact

Mohamed Hisham • [mohamed.hisham.abdellatif03@gmail.com](mailto:mohamed.hisham.abdellatif03@gmail.com)
