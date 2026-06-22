# Model Comparison Report

Comparing Model A (**models/gcn_best.pt**) vs Model B (**models/gcn_all_time_best_v12.pt**).

## Overall Metrics Comparison

| Metric | Model A | Model B | Delta (B - A) | Status |
|---|---:|---:|---:|---|
| 3-of-4 near-miss candidates in top-20 | 796.0000 | 943.0000 | +147.0000 | 🟢 Improved |
| Any top-5 partition solves all 4 groups | 4.6000 | 19.3000 | +14.7000 | 🟢 Improved |
| Avg best correct groups across top partitions | 0.8300 | 1.6000 | +0.7700 | 🟢 Improved |
| Avg correct groups in top partition | 0.5600 | 1.1100 | +0.5500 | 🟢 Improved |
| Mean rank of true groups found in top-20 | 5.8400 | 5.2400 | -0.6000 | 🟢 Improved |
| Median rank of true groups found in top-20 | 4.0000 | 3.0000 | -1.0000 | 🟢 Improved |
| Overall GCN Candidate MRR | 0.1476 | 0.1678 | +0.0202 | 🟢 Improved |
| Overall Group Relation Accuracy | 40.1000 | 25.3000 | -14.8000 | 🔴 Regressed |
| Overall Pairwise Relation Accuracy | 77.4000 | 79.7000 | +2.3000 | 🟢 Improved |
| Puzzles with all true groups in top-20 | 5.5000 | 22.9000 | +17.4000 | 🟢 Improved |
| Puzzles with any true group in top-20 | 67.0000 | 80.7000 | +13.7000 | 🟢 Improved |
| Puzzles with complete partition candidates | 88.1000 | 96.3000 | +8.2000 | 🟢 Improved |
| Top partition solves all 4 groups | 3.7000 | 9.2000 | +5.5000 | 🟢 Improved |
| True groups in top-20 candidates | 28.7000 | 46.3000 | +17.6000 | 🟢 Improved |
| Validation puzzles | 109.0000 | 109.0000 | 0 | No Change |

## Archetype Metrics Comparison

| Archetype | Metric | Model A | Model B | Delta (B - A) | Status |
|---|---|---:|---:|---:|---|
| COMMON_PHRASE | recall | 0.0000 | 0.0000 | 0 | No Change |
| COMMON_PHRASE | exact_mrr | 0.0034 | 0.0172 | +0.0138 | 🟢 Improved |
| COMMON_PHRASE | pairwise_acc | 0.0000 | 0.0000 | 0 | No Change |
| COMMON_PHRASE | group_acc | 0.0000 | 0.0000 | 0 | No Change |
| COMMON_PHRASE | avg_best_rank | 0.0000 | 0.0000 | 0 | No Change |
| FILL_IN_THE_BLANK | recall | 0.0682 | 0.2955 | +0.2273 | 🟢 Improved |
| FILL_IN_THE_BLANK | exact_mrr | 0.0065 | 0.0483 | +0.0417 | 🟢 Improved |
| FILL_IN_THE_BLANK | pairwise_acc | 0.0152 | 0.0909 | +0.0758 | 🟢 Improved |
| FILL_IN_THE_BLANK | group_acc | 0.1591 | 0.7955 | +0.6364 | 🟢 Improved |
| FILL_IN_THE_BLANK | avg_best_rank | 4.6667 | 7.4615 | +2.7949 | 🔴 Regressed |
| NAMED_ENTITY_SET | recall | 0.1250 | 0.2656 | +0.1406 | 🟢 Improved |
| NAMED_ENTITY_SET | exact_mrr | 0.0771 | 0.0821 | +0.0050 | 🟢 Improved |
| NAMED_ENTITY_SET | pairwise_acc | 0.1198 | 0.0703 | -0.0495 | 🔴 Regressed |
| NAMED_ENTITY_SET | group_acc | 0.3750 | 0.6875 | +0.3125 | 🟢 Improved |
| NAMED_ENTITY_SET | avg_best_rank | 7.1250 | 7.5294 | +0.4044 | 🔴 Regressed |
| NO_RELATION | recall | 0.0000 | 0.0000 | 0 | No Change |
| NO_RELATION | exact_mrr | 0.0000 | 0.0000 | 0 | No Change |
| NO_RELATION | pairwise_acc | 0.9313 | 0.9566 | +0.0253 | 🟢 Improved |
| NO_RELATION | group_acc | 0.3969 | 0.2266 | -0.1703 | 🔴 Regressed |
| NO_RELATION | avg_best_rank | 0.0000 | 0.0000 | 0 | No Change |
| SEMANTIC_SET | recall | 0.3169 | 0.4859 | +0.1690 | 🟢 Improved |
| SEMANTIC_SET | exact_mrr | 0.1490 | 0.1402 | -0.0088 | 🔴 Regressed |
| SEMANTIC_SET | pairwise_acc | 0.1185 | 0.0869 | -0.0317 | 🔴 Regressed |
| SEMANTIC_SET | group_acc | 0.6268 | 0.5915 | -0.0352 | 🔴 Regressed |
| SEMANTIC_SET | avg_best_rank | 6.6000 | 5.7826 | -0.8174 | 🟢 Improved |
| SOUND_OR_SPELLING | recall | 0.1176 | 0.2941 | +0.1765 | 🟢 Improved |
| SOUND_OR_SPELLING | exact_mrr | 0.1196 | 0.1617 | +0.0420 | 🟢 Improved |
| SOUND_OR_SPELLING | pairwise_acc | 0.1471 | 0.3922 | +0.2451 | 🟢 Improved |
| SOUND_OR_SPELLING | group_acc | 0.1765 | 0.6471 | +0.4706 | 🟢 Improved |
| SOUND_OR_SPELLING | avg_best_rank | 4.0000 | 4.2000 | +0.2000 | 🔴 Regressed |
| SYNONYM_OR_NEAR | recall | 0.4961 | 0.6378 | +0.1417 | 🟢 Improved |
| SYNONYM_OR_NEAR | exact_mrr | 0.2783 | 0.2963 | +0.0181 | 🟢 Improved |
| SYNONYM_OR_NEAR | pairwise_acc | 0.2559 | 0.2730 | +0.0171 | 🟢 Improved |
| SYNONYM_OR_NEAR | group_acc | 0.5827 | 0.8425 | +0.2598 | 🟢 Improved |
| SYNONYM_OR_NEAR | avg_best_rank | 5.3333 | 3.6790 | -1.6543 | 🟢 Improved |
| WORDPLAY_TRANSFORM | recall | 0.1379 | 0.4828 | +0.3448 | 🟢 Improved |
| WORDPLAY_TRANSFORM | exact_mrr | 0.0171 | 0.1447 | +0.1276 | 🟢 Improved |
| WORDPLAY_TRANSFORM | pairwise_acc | 0.0287 | 0.1667 | +0.1379 | 🟢 Improved |
| WORDPLAY_TRANSFORM | group_acc | 0.1724 | 0.4483 | +0.2759 | 🟢 Improved |
| WORDPLAY_TRANSFORM | avg_best_rank | 4.5000 | 7.0714 | +2.5714 | 🔴 Regressed |
| WORD_FORM | recall | 0.0000 | 0.3000 | +0.3000 | 🟢 Improved |
| WORD_FORM | exact_mrr | 0.0099 | 0.1242 | +0.1143 | 🟢 Improved |
| WORD_FORM | pairwise_acc | 0.1667 | 0.2000 | +0.0333 | 🟢 Improved |
| WORD_FORM | group_acc | 0.2000 | 0.2000 | 0 | No Change |
| WORD_FORM | avg_best_rank | 0.0000 | 5.3333 | +5.3333 | 🔴 Regressed |
