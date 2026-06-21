# Model Comparison Report

Comparing Model A (**gcn_all_time_best**) vs Model B (**gcn_all_time_best_v12**).

## Overall Metrics Comparison

| Metric | Model A | Model B | Delta (B - A) | Status |
|---|---:|---:|---:|---|
| Any top-5 partition solves all 4 groups | 4.6000 | 19.3000 | +14.7000 | 🟢 Improved |
| Avg best correct groups across top partitions | 0.7600 | 1.6000 | +0.8400 | 🟢 Improved |
| Avg correct groups in top partition | 0.5500 | 1.1100 | +0.5600 | 🟢 Improved |
| Mean rank of true groups found in top-20 | 5.6200 | 5.2200 | -0.4000 | 🟢 Improved |
| Median rank of true groups found in top-20 | 3.0000 | 3.0000 | 0 | No Change |
| Overall GCN Candidate MRR | 0.1528 | 0.1678 | +0.0150 | 🟢 Improved |
| Overall Group Relation Accuracy | 18.7000 | 25.4000 | +6.7000 | 🟢 Improved |
| Overall Pairwise Relation Accuracy | 76.1000 | 79.7000 | +3.6000 | 🟢 Improved |
| Puzzles with complete partition candidates | 83.5000 | 96.3000 | +12.8000 | 🟢 Improved |
| Top partition solves all 4 groups | 2.8000 | 9.2000 | +6.4000 | 🟢 Improved |
| True groups in top-20 candidates | 28.2000 | 46.3000 | +18.1000 | 🟢 Improved |
| val_3_of_4_near_miss_candidates_in_top_20 | 815.0000 | 942.0000 | +127.0000 | 🟢 Improved |
| val_puzzles_with_all_true_groups_in_top_20 | 7.3000 | 22.9000 | +15.6000 | 🟢 Improved |
| val_puzzles_with_any_true_group_in_top_20 | 65.1000 | 80.7000 | +15.6000 | 🟢 Improved |
| val_validation_puzzles | 109.0000 | 109.0000 | 0 | No Change |

## Archetype Metrics Comparison

| Archetype | Metric | Model A | Model B | Delta (B - A) | Status |
|---|---|---:|---:|---:|---|
