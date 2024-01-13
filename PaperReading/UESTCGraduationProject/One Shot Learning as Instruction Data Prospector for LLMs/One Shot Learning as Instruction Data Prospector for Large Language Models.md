# One Shot Learning as Instruction Data Prospector for LLMs

## Abstract
Current instruction tuning practices often rely on expanding dataset size without a clear strategy for ensuring data quality, which can inadvently introduce noise and degrade model performance.

***NUGGETS***, a methodology that employs one shot learning to select high-quality instruction data from expansive datasets.

## Introduction
Instruction tuning
: the process involves supervised fine-tuning on input-ouput pairs.

- Smaller but valuable datasets tend to be more effective in harnessing the capability of LLMs
- Blindly expanding the quantity of instruction data without ensuring quality might introduce noise and lead to hallucination

Use one shot learning to score the influence of a instruction.

Compare the differnce between one shot learning and zero shot learning, and keep the good instruction.