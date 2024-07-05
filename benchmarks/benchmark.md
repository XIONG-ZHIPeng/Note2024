TheoremQA, CSQA, TruthfulQA


|Datasets| SOTA Model| Link| SOTA Scores | Challenging|
|--------|-----| ----|----------  | --- |
|Strongly Generalizable Question Answering(GrailQA)| Bert & T5 | [GrailQA](https://dki-lab.github.io/GrailQA/) [SOTA paper](https://aclanthology.org/2023.acl-long.270/)| Leaderboard: Overall(EM:73.418, F1:81.869), Compositional Generalization(EM:74.806, F1:82.293), Zero-shot Generalization(EM:71.575, F1:78.536)| The dataset is a KBQA dataset with 64,331 questions annotated with both answers and corresponding logical forms in different syntax (i.e., SPARQL, S-expression, etc.). This places requirements on the model's understanding ability.|

![Example](./GrailQA/example.png)


--------------------------------------------------
|Datasets| SOTA Model| Link| SOTA Scores | Challenging|
|--------|---------| ----|----------  | --- |
|HotpotQA|Beam Retrieval&DeBERTa&gpt3.5|[HotpotQA](https://hotpotqa.github.io/) [SOTA paper](https://arxiv.org/abs/2308.08973) | Leaderboard: Ans(EM:72.69, F1:85.04), Sup(EM:66.25, F1:90.09), Joint(EM:50.53, F1:77.54)|The SOTA hits 90+ Sup-F1 Score, they can find pretty precisely supporting facts using Beam retrieval. However, what they find just is the long passage, and they score 85 on the Ans-F1 using Deberta, gpt3.5 and longchat from openai|

![Example](./hotpot/Types.png)