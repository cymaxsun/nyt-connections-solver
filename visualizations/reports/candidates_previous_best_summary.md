# GCN Subgraph Predictions - All Validation Puzzles

Generated from the current `models/gcn_best.pt` checkpoint loaded by the training pipeline.

This document summarizes the top 5 candidate partitions built from GCN predictions for all 109 validation puzzles. Each group is labeled with exact correctness or maximum overlap with a ground truth category.

## Aggregate Summary

| Metric | Value | Previous | Change |
|---|---:|---:|---:|
| Validation puzzles | 109 | 109 | 0 |
| Overall GCN Candidate MRR | 0.1277 | 0.1233 | 🟢 +0.00 (improved) |
| Overall Pairwise Relation Accuracy | 79.0% | 79.6% | 🔴 -0.6% (regressed) |
| Overall Group Relation Accuracy | 94.2% | 94.2% | 0.0% |
| Puzzles with complete partition candidates | 88 / 109 (80.7%) | 81 / 109 (74.3%) | 🟢 +6.4% (improved) |
| Top partition solves all 4 groups | 4 / 109 (3.7%) | 4 / 109 (3.7%) | 0.0% |
| Any top-5 partition solves all 4 groups | 10 / 109 (9.2%) | 9 / 109 (8.3%) | 🟢 +0.9% (improved) |
| Avg correct groups in top partition | 0.56 / 4 | 0.60 / 4 | 🔴 -0.04 (regressed) |
| Avg best correct groups across top partitions | 0.89 / 4 | 0.91 / 4 | 🔴 -0.02 (regressed) |
| True groups in top-20 candidates | 127 / 436 (29.1%) | 126 / 436 (28.9%) | 🟢 +0.2% (improved) |
| Puzzles with any true group in top-20 | 75 / 109 (68.8%) | 70 / 109 (64.2%) | 🟢 +4.6% (improved) |
| Puzzles with all true groups in top-20 | 11 / 109 (10.1%) | 9 / 109 (8.3%) | 🟢 +1.8% (improved) |
| Mean rank of true groups found in top-20 | 5.82 | 5.01 | 🔴 +0.81 (regressed) |
| Median rank of true groups found in top-20 | 4.0 | 3.0 | 🔴 +1.00 (regressed) |
| 3-of-4 near-miss candidates in top-20 | 780 | 769 | 🟢 +11 (improved) |

### Recall By Relation Archetype

| Archetype | True Groups | Hit Top 20 | Recall | Hit Top 5 | Avg Best Rank | Exact MRR | Pairwise Acc | Group Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| COMMON_PHRASE | 4 | 0 | 0.0% | 0 | 0.00 | 0.0024 | 0.0% | 0.0% |
| FILL_IN_THE_BLANK | 43 | 5 | 11.6% | 3 | 6.00 | 0.0138 | 1.6% | 2.3% |
| NAMED_ENTITY_SET | 62 | 12 | 19.4% | 6 | 7.58 | 0.0597 | 0.5% | 0.0% |
| NO_RELATION | 0 | 0 | 0.0% | 0 | 0.00 | 0.0000 | 95.0% | 100.0% |
| SEMANTIC_SET | 151 | 44 | 29.1% | 31 | 5.11 | 0.1411 | 14.5% | 0.0% |
| SOUND_OR_SPELLING | 19 | 2 | 10.5% | 0 | 10.00 | 0.0163 | 1.8% | 0.0% |
| SYNONYM_OR_NEAR | 119 | 59 | 49.6% | 38 | 5.66 | 0.2372 | 32.2% | 2.5% |
| WORDPLAY_TRANSFORM | 31 | 4 | 12.9% | 2 | 8.25 | 0.0164 | 8.1% | 0.0% |
| WORD_FORM | 7 | 1 | 14.3% | 0 | 6.00 | 0.1463 | 2.4% | 0.0% |

---

## Puzzle 0 (ID: 688)
**Words on Board:** MOUNTAIN, ROPE, RHOMBUS, PLATE, INFIELD, TREE, BATTER, DOUGH, GEMSTONE, CANDLESTICK, MIXTURE, SUIT, PASTE, PLACEMAT, PITCHER, LADDER

### Ground Truth Categories:
* **Level 0 (COOKING CONCOCTIONS) [Type: SEMANTIC_SET]:** BATTER, DOUGH, MIXTURE, PASTE
* **Level 1 (SEEN ON A TABLE AT A DINNER PARTY) [Type: SEMANTIC_SET]:** CANDLESTICK, PITCHER, PLACEMAT, PLATE
* **Level 2 (THINGS TO CLIMB) [Type: SEMANTIC_SET]:** LADDER, MOUNTAIN, ROPE, TREE
* **Level 3 (WHAT "DIAMOND" CAN REFER TO) [Type: WORDPLAY_TRANSFORM]:** GEMSTONE, INFIELD, RHOMBUS, SUIT

### Top Candidate Partitions:
1. **Partition Score: 0.5447**
   - Group 1: **0.7439** | PLATE, INFIELD, BATTER, PITCHER                                   | INCORRECT (Max overlap: 2/4 with SEEN ON A TABLE AT A DINNER PARTY)
   - Group 2: **0.5801** | RHOMBUS, TREE, GEMSTONE, CANDLESTICK                              | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
   - Group 3: **0.5442** | DOUGH, MIXTURE, PASTE, PLACEMAT                                   | INCORRECT (Max overlap: 3/4 with COOKING CONCOCTIONS)
   - Group 4: **0.5273** | MOUNTAIN, ROPE, SUIT, LADDER                                      | INCORRECT (Max overlap: 3/4 with THINGS TO CLIMB)
2. **Partition Score: 0.5439**
   - Group 1: **0.6944** | BATTER, DOUGH, MIXTURE, PASTE                                     | CORRECT GROUP (COOKING CONCOCTIONS, Level 0)
   - Group 2: **0.5801** | RHOMBUS, TREE, GEMSTONE, CANDLESTICK                              | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
   - Group 3: **0.5408** | PLATE, INFIELD, PLACEMAT, PITCHER                                 | INCORRECT (Max overlap: 3/4 with SEEN ON A TABLE AT A DINNER PARTY)
   - Group 4: **0.5273** | MOUNTAIN, ROPE, SUIT, LADDER                                      | INCORRECT (Max overlap: 3/4 with THINGS TO CLIMB)
3. **Partition Score: 0.5429**
   - Group 1: **0.5579** | MOUNTAIN, RHOMBUS, GEMSTONE, CANDLESTICK                          | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
   - Group 2: **0.5493** | ROPE, TREE, PITCHER, LADDER                                       | INCORRECT (Max overlap: 3/4 with THINGS TO CLIMB)
   - Group 3: **0.5442** | DOUGH, MIXTURE, PASTE, PLACEMAT                                   | INCORRECT (Max overlap: 3/4 with COOKING CONCOCTIONS)
   - Group 4: **0.5392** | PLATE, INFIELD, BATTER, SUIT                                      | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
4. **Partition Score: 0.5367**
   - Group 1: **0.5579** | MOUNTAIN, RHOMBUS, GEMSTONE, CANDLESTICK                          | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
   - Group 2: **0.5519** | INFIELD, BATTER, DOUGH, MIXTURE                                   | INCORRECT (Max overlap: 3/4 with COOKING CONCOCTIONS)
   - Group 3: **0.5493** | ROPE, TREE, PITCHER, LADDER                                       | INCORRECT (Max overlap: 3/4 with THINGS TO CLIMB)
   - Group 4: **0.5228** | PLATE, SUIT, PASTE, PLACEMAT                                      | INCORRECT (Max overlap: 2/4 with SEEN ON A TABLE AT A DINNER PARTY)
5. **Partition Score: 0.5318**
   - Group 1: **0.6944** | BATTER, DOUGH, MIXTURE, PASTE                                     | CORRECT GROUP (COOKING CONCOCTIONS, Level 0)
   - Group 2: **0.5579** | MOUNTAIN, RHOMBUS, GEMSTONE, CANDLESTICK                          | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
   - Group 3: **0.5493** | ROPE, TREE, PITCHER, LADDER                                       | INCORRECT (Max overlap: 3/4 with THINGS TO CLIMB)
   - Group 4: **0.5100** | PLATE, INFIELD, SUIT, PLACEMAT                                    | INCORRECT (Max overlap: 2/4 with SEEN ON A TABLE AT A DINNER PARTY)

### Top Candidate Groups:
   - Group 1: **0.7439** | PLATE, INFIELD, BATTER, PITCHER                                   | INCORRECT (Max overlap: 2/4 with SEEN ON A TABLE AT A DINNER PARTY)
   - Group 2: **0.5801** | RHOMBUS, TREE, GEMSTONE, CANDLESTICK                              | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
   - Group 3: **0.5442** | DOUGH, MIXTURE, PASTE, PLACEMAT                                   | INCORRECT (Max overlap: 3/4 with COOKING CONCOCTIONS)
   - Group 4: **0.5273** | MOUNTAIN, ROPE, SUIT, LADDER                                      | INCORRECT (Max overlap: 3/4 with THINGS TO CLIMB)
   - Group 5: **0.6944** | BATTER, DOUGH, MIXTURE, PASTE                                     | CORRECT GROUP (COOKING CONCOCTIONS, Level 0)
   - Group 6: **0.5408** | PLATE, INFIELD, PLACEMAT, PITCHER                                 | INCORRECT (Max overlap: 3/4 with SEEN ON A TABLE AT A DINNER PARTY)
   - Group 7: **0.5579** | MOUNTAIN, RHOMBUS, GEMSTONE, CANDLESTICK                          | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
   - Group 8: **0.5493** | ROPE, TREE, PITCHER, LADDER                                       | INCORRECT (Max overlap: 3/4 with THINGS TO CLIMB)
   - Group 9: **0.5392** | PLATE, INFIELD, BATTER, SUIT                                      | INCORRECT (Max overlap: 2/4 with WHAT "DIAMOND" CAN REFER TO)
   - Group 10: **0.5519** | INFIELD, BATTER, DOUGH, MIXTURE                                   | INCORRECT (Max overlap: 3/4 with COOKING CONCOCTIONS)
   - Group 11: **0.5228** | PLATE, SUIT, PASTE, PLACEMAT                                      | INCORRECT (Max overlap: 2/4 with SEEN ON A TABLE AT A DINNER PARTY)
   - Group 12: **0.5100** | PLATE, INFIELD, SUIT, PLACEMAT                                    | INCORRECT (Max overlap: 2/4 with SEEN ON A TABLE AT A DINNER PARTY)
   - Group 13: **0.5118** | ROPE, TREE, SUIT, LADDER                                          | INCORRECT (Max overlap: 3/4 with THINGS TO CLIMB)
   - Group 14: **0.5554** | PLATE, INFIELD, BATTER, MIXTURE                                   | INCORRECT (Max overlap: 2/4 with COOKING CONCOCTIONS)
   - Group 15: **0.5089** | DOUGH, SUIT, PASTE, PLACEMAT                                      | INCORRECT (Max overlap: 2/4 with COOKING CONCOCTIONS)
   - Group 16: **0.5287** | PLATE, INFIELD, BATTER, PLACEMAT                                  | INCORRECT (Max overlap: 2/4 with SEEN ON A TABLE AT A DINNER PARTY)
   - Group 17: **0.5182** | DOUGH, MIXTURE, SUIT, PASTE                                       | INCORRECT (Max overlap: 3/4 with COOKING CONCOCTIONS)
   - Group 18: **0.5669** | MOUNTAIN, RHOMBUS, TREE, GEMSTONE                                 | INCORRECT (Max overlap: 2/4 with THINGS TO CLIMB)
   - Group 19: **0.4967** | ROPE, CANDLESTICK, SUIT, LADDER                                   | INCORRECT (Max overlap: 2/4 with THINGS TO CLIMB)
   - Group 20: **0.5103** | ROPE, CANDLESTICK, PITCHER, LADDER                                | INCORRECT (Max overlap: 2/4 with THINGS TO CLIMB)

---

## Puzzle 1 (ID: 993)
**Words on Board:** BEAM, POPCORN, STATION, POSITION, FUNKY, STRIKE, STANDING, SAFE, VAULT, FOUL, RANK, BALL, RINGS, SPRING, RUBBER, HORSE

### Ground Truth Categories:
* **Level 0 (GYMNASTICS APPARATUS) [Type: SEMANTIC_SET]:** BEAM, HORSE, RINGS, VAULT
* **Level 1 (STATUS) [Type: SYNONYM_OR_NEAR]:** POSITION, RANK, STANDING, STATION
* **Level 2 (BASEBALL CALLS) [Type: SEMANTIC_SET]:** BALL, FOUL, SAFE, STRIKE
* **Level 3 (___ CHICKEN) [Type: FILL_IN_THE_BLANK]:** FUNKY, POPCORN, RUBBER, SPRING

### Top Candidate Partitions:
1. **Partition Score: 0.5434**
   - Group 1: **0.6661** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1)
   - Group 2: **0.5854** | BEAM, POPCORN, RINGS, HORSE                                       | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 3: **0.5459** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS)
   - Group 4: **0.5211** | SAFE, VAULT, SPRING, RUBBER                                       | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
2. **Partition Score: 0.5390**
   - Group 1: **0.6661** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1)
   - Group 2: **0.5459** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS)
   - Group 3: **0.5401** | POPCORN, SPRING, RUBBER, HORSE                                    | INCORRECT (Max overlap: 3/4 with ___ CHICKEN)
   - Group 4: **0.5350** | BEAM, SAFE, VAULT, RINGS                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
3. **Partition Score: 0.5324**
   - Group 1: **0.6661** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1)
   - Group 2: **0.5677** | BEAM, SAFE, VAULT, SPRING                                         | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 3: **0.5459** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS)
   - Group 4: **0.5080** | POPCORN, RINGS, RUBBER, HORSE                                     | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
4. **Partition Score: 0.5321**
   - Group 1: **0.6661** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1)
   - Group 2: **0.6250** | BEAM, SAFE, VAULT, HORSE                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 3: **0.5459** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS)
   - Group 4: **0.4788** | POPCORN, RINGS, SPRING, RUBBER                                    | INCORRECT (Max overlap: 3/4 with ___ CHICKEN)
5. **Partition Score: 0.5307**
   - Group 1: **0.6661** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1)
   - Group 2: **0.5632** | BEAM, POPCORN, VAULT, SPRING                                      | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 3: **0.5459** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS)
   - Group 4: **0.5068** | SAFE, RINGS, RUBBER, HORSE                                        | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)

### Top Candidate Groups:
   - Group 1: **0.6661** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1)
   - Group 2: **0.5854** | BEAM, POPCORN, RINGS, HORSE                                       | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 3: **0.5459** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS)
   - Group 4: **0.5211** | SAFE, VAULT, SPRING, RUBBER                                       | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 5: **0.5401** | POPCORN, SPRING, RUBBER, HORSE                                    | INCORRECT (Max overlap: 3/4 with ___ CHICKEN)
   - Group 6: **0.5350** | BEAM, SAFE, VAULT, RINGS                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 7: **0.5677** | BEAM, SAFE, VAULT, SPRING                                         | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 8: **0.5080** | POPCORN, RINGS, RUBBER, HORSE                                     | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 9: **0.6250** | BEAM, SAFE, VAULT, HORSE                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 10: **0.4788** | POPCORN, RINGS, SPRING, RUBBER                                    | INCORRECT (Max overlap: 3/4 with ___ CHICKEN)
   - Group 11: **0.5632** | BEAM, POPCORN, VAULT, SPRING                                      | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 12: **0.5068** | SAFE, RINGS, RUBBER, HORSE                                        | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 13: **0.5972** | BEAM, RINGS, RUBBER, HORSE                                        | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 14: **0.4869** | POPCORN, SAFE, VAULT, SPRING                                      | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 15: **0.6099** | BEAM, RINGS, SPRING, HORSE                                        | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 16: **0.4745** | POPCORN, SAFE, VAULT, RUBBER                                      | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 17: **0.5773** | POPCORN, VAULT, SPRING, HORSE                                     | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 18: **0.4900** | BEAM, SAFE, RINGS, RUBBER                                         | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 19: **0.5400** | SAFE, VAULT, RINGS, HORSE                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 20: **0.5051** | BEAM, POPCORN, SPRING, RUBBER                                     | INCORRECT (Max overlap: 3/4 with ___ CHICKEN)

---

## Puzzle 2 (ID: 320)
**Words on Board:** SIGHT, IMPACT, TASTE, TOUCH, BAKE, ELEGANCE, STYLE, SUN, SEN, BASK, SOUR, TAN, GRACE, MOVE, AFFECT, SINE

### Ground Truth Categories:
* **Level 0 (REFINED SENSIBILITY) [Type: SYNONYM_OR_NEAR]:** ELEGANCE, GRACE, STYLE, TASTE
* **Level 1 (CATCH SOME RAYS) [Type: SYNONYM_OR_NEAR]:** BAKE, BASK, SUN, TAN
* **Level 2 (EMOTIONALLY SWAY ) [Type: SYNONYM_OR_NEAR]:** AFFECT, IMPACT, MOVE, TOUCH
* **Level 3 (NUMBERS WITH FIRST LETTERS REPLACED BY “S”) [Type: WORDPLAY_TRANSFORM]:** SEN, SIGHT, SINE, SOUR

### Top Candidate Partitions:
1. **Partition Score: 0.5498**
   - Group 1: **0.7417** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2)
   - Group 2: **0.7316** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 3: **0.5597** | TASTE, ELEGANCE, STYLE, SOUR                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 4: **0.4540** | SIGHT, BAKE, SEN, GRACE                                           | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
2. **Partition Score: 0.5242**
   - Group 1: **0.7417** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2)
   - Group 2: **0.7316** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 3: **0.4929** | SIGHT, TASTE, ELEGANCE, SOUR                                      | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 4: **0.4361** | BAKE, STYLE, SEN, GRACE                                           | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
3. **Partition Score: 0.5228**
   - Group 1: **0.7417** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2)
   - Group 2: **0.7316** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 3: **0.5116** | TASTE, ELEGANCE, SOUR, GRACE                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 4: **0.4240** | SIGHT, BAKE, STYLE, SEN                                           | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
4. **Partition Score: 0.5172**
   - Group 1: **0.7417** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2)
   - Group 2: **0.7316** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 3: **0.4826** | BAKE, ELEGANCE, STYLE, GRACE                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 4: **0.4273** | SIGHT, TASTE, SEN, SOUR                                           | INCORRECT (Max overlap: 3/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
5. **Partition Score: 0.5142**
   - Group 1: **0.7417** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2)
   - Group 2: **0.7316** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 3: **0.4816** | TASTE, BAKE, STYLE, GRACE                                         | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 4: **0.4219** | SIGHT, ELEGANCE, SEN, SOUR                                        | INCORRECT (Max overlap: 3/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)

### Top Candidate Groups:
   - Group 1: **0.7417** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2)
   - Group 2: **0.7316** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 3: **0.5597** | TASTE, ELEGANCE, STYLE, SOUR                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 4: **0.4540** | SIGHT, BAKE, SEN, GRACE                                           | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 5: **0.4929** | SIGHT, TASTE, ELEGANCE, SOUR                                      | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 6: **0.4361** | BAKE, STYLE, SEN, GRACE                                           | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 7: **0.5116** | TASTE, ELEGANCE, SOUR, GRACE                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 8: **0.4240** | SIGHT, BAKE, STYLE, SEN                                           | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 9: **0.4826** | BAKE, ELEGANCE, STYLE, GRACE                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 10: **0.4273** | SIGHT, TASTE, SEN, SOUR                                           | INCORRECT (Max overlap: 3/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 11: **0.4816** | TASTE, BAKE, STYLE, GRACE                                         | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 12: **0.4219** | SIGHT, ELEGANCE, SEN, SOUR                                        | INCORRECT (Max overlap: 3/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 13: **0.4707** | SIGHT, TASTE, BAKE, GRACE                                         | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 14: **0.4127** | ELEGANCE, STYLE, SEN, SOUR                                        | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 15: **0.4495** | TASTE, STYLE, SEN, SOUR                                           | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 16: **0.4149** | SIGHT, BAKE, ELEGANCE, GRACE                                      | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 17: **0.4933** | SUN, SEN, TAN, SINE                                               | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS)
   - Group 18: **0.4728** | SIGHT, BAKE, BASK, GRACE                                          | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS)
   - Group 19: **0.4557** | SIGHT, TASTE, BAKE, STYLE                                         | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 20: **0.4026** | ELEGANCE, SEN, SOUR, GRACE                                        | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)

---

## Puzzle 3 (ID: 731)
**Words on Board:** STRUT, NUMBER, DAGGER, EYEBROW, ELVES, PARENS, BANANA, LEPRECHAUN, ASTERISK, RAINBOW, FLIGHT PATH, BLUSTER, CROW, COUNT, ROOSTER, SHOW OFF

### Ground Truth Categories:
* **Level 0 (BOAST) [Type: SYNONYM_OR_NEAR]:** BLUSTER, CROW, SHOW OFF, STRUT
* **Level 1 (ARC-SHAPED THINGS) [Type: SEMANTIC_SET]:** BANANA, EYEBROW, FLIGHT PATH, RAINBOW
* **Level 2 (CEREAL MASCOTS) [Type: NAMED_ENTITY_SET]:** COUNT, ELVES, LEPRECHAUN, ROOSTER
* **Level 3 (WAYS TO DENOTE A CITATION) [Type: SEMANTIC_SET]:** ASTERISK, DAGGER, NUMBER, PARENS

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6683** | BANANA, LEPRECHAUN, RAINBOW, ROOSTER                              | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)
   - Group 2: **0.6128** | EYEBROW, BANANA, RAINBOW, ROOSTER                                 | INCORRECT (Max overlap: 3/4 with ARC-SHAPED THINGS)
   - Group 3: **0.6102** | ELVES, LEPRECHAUN, RAINBOW, ROOSTER                               | INCORRECT (Max overlap: 3/4 with CEREAL MASCOTS)
   - Group 4: **0.6002** | DAGGER, BANANA, RAINBOW, ROOSTER                                  | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)
   - Group 5: **0.5963** | ELVES, BANANA, RAINBOW, ROOSTER                                   | INCORRECT (Max overlap: 2/4 with CEREAL MASCOTS)
   - Group 6: **0.5936** | ELVES, BANANA, LEPRECHAUN, RAINBOW                                | INCORRECT (Max overlap: 2/4 with CEREAL MASCOTS)
   - Group 7: **0.5820** | DAGGER, ASTERISK, RAINBOW, ROOSTER                                | INCORRECT (Max overlap: 2/4 with WAYS TO DENOTE A CITATION)
   - Group 8: **0.5817** | BANANA, ASTERISK, RAINBOW, ROOSTER                                | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)
   - Group 9: **0.5717** | BANANA, RAINBOW, CROW, ROOSTER                                    | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)
   - Group 10: **0.5680** | ELVES, BANANA, LEPRECHAUN, ROOSTER                                | INCORRECT (Max overlap: 3/4 with CEREAL MASCOTS)
   - Group 11: **0.5660** | PARENS, BANANA, RAINBOW, ROOSTER                                  | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)
   - Group 12: **0.5404** | DAGGER, EYEBROW, RAINBOW, ROOSTER                                 | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)
   - Group 13: **0.5384** | DAGGER, EYEBROW, BANANA, RAINBOW                                  | INCORRECT (Max overlap: 3/4 with ARC-SHAPED THINGS)
   - Group 14: **0.5380** | PARENS, BANANA, LEPRECHAUN, RAINBOW                               | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)
   - Group 15: **0.5370** | DAGGER, BANANA, ASTERISK, RAINBOW                                 | INCORRECT (Max overlap: 2/4 with WAYS TO DENOTE A CITATION)
   - Group 16: **0.5361** | DAGGER, BANANA, ASTERISK, ROOSTER                                 | INCORRECT (Max overlap: 2/4 with WAYS TO DENOTE A CITATION)
   - Group 17: **0.5356** | EYEBROW, ASTERISK, RAINBOW, ROOSTER                               | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)
   - Group 18: **0.5346** | DAGGER, LEPRECHAUN, RAINBOW, ROOSTER                              | INCORRECT (Max overlap: 2/4 with CEREAL MASCOTS)
   - Group 19: **0.5336** | EYEBROW, PARENS, BANANA, RAINBOW                                  | INCORRECT (Max overlap: 3/4 with ARC-SHAPED THINGS)
   - Group 20: **0.5327** | ELVES, PARENS, BANANA, RAINBOW                                    | INCORRECT (Max overlap: 2/4 with ARC-SHAPED THINGS)

---

## Puzzle 4 (ID: 206)
**Words on Board:** CHECK, TIP, MIKE, PAIN, COLE, TAP, WIRE, TICK, MARK, 40, GLIDE, SOAR, X, BUG, FLY, FLOAT

### Ground Truth Categories:
* **Level 0 (MOVE THROUGH THE AIR) [Type: SYNONYM_OR_NEAR]:** FLOAT, FLY, GLIDE, SOAR
* **Level 1 (HIDDEN LISTENING DEVICES) [Type: SYNONYM_OR_NEAR]:** BUG, MIKE, TAP, WIRE
* **Level 2 (SELECT, AS A BOX ON A FORM) [Type: SYNONYM_OR_NEAR]:** CHECK, MARK, TICK, X
* **Level 3 (RAPPERS MINUS FIRST LETTER) [Type: WORDPLAY_TRANSFORM]:** 40, COLE, PAIN, TIP

### Top Candidate Partitions:
1. **Partition Score: 0.5280**
   - Group 1: **0.6940** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0)
   - Group 2: **0.6170** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.5197** | CHECK, TIP, TICK, MARK                                            | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM)
   - Group 4: **0.4876** | TAP, WIRE, X, BUG                                                 | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)
2. **Partition Score: 0.5273**
   - Group 1: **0.6940** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0)
   - Group 2: **0.5590** | MIKE, COLE, 40, BUG                                               | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 3: **0.5260** | PAIN, WIRE, MARK, X                                               | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 4: **0.5120** | CHECK, TIP, TAP, TICK                                             | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
3. **Partition Score: 0.5252**
   - Group 1: **0.6940** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0)
   - Group 2: **0.6170** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.5120** | CHECK, TIP, TAP, TICK                                             | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 4: **0.4860** | WIRE, MARK, X, BUG                                                | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
4. **Partition Score: 0.5196**
   - Group 1: **0.6940** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0)
   - Group 2: **0.6194** | MIKE, PAIN, 40, BUG                                               | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 3: **0.5120** | CHECK, TIP, TAP, TICK                                             | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 4: **0.4735** | COLE, WIRE, MARK, X                                               | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
5. **Partition Score: 0.5117**
   - Group 1: **0.6940** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0)
   - Group 2: **0.5604** | MIKE, PAIN, COLE, MARK                                            | INCORRECT (Max overlap: 2/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.5120** | CHECK, TIP, TAP, TICK                                             | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 4: **0.4873** | WIRE, 40, X, BUG                                                  | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)

### Top Candidate Groups:
   - Group 1: **0.6940** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0)
   - Group 2: **0.6170** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.5197** | CHECK, TIP, TICK, MARK                                            | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM)
   - Group 4: **0.4876** | TAP, WIRE, X, BUG                                                 | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)
   - Group 5: **0.5590** | MIKE, COLE, 40, BUG                                               | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 6: **0.5260** | PAIN, WIRE, MARK, X                                               | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 7: **0.5120** | CHECK, TIP, TAP, TICK                                             | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 8: **0.4860** | WIRE, MARK, X, BUG                                                | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 9: **0.6194** | MIKE, PAIN, 40, BUG                                               | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 10: **0.4735** | COLE, WIRE, MARK, X                                               | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 11: **0.5604** | MIKE, PAIN, COLE, MARK                                            | INCORRECT (Max overlap: 2/4 with RAPPERS MINUS FIRST LETTER)
   - Group 12: **0.4873** | WIRE, 40, X, BUG                                                  | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 13: **0.5143** | MIKE, COLE, WIRE, MARK                                            | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 14: **0.5053** | PAIN, 40, X, BUG                                                  | INCORRECT (Max overlap: 2/4 with RAPPERS MINUS FIRST LETTER)
   - Group 15: **0.5150** | CHECK, GLIDE, SOAR, FLY                                           | INCORRECT (Max overlap: 3/4 with MOVE THROUGH THE AIR)
   - Group 16: **0.4987** | TIP, TAP, TICK, MARK                                              | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 17: **0.4889** | WIRE, X, BUG, FLOAT                                               | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 18: **0.5949** | CHECK, TICK, MARK, X                                              | CORRECT GROUP (SELECT, AS A BOX ON A FORM, Level 2)
   - Group 19: **0.4833** | TAP, WIRE, BUG, FLOAT                                             | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)
   - Group 20: **0.4518** | TIP, GLIDE, SOAR, FLY                                             | INCORRECT (Max overlap: 3/4 with MOVE THROUGH THE AIR)

---

## Puzzle 5 (ID: 707)
**Words on Board:** DRILL, EXCELLENT, EXERCISE, NOT QUITE, AREA, LESSON, ATHLETIC, ALMOST, ONE, WARM, OPEN, EASY, CLOSE, GAME, FLEXIBLE, ASSIGNMENT

### Ground Truth Categories:
* **Level 0 (TASKS FOR A STUDENT) [Type: SEMANTIC_SET]:** ASSIGNMENT, DRILL, EXERCISE, LESSON
* **Level 1 (ENCOURAGING RESPONSES IN A GUESSING GAME) [Type: SYNONYM_OR_NEAR]:** ALMOST, CLOSE, NOT QUITE, WARM
* **Level 2 (UP FOR ANYTHING) [Type: SYNONYM_OR_NEAR]:** EASY, FLEXIBLE, GAME, OPEN
* **Level 3 (WHAT “A” MIGHT MEAN) [Type: WORDPLAY_TRANSFORM]:** AREA, ATHLETIC, EXCELLENT, ONE

### Top Candidate Partitions:
1. **Partition Score: 0.5661**
   - Group 1: **0.6371** | NOT QUITE, ALMOST, ONE, CLOSE                                     | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 2: **0.5968** | EXCELLENT, ATHLETIC, EASY, FLEXIBLE                               | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 3: **0.5824** | AREA, WARM, OPEN, GAME                                            | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 4: **0.5427** | DRILL, EXERCISE, LESSON, ASSIGNMENT                               | CORRECT GROUP (TASKS FOR A STUDENT, Level 0)
2. **Partition Score: 0.5629**
   - Group 1: **0.6533** | EXCELLENT, NOT QUITE, ALMOST, CLOSE                               | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 2: **0.6020** | ONE, WARM, OPEN, EASY                                             | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 3: **0.5642** | AREA, ATHLETIC, GAME, FLEXIBLE                                    | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 4: **0.5427** | DRILL, EXERCISE, LESSON, ASSIGNMENT                               | CORRECT GROUP (TASKS FOR A STUDENT, Level 0)
3. **Partition Score: 0.5622**
   - Group 1: **0.6371** | NOT QUITE, ALMOST, ONE, CLOSE                                     | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 2: **0.5991** | EXCELLENT, WARM, OPEN, EASY                                       | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 3: **0.5642** | AREA, ATHLETIC, GAME, FLEXIBLE                                    | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 4: **0.5427** | DRILL, EXERCISE, LESSON, ASSIGNMENT                               | CORRECT GROUP (TASKS FOR A STUDENT, Level 0)
4. **Partition Score: 0.5616**
   - Group 1: **0.6371** | NOT QUITE, ALMOST, ONE, CLOSE                                     | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 2: **0.6172** | EXCELLENT, OPEN, EASY, FLEXIBLE                                   | INCORRECT (Max overlap: 3/4 with UP FOR ANYTHING)
   - Group 3: **0.5438** | AREA, ATHLETIC, WARM, GAME                                        | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 4: **0.5427** | DRILL, EXERCISE, LESSON, ASSIGNMENT                               | CORRECT GROUP (TASKS FOR A STUDENT, Level 0)
5. **Partition Score: 0.5609**
   - Group 1: **0.6533** | EXCELLENT, NOT QUITE, ALMOST, CLOSE                               | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 2: **0.5887** | ATHLETIC, WARM, EASY, FLEXIBLE                                    | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 3: **0.5695** | AREA, ONE, OPEN, GAME                                             | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 4: **0.5427** | DRILL, EXERCISE, LESSON, ASSIGNMENT                               | CORRECT GROUP (TASKS FOR A STUDENT, Level 0)

### Top Candidate Groups:
   - Group 1: **0.6371** | NOT QUITE, ALMOST, ONE, CLOSE                                     | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 2: **0.5968** | EXCELLENT, ATHLETIC, EASY, FLEXIBLE                               | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 3: **0.5824** | AREA, WARM, OPEN, GAME                                            | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 4: **0.5427** | DRILL, EXERCISE, LESSON, ASSIGNMENT                               | CORRECT GROUP (TASKS FOR A STUDENT, Level 0)
   - Group 5: **0.6533** | EXCELLENT, NOT QUITE, ALMOST, CLOSE                               | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 6: **0.6020** | ONE, WARM, OPEN, EASY                                             | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 7: **0.5642** | AREA, ATHLETIC, GAME, FLEXIBLE                                    | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 8: **0.5991** | EXCELLENT, WARM, OPEN, EASY                                       | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 9: **0.6172** | EXCELLENT, OPEN, EASY, FLEXIBLE                                   | INCORRECT (Max overlap: 3/4 with UP FOR ANYTHING)
   - Group 10: **0.5438** | AREA, ATHLETIC, WARM, GAME                                        | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 11: **0.5887** | ATHLETIC, WARM, EASY, FLEXIBLE                                    | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 12: **0.5695** | AREA, ONE, OPEN, GAME                                             | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 13: **0.5870** | AREA, ONE, WARM, GAME                                             | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 14: **0.5711** | NOT QUITE, ALMOST, OPEN, CLOSE                                    | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 15: **0.5843** | EXCELLENT, ATHLETIC, WARM, FLEXIBLE                               | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 16: **0.5801** | AREA, ONE, EASY, GAME                                             | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)
   - Group 17: **0.5780** | NOT QUITE, ALMOST, EASY, CLOSE                                    | INCORRECT (Max overlap: 3/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 18: **0.6007** | ATHLETIC, WARM, EASY, GAME                                        | INCORRECT (Max overlap: 2/4 with UP FOR ANYTHING)
   - Group 19: **0.5994** | EXCELLENT, NOT QUITE, ALMOST, FLEXIBLE                            | INCORRECT (Max overlap: 2/4 with ENCOURAGING RESPONSES IN A GUESSING GAME)
   - Group 20: **0.5467** | AREA, ONE, OPEN, CLOSE                                            | INCORRECT (Max overlap: 2/4 with WHAT “A” MIGHT MEAN)

---

## Puzzle 6 (ID: 1043)
**Words on Board:** MOTHER, DEVOTE, SKIRT, WHAMMY, PULP, NEIGHBOR, EDUCATED, HISTORICAL, TOTORO, FLANK, ASIAGO, MY, TOUCH, SCIENCE, LITERARY, VERY

### Ground Truth Categories:
* **Level 0 (BORDER) [Type: SYNONYM_OR_NEAR]:** FLANK, NEIGHBOR, SKIRT, TOUCH
* **Level 1 (KINDS OF FICTION) [Type: SEMANTIC_SET]:** HISTORICAL, LITERARY, PULP, SCIENCE
* **Level 2 (WORDS IN A PLANETARY MNEMONIC) [Type: COMMON_PHRASE]:** EDUCATED, MOTHER, MY, VERY
* **Level 3 (STARTING WITH FOUR-LETTER '80S BANDS) [Type: WORDPLAY_TRANSFORM]:** ASIAGO, DEVOTE, TOTORO, WHAMMY

### Top Candidate Partitions:
1. **Partition Score: 0.4999**
   - Group 1: **0.5329** | DEVOTE, EDUCATED, HISTORICAL, LITERARY                            | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 2: **0.5024** | WHAMMY, PULP, MY, SCIENCE                                         | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 3: **0.5020** | MOTHER, NEIGHBOR, TOTORO, ASIAGO                                  | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 4: **0.4977** | SKIRT, FLANK, TOUCH, VERY                                         | INCORRECT (Max overlap: 3/4 with BORDER)
2. **Partition Score: 0.4977**
   - Group 1: **0.5518** | MOTHER, WHAMMY, PULP, SCIENCE                                     | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 2: **0.5329** | DEVOTE, EDUCATED, HISTORICAL, LITERARY                            | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 3: **0.4977** | SKIRT, FLANK, TOUCH, VERY                                         | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 4: **0.4801** | NEIGHBOR, TOTORO, ASIAGO, MY                                      | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
3. **Partition Score: 0.4973**
   - Group 1: **0.5329** | DEVOTE, EDUCATED, HISTORICAL, LITERARY                            | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 2: **0.5049** | WHAMMY, NEIGHBOR, TOTORO, ASIAGO                                  | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 3: **0.4977** | SKIRT, FLANK, TOUCH, VERY                                         | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 4: **0.4934** | MOTHER, PULP, MY, SCIENCE                                         | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
4. **Partition Score: 0.4888**
   - Group 1: **0.5329** | DEVOTE, EDUCATED, HISTORICAL, LITERARY                            | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 2: **0.5219** | MOTHER, NEIGHBOR, TOTORO, MY                                      | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 3: **0.4977** | SKIRT, FLANK, TOUCH, VERY                                         | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 4: **0.4678** | WHAMMY, PULP, ASIAGO, SCIENCE                                     | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
5. **Partition Score: 0.4885**
   - Group 1: **0.5329** | DEVOTE, EDUCATED, HISTORICAL, LITERARY                            | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 2: **0.5020** | MOTHER, NEIGHBOR, TOTORO, ASIAGO                                  | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 3: **0.4896** | SKIRT, PULP, FLANK, TOUCH                                         | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 4: **0.4813** | WHAMMY, MY, SCIENCE, VERY                                         | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)

### Top Candidate Groups:
   - Group 1: **0.5329** | DEVOTE, EDUCATED, HISTORICAL, LITERARY                            | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 2: **0.5024** | WHAMMY, PULP, MY, SCIENCE                                         | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 3: **0.5020** | MOTHER, NEIGHBOR, TOTORO, ASIAGO                                  | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 4: **0.4977** | SKIRT, FLANK, TOUCH, VERY                                         | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 5: **0.5518** | MOTHER, WHAMMY, PULP, SCIENCE                                     | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 6: **0.4801** | NEIGHBOR, TOTORO, ASIAGO, MY                                      | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 7: **0.5049** | WHAMMY, NEIGHBOR, TOTORO, ASIAGO                                  | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 8: **0.4934** | MOTHER, PULP, MY, SCIENCE                                         | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 9: **0.5219** | MOTHER, NEIGHBOR, TOTORO, MY                                      | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 10: **0.4678** | WHAMMY, PULP, ASIAGO, SCIENCE                                     | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 11: **0.4896** | SKIRT, PULP, FLANK, TOUCH                                         | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 12: **0.4813** | WHAMMY, MY, SCIENCE, VERY                                         | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 13: **0.5144** | MOTHER, WHAMMY, PULP, MY                                          | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 14: **0.4692** | NEIGHBOR, TOTORO, ASIAGO, SCIENCE                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 15: **0.4915** | MOTHER, TOTORO, ASIAGO, MY                                        | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 16: **0.4844** | WHAMMY, NEIGHBOR, SCIENCE, VERY                                   | INCORRECT (Max overlap: 1/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 17: **0.4961** | SKIRT, NEIGHBOR, FLANK, TOUCH                                     | CORRECT GROUP (BORDER, Level 0)
   - Group 18: **0.4799** | WHAMMY, PULP, SCIENCE, VERY                                       | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 19: **0.5140** | WHAMMY, TOTORO, ASIAGO, MY                                        | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 20: **0.4709** | MOTHER, NEIGHBOR, SCIENCE, VERY                                   | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)

---

## Puzzle 7 (ID: 986)
**Words on Board:** POSTURE, CHRISTMAS TREE, BOLT, MASQUERADE, WEDDING, BLARNEY STONE, PARTY HAT, BLUFF, VOLCANO, FRONT, MISTLETOE, INHALE, CONE, GORGE, NEW YEAR'S EVE, SCARF

### Ground Truth Categories:
* **Level 0 (EAT VORACIOUSLY) [Type: SYNONYM_OR_NEAR]:** BOLT, GORGE, INHALE, SCARF
* **Level 1 (CONICAL THINGS) [Type: SEMANTIC_SET]:** CHRISTMAS TREE, CONE, PARTY HAT, VOLCANO
* **Level 2 (POSE) [Type: SYNONYM_OR_NEAR]:** BLUFF, FRONT, MASQUERADE, POSTURE
* **Level 3 (SETTINGS FOR A KISS) [Type: NAMED_ENTITY_SET]:** BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE, WEDDING

### Top Candidate Partitions:
1. **Partition Score: 0.5178**
   - Group 1: **0.5802** | BLUFF, FRONT, INHALE, SCARF                                       | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 2: **0.5784** | CHRISTMAS TREE, BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE          | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 3: **0.5266** | POSTURE, MASQUERADE, WEDDING, PARTY HAT                           | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 4: **0.4831** | BOLT, VOLCANO, CONE, GORGE                                        | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
2. **Partition Score: 0.5078**
   - Group 1: **0.5784** | CHRISTMAS TREE, BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE          | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 2: **0.5427** | BOLT, FRONT, CONE, SCARF                                          | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 3: **0.5266** | POSTURE, MASQUERADE, WEDDING, PARTY HAT                           | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 4: **0.4809** | BLUFF, VOLCANO, INHALE, GORGE                                     | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
3. **Partition Score: 0.5062**
   - Group 1: **0.5784** | BOLT, FRONT, INHALE, SCARF                                        | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 2: **0.5784** | CHRISTMAS TREE, BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE          | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 3: **0.5266** | POSTURE, MASQUERADE, WEDDING, PARTY HAT                           | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 4: **0.4599** | BLUFF, VOLCANO, CONE, GORGE                                       | INCORRECT (Max overlap: 2/4 with CONICAL THINGS)
4. **Partition Score: 0.4989**
   - Group 1: **0.5784** | CHRISTMAS TREE, BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE          | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 2: **0.5501** | FRONT, INHALE, GORGE, SCARF                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 3: **0.5266** | POSTURE, MASQUERADE, WEDDING, PARTY HAT                           | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 4: **0.4594** | BOLT, BLUFF, VOLCANO, CONE                                        | INCORRECT (Max overlap: 2/4 with CONICAL THINGS)
5. **Partition Score: 0.4981**
   - Group 1: **0.6269** | POSTURE, BLUFF, FRONT, INHALE                                     | INCORRECT (Max overlap: 3/4 with POSE)
   - Group 2: **0.5784** | CHRISTMAS TREE, BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE          | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 3: **0.4831** | BOLT, VOLCANO, CONE, GORGE                                        | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 4: **0.4654** | MASQUERADE, WEDDING, PARTY HAT, SCARF                             | INCORRECT (Max overlap: 1/4 with POSE)

### Top Candidate Groups:
   - Group 1: **0.5802** | BLUFF, FRONT, INHALE, SCARF                                       | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 2: **0.5784** | CHRISTMAS TREE, BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE          | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 3: **0.5266** | POSTURE, MASQUERADE, WEDDING, PARTY HAT                           | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 4: **0.4831** | BOLT, VOLCANO, CONE, GORGE                                        | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 5: **0.5427** | BOLT, FRONT, CONE, SCARF                                          | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 6: **0.4809** | BLUFF, VOLCANO, INHALE, GORGE                                     | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 7: **0.5784** | BOLT, FRONT, INHALE, SCARF                                        | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 8: **0.4599** | BLUFF, VOLCANO, CONE, GORGE                                       | INCORRECT (Max overlap: 2/4 with CONICAL THINGS)
   - Group 9: **0.5501** | FRONT, INHALE, GORGE, SCARF                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 10: **0.4594** | BOLT, BLUFF, VOLCANO, CONE                                        | INCORRECT (Max overlap: 2/4 with CONICAL THINGS)
   - Group 11: **0.6269** | POSTURE, BLUFF, FRONT, INHALE                                     | INCORRECT (Max overlap: 3/4 with POSE)
   - Group 12: **0.4654** | MASQUERADE, WEDDING, PARTY HAT, SCARF                             | INCORRECT (Max overlap: 1/4 with POSE)
   - Group 13: **0.4929** | BOLT, BLUFF, VOLCANO, GORGE                                       | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 14: **0.4726** | FRONT, INHALE, CONE, SCARF                                        | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 15: **0.6136** | POSTURE, BOLT, FRONT, INHALE                                      | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 16: **0.5896** | POSTURE, FRONT, INHALE, GORGE                                     | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 17: **0.5011** | FRONT, CONE, GORGE, SCARF                                         | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 18: **0.4654** | BOLT, BLUFF, VOLCANO, INHALE                                      | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 19: **0.4932** | POSTURE, MASQUERADE, WEDDING, NEW YEAR'S EVE                      | INCORRECT (Max overlap: 2/4 with POSE)
   - Group 20: **0.4887** | CHRISTMAS TREE, BLARNEY STONE, PARTY HAT, MISTLETOE               | INCORRECT (Max overlap: 2/4 with CONICAL THINGS)

---

## Puzzle 8 (ID: 925)
**Words on Board:** UNCONSCIOUS, DOWNFALL, LITTLE RED RIDING HOOD, SOFT SPOT, OEDIPUS COMPLEX, DRACULA, DARTH VADER, LINKLATER, BRATZ, FRANKENSTEIN, SUPEREGO, FIXATION, SUPERMAN, DOGMA, ACHILLES’ HEEL, KRYPTONITE

### Ground Truth Categories:
* **Level 0 (VULNERABILITY) [Type: SYNONYM_OR_NEAR]:** ACHILLES’ HEEL, DOWNFALL, KRYPTONITE, SOFT SPOT
* **Level 1 (FREUDIAN CONCEPTS) [Type: SEMANTIC_SET]:** FIXATION, OEDIPUS COMPLEX, SUPEREGO, UNCONSCIOUS
* **Level 2 (CHARACTERS IN CAPES) [Type: NAMED_ENTITY_SET]:** DARTH VADER, DRACULA, LITTLE RED RIDING HOOD, SUPERMAN
* **Level 3 (STARTING WITH SLANG FOR SAUSAGE) [Type: WORDPLAY_TRANSFORM]:** BRATZ, DOGMA, FRANKENSTEIN, LINKLATER

### Top Candidate Partitions:
1. **Partition Score: 0.4967**
   - Group 1: **0.5339** | LITTLE RED RIDING HOOD, DARTH VADER, LINKLATER, BRATZ             | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 2: **0.5088** | DRACULA, FRANKENSTEIN, SUPERMAN, KRYPTONITE                       | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 3: **0.4933** | UNCONSCIOUS, OEDIPUS COMPLEX, SUPEREGO, FIXATION                  | CORRECT GROUP (FREUDIAN CONCEPTS, Level 1)
   - Group 4: **0.4923** | DOWNFALL, SOFT SPOT, DOGMA, ACHILLES’ HEEL                        | INCORRECT (Max overlap: 3/4 with VULNERABILITY)
2. **Partition Score: 0.4961**
   - Group 1: **0.5339** | LITTLE RED RIDING HOOD, DARTH VADER, LINKLATER, BRATZ             | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 2: **0.5088** | DRACULA, FRANKENSTEIN, SUPERMAN, KRYPTONITE                       | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 3: **0.5036** | DOWNFALL, SUPEREGO, DOGMA, ACHILLES’ HEEL                         | INCORRECT (Max overlap: 2/4 with VULNERABILITY)
   - Group 4: **0.4860** | UNCONSCIOUS, SOFT SPOT, OEDIPUS COMPLEX, FIXATION                 | INCORRECT (Max overlap: 3/4 with FREUDIAN CONCEPTS)
3. **Partition Score: 0.4959**
   - Group 1: **0.5132** | DRACULA, LINKLATER, FRANKENSTEIN, SUPERMAN                        | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 2: **0.5058** | LITTLE RED RIDING HOOD, DARTH VADER, BRATZ, KRYPTONITE            | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 3: **0.4933** | UNCONSCIOUS, OEDIPUS COMPLEX, SUPEREGO, FIXATION                  | CORRECT GROUP (FREUDIAN CONCEPTS, Level 1)
   - Group 4: **0.4923** | DOWNFALL, SOFT SPOT, DOGMA, ACHILLES’ HEEL                        | INCORRECT (Max overlap: 3/4 with VULNERABILITY)
4. **Partition Score: 0.4954**
   - Group 1: **0.5132** | DRACULA, LINKLATER, FRANKENSTEIN, SUPERMAN                        | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 2: **0.5058** | LITTLE RED RIDING HOOD, DARTH VADER, BRATZ, KRYPTONITE            | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 3: **0.5036** | DOWNFALL, SUPEREGO, DOGMA, ACHILLES’ HEEL                         | INCORRECT (Max overlap: 2/4 with VULNERABILITY)
   - Group 4: **0.4860** | UNCONSCIOUS, SOFT SPOT, OEDIPUS COMPLEX, FIXATION                 | INCORRECT (Max overlap: 3/4 with FREUDIAN CONCEPTS)
5. **Partition Score: 0.4942**
   - Group 1: **0.5034** | LITTLE RED RIDING HOOD, LINKLATER, BRATZ, KRYPTONITE              | INCORRECT (Max overlap: 2/4 with STARTING WITH SLANG FOR SAUSAGE)
   - Group 2: **0.4989** | DRACULA, DARTH VADER, FRANKENSTEIN, SUPERMAN                      | INCORRECT (Max overlap: 3/4 with CHARACTERS IN CAPES)
   - Group 3: **0.4933** | UNCONSCIOUS, OEDIPUS COMPLEX, SUPEREGO, FIXATION                  | CORRECT GROUP (FREUDIAN CONCEPTS, Level 1)
   - Group 4: **0.4923** | DOWNFALL, SOFT SPOT, DOGMA, ACHILLES’ HEEL                        | INCORRECT (Max overlap: 3/4 with VULNERABILITY)

### Top Candidate Groups:
   - Group 1: **0.5339** | LITTLE RED RIDING HOOD, DARTH VADER, LINKLATER, BRATZ             | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 2: **0.5088** | DRACULA, FRANKENSTEIN, SUPERMAN, KRYPTONITE                       | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 3: **0.4933** | UNCONSCIOUS, OEDIPUS COMPLEX, SUPEREGO, FIXATION                  | CORRECT GROUP (FREUDIAN CONCEPTS, Level 1)
   - Group 4: **0.4923** | DOWNFALL, SOFT SPOT, DOGMA, ACHILLES’ HEEL                        | INCORRECT (Max overlap: 3/4 with VULNERABILITY)
   - Group 5: **0.5036** | DOWNFALL, SUPEREGO, DOGMA, ACHILLES’ HEEL                         | INCORRECT (Max overlap: 2/4 with VULNERABILITY)
   - Group 6: **0.4860** | UNCONSCIOUS, SOFT SPOT, OEDIPUS COMPLEX, FIXATION                 | INCORRECT (Max overlap: 3/4 with FREUDIAN CONCEPTS)
   - Group 7: **0.5132** | DRACULA, LINKLATER, FRANKENSTEIN, SUPERMAN                        | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 8: **0.5058** | LITTLE RED RIDING HOOD, DARTH VADER, BRATZ, KRYPTONITE            | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 9: **0.5034** | LITTLE RED RIDING HOOD, LINKLATER, BRATZ, KRYPTONITE              | INCORRECT (Max overlap: 2/4 with STARTING WITH SLANG FOR SAUSAGE)
   - Group 10: **0.4989** | DRACULA, DARTH VADER, FRANKENSTEIN, SUPERMAN                      | INCORRECT (Max overlap: 3/4 with CHARACTERS IN CAPES)
   - Group 11: **0.5431** | LITTLE RED RIDING HOOD, DRACULA, DARTH VADER, BRATZ               | INCORRECT (Max overlap: 3/4 with CHARACTERS IN CAPES)
   - Group 12: **0.4818** | LINKLATER, FRANKENSTEIN, SUPERMAN, KRYPTONITE                     | INCORRECT (Max overlap: 2/4 with STARTING WITH SLANG FOR SAUSAGE)
   - Group 13: **0.5021** | DARTH VADER, LINKLATER, FRANKENSTEIN, SUPERMAN                    | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 14: **0.4819** | LITTLE RED RIDING HOOD, DRACULA, BRATZ, KRYPTONITE                | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 15: **0.4952** | DRACULA, DARTH VADER, LINKLATER, FRANKENSTEIN                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 16: **0.4815** | LITTLE RED RIDING HOOD, BRATZ, SUPERMAN, KRYPTONITE               | INCORRECT (Max overlap: 2/4 with CHARACTERS IN CAPES)
   - Group 17: **0.4857** | UNCONSCIOUS, OEDIPUS COMPLEX, FIXATION, DOGMA                     | INCORRECT (Max overlap: 3/4 with FREUDIAN CONCEPTS)
   - Group 18: **0.4764** | DOWNFALL, SOFT SPOT, SUPEREGO, ACHILLES’ HEEL                     | INCORRECT (Max overlap: 3/4 with VULNERABILITY)
   - Group 19: **0.5331** | LITTLE RED RIDING HOOD, DRACULA, BRATZ, SUPERMAN                  | INCORRECT (Max overlap: 3/4 with CHARACTERS IN CAPES)
   - Group 20: **0.4787** | DARTH VADER, LINKLATER, FRANKENSTEIN, KRYPTONITE                  | INCORRECT (Max overlap: 2/4 with STARTING WITH SLANG FOR SAUSAGE)

---

## Puzzle 9 (ID: 1021)
**Words on Board:** PLANK, CALF RAISE, CRUNCH, CHICK FLICK, KIT KAT, ABSENCE, DEFICIT, WIRELESS, SPORTS, FRY COOK, JOLLY ROGER, PLUNGE, CANNON, PINCH, PUSH-UP, CROW'S NEST

### Ground Truth Categories:
* **Level 0 (SHORTAGE) [Type: SYNONYM_OR_NEAR]:** ABSENCE, CRUNCH, DEFICIT, PINCH
* **Level 1 (PARTS OF A PIRATE SHIP) [Type: SEMANTIC_SET]:** CANNON, CROW'S NEST, JOLLY ROGER, PLANK
* **Level 2 (KINDS OF BRAS) [Type: SEMANTIC_SET]:** PLUNGE, PUSH-UP, SPORTS, WIRELESS
* **Level 3 (STARTING WITH BABY ANIMALS) [Type: WORDPLAY_TRANSFORM]:** CALF RAISE, CHICK FLICK, FRY COOK, KIT KAT

### Top Candidate Partitions:
1. **Partition Score: 0.4752**
   - Group 1: **0.5690** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
   - Group 2: **0.5048** | CHICK FLICK, FRY COOK, JOLLY ROGER, CROW'S NEST                   | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 3: **0.4767** | KIT KAT, WIRELESS, SPORTS, CANNON                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
   - Group 4: **0.4597** | PLANK, CALF RAISE, PLUNGE, PUSH-UP                                | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
2. **Partition Score: 0.4734**
   - Group 1: **0.5690** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
   - Group 2: **0.5507** | CHICK FLICK, KIT KAT, JOLLY ROGER, CROW'S NEST                    | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 3: **0.4597** | PLANK, CALF RAISE, PLUNGE, PUSH-UP                                | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
   - Group 4: **0.4415** | WIRELESS, SPORTS, FRY COOK, CANNON                                | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
3. **Partition Score: 0.4699**
   - Group 1: **0.5048** | CHICK FLICK, FRY COOK, JOLLY ROGER, CROW'S NEST                   | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 2: **0.4953** | ABSENCE, DEFICIT, PLUNGE, PINCH                                   | INCORRECT (Max overlap: 3/4 with SHORTAGE)
   - Group 3: **0.4767** | KIT KAT, WIRELESS, SPORTS, CANNON                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
   - Group 4: **0.4537** | PLANK, CALF RAISE, CRUNCH, PUSH-UP                                | INCORRECT (Max overlap: 1/4 with PARTS OF A PIRATE SHIP)
4. **Partition Score: 0.4652**
   - Group 1: **0.5690** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
   - Group 2: **0.5499** | KIT KAT, FRY COOK, JOLLY ROGER, CROW'S NEST                       | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 3: **0.4381** | CALF RAISE, CHICK FLICK, PLUNGE, PUSH-UP                          | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 4: **0.4364** | PLANK, WIRELESS, SPORTS, CANNON                                   | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)
5. **Partition Score: 0.4594**
   - Group 1: **0.5680** | CRUNCH, DEFICIT, PLUNGE, PINCH                                    | INCORRECT (Max overlap: 3/4 with SHORTAGE)
   - Group 2: **0.5507** | CHICK FLICK, KIT KAT, JOLLY ROGER, CROW'S NEST                    | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 3: **0.4415** | WIRELESS, SPORTS, FRY COOK, CANNON                                | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
   - Group 4: **0.4227** | PLANK, CALF RAISE, ABSENCE, PUSH-UP                               | INCORRECT (Max overlap: 1/4 with PARTS OF A PIRATE SHIP)

### Top Candidate Groups:
   - Group 1: **0.5690** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
   - Group 2: **0.5048** | CHICK FLICK, FRY COOK, JOLLY ROGER, CROW'S NEST                   | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 3: **0.4767** | KIT KAT, WIRELESS, SPORTS, CANNON                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
   - Group 4: **0.4597** | PLANK, CALF RAISE, PLUNGE, PUSH-UP                                | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
   - Group 5: **0.5507** | CHICK FLICK, KIT KAT, JOLLY ROGER, CROW'S NEST                    | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 6: **0.4415** | WIRELESS, SPORTS, FRY COOK, CANNON                                | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
   - Group 7: **0.4953** | ABSENCE, DEFICIT, PLUNGE, PINCH                                   | INCORRECT (Max overlap: 3/4 with SHORTAGE)
   - Group 8: **0.4537** | PLANK, CALF RAISE, CRUNCH, PUSH-UP                                | INCORRECT (Max overlap: 1/4 with PARTS OF A PIRATE SHIP)
   - Group 9: **0.5499** | KIT KAT, FRY COOK, JOLLY ROGER, CROW'S NEST                       | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 10: **0.4381** | CALF RAISE, CHICK FLICK, PLUNGE, PUSH-UP                          | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 11: **0.4364** | PLANK, WIRELESS, SPORTS, CANNON                                   | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)
   - Group 12: **0.5680** | CRUNCH, DEFICIT, PLUNGE, PINCH                                    | INCORRECT (Max overlap: 3/4 with SHORTAGE)
   - Group 13: **0.4227** | PLANK, CALF RAISE, ABSENCE, PUSH-UP                               | INCORRECT (Max overlap: 1/4 with PARTS OF A PIRATE SHIP)
   - Group 14: **0.4587** | CALF RAISE, CRUNCH, DEFICIT, PINCH                                | INCORRECT (Max overlap: 3/4 with SHORTAGE)
   - Group 15: **0.4494** | PLANK, ABSENCE, PLUNGE, PUSH-UP                                   | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)
   - Group 16: **0.5188** | PLANK, DEFICIT, PLUNGE, PINCH                                     | INCORRECT (Max overlap: 2/4 with SHORTAGE)
   - Group 17: **0.4255** | CALF RAISE, CRUNCH, ABSENCE, PUSH-UP                              | INCORRECT (Max overlap: 2/4 with SHORTAGE)
   - Group 18: **0.5005** | PLANK, SPORTS, PLUNGE, PUSH-UP                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BRAS)
   - Group 19: **0.4497** | CALF RAISE, CHICK FLICK, JOLLY ROGER, CROW'S NEST                 | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 20: **0.4339** | KIT KAT, WIRELESS, FRY COOK, CANNON                               | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)

---

## Puzzle 10 (ID: 434)
**Words on Board:** NERD, GRUMP, RUNT, WHAT IF, SLEEP, SAY, DO, SNOOZE, ALARM, PERHAPS, DOPE, SUPPOSE, TIME SET, KISS, HOUR, WHOPPER

### Ground Truth Categories:
* **Level 0 (ALARM CLOCK BUTTONS) [Type: SEMANTIC_SET]:** ALARM, HOUR, SNOOZE, TIME SET
* **Level 1 (“HERE’S A THOUGHT ...”) [Type: SYNONYM_OR_NEAR]:** PERHAPS, SAY, SUPPOSE, WHAT IF
* **Level 2 (CANDY PIECES) [Type: NAMED_ENTITY_SET]:** KISS, NERD, RUNT, WHOPPER
* **Level 3 (SEVEN DWARFS MINUS LAST LETTER) [Type: WORDPLAY_TRANSFORM]:** DO, DOPE, GRUMP, SLEEP

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6548** | SLEEP, SNOOZE, ALARM, HOUR                                        | INCORRECT (Max overlap: 3/4 with ALARM CLOCK BUTTONS)
   - Group 2: **0.6141** | SNOOZE, ALARM, TIME SET, HOUR                                     | CORRECT GROUP (ALARM CLOCK BUTTONS, Level 0)
   - Group 3: **0.6080** | SLEEP, SNOOZE, ALARM, TIME SET                                    | INCORRECT (Max overlap: 3/4 with ALARM CLOCK BUTTONS)
   - Group 4: **0.6059** | SLEEP, SNOOZE, TIME SET, HOUR                                     | INCORRECT (Max overlap: 3/4 with ALARM CLOCK BUTTONS)
   - Group 5: **0.5996** | SLEEP, ALARM, TIME SET, HOUR                                      | INCORRECT (Max overlap: 3/4 with ALARM CLOCK BUTTONS)
   - Group 6: **0.5853** | SLEEP, DO, SNOOZE, HOUR                                           | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 7: **0.5690** | NERD, GRUMP, RUNT, SNOOZE                                         | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 8: **0.5634** | SLEEP, DO, SNOOZE, ALARM                                          | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 9: **0.5626** | GRUMP, SLEEP, SNOOZE, ALARM                                       | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 10: **0.5479** | SLEEP, DO, ALARM, HOUR                                            | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 11: **0.5469** | GRUMP, SNOOZE, ALARM, TIME SET                                    | INCORRECT (Max overlap: 3/4 with ALARM CLOCK BUTTONS)
   - Group 12: **0.5449** | SLEEP, SNOOZE, ALARM, KISS                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 13: **0.5415** | DO, SNOOZE, TIME SET, HOUR                                        | INCORRECT (Max overlap: 3/4 with ALARM CLOCK BUTTONS)
   - Group 14: **0.5387** | NERD, GRUMP, SNOOZE, WHOPPER                                      | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 15: **0.5386** | RUNT, SLEEP, SNOOZE, ALARM                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 16: **0.5383** | SLEEP, DO, TIME SET, HOUR                                         | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 17: **0.5375** | DO, SNOOZE, DOPE, HOUR                                            | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 18: **0.5372** | SLEEP, DO, DOPE, HOUR                                             | INCORRECT (Max overlap: 3/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 19: **0.5357** | DO, DOPE, TIME SET, HOUR                                          | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 20: **0.5320** | GRUMP, RUNT, SNOOZE, ALARM                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)

---

## Puzzle 11 (ID: 622)
**Words on Board:** GLITTER, GOOSE, PAPER, CELTIC, PACKER, CURL, YANKEE, ROD, FEATHER, PARACHUTE, CRIMP, MACARONI, TEASE, DOODLE, CANADIEN, GLUE

### Ground Truth Categories:
* **Level 0 (MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS) [Type: NAMED_ENTITY_SET]:** CANADIEN, CELTIC, PACKER, YANKEE
* **Level 1 (CREATE SOME VOLUME/TEXTURE IN HAIR) [Type: SYNONYM_OR_NEAR]:** CRIMP, CURL, FEATHER, TEASE
* **Level 2 (SUPPLIES FOR MACARONI ART) [Type: SEMANTIC_SET]:** GLITTER, GLUE, MACARONI, PAPER
* **Level 3 (WORDS AFTER “GOLDEN”) [Type: FILL_IN_THE_BLANK]:** DOODLE, GOOSE, PARACHUTE, ROD

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6895** | GOOSE, CELTIC, YANKEE, DOODLE                                     | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 2: **0.6596** | GOOSE, CELTIC, YANKEE, FEATHER                                    | INCORRECT (Max overlap: 2/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 3: **0.6574** | GOOSE, CELTIC, PACKER, YANKEE                                     | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 4: **0.6379** | GOOSE, YANKEE, FEATHER, DOODLE                                    | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 5: **0.6377** | GOOSE, YANKEE, ROD, DOODLE                                        | INCORRECT (Max overlap: 3/4 with WORDS AFTER “GOLDEN”)
   - Group 6: **0.6363** | GOOSE, CELTIC, FEATHER, DOODLE                                    | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 7: **0.6244** | GOOSE, PAPER, CELTIC, FEATHER                                     | INCORRECT (Max overlap: 1/4 with WORDS AFTER “GOLDEN”)
   - Group 8: **0.6217** | GOOSE, PAPER, FEATHER, DOODLE                                     | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 9: **0.6203** | GOOSE, CELTIC, PACKER, FEATHER                                    | INCORRECT (Max overlap: 2/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 10: **0.6202** | GOOSE, PAPER, YANKEE, DOODLE                                      | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 11: **0.6156** | CELTIC, PACKER, YANKEE, FEATHER                                   | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 12: **0.6137** | GOOSE, PACKER, YANKEE, ROD                                        | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 13: **0.6101** | GOOSE, PAPER, YANKEE, FEATHER                                     | INCORRECT (Max overlap: 1/4 with WORDS AFTER “GOLDEN”)
   - Group 14: **0.6070** | CELTIC, YANKEE, FEATHER, DOODLE                                   | INCORRECT (Max overlap: 2/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 15: **0.6032** | GOOSE, PAPER, FEATHER, GLUE                                       | INCORRECT (Max overlap: 2/4 with SUPPLIES FOR MACARONI ART)
   - Group 16: **0.6027** | GLITTER, GOOSE, CELTIC, FEATHER                                   | INCORRECT (Max overlap: 1/4 with SUPPLIES FOR MACARONI ART)
   - Group 17: **0.6025** | GOOSE, PACKER, YANKEE, FEATHER                                    | INCORRECT (Max overlap: 2/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 18: **0.6020** | GOOSE, CELTIC, FEATHER, PARACHUTE                                 | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 19: **0.6004** | GLITTER, PAPER, FEATHER, GLUE                                     | INCORRECT (Max overlap: 3/4 with SUPPLIES FOR MACARONI ART)
   - Group 20: **0.5987** | GOOSE, PACKER, YANKEE, DOODLE                                     | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)

---

## Puzzle 12 (ID: 541)
**Words on Board:** OSCAR, CUZ, CECE, JUNIOR, EDIE, EMMY, TONY, COUNT, GRAMMY, COOKIE, KATIE, MEADOW, MUMMY, POP, CARMELA, SNUFFY

### Ground Truth Categories:
* **Level 0 (SOPRANOS) [Type: NAMED_ENTITY_SET]:** CARMELA, JUNIOR, MEADOW, TONY
* **Level 1 (FAMILIAL NICKNAMES) [Type: SYNONYM_OR_NEAR]:** CUZ, GRAMMY, MUMMY, POP
* **Level 2 (“SESAME STREET” CHARACTERS) [Type: NAMED_ENTITY_SET]:** COOKIE, COUNT, OSCAR, SNUFFY
* **Level 3 (NAMES THAT SOUND LIKE TWO LETTERS) [Type: SOUND_OR_SPELLING]:** CECE, EDIE, EMMY, KATIE

### Top Candidate Partitions:
1. **Partition Score: 0.5196**
   - Group 1: **0.5867** | OSCAR, EDIE, EMMY, GRAMMY                                         | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 2: **0.5382** | CECE, TONY, CARMELA, SNUFFY                                       | INCORRECT (Max overlap: 2/4 with SOPRANOS)
   - Group 3: **0.5146** | KATIE, MEADOW, MUMMY, POP                                         | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 4: **0.5128** | CUZ, JUNIOR, COUNT, COOKIE                                        | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
2. **Partition Score: 0.5150**
   - Group 1: **0.5668** | OSCAR, EMMY, TONY, GRAMMY                                         | INCORRECT (Max overlap: 1/4 with “SESAME STREET” CHARACTERS)
   - Group 2: **0.5200** | CECE, EDIE, CARMELA, SNUFFY                                       | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 3: **0.5146** | KATIE, MEADOW, MUMMY, POP                                         | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 4: **0.5128** | CUZ, JUNIOR, COUNT, COOKIE                                        | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
3. **Partition Score: 0.5096**
   - Group 1: **0.5382** | CECE, TONY, CARMELA, SNUFFY                                       | INCORRECT (Max overlap: 2/4 with SOPRANOS)
   - Group 2: **0.5344** | EDIE, KATIE, MEADOW, MUMMY                                        | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 3: **0.5128** | CUZ, JUNIOR, COUNT, COOKIE                                        | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 4: **0.4957** | OSCAR, EMMY, GRAMMY, POP                                          | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
4. **Partition Score: 0.5073**
   - Group 1: **0.5210** | OSCAR, EMMY, GRAMMY, MUMMY                                        | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 2: **0.5200** | CECE, EDIE, CARMELA, SNUFFY                                       | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 3: **0.5128** | CUZ, JUNIOR, COUNT, COOKIE                                        | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 4: **0.4982** | TONY, KATIE, MEADOW, POP                                          | INCORRECT (Max overlap: 2/4 with SOPRANOS)
5. **Partition Score: 0.5061**
   - Group 1: **0.5382** | CECE, TONY, CARMELA, SNUFFY                                       | INCORRECT (Max overlap: 2/4 with SOPRANOS)
   - Group 2: **0.5128** | CUZ, JUNIOR, COUNT, COOKIE                                        | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 3: **0.5121** | OSCAR, KATIE, MUMMY, POP                                          | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 4: **0.4997** | EDIE, EMMY, GRAMMY, MEADOW                                        | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)

### Top Candidate Groups:
   - Group 1: **0.5867** | OSCAR, EDIE, EMMY, GRAMMY                                         | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 2: **0.5382** | CECE, TONY, CARMELA, SNUFFY                                       | INCORRECT (Max overlap: 2/4 with SOPRANOS)
   - Group 3: **0.5146** | KATIE, MEADOW, MUMMY, POP                                         | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 4: **0.5128** | CUZ, JUNIOR, COUNT, COOKIE                                        | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 5: **0.5668** | OSCAR, EMMY, TONY, GRAMMY                                         | INCORRECT (Max overlap: 1/4 with “SESAME STREET” CHARACTERS)
   - Group 6: **0.5200** | CECE, EDIE, CARMELA, SNUFFY                                       | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 7: **0.5344** | EDIE, KATIE, MEADOW, MUMMY                                        | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 8: **0.4957** | OSCAR, EMMY, GRAMMY, POP                                          | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 9: **0.5210** | OSCAR, EMMY, GRAMMY, MUMMY                                        | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 10: **0.4982** | TONY, KATIE, MEADOW, POP                                          | INCORRECT (Max overlap: 2/4 with SOPRANOS)
   - Group 11: **0.5121** | OSCAR, KATIE, MUMMY, POP                                          | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 12: **0.4997** | EDIE, EMMY, GRAMMY, MEADOW                                        | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 13: **0.5172** | TONY, KATIE, MEADOW, MUMMY                                        | INCORRECT (Max overlap: 2/4 with SOPRANOS)
   - Group 14: **0.5630** | CECE, KATIE, CARMELA, SNUFFY                                      | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 15: **0.5013** | OSCAR, TONY, MUMMY, POP                                           | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 16: **0.5029** | CECE, EDIE, TONY, SNUFFY                                          | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 17: **0.4977** | OSCAR, EMMY, GRAMMY, CARMELA                                      | INCORRECT (Max overlap: 1/4 with “SESAME STREET” CHARACTERS)
   - Group 18: **0.4975** | EMMY, GRAMMY, KATIE, MEADOW                                       | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 19: **0.4978** | EDIE, TONY, MEADOW, MUMMY                                         | INCORRECT (Max overlap: 2/4 with SOPRANOS)
   - Group 20: **0.5084** | CECE, EDIE, EMMY, GRAMMY                                          | INCORRECT (Max overlap: 3/4 with NAMES THAT SOUND LIKE TWO LETTERS)

---

## Puzzle 13 (ID: 1005)
**Words on Board:** SPORK, FROG, CORNER, SPROCKET, SMOG, BOGART, MONOPOLIZE, HOG, GEAR, COG, MOTEL, DOZE, BLOG, PINION, DOG, HORN

### Ground Truth Categories:
* **Level 0 (GREEDILY CONTROL) [Type: SYNONYM_OR_NEAR]:** BOGART, CORNER, HOG, MONOPOLIZE
* **Level 1 (TOOTHED WHEELS) [Type: SEMANTIC_SET]:** COG, GEAR, PINION, SPROCKET
* **Level 2 (PORTMANTEAUX) [Type: WORDPLAY_TRANSFORM]:** BLOG, MOTEL, SMOG, SPORK
* **Level 3 (BULL___) [Type: FILL_IN_THE_BLANK]:** DOG, DOZE, FROG, HORN

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7831** | SPROCKET, GEAR, COG, PINION                                       | CORRECT GROUP (TOOTHED WHEELS, Level 1)
   - Group 2: **0.7044** | CORNER, SPROCKET, GEAR, COG                                       | INCORRECT (Max overlap: 3/4 with TOOTHED WHEELS)
   - Group 3: **0.6966** | FROG, HOG, DOG, HORN                                              | INCORRECT (Max overlap: 3/4 with BULL___)
   - Group 4: **0.6908** | CORNER, SPROCKET, GEAR, PINION                                    | INCORRECT (Max overlap: 3/4 with TOOTHED WHEELS)
   - Group 5: **0.6517** | FROG, HOG, BLOG, DOG                                              | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 6: **0.6478** | SPORK, FROG, SMOG, BLOG                                           | INCORRECT (Max overlap: 3/4 with PORTMANTEAUX)
   - Group 7: **0.6460** | CORNER, GEAR, COG, PINION                                         | INCORRECT (Max overlap: 3/4 with TOOTHED WHEELS)
   - Group 8: **0.6358** | HOG, DOZE, DOG, HORN                                              | INCORRECT (Max overlap: 3/4 with BULL___)
   - Group 9: **0.6319** | FROG, BOGART, HOG, DOG                                            | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 10: **0.6267** | FROG, HOG, DOZE, HORN                                             | INCORRECT (Max overlap: 3/4 with BULL___)
   - Group 11: **0.6264** | FROG, HOG, DOZE, DOG                                              | INCORRECT (Max overlap: 3/4 with BULL___)
   - Group 12: **0.6166** | FROG, DOZE, DOG, HORN                                             | CORRECT GROUP (BULL___, Level 3)
   - Group 13: **0.6123** | FROG, BOGART, HOG, BLOG                                           | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
   - Group 14: **0.6090** | SPORK, FROG, DOZE, BLOG                                           | INCORRECT (Max overlap: 2/4 with PORTMANTEAUX)
   - Group 15: **0.6058** | FROG, DOZE, BLOG, DOG                                             | INCORRECT (Max overlap: 3/4 with BULL___)
   - Group 16: **0.6028** | SPORK, FROG, HOG, DOG                                             | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 17: **0.6008** | SPORK, FROG, BLOG, DOG                                            | INCORRECT (Max overlap: 2/4 with PORTMANTEAUX)
   - Group 18: **0.6001** | FROG, SMOG, BOGART, BLOG                                          | INCORRECT (Max overlap: 2/4 with PORTMANTEAUX)
   - Group 19: **0.5998** | BOGART, HOG, BLOG, DOG                                            | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
   - Group 20: **0.5954** | CORNER, SPROCKET, COG, PINION                                     | INCORRECT (Max overlap: 3/4 with TOOTHED WHEELS)

---

## Puzzle 14 (ID: 170)
**Words on Board:** ISLAND, CRAM, KEY, BAG, BEDROOM, ATOLL, KITCHEN, PACK, STUDY, DEN, SPROUT, BAR, JAM, COUNTER, DIP, STUFF

### Ground Truth Categories:
* **Level 0 (ROOMS IN A HOUSE) [Type: SEMANTIC_SET]:** BEDROOM, DEN, KITCHEN, STUDY
* **Level 1 (LAND SURROUNDED BY WATER) [Type: SEMANTIC_SET]:** ATOLL, BAR, ISLAND, KEY
* **Level 2 (FILL TO EXCESS) [Type: SYNONYM_OR_NEAR]:** CRAM, JAM, PACK, STUFF
* **Level 3 (BEAN ___) [Type: FILL_IN_THE_BLANK]:** BAG, COUNTER, DIP, SPROUT

### Top Candidate Partitions:
1. **Partition Score: 0.4993**
   - Group 1: **0.5292** | CRAM, STUDY, JAM, STUFF                                           | INCORRECT (Max overlap: 3/4 with FILL TO EXCESS)
   - Group 2: **0.5220** | BAG, PACK, SPROUT, DIP                                            | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 3: **0.5025** | ISLAND, KEY, ATOLL, KITCHEN                                       | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER)
   - Group 4: **0.4863** | BEDROOM, DEN, BAR, COUNTER                                        | INCORRECT (Max overlap: 2/4 with ROOMS IN A HOUSE)
2. **Partition Score: 0.4939**
   - Group 1: **0.5292** | CRAM, STUDY, JAM, STUFF                                           | INCORRECT (Max overlap: 3/4 with FILL TO EXCESS)
   - Group 2: **0.5220** | BAG, PACK, SPROUT, DIP                                            | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 3: **0.4850** | ISLAND, KEY, BAR, COUNTER                                         | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER)
   - Group 4: **0.4843** | BEDROOM, ATOLL, KITCHEN, DEN                                      | INCORRECT (Max overlap: 3/4 with ROOMS IN A HOUSE)
3. **Partition Score: 0.4869**
   - Group 1: **0.5292** | CRAM, STUDY, JAM, STUFF                                           | INCORRECT (Max overlap: 3/4 with FILL TO EXCESS)
   - Group 2: **0.5121** | ISLAND, BEDROOM, ATOLL, KITCHEN                                   | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 3: **0.5101** | BAG, DEN, SPROUT, DIP                                             | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 4: **0.4626** | KEY, PACK, BAR, COUNTER                                           | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
4. **Partition Score: 0.4801**
   - Group 1: **0.5292** | CRAM, STUDY, JAM, STUFF                                           | INCORRECT (Max overlap: 3/4 with FILL TO EXCESS)
   - Group 2: **0.5220** | BAG, PACK, SPROUT, DIP                                            | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 3: **0.4779** | KEY, BEDROOM, BAR, COUNTER                                        | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 4: **0.4602** | ISLAND, ATOLL, KITCHEN, DEN                                       | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
5. **Partition Score: 0.4795**
   - Group 1: **0.5292** | CRAM, STUDY, JAM, STUFF                                           | INCORRECT (Max overlap: 3/4 with FILL TO EXCESS)
   - Group 2: **0.5220** | BAG, PACK, SPROUT, DIP                                            | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 3: **0.5121** | ISLAND, BEDROOM, ATOLL, KITCHEN                                   | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 4: **0.4420** | KEY, DEN, BAR, COUNTER                                            | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)

### Top Candidate Groups:
   - Group 1: **0.5292** | CRAM, STUDY, JAM, STUFF                                           | INCORRECT (Max overlap: 3/4 with FILL TO EXCESS)
   - Group 2: **0.5220** | BAG, PACK, SPROUT, DIP                                            | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 3: **0.5025** | ISLAND, KEY, ATOLL, KITCHEN                                       | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER)
   - Group 4: **0.4863** | BEDROOM, DEN, BAR, COUNTER                                        | INCORRECT (Max overlap: 2/4 with ROOMS IN A HOUSE)
   - Group 5: **0.4850** | ISLAND, KEY, BAR, COUNTER                                         | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER)
   - Group 6: **0.4843** | BEDROOM, ATOLL, KITCHEN, DEN                                      | INCORRECT (Max overlap: 3/4 with ROOMS IN A HOUSE)
   - Group 7: **0.5121** | ISLAND, BEDROOM, ATOLL, KITCHEN                                   | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 8: **0.5101** | BAG, DEN, SPROUT, DIP                                             | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 9: **0.4626** | KEY, PACK, BAR, COUNTER                                           | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 10: **0.4779** | KEY, BEDROOM, BAR, COUNTER                                        | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 11: **0.4602** | ISLAND, ATOLL, KITCHEN, DEN                                       | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 12: **0.4420** | KEY, DEN, BAR, COUNTER                                            | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 13: **0.5899** | ISLAND, BEDROOM, KITCHEN, DEN                                     | INCORRECT (Max overlap: 3/4 with ROOMS IN A HOUSE)
   - Group 14: **0.4327** | KEY, ATOLL, BAR, COUNTER                                          | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER)
   - Group 15: **0.5036** | KITCHEN, DEN, BAR, COUNTER                                        | INCORRECT (Max overlap: 2/4 with ROOMS IN A HOUSE)
   - Group 16: **0.4452** | ISLAND, KEY, BEDROOM, ATOLL                                       | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER)
   - Group 17: **0.5475** | BEDROOM, KITCHEN, BAR, COUNTER                                    | INCORRECT (Max overlap: 2/4 with ROOMS IN A HOUSE)
   - Group 18: **0.4189** | ISLAND, KEY, ATOLL, DEN                                           | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER)
   - Group 19: **0.5198** | KEY, KITCHEN, BAR, COUNTER                                        | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 20: **0.4225** | ISLAND, BEDROOM, ATOLL, DEN                                       | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)

---

## Puzzle 15 (ID: 563)
**Words on Board:** JENNY, RUDOLPH, ROBIN HOOD, FEY, STRONG, CUPID, VIXEN, SAGITTARIUS, STAR, SHANNON, HAWKEYE, MOON, PLANET, COMET, QUEEN, NANNY

### Ground Truth Categories:
* **Level 0 (CELESTIAL OBJECTS) [Type: SEMANTIC_SET]:** COMET, MOON, PLANET, STAR
* **Level 1 (ARCHERS) [Type: NAMED_ENTITY_SET]:** CUPID, HAWKEYE, ROBIN HOOD, SAGITTARIUS
* **Level 2 (FEMALE ANIMALS) [Type: SEMANTIC_SET]:** JENNY, NANNY, QUEEN, VIXEN
* **Level 3 (“S.N.L.” CAST MEMBERS) [Type: NAMED_ENTITY_SET]:** FEY, RUDOLPH, SHANNON, STRONG

### Top Candidate Partitions:
1. **Partition Score: 0.4795**
   - Group 1: **0.5770** | VIXEN, STAR, PLANET, COMET                                        | INCORRECT (Max overlap: 3/4 with CELESTIAL OBJECTS)
   - Group 2: **0.5087** | JENNY, ROBIN HOOD, FEY, QUEEN                                     | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 3: **0.4740** | SAGITTARIUS, SHANNON, HAWKEYE, NANNY                              | INCORRECT (Max overlap: 2/4 with ARCHERS)
   - Group 4: **0.4675** | RUDOLPH, STRONG, CUPID, MOON                                      | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS)
2. **Partition Score: 0.4764**
   - Group 1: **0.5770** | VIXEN, STAR, PLANET, COMET                                        | INCORRECT (Max overlap: 3/4 with CELESTIAL OBJECTS)
   - Group 2: **0.5284** | JENNY, FEY, QUEEN, NANNY                                          | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS)
   - Group 3: **0.4675** | RUDOLPH, STRONG, CUPID, MOON                                      | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS)
   - Group 4: **0.4549** | ROBIN HOOD, SAGITTARIUS, SHANNON, HAWKEYE                         | INCORRECT (Max overlap: 3/4 with ARCHERS)
3. **Partition Score: 0.4736**
   - Group 1: **0.5770** | VIXEN, STAR, PLANET, COMET                                        | INCORRECT (Max overlap: 3/4 with CELESTIAL OBJECTS)
   - Group 2: **0.5017** | SAGITTARIUS, SHANNON, QUEEN, NANNY                                | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 3: **0.4675** | RUDOLPH, STRONG, CUPID, MOON                                      | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS)
   - Group 4: **0.4626** | JENNY, ROBIN HOOD, FEY, HAWKEYE                                   | INCORRECT (Max overlap: 2/4 with ARCHERS)
4. **Partition Score: 0.4717**
   - Group 1: **0.5770** | VIXEN, STAR, PLANET, COMET                                        | INCORRECT (Max overlap: 3/4 with CELESTIAL OBJECTS)
   - Group 2: **0.4850** | JENNY, SAGITTARIUS, QUEEN, NANNY                                  | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS)
   - Group 3: **0.4675** | RUDOLPH, STRONG, CUPID, MOON                                      | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS)
   - Group 4: **0.4671** | ROBIN HOOD, FEY, SHANNON, HAWKEYE                                 | INCORRECT (Max overlap: 2/4 with ARCHERS)
5. **Partition Score: 0.4715**
   - Group 1: **0.5770** | VIXEN, STAR, PLANET, COMET                                        | INCORRECT (Max overlap: 3/4 with CELESTIAL OBJECTS)
   - Group 2: **0.5455** | JENNY, FEY, SHANNON, QUEEN                                        | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 3: **0.4675** | RUDOLPH, STRONG, CUPID, MOON                                      | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS)
   - Group 4: **0.4364** | ROBIN HOOD, SAGITTARIUS, HAWKEYE, NANNY                           | INCORRECT (Max overlap: 3/4 with ARCHERS)

### Top Candidate Groups:
   - Group 1: **0.5770** | VIXEN, STAR, PLANET, COMET                                        | INCORRECT (Max overlap: 3/4 with CELESTIAL OBJECTS)
   - Group 2: **0.5087** | JENNY, ROBIN HOOD, FEY, QUEEN                                     | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 3: **0.4740** | SAGITTARIUS, SHANNON, HAWKEYE, NANNY                              | INCORRECT (Max overlap: 2/4 with ARCHERS)
   - Group 4: **0.4675** | RUDOLPH, STRONG, CUPID, MOON                                      | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS)
   - Group 5: **0.5284** | JENNY, FEY, QUEEN, NANNY                                          | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS)
   - Group 6: **0.4549** | ROBIN HOOD, SAGITTARIUS, SHANNON, HAWKEYE                         | INCORRECT (Max overlap: 3/4 with ARCHERS)
   - Group 7: **0.5017** | SAGITTARIUS, SHANNON, QUEEN, NANNY                                | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 8: **0.4626** | JENNY, ROBIN HOOD, FEY, HAWKEYE                                   | INCORRECT (Max overlap: 2/4 with ARCHERS)
   - Group 9: **0.4850** | JENNY, SAGITTARIUS, QUEEN, NANNY                                  | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS)
   - Group 10: **0.4671** | ROBIN HOOD, FEY, SHANNON, HAWKEYE                                 | INCORRECT (Max overlap: 2/4 with ARCHERS)
   - Group 11: **0.5455** | JENNY, FEY, SHANNON, QUEEN                                        | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 12: **0.4364** | ROBIN HOOD, SAGITTARIUS, HAWKEYE, NANNY                           | INCORRECT (Max overlap: 3/4 with ARCHERS)
   - Group 13: **0.4755** | JENNY, ROBIN HOOD, FEY, NANNY                                     | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 14: **0.4645** | SAGITTARIUS, SHANNON, HAWKEYE, QUEEN                              | INCORRECT (Max overlap: 2/4 with ARCHERS)
   - Group 15: **0.4610** | ROBIN HOOD, CUPID, SAGITTARIUS, HAWKEYE                           | CORRECT GROUP (ARCHERS, Level 1)
   - Group 16: **0.4298** | RUDOLPH, STRONG, MOON, NANNY                                      | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS)
   - Group 17: **0.5107** | RUDOLPH, ROBIN HOOD, CUPID, HAWKEYE                               | INCORRECT (Max overlap: 3/4 with ARCHERS)
   - Group 18: **0.4914** | JENNY, FEY, SHANNON, NANNY                                        | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 19: **0.4318** | STRONG, SAGITTARIUS, MOON, QUEEN                                  | INCORRECT (Max overlap: 1/4 with “S.N.L.” CAST MEMBERS)
   - Group 20: **0.4524** | ROBIN HOOD, SAGITTARIUS, HAWKEYE, QUEEN                           | INCORRECT (Max overlap: 3/4 with ARCHERS)

---

## Puzzle 16 (ID: 487)
**Words on Board:** DOE, HER, EYE, ELF, TEA, RAD, ILL, LEG, BIG, SEW, BAD, HIP, ARM, FAR, FLY, SAW

### Ground Truth Categories:
* **Level 0 (BODY PARTS) [Type: SEMANTIC_SET]:** ARM, EYE, HIP, LEG
* **Level 1 (COOL, IN ’80S SLANG) [Type: SYNONYM_OR_NEAR]:** BAD, FLY, ILL, RAD
* **Level 2 (MOVIES) [Type: NAMED_ENTITY_SET]:** BIG, ELF, HER, SAW
* **Level 3 (WORDS IN “DO-RE-MI”) [Type: SOUND_OR_SPELLING]:** DOE, FAR, SEW, TEA

### Top Candidate Partitions:
1. **Partition Score: 0.6151**
   - Group 1: **0.7037** | HER, EYE, TEA, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 2: **0.6435** | LEG, HIP, ARM, FLY                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)
   - Group 3: **0.6135** | DOE, ELF, RAD, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 4: **0.6018** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
2. **Partition Score: 0.6116**
   - Group 1: **0.6832** | DOE, HER, EYE, TEA                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 2: **0.6335** | ELF, RAD, FLY, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 3: **0.6093** | LEG, SEW, HIP, ARM                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)
   - Group 4: **0.6018** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
3. **Partition Score: 0.6115**
   - Group 1: **0.7147** | DOE, HER, TEA, SEW                                                | INCORRECT (Max overlap: 3/4 with WORDS IN “DO-RE-MI”)
   - Group 2: **0.6335** | ELF, RAD, FLY, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 3: **0.6090** | EYE, LEG, HIP, ARM                                                | CORRECT GROUP (BODY PARTS, Level 0)
   - Group 4: **0.6018** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
4. **Partition Score: 0.6105**
   - Group 1: **0.7037** | HER, EYE, TEA, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 2: **0.6240** | DOE, ELF, RAD, FLY                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 3: **0.6145** | LEG, HIP, ARM, SAW                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)
   - Group 4: **0.6018** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
5. **Partition Score: 0.6100**
   - Group 1: **0.7079** | HER, EYE, ELF, TEA                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 2: **0.6273** | DOE, RAD, FLY, SAW                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 3: **0.6093** | LEG, SEW, HIP, ARM                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)
   - Group 4: **0.6018** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)

### Top Candidate Groups:
   - Group 1: **0.7037** | HER, EYE, TEA, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 2: **0.6435** | LEG, HIP, ARM, FLY                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)
   - Group 3: **0.6135** | DOE, ELF, RAD, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 4: **0.6018** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 5: **0.6832** | DOE, HER, EYE, TEA                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 6: **0.6335** | ELF, RAD, FLY, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 7: **0.6093** | LEG, SEW, HIP, ARM                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)
   - Group 8: **0.7147** | DOE, HER, TEA, SEW                                                | INCORRECT (Max overlap: 3/4 with WORDS IN “DO-RE-MI”)
   - Group 9: **0.6090** | EYE, LEG, HIP, ARM                                                | CORRECT GROUP (BODY PARTS, Level 0)
   - Group 10: **0.6240** | DOE, ELF, RAD, FLY                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 11: **0.6145** | LEG, HIP, ARM, SAW                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)
   - Group 12: **0.7079** | HER, EYE, ELF, TEA                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 13: **0.6273** | DOE, RAD, FLY, SAW                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 14: **0.7482** | HER, ELF, TEA, SEW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 15: **0.6073** | ELF, LEG, HIP, ARM                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)
   - Group 16: **0.6348** | HER, TEA, SEW, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 17: **0.6618** | EYE, TEA, SEW, SAW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 18: **0.5948** | DOE, HER, ELF, RAD                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 19: **0.6964** | DOE, HER, EYE, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 20: **0.5963** | TEA, LEG, HIP, ARM                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS)

---

## Puzzle 17 (ID: 676)
**Words on Board:** YOUNG, CHEESE, MIDRIFF, BONDS, TRUNK, TORSO, CRUST, SAUCE, SIX-PACK, CASE, TOPPINGS, FORTY, GROWLER, TROUT, MANTLE, CORE

### Ground Truth Categories:
* **Level 0 (CENTRAL SECTION OF THE BODY) [Type: SYNONYM_OR_NEAR]:** CORE, MIDRIFF, TORSO, TRUNK
* **Level 1 (COMPONENTS OF A PIZZA) [Type: SEMANTIC_SET]:** CHEESE, CRUST, SAUCE, TOPPINGS
* **Level 2 (UNITS OF BEER) [Type: SEMANTIC_SET]:** CASE, FORTY, GROWLER, SIX-PACK
* **Level 3 (BASEBALL GREATS) [Type: NAMED_ENTITY_SET]:** BONDS, MANTLE, TROUT, YOUNG

### Top Candidate Partitions:
1. **Partition Score: 0.4625**
   - Group 1: **0.5774** | BONDS, TOPPINGS, GROWLER, TROUT                                   | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 2: **0.5375** | YOUNG, CHEESE, SAUCE, FORTY                                       | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 3: **0.4430** | CRUST, SIX-PACK, CASE, MANTLE                                     | INCORRECT (Max overlap: 2/4 with UNITS OF BEER)
   - Group 4: **0.4348** | MIDRIFF, TRUNK, TORSO, CORE                                       | CORRECT GROUP (CENTRAL SECTION OF THE BODY, Level 0)
2. **Partition Score: 0.4576**
   - Group 1: **0.5169** | TOPPINGS, FORTY, GROWLER, TROUT                                   | INCORRECT (Max overlap: 2/4 with UNITS OF BEER)
   - Group 2: **0.4863** | YOUNG, CHEESE, BONDS, SIX-PACK                                    | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 3: **0.4748** | CRUST, SAUCE, CASE, MANTLE                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 4: **0.4348** | MIDRIFF, TRUNK, TORSO, CORE                                       | CORRECT GROUP (CENTRAL SECTION OF THE BODY, Level 0)
3. **Partition Score: 0.4574**
   - Group 1: **0.5675** | CHEESE, FORTY, GROWLER, TROUT                                     | INCORRECT (Max overlap: 2/4 with UNITS OF BEER)
   - Group 2: **0.4852** | YOUNG, BONDS, SIX-PACK, TOPPINGS                                  | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 3: **0.4748** | CRUST, SAUCE, CASE, MANTLE                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 4: **0.4348** | MIDRIFF, TRUNK, TORSO, CORE                                       | CORRECT GROUP (CENTRAL SECTION OF THE BODY, Level 0)
4. **Partition Score: 0.4573**
   - Group 1: **0.5521** | BONDS, FORTY, GROWLER, TROUT                                      | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 2: **0.4848** | YOUNG, CHEESE, SIX-PACK, TOPPINGS                                 | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 3: **0.4748** | CRUST, SAUCE, CASE, MANTLE                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 4: **0.4348** | MIDRIFF, TRUNK, TORSO, CORE                                       | CORRECT GROUP (CENTRAL SECTION OF THE BODY, Level 0)
5. **Partition Score: 0.4560**
   - Group 1: **0.6036** | CHEESE, TOPPINGS, GROWLER, TROUT                                  | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 2: **0.4796** | YOUNG, BONDS, SIX-PACK, FORTY                                     | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 3: **0.4748** | CRUST, SAUCE, CASE, MANTLE                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 4: **0.4348** | MIDRIFF, TRUNK, TORSO, CORE                                       | CORRECT GROUP (CENTRAL SECTION OF THE BODY, Level 0)

### Top Candidate Groups:
   - Group 1: **0.5774** | BONDS, TOPPINGS, GROWLER, TROUT                                   | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 2: **0.5375** | YOUNG, CHEESE, SAUCE, FORTY                                       | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 3: **0.4430** | CRUST, SIX-PACK, CASE, MANTLE                                     | INCORRECT (Max overlap: 2/4 with UNITS OF BEER)
   - Group 4: **0.4348** | MIDRIFF, TRUNK, TORSO, CORE                                       | CORRECT GROUP (CENTRAL SECTION OF THE BODY, Level 0)
   - Group 5: **0.5169** | TOPPINGS, FORTY, GROWLER, TROUT                                   | INCORRECT (Max overlap: 2/4 with UNITS OF BEER)
   - Group 6: **0.4863** | YOUNG, CHEESE, BONDS, SIX-PACK                                    | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 7: **0.4748** | CRUST, SAUCE, CASE, MANTLE                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 8: **0.5675** | CHEESE, FORTY, GROWLER, TROUT                                     | INCORRECT (Max overlap: 2/4 with UNITS OF BEER)
   - Group 9: **0.4852** | YOUNG, BONDS, SIX-PACK, TOPPINGS                                  | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 10: **0.5521** | BONDS, FORTY, GROWLER, TROUT                                      | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 11: **0.4848** | YOUNG, CHEESE, SIX-PACK, TOPPINGS                                 | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 12: **0.6036** | CHEESE, TOPPINGS, GROWLER, TROUT                                  | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 13: **0.4796** | YOUNG, BONDS, SIX-PACK, FORTY                                     | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 14: **0.5084** | BONDS, SAUCE, GROWLER, TROUT                                      | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 15: **0.5079** | YOUNG, CHEESE, TOPPINGS, FORTY                                    | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 16: **0.4724** | YOUNG, CHEESE, SIX-PACK, FORTY                                    | INCORRECT (Max overlap: 2/4 with UNITS OF BEER)
   - Group 17: **0.5026** | YOUNG, CHEESE, BONDS, SAUCE                                       | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 18: **0.5528** | CHEESE, BONDS, FORTY, TROUT                                       | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)
   - Group 19: **0.5127** | SAUCE, SIX-PACK, TOPPINGS, GROWLER                                | INCORRECT (Max overlap: 2/4 with COMPONENTS OF A PIZZA)
   - Group 20: **0.4314** | YOUNG, CRUST, CASE, MANTLE                                        | INCORRECT (Max overlap: 2/4 with BASEBALL GREATS)

---

## Puzzle 18 (ID: 132)
**Words on Board:** HOOK, TRIPE, BUNK, SPAM, WIRE, SAUCER, CUP, STRAP, DISH, BALONEY, LASER, SCUBA, BOWL, CROCK, PLATE, RADAR

### Ground Truth Categories:
* **Level 0 (TABLEWARE) [Type: SEMANTIC_SET]:** BOWL, DISH, PLATE, SAUCER
* **Level 1 (NONSENSE) [Type: SYNONYM_OR_NEAR]:** BALONEY, BUNK, CROCK, TRIPE
* **Level 2 (BRA PARTS) [Type: SEMANTIC_SET]:** CUP, HOOK, STRAP, WIRE
* **Level 3 (ACRONYMS) [Type: WORDPLAY_TRANSFORM]:** LASER, RADAR, SCUBA, SPAM

### Top Candidate Partitions:
1. **Partition Score: 0.5013**
   - Group 1: **0.6724** | SAUCER, DISH, BOWL, PLATE                                         | CORRECT GROUP (TABLEWARE, Level 0)
   - Group 2: **0.6536** | TRIPE, BUNK, BALONEY, CROCK                                       | CORRECT GROUP (NONSENSE, Level 1)
   - Group 3: **0.4880** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
   - Group 4: **0.4318** | HOOK, WIRE, CUP, STRAP                                            | CORRECT GROUP (BRA PARTS, Level 2)
2. **Partition Score: 0.4927**
   - Group 1: **0.6724** | SAUCER, DISH, BOWL, PLATE                                         | CORRECT GROUP (TABLEWARE, Level 0)
   - Group 2: **0.5060** | STRAP, LASER, SCUBA, RADAR                                        | INCORRECT (Max overlap: 3/4 with ACRONYMS)
   - Group 3: **0.4886** | TRIPE, SPAM, WIRE, BALONEY                                        | INCORRECT (Max overlap: 2/4 with NONSENSE)
   - Group 4: **0.4881** | HOOK, BUNK, CUP, CROCK                                            | INCORRECT (Max overlap: 2/4 with BRA PARTS)
3. **Partition Score: 0.4858**
   - Group 1: **0.6724** | SAUCER, DISH, BOWL, PLATE                                         | CORRECT GROUP (TABLEWARE, Level 0)
   - Group 2: **0.5650** | TRIPE, BUNK, SPAM, BALONEY                                        | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 3: **0.4773** | WIRE, LASER, SCUBA, RADAR                                         | INCORRECT (Max overlap: 3/4 with ACRONYMS)
   - Group 4: **0.4505** | HOOK, CUP, STRAP, CROCK                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)
4. **Partition Score: 0.4749**
   - Group 1: **0.6724** | SAUCER, DISH, BOWL, PLATE                                         | CORRECT GROUP (TABLEWARE, Level 0)
   - Group 2: **0.5104** | TRIPE, BUNK, WIRE, BALONEY                                        | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 3: **0.4880** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
   - Group 4: **0.4505** | HOOK, CUP, STRAP, CROCK                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)
5. **Partition Score: 0.4742**
   - Group 1: **0.7706** | SAUCER, CUP, DISH, PLATE                                          | INCORRECT (Max overlap: 3/4 with TABLEWARE)
   - Group 2: **0.6536** | TRIPE, BUNK, BALONEY, CROCK                                       | CORRECT GROUP (NONSENSE, Level 1)
   - Group 3: **0.4880** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
   - Group 4: **0.3776** | HOOK, WIRE, STRAP, BOWL                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)

### Top Candidate Groups:
   - Group 1: **0.6724** | SAUCER, DISH, BOWL, PLATE                                         | CORRECT GROUP (TABLEWARE, Level 0)
   - Group 2: **0.6536** | TRIPE, BUNK, BALONEY, CROCK                                       | CORRECT GROUP (NONSENSE, Level 1)
   - Group 3: **0.4880** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
   - Group 4: **0.4318** | HOOK, WIRE, CUP, STRAP                                            | CORRECT GROUP (BRA PARTS, Level 2)
   - Group 5: **0.5060** | STRAP, LASER, SCUBA, RADAR                                        | INCORRECT (Max overlap: 3/4 with ACRONYMS)
   - Group 6: **0.4886** | TRIPE, SPAM, WIRE, BALONEY                                        | INCORRECT (Max overlap: 2/4 with NONSENSE)
   - Group 7: **0.4881** | HOOK, BUNK, CUP, CROCK                                            | INCORRECT (Max overlap: 2/4 with BRA PARTS)
   - Group 8: **0.5650** | TRIPE, BUNK, SPAM, BALONEY                                        | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 9: **0.4773** | WIRE, LASER, SCUBA, RADAR                                         | INCORRECT (Max overlap: 3/4 with ACRONYMS)
   - Group 10: **0.4505** | HOOK, CUP, STRAP, CROCK                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)
   - Group 11: **0.5104** | TRIPE, BUNK, WIRE, BALONEY                                        | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 12: **0.7706** | SAUCER, CUP, DISH, PLATE                                          | INCORRECT (Max overlap: 3/4 with TABLEWARE)
   - Group 13: **0.3776** | HOOK, WIRE, STRAP, BOWL                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)
   - Group 14: **0.4597** | TRIPE, SPAM, STRAP, BALONEY                                       | INCORRECT (Max overlap: 2/4 with NONSENSE)
   - Group 15: **0.4900** | BUNK, SPAM, WIRE, BALONEY                                         | INCORRECT (Max overlap: 2/4 with NONSENSE)
   - Group 16: **0.4390** | HOOK, TRIPE, CUP, CROCK                                           | INCORRECT (Max overlap: 2/4 with BRA PARTS)
   - Group 17: **0.5377** | HOOK, TRIPE, WIRE, STRAP                                          | INCORRECT (Max overlap: 3/4 with BRA PARTS)
   - Group 18: **0.4072** | BUNK, CUP, BALONEY, CROCK                                         | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 19: **0.4670** | BUNK, WIRE, STRAP, BALONEY                                        | INCORRECT (Max overlap: 2/4 with NONSENSE)
   - Group 20: **0.4458** | BUNK, LASER, SCUBA, RADAR                                         | INCORRECT (Max overlap: 3/4 with ACRONYMS)

---

## Puzzle 19 (ID: 129)
**Words on Board:** PANT, TONG, SNOOZE, BOXER, PUFF, BREEZE, KICK, DRAG, GOGGLE, DRAFT, YAWN, TANG, GUST, ZIP, BORE, BITE

### Ground Truth Categories:
* **Level 0 (SOMETHING TIRESOME) [Type: SYNONYM_OR_NEAR]:** BORE, DRAG, SNOOZE, YAWN
* **Level 1 (BIT OF WIND) [Type: SYNONYM_OR_NEAR]:** BREEZE, DRAFT, GUST, PUFF
* **Level 2 (PIQUANCY) [Type: SYNONYM_OR_NEAR]:** BITE, KICK, TANG, ZIP
* **Level 3 (SINGULAR OF THINGS SEEN IN PAIRS) [Type: WORDPLAY_TRANSFORM]:** BOXER, GOGGLE, PANT, TONG

### Top Candidate Partitions:
1. **Partition Score: 0.5143**
   - Group 1: **0.6158** | SNOOZE, GOGGLE, YAWN, BORE                                        | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 2: **0.5814** | TONG, BOXER, TANG, BITE                                           | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 3: **0.5012** | PANT, PUFF, BREEZE, GUST                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 4: **0.4873** | KICK, DRAG, DRAFT, ZIP                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
2. **Partition Score: 0.5051**
   - Group 1: **0.5502** | SNOOZE, BOXER, YAWN, BORE                                         | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 2: **0.5445** | TONG, GOGGLE, TANG, BITE                                          | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 3: **0.5012** | PANT, PUFF, BREEZE, GUST                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 4: **0.4873** | KICK, DRAG, DRAFT, ZIP                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
3. **Partition Score: 0.5015**
   - Group 1: **0.5469** | SNOOZE, BOXER, GOGGLE, BORE                                       | INCORRECT (Max overlap: 2/4 with SOMETHING TIRESOME)
   - Group 2: **0.5302** | TONG, YAWN, TANG, BITE                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 3: **0.5012** | PANT, PUFF, BREEZE, GUST                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 4: **0.4873** | KICK, DRAG, DRAFT, ZIP                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
4. **Partition Score: 0.4928**
   - Group 1: **0.6817** | TONG, BOXER, GOGGLE, TANG                                         | INCORRECT (Max overlap: 3/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 2: **0.5012** | PANT, PUFF, BREEZE, GUST                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 3: **0.4953** | SNOOZE, YAWN, BORE, BITE                                          | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 4: **0.4873** | KICK, DRAG, DRAFT, ZIP                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
5. **Partition Score: 0.4912**
   - Group 1: **0.5538** | BOXER, GOGGLE, YAWN, BORE                                         | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 2: **0.5012** | PANT, PUFF, BREEZE, GUST                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 3: **0.4891** | TONG, SNOOZE, TANG, BITE                                          | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 4: **0.4873** | KICK, DRAG, DRAFT, ZIP                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)

### Top Candidate Groups:
   - Group 1: **0.6158** | SNOOZE, GOGGLE, YAWN, BORE                                        | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 2: **0.5814** | TONG, BOXER, TANG, BITE                                           | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 3: **0.5012** | PANT, PUFF, BREEZE, GUST                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 4: **0.4873** | KICK, DRAG, DRAFT, ZIP                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 5: **0.5502** | SNOOZE, BOXER, YAWN, BORE                                         | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 6: **0.5445** | TONG, GOGGLE, TANG, BITE                                          | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 7: **0.5469** | SNOOZE, BOXER, GOGGLE, BORE                                       | INCORRECT (Max overlap: 2/4 with SOMETHING TIRESOME)
   - Group 8: **0.5302** | TONG, YAWN, TANG, BITE                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 9: **0.6817** | TONG, BOXER, GOGGLE, TANG                                         | INCORRECT (Max overlap: 3/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 10: **0.4953** | SNOOZE, YAWN, BORE, BITE                                          | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 11: **0.5538** | BOXER, GOGGLE, YAWN, BORE                                         | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 12: **0.4891** | TONG, SNOOZE, TANG, BITE                                          | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 13: **0.5095** | TONG, BOXER, GOGGLE, BITE                                         | INCORRECT (Max overlap: 3/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 14: **0.4836** | SNOOZE, YAWN, TANG, BORE                                          | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 15: **0.5017** | SNOOZE, BOXER, TANG, BITE                                         | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 16: **0.4805** | TONG, GOGGLE, YAWN, BORE                                          | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)

---

## Puzzle 20 (ID: 785)
**Words on Board:** EFFORT, BEETLE, BEECH, CEDAR, ZITI, YEW, APPLE, COOKIE, DECAY, EASY, APHID, VENDETTA, PINE, MITE, GEO, TICK

### Ground Truth Categories:
* **Level 0 (ARTHROPODS) [Type: SEMANTIC_SET]:** APHID, BEETLE, MITE, TICK
* **Level 1 (TREES) [Type: SEMANTIC_SET]:** BEECH, CEDAR, PINE, YEW
* **Level 2 ([LETTER] (IS) FOR ___) [Type: FILL_IN_THE_BLANK]:** APPLE, COOKIE, EFFORT, VENDETTA
* **Level 3 (WORDS THAT SOUNDS LIKE TWO LETTERS) [Type: SOUND_OR_SPELLING]:** DECAY, EASY, GEO, ZITI

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7918** | BEECH, CEDAR, YEW, PINE                                           | CORRECT GROUP (TREES, Level 1)
   - Group 2: **0.6317** | BEECH, CEDAR, APPLE, PINE                                         | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 3: **0.6158** | BEECH, YEW, APPLE, PINE                                           | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 4: **0.6112** | BEECH, YEW, APHID, PINE                                           | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 5: **0.5895** | BEECH, CEDAR, YEW, APPLE                                          | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 6: **0.5851** | BEECH, YEW, PINE, GEO                                             | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 7: **0.5825** | BEECH, CEDAR, APHID, PINE                                         | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 8: **0.5749** | BEECH, CEDAR, COOKIE, PINE                                        | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 9: **0.5727** | BEECH, APPLE, APHID, PINE                                         | INCORRECT (Max overlap: 2/4 with TREES)
   - Group 10: **0.5712** | COOKIE, APHID, MITE, TICK                                         | INCORRECT (Max overlap: 3/4 with ARTHROPODS)
   - Group 11: **0.5703** | BEETLE, BEECH, CEDAR, PINE                                        | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 12: **0.5675** | BEETLE, APPLE, COOKIE, APHID                                      | INCORRECT (Max overlap: 2/4 with ARTHROPODS)
   - Group 13: **0.5670** | BEETLE, COOKIE, APHID, MITE                                       | INCORRECT (Max overlap: 3/4 with ARTHROPODS)
   - Group 14: **0.5642** | CEDAR, YEW, APPLE, PINE                                           | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 15: **0.5631** | APPLE, COOKIE, APHID, GEO                                         | INCORRECT (Max overlap: 2/4 with [LETTER] (IS) FOR ___)
   - Group 16: **0.5554** | BEECH, CEDAR, YEW, APHID                                          | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 17: **0.5543** | BEECH, CEDAR, PINE, GEO                                           | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 18: **0.5522** | BEECH, CEDAR, YEW, COOKIE                                         | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 19: **0.5497** | CEDAR, YEW, COOKIE, PINE                                          | INCORRECT (Max overlap: 3/4 with TREES)
   - Group 20: **0.5491** | BEETLE, APPLE, APHID, PINE                                        | INCORRECT (Max overlap: 2/4 with ARTHROPODS)

---

## Puzzle 21 (ID: 546)
**Words on Board:** WEDGE, SLUG, PUMA, SEOUL, CATERPILLAR, DOVE, BLOW, GREYHOUND, SOCK, INDY, SHOEHORN, WRAP, METTLE, SQUEEZE, SANDWICH, BELT

### Ground Truth Categories:
* **Level 0 (PUNCH) [Type: SYNONYM_OR_NEAR]:** BELT, BLOW, SOCK, SLUG
* **Level 1 (CRAM) [Type: SYNONYM_OR_NEAR]:** SANDWICH, SHOEHORN, SQUEEZE, WEDGE
* **Level 2 (COMPANIES NAMED AFTER ANIMALS) [Type: NAMED_ENTITY_SET]:** CATERPILLAR, DOVE, GREYHOUND, PUMA
* **Level 3 (HOMOPHONES OF MUSIC GENRES) [Type: SOUND_OR_SPELLING]:** INDY, METTLE, SEOUL, WRAP

### Top Candidate Partitions:
1. **Partition Score: 0.5629**
   - Group 1: **0.7176** | WEDGE, SHOEHORN, WRAP, SQUEEZE                                    | INCORRECT (Max overlap: 3/4 with CRAM)
   - Group 2: **0.6565** | SLUG, BLOW, SOCK, BELT                                            | CORRECT GROUP (PUNCH, Level 0)
   - Group 3: **0.6181** | PUMA, SEOUL, CATERPILLAR, GREYHOUND                               | INCORRECT (Max overlap: 3/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 4: **0.4885** | DOVE, INDY, METTLE, SANDWICH                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF MUSIC GENRES)
2. **Partition Score: 0.5515**
   - Group 1: **0.7176** | WEDGE, SHOEHORN, WRAP, SQUEEZE                                    | INCORRECT (Max overlap: 3/4 with CRAM)
   - Group 2: **0.6565** | SLUG, BLOW, SOCK, BELT                                            | CORRECT GROUP (PUNCH, Level 0)
   - Group 3: **0.6517** | PUMA, CATERPILLAR, DOVE, GREYHOUND                                | CORRECT GROUP (COMPANIES NAMED AFTER ANIMALS, Level 2)
   - Group 4: **0.4489** | SEOUL, INDY, METTLE, SANDWICH                                     | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF MUSIC GENRES)
3. **Partition Score: 0.5333**
   - Group 1: **0.5655** | SEOUL, GREYHOUND, INDY, METTLE                                    | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF MUSIC GENRES)
   - Group 2: **0.5527** | WEDGE, SHOEHORN, WRAP, SANDWICH                                   | INCORRECT (Max overlap: 3/4 with CRAM)
   - Group 3: **0.5360** | BLOW, SOCK, SQUEEZE, BELT                                         | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 4: **0.5223** | SLUG, PUMA, CATERPILLAR, DOVE                                     | INCORRECT (Max overlap: 3/4 with COMPANIES NAMED AFTER ANIMALS)
4. **Partition Score: 0.5324**
   - Group 1: **0.7176** | WEDGE, SHOEHORN, WRAP, SQUEEZE                                    | INCORRECT (Max overlap: 3/4 with CRAM)
   - Group 2: **0.6565** | SLUG, BLOW, SOCK, BELT                                            | CORRECT GROUP (PUNCH, Level 0)
   - Group 3: **0.5456** | PUMA, CATERPILLAR, GREYHOUND, INDY                                | INCORRECT (Max overlap: 3/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 4: **0.4636** | SEOUL, DOVE, METTLE, SANDWICH                                     | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF MUSIC GENRES)
5. **Partition Score: 0.5317**
   - Group 1: **0.5527** | WEDGE, SHOEHORN, WRAP, SANDWICH                                   | INCORRECT (Max overlap: 3/4 with CRAM)
   - Group 2: **0.5360** | BLOW, SOCK, SQUEEZE, BELT                                         | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 3: **0.5337** | SLUG, PUMA, DOVE, METTLE                                          | INCORRECT (Max overlap: 2/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 4: **0.5285** | SEOUL, CATERPILLAR, GREYHOUND, INDY                               | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF MUSIC GENRES)

### Top Candidate Groups:
   - Group 1: **0.7176** | WEDGE, SHOEHORN, WRAP, SQUEEZE                                    | INCORRECT (Max overlap: 3/4 with CRAM)
   - Group 2: **0.6565** | SLUG, BLOW, SOCK, BELT                                            | CORRECT GROUP (PUNCH, Level 0)
   - Group 3: **0.6181** | PUMA, SEOUL, CATERPILLAR, GREYHOUND                               | INCORRECT (Max overlap: 3/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 4: **0.4885** | DOVE, INDY, METTLE, SANDWICH                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF MUSIC GENRES)
   - Group 5: **0.6517** | PUMA, CATERPILLAR, DOVE, GREYHOUND                                | CORRECT GROUP (COMPANIES NAMED AFTER ANIMALS, Level 2)
   - Group 6: **0.4489** | SEOUL, INDY, METTLE, SANDWICH                                     | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF MUSIC GENRES)
   - Group 7: **0.5655** | SEOUL, GREYHOUND, INDY, METTLE                                    | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF MUSIC GENRES)
   - Group 8: **0.5527** | WEDGE, SHOEHORN, WRAP, SANDWICH                                   | INCORRECT (Max overlap: 3/4 with CRAM)
   - Group 9: **0.5360** | BLOW, SOCK, SQUEEZE, BELT                                         | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 10: **0.5223** | SLUG, PUMA, CATERPILLAR, DOVE                                     | INCORRECT (Max overlap: 3/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 11: **0.5456** | PUMA, CATERPILLAR, GREYHOUND, INDY                                | INCORRECT (Max overlap: 3/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 12: **0.4636** | SEOUL, DOVE, METTLE, SANDWICH                                     | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF MUSIC GENRES)
   - Group 13: **0.5337** | SLUG, PUMA, DOVE, METTLE                                          | INCORRECT (Max overlap: 2/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 14: **0.5285** | SEOUL, CATERPILLAR, GREYHOUND, INDY                               | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF MUSIC GENRES)
   - Group 15: **0.5699** | PUMA, CATERPILLAR, GREYHOUND, METTLE                              | INCORRECT (Max overlap: 3/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 16: **0.4497** | SEOUL, DOVE, INDY, SANDWICH                                       | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF MUSIC GENRES)
   - Group 17: **0.6349** | WEDGE, BLOW, SOCK, BELT                                           | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 18: **0.6261** | PUMA, SEOUL, GREYHOUND, INDY                                      | INCORRECT (Max overlap: 2/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 19: **0.5082** | SLUG, CATERPILLAR, DOVE, METTLE                                   | INCORRECT (Max overlap: 2/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 20: **0.4937** | SHOEHORN, WRAP, SQUEEZE, SANDWICH                                 | INCORRECT (Max overlap: 3/4 with CRAM)

---

## Puzzle 22 (ID: 1046)
**Words on Board:** DICK, CLIFF, PITCH, POLYHEDRON, SPOT, CATCH, REGISTER, FINE PRINT, STRINGS, MOTHER, RANGE, CAVEAT, TONE, BUILDING, JANE, CLOCK

### Ground Truth Categories:
* **Level 0 (STIPULATION) [Type: SYNONYM_OR_NEAR]:** CATCH, CAVEAT, FINE PRINT, STRINGS
* **Level 1 (VOCAL CHARACTERISTICS) [Type: SEMANTIC_SET]:** PITCH, RANGE, REGISTER, TONE
* **Level 2 (CHARACTERS IN "DICK AND JANE") [Type: NAMED_ENTITY_SET]:** DICK, JANE, MOTHER, SPOT
* **Level 3 (THINGS WITH FACES) [Type: SEMANTIC_SET]:** BUILDING, CLIFF, CLOCK, POLYHEDRON

### Top Candidate Partitions:
1. **Partition Score: 0.4818**
   - Group 1: **0.5383** | POLYHEDRON, SPOT, BUILDING, CLOCK                                 | INCORRECT (Max overlap: 3/4 with THINGS WITH FACES)
   - Group 2: **0.5355** | DICK, CLIFF, MOTHER, JANE                                         | INCORRECT (Max overlap: 3/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.5034** | PITCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 4: **0.4441** | CATCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 3/4 with STIPULATION)
2. **Partition Score: 0.4808**
   - Group 1: **0.5334** | CLIFF, MOTHER, BUILDING, CLOCK                                    | INCORRECT (Max overlap: 3/4 with THINGS WITH FACES)
   - Group 2: **0.5315** | DICK, POLYHEDRON, SPOT, JANE                                      | INCORRECT (Max overlap: 3/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.5034** | PITCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 4: **0.4441** | CATCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 3/4 with STIPULATION)
3. **Partition Score: 0.4806**
   - Group 1: **0.5371** | POLYHEDRON, MOTHER, BUILDING, JANE                                | INCORRECT (Max overlap: 2/4 with THINGS WITH FACES)
   - Group 2: **0.5309** | DICK, CLIFF, SPOT, CLOCK                                          | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.5034** | PITCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 4: **0.4441** | CATCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 3/4 with STIPULATION)
4. **Partition Score: 0.4797**
   - Group 1: **0.5438** | MOTHER, BUILDING, JANE, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 2: **0.5273** | DICK, CLIFF, POLYHEDRON, SPOT                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.5034** | PITCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 4: **0.4441** | CATCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 3/4 with STIPULATION)
5. **Partition Score: 0.4786**
   - Group 1: **0.5589** | CLIFF, MOTHER, JANE, CLOCK                                        | INCORRECT (Max overlap: 2/4 with THINGS WITH FACES)
   - Group 2: **0.5229** | DICK, POLYHEDRON, SPOT, BUILDING                                  | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.5034** | PITCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 4: **0.4441** | CATCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 3/4 with STIPULATION)

### Top Candidate Groups:
   - Group 1: **0.5383** | POLYHEDRON, SPOT, BUILDING, CLOCK                                 | INCORRECT (Max overlap: 3/4 with THINGS WITH FACES)
   - Group 2: **0.5355** | DICK, CLIFF, MOTHER, JANE                                         | INCORRECT (Max overlap: 3/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.5034** | PITCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 4: **0.4441** | CATCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 3/4 with STIPULATION)
   - Group 5: **0.5334** | CLIFF, MOTHER, BUILDING, CLOCK                                    | INCORRECT (Max overlap: 3/4 with THINGS WITH FACES)
   - Group 6: **0.5315** | DICK, POLYHEDRON, SPOT, JANE                                      | INCORRECT (Max overlap: 3/4 with CHARACTERS IN "DICK AND JANE")
   - Group 7: **0.5371** | POLYHEDRON, MOTHER, BUILDING, JANE                                | INCORRECT (Max overlap: 2/4 with THINGS WITH FACES)
   - Group 8: **0.5309** | DICK, CLIFF, SPOT, CLOCK                                          | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 9: **0.5438** | MOTHER, BUILDING, JANE, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 10: **0.5273** | DICK, CLIFF, POLYHEDRON, SPOT                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 11: **0.5589** | CLIFF, MOTHER, JANE, CLOCK                                        | INCORRECT (Max overlap: 2/4 with THINGS WITH FACES)
   - Group 12: **0.5229** | DICK, POLYHEDRON, SPOT, BUILDING                                  | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 13: **0.5190** | CLIFF, POLYHEDRON, BUILDING, JANE                                 | INCORRECT (Max overlap: 3/4 with THINGS WITH FACES)
   - Group 14: **0.5185** | DICK, SPOT, MOTHER, CLOCK                                         | INCORRECT (Max overlap: 3/4 with CHARACTERS IN "DICK AND JANE")
   - Group 15: **0.6296** | DICK, POLYHEDRON, SPOT, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 16: **0.5156** | CLIFF, MOTHER, BUILDING, JANE                                     | INCORRECT (Max overlap: 2/4 with THINGS WITH FACES)
   - Group 17: **0.5223** | DICK, SPOT, JANE, CLOCK                                           | INCORRECT (Max overlap: 3/4 with CHARACTERS IN "DICK AND JANE")
   - Group 18: **0.5138** | CLIFF, POLYHEDRON, MOTHER, BUILDING                               | INCORRECT (Max overlap: 3/4 with THINGS WITH FACES)
   - Group 19: **0.5389** | CLIFF, POLYHEDRON, MOTHER, JANE                                   | INCORRECT (Max overlap: 2/4 with THINGS WITH FACES)
   - Group 20: **0.5132** | DICK, SPOT, BUILDING, CLOCK                                       | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")

---

## Puzzle 23 (ID: 71)
**Words on Board:** MUG, SOPRANO, MONTANA, SPRITE, SQUIRT, COLORADO, YES, STARK, UTAH, NEVADA, CRUSH, ARIZONA, HAWK, KANSAS, GENESIS, RUSH

### Ground Truth Categories:
* **Level 0 (U.S. MOUNTAIN STATES) [Type: NAMED_ENTITY_SET]:** ARIZONA, COLORADO, NEVADA, UTAH
* **Level 1 (SODA BRANDS) [Type: NAMED_ENTITY_SET]:** CRUSH, MUG, SPRITE, SQUIRT
* **Level 2 (CLASSIC ROCK BANDS) [Type: NAMED_ENTITY_SET]:** GENESIS, KANSAS, RUSH, YES
* **Level 3 (TONY ___) [Type: FILL_IN_THE_BLANK]:** HAWK, MONTANA, SOPRANO, STARK

### Top Candidate Partitions:
1. **Partition Score: 0.5396**
   - Group 1: **0.5570** | SOPRANO, SPRITE, STARK, HAWK                                      | INCORRECT (Max overlap: 3/4 with TONY ___)
   - Group 2: **0.5512** | MONTANA, NEVADA, KANSAS, GENESIS                                  | INCORRECT (Max overlap: 2/4 with CLASSIC ROCK BANDS)
   - Group 3: **0.5461** | COLORADO, UTAH, CRUSH, ARIZONA                                    | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 4: **0.5306** | MUG, SQUIRT, YES, RUSH                                            | INCORRECT (Max overlap: 2/4 with SODA BRANDS)
2. **Partition Score: 0.5373**
   - Group 1: **0.5658** | MUG, SPRITE, SQUIRT, YES                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 2: **0.5403** | SOPRANO, STARK, HAWK, GENESIS                                     | INCORRECT (Max overlap: 3/4 with TONY ___)
   - Group 3: **0.5377** | COLORADO, NEVADA, CRUSH, ARIZONA                                  | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 4: **0.5356** | MONTANA, UTAH, KANSAS, RUSH                                       | INCORRECT (Max overlap: 2/4 with CLASSIC ROCK BANDS)
3. **Partition Score: 0.5362**
   - Group 1: **0.5658** | MUG, SPRITE, SQUIRT, YES                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 2: **0.5530** | MONTANA, COLORADO, KANSAS, RUSH                                   | INCORRECT (Max overlap: 2/4 with CLASSIC ROCK BANDS)
   - Group 3: **0.5403** | SOPRANO, STARK, HAWK, GENESIS                                     | INCORRECT (Max overlap: 3/4 with TONY ___)
   - Group 4: **0.5257** | UTAH, NEVADA, CRUSH, ARIZONA                                      | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
4. **Partition Score: 0.5349**
   - Group 1: **0.5570** | SOPRANO, SPRITE, STARK, HAWK                                      | INCORRECT (Max overlap: 3/4 with TONY ___)
   - Group 2: **0.5487** | MONTANA, UTAH, CRUSH, ARIZONA                                     | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 3: **0.5306** | MUG, SQUIRT, YES, RUSH                                            | INCORRECT (Max overlap: 2/4 with SODA BRANDS)
   - Group 4: **0.5301** | COLORADO, NEVADA, KANSAS, GENESIS                                 | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
5. **Partition Score: 0.5341**
   - Group 1: **0.5570** | SOPRANO, SPRITE, STARK, HAWK                                      | INCORRECT (Max overlap: 3/4 with TONY ___)
   - Group 2: **0.5448** | UTAH, CRUSH, ARIZONA, KANSAS                                      | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 3: **0.5306** | MUG, SQUIRT, YES, RUSH                                            | INCORRECT (Max overlap: 2/4 with SODA BRANDS)
   - Group 4: **0.5305** | MONTANA, COLORADO, NEVADA, GENESIS                                | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)

### Top Candidate Groups:
   - Group 1: **0.5570** | SOPRANO, SPRITE, STARK, HAWK                                      | INCORRECT (Max overlap: 3/4 with TONY ___)
   - Group 2: **0.5512** | MONTANA, NEVADA, KANSAS, GENESIS                                  | INCORRECT (Max overlap: 2/4 with CLASSIC ROCK BANDS)
   - Group 3: **0.5461** | COLORADO, UTAH, CRUSH, ARIZONA                                    | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 4: **0.5306** | MUG, SQUIRT, YES, RUSH                                            | INCORRECT (Max overlap: 2/4 with SODA BRANDS)
   - Group 5: **0.5658** | MUG, SPRITE, SQUIRT, YES                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 6: **0.5403** | SOPRANO, STARK, HAWK, GENESIS                                     | INCORRECT (Max overlap: 3/4 with TONY ___)
   - Group 7: **0.5377** | COLORADO, NEVADA, CRUSH, ARIZONA                                  | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 8: **0.5356** | MONTANA, UTAH, KANSAS, RUSH                                       | INCORRECT (Max overlap: 2/4 with CLASSIC ROCK BANDS)
   - Group 9: **0.5530** | MONTANA, COLORADO, KANSAS, RUSH                                   | INCORRECT (Max overlap: 2/4 with CLASSIC ROCK BANDS)
   - Group 10: **0.5257** | UTAH, NEVADA, CRUSH, ARIZONA                                      | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 11: **0.5487** | MONTANA, UTAH, CRUSH, ARIZONA                                     | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 12: **0.5301** | COLORADO, NEVADA, KANSAS, GENESIS                                 | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 13: **0.5448** | UTAH, CRUSH, ARIZONA, KANSAS                                      | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 14: **0.5305** | MONTANA, COLORADO, NEVADA, GENESIS                                | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 15: **0.5626** | MONTANA, COLORADO, NEVADA, CRUSH                                  | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 16: **0.5155** | UTAH, ARIZONA, KANSAS, RUSH                                       | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 17: **0.5211** | COLORADO, NEVADA, KANSAS, RUSH                                    | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 18: **0.5368** | COLORADO, UTAH, KANSAS, RUSH                                      | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 19: **0.5262** | MONTANA, NEVADA, CRUSH, ARIZONA                                   | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 20: **0.5461** | SPRITE, SQUIRT, YES, GENESIS                                      | INCORRECT (Max overlap: 2/4 with SODA BRANDS)

---

## Puzzle 24 (ID: 836)
**Words on Board:** PEPPER, SCATTER, CREPE PAPER, SPRINKLE, PICTURE, FLICK, LITTER, TOOTH, POTATO, TALK, FILM, PRUNE, SHAR PEI, BRAIN, FEATURE, SIXTEEN

### Ground Truth Categories:
* **Level 0 (MOVIE) [Type: SYNONYM_OR_NEAR]:** FEATURE, FILM, FLICK, PICTURE
* **Level 1 (STREW) [Type: SYNONYM_OR_NEAR]:** LITTER, PEPPER, SCATTER, SPRINKLE
* **Level 2 (WRINKLY THINGS) [Type: SEMANTIC_SET]:** BRAIN, CREPE PAPER, PRUNE, SHAR PEI
* **Level 3 (SWEET ___) [Type: FILL_IN_THE_BLANK]:** POTATO, SIXTEEN, TALK, TOOTH

### Top Candidate Partitions:
1. **Partition Score: 0.5522**
   - Group 1: **0.7881** | PICTURE, FLICK, FILM, FEATURE                                     | CORRECT GROUP (MOVIE, Level 0)
   - Group 2: **0.6120** | CREPE PAPER, POTATO, SHAR PEI, SIXTEEN                            | INCORRECT (Max overlap: 2/4 with WRINKLY THINGS)
   - Group 3: **0.6060** | SCATTER, SPRINKLE, LITTER, PRUNE                                  | INCORRECT (Max overlap: 3/4 with STREW)
   - Group 4: **0.4955** | PEPPER, TOOTH, TALK, BRAIN                                        | INCORRECT (Max overlap: 2/4 with SWEET ___)
2. **Partition Score: 0.5262**
   - Group 1: **0.6120** | CREPE PAPER, POTATO, SHAR PEI, SIXTEEN                            | INCORRECT (Max overlap: 2/4 with WRINKLY THINGS)
   - Group 2: **0.6104** | SCATTER, SPRINKLE, LITTER, FEATURE                                | INCORRECT (Max overlap: 3/4 with STREW)
   - Group 3: **0.5034** | PICTURE, FLICK, FILM, PRUNE                                       | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 4: **0.4955** | PEPPER, TOOTH, TALK, BRAIN                                        | INCORRECT (Max overlap: 2/4 with SWEET ___)
3. **Partition Score: 0.5258**
   - Group 1: **0.6120** | CREPE PAPER, POTATO, SHAR PEI, SIXTEEN                            | INCORRECT (Max overlap: 2/4 with WRINKLY THINGS)
   - Group 2: **0.5666** | SCATTER, PICTURE, FLICK, FILM                                     | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 3: **0.5457** | SPRINKLE, LITTER, PRUNE, FEATURE                                  | INCORRECT (Max overlap: 2/4 with STREW)
   - Group 4: **0.4955** | PEPPER, TOOTH, TALK, BRAIN                                        | INCORRECT (Max overlap: 2/4 with SWEET ___)
4. **Partition Score: 0.5189**
   - Group 1: **0.6120** | CREPE PAPER, POTATO, SHAR PEI, SIXTEEN                            | INCORRECT (Max overlap: 2/4 with WRINKLY THINGS)
   - Group 2: **0.5750** | PICTURE, FLICK, LITTER, FILM                                      | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 3: **0.5097** | SCATTER, SPRINKLE, PRUNE, FEATURE                                 | INCORRECT (Max overlap: 2/4 with STREW)
   - Group 4: **0.4955** | PEPPER, TOOTH, TALK, BRAIN                                        | INCORRECT (Max overlap: 2/4 with SWEET ___)
5. **Partition Score: 0.5171**
   - Group 1: **0.6120** | CREPE PAPER, POTATO, SHAR PEI, SIXTEEN                            | INCORRECT (Max overlap: 2/4 with WRINKLY THINGS)
   - Group 2: **0.5682** | SPRINKLE, PICTURE, FLICK, FILM                                    | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 3: **0.5091** | SCATTER, LITTER, PRUNE, FEATURE                                   | INCORRECT (Max overlap: 2/4 with STREW)
   - Group 4: **0.4955** | PEPPER, TOOTH, TALK, BRAIN                                        | INCORRECT (Max overlap: 2/4 with SWEET ___)

### Top Candidate Groups:
   - Group 1: **0.7881** | PICTURE, FLICK, FILM, FEATURE                                     | CORRECT GROUP (MOVIE, Level 0)
   - Group 2: **0.6120** | CREPE PAPER, POTATO, SHAR PEI, SIXTEEN                            | INCORRECT (Max overlap: 2/4 with WRINKLY THINGS)
   - Group 3: **0.6060** | SCATTER, SPRINKLE, LITTER, PRUNE                                  | INCORRECT (Max overlap: 3/4 with STREW)
   - Group 4: **0.4955** | PEPPER, TOOTH, TALK, BRAIN                                        | INCORRECT (Max overlap: 2/4 with SWEET ___)
   - Group 5: **0.6104** | SCATTER, SPRINKLE, LITTER, FEATURE                                | INCORRECT (Max overlap: 3/4 with STREW)
   - Group 6: **0.5034** | PICTURE, FLICK, FILM, PRUNE                                       | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 7: **0.5666** | SCATTER, PICTURE, FLICK, FILM                                     | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 8: **0.5457** | SPRINKLE, LITTER, PRUNE, FEATURE                                  | INCORRECT (Max overlap: 2/4 with STREW)
   - Group 9: **0.5750** | PICTURE, FLICK, LITTER, FILM                                      | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 10: **0.5097** | SCATTER, SPRINKLE, PRUNE, FEATURE                                 | INCORRECT (Max overlap: 2/4 with STREW)
   - Group 11: **0.5682** | SPRINKLE, PICTURE, FLICK, FILM                                    | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 12: **0.5091** | SCATTER, LITTER, PRUNE, FEATURE                                   | INCORRECT (Max overlap: 2/4 with STREW)
   - Group 13: **0.4893** | PEPPER, POTATO, TALK, BRAIN                                       | INCORRECT (Max overlap: 2/4 with SWEET ___)
   - Group 14: **0.4777** | CREPE PAPER, TOOTH, SHAR PEI, SIXTEEN                             | INCORRECT (Max overlap: 2/4 with WRINKLY THINGS)
   - Group 15: **0.5583** | TOOTH, TALK, BRAIN, SIXTEEN                                       | INCORRECT (Max overlap: 3/4 with SWEET ___)
   - Group 16: **0.4295** | PEPPER, CREPE PAPER, POTATO, SHAR PEI                             | INCORRECT (Max overlap: 2/4 with WRINKLY THINGS)
   - Group 17: **0.5345** | SCATTER, SPRINKLE, FLICK, LITTER                                  | INCORRECT (Max overlap: 3/4 with STREW)
   - Group 18: **0.4928** | PICTURE, FILM, PRUNE, FEATURE                                     | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 19: **0.5619** | SCATTER, PICTURE, FILM, FEATURE                                   | INCORRECT (Max overlap: 3/4 with MOVIE)
   - Group 20: **0.4766** | SPRINKLE, FLICK, LITTER, PRUNE                                    | INCORRECT (Max overlap: 2/4 with STREW)

---

## Puzzle 25 (ID: 498)
**Words on Board:** MUNG, PULL, DEAD, NAVY, DRIVE, NEUTRAL, DRAW, KIDNEY, LIVER, GRAB, REVERSE, PINTO, CAR, LOW, HOOK, WHIRL

### Ground Truth Categories:
* **Level 0 (KINDS OF BEANS) [Type: SEMANTIC_SET]:** KIDNEY, MUNG, NAVY, PINTO
* **Level 1 (ATTRACT) [Type: SYNONYM_OR_NEAR]:** DRAW, GRAB, HOOK, PULL
* **Level 2 (AUTOMATIC GEAR SHIFTER POSITIONS) [Type: SEMANTIC_SET]:** DRIVE, LOW, NEUTRAL, REVERSE
* **Level 3 (___POOL) [Type: FILL_IN_THE_BLANK]:** CAR, DEAD, LIVER, WHIRL

### Top Candidate Partitions:
1. **Partition Score: 0.4982**
   - Group 1: **0.6069** | NAVY, KIDNEY, PINTO, CAR                                          | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.5950** | PULL, DRAW, GRAB, HOOK                                            | CORRECT GROUP (ATTRACT, Level 1)
   - Group 3: **0.4733** | DEAD, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 4: **0.4623** | MUNG, DRIVE, LIVER, WHIRL                                         | INCORRECT (Max overlap: 2/4 with ___POOL)
2. **Partition Score: 0.4898**
   - Group 1: **0.6069** | NAVY, KIDNEY, PINTO, CAR                                          | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.5950** | PULL, DRAW, GRAB, HOOK                                            | CORRECT GROUP (ATTRACT, Level 1)
   - Group 3: **0.4644** | MUNG, DEAD, DRIVE, WHIRL                                          | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 4: **0.4499** | NEUTRAL, LIVER, REVERSE, LOW                                      | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
3. **Partition Score: 0.4812**
   - Group 1: **0.6069** | NAVY, KIDNEY, PINTO, CAR                                          | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.5950** | PULL, DRAW, GRAB, HOOK                                            | CORRECT GROUP (ATTRACT, Level 1)
   - Group 3: **0.4899** | MUNG, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 4: **0.4200** | DEAD, DRIVE, LIVER, WHIRL                                         | INCORRECT (Max overlap: 3/4 with ___POOL)
4. **Partition Score: 0.4808**
   - Group 1: **0.5950** | PULL, DRAW, GRAB, HOOK                                            | CORRECT GROUP (ATTRACT, Level 1)
   - Group 2: **0.5888** | MUNG, KIDNEY, PINTO, CAR                                          | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 3: **0.4733** | DEAD, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 4: **0.4305** | NAVY, DRIVE, LIVER, WHIRL                                         | INCORRECT (Max overlap: 2/4 with ___POOL)
5. **Partition Score: 0.4794**
   - Group 1: **0.6069** | NAVY, KIDNEY, PINTO, CAR                                          | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.5489** | PULL, DEAD, DRAW, HOOK                                            | INCORRECT (Max overlap: 3/4 with ATTRACT)
   - Group 3: **0.4688** | MUNG, DRIVE, GRAB, WHIRL                                          | INCORRECT (Max overlap: 1/4 with KINDS OF BEANS)
   - Group 4: **0.4499** | NEUTRAL, LIVER, REVERSE, LOW                                      | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)

### Top Candidate Groups:
   - Group 1: **0.6069** | NAVY, KIDNEY, PINTO, CAR                                          | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.5950** | PULL, DRAW, GRAB, HOOK                                            | CORRECT GROUP (ATTRACT, Level 1)
   - Group 3: **0.4733** | DEAD, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 4: **0.4623** | MUNG, DRIVE, LIVER, WHIRL                                         | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 5: **0.4644** | MUNG, DEAD, DRIVE, WHIRL                                          | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 6: **0.4499** | NEUTRAL, LIVER, REVERSE, LOW                                      | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 7: **0.4899** | MUNG, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 8: **0.4200** | DEAD, DRIVE, LIVER, WHIRL                                         | INCORRECT (Max overlap: 3/4 with ___POOL)
   - Group 9: **0.5888** | MUNG, KIDNEY, PINTO, CAR                                          | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 10: **0.4305** | NAVY, DRIVE, LIVER, WHIRL                                         | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 11: **0.5489** | PULL, DEAD, DRAW, HOOK                                            | INCORRECT (Max overlap: 3/4 with ATTRACT)
   - Group 12: **0.4688** | MUNG, DRIVE, GRAB, WHIRL                                          | INCORRECT (Max overlap: 1/4 with KINDS OF BEANS)
   - Group 13: **0.6190** | PULL, DRIVE, DRAW, HOOK                                           | INCORRECT (Max overlap: 3/4 with ATTRACT)
   - Group 14: **0.4296** | MUNG, DEAD, GRAB, WHIRL                                           | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 15: **0.4872** | NAVY, KIDNEY, LIVER, PINTO                                        | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 16: **0.4761** | MUNG, DRIVE, CAR, WHIRL                                           | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 17: **0.4809** | MUNG, DRIVE, REVERSE, WHIRL                                       | INCORRECT (Max overlap: 2/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 18: **0.4170** | DEAD, NEUTRAL, LIVER, LOW                                         | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 19: **0.4501** | MUNG, DEAD, DRIVE, LIVER                                          | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 20: **0.4282** | NEUTRAL, REVERSE, LOW, WHIRL                                      | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)

---

## Puzzle 26 (ID: 750)
**Words on Board:** AIRPLANE, DRIVE, VELVET, CIRCUS, BLACK, HOT TUB NOZZLE, ROLLER COASTER, NFL PLAYER, BRIDGE, CROWN, HIGHWAY, WHIRLWIND, VENEER, FILLING, SOAP OPERA, PEAKS

### Ground Truth Categories:
* **Level 0 (DENTAL ADDITIONS) [Type: SEMANTIC_SET]:** BRIDGE, CROWN, FILLING, VENEER
* **Level 1 (METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT) [Type: SYNONYM_OR_NEAR]:** CIRCUS, ROLLER COASTER, SOAP OPERA, WHIRLWIND
* **Level 2 (SECOND WORDS IN DAVID LYNCH TITLES) [Type: NAMED_ENTITY_SET]:** DRIVE, HIGHWAY, PEAKS, VELVET
* **Level 3 (WHAT “JET” MIGHT REFER TO) [Type: WORDPLAY_TRANSFORM]:** AIRPLANE, BLACK, HOT TUB NOZZLE, NFL PLAYER

### Top Candidate Partitions:
1. **Partition Score: 0.5599**
   - Group 1: **0.5973** | HOT TUB NOZZLE, ROLLER COASTER, WHIRLWIND, SOAP OPERA             | INCORRECT (Max overlap: 3/4 with METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT)
   - Group 2: **0.5874** | AIRPLANE, CIRCUS, BLACK, NFL PLAYER                               | INCORRECT (Max overlap: 3/4 with WHAT “JET” MIGHT REFER TO)
   - Group 3: **0.5751** | DRIVE, VELVET, BRIDGE, HIGHWAY                                    | INCORRECT (Max overlap: 3/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 4: **0.5387** | CROWN, VENEER, FILLING, PEAKS                                     | INCORRECT (Max overlap: 3/4 with DENTAL ADDITIONS)
2. **Partition Score: 0.5581**
   - Group 1: **0.6083** | AIRPLANE, DRIVE, BRIDGE, HIGHWAY                                  | INCORRECT (Max overlap: 2/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 2: **0.5973** | HOT TUB NOZZLE, ROLLER COASTER, WHIRLWIND, SOAP OPERA             | INCORRECT (Max overlap: 3/4 with METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT)
   - Group 3: **0.5579** | VELVET, CIRCUS, BLACK, NFL PLAYER                                 | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 4: **0.5387** | CROWN, VENEER, FILLING, PEAKS                                     | INCORRECT (Max overlap: 3/4 with DENTAL ADDITIONS)
3. **Partition Score: 0.5536**
   - Group 1: **0.6070** | AIRPLANE, VELVET, BLACK, NFL PLAYER                               | INCORRECT (Max overlap: 3/4 with WHAT “JET” MIGHT REFER TO)
   - Group 2: **0.5973** | HOT TUB NOZZLE, ROLLER COASTER, WHIRLWIND, SOAP OPERA             | INCORRECT (Max overlap: 3/4 with METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT)
   - Group 3: **0.5398** | DRIVE, CIRCUS, BRIDGE, HIGHWAY                                    | INCORRECT (Max overlap: 2/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 4: **0.5387** | CROWN, VENEER, FILLING, PEAKS                                     | INCORRECT (Max overlap: 3/4 with DENTAL ADDITIONS)
4. **Partition Score: 0.5527**
   - Group 1: **0.5795** | AIRPLANE, HOT TUB NOZZLE, ROLLER COASTER, SOAP OPERA              | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 2: **0.5751** | DRIVE, VELVET, BRIDGE, HIGHWAY                                    | INCORRECT (Max overlap: 3/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 3: **0.5586** | CIRCUS, BLACK, NFL PLAYER, WHIRLWIND                              | INCORRECT (Max overlap: 2/4 with METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT)
   - Group 4: **0.5387** | CROWN, VENEER, FILLING, PEAKS                                     | INCORRECT (Max overlap: 3/4 with DENTAL ADDITIONS)
5. **Partition Score: 0.5525**
   - Group 1: **0.5979** | AIRPLANE, CIRCUS, BLACK, SOAP OPERA                               | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 2: **0.5751** | DRIVE, VELVET, BRIDGE, HIGHWAY                                    | INCORRECT (Max overlap: 3/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 3: **0.5576** | HOT TUB NOZZLE, ROLLER COASTER, NFL PLAYER, WHIRLWIND             | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 4: **0.5387** | CROWN, VENEER, FILLING, PEAKS                                     | INCORRECT (Max overlap: 3/4 with DENTAL ADDITIONS)

### Top Candidate Groups:
   - Group 1: **0.5973** | HOT TUB NOZZLE, ROLLER COASTER, WHIRLWIND, SOAP OPERA             | INCORRECT (Max overlap: 3/4 with METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT)
   - Group 2: **0.5874** | AIRPLANE, CIRCUS, BLACK, NFL PLAYER                               | INCORRECT (Max overlap: 3/4 with WHAT “JET” MIGHT REFER TO)
   - Group 3: **0.5751** | DRIVE, VELVET, BRIDGE, HIGHWAY                                    | INCORRECT (Max overlap: 3/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 4: **0.5387** | CROWN, VENEER, FILLING, PEAKS                                     | INCORRECT (Max overlap: 3/4 with DENTAL ADDITIONS)
   - Group 5: **0.6083** | AIRPLANE, DRIVE, BRIDGE, HIGHWAY                                  | INCORRECT (Max overlap: 2/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 6: **0.5579** | VELVET, CIRCUS, BLACK, NFL PLAYER                                 | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 7: **0.6070** | AIRPLANE, VELVET, BLACK, NFL PLAYER                               | INCORRECT (Max overlap: 3/4 with WHAT “JET” MIGHT REFER TO)
   - Group 8: **0.5398** | DRIVE, CIRCUS, BRIDGE, HIGHWAY                                    | INCORRECT (Max overlap: 2/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 9: **0.5795** | AIRPLANE, HOT TUB NOZZLE, ROLLER COASTER, SOAP OPERA              | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 10: **0.5586** | CIRCUS, BLACK, NFL PLAYER, WHIRLWIND                              | INCORRECT (Max overlap: 2/4 with METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT)
   - Group 11: **0.5979** | AIRPLANE, CIRCUS, BLACK, SOAP OPERA                               | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 12: **0.5576** | HOT TUB NOZZLE, ROLLER COASTER, NFL PLAYER, WHIRLWIND             | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 13: **0.5712** | VELVET, CIRCUS, BLACK, SOAP OPERA                                 | INCORRECT (Max overlap: 2/4 with METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT)
   - Group 14: **0.5833** | AIRPLANE, VELVET, CIRCUS, NFL PLAYER                              | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 15: **0.5447** | DRIVE, BLACK, BRIDGE, HIGHWAY                                     | INCORRECT (Max overlap: 2/4 with SECOND WORDS IN DAVID LYNCH TITLES)
   - Group 16: **0.5834** | VELVET, CIRCUS, BLACK, WHIRLWIND                                  | INCORRECT (Max overlap: 2/4 with METAPHORS FOR A DRAMATIC AND CHAOTIC EVENT)
   - Group 17: **0.5427** | HOT TUB NOZZLE, ROLLER COASTER, NFL PLAYER, SOAP OPERA            | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 18: **0.5735** | HOT TUB NOZZLE, NFL PLAYER, WHIRLWIND, SOAP OPERA                 | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 19: **0.5521** | AIRPLANE, CIRCUS, BLACK, ROLLER COASTER                           | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)
   - Group 20: **0.5923** | AIRPLANE, HOT TUB NOZZLE, ROLLER COASTER, WHIRLWIND               | INCORRECT (Max overlap: 2/4 with WHAT “JET” MIGHT REFER TO)

---

## Puzzle 27 (ID: 88)
**Words on Board:** ROGER, ROAD, MET, FRAMED, PICTURE, MAX, WHO, MAD, WHEN, HARRY, HORROR, SALLY, ROCKY, RABBIT, SHOW, FURY

### Ground Truth Categories:
* **Level 0 (ROCKY HORROR PICTURE SHOW) [Type: NAMED_ENTITY_SET]:** HORROR, PICTURE, ROCKY, SHOW
* **Level 1 (WHO FRAMED ROGER RABBIT) [Type: NAMED_ENTITY_SET]:** FRAMED, RABBIT, ROGER, WHO
* **Level 2 (WHEN HARRY MET SALLY) [Type: NAMED_ENTITY_SET]:** HARRY, MET, SALLY, WHEN
* **Level 3 (MAD MAX FURY ROAD) [Type: NAMED_ENTITY_SET]:** FURY, MAD, MAX, ROAD

### Top Candidate Partitions:
1. **Partition Score: 0.5380**
   - Group 1: **0.5631** | ROAD, MAX, MAD, FURY                                              | CORRECT GROUP (MAD MAX FURY ROAD, Level 3)
   - Group 2: **0.5521** | ROGER, HARRY, HORROR, ROCKY                                       | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 3: **0.5518** | MET, FRAMED, PICTURE, SHOW                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 4: **0.5241** | WHO, WHEN, SALLY, RABBIT                                          | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
2. **Partition Score: 0.5359**
   - Group 1: **0.5639** | HARRY, HORROR, ROCKY, FURY                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 2: **0.5518** | MET, FRAMED, PICTURE, SHOW                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 3: **0.5434** | ROGER, ROAD, MAX, MAD                                             | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 4: **0.5241** | WHO, WHEN, SALLY, RABBIT                                          | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
3. **Partition Score: 0.5317**
   - Group 1: **0.5518** | MET, FRAMED, PICTURE, SHOW                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 2: **0.5494** | MAX, HARRY, HORROR, ROCKY                                         | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 3: **0.5293** | ROGER, ROAD, MAD, FURY                                            | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 4: **0.5241** | WHO, WHEN, SALLY, RABBIT                                          | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
4. **Partition Score: 0.5305**
   - Group 1: **0.5518** | MET, FRAMED, PICTURE, SHOW                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 2: **0.5419** | ROGER, MAX, HARRY, ROCKY                                          | INCORRECT (Max overlap: 1/4 with WHO FRAMED ROGER RABBIT)
   - Group 3: **0.5319** | ROAD, MAD, HORROR, FURY                                           | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 4: **0.5241** | WHO, WHEN, SALLY, RABBIT                                          | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
5. **Partition Score: 0.5288**
   - Group 1: **0.5518** | MET, FRAMED, PICTURE, SHOW                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 2: **0.5505** | ROGER, HARRY, HORROR, RABBIT                                      | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
   - Group 3: **0.5477** | ROAD, MAD, ROCKY, FURY                                            | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 4: **0.5085** | MAX, WHO, WHEN, SALLY                                             | INCORRECT (Max overlap: 2/4 with WHEN HARRY MET SALLY)

### Top Candidate Groups:
   - Group 1: **0.5631** | ROAD, MAX, MAD, FURY                                              | CORRECT GROUP (MAD MAX FURY ROAD, Level 3)
   - Group 2: **0.5521** | ROGER, HARRY, HORROR, ROCKY                                       | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 3: **0.5518** | MET, FRAMED, PICTURE, SHOW                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 4: **0.5241** | WHO, WHEN, SALLY, RABBIT                                          | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
   - Group 5: **0.5639** | HARRY, HORROR, ROCKY, FURY                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 6: **0.5434** | ROGER, ROAD, MAX, MAD                                             | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 7: **0.5494** | MAX, HARRY, HORROR, ROCKY                                         | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 8: **0.5293** | ROGER, ROAD, MAD, FURY                                            | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 9: **0.5419** | ROGER, MAX, HARRY, ROCKY                                          | INCORRECT (Max overlap: 1/4 with WHO FRAMED ROGER RABBIT)
   - Group 10: **0.5319** | ROAD, MAD, HORROR, FURY                                           | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 11: **0.5505** | ROGER, HARRY, HORROR, RABBIT                                      | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
   - Group 12: **0.5477** | ROAD, MAD, ROCKY, FURY                                            | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 13: **0.5085** | MAX, WHO, WHEN, SALLY                                             | INCORRECT (Max overlap: 2/4 with WHEN HARRY MET SALLY)
   - Group 14: **0.5676** | ROAD, MAX, MAD, ROCKY                                             | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD)
   - Group 15: **0.5160** | ROGER, HARRY, HORROR, FURY                                        | INCORRECT (Max overlap: 1/4 with WHO FRAMED ROGER RABBIT)
   - Group 16: **0.5453** | ROGER, HARRY, HORROR, SALLY                                       | INCORRECT (Max overlap: 2/4 with WHEN HARRY MET SALLY)
   - Group 17: **0.5048** | WHO, WHEN, ROCKY, RABBIT                                          | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
   - Group 18: **0.5004** | WHO, WHEN, SALLY, ROCKY                                           | INCORRECT (Max overlap: 2/4 with WHEN HARRY MET SALLY)
   - Group 19: **0.5945** | ROGER, HARRY, ROCKY, RABBIT                                       | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
   - Group 20: **0.6422** | HARRY, HORROR, ROCKY, RABBIT                                      | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)

---

## Puzzle 28 (ID: 81)
**Words on Board:** SCRATCH, NICK, NACHO, DING, BINGO, LUMBER, WING, APPLE, POPPER, FRY, YES, RIGHT, CRACKER, CHIP, CORRECT, FLAP

### Ground Truth Categories:
* **Level 0 (APPETIZER UNIT) [Type: SEMANTIC_SET]:** FRY, NACHO, POPPER, WING
* **Level 1 (RESPONSE TO A CORRECT ANSWER) [Type: SYNONYM_OR_NEAR]:** BINGO, CORRECT, RIGHT, YES
* **Level 2 (MAR) [Type: SYNONYM_OR_NEAR]:** CHIP, DING, NICK, SCRATCH
* **Level 3 (___JACK) [Type: FILL_IN_THE_BLANK]:** APPLE, CRACKER, FLAP, LUMBER

### Top Candidate Partitions:
1. **Partition Score: 0.5423**
   - Group 1: **0.6726** | NICK, NACHO, DING, CHIP                                           | INCORRECT (Max overlap: 3/4 with MAR)
   - Group 2: **0.6342** | BINGO, LUMBER, APPLE, POPPER                                      | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 3: **0.5706** | WING, FRY, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT)
   - Group 4: **0.4823** | SCRATCH, YES, CRACKER, FLAP                                       | INCORRECT (Max overlap: 2/4 with ___JACK)
2. **Partition Score: 0.5412**
   - Group 1: **0.6198** | NICK, WING, RIGHT, CORRECT                                        | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 2: **0.6101** | SCRATCH, NACHO, FRY, CHIP                                         | INCORRECT (Max overlap: 2/4 with MAR)
   - Group 3: **0.5875** | LUMBER, APPLE, POPPER, CRACKER                                    | INCORRECT (Max overlap: 3/4 with ___JACK)
   - Group 4: **0.4836** | DING, BINGO, YES, FLAP                                            | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
3. **Partition Score: 0.5409**
   - Group 1: **0.6342** | BINGO, LUMBER, APPLE, POPPER                                      | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 2: **0.6198** | NICK, WING, RIGHT, CORRECT                                        | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 3: **0.5791** | NACHO, DING, FRY, CHIP                                            | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT)
   - Group 4: **0.4823** | SCRATCH, YES, CRACKER, FLAP                                       | INCORRECT (Max overlap: 2/4 with ___JACK)
4. **Partition Score: 0.5403**
   - Group 1: **0.6342** | BINGO, LUMBER, APPLE, POPPER                                      | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 2: **0.6264** | SCRATCH, NACHO, DING, CHIP                                        | INCORRECT (Max overlap: 3/4 with MAR)
   - Group 3: **0.5706** | WING, FRY, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT)
   - Group 4: **0.4820** | NICK, YES, CRACKER, FLAP                                          | INCORRECT (Max overlap: 2/4 with ___JACK)
5. **Partition Score: 0.5392**
   - Group 1: **0.6342** | BINGO, LUMBER, APPLE, POPPER                                      | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 2: **0.6198** | NICK, WING, RIGHT, CORRECT                                        | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 3: **0.6101** | SCRATCH, NACHO, FRY, CHIP                                         | INCORRECT (Max overlap: 2/4 with MAR)
   - Group 4: **0.4634** | DING, YES, CRACKER, FLAP                                          | INCORRECT (Max overlap: 2/4 with ___JACK)

### Top Candidate Groups:
   - Group 1: **0.6726** | NICK, NACHO, DING, CHIP                                           | INCORRECT (Max overlap: 3/4 with MAR)
   - Group 2: **0.6342** | BINGO, LUMBER, APPLE, POPPER                                      | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 3: **0.5706** | WING, FRY, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT)
   - Group 4: **0.4823** | SCRATCH, YES, CRACKER, FLAP                                       | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 5: **0.6198** | NICK, WING, RIGHT, CORRECT                                        | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 6: **0.6101** | SCRATCH, NACHO, FRY, CHIP                                         | INCORRECT (Max overlap: 2/4 with MAR)
   - Group 7: **0.5875** | LUMBER, APPLE, POPPER, CRACKER                                    | INCORRECT (Max overlap: 3/4 with ___JACK)
   - Group 8: **0.4836** | DING, BINGO, YES, FLAP                                            | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 9: **0.5791** | NACHO, DING, FRY, CHIP                                            | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT)
   - Group 10: **0.6264** | SCRATCH, NACHO, DING, CHIP                                        | INCORRECT (Max overlap: 3/4 with MAR)
   - Group 11: **0.4820** | NICK, YES, CRACKER, FLAP                                          | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 12: **0.4634** | DING, YES, CRACKER, FLAP                                          | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 13: **0.6112** | SCRATCH, NICK, DING, FLAP                                         | INCORRECT (Max overlap: 3/4 with MAR)
   - Group 14: **0.5285** | NACHO, FRY, CRACKER, CHIP                                         | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT)
   - Group 15: **0.5081** | WING, YES, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 3/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 16: **0.6187** | BINGO, LUMBER, APPLE, CRACKER                                     | INCORRECT (Max overlap: 3/4 with ___JACK)
   - Group 17: **0.4628** | DING, POPPER, YES, FLAP                                           | INCORRECT (Max overlap: 1/4 with MAR)
   - Group 18: **0.4938** | SCRATCH, BINGO, YES, FLAP                                         | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 19: **0.6749** | SCRATCH, NICK, NACHO, CHIP                                        | INCORRECT (Max overlap: 3/4 with MAR)
   - Group 20: **0.6770** | NICK, NACHO, FRY, CHIP                                            | INCORRECT (Max overlap: 2/4 with MAR)

---

## Puzzle 29 (ID: 1018)
**Words on Board:** PITCHER, ENTER, BOARD, MOMENTUM, ACCELERATION, POWER, FIGURE, ILLUSTRATION, FORCE, MOUNT, EMBARK, PLATE, MASS, ROBERT, PICTURE, FACE

### Ground Truth Categories:
* **Level 0 (STEP ONTO, AS A VEHICLE) [Type: SYNONYM_OR_NEAR]:** BOARD, EMBARK, ENTER, MOUNT
* **Level 1 (QUANTITIES IN MECHANICS) [Type: SEMANTIC_SET]:** ACCELERATION, FORCE, MASS, MOMENTUM
* **Level 2 (TEXTBOOK IMAGES) [Type: SYNONYM_OR_NEAR]:** FIGURE, ILLUSTRATION, PICTURE, PLATE
* **Level 3 (___ PLANT) [Type: FILL_IN_THE_BLANK]:** FACE, PITCHER, POWER, ROBERT

### Top Candidate Partitions:
1. **Partition Score: 0.5048**
   - Group 1: **0.6436** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS)
   - Group 2: **0.6390** | FIGURE, ILLUSTRATION, PLATE, PICTURE                              | CORRECT GROUP (TEXTBOOK IMAGES, Level 2)
   - Group 3: **0.5095** | ENTER, BOARD, EMBARK, FACE                                        | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 4: **0.4353** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)
2. **Partition Score: 0.5040**
   - Group 1: **0.6497** | MOMENTUM, ACCELERATION, FORCE, MASS                               | CORRECT GROUP (QUANTITIES IN MECHANICS, Level 1)
   - Group 2: **0.6390** | FIGURE, ILLUSTRATION, PLATE, PICTURE                              | CORRECT GROUP (TEXTBOOK IMAGES, Level 2)
   - Group 3: **0.5095** | ENTER, BOARD, EMBARK, FACE                                        | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 4: **0.4337** | PITCHER, POWER, MOUNT, ROBERT                                     | INCORRECT (Max overlap: 3/4 with ___ PLANT)
3. **Partition Score: 0.5021**
   - Group 1: **0.6684** | FIGURE, ILLUSTRATION, PICTURE, FACE                               | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 2: **0.6497** | MOMENTUM, ACCELERATION, FORCE, MASS                               | CORRECT GROUP (QUANTITIES IN MECHANICS, Level 1)
   - Group 3: **0.4915** | ENTER, BOARD, EMBARK, PLATE                                       | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 4: **0.4337** | PITCHER, POWER, MOUNT, ROBERT                                     | INCORRECT (Max overlap: 3/4 with ___ PLANT)
4. **Partition Score: 0.5014**
   - Group 1: **0.6684** | FIGURE, ILLUSTRATION, PICTURE, FACE                               | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 2: **0.6436** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS)
   - Group 3: **0.4915** | ENTER, BOARD, EMBARK, PLATE                                       | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 4: **0.4353** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)
5. **Partition Score: 0.4886**
   - Group 1: **0.6497** | MOMENTUM, ACCELERATION, FORCE, MASS                               | CORRECT GROUP (QUANTITIES IN MECHANICS, Level 1)
   - Group 2: **0.6390** | FIGURE, ILLUSTRATION, PLATE, PICTURE                              | CORRECT GROUP (TEXTBOOK IMAGES, Level 2)
   - Group 3: **0.4743** | ENTER, MOUNT, EMBARK, FACE                                        | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 4: **0.4205** | PITCHER, BOARD, POWER, ROBERT                                     | INCORRECT (Max overlap: 3/4 with ___ PLANT)

### Top Candidate Groups:
   - Group 1: **0.6436** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS)
   - Group 2: **0.6390** | FIGURE, ILLUSTRATION, PLATE, PICTURE                              | CORRECT GROUP (TEXTBOOK IMAGES, Level 2)
   - Group 3: **0.5095** | ENTER, BOARD, EMBARK, FACE                                        | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 4: **0.4353** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)
   - Group 5: **0.6497** | MOMENTUM, ACCELERATION, FORCE, MASS                               | CORRECT GROUP (QUANTITIES IN MECHANICS, Level 1)
   - Group 6: **0.4337** | PITCHER, POWER, MOUNT, ROBERT                                     | INCORRECT (Max overlap: 3/4 with ___ PLANT)
   - Group 7: **0.6684** | FIGURE, ILLUSTRATION, PICTURE, FACE                               | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 8: **0.4915** | ENTER, BOARD, EMBARK, PLATE                                       | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 9: **0.4743** | ENTER, MOUNT, EMBARK, FACE                                        | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 10: **0.4205** | PITCHER, BOARD, POWER, ROBERT                                     | INCORRECT (Max overlap: 3/4 with ___ PLANT)
   - Group 11: **0.6247** | ENTER, FIGURE, ILLUSTRATION, PICTURE                              | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 12: **0.4546** | BOARD, EMBARK, PLATE, FACE                                        | INCORRECT (Max overlap: 2/4 with STEP ONTO, AS A VEHICLE)
   - Group 13: **0.5593** | ILLUSTRATION, PLATE, PICTURE, FACE                                | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 14: **0.5009** | ENTER, BOARD, FIGURE, EMBARK                                      | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 15: **0.4362** | ENTER, MOUNT, EMBARK, PLATE                                       | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE)
   - Group 16: **0.4834** | MOMENTUM, FORCE, MOUNT, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS)
   - Group 17: **0.4432** | PITCHER, ACCELERATION, POWER, ROBERT                              | INCORRECT (Max overlap: 3/4 with ___ PLANT)
   - Group 18: **0.5874** | MOMENTUM, ACCELERATION, POWER, MASS                               | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS)
   - Group 19: **0.4598** | ENTER, FIGURE, FORCE, EMBARK                                      | INCORRECT (Max overlap: 2/4 with STEP ONTO, AS A VEHICLE)
   - Group 20: **0.4292** | PITCHER, BOARD, MOUNT, ROBERT                                     | INCORRECT (Max overlap: 2/4 with ___ PLANT)

---

## Puzzle 30 (ID: 915)
**Words on Board:** ARE, PALAZZO, GAUCHO, GOODEN, HAREM, SEAVER, PIAZZA, STRAWBERRY, MORTGAGE, HER, CULOTTE, POIROT, HERCULE, AJA, APOSTLE, DEPOT

### Ground Truth Categories:
* **Level 0 (WIDE-LEGGED PANT STYLES) [Type: SEMANTIC_SET]:** CULOTTE, GAUCHO, HAREM, PALAZZO
* **Level 1 (SILENT "T") [Type: SOUND_OR_SPELLING]:** APOSTLE, DEPOT, MORTGAGE, POIROT
* **Level 2 (NEW YORK METS LEGENDS) [Type: NAMED_ENTITY_SET]:** GOODEN, PIAZZA, SEAVER, STRAWBERRY
* **Level 3 (GREEK MYTHOLOGICAL FIGURES MINUS A LETTER) [Type: WORDPLAY_TRANSFORM]:** AJA, ARE, HER, HERCULE

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.5975** | PALAZZO, GAUCHO, CULOTTE, POIROT                                  | INCORRECT (Max overlap: 3/4 with WIDE-LEGGED PANT STYLES)
   - Group 2: **0.5931** | PALAZZO, SEAVER, PIAZZA, POIROT                                   | INCORRECT (Max overlap: 2/4 with NEW YORK METS LEGENDS)
   - Group 3: **0.5795** | PALAZZO, GAUCHO, PIAZZA, POIROT                                   | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 4: **0.5631** | PALAZZO, GAUCHO, SEAVER, PIAZZA                                   | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 5: **0.5622** | PALAZZO, GAUCHO, SEAVER, POIROT                                   | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 6: **0.5528** | GAUCHO, SEAVER, PIAZZA, POIROT                                    | INCORRECT (Max overlap: 2/4 with NEW YORK METS LEGENDS)
   - Group 7: **0.5411** | GAUCHO, PIAZZA, CULOTTE, POIROT                                   | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 8: **0.5343** | PALAZZO, SEAVER, PIAZZA, DEPOT                                    | INCORRECT (Max overlap: 2/4 with NEW YORK METS LEGENDS)
   - Group 9: **0.5315** | PALAZZO, SEAVER, POIROT, HERCULE                                  | INCORRECT (Max overlap: 1/4 with WIDE-LEGGED PANT STYLES)
   - Group 10: **0.5312** | PALAZZO, CULOTTE, POIROT, HERCULE                                 | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 11: **0.5297** | PALAZZO, PIAZZA, CULOTTE, POIROT                                  | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 12: **0.5287** | PALAZZO, SEAVER, CULOTTE, POIROT                                  | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 13: **0.5224** | PALAZZO, GAUCHO, PIAZZA, CULOTTE                                  | INCORRECT (Max overlap: 3/4 with WIDE-LEGGED PANT STYLES)
   - Group 14: **0.5215** | GAUCHO, STRAWBERRY, CULOTTE, POIROT                               | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 15: **0.5209** | PALAZZO, GAUCHO, HAREM, CULOTTE                                   | CORRECT GROUP (WIDE-LEGGED PANT STYLES, Level 0)
   - Group 16: **0.5209** | GAUCHO, SEAVER, CULOTTE, POIROT                                   | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 17: **0.5156** | PALAZZO, GAUCHO, PIAZZA, DEPOT                                    | INCORRECT (Max overlap: 2/4 with WIDE-LEGGED PANT STYLES)
   - Group 18: **0.5149** | PALAZZO, GAUCHO, STRAWBERRY, CULOTTE                              | INCORRECT (Max overlap: 3/4 with WIDE-LEGGED PANT STYLES)
   - Group 19: **0.5149** | PALAZZO, GAUCHO, SEAVER, CULOTTE                                  | INCORRECT (Max overlap: 3/4 with WIDE-LEGGED PANT STYLES)
   - Group 20: **0.5124** | GAUCHO, HAREM, CULOTTE, POIROT                                    | INCORRECT (Max overlap: 3/4 with WIDE-LEGGED PANT STYLES)

---

## Puzzle 31 (ID: 247)
**Words on Board:** SNACK, DAIRY, MOZZARELLA, JAWBREAKER, GOAD, PRODUCE, URGE, SPUR, BANANAS, FROZEN, FIGURE, ORANGE, STEADY, EGG, MEATBALL, FISH

### Ground Truth Categories:
* **Level 0 (ENCOURAGE, WITH "ON") [Type: COMMON_PHRASE]:** EGG, GOAD, SPUR, URGE
* **Level 1 (SPHERICAL FOODS) [Type: SEMANTIC_SET]:** JAWBREAKER, MEATBALL, MOZZARELLA, ORANGE
* **Level 2 (GROCERY STORE AISLES) [Type: SEMANTIC_SET]:** DAIRY, FROZEN, PRODUCE, SNACK
* **Level 3 (GO ___) [Type: FILL_IN_THE_BLANK]:** BANANAS, FIGURE, FISH, STEADY

### Top Candidate Partitions:
1. **Partition Score: 0.5663**
   - Group 1: **0.6373** | DAIRY, BANANAS, ORANGE, FISH                                      | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 2: **0.5867** | SNACK, MOZZARELLA, EGG, MEATBALL                                  | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 3: **0.5611** | PRODUCE, FROZEN, FIGURE, STEADY                                   | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 4: **0.5587** | JAWBREAKER, GOAD, URGE, SPUR                                      | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON")
2. **Partition Score: 0.5620**
   - Group 1: **0.6428** | DAIRY, ORANGE, EGG, FISH                                          | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
   - Group 2: **0.5695** | SNACK, MOZZARELLA, BANANAS, MEATBALL                              | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 3: **0.5611** | PRODUCE, FROZEN, FIGURE, STEADY                                   | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 4: **0.5587** | JAWBREAKER, GOAD, URGE, SPUR                                      | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON")
3. **Partition Score: 0.5606**
   - Group 1: **0.5867** | SNACK, MOZZARELLA, EGG, MEATBALL                                  | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 2: **0.5658** | DAIRY, FROZEN, ORANGE, STEADY                                     | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 3: **0.5589** | PRODUCE, BANANAS, FIGURE, FISH                                    | INCORRECT (Max overlap: 3/4 with GO ___)
   - Group 4: **0.5587** | JAWBREAKER, GOAD, URGE, SPUR                                      | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON")
4. **Partition Score: 0.5600**
   - Group 1: **0.6029** | DAIRY, MOZZARELLA, BANANAS, ORANGE                                | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 2: **0.5614** | SNACK, EGG, MEATBALL, FISH                                        | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
   - Group 3: **0.5611** | PRODUCE, FROZEN, FIGURE, STEADY                                   | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 4: **0.5587** | JAWBREAKER, GOAD, URGE, SPUR                                      | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON")
5. **Partition Score: 0.5600**
   - Group 1: **0.6019** | MOZZARELLA, BANANAS, ORANGE, FISH                                 | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 2: **0.5612** | SNACK, DAIRY, EGG, MEATBALL                                       | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 3: **0.5611** | PRODUCE, FROZEN, FIGURE, STEADY                                   | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 4: **0.5587** | JAWBREAKER, GOAD, URGE, SPUR                                      | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON")

### Top Candidate Groups:
   - Group 1: **0.6373** | DAIRY, BANANAS, ORANGE, FISH                                      | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 2: **0.5867** | SNACK, MOZZARELLA, EGG, MEATBALL                                  | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 3: **0.5611** | PRODUCE, FROZEN, FIGURE, STEADY                                   | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 4: **0.5587** | JAWBREAKER, GOAD, URGE, SPUR                                      | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON")
   - Group 5: **0.6428** | DAIRY, ORANGE, EGG, FISH                                          | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
   - Group 6: **0.5695** | SNACK, MOZZARELLA, BANANAS, MEATBALL                              | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 7: **0.5658** | DAIRY, FROZEN, ORANGE, STEADY                                     | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 8: **0.5589** | PRODUCE, BANANAS, FIGURE, FISH                                    | INCORRECT (Max overlap: 3/4 with GO ___)
   - Group 9: **0.6029** | DAIRY, MOZZARELLA, BANANAS, ORANGE                                | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 10: **0.5614** | SNACK, EGG, MEATBALL, FISH                                        | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
   - Group 11: **0.6019** | MOZZARELLA, BANANAS, ORANGE, FISH                                 | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 12: **0.5612** | SNACK, DAIRY, EGG, MEATBALL                                       | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 13: **0.5600** | DAIRY, FROZEN, FIGURE, STEADY                                     | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 14: **0.5600** | PRODUCE, BANANAS, ORANGE, FISH                                    | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 15: **0.6142** | SNACK, DAIRY, BANANAS, ORANGE                                     | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 16: **0.5577** | MOZZARELLA, EGG, MEATBALL, FISH                                   | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS)
   - Group 17: **0.5566** | PRODUCE, ORANGE, EGG, FISH                                        | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
   - Group 18: **0.6680** | BANANAS, ORANGE, EGG, FISH                                        | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 19: **0.5532** | SNACK, DAIRY, MOZZARELLA, MEATBALL                                | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 20: **0.6083** | SNACK, ORANGE, EGG, FISH                                          | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)

---

## Puzzle 32 (ID: 60)
**Words on Board:** ANKLET, CHARM, PLEASE, TICKLE, RING, FIELD, PURGE, DIAMOND, BANGLE, RINK, SCREAM, BROOCH, SAW, PENDANT, COURT, DELIGHT

### Ground Truth Categories:
* **Level 0 (HORROR FRANCHISES) [Type: NAMED_ENTITY_SET]:** PURGE, RING, SAW, SCREAM
* **Level 1 (SPORTS VENUES) [Type: SEMANTIC_SET]:** COURT, DIAMOND, FIELD, RINK
* **Level 2 (MAKE HAPPY) [Type: SYNONYM_OR_NEAR]:** CHARM, DELIGHT, PLEASE, TICKLE
* **Level 3 (JEWELRY) [Type: SEMANTIC_SET]:** ANKLET, BANGLE, BROOCH, PENDANT

### Top Candidate Partitions:
1. **Partition Score: 0.5068**
   - Group 1: **0.5609** | ANKLET, PURGE, BANGLE, PENDANT                                    | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 2: **0.5599** | CHARM, PLEASE, SAW, DELIGHT                                       | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 3: **0.5012** | RING, DIAMOND, RINK, BROOCH                                       | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 4: **0.4831** | TICKLE, FIELD, SCREAM, COURT                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
2. **Partition Score: 0.5036**
   - Group 1: **0.5644** | ANKLET, BANGLE, SAW, PENDANT                                      | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 2: **0.5472** | CHARM, PLEASE, PURGE, DELIGHT                                     | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 3: **0.5012** | RING, DIAMOND, RINK, BROOCH                                       | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 4: **0.4831** | TICKLE, FIELD, SCREAM, COURT                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
3. **Partition Score: 0.5028**
   - Group 1: **0.5736** | ANKLET, CHARM, BANGLE, PENDANT                                    | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 2: **0.5437** | PLEASE, PURGE, SAW, DELIGHT                                       | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 3: **0.5012** | RING, DIAMOND, RINK, BROOCH                                       | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 4: **0.4831** | TICKLE, FIELD, SCREAM, COURT                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
4. **Partition Score: 0.5002**
   - Group 1: **0.5614** | ANKLET, BANGLE, PENDANT, DELIGHT                                  | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 2: **0.5333** | CHARM, PLEASE, PURGE, SAW                                         | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 3: **0.5012** | RING, DIAMOND, RINK, BROOCH                                       | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 4: **0.4831** | TICKLE, FIELD, SCREAM, COURT                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
5. **Partition Score: 0.4935**
   - Group 1: **0.5426** | CHARM, PURGE, SAW, DELIGHT                                        | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 2: **0.5065** | ANKLET, PLEASE, BANGLE, PENDANT                                   | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 3: **0.5012** | RING, DIAMOND, RINK, BROOCH                                       | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 4: **0.4831** | TICKLE, FIELD, SCREAM, COURT                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)

### Top Candidate Groups:
   - Group 1: **0.5609** | ANKLET, PURGE, BANGLE, PENDANT                                    | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 2: **0.5599** | CHARM, PLEASE, SAW, DELIGHT                                       | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 3: **0.5012** | RING, DIAMOND, RINK, BROOCH                                       | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 4: **0.4831** | TICKLE, FIELD, SCREAM, COURT                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 5: **0.5644** | ANKLET, BANGLE, SAW, PENDANT                                      | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 6: **0.5472** | CHARM, PLEASE, PURGE, DELIGHT                                     | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 7: **0.5736** | ANKLET, CHARM, BANGLE, PENDANT                                    | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 8: **0.5437** | PLEASE, PURGE, SAW, DELIGHT                                       | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 9: **0.5614** | ANKLET, BANGLE, PENDANT, DELIGHT                                  | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 10: **0.5333** | CHARM, PLEASE, PURGE, SAW                                         | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 11: **0.5426** | CHARM, PURGE, SAW, DELIGHT                                        | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 12: **0.5065** | ANKLET, PLEASE, BANGLE, PENDANT                                   | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 13: **0.5455** | CHARM, BANGLE, PENDANT, DELIGHT                                   | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 14: **0.4966** | ANKLET, PLEASE, PURGE, SAW                                        | INCORRECT (Max overlap: 2/4 with HORROR FRANCHISES)
   - Group 15: **0.5184** | PLEASE, PURGE, SAW, PENDANT                                       | INCORRECT (Max overlap: 2/4 with HORROR FRANCHISES)
   - Group 16: **0.4765** | ANKLET, CHARM, BANGLE, DELIGHT                                    | INCORRECT (Max overlap: 2/4 with JEWELRY)
   - Group 17: **0.4974** | ANKLET, CHARM, PURGE, SAW                                         | INCORRECT (Max overlap: 2/4 with HORROR FRANCHISES)
   - Group 18: **0.4783** | PLEASE, BANGLE, PENDANT, DELIGHT                                  | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)

---

## Puzzle 33 (ID: 246)
**Words on Board:** LAG, PARROT, APOLLO, CANDLES, DROP, MIME, MONKEY, FANTASTIC, FREEZE, SAILOR, SAMURAI, PRISONER, PRINCESS, REFEREE, GENIE, ECHO

### Ground Truth Categories:
* **Level 0 (BAD THINGS FOR A VIDEO CALL TO DO) [Type: SEMANTIC_SET]:** DROP, ECHO, FREEZE, LAG
* **Level 1 (COSTUMES WITH STRIPED SHIRTS) [Type: SEMANTIC_SET]:** MIME, PRISONER, REFEREE, SAILOR
* **Level 2 (SEEN IN “ALADDIN”) [Type: SEMANTIC_SET]:** GENIE, MONKEY, PARROT, PRINCESS
* **Level 3 (MOVIES MINUS NUMBERS) [Type: WORDPLAY_TRANSFORM]:** APOLLO, CANDLES, FANTASTIC, SAMURAI

### Top Candidate Partitions:
1. **Partition Score: 0.5149**
   - Group 1: **0.5610** | SAILOR, PRISONER, PRINCESS, REFEREE                               | INCORRECT (Max overlap: 3/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 2: **0.5237** | APOLLO, CANDLES, GENIE, ECHO                                      | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 3: **0.5219** | LAG, DROP, MONKEY, FREEZE                                         | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 4: **0.5069** | PARROT, MIME, FANTASTIC, SAMURAI                                  | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
2. **Partition Score: 0.5143**
   - Group 1: **0.5237** | APOLLO, CANDLES, GENIE, ECHO                                      | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 2: **0.5219** | LAG, DROP, MONKEY, FREEZE                                         | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 3: **0.5170** | MIME, SAILOR, SAMURAI, PRINCESS                                   | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 4: **0.5092** | PARROT, FANTASTIC, PRISONER, REFEREE                              | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
3. **Partition Score: 0.5131**
   - Group 1: **0.5237** | APOLLO, CANDLES, GENIE, ECHO                                      | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 2: **0.5219** | LAG, DROP, MONKEY, FREEZE                                         | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 3: **0.5127** | MIME, SAILOR, PRISONER, PRINCESS                                  | INCORRECT (Max overlap: 3/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 4: **0.5089** | PARROT, FANTASTIC, SAMURAI, REFEREE                               | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
4. **Partition Score: 0.5116**
   - Group 1: **0.5275** | PARROT, MIME, MONKEY, SAMURAI                                     | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 2: **0.5272** | FANTASTIC, SAILOR, PRISONER, PRINCESS                             | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 3: **0.5237** | APOLLO, CANDLES, GENIE, ECHO                                      | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 4: **0.4978** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
5. **Partition Score: 0.5110**
   - Group 1: **0.5729** | PARROT, MONKEY, FANTASTIC, SAILOR                                 | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 2: **0.5246** | MIME, SAMURAI, PRISONER, PRINCESS                                 | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 3: **0.5237** | APOLLO, CANDLES, GENIE, ECHO                                      | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 4: **0.4978** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)

### Top Candidate Groups:
   - Group 1: **0.5610** | SAILOR, PRISONER, PRINCESS, REFEREE                               | INCORRECT (Max overlap: 3/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 2: **0.5237** | APOLLO, CANDLES, GENIE, ECHO                                      | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 3: **0.5219** | LAG, DROP, MONKEY, FREEZE                                         | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 4: **0.5069** | PARROT, MIME, FANTASTIC, SAMURAI                                  | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 5: **0.5170** | MIME, SAILOR, SAMURAI, PRINCESS                                   | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 6: **0.5092** | PARROT, FANTASTIC, PRISONER, REFEREE                              | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 7: **0.5127** | MIME, SAILOR, PRISONER, PRINCESS                                  | INCORRECT (Max overlap: 3/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 8: **0.5089** | PARROT, FANTASTIC, SAMURAI, REFEREE                               | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 9: **0.5275** | PARROT, MIME, MONKEY, SAMURAI                                     | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 10: **0.5272** | FANTASTIC, SAILOR, PRISONER, PRINCESS                             | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 11: **0.4978** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 12: **0.5729** | PARROT, MONKEY, FANTASTIC, SAILOR                                 | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 13: **0.5246** | MIME, SAMURAI, PRISONER, PRINCESS                                 | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 14: **0.5476** | PARROT, MIME, MONKEY, SAILOR                                      | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 15: **0.5187** | FANTASTIC, SAMURAI, PRISONER, PRINCESS                            | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 16: **0.4962** | PARROT, FANTASTIC, SAILOR, REFEREE                                | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 17: **0.5371** | PARROT, MONKEY, FANTASTIC, PRISONER                               | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 18: **0.5596** | PARROT, FANTASTIC, SAILOR, PRINCESS                               | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 19: **0.5169** | MIME, MONKEY, SAMURAI, PRISONER                                   | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 20: **0.5051** | MIME, SAILOR, SAMURAI, PRISONER                                   | INCORRECT (Max overlap: 3/4 with COSTUMES WITH STRIPED SHIRTS)

---

## Puzzle 34 (ID: 315)
**Words on Board:** CYMBAL, SYMBOL, CAR, WIG, MODEL, SIMMER, TRACK, IDEAL, WAX, SCIMITAR, DRUM, EXAMPLE, CONDUCTOR, STATION, SYMPHONY, MARK

### Ground Truth Categories:
* **Level 0 (EMBODIMENT) [Type: SYNONYM_OR_NEAR]:** EXAMPLE, IDEAL, MODEL, SYMBOL
* **Level 1 (RELATED TO TRAINS) [Type: SEMANTIC_SET]:** CAR, CONDUCTOR, STATION, TRACK
* **Level 2 (STARTING WITH THE SAME SOUND) [Type: SOUND_OR_SPELLING]:** CYMBAL, SCIMITAR, SIMMER, SYMPHONY
* **Level 3 (EAR___) [Type: FILL_IN_THE_BLANK]:** DRUM, MARK, WAX, WIG

### Top Candidate Partitions:
1. **Partition Score: 0.5083**
   - Group 1: **0.6081** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT)
   - Group 2: **0.6054** | CAR, WIG, WAX, SCIMITAR                                           | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 3: **0.5462** | CYMBAL, DRUM, CONDUCTOR, SYMPHONY                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 4: **0.4408** | SYMBOL, SIMMER, TRACK, STATION                                    | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
2. **Partition Score: 0.5041**
   - Group 1: **0.6081** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT)
   - Group 2: **0.5803** | CYMBAL, SCIMITAR, CONDUCTOR, SYMPHONY                             | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 3: **0.5546** | CAR, WIG, WAX, DRUM                                               | INCORRECT (Max overlap: 3/4 with EAR___)
   - Group 4: **0.4408** | SYMBOL, SIMMER, TRACK, STATION                                    | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
3. **Partition Score: 0.4869**
   - Group 1: **0.6081** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT)
   - Group 2: **0.5499** | CYMBAL, SCIMITAR, DRUM, CONDUCTOR                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 3: **0.5159** | CAR, WIG, WAX, SYMPHONY                                           | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 4: **0.4408** | SYMBOL, SIMMER, TRACK, STATION                                    | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
4. **Partition Score: 0.4806**
   - Group 1: **0.6081** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT)
   - Group 2: **0.5446** | CYMBAL, CAR, WAX, DRUM                                            | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 3: **0.4963** | WIG, SCIMITAR, CONDUCTOR, SYMPHONY                                | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 4: **0.4408** | SYMBOL, SIMMER, TRACK, STATION                                    | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
5. **Partition Score: 0.4802**
   - Group 1: **0.6081** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT)
   - Group 2: **0.5598** | CYMBAL, CAR, WIG, WAX                                             | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 3: **0.4796** | SCIMITAR, DRUM, CONDUCTOR, SYMPHONY                               | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 4: **0.4408** | SYMBOL, SIMMER, TRACK, STATION                                    | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)

### Top Candidate Groups:
   - Group 1: **0.6081** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT)
   - Group 2: **0.6054** | CAR, WIG, WAX, SCIMITAR                                           | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 3: **0.5462** | CYMBAL, DRUM, CONDUCTOR, SYMPHONY                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 4: **0.4408** | SYMBOL, SIMMER, TRACK, STATION                                    | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
   - Group 5: **0.5803** | CYMBAL, SCIMITAR, CONDUCTOR, SYMPHONY                             | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 6: **0.5546** | CAR, WIG, WAX, DRUM                                               | INCORRECT (Max overlap: 3/4 with EAR___)
   - Group 7: **0.5499** | CYMBAL, SCIMITAR, DRUM, CONDUCTOR                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 8: **0.5159** | CAR, WIG, WAX, SYMPHONY                                           | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 9: **0.5446** | CYMBAL, CAR, WAX, DRUM                                            | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 10: **0.4963** | WIG, SCIMITAR, CONDUCTOR, SYMPHONY                                | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 11: **0.5598** | CYMBAL, CAR, WIG, WAX                                             | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 12: **0.4796** | SCIMITAR, DRUM, CONDUCTOR, SYMPHONY                               | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 13: **0.5538** | CYMBAL, WAX, SCIMITAR, SYMPHONY                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 14: **0.4784** | CAR, WIG, DRUM, CONDUCTOR                                         | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
   - Group 15: **0.5266** | CYMBAL, WIG, WAX, DRUM                                            | INCORRECT (Max overlap: 3/4 with EAR___)
   - Group 16: **0.4929** | CAR, SCIMITAR, CONDUCTOR, SYMPHONY                                | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
   - Group 17: **0.5566** | CYMBAL, WIG, WAX, SCIMITAR                                        | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 18: **0.4599** | CAR, DRUM, CONDUCTOR, SYMPHONY                                    | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
   - Group 19: **0.5174** | CYMBAL, CAR, DRUM, CONDUCTOR                                      | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
   - Group 20: **0.4979** | WIG, WAX, SCIMITAR, SYMPHONY                                      | INCORRECT (Max overlap: 2/4 with EAR___)

---

## Puzzle 35 (ID: 827)
**Words on Board:** TILE, COAST, LAMINATE, PIP, WOOD, FIREWORKS, SHORE, WAILER, BANSHEE, CHEMISTRY, CARPET, CONNECTION, STRAND, BANK, HEARTBREAKER, SPARK

### Ground Truth Categories:
* **Level 0 (FLOORING OPTIONS) [Type: SEMANTIC_SET]:** CARPET, LAMINATE, TILE, WOOD
* **Level 1 (BEACHY AREA) [Type: SYNONYM_OR_NEAR]:** BANK, COAST, SHORE, STRAND
* **Level 2 (ROMANTIC VIBE) [Type: SYNONYM_OR_NEAR]:** CHEMISTRY, CONNECTION, FIREWORKS, SPARK
* **Level 3 (MEMBER OF A CLASSIC BACKING BAND) [Type: NAMED_ENTITY_SET]:** BANSHEE, HEARTBREAKER, PIP, WAILER

### Top Candidate Partitions:
1. **Partition Score: 0.5951**
   - Group 1: **0.7148** | COAST, SHORE, STRAND, BANK                                        | CORRECT GROUP (BEACHY AREA, Level 1)
   - Group 2: **0.6723** | TILE, LAMINATE, WOOD, CARPET                                      | CORRECT GROUP (FLOORING OPTIONS, Level 0)
   - Group 3: **0.5805** | WAILER, CONNECTION, HEARTBREAKER, SPARK                           | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 4: **0.5638** | PIP, FIREWORKS, BANSHEE, CHEMISTRY                                | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
2. **Partition Score: 0.5694**
   - Group 1: **0.7148** | COAST, SHORE, STRAND, BANK                                        | CORRECT GROUP (BEACHY AREA, Level 1)
   - Group 2: **0.5890** | WOOD, FIREWORKS, BANSHEE, CHEMISTRY                               | INCORRECT (Max overlap: 2/4 with ROMANTIC VIBE)
   - Group 3: **0.5805** | WAILER, CONNECTION, HEARTBREAKER, SPARK                           | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 4: **0.5541** | TILE, LAMINATE, PIP, CARPET                                       | INCORRECT (Max overlap: 3/4 with FLOORING OPTIONS)
3. **Partition Score: 0.5630**
   - Group 1: **0.7148** | COAST, SHORE, STRAND, BANK                                        | CORRECT GROUP (BEACHY AREA, Level 1)
   - Group 2: **0.6723** | TILE, LAMINATE, WOOD, CARPET                                      | CORRECT GROUP (FLOORING OPTIONS, Level 0)
   - Group 3: **0.5303** | FIREWORKS, WAILER, BANSHEE, HEARTBREAKER                          | INCORRECT (Max overlap: 3/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 4: **0.5247** | PIP, CHEMISTRY, CONNECTION, SPARK                                 | INCORRECT (Max overlap: 3/4 with ROMANTIC VIBE)
4. **Partition Score: 0.5609**
   - Group 1: **0.7148** | COAST, SHORE, STRAND, BANK                                        | CORRECT GROUP (BEACHY AREA, Level 1)
   - Group 2: **0.6723** | TILE, LAMINATE, WOOD, CARPET                                      | CORRECT GROUP (FLOORING OPTIONS, Level 0)
   - Group 3: **0.6069** | FIREWORKS, BANSHEE, CHEMISTRY, SPARK                              | INCORRECT (Max overlap: 3/4 with ROMANTIC VIBE)
   - Group 4: **0.4821** | PIP, WAILER, CONNECTION, HEARTBREAKER                             | INCORRECT (Max overlap: 3/4 with MEMBER OF A CLASSIC BACKING BAND)
5. **Partition Score: 0.5573**
   - Group 1: **0.7148** | COAST, SHORE, STRAND, BANK                                        | CORRECT GROUP (BEACHY AREA, Level 1)
   - Group 2: **0.6723** | TILE, LAMINATE, WOOD, CARPET                                      | CORRECT GROUP (FLOORING OPTIONS, Level 0)
   - Group 3: **0.5501** | PIP, WAILER, CONNECTION, SPARK                                    | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 4: **0.5034** | FIREWORKS, BANSHEE, CHEMISTRY, HEARTBREAKER                       | INCORRECT (Max overlap: 2/4 with ROMANTIC VIBE)

### Top Candidate Groups:
   - Group 1: **0.7148** | COAST, SHORE, STRAND, BANK                                        | CORRECT GROUP (BEACHY AREA, Level 1)
   - Group 2: **0.6723** | TILE, LAMINATE, WOOD, CARPET                                      | CORRECT GROUP (FLOORING OPTIONS, Level 0)
   - Group 3: **0.5805** | WAILER, CONNECTION, HEARTBREAKER, SPARK                           | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 4: **0.5638** | PIP, FIREWORKS, BANSHEE, CHEMISTRY                                | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 5: **0.5890** | WOOD, FIREWORKS, BANSHEE, CHEMISTRY                               | INCORRECT (Max overlap: 2/4 with ROMANTIC VIBE)
   - Group 6: **0.5541** | TILE, LAMINATE, PIP, CARPET                                       | INCORRECT (Max overlap: 3/4 with FLOORING OPTIONS)
   - Group 7: **0.5303** | FIREWORKS, WAILER, BANSHEE, HEARTBREAKER                          | INCORRECT (Max overlap: 3/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 8: **0.5247** | PIP, CHEMISTRY, CONNECTION, SPARK                                 | INCORRECT (Max overlap: 3/4 with ROMANTIC VIBE)
   - Group 9: **0.6069** | FIREWORKS, BANSHEE, CHEMISTRY, SPARK                              | INCORRECT (Max overlap: 3/4 with ROMANTIC VIBE)
   - Group 10: **0.4821** | PIP, WAILER, CONNECTION, HEARTBREAKER                             | INCORRECT (Max overlap: 3/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 11: **0.5501** | PIP, WAILER, CONNECTION, SPARK                                    | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 12: **0.5034** | FIREWORKS, BANSHEE, CHEMISTRY, HEARTBREAKER                       | INCORRECT (Max overlap: 2/4 with ROMANTIC VIBE)
   - Group 13: **0.5415** | PIP, BANSHEE, CHEMISTRY, SPARK                                    | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 14: **0.5039** | FIREWORKS, WAILER, CONNECTION, HEARTBREAKER                       | INCORRECT (Max overlap: 2/4 with ROMANTIC VIBE)
   - Group 15: **0.5233** | FIREWORKS, WAILER, BANSHEE, CHEMISTRY                             | INCORRECT (Max overlap: 2/4 with ROMANTIC VIBE)
   - Group 16: **0.5102** | PIP, CONNECTION, HEARTBREAKER, SPARK                              | INCORRECT (Max overlap: 2/4 with MEMBER OF A CLASSIC BACKING BAND)
   - Group 17: **0.5511** | FIREWORKS, CHEMISTRY, CONNECTION, SPARK                           | CORRECT GROUP (ROMANTIC VIBE, Level 2)
   - Group 18: **0.4813** | PIP, WAILER, BANSHEE, HEARTBREAKER                                | CORRECT GROUP (MEMBER OF A CLASSIC BACKING BAND, Level 3)
   - Group 19: **0.5563** | PIP, FIREWORKS, CHEMISTRY, SPARK                                  | INCORRECT (Max overlap: 3/4 with ROMANTIC VIBE)
   - Group 20: **0.4756** | WAILER, BANSHEE, CONNECTION, HEARTBREAKER                         | INCORRECT (Max overlap: 3/4 with MEMBER OF A CLASSIC BACKING BAND)

---

## Puzzle 36 (ID: 852)
**Words on Board:** THIRD, DEVIL, MAGICIAN, STAR, CONTINENT, BIG, MAJOR, NAKED, SERIOUS, LOVERS, DEADLY SIN, MAGIC, WONDER, EVIL, SISTER, IMPORTANT

### Ground Truth Categories:
* **Level 0 (SIGNIFICANT) [Type: SYNONYM_OR_NEAR]:** BIG, IMPORTANT, MAJOR, SERIOUS
* **Level 1 (ONE IN A SEPTET) [Type: SEMANTIC_SET]:** CONTINENT, DEADLY SIN, SISTER, WONDER
* **Level 2 (TAROT CARDS, WITH "THE") [Type: NAMED_ENTITY_SET]:** DEVIL, LOVERS, MAGICIAN, STAR
* **Level 3 (___ EYE) [Type: FILL_IN_THE_BLANK]:** EVIL, MAGIC, NAKED, THIRD

### Top Candidate Partitions:
1. **Partition Score: 0.5457**
   - Group 1: **0.7388** | THIRD, MAJOR, SERIOUS, IMPORTANT                                  | INCORRECT (Max overlap: 3/4 with SIGNIFICANT)
   - Group 2: **0.6958** | DEVIL, DEADLY SIN, MAGIC, EVIL                                    | INCORRECT (Max overlap: 2/4 with ___ EYE)
   - Group 3: **0.5825** | MAGICIAN, NAKED, LOVERS, SISTER                                   | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 4: **0.4524** | STAR, CONTINENT, BIG, WONDER                                      | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
2. **Partition Score: 0.5415**
   - Group 1: **0.7388** | THIRD, MAJOR, SERIOUS, IMPORTANT                                  | INCORRECT (Max overlap: 3/4 with SIGNIFICANT)
   - Group 2: **0.6680** | DEVIL, NAKED, MAGIC, EVIL                                         | INCORRECT (Max overlap: 3/4 with ___ EYE)
   - Group 3: **0.5932** | MAGICIAN, LOVERS, DEADLY SIN, SISTER                              | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 4: **0.4524** | STAR, CONTINENT, BIG, WONDER                                      | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
3. **Partition Score: 0.5386**
   - Group 1: **0.7388** | THIRD, MAJOR, SERIOUS, IMPORTANT                                  | INCORRECT (Max overlap: 3/4 with SIGNIFICANT)
   - Group 2: **0.6544** | DEVIL, MAGICIAN, MAGIC, EVIL                                      | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 3: **0.5952** | NAKED, LOVERS, DEADLY SIN, SISTER                                 | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
   - Group 4: **0.4524** | STAR, CONTINENT, BIG, WONDER                                      | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
4. **Partition Score: 0.5367**
   - Group 1: **0.7388** | THIRD, MAJOR, SERIOUS, IMPORTANT                                  | INCORRECT (Max overlap: 3/4 with SIGNIFICANT)
   - Group 2: **0.6373** | DEVIL, LOVERS, DEADLY SIN, MAGIC                                  | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 3: **0.6048** | MAGICIAN, NAKED, EVIL, SISTER                                     | INCORRECT (Max overlap: 2/4 with ___ EYE)
   - Group 4: **0.4524** | STAR, CONTINENT, BIG, WONDER                                      | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
5. **Partition Score: 0.5352**
   - Group 1: **0.7388** | THIRD, MAJOR, SERIOUS, IMPORTANT                                  | INCORRECT (Max overlap: 3/4 with SIGNIFICANT)
   - Group 2: **0.6741** | DEVIL, LOVERS, MAGIC, EVIL                                        | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 3: **0.5619** | MAGICIAN, NAKED, DEADLY SIN, SISTER                               | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
   - Group 4: **0.4524** | STAR, CONTINENT, BIG, WONDER                                      | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)

### Top Candidate Groups:
   - Group 1: **0.7388** | THIRD, MAJOR, SERIOUS, IMPORTANT                                  | INCORRECT (Max overlap: 3/4 with SIGNIFICANT)
   - Group 2: **0.6958** | DEVIL, DEADLY SIN, MAGIC, EVIL                                    | INCORRECT (Max overlap: 2/4 with ___ EYE)
   - Group 3: **0.5825** | MAGICIAN, NAKED, LOVERS, SISTER                                   | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 4: **0.4524** | STAR, CONTINENT, BIG, WONDER                                      | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
   - Group 5: **0.6680** | DEVIL, NAKED, MAGIC, EVIL                                         | INCORRECT (Max overlap: 3/4 with ___ EYE)
   - Group 6: **0.5932** | MAGICIAN, LOVERS, DEADLY SIN, SISTER                              | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 7: **0.6544** | DEVIL, MAGICIAN, MAGIC, EVIL                                      | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 8: **0.5952** | NAKED, LOVERS, DEADLY SIN, SISTER                                 | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
   - Group 9: **0.6373** | DEVIL, LOVERS, DEADLY SIN, MAGIC                                  | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 10: **0.6048** | MAGICIAN, NAKED, EVIL, SISTER                                     | INCORRECT (Max overlap: 2/4 with ___ EYE)
   - Group 11: **0.6741** | DEVIL, LOVERS, MAGIC, EVIL                                        | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 12: **0.5619** | MAGICIAN, NAKED, DEADLY SIN, SISTER                               | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)
   - Group 13: **0.6641** | NAKED, LOVERS, MAGIC, SISTER                                      | INCORRECT (Max overlap: 2/4 with ___ EYE)
   - Group 14: **0.5718** | DEVIL, MAGICIAN, DEADLY SIN, EVIL                                 | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 15: **0.6776** | NAKED, MAGIC, EVIL, SISTER                                        | INCORRECT (Max overlap: 3/4 with ___ EYE)
   - Group 16: **0.5515** | DEVIL, MAGICIAN, LOVERS, DEADLY SIN                               | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH "THE")
   - Group 17: **0.6205** | DEVIL, LOVERS, DEADLY SIN, EVIL                                   | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 18: **0.6074** | MAGICIAN, NAKED, MAGIC, SISTER                                    | INCORRECT (Max overlap: 2/4 with ___ EYE)
   - Group 19: **0.6153** | DEVIL, NAKED, LOVERS, MAGIC                                       | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH "THE")
   - Group 20: **0.6118** | MAGICIAN, DEADLY SIN, EVIL, SISTER                                | INCORRECT (Max overlap: 2/4 with ONE IN A SEPTET)

---

## Puzzle 37 (ID: 900)
**Words on Board:** STRESS, BEAT, PROPER, FRET, TAKE, PEG, STRING, FAIR, RHYTHM, RIGHT, LOUDNESS, PICKUP, JUST, INTONATION, BEST, WORST

### Ground Truth Categories:
* **Level 0 (FITTING) [Type: SYNONYM_OR_NEAR]:** FAIR, JUST, PROPER, RIGHT
* **Level 1 (ACHIEVE VICTORY OVER) [Type: SYNONYM_OR_NEAR]:** BEAT, BEST, TAKE, WORST
* **Level 2 (PARTS OF AN ELECTRIC GUITAR) [Type: SEMANTIC_SET]:** FRET, PEG, PICKUP, STRING
* **Level 3 (PHONETIC ELEMENTS OF SPEECH) [Type: SEMANTIC_SET]:** INTONATION, LOUDNESS, RHYTHM, STRESS

### Top Candidate Partitions:
1. **Partition Score: 0.6205**
   - Group 1: **0.7258** | PROPER, FAIR, RIGHT, JUST                                         | CORRECT GROUP (FITTING, Level 0)
   - Group 2: **0.6388** | BEAT, TAKE, BEST, WORST                                           | CORRECT GROUP (ACHIEVE VICTORY OVER, Level 1)
   - Group 3: **0.6166** | STRESS, RHYTHM, LOUDNESS, INTONATION                              | CORRECT GROUP (PHONETIC ELEMENTS OF SPEECH, Level 3)
   - Group 4: **0.6134** | FRET, PEG, STRING, PICKUP                                         | CORRECT GROUP (PARTS OF AN ELECTRIC GUITAR, Level 2)
2. **Partition Score: 0.6082**
   - Group 1: **0.7258** | PROPER, FAIR, RIGHT, JUST                                         | CORRECT GROUP (FITTING, Level 0)
   - Group 2: **0.6464** | BEAT, FRET, BEST, WORST                                           | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)
   - Group 3: **0.6166** | STRESS, RHYTHM, LOUDNESS, INTONATION                              | CORRECT GROUP (PHONETIC ELEMENTS OF SPEECH, Level 3)
   - Group 4: **0.5849** | TAKE, PEG, STRING, PICKUP                                         | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
3. **Partition Score: 0.6064**
   - Group 1: **0.7258** | PROPER, FAIR, RIGHT, JUST                                         | CORRECT GROUP (FITTING, Level 0)
   - Group 2: **0.6166** | STRESS, RHYTHM, LOUDNESS, INTONATION                              | CORRECT GROUP (PHONETIC ELEMENTS OF SPEECH, Level 3)
   - Group 3: **0.6084** | BEAT, PEG, BEST, WORST                                            | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)
   - Group 4: **0.6004** | FRET, TAKE, STRING, PICKUP                                        | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
4. **Partition Score: 0.5931**
   - Group 1: **0.7258** | PROPER, FAIR, RIGHT, JUST                                         | CORRECT GROUP (FITTING, Level 0)
   - Group 2: **0.6166** | STRESS, RHYTHM, LOUDNESS, INTONATION                              | CORRECT GROUP (PHONETIC ELEMENTS OF SPEECH, Level 3)
   - Group 3: **0.5926** | FRET, PEG, STRING, WORST                                          | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 4: **0.5816** | BEAT, TAKE, PICKUP, BEST                                          | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)
5. **Partition Score: 0.5801**
   - Group 1: **0.7258** | PROPER, FAIR, RIGHT, JUST                                         | CORRECT GROUP (FITTING, Level 0)
   - Group 2: **0.6328** | FRET, TAKE, PEG, STRING                                           | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 3: **0.6166** | STRESS, RHYTHM, LOUDNESS, INTONATION                              | CORRECT GROUP (PHONETIC ELEMENTS OF SPEECH, Level 3)
   - Group 4: **0.5356** | BEAT, PICKUP, BEST, WORST                                         | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)

### Top Candidate Groups:
   - Group 1: **0.7258** | PROPER, FAIR, RIGHT, JUST                                         | CORRECT GROUP (FITTING, Level 0)
   - Group 2: **0.6388** | BEAT, TAKE, BEST, WORST                                           | CORRECT GROUP (ACHIEVE VICTORY OVER, Level 1)
   - Group 3: **0.6166** | STRESS, RHYTHM, LOUDNESS, INTONATION                              | CORRECT GROUP (PHONETIC ELEMENTS OF SPEECH, Level 3)
   - Group 4: **0.6134** | FRET, PEG, STRING, PICKUP                                         | CORRECT GROUP (PARTS OF AN ELECTRIC GUITAR, Level 2)
   - Group 5: **0.6464** | BEAT, FRET, BEST, WORST                                           | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)
   - Group 6: **0.5849** | TAKE, PEG, STRING, PICKUP                                         | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 7: **0.6084** | BEAT, PEG, BEST, WORST                                            | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)
   - Group 8: **0.6004** | FRET, TAKE, STRING, PICKUP                                        | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 9: **0.5926** | FRET, PEG, STRING, WORST                                          | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 10: **0.5816** | BEAT, TAKE, PICKUP, BEST                                          | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)
   - Group 11: **0.6328** | FRET, TAKE, PEG, STRING                                           | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 12: **0.5356** | BEAT, PICKUP, BEST, WORST                                         | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)
   - Group 13: **0.5730** | BEAT, TAKE, STRING, PICKUP                                        | INCORRECT (Max overlap: 2/4 with ACHIEVE VICTORY OVER)
   - Group 14: **0.5527** | FRET, PEG, BEST, WORST                                            | INCORRECT (Max overlap: 2/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 15: **0.5595** | BEAT, PEG, STRING, PICKUP                                         | INCORRECT (Max overlap: 3/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 16: **0.5589** | FRET, TAKE, BEST, WORST                                           | INCORRECT (Max overlap: 3/4 with ACHIEVE VICTORY OVER)
   - Group 17: **0.5742** | FRET, TAKE, STRING, WORST                                         | INCORRECT (Max overlap: 2/4 with PARTS OF AN ELECTRIC GUITAR)
   - Group 18: **0.5478** | BEAT, PEG, PICKUP, BEST                                           | INCORRECT (Max overlap: 2/4 with ACHIEVE VICTORY OVER)
   - Group 19: **0.5772** | BEAT, TAKE, PEG, PICKUP                                           | INCORRECT (Max overlap: 2/4 with ACHIEVE VICTORY OVER)
   - Group 20: **0.5452** | FRET, STRING, BEST, WORST                                         | INCORRECT (Max overlap: 2/4 with PARTS OF AN ELECTRIC GUITAR)

---

## Puzzle 38 (ID: 372)
**Words on Board:** SEND, MAIL, BALM, FIX, LINER, STAIN, ANGLE, HOLE, CORNER, POST, TEMPERATURE, GLOSS, EDUCATION, CRIME, SPOT, SHIP

### Ground Truth Categories:
* **Level 0 (DELIVER, AS A PACKAGE) [Type: SYNONYM_OR_NEAR]:** MAIL, POST, SEND, SHIP
* **Level 1 (KINDS OF LIP MAKEUP) [Type: SEMANTIC_SET]:** BALM, GLOSS, LINER, STAIN
* **Level 2 (PREDICAMENT) [Type: SYNONYM_OR_NEAR]:** CORNER, FIX, HOLE, SPOT
* **Level 3 (MEASURED IN DEGREES) [Type: SEMANTIC_SET]:** ANGLE, CRIME, EDUCATION, TEMPERATURE

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6898** | SEND, MAIL, POST, SHIP                                            | CORRECT GROUP (DELIVER, AS A PACKAGE, Level 0)
   - Group 2: **0.5989** | BALM, STAIN, GLOSS, SPOT                                          | INCORRECT (Max overlap: 3/4 with KINDS OF LIP MAKEUP)
   - Group 3: **0.5931** | BALM, TEMPERATURE, EDUCATION, CRIME                               | INCORRECT (Max overlap: 3/4 with MEASURED IN DEGREES)
   - Group 4: **0.5824** | BALM, EDUCATION, CRIME, SPOT                                      | INCORRECT (Max overlap: 2/4 with MEASURED IN DEGREES)
   - Group 5: **0.5581** | STAIN, POST, GLOSS, SPOT                                          | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 6: **0.5550** | BALM, GLOSS, EDUCATION, SPOT                                      | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 7: **0.5532** | BALM, GLOSS, CRIME, SPOT                                          | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 8: **0.5525** | STAIN, GLOSS, CRIME, SPOT                                         | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 9: **0.5523** | STAIN, EDUCATION, CRIME, SPOT                                     | INCORRECT (Max overlap: 2/4 with MEASURED IN DEGREES)
   - Group 10: **0.5489** | STAIN, GLOSS, EDUCATION, SPOT                                     | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 11: **0.5462** | BALM, STAIN, EDUCATION, CRIME                                     | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 12: **0.5423** | BALM, STAIN, CRIME, SPOT                                          | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 13: **0.5417** | POST, CRIME, SPOT, SHIP                                           | INCORRECT (Max overlap: 2/4 with DELIVER, AS A PACKAGE)
   - Group 14: **0.5416** | BALM, TEMPERATURE, EDUCATION, SPOT                                | INCORRECT (Max overlap: 2/4 with MEASURED IN DEGREES)
   - Group 15: **0.5356** | BALM, GLOSS, EDUCATION, CRIME                                     | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 16: **0.5338** | BALM, STAIN, EDUCATION, SPOT                                      | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 17: **0.5326** | BALM, TEMPERATURE, CRIME, SPOT                                    | INCORRECT (Max overlap: 2/4 with MEASURED IN DEGREES)
   - Group 18: **0.5309** | TEMPERATURE, EDUCATION, CRIME, SPOT                               | INCORRECT (Max overlap: 3/4 with MEASURED IN DEGREES)
   - Group 19: **0.5296** | STAIN, POST, SPOT, SHIP                                           | INCORRECT (Max overlap: 2/4 with DELIVER, AS A PACKAGE)
   - Group 20: **0.5283** | POST, EDUCATION, CRIME, SPOT                                      | INCORRECT (Max overlap: 2/4 with MEASURED IN DEGREES)

---

## Puzzle 39 (ID: 953)
**Words on Board:** BROOKLYN, KILLER, WEAVE, GOLDEN GATE, RIALTO, CARPENTER, CRAVEN, WANTON, TWIST, NEEDLE, DESIREE, BUMBLE, TOWER, HONEY, WIND, LACE

### Ground Truth Categories:
* **Level 0 (INTERTWINE) [Type: SYNONYM_OR_NEAR]:** LACE, TWIST, WEAVE, WIND
* **Level 1 (KINDS OF BEES) [Type: NAMED_ENTITY_SET]:** BUMBLE, CARPENTER, HONEY, KILLER
* **Level 2 (FAMOUS BRIDGES) [Type: NAMED_ENTITY_SET]:** BROOKLYN, GOLDEN GATE, RIALTO, TOWER
* **Level 3 (STARTING WITH SYNONYMS FOR "HANKER FOR") [Type: WORDPLAY_TRANSFORM]:** CRAVEN, DESIREE, NEEDLE, WANTON

### Top Candidate Partitions:
1. **Partition Score: 0.5464**
   - Group 1: **0.7202** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0)
   - Group 2: **0.6166** | BROOKLYN, GOLDEN GATE, RIALTO, DESIREE                            | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES)
   - Group 3: **0.5239** | CARPENTER, CRAVEN, WANTON, TOWER                                  | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 4: **0.5225** | KILLER, NEEDLE, BUMBLE, HONEY                                     | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
2. **Partition Score: 0.5447**
   - Group 1: **0.7202** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0)
   - Group 2: **0.6166** | BROOKLYN, GOLDEN GATE, RIALTO, DESIREE                            | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES)
   - Group 3: **0.5909** | CARPENTER, CRAVEN, NEEDLE, TOWER                                  | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 4: **0.4855** | KILLER, WANTON, BUMBLE, HONEY                                     | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
3. **Partition Score: 0.5433**
   - Group 1: **0.7202** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0)
   - Group 2: **0.6166** | BROOKLYN, GOLDEN GATE, RIALTO, DESIREE                            | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES)
   - Group 3: **0.5490** | CARPENTER, BUMBLE, TOWER, HONEY                                   | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 4: **0.5037** | KILLER, CRAVEN, WANTON, NEEDLE                                    | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
4. **Partition Score: 0.5430**
   - Group 1: **0.7202** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0)
   - Group 2: **0.6166** | BROOKLYN, GOLDEN GATE, RIALTO, DESIREE                            | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES)
   - Group 3: **0.5768** | KILLER, BUMBLE, TOWER, HONEY                                      | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 4: **0.4892** | CARPENTER, CRAVEN, WANTON, NEEDLE                                 | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
5. **Partition Score: 0.5424**
   - Group 1: **0.7202** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0)
   - Group 2: **0.5973** | KILLER, DESIREE, BUMBLE, HONEY                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 3: **0.5940** | BROOKLYN, GOLDEN GATE, RIALTO, TOWER                              | CORRECT GROUP (FAMOUS BRIDGES, Level 2)
   - Group 4: **0.4892** | CARPENTER, CRAVEN, WANTON, NEEDLE                                 | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")

### Top Candidate Groups:
   - Group 1: **0.7202** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0)
   - Group 2: **0.6166** | BROOKLYN, GOLDEN GATE, RIALTO, DESIREE                            | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES)
   - Group 3: **0.5239** | CARPENTER, CRAVEN, WANTON, TOWER                                  | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 4: **0.5225** | KILLER, NEEDLE, BUMBLE, HONEY                                     | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 5: **0.5909** | CARPENTER, CRAVEN, NEEDLE, TOWER                                  | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 6: **0.4855** | KILLER, WANTON, BUMBLE, HONEY                                     | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 7: **0.5490** | CARPENTER, BUMBLE, TOWER, HONEY                                   | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 8: **0.5037** | KILLER, CRAVEN, WANTON, NEEDLE                                    | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 9: **0.5768** | KILLER, BUMBLE, TOWER, HONEY                                      | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 10: **0.4892** | CARPENTER, CRAVEN, WANTON, NEEDLE                                 | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 11: **0.5973** | KILLER, DESIREE, BUMBLE, HONEY                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 12: **0.5940** | BROOKLYN, GOLDEN GATE, RIALTO, TOWER                              | CORRECT GROUP (FAMOUS BRIDGES, Level 2)
   - Group 13: **0.5655** | CARPENTER, DESIREE, BUMBLE, HONEY                                 | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 14: **0.5265** | CARPENTER, CRAVEN, WANTON, HONEY                                  | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 15: **0.5092** | KILLER, NEEDLE, BUMBLE, TOWER                                     | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 16: **0.5173** | KILLER, CARPENTER, NEEDLE, BUMBLE                                 | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 17: **0.5098** | CRAVEN, WANTON, TOWER, HONEY                                      | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 18: **0.5511** | CRAVEN, BUMBLE, TOWER, HONEY                                      | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 19: **0.4913** | KILLER, CARPENTER, WANTON, NEEDLE                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 20: **0.5554** | KILLER, CARPENTER, CRAVEN, WANTON                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)

---

## Puzzle 40 (ID: 20)
**Words on Board:** BROWN, RICE, BONG, LEE, PRINCE, KING, SPELT, BARLEY, RYE, DUKE, EARL, OAT, FORD, HOWARD, STONE, BARON

### Ground Truth Categories:
* **Level 0 (GRAINS) [Type: SEMANTIC_SET]:** BARLEY, OAT, RYE, SPELT
* **Level 1 (ROYAL TITLES) [Type: SEMANTIC_SET]:** BARON, EARL, KING, PRINCE
* **Level 2 (UNIVERSITIES) [Type: NAMED_ENTITY_SET]:** BROWN, DUKE, HOWARD, RICE
* **Level 3 (BEST DIRECTOR OSCAR WINNERS) [Type: NAMED_ENTITY_SET]:** BONG, FORD, LEE, STONE

### Top Candidate Partitions:
1. **Partition Score: 0.5367**
   - Group 1: **0.8857** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS)
   - Group 2: **0.5612** | PRINCE, KING, SPELT, BARON                                        | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 3: **0.5503** | LEE, DUKE, EARL, HOWARD                                           | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 4: **0.5177** | BROWN, BONG, FORD, STONE                                          | INCORRECT (Max overlap: 3/4 with BEST DIRECTOR OSCAR WINNERS)
2. **Partition Score: 0.5222**
   - Group 1: **0.8857** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS)
   - Group 2: **0.5612** | PRINCE, KING, SPELT, BARON                                        | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 3: **0.5197** | BROWN, DUKE, EARL, HOWARD                                         | INCORRECT (Max overlap: 3/4 with UNIVERSITIES)
   - Group 4: **0.5039** | BONG, LEE, FORD, STONE                                            | CORRECT GROUP (BEST DIRECTOR OSCAR WINNERS, Level 3)
3. **Partition Score: 0.5198**
   - Group 1: **0.8857** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS)
   - Group 2: **0.5612** | PRINCE, KING, SPELT, BARON                                        | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 3: **0.5271** | LEE, DUKE, FORD, HOWARD                                           | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 4: **0.4954** | BROWN, BONG, EARL, STONE                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
4. **Partition Score: 0.5175**
   - Group 1: **0.8857** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS)
   - Group 2: **0.5447** | BROWN, LEE, FORD, HOWARD                                          | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 3: **0.5149** | BONG, KING, SPELT, STONE                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 4: **0.5052** | PRINCE, DUKE, EARL, BARON                                         | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
5. **Partition Score: 0.5170**
   - Group 1: **0.8857** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS)
   - Group 2: **0.5612** | PRINCE, KING, SPELT, BARON                                        | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 3: **0.5028** | BROWN, BONG, FORD, HOWARD                                         | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 4: **0.5020** | LEE, DUKE, EARL, STONE                                            | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)

### Top Candidate Groups:
   - Group 1: **0.8857** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS)
   - Group 2: **0.5612** | PRINCE, KING, SPELT, BARON                                        | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 3: **0.5503** | LEE, DUKE, EARL, HOWARD                                           | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 4: **0.5177** | BROWN, BONG, FORD, STONE                                          | INCORRECT (Max overlap: 3/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 5: **0.5197** | BROWN, DUKE, EARL, HOWARD                                         | INCORRECT (Max overlap: 3/4 with UNIVERSITIES)
   - Group 6: **0.5039** | BONG, LEE, FORD, STONE                                            | CORRECT GROUP (BEST DIRECTOR OSCAR WINNERS, Level 3)
   - Group 7: **0.5271** | LEE, DUKE, FORD, HOWARD                                           | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 8: **0.4954** | BROWN, BONG, EARL, STONE                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 9: **0.5447** | BROWN, LEE, FORD, HOWARD                                          | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 10: **0.5149** | BONG, KING, SPELT, STONE                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 11: **0.5052** | PRINCE, DUKE, EARL, BARON                                         | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 12: **0.5028** | BROWN, BONG, FORD, HOWARD                                         | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 13: **0.5020** | LEE, DUKE, EARL, STONE                                            | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 14: **0.6994** | SPELT, BARLEY, RYE, OAT                                           | CORRECT GROUP (GRAINS, Level 0)
   - Group 15: **0.5412** | PRINCE, KING, EARL, BARON                                         | CORRECT GROUP (ROYAL TITLES, Level 1)
   - Group 16: **0.4972** | BROWN, RICE, BONG, STONE                                          | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 17: **0.5420** | BROWN, BONG, LEE, STONE                                           | INCORRECT (Max overlap: 3/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 18: **0.4747** | DUKE, EARL, FORD, HOWARD                                          | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 19: **0.5575** | BROWN, LEE, DUKE, STONE                                           | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)
   - Group 20: **0.4652** | BONG, EARL, FORD, HOWARD                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)

---

## Puzzle 41 (ID: 501)
**Words on Board:** BILL, ADIEU, GAMES, AUDIO, SCHEDULE, NEWS, PROGRAM, TEMPS, AIRPLANE, FORTUNE TELLER, BELLE, PAIN, SLATE, COOKING, FAN, CRANE

### Ground Truth Categories:
* **Level 0 (LINEUP) [Type: SYNONYM_OR_NEAR]:** BILL, PROGRAM, SCHEDULE, SLATE
* **Level 1 (NYT OFFERINGS) [Type: NAMED_ENTITY_SET]:** AUDIO, COOKING, GAMES, NEWS
* **Level 2 (THINGS MADE BY FOLDING PAPER) [Type: SEMANTIC_SET]:** AIRPLANE, CRANE, FAN, FORTUNE TELLER
* **Level 3 (FRENCH WORDS) [Type: SEMANTIC_SET]:** ADIEU, BELLE, PAIN, TEMPS

### Top Candidate Partitions:
1. **Partition Score: 0.5234**
   - Group 1: **0.5608** | GAMES, TEMPS, PAIN, FAN                                           | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 2: **0.5380** | SCHEDULE, NEWS, PROGRAM, SLATE                                    | INCORRECT (Max overlap: 3/4 with LINEUP)
   - Group 3: **0.5321** | BILL, ADIEU, AIRPLANE, CRANE                                      | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 4: **0.5116** | AUDIO, FORTUNE TELLER, BELLE, COOKING                             | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
2. **Partition Score: 0.5218**
   - Group 1: **0.5608** | GAMES, TEMPS, PAIN, FAN                                           | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 2: **0.5536** | FORTUNE TELLER, BELLE, COOKING, CRANE                             | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 3: **0.5380** | SCHEDULE, NEWS, PROGRAM, SLATE                                    | INCORRECT (Max overlap: 3/4 with LINEUP)
   - Group 4: **0.4978** | BILL, ADIEU, AUDIO, AIRPLANE                                      | INCORRECT (Max overlap: 1/4 with LINEUP)
3. **Partition Score: 0.5217**
   - Group 1: **0.5608** | GAMES, TEMPS, PAIN, FAN                                           | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 2: **0.5380** | SCHEDULE, NEWS, PROGRAM, SLATE                                    | INCORRECT (Max overlap: 3/4 with LINEUP)
   - Group 3: **0.5352** | ADIEU, AUDIO, FORTUNE TELLER, BELLE                               | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 4: **0.5068** | BILL, AIRPLANE, COOKING, CRANE                                    | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
4. **Partition Score: 0.5171**
   - Group 1: **0.5546** | GAMES, TEMPS, PAIN, COOKING                                       | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
   - Group 2: **0.5380** | SCHEDULE, NEWS, PROGRAM, SLATE                                    | INCORRECT (Max overlap: 3/4 with LINEUP)
   - Group 3: **0.5352** | ADIEU, AUDIO, FORTUNE TELLER, BELLE                               | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 4: **0.4977** | BILL, AIRPLANE, FAN, CRANE                                        | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
5. **Partition Score: 0.5155**
   - Group 1: **0.5926** | AIRPLANE, FORTUNE TELLER, BELLE, CRANE                            | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 2: **0.5608** | GAMES, TEMPS, PAIN, FAN                                           | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 3: **0.5380** | SCHEDULE, NEWS, PROGRAM, SLATE                                    | INCORRECT (Max overlap: 3/4 with LINEUP)
   - Group 4: **0.4817** | BILL, ADIEU, AUDIO, COOKING                                       | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)

### Top Candidate Groups:
   - Group 1: **0.5608** | GAMES, TEMPS, PAIN, FAN                                           | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 2: **0.5380** | SCHEDULE, NEWS, PROGRAM, SLATE                                    | INCORRECT (Max overlap: 3/4 with LINEUP)
   - Group 3: **0.5321** | BILL, ADIEU, AIRPLANE, CRANE                                      | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 4: **0.5116** | AUDIO, FORTUNE TELLER, BELLE, COOKING                             | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
   - Group 5: **0.5536** | FORTUNE TELLER, BELLE, COOKING, CRANE                             | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 6: **0.4978** | BILL, ADIEU, AUDIO, AIRPLANE                                      | INCORRECT (Max overlap: 1/4 with LINEUP)
   - Group 7: **0.5352** | ADIEU, AUDIO, FORTUNE TELLER, BELLE                               | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 8: **0.5068** | BILL, AIRPLANE, COOKING, CRANE                                    | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 9: **0.5546** | GAMES, TEMPS, PAIN, COOKING                                       | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
   - Group 10: **0.4977** | BILL, AIRPLANE, FAN, CRANE                                        | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 11: **0.5926** | AIRPLANE, FORTUNE TELLER, BELLE, CRANE                            | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 12: **0.4817** | BILL, ADIEU, AUDIO, COOKING                                       | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
   - Group 13: **0.5234** | FORTUNE TELLER, BELLE, FAN, CRANE                                 | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 14: **0.5246** | TEMPS, PAIN, COOKING, FAN                                         | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 15: **0.4860** | BILL, GAMES, AIRPLANE, CRANE                                      | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 16: **0.5312** | FORTUNE TELLER, BELLE, COOKING, FAN                               | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 17: **0.4823** | GAMES, AUDIO, TEMPS, PAIN                                         | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
   - Group 18: **0.5389** | BILL, ADIEU, AIRPLANE, COOKING                                    | INCORRECT (Max overlap: 1/4 with LINEUP)
   - Group 19: **0.5144** | AUDIO, AIRPLANE, FORTUNE TELLER, BELLE                            | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 20: **0.4850** | BILL, ADIEU, GAMES, CRANE                                         | INCORRECT (Max overlap: 1/4 with LINEUP)

---

## Puzzle 42 (ID: 332)
**Words on Board:** RUBY, SPONGE, BUBBLE, SPLASH, DROP, CHERRY, BRICK, ROSE, PICK, TOP, SPOT, CREAM, BIRD, MUD, BEST, SPRINKLE

### Ground Truth Categories:
* **Level 0 (SHADES OF RED) [Type: SEMANTIC_SET]:** BRICK, CHERRY, ROSE, RUBY
* **Level 1 (LITTLE BIT OF A BEVERAGE) [Type: SYNONYM_OR_NEAR]:** DROP, SPLASH, SPOT, SPRINKLE
* **Level 2 (CHOICEST) [Type: SYNONYM_OR_NEAR]:** BEST, CREAM, PICK, TOP
* **Level 3 (___ BATH) [Type: FILL_IN_THE_BLANK]:** BIRD, BUBBLE, MUD, SPONGE

### Top Candidate Partitions:
1. **Partition Score: 0.5423**
   - Group 1: **0.6494** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 2: **0.6294** | DROP, PICK, SPOT, SPRINKLE                                        | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 3: **0.5201** | BRICK, TOP, CREAM, BEST                                           | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 4: **0.5098** | SPONGE, BUBBLE, SPLASH, MUD                                       | INCORRECT (Max overlap: 3/4 with ___ BATH)
2. **Partition Score: 0.5322**
   - Group 1: **0.6494** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 2: **0.6294** | DROP, PICK, SPOT, SPRINKLE                                        | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 3: **0.5292** | BUBBLE, SPLASH, BRICK, MUD                                        | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 4: **0.4851** | SPONGE, TOP, CREAM, BEST                                          | INCORRECT (Max overlap: 3/4 with CHOICEST)
3. **Partition Score: 0.5288**
   - Group 1: **0.7072** | SPLASH, DROP, SPOT, SPRINKLE                                      | CORRECT GROUP (LITTLE BIT OF A BEVERAGE, Level 1)
   - Group 2: **0.6494** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 3: **0.5603** | SPONGE, BUBBLE, BRICK, MUD                                        | INCORRECT (Max overlap: 3/4 with ___ BATH)
   - Group 4: **0.4528** | PICK, TOP, CREAM, BEST                                            | CORRECT GROUP (CHOICEST, Level 2)
4. **Partition Score: 0.5283**
   - Group 1: **0.7072** | SPLASH, DROP, SPOT, SPRINKLE                                      | CORRECT GROUP (LITTLE BIT OF A BEVERAGE, Level 1)
   - Group 2: **0.6494** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 3: **0.5023** | BUBBLE, BRICK, TOP, MUD                                           | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 4: **0.4807** | SPONGE, PICK, CREAM, BEST                                         | INCORRECT (Max overlap: 3/4 with CHOICEST)
5. **Partition Score: 0.5272**
   - Group 1: **0.6494** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 2: **0.6342** | SPLASH, SPOT, MUD, SPRINKLE                                       | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 3: **0.5235** | SPONGE, BUBBLE, BRICK, TOP                                        | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 4: **0.4755** | DROP, PICK, CREAM, BEST                                           | INCORRECT (Max overlap: 3/4 with CHOICEST)

### Top Candidate Groups:
   - Group 1: **0.6494** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 2: **0.6294** | DROP, PICK, SPOT, SPRINKLE                                        | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 3: **0.5201** | BRICK, TOP, CREAM, BEST                                           | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 4: **0.5098** | SPONGE, BUBBLE, SPLASH, MUD                                       | INCORRECT (Max overlap: 3/4 with ___ BATH)
   - Group 5: **0.5292** | BUBBLE, SPLASH, BRICK, MUD                                        | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 6: **0.4851** | SPONGE, TOP, CREAM, BEST                                          | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 7: **0.7072** | SPLASH, DROP, SPOT, SPRINKLE                                      | CORRECT GROUP (LITTLE BIT OF A BEVERAGE, Level 1)
   - Group 8: **0.5603** | SPONGE, BUBBLE, BRICK, MUD                                        | INCORRECT (Max overlap: 3/4 with ___ BATH)
   - Group 9: **0.4528** | PICK, TOP, CREAM, BEST                                            | CORRECT GROUP (CHOICEST, Level 2)
   - Group 10: **0.5023** | BUBBLE, BRICK, TOP, MUD                                           | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 11: **0.4807** | SPONGE, PICK, CREAM, BEST                                         | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 12: **0.6342** | SPLASH, SPOT, MUD, SPRINKLE                                       | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 13: **0.5235** | SPONGE, BUBBLE, BRICK, TOP                                        | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 14: **0.4755** | DROP, PICK, CREAM, BEST                                           | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 15: **0.5884** | DROP, PICK, SPOT, CREAM                                           | INCORRECT (Max overlap: 2/4 with LITTLE BIT OF A BEVERAGE)
   - Group 16: **0.5240** | BUBBLE, BRICK, TOP, BEST                                          | INCORRECT (Max overlap: 2/4 with CHOICEST)
   - Group 17: **0.4924** | SPONGE, SPLASH, MUD, SPRINKLE                                     | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 18: **0.5144** | SPONGE, BUBBLE, SPLASH, BRICK                                     | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 19: **0.4674** | TOP, CREAM, MUD, BEST                                             | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 20: **0.4866** | SPONGE, SPLASH, BRICK, MUD                                        | INCORRECT (Max overlap: 2/4 with ___ BATH)

---

## Puzzle 43 (ID: 614)
**Words on Board:** SURPRISE, SHED, INDULGE, HISS, SLITHER, RATTLE, BABY, STRAIGHT, BAE, CREAK, HUMOR, SEE, GUESS WHO, GOTCHA, PAMPER, BOO

### Ground Truth Categories:
* **Level 0 (MOLLYCODDLE) [Type: SYNONYM_OR_NEAR]:** BABY, HUMOR, INDULGE, PAMPER
* **Level 1 (THINGS A RATTLESNAKE DOES) [Type: SEMANTIC_SET]:** HISS, RATTLE, SHED, SLITHER
* **Level 2 (WORDS SAID TO AN UNSUSPECTING PERSON) [Type: SEMANTIC_SET]:** BOO, GOTCHA, GUESS WHO, SURPRISE
* **Level 3 (HOMOPHONES OF BODIES OF WATER) [Type: SOUND_OR_SPELLING]:** BAE, CREAK, SEE, STRAIGHT

### Top Candidate Partitions:
1. **Partition Score: 0.4610**
   - Group 1: **0.5581** | SHED, INDULGE, BABY, PAMPER                                       | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE)
   - Group 2: **0.5271** | HISS, SLITHER, RATTLE, CREAK                                      | INCORRECT (Max overlap: 3/4 with THINGS A RATTLESNAKE DOES)
   - Group 3: **0.4863** | SURPRISE, HUMOR, SEE, BOO                                         | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 4: **0.4154** | STRAIGHT, BAE, GUESS WHO, GOTCHA                                  | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
2. **Partition Score: 0.4591**
   - Group 1: **0.6267** | INDULGE, BABY, HUMOR, PAMPER                                      | CORRECT GROUP (MOLLYCODDLE, Level 0)
   - Group 2: **0.5271** | HISS, SLITHER, RATTLE, CREAK                                      | INCORRECT (Max overlap: 3/4 with THINGS A RATTLESNAKE DOES)
   - Group 3: **0.4784** | SURPRISE, SHED, SEE, BOO                                          | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 4: **0.4154** | STRAIGHT, BAE, GUESS WHO, GOTCHA                                  | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
3. **Partition Score: 0.4499**
   - Group 1: **0.4677** | INDULGE, SLITHER, BABY, PAMPER                                    | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE)
   - Group 2: **0.4576** | SURPRISE, SHED, HUMOR, BOO                                        | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 3: **0.4575** | HISS, RATTLE, STRAIGHT, CREAK                                     | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 4: **0.4421** | BAE, SEE, GUESS WHO, GOTCHA                                       | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
4. **Partition Score: 0.4450**
   - Group 1: **0.6267** | INDULGE, BABY, HUMOR, PAMPER                                      | CORRECT GROUP (MOLLYCODDLE, Level 0)
   - Group 2: **0.5060** | SURPRISE, SHED, SLITHER, SEE                                      | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 3: **0.4431** | HISS, RATTLE, CREAK, BOO                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 4: **0.4154** | STRAIGHT, BAE, GUESS WHO, GOTCHA                                  | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
5. **Partition Score: 0.4448**
   - Group 1: **0.6267** | INDULGE, BABY, HUMOR, PAMPER                                      | CORRECT GROUP (MOLLYCODDLE, Level 0)
   - Group 2: **0.5549** | HISS, RATTLE, BAE, CREAK                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 3: **0.4175** | SHED, SLITHER, SEE, BOO                                           | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 4: **0.4033** | SURPRISE, STRAIGHT, GUESS WHO, GOTCHA                             | INCORRECT (Max overlap: 3/4 with WORDS SAID TO AN UNSUSPECTING PERSON)

### Top Candidate Groups:
   - Group 1: **0.5581** | SHED, INDULGE, BABY, PAMPER                                       | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE)
   - Group 2: **0.5271** | HISS, SLITHER, RATTLE, CREAK                                      | INCORRECT (Max overlap: 3/4 with THINGS A RATTLESNAKE DOES)
   - Group 3: **0.4863** | SURPRISE, HUMOR, SEE, BOO                                         | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 4: **0.4154** | STRAIGHT, BAE, GUESS WHO, GOTCHA                                  | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 5: **0.6267** | INDULGE, BABY, HUMOR, PAMPER                                      | CORRECT GROUP (MOLLYCODDLE, Level 0)
   - Group 6: **0.4784** | SURPRISE, SHED, SEE, BOO                                          | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 7: **0.4677** | INDULGE, SLITHER, BABY, PAMPER                                    | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE)
   - Group 8: **0.4576** | SURPRISE, SHED, HUMOR, BOO                                        | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 9: **0.4575** | HISS, RATTLE, STRAIGHT, CREAK                                     | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 10: **0.4421** | BAE, SEE, GUESS WHO, GOTCHA                                       | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 11: **0.5060** | SURPRISE, SHED, SLITHER, SEE                                      | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 12: **0.4431** | HISS, RATTLE, CREAK, BOO                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 13: **0.5549** | HISS, RATTLE, BAE, CREAK                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 14: **0.4175** | SHED, SLITHER, SEE, BOO                                           | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 15: **0.4033** | SURPRISE, STRAIGHT, GUESS WHO, GOTCHA                             | INCORRECT (Max overlap: 3/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 16: **0.4598** | SURPRISE, SHED, SLITHER, HUMOR                                    | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 17: **0.4332** | INDULGE, BABY, PAMPER, BOO                                        | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE)
   - Group 18: **0.4540** | SHED, HUMOR, SEE, BOO                                             | INCORRECT (Max overlap: 1/4 with THINGS A RATTLESNAKE DOES)
   - Group 19: **0.4225** | SURPRISE, BAE, GUESS WHO, GOTCHA                                  | INCORRECT (Max overlap: 3/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 20: **0.5092** | HISS, RATTLE, CREAK, SEE                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)

---

## Puzzle 44 (ID: 1)
**Words on Board:** SLEET, SHIFT, HAIL, MOM, JAZZ, HEAT, SNOW, OPTION, NETS, TAB, RACECAR, RAIN, KAYAK, LEVEL, RETURN, BUCKS

### Ground Truth Categories:
* **Level 0 (WET WEATHER) [Type: SEMANTIC_SET]:** HAIL, RAIN, SLEET, SNOW
* **Level 1 (NBA TEAMS) [Type: NAMED_ENTITY_SET]:** BUCKS, HEAT, JAZZ, NETS
* **Level 2 (KEYBOARD KEYS) [Type: NAMED_ENTITY_SET]:** OPTION, RETURN, SHIFT, TAB
* **Level 3 (PALINDROMES) [Type: WORD_FORM]:** KAYAK, LEVEL, MOM, RACECAR

### Top Candidate Partitions:
1. **Partition Score: 0.5974**
   - Group 1: **0.6761** | MOM, JAZZ, RACECAR, KAYAK                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 2: **0.6743** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 3: **0.5856** | OPTION, NETS, TAB, RETURN                                         | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 4: **0.5649** | SHIFT, HEAT, LEVEL, BUCKS                                         | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
2. **Partition Score: 0.5959**
   - Group 1: **0.7061** | SHIFT, OPTION, TAB, RETURN                                        | CORRECT GROUP (KEYBOARD KEYS, Level 2)
   - Group 2: **0.6761** | MOM, JAZZ, RACECAR, KAYAK                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.6743** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 4: **0.5166** | HEAT, NETS, LEVEL, BUCKS                                          | INCORRECT (Max overlap: 3/4 with NBA TEAMS)
3. **Partition Score: 0.5703**
   - Group 1: **0.6761** | MOM, JAZZ, RACECAR, KAYAK                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 2: **0.6743** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 3: **0.5504** | SHIFT, HEAT, NETS, BUCKS                                          | INCORRECT (Max overlap: 3/4 with NBA TEAMS)
   - Group 4: **0.5283** | OPTION, TAB, LEVEL, RETURN                                        | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
4. **Partition Score: 0.5668**
   - Group 1: **0.6761** | MOM, JAZZ, RACECAR, KAYAK                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 2: **0.6743** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 3: **0.5408** | SHIFT, OPTION, RETURN, BUCKS                                      | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 4: **0.5261** | HEAT, NETS, TAB, LEVEL                                            | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
5. **Partition Score: 0.5662**
   - Group 1: **0.6761** | MOM, JAZZ, RACECAR, KAYAK                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 2: **0.6743** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 3: **0.5489** | NETS, TAB, LEVEL, RETURN                                          | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 4: **0.5207** | SHIFT, HEAT, OPTION, BUCKS                                        | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)

### Top Candidate Groups:
   - Group 1: **0.6761** | MOM, JAZZ, RACECAR, KAYAK                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 2: **0.6743** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 3: **0.5856** | OPTION, NETS, TAB, RETURN                                         | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 4: **0.5649** | SHIFT, HEAT, LEVEL, BUCKS                                         | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
   - Group 5: **0.7061** | SHIFT, OPTION, TAB, RETURN                                        | CORRECT GROUP (KEYBOARD KEYS, Level 2)
   - Group 6: **0.5166** | HEAT, NETS, LEVEL, BUCKS                                          | INCORRECT (Max overlap: 3/4 with NBA TEAMS)
   - Group 7: **0.5504** | SHIFT, HEAT, NETS, BUCKS                                          | INCORRECT (Max overlap: 3/4 with NBA TEAMS)
   - Group 8: **0.5283** | OPTION, TAB, LEVEL, RETURN                                        | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 9: **0.5408** | SHIFT, OPTION, RETURN, BUCKS                                      | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 10: **0.5261** | HEAT, NETS, TAB, LEVEL                                            | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
   - Group 11: **0.5489** | NETS, TAB, LEVEL, RETURN                                          | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 12: **0.5207** | SHIFT, HEAT, OPTION, BUCKS                                        | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 13: **0.6606** | SHIFT, NETS, TAB, RETURN                                          | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 14: **0.4602** | HEAT, OPTION, LEVEL, BUCKS                                        | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
   - Group 15: **0.6287** | SHIFT, TAB, LEVEL, RETURN                                         | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 16: **0.4609** | HEAT, OPTION, NETS, BUCKS                                         | INCORRECT (Max overlap: 3/4 with NBA TEAMS)
   - Group 17: **0.5558** | SHIFT, HEAT, TAB, BUCKS                                           | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 18: **0.4969** | OPTION, NETS, LEVEL, RETURN                                       | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 19: **0.5400** | HEAT, NETS, TAB, RETURN                                           | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
   - Group 20: **0.5044** | SHIFT, OPTION, LEVEL, BUCKS                                       | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)

---

## Puzzle 45 (ID: 544)
**Words on Board:** STUMP, REX, CORE, JINX, SLINKY, SPELL, VEX, POX, PERPLEX, MANIA, GATE, PILLED, HAMM, HEX, PUZZLE, BUZZ

### Ground Truth Categories:
* **Level 0 (BAFFLE) [Type: SYNONYM_OR_NEAR]:** PERPLEX, PUZZLE, STUMP, VEX
* **Level 1 (CURSE) [Type: SYNONYM_OR_NEAR]:** HEX, JINX, POX, SPELL
* **Level 2 (“TOY STORY” CHARACTERS, FAMILIARLY) [Type: NAMED_ENTITY_SET]:** BUZZ, HAMM, REX, SLINKY
* **Level 3 (COLLOQUIAL SUFFIXES) [Type: WORD_FORM]:** CORE, GATE, MANIA, PILLED

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7366** | JINX, SPELL, VEX, HEX                                             | INCORRECT (Max overlap: 3/4 with CURSE)
   - Group 2: **0.7159** | REX, CORE, MANIA, BUZZ                                            | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 3: **0.7017** | REX, POX, MANIA, HAMM                                             | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 4: **0.6848** | REX, CORE, MANIA, HAMM                                            | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 5: **0.6823** | SPELL, VEX, PERPLEX, PUZZLE                                       | INCORRECT (Max overlap: 3/4 with BAFFLE)
   - Group 6: **0.6764** | REX, MANIA, HAMM, BUZZ                                            | INCORRECT (Max overlap: 3/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 7: **0.6690** | STUMP, REX, MANIA, BUZZ                                           | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 8: **0.6684** | REX, CORE, POX, MANIA                                             | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES)
   - Group 9: **0.6640** | REX, POX, MANIA, BUZZ                                             | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 10: **0.6621** | REX, CORE, GATE, BUZZ                                             | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 11: **0.6599** | STUMP, REX, GATE, BUZZ                                            | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 12: **0.6544** | STUMP, REX, CORE, MANIA                                           | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES)
   - Group 13: **0.6538** | REX, CORE, MANIA, GATE                                            | INCORRECT (Max overlap: 3/4 with COLLOQUIAL SUFFIXES)
   - Group 14: **0.6538** | CORE, MANIA, HAMM, BUZZ                                           | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES)
   - Group 15: **0.6519** | STUMP, REX, CORE, BUZZ                                            | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 16: **0.6500** | REX, MANIA, GATE, HAMM                                            | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 17: **0.6500** | STUMP, REX, MANIA, HAMM                                           | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 18: **0.6485** | CORE, MANIA, GATE, BUZZ                                           | INCORRECT (Max overlap: 3/4 with COLLOQUIAL SUFFIXES)
   - Group 19: **0.6476** | REX, MANIA, GATE, BUZZ                                            | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 20: **0.6468** | STUMP, REX, MANIA, GATE                                           | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES)

---

## Puzzle 46 (ID: 798)
**Words on Board:** HANDY, WELCOME, ASSEMBLY, EXIT, PUSH, OPEN, ENVELOPE, CLOSE, STAMP, PRESS, NEARBY, SPEECH, ACCESSIBLE, NAME, ADDRESS, PETITION

### Ground Truth Categories:
* **Level 0 (CONVENIENTLY LOCATED) [Type: SYNONYM_OR_NEAR]:** ACCESSIBLE, CLOSE, HANDY, NEARBY
* **Level 1 (NEEDS FOR SENDING A LETTER) [Type: SEMANTIC_SET]:** ADDRESS, ENVELOPE, NAME, STAMP
* **Level 2 (WORDS ON A DOOR) [Type: SEMANTIC_SET]:** EXIT, OPEN, PUSH, WELCOME
* **Level 3 (FIRST AMENDMENT FREEDOMS) [Type: SEMANTIC_SET]:** ASSEMBLY, PETITION, PRESS, SPEECH

### Top Candidate Partitions:
1. **Partition Score: 0.4860**
   - Group 1: **0.5358** | HANDY, WELCOME, NEARBY, ACCESSIBLE                                | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 2: **0.5142** | SPEECH, NAME, ADDRESS, PETITION                                   | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS)
   - Group 3: **0.4969** | ASSEMBLY, EXIT, ENVELOPE, STAMP                                   | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 4: **0.4664** | PUSH, OPEN, CLOSE, PRESS                                          | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
2. **Partition Score: 0.4610**
   - Group 1: **0.5358** | HANDY, WELCOME, NEARBY, ACCESSIBLE                                | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 2: **0.4969** | ASSEMBLY, EXIT, ENVELOPE, STAMP                                   | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 3: **0.4497** | PUSH, OPEN, CLOSE, NAME                                           | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
   - Group 4: **0.4487** | PRESS, SPEECH, ADDRESS, PETITION                                  | INCORRECT (Max overlap: 3/4 with FIRST AMENDMENT FREEDOMS)
3. **Partition Score: 0.4576**
   - Group 1: **0.5139** | HANDY, CLOSE, NEARBY, ACCESSIBLE                                  | CORRECT GROUP (CONVENIENTLY LOCATED, Level 0)
   - Group 2: **0.4969** | ASSEMBLY, EXIT, ENVELOPE, STAMP                                   | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 3: **0.4903** | WELCOME, SPEECH, NAME, ADDRESS                                    | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 4: **0.4216** | PUSH, OPEN, PRESS, PETITION                                       | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
4. **Partition Score: 0.4536**
   - Group 1: **0.5292** | WELCOME, SPEECH, ADDRESS, PETITION                                | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS)
   - Group 2: **0.4969** | ASSEMBLY, EXIT, ENVELOPE, STAMP                                   | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 3: **0.4664** | PUSH, OPEN, CLOSE, PRESS                                          | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
   - Group 4: **0.4256** | HANDY, NEARBY, ACCESSIBLE, NAME                                   | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
5. **Partition Score: 0.4449**
   - Group 1: **0.4969** | ASSEMBLY, EXIT, ENVELOPE, STAMP                                   | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 2: **0.4956** | OPEN, CLOSE, NEARBY, NAME                                         | INCORRECT (Max overlap: 2/4 with CONVENIENTLY LOCATED)
   - Group 3: **0.4424** | HANDY, WELCOME, ACCESSIBLE, PETITION                              | INCORRECT (Max overlap: 2/4 with CONVENIENTLY LOCATED)
   - Group 4: **0.4208** | PUSH, PRESS, SPEECH, ADDRESS                                      | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS)

### Top Candidate Groups:
   - Group 1: **0.5358** | HANDY, WELCOME, NEARBY, ACCESSIBLE                                | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 2: **0.5142** | SPEECH, NAME, ADDRESS, PETITION                                   | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS)
   - Group 3: **0.4969** | ASSEMBLY, EXIT, ENVELOPE, STAMP                                   | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 4: **0.4664** | PUSH, OPEN, CLOSE, PRESS                                          | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
   - Group 5: **0.4497** | PUSH, OPEN, CLOSE, NAME                                           | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
   - Group 6: **0.4487** | PRESS, SPEECH, ADDRESS, PETITION                                  | INCORRECT (Max overlap: 3/4 with FIRST AMENDMENT FREEDOMS)
   - Group 7: **0.5139** | HANDY, CLOSE, NEARBY, ACCESSIBLE                                  | CORRECT GROUP (CONVENIENTLY LOCATED, Level 0)
   - Group 8: **0.4903** | WELCOME, SPEECH, NAME, ADDRESS                                    | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 9: **0.4216** | PUSH, OPEN, PRESS, PETITION                                       | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
   - Group 10: **0.5292** | WELCOME, SPEECH, ADDRESS, PETITION                                | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS)
   - Group 11: **0.4256** | HANDY, NEARBY, ACCESSIBLE, NAME                                   | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 12: **0.4956** | OPEN, CLOSE, NEARBY, NAME                                         | INCORRECT (Max overlap: 2/4 with CONVENIENTLY LOCATED)
   - Group 13: **0.4424** | HANDY, WELCOME, ACCESSIBLE, PETITION                              | INCORRECT (Max overlap: 2/4 with CONVENIENTLY LOCATED)
   - Group 14: **0.4208** | PUSH, PRESS, SPEECH, ADDRESS                                      | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS)
   - Group 15: **0.4716** | WELCOME, ASSEMBLY, ENVELOPE, STAMP                                | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 16: **0.4179** | HANDY, EXIT, NEARBY, ACCESSIBLE                                   | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 17: **0.5523** | HANDY, ASSEMBLY, ENVELOPE, STAMP                                  | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 18: **0.4328** | EXIT, CLOSE, NEARBY, ACCESSIBLE                                   | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 19: **0.4160** | WELCOME, OPEN, NAME, PETITION                                     | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
   - Group 20: **0.4442** | PUSH, OPEN, CLOSE, NEARBY                                         | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)

---

## Puzzle 47 (ID: 1031)
**Words on Board:** BEAM, SNOWFLAKE, COLUMN, JUMPER CABLES, BRACE, SPARE TIRE, PATRON, SPONSOR, ANGEL, STRUT, SCREWDRIVER, BOMBAY, CHAMPION, CHELSEA, ICE SCRAPER, JACK

### Ground Truth Categories:
* **Level 0 (FOUND IN THE TRUNK OF A CAR) [Type: SEMANTIC_SET]:** ICE SCRAPER, JACK, JUMPER CABLES, SPARE TIRE
* **Level 1 (BENEFACTOR) [Type: SYNONYM_OR_NEAR]:** ANGEL, CHAMPION, PATRON, SPONSOR
* **Level 2 (STRUCTURAL SUPPORTS) [Type: SYNONYM_OR_NEAR]:** BEAM, BRACE, COLUMN, STRUT
* **Level 3 (ENDING IN BODIES OF WATER) [Type: WORD_FORM]:** BOMBAY, CHELSEA, SCREWDRIVER, SNOWFLAKE

### Top Candidate Partitions:
1. **Partition Score: 0.5250**
   - Group 1: **0.6836** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 2: **0.6544** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1)
   - Group 3: **0.5171** | SNOWFLAKE, SPARE TIRE, SCREWDRIVER, ICE SCRAPER                   | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)
   - Group 4: **0.4641** | JUMPER CABLES, BOMBAY, CHELSEA, JACK                              | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
2. **Partition Score: 0.5233**
   - Group 1: **0.6836** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 2: **0.6544** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1)
   - Group 3: **0.5468** | JUMPER CABLES, SPARE TIRE, SCREWDRIVER, ICE SCRAPER               | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 4: **0.4460** | SNOWFLAKE, BOMBAY, CHELSEA, JACK                                  | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
3. **Partition Score: 0.5042**
   - Group 1: **0.5976** | BEAM, BRACE, STRUT, CHAMPION                                      | INCORRECT (Max overlap: 3/4 with STRUCTURAL SUPPORTS)
   - Group 2: **0.5714** | COLUMN, PATRON, SPONSOR, ANGEL                                    | INCORRECT (Max overlap: 3/4 with BENEFACTOR)
   - Group 3: **0.5171** | SNOWFLAKE, SPARE TIRE, SCREWDRIVER, ICE SCRAPER                   | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)
   - Group 4: **0.4641** | JUMPER CABLES, BOMBAY, CHELSEA, JACK                              | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
4. **Partition Score: 0.5025**
   - Group 1: **0.5976** | BEAM, BRACE, STRUT, CHAMPION                                      | INCORRECT (Max overlap: 3/4 with STRUCTURAL SUPPORTS)
   - Group 2: **0.5714** | COLUMN, PATRON, SPONSOR, ANGEL                                    | INCORRECT (Max overlap: 3/4 with BENEFACTOR)
   - Group 3: **0.5468** | JUMPER CABLES, SPARE TIRE, SCREWDRIVER, ICE SCRAPER               | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 4: **0.4460** | SNOWFLAKE, BOMBAY, CHELSEA, JACK                                  | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
5. **Partition Score: 0.4941**
   - Group 1: **0.6836** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 2: **0.6544** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1)
   - Group 3: **0.4829** | SCREWDRIVER, BOMBAY, CHELSEA, JACK                                | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
   - Group 4: **0.4195** | SNOWFLAKE, JUMPER CABLES, SPARE TIRE, ICE SCRAPER                 | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR)

### Top Candidate Groups:
   - Group 1: **0.6836** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 2: **0.6544** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1)
   - Group 3: **0.5171** | SNOWFLAKE, SPARE TIRE, SCREWDRIVER, ICE SCRAPER                   | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)
   - Group 4: **0.4641** | JUMPER CABLES, BOMBAY, CHELSEA, JACK                              | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 5: **0.5468** | JUMPER CABLES, SPARE TIRE, SCREWDRIVER, ICE SCRAPER               | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 6: **0.4460** | SNOWFLAKE, BOMBAY, CHELSEA, JACK                                  | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
   - Group 7: **0.5976** | BEAM, BRACE, STRUT, CHAMPION                                      | INCORRECT (Max overlap: 3/4 with STRUCTURAL SUPPORTS)
   - Group 8: **0.5714** | COLUMN, PATRON, SPONSOR, ANGEL                                    | INCORRECT (Max overlap: 3/4 with BENEFACTOR)
   - Group 9: **0.4829** | SCREWDRIVER, BOMBAY, CHELSEA, JACK                                | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
   - Group 10: **0.4195** | SNOWFLAKE, JUMPER CABLES, SPARE TIRE, ICE SCRAPER                 | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 11: **0.5202** | JUMPER CABLES, SPARE TIRE, SCREWDRIVER, JACK                      | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 12: **0.3986** | SNOWFLAKE, BOMBAY, CHELSEA, ICE SCRAPER                           | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
   - Group 13: **0.4595** | JUMPER CABLES, SCREWDRIVER, BOMBAY, JACK                          | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 14: **0.4276** | SNOWFLAKE, SPARE TIRE, CHELSEA, ICE SCRAPER                       | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)
   - Group 15: **0.4410** | SNOWFLAKE, SPARE TIRE, ICE SCRAPER, JACK                          | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 16: **0.4355** | JUMPER CABLES, SCREWDRIVER, BOMBAY, CHELSEA                       | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
   - Group 17: **0.5294** | BEAM, PATRON, SPONSOR, ANGEL                                      | INCORRECT (Max overlap: 3/4 with BENEFACTOR)
   - Group 18: **0.5189** | COLUMN, BRACE, STRUT, CHAMPION                                    | INCORRECT (Max overlap: 3/4 with STRUCTURAL SUPPORTS)
   - Group 19: **0.4779** | JUMPER CABLES, SPARE TIRE, SCREWDRIVER, CHELSEA                   | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 20: **0.4008** | SNOWFLAKE, BOMBAY, ICE SCRAPER, JACK                              | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)

---

## Puzzle 48 (ID: 166)
**Words on Board:** PAN, FIAT, SLAM, RAM, ROAST, ALONE, LILY, SURVIVOR, MAXI, MOUSE, KNOCK, BACHELOR, CHOPPED, JAGUAR, MINI, CATFISH

### Ground Truth Categories:
* **Level 0 (CRITICIZE) [Type: SYNONYM_OR_NEAR]:** KNOCK, PAN, ROAST, SLAM
* **Level 1 (REALITY SHOWS) [Type: NAMED_ENTITY_SET]:** ALONE, CATFISH, CHOPPED, SURVIVOR
* **Level 2 (CAR BRANDS) [Type: NAMED_ENTITY_SET]:** FIAT, JAGUAR, MINI, RAM
* **Level 3 (___ PAD) [Type: FILL_IN_THE_BLANK]:** BACHELOR, LILY, MAXI, MOUSE

### Top Candidate Partitions:
1. **Partition Score: 0.4471**
   - Group 1: **0.6408** | ROAST, ALONE, KNOCK, CHOPPED                                      | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 2: **0.5118** | RAM, SURVIVOR, MOUSE, CATFISH                                     | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 3: **0.4528** | FIAT, BACHELOR, JAGUAR, MINI                                      | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
   - Group 4: **0.4119** | PAN, SLAM, LILY, MAXI                                             | INCORRECT (Max overlap: 2/4 with CRITICIZE)
2. **Partition Score: 0.4448**
   - Group 1: **0.6408** | ROAST, ALONE, KNOCK, CHOPPED                                      | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 2: **0.5399** | SURVIVOR, MOUSE, BACHELOR, CATFISH                                | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 3: **0.4135** | FIAT, MAXI, JAGUAR, MINI                                          | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
   - Group 4: **0.4130** | PAN, SLAM, RAM, LILY                                              | INCORRECT (Max overlap: 2/4 with CRITICIZE)
3. **Partition Score: 0.4432**
   - Group 1: **0.6408** | ROAST, ALONE, KNOCK, CHOPPED                                      | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 2: **0.5118** | RAM, SURVIVOR, MOUSE, CATFISH                                     | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 3: **0.4339** | PAN, SLAM, LILY, BACHELOR                                         | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 4: **0.4135** | FIAT, MAXI, JAGUAR, MINI                                          | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
4. **Partition Score: 0.4393**
   - Group 1: **0.6408** | ROAST, ALONE, KNOCK, CHOPPED                                      | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 2: **0.4902** | RAM, SURVIVOR, MOUSE, BACHELOR                                    | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 3: **0.4397** | PAN, SLAM, LILY, CATFISH                                          | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 4: **0.4135** | FIAT, MAXI, JAGUAR, MINI                                          | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
5. **Partition Score: 0.4352**
   - Group 1: **0.6408** | ROAST, ALONE, KNOCK, CHOPPED                                      | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 2: **0.4902** | RAM, SURVIVOR, MOUSE, BACHELOR                                    | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 3: **0.4268** | FIAT, JAGUAR, MINI, CATFISH                                       | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
   - Group 4: **0.4119** | PAN, SLAM, LILY, MAXI                                             | INCORRECT (Max overlap: 2/4 with CRITICIZE)

### Top Candidate Groups:
   - Group 1: **0.6408** | ROAST, ALONE, KNOCK, CHOPPED                                      | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 2: **0.5118** | RAM, SURVIVOR, MOUSE, CATFISH                                     | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 3: **0.4528** | FIAT, BACHELOR, JAGUAR, MINI                                      | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
   - Group 4: **0.4119** | PAN, SLAM, LILY, MAXI                                             | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 5: **0.5399** | SURVIVOR, MOUSE, BACHELOR, CATFISH                                | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 6: **0.4135** | FIAT, MAXI, JAGUAR, MINI                                          | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
   - Group 7: **0.4130** | PAN, SLAM, RAM, LILY                                              | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 8: **0.4339** | PAN, SLAM, LILY, BACHELOR                                         | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 9: **0.4902** | RAM, SURVIVOR, MOUSE, BACHELOR                                    | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 10: **0.4397** | PAN, SLAM, LILY, CATFISH                                          | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 11: **0.4268** | FIAT, JAGUAR, MINI, CATFISH                                       | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
   - Group 12: **0.4984** | RAM, SURVIVOR, MOUSE, JAGUAR                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS)
   - Group 13: **0.4179** | FIAT, BACHELOR, MINI, CATFISH                                     | INCORRECT (Max overlap: 2/4 with CAR BRANDS)
   - Group 14: **0.4745** | FIAT, RAM, SURVIVOR, CATFISH                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS)
   - Group 15: **0.4303** | MOUSE, BACHELOR, JAGUAR, MINI                                     | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 16: **0.3837** | FIAT, RAM, JAGUAR, MINI                                           | CORRECT GROUP (CAR BRANDS, Level 2)
   - Group 17: **0.4783** | RAM, SURVIVOR, BACHELOR, CATFISH                                  | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 18: **0.4138** | FIAT, MOUSE, JAGUAR, MINI                                         | INCORRECT (Max overlap: 3/4 with CAR BRANDS)
   - Group 19: **0.4959** | RAM, SURVIVOR, JAGUAR, CATFISH                                    | INCORRECT (Max overlap: 2/4 with CAR BRANDS)
   - Group 20: **0.3966** | FIAT, MOUSE, BACHELOR, MINI                                       | INCORRECT (Max overlap: 2/4 with CAR BRANDS)

---

## Puzzle 49 (ID: 942)
**Words on Board:** DEEP END, CARDINAL, LIMB, HEART EMOJI, DIRECTION, 3 BALL, 6 MAFIA, THIN ICE, 8 BALL, CHAINZ, LEST, OAST, NON BLONDES, FORTH, SOLO CUP, COUTH

### Ground Truth Categories:
* **Level 0 (THINGS THAT ARE RED) [Type: SEMANTIC_SET]:** 3 BALL, CARDINAL, HEART EMOJI, SOLO CUP
* **Level 1 (USED IN METAPHORS FOR PRECARIOUS SITUATIONS) [Type: COMMON_PHRASE]:** 8 BALL, DEEP END, LIMB, THIN ICE
* **Level 2 (MUSICAL ARTISTS MINUS STARTING NUMBERS) [Type: WORDPLAY_TRANSFORM]:** 6 MAFIA, CHAINZ, DIRECTION, NON BLONDES
* **Level 3 (CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED) [Type: WORDPLAY_TRANSFORM]:** COUTH, FORTH, LEST, OAST

### Top Candidate Partitions:
1. **Partition Score: 0.4941**
   - Group 1: **0.5042** | DEEP END, LIMB, DIRECTION, FORTH                                  | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 2: **0.5011** | CARDINAL, LEST, OAST, COUTH                                       | INCORRECT (Max overlap: 3/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 3: **0.4952** | HEART EMOJI, 3 BALL, 6 MAFIA, 8 BALL                              | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE RED)
   - Group 4: **0.4900** | THIN ICE, CHAINZ, NON BLONDES, SOLO CUP                           | INCORRECT (Max overlap: 2/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)
2. **Partition Score: 0.4910**
   - Group 1: **0.5028** | DEEP END, THIN ICE, CHAINZ, SOLO CUP                              | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 2: **0.4957** | CARDINAL, LIMB, DIRECTION, FORTH                                  | INCORRECT (Max overlap: 1/4 with THINGS THAT ARE RED)
   - Group 3: **0.4952** | HEART EMOJI, 3 BALL, 6 MAFIA, 8 BALL                              | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE RED)
   - Group 4: **0.4866** | LEST, OAST, NON BLONDES, COUTH                                    | INCORRECT (Max overlap: 3/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
3. **Partition Score: 0.4891**
   - Group 1: **0.5917** | CARDINAL, DIRECTION, FORTH, COUTH                                 | INCORRECT (Max overlap: 2/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 2: **0.5028** | DEEP END, THIN ICE, CHAINZ, SOLO CUP                              | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 3: **0.4952** | HEART EMOJI, 3 BALL, 6 MAFIA, 8 BALL                              | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE RED)
   - Group 4: **0.4791** | LIMB, LEST, OAST, NON BLONDES                                     | INCORRECT (Max overlap: 2/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
4. **Partition Score: 0.4886**
   - Group 1: **0.5413** | LIMB, LEST, OAST, FORTH                                           | INCORRECT (Max overlap: 3/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 2: **0.5028** | DEEP END, THIN ICE, CHAINZ, SOLO CUP                              | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 3: **0.4841** | CARDINAL, HEART EMOJI, 3 BALL, 8 BALL                             | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE RED)
   - Group 4: **0.4837** | DIRECTION, 6 MAFIA, NON BLONDES, COUTH                            | INCORRECT (Max overlap: 3/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)
5. **Partition Score: 0.4872**
   - Group 1: **0.5413** | LIMB, LEST, OAST, FORTH                                           | INCORRECT (Max overlap: 3/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 2: **0.4907** | DEEP END, DIRECTION, 6 MAFIA, COUTH                               | INCORRECT (Max overlap: 2/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)
   - Group 3: **0.4900** | THIN ICE, CHAINZ, NON BLONDES, SOLO CUP                           | INCORRECT (Max overlap: 2/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)
   - Group 4: **0.4841** | CARDINAL, HEART EMOJI, 3 BALL, 8 BALL                             | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE RED)

### Top Candidate Groups:
   - Group 1: **0.5042** | DEEP END, LIMB, DIRECTION, FORTH                                  | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 2: **0.5011** | CARDINAL, LEST, OAST, COUTH                                       | INCORRECT (Max overlap: 3/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 3: **0.4952** | HEART EMOJI, 3 BALL, 6 MAFIA, 8 BALL                              | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE RED)
   - Group 4: **0.4900** | THIN ICE, CHAINZ, NON BLONDES, SOLO CUP                           | INCORRECT (Max overlap: 2/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)
   - Group 5: **0.5028** | DEEP END, THIN ICE, CHAINZ, SOLO CUP                              | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 6: **0.4957** | CARDINAL, LIMB, DIRECTION, FORTH                                  | INCORRECT (Max overlap: 1/4 with THINGS THAT ARE RED)
   - Group 7: **0.4866** | LEST, OAST, NON BLONDES, COUTH                                    | INCORRECT (Max overlap: 3/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 8: **0.5917** | CARDINAL, DIRECTION, FORTH, COUTH                                 | INCORRECT (Max overlap: 2/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 9: **0.4791** | LIMB, LEST, OAST, NON BLONDES                                     | INCORRECT (Max overlap: 2/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 10: **0.5413** | LIMB, LEST, OAST, FORTH                                           | INCORRECT (Max overlap: 3/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 11: **0.4841** | CARDINAL, HEART EMOJI, 3 BALL, 8 BALL                             | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE RED)
   - Group 12: **0.4837** | DIRECTION, 6 MAFIA, NON BLONDES, COUTH                            | INCORRECT (Max overlap: 3/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)
   - Group 13: **0.4907** | DEEP END, DIRECTION, 6 MAFIA, COUTH                               | INCORRECT (Max overlap: 2/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)
   - Group 14: **0.4880** | DEEP END, LIMB, FORTH, SOLO CUP                                   | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 15: **0.4809** | DIRECTION, THIN ICE, CHAINZ, NON BLONDES                          | INCORRECT (Max overlap: 3/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)
   - Group 16: **0.5936** | CARDINAL, LEST, FORTH, COUTH                                      | INCORRECT (Max overlap: 3/4 with CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED)
   - Group 17: **0.4781** | DEEP END, LIMB, DIRECTION, OAST                                   | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 18: **0.5855** | LEST, OAST, FORTH, COUTH                                          | CORRECT GROUP (CARDINAL DIRECTIONS WITH FIRST LETTER CHANGED, Level 3)
   - Group 19: **0.5091** | DEEP END, LIMB, DIRECTION, CHAINZ                                 | INCORRECT (Max overlap: 2/4 with USED IN METAPHORS FOR PRECARIOUS SITUATIONS)
   - Group 20: **0.4729** | 6 MAFIA, THIN ICE, NON BLONDES, SOLO CUP                          | INCORRECT (Max overlap: 2/4 with MUSICAL ARTISTS MINUS STARTING NUMBERS)

---

## Puzzle 50 (ID: 383)
**Words on Board:** CUE, PROMPT, SHORT, DRAWER, WORD, CLUTCH, LICENSE, BRIEF, FREEDOM, LATITUDE, SIGNAL, MESSENGER, SLACK, TOTE, SATCHEL, BOXER

### Ground Truth Categories:
* **Level 0 (TYPES OF BAGS) [Type: SEMANTIC_SET]:** CLUTCH, MESSENGER, SATCHEL, TOTE
* **Level 1 (WIGGLE ROOM) [Type: SYNONYM_OR_NEAR]:** FREEDOM, LATITUDE, LICENSE, SLACK
* **Level 2 (INDICATION TO PROCEED) [Type: SYNONYM_OR_NEAR]:** CUE, PROMPT, SIGNAL, WORD
* **Level 3 (UNDERWEAR IN THE SINGULAR) [Type: WORDPLAY_TRANSFORM]:** BOXER, BRIEF, DRAWER, SHORT

### Top Candidate Partitions:
1. **Partition Score: 0.4883**
   - Group 1: **0.6269** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.5299** | CUE, PROMPT, SHORT, SIGNAL                                        | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED)
   - Group 3: **0.4785** | WORD, LATITUDE, MESSENGER, SLACK                                  | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 4: **0.4724** | CLUTCH, LICENSE, BRIEF, FREEDOM                                   | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
2. **Partition Score: 0.4812**
   - Group 1: **0.6269** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.5299** | CUE, PROMPT, SHORT, SIGNAL                                        | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED)
   - Group 3: **0.5275** | LICENSE, BRIEF, FREEDOM, LATITUDE                                 | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM)
   - Group 4: **0.4336** | WORD, CLUTCH, MESSENGER, SLACK                                    | INCORRECT (Max overlap: 2/4 with TYPES OF BAGS)
3. **Partition Score: 0.4726**
   - Group 1: **0.6269** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.5330** | CUE, PROMPT, CLUTCH, SIGNAL                                       | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED)
   - Group 3: **0.4785** | WORD, LATITUDE, MESSENGER, SLACK                                  | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 4: **0.4394** | SHORT, LICENSE, BRIEF, FREEDOM                                    | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
4. **Partition Score: 0.4622**
   - Group 1: **0.6269** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.5299** | CUE, PROMPT, SHORT, SIGNAL                                        | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED)
   - Group 3: **0.5164** | CLUTCH, LICENSE, FREEDOM, LATITUDE                                | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM)
   - Group 4: **0.4013** | WORD, BRIEF, MESSENGER, SLACK                                     | INCORRECT (Max overlap: 1/4 with INDICATION TO PROCEED)
5. **Partition Score: 0.4532**
   - Group 1: **0.6269** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.5378** | CUE, PROMPT, FREEDOM, SIGNAL                                      | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED)
   - Group 3: **0.4785** | WORD, LATITUDE, MESSENGER, SLACK                                  | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 4: **0.3983** | SHORT, CLUTCH, LICENSE, BRIEF                                     | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)

### Top Candidate Groups:
   - Group 1: **0.6269** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.5299** | CUE, PROMPT, SHORT, SIGNAL                                        | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED)
   - Group 3: **0.4785** | WORD, LATITUDE, MESSENGER, SLACK                                  | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 4: **0.4724** | CLUTCH, LICENSE, BRIEF, FREEDOM                                   | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 5: **0.5275** | LICENSE, BRIEF, FREEDOM, LATITUDE                                 | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM)
   - Group 6: **0.4336** | WORD, CLUTCH, MESSENGER, SLACK                                    | INCORRECT (Max overlap: 2/4 with TYPES OF BAGS)
   - Group 7: **0.5330** | CUE, PROMPT, CLUTCH, SIGNAL                                       | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED)
   - Group 8: **0.4394** | SHORT, LICENSE, BRIEF, FREEDOM                                    | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 9: **0.5164** | CLUTCH, LICENSE, FREEDOM, LATITUDE                                | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM)
   - Group 10: **0.4013** | WORD, BRIEF, MESSENGER, SLACK                                     | INCORRECT (Max overlap: 1/4 with INDICATION TO PROCEED)
   - Group 11: **0.5378** | CUE, PROMPT, FREEDOM, SIGNAL                                      | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED)
   - Group 12: **0.3983** | SHORT, CLUTCH, LICENSE, BRIEF                                     | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 13: **0.4065** | SHORT, LICENSE, BRIEF, LATITUDE                                   | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 14: **0.3619** | SHORT, WORD, MESSENGER, SLACK                                     | INCORRECT (Max overlap: 1/4 with UNDERWEAR IN THE SINGULAR)
   - Group 15: **0.4627** | SHORT, CLUTCH, BRIEF, SIGNAL                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 16: **0.4190** | CUE, PROMPT, LICENSE, FREEDOM                                     | INCORRECT (Max overlap: 2/4 with INDICATION TO PROCEED)
   - Group 17: **0.4344** | PROMPT, LICENSE, BRIEF, FREEDOM                                   | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 18: **0.4299** | CUE, SHORT, CLUTCH, SIGNAL                                        | INCORRECT (Max overlap: 2/4 with INDICATION TO PROCEED)
   - Group 19: **0.4567** | CUE, PROMPT, SHORT, BRIEF                                         | INCORRECT (Max overlap: 2/4 with INDICATION TO PROCEED)
   - Group 20: **0.4124** | CLUTCH, LICENSE, FREEDOM, SIGNAL                                  | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)

---

## Puzzle 51 (ID: 982)
**Words on Board:** EGGS, STU, POLYESTER SUIT, SEER, JOHN TRAVOLTA, SHOVEL, BASKET, DISCO, PLATFORM SHOES, BOYLE, BELLOWS, TONGS, DYE, POKER, BRAYS, PEEPS

### Ground Truth Categories:
* **Level 0 (EASTER SUPPLIES) [Type: SEMANTIC_SET]:** BASKET, DYE, EGGS, PEEPS
* **Level 1 (FIREPLACE ACCESSORIES) [Type: SEMANTIC_SET]:** BELLOWS, POKER, SHOVEL, TONGS
* **Level 2 (ELEMENTS OF "SATURDAY NIGHT FEVER") [Type: NAMED_ENTITY_SET]:** DISCO, JOHN TRAVOLTA, PLATFORM SHOES, POLYESTER SUIT
* **Level 3 (HOMOPHONES OF WAYS TO COOK SOMETHING) [Type: SOUND_OR_SPELLING]:** BOYLE, BRAYS, SEER, STU

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6530** | BELLOWS, TONGS, BRAYS, PEEPS                                      | INCORRECT (Max overlap: 2/4 with FIREPLACE ACCESSORIES)
   - Group 2: **0.5635** | EGGS, BELLOWS, BRAYS, PEEPS                                       | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 3: **0.5627** | SEER, BELLOWS, BRAYS, PEEPS                                       | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 4: **0.5601** | BELLOWS, DYE, BRAYS, PEEPS                                        | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 5: **0.5524** | SHOVEL, BASKET, BELLOWS, TONGS                                    | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES)
   - Group 6: **0.5460** | BOYLE, BELLOWS, BRAYS, PEEPS                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 7: **0.5456** | SHOVEL, BELLOWS, TONGS, PEEPS                                     | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES)
   - Group 8: **0.5383** | BASKET, BELLOWS, BRAYS, PEEPS                                     | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 9: **0.5289** | SEER, BELLOWS, TONGS, PEEPS                                       | INCORRECT (Max overlap: 2/4 with FIREPLACE ACCESSORIES)
   - Group 10: **0.5285** | EGGS, BASKET, BELLOWS, TONGS                                      | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 11: **0.5251** | BOYLE, BELLOWS, TONGS, BRAYS                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 12: **0.5229** | EGGS, BELLOWS, TONGS, BRAYS                                       | INCORRECT (Max overlap: 2/4 with FIREPLACE ACCESSORIES)
   - Group 13: **0.5216** | SHOVEL, BELLOWS, BRAYS, PEEPS                                     | INCORRECT (Max overlap: 2/4 with FIREPLACE ACCESSORIES)
   - Group 14: **0.5207** | SEER, SHOVEL, BELLOWS, TONGS                                      | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES)
   - Group 15: **0.5196** | EGGS, BELLOWS, TONGS, PEEPS                                       | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 16: **0.5183** | SEER, BOYLE, BELLOWS, DYE                                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 17: **0.5160** | EGGS, BOYLE, BELLOWS, DYE                                         | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 18: **0.5136** | SHOVEL, BOYLE, BELLOWS, TONGS                                     | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES)
   - Group 19: **0.5136** | EGGS, BOYLE, BELLOWS, TONGS                                       | INCORRECT (Max overlap: 2/4 with FIREPLACE ACCESSORIES)
   - Group 20: **0.5064** | SHOVEL, BASKET, TONGS, POKER                                      | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES)

---

## Puzzle 52 (ID: 204)
**Words on Board:** WHOA, PYRAMID, WHEEL, WHY, CAESAR, FEUD, PLANT, GREEK, WEDGE, GREEN, WATER, WEED, MILLIONAIRE, SEED, WEE, WAY

### Ground Truth Categories:
* **Level 0 (GARDENING NOUNS/VERBS) [Type: SEMANTIC_SET]:** PLANT, SEED, WATER, WEED
* **Level 1 (KINDS OF SALADS) [Type: NAMED_ENTITY_SET]:** CAESAR, GREEK, GREEN, WEDGE
* **Level 2 (CLASSIC GAME SHOWS, FAMILIARLY) [Type: NAMED_ENTITY_SET]:** FEUD, MILLIONAIRE, PYRAMID, WHEEL
* **Level 3 (W + VOWEL SOUND) [Type: SOUND_OR_SPELLING]:** WAY, WEE, WHY, WHOA

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7076** | WHEEL, GREEK, GREEN, WATER                                        | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS)
   - Group 2: **0.7024** | CAESAR, FEUD, GREEK, WEE                                          | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS)
   - Group 3: **0.6905** | FEUD, GREEK, WEE, WAY                                             | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND)
   - Group 4: **0.6778** | WHEEL, FEUD, GREEK, WEE                                           | INCORRECT (Max overlap: 2/4 with CLASSIC GAME SHOWS, FAMILIARLY)
   - Group 5: **0.6760** | WHOA, FEUD, GREEK, WEE                                            | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND)
   - Group 6: **0.6747** | GREEK, GREEN, WATER, WAY                                          | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS)
   - Group 7: **0.6739** | WHEEL, GREEN, WATER, WAY                                          | INCORRECT (Max overlap: 1/4 with CLASSIC GAME SHOWS, FAMILIARLY)
   - Group 8: **0.6726** | WHEEL, GREEK, WATER, WAY                                          | INCORRECT (Max overlap: 1/4 with CLASSIC GAME SHOWS, FAMILIARLY)
   - Group 9: **0.6689** | WHEEL, GREEK, WEE, WAY                                            | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND)
   - Group 10: **0.6687** | WHOA, GREEK, WEE, WAY                                             | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND)
   - Group 11: **0.6640** | WHOA, FEUD, WEE, WAY                                              | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND)
   - Group 12: **0.6635** | WHOA, CAESAR, FEUD, GREEK                                         | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS)
   - Group 13: **0.6634** | CAESAR, FEUD, GREEK, MILLIONAIRE                                  | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS)
   - Group 14: **0.6614** | WHEEL, FEUD, GREEK, WEDGE                                         | INCORRECT (Max overlap: 2/4 with CLASSIC GAME SHOWS, FAMILIARLY)
   - Group 15: **0.6608** | FEUD, GREEK, WEDGE, WAY                                           | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS)
   - Group 16: **0.6589** | WHEEL, GREEK, WEDGE, GREEN                                        | INCORRECT (Max overlap: 3/4 with KINDS OF SALADS)
   - Group 17: **0.6582** | WHOA, FEUD, GREEK, WAY                                            | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND)
   - Group 18: **0.6570** | WHEEL, CAESAR, FEUD, GREEK                                        | INCORRECT (Max overlap: 2/4 with CLASSIC GAME SHOWS, FAMILIARLY)
   - Group 19: **0.6549** | WHEEL, CAESAR, GREEK, WEE                                         | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS)
   - Group 20: **0.6509** | WHEEL, FEUD, GREEK, WAY                                           | INCORRECT (Max overlap: 2/4 with CLASSIC GAME SHOWS, FAMILIARLY)

---

## Puzzle 53 (ID: 624)
**Words on Board:** SWALLOW, SHINE, GULP, CHINA, GIVE, ANCHOR, SCARF, BUCKLE, MERMAID, COMPASS, BOW, BUTTE, WOLF, GOBBLE, HEARTH, CAVE

### Ground Truth Categories:
* **Level 0 (EAT VORACIOUSLY) [Type: SYNONYM_OR_NEAR]:** GOBBLE, GULP, SCARF, WOLF
* **Level 1 (BEND UNDER PRESSURE) [Type: SYNONYM_OR_NEAR]:** BOW, BUCKLE, CAVE, GIVE
* **Level 2 (CLASSIC NAUTICAL TATTOOS) [Type: NAMED_ENTITY_SET]:** ANCHOR, COMPASS, MERMAID, SWALLOW
* **Level 3 (BODY PARTS PLUS LETTER) [Type: WORDPLAY_TRANSFORM]:** BUTTE, CHINA, HEARTH, SHINE

### Top Candidate Partitions:
1. **Partition Score: 0.5727**
   - Group 1: **0.7239** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 2: **0.5890** | ANCHOR, COMPASS, BOW, HEARTH                                      | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 3: **0.5719** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.5649** | CHINA, MERMAID, BUTTE, CAVE                                       | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
2. **Partition Score: 0.5622**
   - Group 1: **0.7239** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 2: **0.5719** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 3: **0.5623** | ANCHOR, COMPASS, BOW, CAVE                                        | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 4: **0.5574** | CHINA, MERMAID, BUTTE, HEARTH                                     | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
3. **Partition Score: 0.5560**
   - Group 1: **0.7239** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 2: **0.5894** | CHINA, BUTTE, HEARTH, CAVE                                        | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 3: **0.5719** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.5314** | ANCHOR, MERMAID, COMPASS, BOW                                     | INCORRECT (Max overlap: 3/4 with CLASSIC NAUTICAL TATTOOS)
4. **Partition Score: 0.5494**
   - Group 1: **0.7239** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 2: **0.6372** | CHINA, MERMAID, HEARTH, CAVE                                      | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 3: **0.5719** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.4943** | ANCHOR, COMPASS, BOW, BUTTE                                       | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
5. **Partition Score: 0.5252**
   - Group 1: **0.7239** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 2: **0.5719** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 3: **0.5298** | ANCHOR, MERMAID, COMPASS, CAVE                                    | INCORRECT (Max overlap: 3/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 4: **0.4995** | CHINA, BOW, BUTTE, HEARTH                                         | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)

### Top Candidate Groups:
   - Group 1: **0.7239** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 2: **0.5890** | ANCHOR, COMPASS, BOW, HEARTH                                      | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 3: **0.5719** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.5649** | CHINA, MERMAID, BUTTE, CAVE                                       | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 5: **0.5623** | ANCHOR, COMPASS, BOW, CAVE                                        | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 6: **0.5574** | CHINA, MERMAID, BUTTE, HEARTH                                     | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 7: **0.5894** | CHINA, BUTTE, HEARTH, CAVE                                        | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 8: **0.5314** | ANCHOR, MERMAID, COMPASS, BOW                                     | INCORRECT (Max overlap: 3/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 9: **0.6372** | CHINA, MERMAID, HEARTH, CAVE                                      | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 10: **0.4943** | ANCHOR, COMPASS, BOW, BUTTE                                       | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 11: **0.5298** | ANCHOR, MERMAID, COMPASS, CAVE                                    | INCORRECT (Max overlap: 3/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 12: **0.4995** | CHINA, BOW, BUTTE, HEARTH                                         | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 13: **0.5229** | ANCHOR, SCARF, COMPASS, CAVE                                      | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 14: **0.4995** | SHINE, GIVE, BUCKLE, BOW                                          | INCORRECT (Max overlap: 3/4 with BEND UNDER PRESSURE)
   - Group 15: **0.5476** | ANCHOR, BOW, HEARTH, CAVE                                         | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 16: **0.4773** | CHINA, MERMAID, COMPASS, BUTTE                                    | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 17: **0.5235** | ANCHOR, MERMAID, BOW, HEARTH                                      | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 18: **0.4885** | CHINA, COMPASS, BUTTE, CAVE                                       | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 19: **0.5061** | CHINA, COMPASS, BUTTE, HEARTH                                     | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 20: **0.4939** | ANCHOR, MERMAID, BOW, CAVE                                        | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)

---

## Puzzle 54 (ID: 940)
**Words on Board:** CIDER, INTEREST, MIRROR, SHARE, RINGER, WINE, STAKE, CRESCENT, GARLIC, CROSS, TROUSERS, STAR, DOUBLE, CLONE, CONCERN, STRIPE

### Ground Truth Categories:
* **Level 0 (DOPPELGÄNGER) [Type: SYNONYM_OR_NEAR]:** CLONE, DOUBLE, MIRROR, RINGER
* **Level 1 (PORTION) [Type: SYNONYM_OR_NEAR]:** CONCERN, INTEREST, SHARE, STAKE
* **Level 2 (COMMON FLAG SYMBOLS) [Type: SEMANTIC_SET]:** CRESCENT, CROSS, STAR, STRIPE
* **Level 3 (PRESSED USING A PRESS) [Type: FILL_IN_THE_BLANK]:** CIDER, GARLIC, TROUSERS, WINE

### Top Candidate Partitions:
1. **Partition Score: 0.5859**
   - Group 1: **0.7239** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1)
   - Group 2: **0.6316** | CROSS, TROUSERS, STAR, STRIPE                                     | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 3: **0.5759** | CIDER, WINE, CRESCENT, GARLIC                                     | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 4: **0.5681** | MIRROR, RINGER, DOUBLE, CLONE                                     | CORRECT GROUP (DOPPELGÄNGER, Level 0)
2. **Partition Score: 0.5838**
   - Group 1: **0.7265** | CRESCENT, CROSS, STAR, STRIPE                                     | CORRECT GROUP (COMMON FLAG SYMBOLS, Level 2)
   - Group 2: **0.7239** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1)
   - Group 3: **0.5681** | MIRROR, RINGER, DOUBLE, CLONE                                     | CORRECT GROUP (DOPPELGÄNGER, Level 0)
   - Group 4: **0.5215** | CIDER, WINE, GARLIC, TROUSERS                                     | CORRECT GROUP (PRESSED USING A PRESS, Level 3)
3. **Partition Score: 0.5646**
   - Group 1: **0.7239** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1)
   - Group 2: **0.6823** | MIRROR, CROSS, STAR, STRIPE                                       | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 3: **0.5944** | CIDER, CRESCENT, GARLIC, TROUSERS                                 | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 4: **0.4909** | RINGER, WINE, DOUBLE, CLONE                                       | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER)
4. **Partition Score: 0.5645**
   - Group 1: **0.7239** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1)
   - Group 2: **0.5944** | CIDER, CRESCENT, GARLIC, TROUSERS                                 | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 3: **0.5681** | MIRROR, RINGER, DOUBLE, CLONE                                     | CORRECT GROUP (DOPPELGÄNGER, Level 0)
   - Group 4: **0.5478** | WINE, CROSS, STAR, STRIPE                                         | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
5. **Partition Score: 0.5635**
   - Group 1: **0.7265** | CRESCENT, CROSS, STAR, STRIPE                                     | CORRECT GROUP (COMMON FLAG SYMBOLS, Level 2)
   - Group 2: **0.7239** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1)
   - Group 3: **0.5483** | CIDER, MIRROR, GARLIC, TROUSERS                                   | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 4: **0.4909** | RINGER, WINE, DOUBLE, CLONE                                       | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER)

### Top Candidate Groups:
   - Group 1: **0.7239** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1)
   - Group 2: **0.6316** | CROSS, TROUSERS, STAR, STRIPE                                     | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 3: **0.5759** | CIDER, WINE, CRESCENT, GARLIC                                     | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 4: **0.5681** | MIRROR, RINGER, DOUBLE, CLONE                                     | CORRECT GROUP (DOPPELGÄNGER, Level 0)
   - Group 5: **0.7265** | CRESCENT, CROSS, STAR, STRIPE                                     | CORRECT GROUP (COMMON FLAG SYMBOLS, Level 2)
   - Group 6: **0.5215** | CIDER, WINE, GARLIC, TROUSERS                                     | CORRECT GROUP (PRESSED USING A PRESS, Level 3)
   - Group 7: **0.6823** | MIRROR, CROSS, STAR, STRIPE                                       | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 8: **0.5944** | CIDER, CRESCENT, GARLIC, TROUSERS                                 | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 9: **0.4909** | RINGER, WINE, DOUBLE, CLONE                                       | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER)
   - Group 10: **0.5478** | WINE, CROSS, STAR, STRIPE                                         | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 11: **0.5483** | CIDER, MIRROR, GARLIC, TROUSERS                                   | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 12: **0.5354** | MIRROR, WINE, GARLIC, TROUSERS                                    | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 13: **0.4880** | CIDER, RINGER, DOUBLE, CLONE                                      | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER)
   - Group 14: **0.6197** | CIDER, MIRROR, CRESCENT, GARLIC                                   | INCORRECT (Max overlap: 2/4 with PRESSED USING A PRESS)
   - Group 15: **0.6410** | CRESCENT, TROUSERS, STAR, STRIPE                                  | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 16: **0.5446** | CIDER, MIRROR, WINE, GARLIC                                       | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 17: **0.5224** | RINGER, CROSS, DOUBLE, CLONE                                      | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER)
   - Group 18: **0.6619** | MIRROR, CRESCENT, STAR, STRIPE                                    | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 19: **0.5558** | WINE, CRESCENT, GARLIC, TROUSERS                                  | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 20: **0.5924** | MIRROR, TROUSERS, STAR, STRIPE                                    | INCORRECT (Max overlap: 2/4 with COMMON FLAG SYMBOLS)

---

## Puzzle 55 (ID: 655)
**Words on Board:** PAPER, SWAY, PHONE, CHANGE, DING, WAVE, GREEN, CORRECT, SCRATCH, RIGHT, SCOPE, CHIP, MOVE, BINGO, TOUCH, REACH

### Ground Truth Categories:
* **Level 0 (AFFECT) [Type: SYNONYM_OR_NEAR]:** MOVE, REACH, SWAY, TOUCH
* **Level 1 (YOU GOT IT!) [Type: SYNONYM_OR_NEAR]:** BINGO, CORRECT, DING, RIGHT
* **Level 2 (SLANG FOR MONEY) [Type: SEMANTIC_SET]:** CHANGE, GREEN, PAPER, SCRATCH
* **Level 3 (OBJECTS WITH THE PREFIX “MICRO-”) [Type: FILL_IN_THE_BLANK]:** CHIP, PHONE, SCOPE, WAVE

### Top Candidate Partitions:
1. **Partition Score: 0.5524**
   - Group 1: **0.6610** | SWAY, CHANGE, MOVE, TOUCH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 2: **0.6419** | PAPER, PHONE, GREEN, BINGO                                        | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 3: **0.5790** | CORRECT, RIGHT, SCOPE, REACH                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 4: **0.4943** | DING, WAVE, SCRATCH, CHIP                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”)
2. **Partition Score: 0.5466**
   - Group 1: **0.6419** | PAPER, PHONE, GREEN, BINGO                                        | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 2: **0.6091** | SWAY, CHANGE, MOVE, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 3: **0.5889** | CORRECT, RIGHT, SCOPE, TOUCH                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 4: **0.4943** | DING, WAVE, SCRATCH, CHIP                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”)
3. **Partition Score: 0.5402**
   - Group 1: **0.6419** | PAPER, PHONE, GREEN, BINGO                                        | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 2: **0.6274** | CHANGE, CORRECT, RIGHT, MOVE                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.5447** | SWAY, SCOPE, TOUCH, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 4: **0.4943** | DING, WAVE, SCRATCH, CHIP                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”)
4. **Partition Score: 0.5378**
   - Group 1: **0.6862** | CHANGE, CORRECT, RIGHT, TOUCH                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 2: **0.6419** | PAPER, PHONE, GREEN, BINGO                                        | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 3: **0.5207** | SWAY, SCOPE, MOVE, REACH                                          | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 4: **0.4943** | DING, WAVE, SCRATCH, CHIP                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”)
5. **Partition Score: 0.5353**
   - Group 1: **0.6568** | SWAY, MOVE, TOUCH, REACH                                          | CORRECT GROUP (AFFECT, Level 0)
   - Group 2: **0.6419** | PAPER, PHONE, GREEN, BINGO                                        | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 3: **0.5107** | CHANGE, CORRECT, RIGHT, SCOPE                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 4: **0.4943** | DING, WAVE, SCRATCH, CHIP                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”)

### Top Candidate Groups:
   - Group 1: **0.6610** | SWAY, CHANGE, MOVE, TOUCH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 2: **0.6419** | PAPER, PHONE, GREEN, BINGO                                        | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 3: **0.5790** | CORRECT, RIGHT, SCOPE, REACH                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 4: **0.4943** | DING, WAVE, SCRATCH, CHIP                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”)
   - Group 5: **0.6091** | SWAY, CHANGE, MOVE, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 6: **0.5889** | CORRECT, RIGHT, SCOPE, TOUCH                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 7: **0.6274** | CHANGE, CORRECT, RIGHT, MOVE                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 8: **0.5447** | SWAY, SCOPE, TOUCH, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 9: **0.6862** | CHANGE, CORRECT, RIGHT, TOUCH                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 10: **0.5207** | SWAY, SCOPE, MOVE, REACH                                          | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 11: **0.6568** | SWAY, MOVE, TOUCH, REACH                                          | CORRECT GROUP (AFFECT, Level 0)
   - Group 12: **0.5107** | CHANGE, CORRECT, RIGHT, SCOPE                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 13: **0.6719** | RIGHT, SCOPE, TOUCH, REACH                                        | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 14: **0.5044** | SWAY, CHANGE, CORRECT, MOVE                                       | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 15: **0.6479** | CHANGE, SCOPE, TOUCH, REACH                                       | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 16: **0.4997** | SWAY, CORRECT, RIGHT, MOVE                                        | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 17: **0.6037** | CORRECT, SCOPE, TOUCH, REACH                                      | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 18: **0.5373** | SWAY, CHANGE, RIGHT, MOVE                                         | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 19: **0.6629** | PAPER, GREEN, SCRATCH, BINGO                                      | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 20: **0.4392** | PHONE, DING, WAVE, CHIP                                           | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)

---

## Puzzle 56 (ID: 862)
**Words on Board:** BIG BEAR, BE, BUGBEAR, CENTAUR, LYRE, UNI, POP, HANG-UP, A, CAPRI, K, DEMON, COMPLEX, AS, I, HUNTER

### Ground Truth Categories:
* **Level 0 (AFFLICTION) [Type: SYNONYM_OR_NEAR]:** BUGBEAR, COMPLEX, DEMON, HANG-UP
* **Level 1 (REPRESENTED BY CONSTELLATIONS) [Type: NAMED_ENTITY_SET]:** BIG BEAR, CENTAUR, HUNTER, LYRE
* **Level 2 (PERIODIC TABLE SYMBOLS) [Type: NAMED_ENTITY_SET]:** AS, BE, I, K
* **Level 3 (___CORN) [Type: FILL_IN_THE_BLANK]:** A, CAPRI, POP, UNI

### Top Candidate Partitions:
1. **Partition Score: 0.4862**
   - Group 1: **0.6621** | BE, A, K, I                                                       | INCORRECT (Max overlap: 3/4 with PERIODIC TABLE SYMBOLS)
   - Group 2: **0.6244** | BUGBEAR, CENTAUR, DEMON, HUNTER                                   | INCORRECT (Max overlap: 2/4 with AFFLICTION)
   - Group 3: **0.4501** | BIG BEAR, LYRE, UNI, AS                                           | INCORRECT (Max overlap: 2/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 4: **0.4351** | POP, HANG-UP, CAPRI, COMPLEX                                      | INCORRECT (Max overlap: 2/4 with ___CORN)
2. **Partition Score: 0.4740**
   - Group 1: **0.6621** | BE, A, K, I                                                       | INCORRECT (Max overlap: 3/4 with PERIODIC TABLE SYMBOLS)
   - Group 2: **0.5757** | CENTAUR, LYRE, DEMON, HUNTER                                      | INCORRECT (Max overlap: 3/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 3: **0.4503** | BIG BEAR, BUGBEAR, UNI, AS                                        | INCORRECT (Max overlap: 1/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 4: **0.4351** | POP, HANG-UP, CAPRI, COMPLEX                                      | INCORRECT (Max overlap: 2/4 with ___CORN)
3. **Partition Score: 0.4688**
   - Group 1: **0.6621** | BE, A, K, I                                                       | INCORRECT (Max overlap: 3/4 with PERIODIC TABLE SYMBOLS)
   - Group 2: **0.5468** | BUGBEAR, CENTAUR, LYRE, DEMON                                     | INCORRECT (Max overlap: 2/4 with AFFLICTION)
   - Group 3: **0.4448** | BIG BEAR, UNI, POP, AS                                            | INCORRECT (Max overlap: 2/4 with ___CORN)
   - Group 4: **0.4418** | HANG-UP, CAPRI, COMPLEX, HUNTER                                   | INCORRECT (Max overlap: 2/4 with AFFLICTION)
4. **Partition Score: 0.4584**
   - Group 1: **0.6621** | BE, A, K, I                                                       | INCORRECT (Max overlap: 3/4 with PERIODIC TABLE SYMBOLS)
   - Group 2: **0.4930** | BIG BEAR, BUGBEAR, CENTAUR, DEMON                                 | INCORRECT (Max overlap: 2/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 3: **0.4571** | LYRE, UNI, POP, AS                                                | INCORRECT (Max overlap: 2/4 with ___CORN)
   - Group 4: **0.4418** | HANG-UP, CAPRI, COMPLEX, HUNTER                                   | INCORRECT (Max overlap: 2/4 with AFFLICTION)
5. **Partition Score: 0.4554**
   - Group 1: **0.6621** | BE, A, K, I                                                       | INCORRECT (Max overlap: 3/4 with PERIODIC TABLE SYMBOLS)
   - Group 2: **0.4615** | CENTAUR, DEMON, COMPLEX, HUNTER                                   | INCORRECT (Max overlap: 2/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 3: **0.4599** | BUGBEAR, POP, HANG-UP, CAPRI                                      | INCORRECT (Max overlap: 2/4 with AFFLICTION)
   - Group 4: **0.4501** | BIG BEAR, LYRE, UNI, AS                                           | INCORRECT (Max overlap: 2/4 with REPRESENTED BY CONSTELLATIONS)

### Top Candidate Groups:
   - Group 1: **0.6621** | BE, A, K, I                                                       | INCORRECT (Max overlap: 3/4 with PERIODIC TABLE SYMBOLS)
   - Group 2: **0.6244** | BUGBEAR, CENTAUR, DEMON, HUNTER                                   | INCORRECT (Max overlap: 2/4 with AFFLICTION)
   - Group 3: **0.4501** | BIG BEAR, LYRE, UNI, AS                                           | INCORRECT (Max overlap: 2/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 4: **0.4351** | POP, HANG-UP, CAPRI, COMPLEX                                      | INCORRECT (Max overlap: 2/4 with ___CORN)
   - Group 5: **0.5757** | CENTAUR, LYRE, DEMON, HUNTER                                      | INCORRECT (Max overlap: 3/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 6: **0.4503** | BIG BEAR, BUGBEAR, UNI, AS                                        | INCORRECT (Max overlap: 1/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 7: **0.5468** | BUGBEAR, CENTAUR, LYRE, DEMON                                     | INCORRECT (Max overlap: 2/4 with AFFLICTION)
   - Group 8: **0.4448** | BIG BEAR, UNI, POP, AS                                            | INCORRECT (Max overlap: 2/4 with ___CORN)
   - Group 9: **0.4418** | HANG-UP, CAPRI, COMPLEX, HUNTER                                   | INCORRECT (Max overlap: 2/4 with AFFLICTION)
   - Group 10: **0.4930** | BIG BEAR, BUGBEAR, CENTAUR, DEMON                                 | INCORRECT (Max overlap: 2/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 11: **0.4571** | LYRE, UNI, POP, AS                                                | INCORRECT (Max overlap: 2/4 with ___CORN)
   - Group 12: **0.4615** | CENTAUR, DEMON, COMPLEX, HUNTER                                   | INCORRECT (Max overlap: 2/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 13: **0.4599** | BUGBEAR, POP, HANG-UP, CAPRI                                      | INCORRECT (Max overlap: 2/4 with AFFLICTION)
   - Group 14: **0.4934** | BIG BEAR, CENTAUR, DEMON, HUNTER                                  | INCORRECT (Max overlap: 3/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 15: **0.4548** | BUGBEAR, LYRE, UNI, AS                                            | INCORRECT (Max overlap: 1/4 with AFFLICTION)
   - Group 16: **0.4354** | LYRE, UNI, AS, HUNTER                                             | INCORRECT (Max overlap: 2/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 17: **0.4494** | BUGBEAR, LYRE, UNI, HANG-UP                                       | INCORRECT (Max overlap: 2/4 with AFFLICTION)
   - Group 18: **0.4434** | BIG BEAR, POP, CAPRI, AS                                          | INCORRECT (Max overlap: 2/4 with ___CORN)
   - Group 19: **0.4549** | BIG BEAR, CENTAUR, LYRE, DEMON                                    | INCORRECT (Max overlap: 3/4 with REPRESENTED BY CONSTELLATIONS)
   - Group 20: **0.4515** | BUGBEAR, UNI, POP, AS                                             | INCORRECT (Max overlap: 2/4 with ___CORN)

---

## Puzzle 57 (ID: 306)
**Words on Board:** NEAT, ULTRA, TIDY, CLEAN, SNOWBALL, STICK, SUPER, UBER, SWELL, MUSHROOM, HYPER, TRIM, DOMINO, BALLOON, MARBLE, JACK

### Ground Truth Categories:
* **Level 0 (ORDERLY) [Type: SYNONYM_OR_NEAR]:** CLEAN, NEAT, TIDY, TRIM
* **Level 1 (AUGMENTATIVE PREFIXES) [Type: SYNONYM_OR_NEAR]:** HYPER, SUPER, UBER, ULTRA
* **Level 2 (BECOME LARGER) [Type: SYNONYM_OR_NEAR]:** BALLOON, MUSHROOM, SNOWBALL, SWELL
* **Level 3 (ITEMS IN CLASSIC KIDS’ GAMES) [Type: SEMANTIC_SET]:** DOMINO, JACK, MARBLE, STICK

### Top Candidate Partitions:
1. **Partition Score: 0.5634**
   - Group 1: **0.8868** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0)
   - Group 2: **0.6793** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 3: **0.5362** | DOMINO, BALLOON, MARBLE, JACK                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 4: **0.5191** | SNOWBALL, STICK, SWELL, MUSHROOM                                  | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
2. **Partition Score: 0.5590**
   - Group 1: **0.8868** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0)
   - Group 2: **0.6793** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 3: **0.5424** | STICK, SWELL, MUSHROOM, BALLOON                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 4: **0.5071** | SNOWBALL, DOMINO, MARBLE, JACK                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES)
3. **Partition Score: 0.5520**
   - Group 1: **0.8868** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0)
   - Group 2: **0.5764** | ULTRA, SNOWBALL, DOMINO, MARBLE                                   | INCORRECT (Max overlap: 2/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 3: **0.5467** | SUPER, UBER, HYPER, JACK                                          | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 4: **0.5424** | STICK, SWELL, MUSHROOM, BALLOON                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
4. **Partition Score: 0.5411**
   - Group 1: **0.8868** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0)
   - Group 2: **0.5855** | SUPER, UBER, HYPER, BALLOON                                       | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 3: **0.5409** | ULTRA, DOMINO, MARBLE, JACK                                       | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 4: **0.5191** | SNOWBALL, STICK, SWELL, MUSHROOM                                  | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
5. **Partition Score: 0.5388**
   - Group 1: **0.8868** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0)
   - Group 2: **0.5706** | ULTRA, DOMINO, BALLOON, MARBLE                                    | INCORRECT (Max overlap: 2/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 3: **0.5467** | SUPER, UBER, HYPER, JACK                                          | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 4: **0.5191** | SNOWBALL, STICK, SWELL, MUSHROOM                                  | INCORRECT (Max overlap: 3/4 with BECOME LARGER)

### Top Candidate Groups:
   - Group 1: **0.8868** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0)
   - Group 2: **0.6793** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 3: **0.5362** | DOMINO, BALLOON, MARBLE, JACK                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 4: **0.5191** | SNOWBALL, STICK, SWELL, MUSHROOM                                  | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 5: **0.5424** | STICK, SWELL, MUSHROOM, BALLOON                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 6: **0.5071** | SNOWBALL, DOMINO, MARBLE, JACK                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 7: **0.5764** | ULTRA, SNOWBALL, DOMINO, MARBLE                                   | INCORRECT (Max overlap: 2/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 8: **0.5467** | SUPER, UBER, HYPER, JACK                                          | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 9: **0.5855** | SUPER, UBER, HYPER, BALLOON                                       | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 10: **0.5409** | ULTRA, DOMINO, MARBLE, JACK                                       | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 11: **0.5706** | ULTRA, DOMINO, BALLOON, MARBLE                                    | INCORRECT (Max overlap: 2/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 12: **0.5754** | SNOWBALL, STICK, SWELL, BALLOON                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 13: **0.5110** | ULTRA, MUSHROOM, DOMINO, MARBLE                                   | INCORRECT (Max overlap: 2/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 14: **0.6833** | SNOWBALL, SWELL, MUSHROOM, BALLOON                                | CORRECT GROUP (BECOME LARGER, Level 2)
   - Group 15: **0.5540** | ULTRA, STICK, SUPER, HYPER                                        | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 16: **0.4525** | UBER, DOMINO, MARBLE, JACK                                        | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 17: **0.5915** | ULTRA, SUPER, UBER, JACK                                          | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 18: **0.4979** | HYPER, DOMINO, BALLOON, MARBLE                                    | INCORRECT (Max overlap: 2/4 with ITEMS IN CLASSIC KIDS’ GAMES)
   - Group 19: **0.4764** | SUPER, UBER, HYPER, MARBLE                                        | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 20: **0.4680** | ULTRA, STICK, DOMINO, JACK                                        | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES)

---

## Puzzle 58 (ID: 641)
**Words on Board:** WILT, WHISTLE, SLANT, FLAG, RIVER, ART, SPIN, THOU, TURN, FLOP, HAIL, WAVE, BIAS, HOLE, ANGLE, ANON

### Ground Truth Categories:
* **Level 0 (PARTIALITY) [Type: SYNONYM_OR_NEAR]:** ANGLE, BIAS, SLANT, SPIN
* **Level 1 (SIGNAL DOWN, AS A TAXI) [Type: SYNONYM_OR_NEAR]:** FLAG, HAIL, WAVE, WHISTLE
* **Level 2 (CARDS IN TEXAS HOLD ’EM) [Type: NAMED_ENTITY_SET]:** FLOP, HOLE, RIVER, TURN
* **Level 3 (SHAKESPEAREAN WORDS) [Type: SEMANTIC_SET]:** ANON, ART, THOU, WILT

### Top Candidate Partitions:
1. **Partition Score: 0.5419**
   - Group 1: **0.6525** | WILT, ART, THOU, HAIL                                             | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 2: **0.5605** | SLANT, TURN, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 3: **0.5594** | SPIN, FLOP, HOLE, ANON                                            | INCORRECT (Max overlap: 2/4 with CARDS IN TEXAS HOLD ’EM)
   - Group 4: **0.5240** | WHISTLE, FLAG, RIVER, WAVE                                        | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
2. **Partition Score: 0.5392**
   - Group 1: **0.6443** | WILT, RIVER, ART, THOU                                            | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 2: **0.5605** | SLANT, TURN, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 3: **0.5594** | SPIN, FLOP, HOLE, ANON                                            | INCORRECT (Max overlap: 2/4 with CARDS IN TEXAS HOLD ’EM)
   - Group 4: **0.5186** | WHISTLE, FLAG, HAIL, WAVE                                         | CORRECT GROUP (SIGNAL DOWN, AS A TAXI, Level 1)
3. **Partition Score: 0.5374**
   - Group 1: **0.6873** | WILT, RIVER, THOU, HAIL                                           | INCORRECT (Max overlap: 2/4 with SHAKESPEAREAN WORDS)
   - Group 2: **0.5605** | SLANT, TURN, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 3: **0.5594** | SPIN, FLOP, HOLE, ANON                                            | INCORRECT (Max overlap: 2/4 with CARDS IN TEXAS HOLD ’EM)
   - Group 4: **0.5150** | WHISTLE, FLAG, ART, WAVE                                          | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
4. **Partition Score: 0.5362**
   - Group 1: **0.5659** | SLANT, SPIN, TURN, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 2: **0.5471** | WILT, ART, THOU, HOLE                                             | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 3: **0.5411** | FLAG, FLOP, BIAS, ANON                                            | INCORRECT (Max overlap: 1/4 with SIGNAL DOWN, AS A TAXI)
   - Group 4: **0.5282** | WHISTLE, RIVER, HAIL, WAVE                                        | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
5. **Partition Score: 0.5362**
   - Group 1: **0.5696** | WILT, RIVER, ART, HOLE                                            | INCORRECT (Max overlap: 2/4 with SHAKESPEAREAN WORDS)
   - Group 2: **0.5605** | SLANT, TURN, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 3: **0.5493** | WHISTLE, FLAG, THOU, HAIL                                         | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
   - Group 4: **0.5175** | SPIN, FLOP, WAVE, ANON                                            | INCORRECT (Max overlap: 1/4 with PARTIALITY)

### Top Candidate Groups:
   - Group 1: **0.6525** | WILT, ART, THOU, HAIL                                             | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 2: **0.5605** | SLANT, TURN, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 3: **0.5594** | SPIN, FLOP, HOLE, ANON                                            | INCORRECT (Max overlap: 2/4 with CARDS IN TEXAS HOLD ’EM)
   - Group 4: **0.5240** | WHISTLE, FLAG, RIVER, WAVE                                        | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
   - Group 5: **0.6443** | WILT, RIVER, ART, THOU                                            | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 6: **0.5186** | WHISTLE, FLAG, HAIL, WAVE                                         | CORRECT GROUP (SIGNAL DOWN, AS A TAXI, Level 1)
   - Group 7: **0.6873** | WILT, RIVER, THOU, HAIL                                           | INCORRECT (Max overlap: 2/4 with SHAKESPEAREAN WORDS)
   - Group 8: **0.5150** | WHISTLE, FLAG, ART, WAVE                                          | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
   - Group 9: **0.5659** | SLANT, SPIN, TURN, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 10: **0.5471** | WILT, ART, THOU, HOLE                                             | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 11: **0.5411** | FLAG, FLOP, BIAS, ANON                                            | INCORRECT (Max overlap: 1/4 with SIGNAL DOWN, AS A TAXI)
   - Group 12: **0.5282** | WHISTLE, RIVER, HAIL, WAVE                                        | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
   - Group 13: **0.5696** | WILT, RIVER, ART, HOLE                                            | INCORRECT (Max overlap: 2/4 with SHAKESPEAREAN WORDS)
   - Group 14: **0.5493** | WHISTLE, FLAG, THOU, HAIL                                         | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
   - Group 15: **0.5175** | SPIN, FLOP, WAVE, ANON                                            | INCORRECT (Max overlap: 1/4 with PARTIALITY)
   - Group 16: **0.5775** | WILT, THOU, HAIL, HOLE                                            | INCORRECT (Max overlap: 2/4 with SHAKESPEAREAN WORDS)
   - Group 17: **0.5159** | WHISTLE, RIVER, ART, WAVE                                         | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 18: **0.6186** | SPIN, FLOP, BIAS, ANON                                            | INCORRECT (Max overlap: 2/4 with PARTIALITY)
   - Group 19: **0.5190** | WHISTLE, FLAG, RIVER, HOLE                                        | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 20: **0.4998** | SLANT, TURN, WAVE, ANGLE                                          | INCORRECT (Max overlap: 2/4 with PARTIALITY)

---

## Puzzle 59 (ID: 892)
**Words on Board:** PLASTER, FIX, ENAMEL, ARTY, KISS, PASTE, CROWN, DECAY, SKIM, ESSAY, STICK, ROOT, PULP, BRUSH, ANY, STROKE

### Ground Truth Categories:
* **Level 0 (ADHERE) [Type: SYNONYM_OR_NEAR]:** FIX, PASTE, PLASTER, STICK
* **Level 1 (GRAZE) [Type: SYNONYM_OR_NEAR]:** BRUSH, KISS, SKIM, STROKE
* **Level 2 (PARTS OF A TOOTH) [Type: SEMANTIC_SET]:** CROWN, ENAMEL, PULP, ROOT
* **Level 3 (WORDS THAT SOUND LIKE TWO LETTERS) [Type: SOUND_OR_SPELLING]:** ANY, ARTY, DECAY, ESSAY

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7340** | KISS, SKIM, BRUSH, STROKE                                         | CORRECT GROUP (GRAZE, Level 1)
   - Group 2: **0.7263** | PLASTER, PASTE, CROWN, BRUSH                                      | INCORRECT (Max overlap: 2/4 with ADHERE)
   - Group 3: **0.6688** | ARTY, ROOT, PULP, ANY                                             | INCORRECT (Max overlap: 2/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 4: **0.6525** | CROWN, ROOT, PULP, ANY                                            | INCORRECT (Max overlap: 3/4 with PARTS OF A TOOTH)
   - Group 5: **0.6489** | PASTE, CROWN, ROOT, BRUSH                                         | INCORRECT (Max overlap: 2/4 with PARTS OF A TOOTH)
   - Group 6: **0.6467** | KISS, PASTE, CROWN, BRUSH                                         | INCORRECT (Max overlap: 2/4 with GRAZE)
   - Group 7: **0.6447** | KISS, PASTE, BRUSH, STROKE                                        | INCORRECT (Max overlap: 3/4 with GRAZE)
   - Group 8: **0.6434** | PLASTER, PASTE, SKIM, BRUSH                                       | INCORRECT (Max overlap: 2/4 with ADHERE)
   - Group 9: **0.6430** | KISS, PASTE, SKIM, BRUSH                                          | INCORRECT (Max overlap: 3/4 with GRAZE)
   - Group 10: **0.6341** | PASTE, CROWN, PULP, BRUSH                                         | INCORRECT (Max overlap: 2/4 with PARTS OF A TOOTH)
   - Group 11: **0.6328** | KISS, CROWN, BRUSH, STROKE                                        | INCORRECT (Max overlap: 3/4 with GRAZE)
   - Group 12: **0.6289** | PASTE, CROWN, BRUSH, STROKE                                       | INCORRECT (Max overlap: 2/4 with GRAZE)
   - Group 13: **0.6221** | CROWN, ROOT, PULP, BRUSH                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A TOOTH)
   - Group 14: **0.6218** | KISS, ROOT, BRUSH, STROKE                                         | INCORRECT (Max overlap: 3/4 with GRAZE)
   - Group 15: **0.6211** | PLASTER, PASTE, STICK, BRUSH                                      | INCORRECT (Max overlap: 3/4 with ADHERE)
   - Group 16: **0.6192** | ARTY, KISS, ROOT, ANY                                             | INCORRECT (Max overlap: 2/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 17: **0.6150** | ARTY, CROWN, ROOT, ANY                                            | INCORRECT (Max overlap: 2/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 18: **0.6109** | ENAMEL, PASTE, CROWN, BRUSH                                       | INCORRECT (Max overlap: 2/4 with PARTS OF A TOOTH)
   - Group 19: **0.6107** | PASTE, CROWN, ROOT, PULP                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A TOOTH)
   - Group 20: **0.6084** | KISS, BRUSH, ANY, STROKE                                          | INCORRECT (Max overlap: 3/4 with GRAZE)

---

## Puzzle 60 (ID: 109)
**Words on Board:** HUNT, CRUNK, GRIME, DRILL, FORAGE, FISH, GLITTER, BEER, RAIL, GLEAM, FLASH, YEAR, BULB, TRAP, SPARKLE, BOUNCE

### Ground Truth Categories:
* **Level 0 (REFLECT LIGHT) [Type: SYNONYM_OR_NEAR]:** FLASH, GLEAM, GLITTER, SPARKLE
* **Level 1 (WAYS TO GATHER FOOD) [Type: SEMANTIC_SET]:** FISH, FORAGE, HUNT, TRAP
* **Level 2 (RAP SUBGENRES) [Type: NAMED_ENTITY_SET]:** BOUNCE, CRUNK, DRILL, GRIME
* **Level 3 (LIGHT ___) [Type: FILL_IN_THE_BLANK]:** BEER, BULB, RAIL, YEAR

### Top Candidate Partitions:
1. **Partition Score: 0.5507**
   - Group 1: **0.9659** | GLITTER, GLEAM, FLASH, SPARKLE                                    | CORRECT GROUP (REFLECT LIGHT, Level 0)
   - Group 2: **0.5554** | HUNT, FORAGE, FISH, RAIL                                          | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 3: **0.5508** | GRIME, DRILL, BULB, TRAP                                          | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 4: **0.5482** | CRUNK, BEER, YEAR, BOUNCE                                         | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
2. **Partition Score: 0.5433**
   - Group 1: **0.9659** | GLITTER, GLEAM, FLASH, SPARKLE                                    | CORRECT GROUP (REFLECT LIGHT, Level 0)
   - Group 2: **0.6042** | FISH, BEER, YEAR, BOUNCE                                          | INCORRECT (Max overlap: 2/4 with LIGHT ___)
   - Group 3: **0.5409** | CRUNK, GRIME, FORAGE, RAIL                                        | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 4: **0.5140** | HUNT, DRILL, BULB, TRAP                                           | INCORRECT (Max overlap: 2/4 with WAYS TO GATHER FOOD)
3. **Partition Score: 0.5425**
   - Group 1: **0.9659** | GLITTER, GLEAM, FLASH, SPARKLE                                    | CORRECT GROUP (REFLECT LIGHT, Level 0)
   - Group 2: **0.6042** | FISH, BEER, YEAR, BOUNCE                                          | INCORRECT (Max overlap: 2/4 with LIGHT ___)
   - Group 3: **0.5508** | GRIME, DRILL, BULB, TRAP                                          | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 4: **0.5074** | HUNT, CRUNK, FORAGE, RAIL                                         | INCORRECT (Max overlap: 2/4 with WAYS TO GATHER FOOD)
4. **Partition Score: 0.5397**
   - Group 1: **0.9659** | GLITTER, GLEAM, FLASH, SPARKLE                                    | CORRECT GROUP (REFLECT LIGHT, Level 0)
   - Group 2: **0.6042** | FISH, BEER, YEAR, BOUNCE                                          | INCORRECT (Max overlap: 2/4 with LIGHT ___)
   - Group 3: **0.5669** | HUNT, FORAGE, RAIL, TRAP                                          | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 4: **0.4938** | CRUNK, GRIME, DRILL, BULB                                         | INCORRECT (Max overlap: 3/4 with RAP SUBGENRES)
5. **Partition Score: 0.5396**
   - Group 1: **0.9659** | GLITTER, GLEAM, FLASH, SPARKLE                                    | CORRECT GROUP (REFLECT LIGHT, Level 0)
   - Group 2: **0.6167** | HUNT, GRIME, FORAGE, TRAP                                         | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 3: **0.6042** | FISH, BEER, YEAR, BOUNCE                                          | INCORRECT (Max overlap: 2/4 with LIGHT ___)
   - Group 4: **0.4688** | CRUNK, DRILL, RAIL, BULB                                          | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)

### Top Candidate Groups:
   - Group 1: **0.9659** | GLITTER, GLEAM, FLASH, SPARKLE                                    | CORRECT GROUP (REFLECT LIGHT, Level 0)
   - Group 2: **0.5554** | HUNT, FORAGE, FISH, RAIL                                          | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 3: **0.5508** | GRIME, DRILL, BULB, TRAP                                          | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 4: **0.5482** | CRUNK, BEER, YEAR, BOUNCE                                         | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 5: **0.6042** | FISH, BEER, YEAR, BOUNCE                                          | INCORRECT (Max overlap: 2/4 with LIGHT ___)
   - Group 6: **0.5409** | CRUNK, GRIME, FORAGE, RAIL                                        | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 7: **0.5140** | HUNT, DRILL, BULB, TRAP                                           | INCORRECT (Max overlap: 2/4 with WAYS TO GATHER FOOD)
   - Group 8: **0.5074** | HUNT, CRUNK, FORAGE, RAIL                                         | INCORRECT (Max overlap: 2/4 with WAYS TO GATHER FOOD)
   - Group 9: **0.5669** | HUNT, FORAGE, RAIL, TRAP                                          | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 10: **0.4938** | CRUNK, GRIME, DRILL, BULB                                         | INCORRECT (Max overlap: 3/4 with RAP SUBGENRES)
   - Group 11: **0.6167** | HUNT, GRIME, FORAGE, TRAP                                         | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 12: **0.4688** | CRUNK, DRILL, RAIL, BULB                                          | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 13: **0.5431** | HUNT, CRUNK, FORAGE, FISH                                         | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 14: **0.5247** | BEER, RAIL, YEAR, BOUNCE                                          | INCORRECT (Max overlap: 3/4 with LIGHT ___)
   - Group 15: **0.5748** | CRUNK, GRIME, DRILL, RAIL                                         | INCORRECT (Max overlap: 3/4 with RAP SUBGENRES)
   - Group 16: **0.4772** | HUNT, FORAGE, BULB, TRAP                                          | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 17: **0.5244** | HUNT, FORAGE, FISH, BOUNCE                                        | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 18: **0.5211** | CRUNK, BEER, RAIL, YEAR                                           | INCORRECT (Max overlap: 3/4 with LIGHT ___)
   - Group 19: **0.5845** | FISH, BEER, RAIL, YEAR                                            | INCORRECT (Max overlap: 3/4 with LIGHT ___)
   - Group 20: **0.5081** | CRUNK, GRIME, FORAGE, BOUNCE                                      | INCORRECT (Max overlap: 3/4 with RAP SUBGENRES)

---

## Puzzle 61 (ID: 935)
**Words on Board:** STANDARD, EEK, LOG, ALE, EXAMPLE, METRIC, RECORD, QUASH, ROUTINE, BIT, BAR, NOTE, GAG, JOT, NUMBER, HIVE

### Ground Truth Categories:
* **Level 0 (WRITE) [Type: SYNONYM_OR_NEAR]:** JOT, LOG, NOTE, RECORD
* **Level 1 (SHTICK) [Type: SYNONYM_OR_NEAR]:** BIT, GAG, NUMBER, ROUTINE
* **Level 2 (BENCHMARK) [Type: SYNONYM_OR_NEAR]:** BAR, EXAMPLE, METRIC, STANDARD
* **Level 3 (VEGETABLES MINUS STARTING LETTER) [Type: WORDPLAY_TRANSFORM]:** ALE, EEK, HIVE, QUASH

### Top Candidate Partitions:
1. **Partition Score: 0.4444**
   - Group 1: **0.6293** | LOG, RECORD, NOTE, JOT                                            | CORRECT GROUP (WRITE, Level 0)
   - Group 2: **0.4614** | METRIC, BIT, BAR, GAG                                             | INCORRECT (Max overlap: 2/4 with BENCHMARK)
   - Group 3: **0.4505** | EEK, ALE, QUASH, HIVE                                             | CORRECT GROUP (VEGETABLES MINUS STARTING LETTER, Level 3)
   - Group 4: **0.4329** | STANDARD, EXAMPLE, ROUTINE, NUMBER                                | INCORRECT (Max overlap: 2/4 with BENCHMARK)
2. **Partition Score: 0.4386**
   - Group 1: **0.6293** | LOG, RECORD, NOTE, JOT                                            | CORRECT GROUP (WRITE, Level 0)
   - Group 2: **0.4957** | EXAMPLE, ROUTINE, BIT, NUMBER                                     | INCORRECT (Max overlap: 3/4 with SHTICK)
   - Group 3: **0.4505** | EEK, ALE, QUASH, HIVE                                             | CORRECT GROUP (VEGETABLES MINUS STARTING LETTER, Level 3)
   - Group 4: **0.4040** | STANDARD, METRIC, BAR, GAG                                        | INCORRECT (Max overlap: 3/4 with BENCHMARK)
3. **Partition Score: 0.4268**
   - Group 1: **0.6016** | LOG, RECORD, ROUTINE, NOTE                                        | INCORRECT (Max overlap: 3/4 with WRITE)
   - Group 2: **0.4505** | EEK, ALE, QUASH, HIVE                                             | CORRECT GROUP (VEGETABLES MINUS STARTING LETTER, Level 3)
   - Group 3: **0.4290** | BIT, BAR, GAG, JOT                                                | INCORRECT (Max overlap: 2/4 with SHTICK)
   - Group 4: **0.4139** | STANDARD, EXAMPLE, METRIC, NUMBER                                 | INCORRECT (Max overlap: 3/4 with BENCHMARK)
4. **Partition Score: 0.4251**
   - Group 1: **0.4895** | LOG, RECORD, ROUTINE, JOT                                         | INCORRECT (Max overlap: 3/4 with WRITE)
   - Group 2: **0.4505** | EEK, ALE, QUASH, HIVE                                             | CORRECT GROUP (VEGETABLES MINUS STARTING LETTER, Level 3)
   - Group 3: **0.4221** | BIT, BAR, NOTE, GAG                                               | INCORRECT (Max overlap: 2/4 with SHTICK)
   - Group 4: **0.4139** | STANDARD, EXAMPLE, METRIC, NUMBER                                 | INCORRECT (Max overlap: 3/4 with BENCHMARK)
5. **Partition Score: 0.4237**
   - Group 1: **0.6293** | LOG, RECORD, NOTE, JOT                                            | CORRECT GROUP (WRITE, Level 0)
   - Group 2: **0.4646** | ROUTINE, BIT, GAG, NUMBER                                         | CORRECT GROUP (SHTICK, Level 1)
   - Group 3: **0.4505** | EEK, ALE, QUASH, HIVE                                             | CORRECT GROUP (VEGETABLES MINUS STARTING LETTER, Level 3)
   - Group 4: **0.3899** | STANDARD, EXAMPLE, METRIC, BAR                                    | CORRECT GROUP (BENCHMARK, Level 2)

### Top Candidate Groups:
   - Group 1: **0.6293** | LOG, RECORD, NOTE, JOT                                            | CORRECT GROUP (WRITE, Level 0)
   - Group 2: **0.4614** | METRIC, BIT, BAR, GAG                                             | INCORRECT (Max overlap: 2/4 with BENCHMARK)
   - Group 3: **0.4505** | EEK, ALE, QUASH, HIVE                                             | CORRECT GROUP (VEGETABLES MINUS STARTING LETTER, Level 3)
   - Group 4: **0.4329** | STANDARD, EXAMPLE, ROUTINE, NUMBER                                | INCORRECT (Max overlap: 2/4 with BENCHMARK)
   - Group 5: **0.4957** | EXAMPLE, ROUTINE, BIT, NUMBER                                     | INCORRECT (Max overlap: 3/4 with SHTICK)
   - Group 6: **0.4040** | STANDARD, METRIC, BAR, GAG                                        | INCORRECT (Max overlap: 3/4 with BENCHMARK)
   - Group 7: **0.6016** | LOG, RECORD, ROUTINE, NOTE                                        | INCORRECT (Max overlap: 3/4 with WRITE)
   - Group 8: **0.4290** | BIT, BAR, GAG, JOT                                                | INCORRECT (Max overlap: 2/4 with SHTICK)
   - Group 9: **0.4139** | STANDARD, EXAMPLE, METRIC, NUMBER                                 | INCORRECT (Max overlap: 3/4 with BENCHMARK)
   - Group 10: **0.4895** | LOG, RECORD, ROUTINE, JOT                                         | INCORRECT (Max overlap: 3/4 with WRITE)
   - Group 11: **0.4221** | BIT, BAR, NOTE, GAG                                               | INCORRECT (Max overlap: 2/4 with SHTICK)
   - Group 12: **0.4646** | ROUTINE, BIT, GAG, NUMBER                                         | CORRECT GROUP (SHTICK, Level 1)
   - Group 13: **0.3899** | STANDARD, EXAMPLE, METRIC, BAR                                    | CORRECT GROUP (BENCHMARK, Level 2)
   - Group 14: **0.4103** | EEK, ALE, GAG, HIVE                                               | INCORRECT (Max overlap: 3/4 with VEGETABLES MINUS STARTING LETTER)
   - Group 15: **0.3832** | STANDARD, METRIC, QUASH, BAR                                      | INCORRECT (Max overlap: 3/4 with BENCHMARK)
   - Group 16: **0.5280** | METRIC, ROUTINE, BIT, NUMBER                                      | INCORRECT (Max overlap: 3/4 with SHTICK)
   - Group 17: **0.3414** | STANDARD, EXAMPLE, BAR, GAG                                       | INCORRECT (Max overlap: 3/4 with BENCHMARK)
   - Group 18: **0.4757** | METRIC, BIT, GAG, NUMBER                                          | INCORRECT (Max overlap: 3/4 with SHTICK)
   - Group 19: **0.3626** | STANDARD, EXAMPLE, BAR, NOTE                                      | INCORRECT (Max overlap: 3/4 with BENCHMARK)
   - Group 20: **0.4141** | LOG, RECORD, ROUTINE, NUMBER                                      | INCORRECT (Max overlap: 2/4 with WRITE)

---

## Puzzle 62 (ID: 520)
**Words on Board:** SPEED, FLORET, SCALES, CLOVE, GRUMBLE, RESOLUTION, CARP, RAM, STORAGE, STALK, CRAB, BLINDFOLD, SPEAR, ROBE, SWORD, BELLYACHE

### Ground Truth Categories:
* **Level 0 (COMPLAIN) [Type: SYNONYM_OR_NEAR]:** BELLYACHE, CARP, CRAB, GRUMBLE
* **Level 1 (VEGETABLE UNITS) [Type: SEMANTIC_SET]:** CLOVE, FLORET, SPEAR, STALK
* **Level 2 (LAPTOP SPECS) [Type: SEMANTIC_SET]:** RAM, RESOLUTION, SPEED, STORAGE
* **Level 3 (FEATURES OF JUSTICE PERSONIFIED) [Type: SEMANTIC_SET]:** BLINDFOLD, ROBE, SCALES, SWORD

### Top Candidate Partitions:
1. **Partition Score: 0.5237**
   - Group 1: **0.5603** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN)
   - Group 2: **0.5529** | FLORET, SCALES, CARP, STALK                                       | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 3: **0.5384** | CLOVE, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 4: **0.5017** | SPEED, RESOLUTION, RAM, STORAGE                                   | CORRECT GROUP (LAPTOP SPECS, Level 2)
2. **Partition Score: 0.5165**
   - Group 1: **0.5619** | FLORET, CLOVE, CARP, STALK                                        | INCORRECT (Max overlap: 3/4 with VEGETABLE UNITS)
   - Group 2: **0.5603** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN)
   - Group 3: **0.5023** | SCALES, SPEAR, ROBE, SWORD                                        | INCORRECT (Max overlap: 3/4 with FEATURES OF JUSTICE PERSONIFIED)
   - Group 4: **0.5017** | SPEED, RESOLUTION, RAM, STORAGE                                   | CORRECT GROUP (LAPTOP SPECS, Level 2)
3. **Partition Score: 0.5164**
   - Group 1: **0.5827** | FLORET, SCALES, CLOVE, STALK                                      | INCORRECT (Max overlap: 3/4 with VEGETABLE UNITS)
   - Group 2: **0.5603** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN)
   - Group 3: **0.5017** | CARP, SPEAR, ROBE, SWORD                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF JUSTICE PERSONIFIED)
   - Group 4: **0.5017** | SPEED, RESOLUTION, RAM, STORAGE                                   | CORRECT GROUP (LAPTOP SPECS, Level 2)
4. **Partition Score: 0.5156**
   - Group 1: **0.5603** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN)
   - Group 2: **0.5372** | FLORET, SCALES, STALK, ROBE                                       | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 3: **0.5217** | CLOVE, CARP, SPEAR, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 4: **0.5017** | SPEED, RESOLUTION, RAM, STORAGE                                   | CORRECT GROUP (LAPTOP SPECS, Level 2)
5. **Partition Score: 0.5149**
   - Group 1: **0.6000** | GRUMBLE, STALK, CRAB, BELLYACHE                                   | INCORRECT (Max overlap: 3/4 with COMPLAIN)
   - Group 2: **0.5296** | FLORET, SCALES, CARP, SWORD                                       | INCORRECT (Max overlap: 2/4 with FEATURES OF JUSTICE PERSONIFIED)
   - Group 3: **0.5268** | CLOVE, BLINDFOLD, SPEAR, ROBE                                     | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 4: **0.5017** | SPEED, RESOLUTION, RAM, STORAGE                                   | CORRECT GROUP (LAPTOP SPECS, Level 2)

### Top Candidate Groups:
   - Group 1: **0.5603** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN)
   - Group 2: **0.5529** | FLORET, SCALES, CARP, STALK                                       | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 3: **0.5384** | CLOVE, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 4: **0.5017** | SPEED, RESOLUTION, RAM, STORAGE                                   | CORRECT GROUP (LAPTOP SPECS, Level 2)
   - Group 5: **0.5619** | FLORET, CLOVE, CARP, STALK                                        | INCORRECT (Max overlap: 3/4 with VEGETABLE UNITS)
   - Group 6: **0.5023** | SCALES, SPEAR, ROBE, SWORD                                        | INCORRECT (Max overlap: 3/4 with FEATURES OF JUSTICE PERSONIFIED)
   - Group 7: **0.5827** | FLORET, SCALES, CLOVE, STALK                                      | INCORRECT (Max overlap: 3/4 with VEGETABLE UNITS)
   - Group 8: **0.5017** | CARP, SPEAR, ROBE, SWORD                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF JUSTICE PERSONIFIED)
   - Group 9: **0.5372** | FLORET, SCALES, STALK, ROBE                                       | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 10: **0.5217** | CLOVE, CARP, SPEAR, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 11: **0.6000** | GRUMBLE, STALK, CRAB, BELLYACHE                                   | INCORRECT (Max overlap: 3/4 with COMPLAIN)
   - Group 12: **0.5296** | FLORET, SCALES, CARP, SWORD                                       | INCORRECT (Max overlap: 2/4 with FEATURES OF JUSTICE PERSONIFIED)
   - Group 13: **0.5268** | CLOVE, BLINDFOLD, SPEAR, ROBE                                     | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 14: **0.5141** | FLORET, SCALES, BLINDFOLD, ROBE                                   | INCORRECT (Max overlap: 3/4 with FEATURES OF JUSTICE PERSONIFIED)
   - Group 15: **0.5525** | FLORET, CLOVE, STALK, ROBE                                        | INCORRECT (Max overlap: 3/4 with VEGETABLE UNITS)
   - Group 16: **0.4917** | SCALES, CARP, SPEAR, SWORD                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF JUSTICE PERSONIFIED)
   - Group 17: **0.5450** | GRUMBLE, CRAB, ROBE, BELLYACHE                                    | INCORRECT (Max overlap: 3/4 with COMPLAIN)
   - Group 18: **0.5123** | FLORET, SCALES, STALK, BLINDFOLD                                  | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 19: **0.5234** | FLORET, CARP, STALK, ROBE                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 20: **0.5098** | SCALES, CLOVE, SPEAR, SWORD                                       | INCORRECT (Max overlap: 2/4 with FEATURES OF JUSTICE PERSONIFIED)

---

## Puzzle 63 (ID: 183)
**Words on Board:** SILK, LACE, LAND, SOLE, SETTLE, BLOW, BABY, EYELET, PACKAGE, SPEECH, PERCH, ROOST, CHIFFON, TONGUE, SATIN, VELVET

### Ground Truth Categories:
* **Level 0 (LUXURIOUS FABRICS) [Type: SEMANTIC_SET]:** CHIFFON, SATIN, SILK, VELVET
* **Level 1 (COME DOWN TO REST) [Type: SYNONYM_OR_NEAR]:** PERCH, ROOST, SETTLE, LAND
* **Level 2 (SHOE PARTS) [Type: SEMANTIC_SET]:** EYELET, LACE, SOLE, TONGUE
* **Level 3 (THINGS THAT ARE DELIVERED) [Type: FILL_IN_THE_BLANK]:** BABY, BLOW, PACKAGE, SPEECH

### Top Candidate Partitions:
1. **Partition Score: 0.5236**
   - Group 1: **0.7443** | SILK, LACE, CHIFFON, VELVET                                       | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS)
   - Group 2: **0.6242** | LAND, SOLE, BLOW, TONGUE                                          | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 3: **0.5064** | SETTLE, PACKAGE, PERCH, ROOST                                     | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST)
   - Group 4: **0.4819** | BABY, EYELET, SPEECH, SATIN                                       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
2. **Partition Score: 0.5160**
   - Group 1: **0.7443** | SILK, LACE, CHIFFON, VELVET                                       | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS)
   - Group 2: **0.5669** | LAND, SETTLE, PERCH, ROOST                                        | CORRECT GROUP (COME DOWN TO REST, Level 1)
   - Group 3: **0.5332** | SOLE, BLOW, PACKAGE, TONGUE                                       | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 4: **0.4819** | BABY, EYELET, SPEECH, SATIN                                       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
3. **Partition Score: 0.5135**
   - Group 1: **0.7362** | SILK, LACE, CHIFFON, SATIN                                        | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS)
   - Group 2: **0.6242** | LAND, SOLE, BLOW, TONGUE                                          | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 3: **0.5064** | SETTLE, PACKAGE, PERCH, ROOST                                     | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST)
   - Group 4: **0.4616** | BABY, EYELET, SPEECH, VELVET                                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
4. **Partition Score: 0.5119**
   - Group 1: **0.5669** | LAND, SETTLE, PERCH, ROOST                                        | CORRECT GROUP (COME DOWN TO REST, Level 1)
   - Group 2: **0.5266** | SOLE, BLOW, SPEECH, TONGUE                                        | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 3: **0.5122** | BABY, EYELET, SATIN, VELVET                                       | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS)
   - Group 4: **0.5044** | SILK, LACE, PACKAGE, CHIFFON                                      | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS)
5. **Partition Score: 0.5109**
   - Group 1: **0.7443** | SILK, LACE, CHIFFON, VELVET                                       | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS)
   - Group 2: **0.5858** | SOLE, SETTLE, PERCH, ROOST                                        | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST)
   - Group 3: **0.4941** | LAND, BLOW, PACKAGE, TONGUE                                       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
   - Group 4: **0.4819** | BABY, EYELET, SPEECH, SATIN                                       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)

### Top Candidate Groups:
   - Group 1: **0.7443** | SILK, LACE, CHIFFON, VELVET                                       | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS)
   - Group 2: **0.6242** | LAND, SOLE, BLOW, TONGUE                                          | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 3: **0.5064** | SETTLE, PACKAGE, PERCH, ROOST                                     | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST)
   - Group 4: **0.4819** | BABY, EYELET, SPEECH, SATIN                                       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
   - Group 5: **0.5669** | LAND, SETTLE, PERCH, ROOST                                        | CORRECT GROUP (COME DOWN TO REST, Level 1)
   - Group 6: **0.5332** | SOLE, BLOW, PACKAGE, TONGUE                                       | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 7: **0.7362** | SILK, LACE, CHIFFON, SATIN                                        | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS)
   - Group 8: **0.4616** | BABY, EYELET, SPEECH, VELVET                                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
   - Group 9: **0.5266** | SOLE, BLOW, SPEECH, TONGUE                                        | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 10: **0.5122** | BABY, EYELET, SATIN, VELVET                                       | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS)
   - Group 11: **0.5044** | SILK, LACE, PACKAGE, CHIFFON                                      | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS)
   - Group 12: **0.5858** | SOLE, SETTLE, PERCH, ROOST                                        | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST)
   - Group 13: **0.4941** | LAND, BLOW, PACKAGE, TONGUE                                       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
   - Group 14: **0.5425** | SILK, LACE, EYELET, CHIFFON                                       | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS)
   - Group 15: **0.4742** | BABY, SPEECH, SATIN, VELVET                                       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
   - Group 16: **0.6389** | SILK, BABY, SATIN, VELVET                                         | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS)
   - Group 17: **0.4615** | LACE, EYELET, PACKAGE, CHIFFON                                    | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 18: **0.5063** | SILK, BABY, EYELET, SATIN                                         | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS)
   - Group 19: **0.4895** | LACE, PACKAGE, CHIFFON, VELVET                                    | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS)
   - Group 20: **0.5476** | LACE, LAND, BLOW, TONGUE                                          | INCORRECT (Max overlap: 2/4 with SHOE PARTS)

---

## Puzzle 64 (ID: 781)
**Words on Board:** LAUGH, RAIL, AID, STRAW, EYE, ROCK, RESORT, PARTY, COMING, LADY, NATURE, FIDDLE, NATIONS, SUPPER, RESPONDER, GUESS

### Ground Truth Categories:
* **Level 0 (FIRST ___) [Type: FILL_IN_THE_BLANK]:** AID, LADY, NATIONS, RESPONDER
* **Level 1 (SECOND ___) [Type: FILL_IN_THE_BLANK]:** COMING, FIDDLE, GUESS, NATURE
* **Level 2 (THIRD ___) [Type: FILL_IN_THE_BLANK]:** EYE, PARTY, RAIL, ROCK
* **Level 3 (LAST ___) [Type: FILL_IN_THE_BLANK]:** LAUGH, RESORT, STRAW, SUPPER

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.5802** | LAUGH, ROCK, LADY, FIDDLE                                         | INCORRECT (Max overlap: 1/4 with LAST ___)
   - Group 2: **0.5627** | LAUGH, EYE, ROCK, LADY                                            | INCORRECT (Max overlap: 2/4 with THIRD ___)
   - Group 3: **0.5615** | LAUGH, RAIL, ROCK, FIDDLE                                         | INCORRECT (Max overlap: 2/4 with THIRD ___)
   - Group 4: **0.5610** | LAUGH, STRAW, ROCK, LADY                                          | INCORRECT (Max overlap: 2/4 with LAST ___)
   - Group 5: **0.5603** | LAUGH, ROCK, LADY, NATIONS                                        | INCORRECT (Max overlap: 2/4 with FIRST ___)
   - Group 6: **0.5562** | LAUGH, ROCK, LADY, GUESS                                          | INCORRECT (Max overlap: 1/4 with LAST ___)
   - Group 7: **0.5506** | RAIL, ROCK, LADY, FIDDLE                                          | INCORRECT (Max overlap: 2/4 with THIRD ___)
   - Group 8: **0.5428** | LAUGH, ROCK, NATIONS, GUESS                                       | INCORRECT (Max overlap: 1/4 with LAST ___)
   - Group 9: **0.5427** | LAUGH, EYE, ROCK, FIDDLE                                          | INCORRECT (Max overlap: 2/4 with THIRD ___)
   - Group 10: **0.5419** | LAUGH, EYE, LADY, FIDDLE                                          | INCORRECT (Max overlap: 1/4 with LAST ___)
   - Group 11: **0.5406** | RAIL, ROCK, FIDDLE, NATIONS                                       | INCORRECT (Max overlap: 2/4 with THIRD ___)
   - Group 12: **0.5332** | RAIL, ROCK, FIDDLE, GUESS                                         | INCORRECT (Max overlap: 2/4 with THIRD ___)
   - Group 13: **0.5319** | RAIL, EYE, ROCK, FIDDLE                                           | INCORRECT (Max overlap: 3/4 with THIRD ___)
   - Group 14: **0.5317** | LAUGH, STRAW, ROCK, GUESS                                         | INCORRECT (Max overlap: 2/4 with LAST ___)
   - Group 15: **0.5300** | LAUGH, RAIL, ROCK, LADY                                           | INCORRECT (Max overlap: 2/4 with THIRD ___)
   - Group 16: **0.5298** | ROCK, LADY, FIDDLE, NATIONS                                       | INCORRECT (Max overlap: 2/4 with FIRST ___)
   - Group 17: **0.5295** | EYE, ROCK, LADY, FIDDLE                                           | INCORRECT (Max overlap: 2/4 with THIRD ___)
   - Group 18: **0.5282** | LAUGH, ROCK, FIDDLE, GUESS                                        | INCORRECT (Max overlap: 2/4 with SECOND ___)
   - Group 19: **0.5281** | STRAW, ROCK, LADY, FIDDLE                                         | INCORRECT (Max overlap: 1/4 with LAST ___)
   - Group 20: **0.5279** | ROCK, LADY, NATIONS, GUESS                                        | INCORRECT (Max overlap: 2/4 with FIRST ___)

---

## Puzzle 65 (ID: 513)
**Words on Board:** TURTLE, DONKEY, CARPET, PRINCESS, FLEECE, MUSHROOM, MARKER, EGG, CLAM, NUT, OGRE, KINGDOM, DRAGON, PEACH, PIPE CLEANER, CATERPILLAR

### Ground Truth Categories:
* **Level 0 (THINGS THAT ARE FUZZY) [Type: SEMANTIC_SET]:** CATERPILLAR, FLEECE, PEACH, PIPE CLEANER
* **Level 1 (THINGS WITH SHELLS) [Type: SEMANTIC_SET]:** CLAM, EGG, NUT, TURTLE
* **Level 2 (FIGURES IN “SHREK”) [Type: NAMED_ENTITY_SET]:** DONKEY, DRAGON, OGRE, PRINCESS
* **Level 3 (MAGIC ___) [Type: FILL_IN_THE_BLANK]:** CARPET, KINGDOM, MARKER, MUSHROOM

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6965** | TURTLE, DONKEY, KINGDOM, DRAGON                                   | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 2: **0.6862** | TURTLE, DONKEY, OGRE, DRAGON                                      | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”)
   - Group 3: **0.6596** | DONKEY, OGRE, KINGDOM, DRAGON                                     | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”)
   - Group 4: **0.6560** | TURTLE, OGRE, KINGDOM, DRAGON                                     | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 5: **0.6506** | TURTLE, PRINCESS, OGRE, KINGDOM                                   | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 6: **0.6423** | TURTLE, DONKEY, OGRE, KINGDOM                                     | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 7: **0.6406** | TURTLE, MUSHROOM, OGRE, KINGDOM                                   | INCORRECT (Max overlap: 2/4 with MAGIC ___)
   - Group 8: **0.6396** | TURTLE, DONKEY, MUSHROOM, DRAGON                                  | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 9: **0.6393** | TURTLE, MUSHROOM, KINGDOM, DRAGON                                 | INCORRECT (Max overlap: 2/4 with MAGIC ___)
   - Group 10: **0.6392** | TURTLE, DONKEY, MUSHROOM, KINGDOM                                 | INCORRECT (Max overlap: 2/4 with MAGIC ___)
   - Group 11: **0.6375** | TURTLE, DONKEY, MARKER, DRAGON                                    | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 12: **0.6372** | TURTLE, MUSHROOM, OGRE, DRAGON                                    | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 13: **0.6340** | TURTLE, DONKEY, CARPET, DRAGON                                    | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 14: **0.6338** | TURTLE, DONKEY, MUSHROOM, OGRE                                    | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 15: **0.6337** | TURTLE, EGG, OGRE, DRAGON                                         | INCORRECT (Max overlap: 2/4 with THINGS WITH SHELLS)
   - Group 16: **0.6331** | DONKEY, CARPET, KINGDOM, DRAGON                                   | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 17: **0.6300** | TURTLE, PRINCESS, KINGDOM, DRAGON                                 | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 18: **0.6286** | DONKEY, MUSHROOM, KINGDOM, DRAGON                                 | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 19: **0.6277** | TURTLE, PRINCESS, OGRE, DRAGON                                    | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”)
   - Group 20: **0.6265** | PRINCESS, OGRE, KINGDOM, DRAGON                                   | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”)

---

## Puzzle 66 (ID: 999)
**Words on Board:** WEARABLE, WHEREFORE, FISHBOWL, WAREHOUSE, FOZZIE, HOT SEAT, MICROSCOPE, VIDEO GAME, GONZO, SPOTLIGHT, ANIMAL, COMPANY, BEAKER, E STREET BAND, MAFIA, WEREWOLF

### Ground Truth Categories:
* **Level 0 (STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY) [Type: SOUND_OR_SPELLING]:** WAREHOUSE, WEARABLE, WEREWOLF, WHEREFORE
* **Level 1 (METAPHORS FOR PUBLIC SCRUTINY) [Type: COMMON_PHRASE]:** FISHBOWL, HOT SEAT, MICROSCOPE, SPOTLIGHT
* **Level 2 (MUPPETS) [Type: NAMED_ENTITY_SET]:** ANIMAL, BEAKER, FOZZIE, GONZO
* **Level 3 (THEY FEATURE A BOSS) [Type: SEMANTIC_SET]:** COMPANY, E STREET BAND, MAFIA, VIDEO GAME

### Top Candidate Partitions:
1. **Partition Score: 0.5238**
   - Group 1: **0.5403** | WHEREFORE, FISHBOWL, MICROSCOPE, BEAKER                           | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 2: **0.5338** | WEARABLE, VIDEO GAME, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 3: **0.5325** | WAREHOUSE, HOT SEAT, COMPANY, E STREET BAND                       | INCORRECT (Max overlap: 2/4 with THEY FEATURE A BOSS)
   - Group 4: **0.5144** | FOZZIE, GONZO, ANIMAL, MAFIA                                      | INCORRECT (Max overlap: 3/4 with MUPPETS)
2. **Partition Score: 0.5229**
   - Group 1: **0.5403** | WHEREFORE, FISHBOWL, MICROSCOPE, BEAKER                           | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 2: **0.5352** | WEARABLE, WAREHOUSE, SPOTLIGHT, WEREWOLF                          | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 3: **0.5276** | HOT SEAT, VIDEO GAME, COMPANY, E STREET BAND                      | INCORRECT (Max overlap: 3/4 with THEY FEATURE A BOSS)
   - Group 4: **0.5144** | FOZZIE, GONZO, ANIMAL, MAFIA                                      | INCORRECT (Max overlap: 3/4 with MUPPETS)
3. **Partition Score: 0.5226**
   - Group 1: **0.5491** | WHEREFORE, FISHBOWL, WAREHOUSE, BEAKER                            | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 2: **0.5340** | WEARABLE, MICROSCOPE, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 3: **0.5276** | HOT SEAT, VIDEO GAME, COMPANY, E STREET BAND                      | INCORRECT (Max overlap: 3/4 with THEY FEATURE A BOSS)
   - Group 4: **0.5144** | FOZZIE, GONZO, ANIMAL, MAFIA                                      | INCORRECT (Max overlap: 3/4 with MUPPETS)
4. **Partition Score: 0.5226**
   - Group 1: **0.5368** | FISHBOWL, VIDEO GAME, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 2: **0.5325** | WAREHOUSE, HOT SEAT, COMPANY, E STREET BAND                       | INCORRECT (Max overlap: 2/4 with THEY FEATURE A BOSS)
   - Group 3: **0.5290** | WEARABLE, WHEREFORE, MICROSCOPE, BEAKER                           | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 4: **0.5144** | FOZZIE, GONZO, ANIMAL, MAFIA                                      | INCORRECT (Max overlap: 3/4 with MUPPETS)
5. **Partition Score: 0.5225**
   - Group 1: **0.5432** | FISHBOWL, MICROSCOPE, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 3/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 2: **0.5337** | WEARABLE, WHEREFORE, WAREHOUSE, BEAKER                            | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 3: **0.5276** | HOT SEAT, VIDEO GAME, COMPANY, E STREET BAND                      | INCORRECT (Max overlap: 3/4 with THEY FEATURE A BOSS)
   - Group 4: **0.5144** | FOZZIE, GONZO, ANIMAL, MAFIA                                      | INCORRECT (Max overlap: 3/4 with MUPPETS)

### Top Candidate Groups:
   - Group 1: **0.5403** | WHEREFORE, FISHBOWL, MICROSCOPE, BEAKER                           | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 2: **0.5338** | WEARABLE, VIDEO GAME, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 3: **0.5325** | WAREHOUSE, HOT SEAT, COMPANY, E STREET BAND                       | INCORRECT (Max overlap: 2/4 with THEY FEATURE A BOSS)
   - Group 4: **0.5144** | FOZZIE, GONZO, ANIMAL, MAFIA                                      | INCORRECT (Max overlap: 3/4 with MUPPETS)
   - Group 5: **0.5352** | WEARABLE, WAREHOUSE, SPOTLIGHT, WEREWOLF                          | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 6: **0.5276** | HOT SEAT, VIDEO GAME, COMPANY, E STREET BAND                      | INCORRECT (Max overlap: 3/4 with THEY FEATURE A BOSS)
   - Group 7: **0.5491** | WHEREFORE, FISHBOWL, WAREHOUSE, BEAKER                            | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 8: **0.5340** | WEARABLE, MICROSCOPE, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 9: **0.5368** | FISHBOWL, VIDEO GAME, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 10: **0.5290** | WEARABLE, WHEREFORE, MICROSCOPE, BEAKER                           | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 11: **0.5432** | FISHBOWL, MICROSCOPE, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 3/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 12: **0.5337** | WEARABLE, WHEREFORE, WAREHOUSE, BEAKER                            | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 13: **0.5483** | FISHBOWL, WAREHOUSE, SPOTLIGHT, WEREWOLF                          | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 14: **0.5289** | WHEREFORE, WAREHOUSE, HOT SEAT, BEAKER                            | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 15: **0.5260** | FISHBOWL, VIDEO GAME, COMPANY, E STREET BAND                      | INCORRECT (Max overlap: 3/4 with THEY FEATURE A BOSS)
   - Group 16: **0.5299** | WEARABLE, FISHBOWL, MICROSCOPE, BEAKER                            | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 17: **0.5262** | WHEREFORE, WAREHOUSE, SPOTLIGHT, WEREWOLF                         | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 18: **0.5328** | WAREHOUSE, VIDEO GAME, COMPANY, E STREET BAND                     | INCORRECT (Max overlap: 3/4 with THEY FEATURE A BOSS)
   - Group 19: **0.5202** | WHEREFORE, FISHBOWL, HOT SEAT, BEAKER                             | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 20: **0.5375** | WHEREFORE, WAREHOUSE, MICROSCOPE, BEAKER                          | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)

---

## Puzzle 67 (ID: 737)
**Words on Board:** TIMEOUT, HOTEL, FLIGHT, MARIONETTE, FREEZE, ELEPHANT, RESOLVE, SPIRIT, FIGHT, GRIT, QUIT, FAWN, MOUSE, TOUR, GLITCH, CAR

### Ground Truth Categories:
* **Level 0 (THINGS TO BOOK FOR A VACATION) [Type: SEMANTIC_SET]:** CAR, FLIGHT, HOTEL, TOUR
* **Level 1 (METTLE) [Type: SYNONYM_OR_NEAR]:** FIGHT, GRIT, RESOLVE, SPIRIT
* **Level 2 (BAD THINGS FOR A WEBSITE TO DO) [Type: SEMANTIC_SET]:** FREEZE, GLITCH, TIMEOUT, QUIT
* **Level 3 (FIGURES IN CLASSIC DISNEY ANIMATED FILMS) [Type: NAMED_ENTITY_SET]:** ELEPHANT, FAWN, MARIONETTE, MOUSE

### Top Candidate Partitions:
1. **Partition Score: 0.5572**
   - Group 1: **0.6242** | HOTEL, FLIGHT, TOUR, CAR                                          | CORRECT GROUP (THINGS TO BOOK FOR A VACATION, Level 0)
   - Group 2: **0.5882** | MARIONETTE, ELEPHANT, FAWN, MOUSE                                 | CORRECT GROUP (FIGURES IN CLASSIC DISNEY ANIMATED FILMS, Level 3)
   - Group 3: **0.5582** | TIMEOUT, FREEZE, QUIT, GLITCH                                     | CORRECT GROUP (BAD THINGS FOR A WEBSITE TO DO, Level 2)
   - Group 4: **0.5412** | RESOLVE, SPIRIT, FIGHT, GRIT                                      | CORRECT GROUP (METTLE, Level 1)
2. **Partition Score: 0.5448**
   - Group 1: **0.5582** | TIMEOUT, FREEZE, QUIT, GLITCH                                     | CORRECT GROUP (BAD THINGS FOR A WEBSITE TO DO, Level 2)
   - Group 2: **0.5536** | HOTEL, FLIGHT, MOUSE, TOUR                                        | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 3: **0.5432** | MARIONETTE, ELEPHANT, FAWN, CAR                                   | INCORRECT (Max overlap: 3/4 with FIGURES IN CLASSIC DISNEY ANIMATED FILMS)
   - Group 4: **0.5412** | RESOLVE, SPIRIT, FIGHT, GRIT                                      | CORRECT GROUP (METTLE, Level 1)
3. **Partition Score: 0.5398**
   - Group 1: **0.5882** | MARIONETTE, ELEPHANT, FAWN, MOUSE                                 | CORRECT GROUP (FIGURES IN CLASSIC DISNEY ANIMATED FILMS, Level 3)
   - Group 2: **0.5530** | HOTEL, FLIGHT, TOUR, GLITCH                                       | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 3: **0.5412** | RESOLVE, SPIRIT, FIGHT, GRIT                                      | CORRECT GROUP (METTLE, Level 1)
   - Group 4: **0.5325** | TIMEOUT, FREEZE, QUIT, CAR                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A WEBSITE TO DO)
4. **Partition Score: 0.5387**
   - Group 1: **0.5882** | MARIONETTE, ELEPHANT, FAWN, MOUSE                                 | CORRECT GROUP (FIGURES IN CLASSIC DISNEY ANIMATED FILMS, Level 3)
   - Group 2: **0.5814** | TIMEOUT, FLIGHT, FREEZE, GLITCH                                   | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A WEBSITE TO DO)
   - Group 3: **0.5412** | RESOLVE, SPIRIT, FIGHT, GRIT                                      | CORRECT GROUP (METTLE, Level 1)
   - Group 4: **0.5160** | HOTEL, QUIT, TOUR, CAR                                            | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
5. **Partition Score: 0.5376**
   - Group 1: **0.5882** | MARIONETTE, ELEPHANT, FAWN, MOUSE                                 | CORRECT GROUP (FIGURES IN CLASSIC DISNEY ANIMATED FILMS, Level 3)
   - Group 2: **0.5608** | TIMEOUT, HOTEL, FLIGHT, TOUR                                      | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 3: **0.5412** | RESOLVE, SPIRIT, FIGHT, GRIT                                      | CORRECT GROUP (METTLE, Level 1)
   - Group 4: **0.5241** | FREEZE, QUIT, GLITCH, CAR                                         | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A WEBSITE TO DO)

### Top Candidate Groups:
   - Group 1: **0.6242** | HOTEL, FLIGHT, TOUR, CAR                                          | CORRECT GROUP (THINGS TO BOOK FOR A VACATION, Level 0)
   - Group 2: **0.5882** | MARIONETTE, ELEPHANT, FAWN, MOUSE                                 | CORRECT GROUP (FIGURES IN CLASSIC DISNEY ANIMATED FILMS, Level 3)
   - Group 3: **0.5582** | TIMEOUT, FREEZE, QUIT, GLITCH                                     | CORRECT GROUP (BAD THINGS FOR A WEBSITE TO DO, Level 2)
   - Group 4: **0.5412** | RESOLVE, SPIRIT, FIGHT, GRIT                                      | CORRECT GROUP (METTLE, Level 1)
   - Group 5: **0.5536** | HOTEL, FLIGHT, MOUSE, TOUR                                        | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 6: **0.5432** | MARIONETTE, ELEPHANT, FAWN, CAR                                   | INCORRECT (Max overlap: 3/4 with FIGURES IN CLASSIC DISNEY ANIMATED FILMS)
   - Group 7: **0.5530** | HOTEL, FLIGHT, TOUR, GLITCH                                       | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 8: **0.5325** | TIMEOUT, FREEZE, QUIT, CAR                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A WEBSITE TO DO)
   - Group 9: **0.5814** | TIMEOUT, FLIGHT, FREEZE, GLITCH                                   | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A WEBSITE TO DO)
   - Group 10: **0.5160** | HOTEL, QUIT, TOUR, CAR                                            | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 11: **0.5608** | TIMEOUT, HOTEL, FLIGHT, TOUR                                      | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 12: **0.5241** | FREEZE, QUIT, GLITCH, CAR                                         | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A WEBSITE TO DO)
   - Group 13: **0.5575** | FLIGHT, FREEZE, QUIT, GLITCH                                      | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A WEBSITE TO DO)
   - Group 14: **0.5247** | TIMEOUT, HOTEL, TOUR, CAR                                         | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 15: **0.5308** | FREEZE, QUIT, MOUSE, GLITCH                                       | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A WEBSITE TO DO)
   - Group 16: **0.5516** | HOTEL, FLIGHT, FREEZE, GLITCH                                     | INCORRECT (Max overlap: 2/4 with THINGS TO BOOK FOR A VACATION)
   - Group 17: **0.5238** | TIMEOUT, QUIT, TOUR, CAR                                          | INCORRECT (Max overlap: 2/4 with BAD THINGS FOR A WEBSITE TO DO)
   - Group 18: **0.5480** | HOTEL, MOUSE, TOUR, CAR                                           | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)
   - Group 19: **0.5248** | FLIGHT, MARIONETTE, ELEPHANT, FAWN                                | INCORRECT (Max overlap: 3/4 with FIGURES IN CLASSIC DISNEY ANIMATED FILMS)
   - Group 20: **0.5535** | FLIGHT, QUIT, TOUR, CAR                                           | INCORRECT (Max overlap: 3/4 with THINGS TO BOOK FOR A VACATION)

---

## Puzzle 68 (ID: 897)
**Words on Board:** TWO-BIT, LOTTERY TICKET, CALAMINE LOTION, HAPPY MEAL, BUG BITE, FLAMINGO, TRIVIAL, SUNNY-SIDE UP, VINYL RECORD, YOUR HEAD, CHERRY BLOSSOM, BARBIE DREAMHOUSE, MERRY-GO-ROUND, MICKEY MOUSE, GLAD-HAND, RINKY-DINK

### Ground Truth Categories:
* **Level 0 (SMALL-TIME) [Type: SYNONYM_OR_NEAR]:** MICKEY MOUSE, RINKY-DINK, TRIVIAL, TWO-BIT
* **Level 1 (THINGS THAT ARE PINK) [Type: SEMANTIC_SET]:** BARBIE DREAMHOUSE, CALAMINE LOTION, CHERRY BLOSSOM, FLAMINGO
* **Level 2 (THINGS YOU CAN SCRATCH) [Type: SEMANTIC_SET]:** BUG BITE, LOTTERY TICKET, VINYL RECORD, YOUR HEAD
* **Level 3 (STARTING WITH OPTIMISTIC WORDS) [Type: WORD_FORM]:** GLAD-HAND, HAPPY MEAL, MERRY-GO-ROUND, SUNNY-SIDE UP

### Top Candidate Partitions:
1. **Partition Score: 0.4879**
   - Group 1: **0.5222** | SUNNY-SIDE UP, VINYL RECORD, MERRY-GO-ROUND, GLAD-HAND            | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 2: **0.5071** | HAPPY MEAL, FLAMINGO, CHERRY BLOSSOM, BARBIE DREAMHOUSE           | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE PINK)
   - Group 3: **0.4969** | TWO-BIT, TRIVIAL, MICKEY MOUSE, RINKY-DINK                        | CORRECT GROUP (SMALL-TIME, Level 0)
   - Group 4: **0.4737** | LOTTERY TICKET, CALAMINE LOTION, BUG BITE, YOUR HEAD              | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN SCRATCH)
2. **Partition Score: 0.4863**
   - Group 1: **0.5011** | HAPPY MEAL, VINYL RECORD, MERRY-GO-ROUND, GLAD-HAND               | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 2: **0.5006** | FLAMINGO, SUNNY-SIDE UP, CHERRY BLOSSOM, BARBIE DREAMHOUSE        | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE PINK)
   - Group 3: **0.4969** | TWO-BIT, TRIVIAL, MICKEY MOUSE, RINKY-DINK                        | CORRECT GROUP (SMALL-TIME, Level 0)
   - Group 4: **0.4737** | LOTTERY TICKET, CALAMINE LOTION, BUG BITE, YOUR HEAD              | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN SCRATCH)
3. **Partition Score: 0.4795**
   - Group 1: **0.4969** | TWO-BIT, TRIVIAL, MICKEY MOUSE, RINKY-DINK                        | CORRECT GROUP (SMALL-TIME, Level 0)
   - Group 2: **0.4941** | HAPPY MEAL, FLAMINGO, SUNNY-SIDE UP, BARBIE DREAMHOUSE            | INCORRECT (Max overlap: 2/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 3: **0.4764** | VINYL RECORD, CHERRY BLOSSOM, MERRY-GO-ROUND, GLAD-HAND           | INCORRECT (Max overlap: 2/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 4: **0.4737** | LOTTERY TICKET, CALAMINE LOTION, BUG BITE, YOUR HEAD              | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN SCRATCH)
4. **Partition Score: 0.4786**
   - Group 1: **0.5220** | HAPPY MEAL, SUNNY-SIDE UP, VINYL RECORD, GLAD-HAND                | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 2: **0.4969** | TWO-BIT, TRIVIAL, MICKEY MOUSE, RINKY-DINK                        | CORRECT GROUP (SMALL-TIME, Level 0)
   - Group 3: **0.4737** | LOTTERY TICKET, CALAMINE LOTION, BUG BITE, YOUR HEAD              | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN SCRATCH)
   - Group 4: **0.4719** | FLAMINGO, CHERRY BLOSSOM, BARBIE DREAMHOUSE, MERRY-GO-ROUND       | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE PINK)
5. **Partition Score: 0.4779**
   - Group 1: **0.5510** | FLAMINGO, SUNNY-SIDE UP, MERRY-GO-ROUND, GLAD-HAND                | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 2: **0.4969** | TWO-BIT, TRIVIAL, MICKEY MOUSE, RINKY-DINK                        | CORRECT GROUP (SMALL-TIME, Level 0)
   - Group 3: **0.4737** | LOTTERY TICKET, CALAMINE LOTION, BUG BITE, YOUR HEAD              | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN SCRATCH)
   - Group 4: **0.4704** | HAPPY MEAL, VINYL RECORD, CHERRY BLOSSOM, BARBIE DREAMHOUSE       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE PINK)

### Top Candidate Groups:
   - Group 1: **0.5222** | SUNNY-SIDE UP, VINYL RECORD, MERRY-GO-ROUND, GLAD-HAND            | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 2: **0.5071** | HAPPY MEAL, FLAMINGO, CHERRY BLOSSOM, BARBIE DREAMHOUSE           | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE PINK)
   - Group 3: **0.4969** | TWO-BIT, TRIVIAL, MICKEY MOUSE, RINKY-DINK                        | CORRECT GROUP (SMALL-TIME, Level 0)
   - Group 4: **0.4737** | LOTTERY TICKET, CALAMINE LOTION, BUG BITE, YOUR HEAD              | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN SCRATCH)
   - Group 5: **0.5011** | HAPPY MEAL, VINYL RECORD, MERRY-GO-ROUND, GLAD-HAND               | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 6: **0.5006** | FLAMINGO, SUNNY-SIDE UP, CHERRY BLOSSOM, BARBIE DREAMHOUSE        | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE PINK)
   - Group 7: **0.4941** | HAPPY MEAL, FLAMINGO, SUNNY-SIDE UP, BARBIE DREAMHOUSE            | INCORRECT (Max overlap: 2/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 8: **0.4764** | VINYL RECORD, CHERRY BLOSSOM, MERRY-GO-ROUND, GLAD-HAND           | INCORRECT (Max overlap: 2/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 9: **0.5220** | HAPPY MEAL, SUNNY-SIDE UP, VINYL RECORD, GLAD-HAND                | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 10: **0.4719** | FLAMINGO, CHERRY BLOSSOM, BARBIE DREAMHOUSE, MERRY-GO-ROUND       | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE PINK)
   - Group 11: **0.5510** | FLAMINGO, SUNNY-SIDE UP, MERRY-GO-ROUND, GLAD-HAND                | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 12: **0.4704** | HAPPY MEAL, VINYL RECORD, CHERRY BLOSSOM, BARBIE DREAMHOUSE       | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE PINK)
   - Group 13: **0.4971** | HAPPY MEAL, SUNNY-SIDE UP, VINYL RECORD, MERRY-GO-ROUND           | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 14: **0.4668** | FLAMINGO, CHERRY BLOSSOM, BARBIE DREAMHOUSE, GLAD-HAND            | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE PINK)
   - Group 15: **0.5083** | FLAMINGO, CHERRY BLOSSOM, MERRY-GO-ROUND, GLAD-HAND               | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE PINK)
   - Group 16: **0.4666** | HAPPY MEAL, SUNNY-SIDE UP, VINYL RECORD, BARBIE DREAMHOUSE        | INCORRECT (Max overlap: 2/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 17: **0.5311** | HAPPY MEAL, FLAMINGO, MERRY-GO-ROUND, GLAD-HAND                   | INCORRECT (Max overlap: 3/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 18: **0.4664** | SUNNY-SIDE UP, VINYL RECORD, CHERRY BLOSSOM, BARBIE DREAMHOUSE    | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE PINK)
   - Group 19: **0.4807** | SUNNY-SIDE UP, VINYL RECORD, CHERRY BLOSSOM, GLAD-HAND            | INCORRECT (Max overlap: 2/4 with STARTING WITH OPTIMISTIC WORDS)
   - Group 20: **0.4739** | HAPPY MEAL, FLAMINGO, BARBIE DREAMHOUSE, MERRY-GO-ROUND           | INCORRECT (Max overlap: 2/4 with STARTING WITH OPTIMISTIC WORDS)

---

## Puzzle 69 (ID: 740)
**Words on Board:** MUSEUM, BUTTON, TAPE, RECORD, SHOOT, SNAKE, HITMAN, UNDERTAKER, ROCK, SEAL, SCISSORS, THREAD, FILM, POETIC, PAPER, NEEDLE

### Ground Truth Categories:
* **Level 0 (ITEMS IN A SEWING KIT) [Type: SEMANTIC_SET]:** BUTTON, NEEDLE, SCISSORS, THREAD
* **Level 1 (CAPTURE ON VIDEO) [Type: SYNONYM_OR_NEAR]:** FILM, RECORD, SHOOT, TAPE
* **Level 2 (PRO WRESTLING ICONS, WITH “THE”) [Type: NAMED_ENTITY_SET]:** HITMAN, ROCK, SNAKE, UNDERTAKER
* **Level 3 (WAX ___) [Type: FILL_IN_THE_BLANK]:** MUSEUM, PAPER, POETIC, SEAL

### Top Candidate Partitions:
1. **Partition Score: 0.5356**
   - Group 1: **0.8248** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1)
   - Group 2: **0.6781** | BUTTON, ROCK, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 3: **0.5682** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 4: **0.4481** | SNAKE, SEAL, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
2. **Partition Score: 0.5262**
   - Group 1: **0.8248** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1)
   - Group 2: **0.6204** | ROCK, SCISSORS, PAPER, NEEDLE                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 3: **0.5682** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 4: **0.4580** | BUTTON, SNAKE, SEAL, THREAD                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
3. **Partition Score: 0.5097**
   - Group 1: **0.8248** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1)
   - Group 2: **0.6177** | MUSEUM, ROCK, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.5051** | HITMAN, UNDERTAKER, POETIC, NEEDLE                                | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 4: **0.4580** | BUTTON, SNAKE, SEAL, THREAD                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
4. **Partition Score: 0.5082**
   - Group 1: **0.8248** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1)
   - Group 2: **0.5755** | HITMAN, UNDERTAKER, ROCK, POETIC                                  | INCORRECT (Max overlap: 3/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 3: **0.5612** | MUSEUM, BUTTON, SCISSORS, PAPER                                   | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 4: **0.4481** | SNAKE, SEAL, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
5. **Partition Score: 0.5064**
   - Group 1: **0.8248** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1)
   - Group 2: **0.5873** | ROCK, SCISSORS, POETIC, PAPER                                     | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.5222** | MUSEUM, HITMAN, UNDERTAKER, NEEDLE                                | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 4: **0.4580** | BUTTON, SNAKE, SEAL, THREAD                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)

### Top Candidate Groups:
   - Group 1: **0.8248** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1)
   - Group 2: **0.6781** | BUTTON, ROCK, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 3: **0.5682** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 4: **0.4481** | SNAKE, SEAL, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 5: **0.6204** | ROCK, SCISSORS, PAPER, NEEDLE                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 6: **0.4580** | BUTTON, SNAKE, SEAL, THREAD                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 7: **0.6177** | MUSEUM, ROCK, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 8: **0.5051** | HITMAN, UNDERTAKER, POETIC, NEEDLE                                | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 9: **0.5755** | HITMAN, UNDERTAKER, ROCK, POETIC                                  | INCORRECT (Max overlap: 3/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 10: **0.5612** | MUSEUM, BUTTON, SCISSORS, PAPER                                   | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 11: **0.5873** | ROCK, SCISSORS, POETIC, PAPER                                     | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 12: **0.5222** | MUSEUM, HITMAN, UNDERTAKER, NEEDLE                                | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 13: **0.5318** | MUSEUM, SCISSORS, PAPER, NEEDLE                                   | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 14: **0.6003** | HITMAN, UNDERTAKER, ROCK, SCISSORS                                | INCORRECT (Max overlap: 3/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 15: **0.5052** | MUSEUM, POETIC, PAPER, NEEDLE                                     | INCORRECT (Max overlap: 3/4 with WAX ___)
   - Group 16: **0.5962** | MUSEUM, HITMAN, UNDERTAKER, ROCK                                  | INCORRECT (Max overlap: 3/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 17: **0.5278** | BUTTON, SCISSORS, POETIC, PAPER                                   | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 18: **0.5055** | SCISSORS, POETIC, PAPER, NEEDLE                                   | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 19: **0.5127** | MUSEUM, BUTTON, POETIC, PAPER                                     | INCORRECT (Max overlap: 3/4 with WAX ___)
   - Group 20: **0.5618** | MUSEUM, BUTTON, ROCK, PAPER                                       | INCORRECT (Max overlap: 2/4 with WAX ___)

---

## Puzzle 70 (ID: 4)
**Words on Board:** SWEEP, CAROUSEL, BAT, MOP, SPIDER, REEBOK, ADIDAS, DUST, IRON, PUMA, SUPER, CATS, VACUUM, NIKE, CABARET, CHICAGO

### Ground Truth Categories:
* **Level 0 (SNEAKER BRANDS) [Type: NAMED_ENTITY_SET]:** ADIDAS, NIKE, PUMA, REEBOK
* **Level 1 (MUSICALS BEGINNING WITH “C”) [Type: WORD_FORM]:** CABARET, CAROUSEL, CATS, CHICAGO
* **Level 2 (CLEANING VERBS) [Type: SYNONYM_OR_NEAR]:** DUST, MOP, SWEEP, VACUUM
* **Level 3 (___ MAN SUPERHEROES) [Type: FILL_IN_THE_BLANK]:** BAT, IRON, SPIDER, SUPER

### Top Candidate Partitions:
1. **Partition Score: 0.5159**
   - Group 1: **0.7231** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0)
   - Group 2: **0.7005** | SWEEP, MOP, DUST, VACUUM                                          | CORRECT GROUP (CLEANING VERBS, Level 2)
   - Group 3: **0.4868** | BAT, IRON, SUPER, CATS                                            | INCORRECT (Max overlap: 3/4 with ___ MAN SUPERHEROES)
   - Group 4: **0.4381** | CAROUSEL, SPIDER, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
2. **Partition Score: 0.5044**
   - Group 1: **0.7231** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0)
   - Group 2: **0.7005** | SWEEP, MOP, DUST, VACUUM                                          | CORRECT GROUP (CLEANING VERBS, Level 2)
   - Group 3: **0.4889** | BAT, SPIDER, IRON, SUPER                                          | CORRECT GROUP (___ MAN SUPERHEROES, Level 3)
   - Group 4: **0.4141** | CAROUSEL, CATS, CABARET, CHICAGO                                  | CORRECT GROUP (MUSICALS BEGINNING WITH “C”, Level 1)
3. **Partition Score: 0.5024**
   - Group 1: **0.7231** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0)
   - Group 2: **0.6051** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 3: **0.5282** | BAT, MOP, SUPER, CATS                                             | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
   - Group 4: **0.4381** | CAROUSEL, SPIDER, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
4. **Partition Score: 0.4971**
   - Group 1: **0.7231** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0)
   - Group 2: **0.6015** | SWEEP, BAT, DUST, VACUUM                                          | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 3: **0.5108** | MOP, IRON, SUPER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
   - Group 4: **0.4381** | CAROUSEL, SPIDER, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
5. **Partition Score: 0.4914**
   - Group 1: **0.7231** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0)
   - Group 2: **0.6194** | SWEEP, BAT, MOP, DUST                                             | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 3: **0.4701** | IRON, SUPER, CATS, VACUUM                                         | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
   - Group 4: **0.4381** | CAROUSEL, SPIDER, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)

### Top Candidate Groups:
   - Group 1: **0.7231** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0)
   - Group 2: **0.7005** | SWEEP, MOP, DUST, VACUUM                                          | CORRECT GROUP (CLEANING VERBS, Level 2)
   - Group 3: **0.4868** | BAT, IRON, SUPER, CATS                                            | INCORRECT (Max overlap: 3/4 with ___ MAN SUPERHEROES)
   - Group 4: **0.4381** | CAROUSEL, SPIDER, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
   - Group 5: **0.4889** | BAT, SPIDER, IRON, SUPER                                          | CORRECT GROUP (___ MAN SUPERHEROES, Level 3)
   - Group 6: **0.4141** | CAROUSEL, CATS, CABARET, CHICAGO                                  | CORRECT GROUP (MUSICALS BEGINNING WITH “C”, Level 1)
   - Group 7: **0.6051** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 8: **0.5282** | BAT, MOP, SUPER, CATS                                             | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
   - Group 9: **0.6015** | SWEEP, BAT, DUST, VACUUM                                          | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 10: **0.5108** | MOP, IRON, SUPER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
   - Group 11: **0.6194** | SWEEP, BAT, MOP, DUST                                             | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 12: **0.4701** | IRON, SUPER, CATS, VACUUM                                         | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
   - Group 13: **0.5314** | BAT, MOP, SPIDER, SUPER                                           | INCORRECT (Max overlap: 3/4 with ___ MAN SUPERHEROES)
   - Group 14: **0.5756** | SWEEP, BAT, MOP, VACUUM                                           | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 15: **0.4772** | DUST, IRON, SUPER, CATS                                           | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
   - Group 16: **0.4963** | MOP, SPIDER, IRON, SUPER                                          | INCORRECT (Max overlap: 3/4 with ___ MAN SUPERHEROES)
   - Group 17: **0.5482** | DUST, IRON, SUPER, VACUUM                                         | INCORRECT (Max overlap: 2/4 with CLEANING VERBS)
   - Group 18: **0.4937** | SWEEP, BAT, MOP, CATS                                             | INCORRECT (Max overlap: 2/4 with CLEANING VERBS)
   - Group 19: **0.5371** | SWEEP, MOP, IRON, VACUUM                                          | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 20: **0.4937** | BAT, DUST, SUPER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)

---

## Puzzle 71 (ID: 465)
**Words on Board:** DISH, DOPE, SNOOP, PORCH, SCOOP, SIZZLE, DEMO, DROOP, BLOOPER, LAD, STOOP, GOOF, HIGHLIGHT, DECK, YARD, INFO

### Ground Truth Categories:
* **Level 0 (GATHERING SPOT OUTSIDE A RESIDENCE) [Type: SEMANTIC_SET]:** DECK, PORCH, STOOP, YARD
* **Level 1 (LOWDOWN) [Type: SYNONYM_OR_NEAR]:** DISH, DOPE, INFO, SCOOP
* **Level 2 (KINDS OF REELS) [Type: SEMANTIC_SET]:** BLOOPER, DEMO, HIGHLIGHT, SIZZLE
* **Level 3 (CARTOON DOGS MINUS “Y”) [Type: WORDPLAY_TRANSFORM]:** DROOP, GOOF, LAD, SNOOP

### Top Candidate Partitions:
1. **Partition Score: 0.5133**
   - Group 1: **0.5924** | PORCH, STOOP, DECK, YARD                                          | CORRECT GROUP (GATHERING SPOT OUTSIDE A RESIDENCE, Level 0)
   - Group 2: **0.5428** | DISH, SNOOP, SCOOP, SIZZLE                                        | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 3: **0.5295** | DOPE, DEMO, HIGHLIGHT, INFO                                       | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 4: **0.4904** | DROOP, BLOOPER, LAD, GOOF                                         | INCORRECT (Max overlap: 3/4 with CARTOON DOGS MINUS “Y”)
2. **Partition Score: 0.5028**
   - Group 1: **0.5924** | PORCH, STOOP, DECK, YARD                                          | CORRECT GROUP (GATHERING SPOT OUTSIDE A RESIDENCE, Level 0)
   - Group 2: **0.5456** | DISH, DOPE, DEMO, INFO                                            | INCORRECT (Max overlap: 3/4 with LOWDOWN)
   - Group 3: **0.4904** | DROOP, BLOOPER, LAD, GOOF                                         | INCORRECT (Max overlap: 3/4 with CARTOON DOGS MINUS “Y”)
   - Group 4: **0.4876** | SNOOP, SCOOP, SIZZLE, HIGHLIGHT                                   | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
3. **Partition Score: 0.5019**
   - Group 1: **0.5498** | DROOP, BLOOPER, STOOP, GOOF                                       | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)
   - Group 2: **0.5428** | DISH, SNOOP, SCOOP, SIZZLE                                        | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 3: **0.5295** | DOPE, DEMO, HIGHLIGHT, INFO                                       | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 4: **0.4676** | PORCH, LAD, DECK, YARD                                            | INCORRECT (Max overlap: 3/4 with GATHERING SPOT OUTSIDE A RESIDENCE)
4. **Partition Score: 0.5010**
   - Group 1: **0.5924** | PORCH, STOOP, DECK, YARD                                          | CORRECT GROUP (GATHERING SPOT OUTSIDE A RESIDENCE, Level 0)
   - Group 2: **0.5473** | DISH, SNOOP, SCOOP, INFO                                          | INCORRECT (Max overlap: 3/4 with LOWDOWN)
   - Group 3: **0.4904** | DROOP, BLOOPER, LAD, GOOF                                         | INCORRECT (Max overlap: 3/4 with CARTOON DOGS MINUS “Y”)
   - Group 4: **0.4831** | DOPE, SIZZLE, DEMO, HIGHLIGHT                                     | INCORRECT (Max overlap: 3/4 with KINDS OF REELS)
5. **Partition Score: 0.4994**
   - Group 1: **0.5924** | PORCH, STOOP, DECK, YARD                                          | CORRECT GROUP (GATHERING SPOT OUTSIDE A RESIDENCE, Level 0)
   - Group 2: **0.5571** | DISH, DOPE, SNOOP, SIZZLE                                         | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 3: **0.4904** | DROOP, BLOOPER, LAD, GOOF                                         | INCORRECT (Max overlap: 3/4 with CARTOON DOGS MINUS “Y”)
   - Group 4: **0.4750** | SCOOP, DEMO, HIGHLIGHT, INFO                                      | INCORRECT (Max overlap: 2/4 with LOWDOWN)

### Top Candidate Groups:
   - Group 1: **0.5924** | PORCH, STOOP, DECK, YARD                                          | CORRECT GROUP (GATHERING SPOT OUTSIDE A RESIDENCE, Level 0)
   - Group 2: **0.5428** | DISH, SNOOP, SCOOP, SIZZLE                                        | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 3: **0.5295** | DOPE, DEMO, HIGHLIGHT, INFO                                       | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 4: **0.4904** | DROOP, BLOOPER, LAD, GOOF                                         | INCORRECT (Max overlap: 3/4 with CARTOON DOGS MINUS “Y”)
   - Group 5: **0.5456** | DISH, DOPE, DEMO, INFO                                            | INCORRECT (Max overlap: 3/4 with LOWDOWN)
   - Group 6: **0.4876** | SNOOP, SCOOP, SIZZLE, HIGHLIGHT                                   | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 7: **0.5498** | DROOP, BLOOPER, STOOP, GOOF                                       | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)
   - Group 8: **0.4676** | PORCH, LAD, DECK, YARD                                            | INCORRECT (Max overlap: 3/4 with GATHERING SPOT OUTSIDE A RESIDENCE)
   - Group 9: **0.5473** | DISH, SNOOP, SCOOP, INFO                                          | INCORRECT (Max overlap: 3/4 with LOWDOWN)
   - Group 10: **0.4831** | DOPE, SIZZLE, DEMO, HIGHLIGHT                                     | INCORRECT (Max overlap: 3/4 with KINDS OF REELS)
   - Group 11: **0.5571** | DISH, DOPE, SNOOP, SIZZLE                                         | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 12: **0.4750** | SCOOP, DEMO, HIGHLIGHT, INFO                                      | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 13: **0.5084** | DOPE, SNOOP, SIZZLE, HIGHLIGHT                                    | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 14: **0.5010** | DISH, SCOOP, DEMO, INFO                                           | INCORRECT (Max overlap: 3/4 with LOWDOWN)
   - Group 15: **0.5086** | SNOOP, DEMO, HIGHLIGHT, INFO                                      | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 16: **0.5006** | DISH, DOPE, SCOOP, SIZZLE                                         | INCORRECT (Max overlap: 3/4 with LOWDOWN)
   - Group 17: **0.5307** | DISH, DOPE, SCOOP, INFO                                           | CORRECT GROUP (LOWDOWN, Level 1)
   - Group 18: **0.4830** | SNOOP, SIZZLE, DEMO, HIGHLIGHT                                    | INCORRECT (Max overlap: 3/4 with KINDS OF REELS)
   - Group 19: **0.5232** | PORCH, DROOP, DECK, YARD                                          | INCORRECT (Max overlap: 3/4 with GATHERING SPOT OUTSIDE A RESIDENCE)
   - Group 20: **0.4624** | BLOOPER, LAD, STOOP, GOOF                                         | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)

---

## Puzzle 72 (ID: 1057)
**Words on Board:** THE PENTAGON, FILM NERD, MAKING OUT, LEFT FIELD, THE BLUE, NECKING, FIRST BASE, HOME PLATE, MEMENTO, NOWHERE, THIN AIR, TONSIL HOCKEY, BURGER KING WHOPPER, PITCHER'S MOUND, SCHOOL CROSSING SIGN, JEANS BACK POCKET

### Ground Truth Categories:
* **Level 0 (CANOODLING) [Type: SYNONYM_OR_NEAR]:** FIRST BASE, MAKING OUT, NECKING, TONSIL HOCKEY
* **Level 1 (FIVE-SIDED THINGS) [Type: SEMANTIC_SET]:** HOME PLATE, JEANS BACK POCKET, SCHOOL CROSSING SIGN, THE PENTAGON
* **Level 2 (UNEXPECTED PLACES TO BE "OUT OF") [Type: FILL_IN_THE_BLANK]:** LEFT FIELD, NOWHERE, THE BLUE, THIN AIR
* **Level 3 (ENDING IN CANDY BRANDS MINUS "S") [Type: WORDPLAY_TRANSFORM]:** BURGER KING WHOPPER, FILM NERD, MEMENTO, PITCHER'S MOUND

### Top Candidate Partitions:
1. **Partition Score: 0.5143**
   - Group 1: **0.5427** | MAKING OUT, NECKING, TONSIL HOCKEY, PITCHER'S MOUND               | INCORRECT (Max overlap: 3/4 with CANOODLING)
   - Group 2: **0.5366** | THE PENTAGON, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 3/4 with FIVE-SIDED THINGS)
   - Group 3: **0.5234** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 4: **0.4985** | FILM NERD, LEFT FIELD, FIRST BASE, HOME PLATE                     | INCORRECT (Max overlap: 1/4 with ENDING IN CANDY BRANDS MINUS "S")
2. **Partition Score: 0.5102**
   - Group 1: **0.6739** | THE PENTAGON, LEFT FIELD, FIRST BASE, HOME PLATE                  | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 2: **0.5427** | MAKING OUT, NECKING, TONSIL HOCKEY, PITCHER'S MOUND               | INCORRECT (Max overlap: 3/4 with CANOODLING)
   - Group 3: **0.5291** | FILM NERD, MEMENTO, NOWHERE, THIN AIR                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 4: **0.4845** | THE BLUE, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
3. **Partition Score: 0.5098**
   - Group 1: **0.6715** | THE PENTAGON, FIRST BASE, HOME PLATE, PITCHER'S MOUND             | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 2: **0.5408** | MAKING OUT, LEFT FIELD, NECKING, TONSIL HOCKEY                    | INCORRECT (Max overlap: 3/4 with CANOODLING)
   - Group 3: **0.5291** | FILM NERD, MEMENTO, NOWHERE, THIN AIR                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 4: **0.4845** | THE BLUE, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
4. **Partition Score: 0.5082**
   - Group 1: **0.6426** | THE PENTAGON, LEFT FIELD, HOME PLATE, PITCHER'S MOUND             | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 2: **0.5347** | MAKING OUT, NECKING, FIRST BASE, TONSIL HOCKEY                    | CORRECT GROUP (CANOODLING, Level 0)
   - Group 3: **0.5291** | FILM NERD, MEMENTO, NOWHERE, THIN AIR                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 4: **0.4845** | THE BLUE, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
5. **Partition Score: 0.5063**
   - Group 1: **0.5427** | MAKING OUT, NECKING, TONSIL HOCKEY, PITCHER'S MOUND               | INCORRECT (Max overlap: 3/4 with CANOODLING)
   - Group 2: **0.5378** | LEFT FIELD, FIRST BASE, HOME PLATE, JEANS BACK POCKET             | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 3: **0.5291** | FILM NERD, MEMENTO, NOWHERE, THIN AIR                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 4: **0.4791** | THE PENTAGON, THE BLUE, BURGER KING WHOPPER, SCHOOL CROSSING SIGN | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)

### Top Candidate Groups:
   - Group 1: **0.5427** | MAKING OUT, NECKING, TONSIL HOCKEY, PITCHER'S MOUND               | INCORRECT (Max overlap: 3/4 with CANOODLING)
   - Group 2: **0.5366** | THE PENTAGON, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 3/4 with FIVE-SIDED THINGS)
   - Group 3: **0.5234** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 4: **0.4985** | FILM NERD, LEFT FIELD, FIRST BASE, HOME PLATE                     | INCORRECT (Max overlap: 1/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 5: **0.6739** | THE PENTAGON, LEFT FIELD, FIRST BASE, HOME PLATE                  | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 6: **0.5291** | FILM NERD, MEMENTO, NOWHERE, THIN AIR                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 7: **0.4845** | THE BLUE, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 8: **0.6715** | THE PENTAGON, FIRST BASE, HOME PLATE, PITCHER'S MOUND             | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 9: **0.5408** | MAKING OUT, LEFT FIELD, NECKING, TONSIL HOCKEY                    | INCORRECT (Max overlap: 3/4 with CANOODLING)
   - Group 10: **0.6426** | THE PENTAGON, LEFT FIELD, HOME PLATE, PITCHER'S MOUND             | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 11: **0.5347** | MAKING OUT, NECKING, FIRST BASE, TONSIL HOCKEY                    | CORRECT GROUP (CANOODLING, Level 0)
   - Group 12: **0.5378** | LEFT FIELD, FIRST BASE, HOME PLATE, JEANS BACK POCKET             | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 13: **0.4791** | THE PENTAGON, THE BLUE, BURGER KING WHOPPER, SCHOOL CROSSING SIGN | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 14: **0.5738** | LEFT FIELD, FIRST BASE, HOME PLATE, THIN AIR                      | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 15: **0.4711** | FILM NERD, THE BLUE, MEMENTO, NOWHERE                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 16: **0.4779** | LEFT FIELD, THE BLUE, FIRST BASE, HOME PLATE                      | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 17: **0.4762** | THE PENTAGON, FILM NERD, BURGER KING WHOPPER, SCHOOL CROSSING SIGN | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 18: **0.6054** | LEFT FIELD, FIRST BASE, HOME PLATE, NOWHERE                       | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 19: **0.4668** | FILM NERD, THE BLUE, MEMENTO, THIN AIR                            | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 20: **0.4728** | FILM NERD, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")

---

## Puzzle 73 (ID: 446)
**Words on Board:** ROW, DIAMOND, DIVE, GLITTER, BOX, TEMPLE, FENCE, CUBE, GOLD, SEQUIN, LIGHTHOUSE, MACHINE, PYRAMID, GARDENS, CREAM, STORM

### Ground Truth Categories:
* **Level 0 (SPARKLING THINGS) [Type: SEMANTIC_SET]:** DIAMOND, GLITTER, GOLD, SEQUIN
* **Level 1 (PARTICIPATE IN SUMMER OLYMPIC EVENTS) [Type: SEMANTIC_SET]:** BOX, DIVE, FENCE, ROW
* **Level 2 (WONDERS OF THE WORLD) [Type: NAMED_ENTITY_SET]:** GARDENS, LIGHTHOUSE, PYRAMID, TEMPLE
* **Level 3 (ICE ___) [Type: FILL_IN_THE_BLANK]:** CREAM, CUBE, MACHINE, STORM

### Top Candidate Partitions:
1. **Partition Score: 0.5300**
   - Group 1: **0.5997** | TEMPLE, LIGHTHOUSE, PYRAMID, GARDENS                              | CORRECT GROUP (WONDERS OF THE WORLD, Level 2)
   - Group 2: **0.5500** | DIAMOND, DIVE, GLITTER, GOLD                                      | INCORRECT (Max overlap: 3/4 with SPARKLING THINGS)
   - Group 3: **0.5389** | ROW, BOX, CUBE, MACHINE                                           | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 4: **0.5155** | FENCE, SEQUIN, CREAM, STORM                                       | INCORRECT (Max overlap: 2/4 with ICE ___)
2. **Partition Score: 0.5282**
   - Group 1: **0.5388** | GLITTER, TEMPLE, LIGHTHOUSE, GARDENS                              | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 2: **0.5344** | FENCE, SEQUIN, PYRAMID, STORM                                     | INCORRECT (Max overlap: 1/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 3: **0.5342** | DIAMOND, DIVE, BOX, GOLD                                          | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 4: **0.5222** | ROW, CUBE, MACHINE, CREAM                                         | INCORRECT (Max overlap: 3/4 with ICE ___)
3. **Partition Score: 0.5266**
   - Group 1: **0.5343** | GLITTER, SEQUIN, PYRAMID, STORM                                   | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 2: **0.5342** | DIAMOND, DIVE, BOX, GOLD                                          | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 3: **0.5277** | TEMPLE, FENCE, LIGHTHOUSE, GARDENS                                | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 4: **0.5222** | ROW, CUBE, MACHINE, CREAM                                         | INCORRECT (Max overlap: 3/4 with ICE ___)
4. **Partition Score: 0.5260**
   - Group 1: **0.5997** | TEMPLE, LIGHTHOUSE, PYRAMID, GARDENS                              | CORRECT GROUP (WONDERS OF THE WORLD, Level 2)
   - Group 2: **0.5567** | DIAMOND, GLITTER, SEQUIN, STORM                                   | INCORRECT (Max overlap: 3/4 with SPARKLING THINGS)
   - Group 3: **0.5222** | ROW, CUBE, MACHINE, CREAM                                         | INCORRECT (Max overlap: 3/4 with ICE ___)
   - Group 4: **0.5125** | DIVE, BOX, FENCE, GOLD                                            | INCORRECT (Max overlap: 3/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
5. **Partition Score: 0.5249**
   - Group 1: **0.5997** | TEMPLE, LIGHTHOUSE, PYRAMID, GARDENS                              | CORRECT GROUP (WONDERS OF THE WORLD, Level 2)
   - Group 2: **0.5529** | DIAMOND, GLITTER, CREAM, STORM                                    | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 3: **0.5217** | ROW, CUBE, SEQUIN, MACHINE                                        | INCORRECT (Max overlap: 2/4 with ICE ___)
   - Group 4: **0.5125** | DIVE, BOX, FENCE, GOLD                                            | INCORRECT (Max overlap: 3/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)

### Top Candidate Groups:
   - Group 1: **0.5997** | TEMPLE, LIGHTHOUSE, PYRAMID, GARDENS                              | CORRECT GROUP (WONDERS OF THE WORLD, Level 2)
   - Group 2: **0.5500** | DIAMOND, DIVE, GLITTER, GOLD                                      | INCORRECT (Max overlap: 3/4 with SPARKLING THINGS)
   - Group 3: **0.5389** | ROW, BOX, CUBE, MACHINE                                           | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 4: **0.5155** | FENCE, SEQUIN, CREAM, STORM                                       | INCORRECT (Max overlap: 2/4 with ICE ___)
   - Group 5: **0.5388** | GLITTER, TEMPLE, LIGHTHOUSE, GARDENS                              | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 6: **0.5344** | FENCE, SEQUIN, PYRAMID, STORM                                     | INCORRECT (Max overlap: 1/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 7: **0.5342** | DIAMOND, DIVE, BOX, GOLD                                          | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 8: **0.5222** | ROW, CUBE, MACHINE, CREAM                                         | INCORRECT (Max overlap: 3/4 with ICE ___)
   - Group 9: **0.5343** | GLITTER, SEQUIN, PYRAMID, STORM                                   | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 10: **0.5277** | TEMPLE, FENCE, LIGHTHOUSE, GARDENS                                | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 11: **0.5567** | DIAMOND, GLITTER, SEQUIN, STORM                                   | INCORRECT (Max overlap: 3/4 with SPARKLING THINGS)
   - Group 12: **0.5125** | DIVE, BOX, FENCE, GOLD                                            | INCORRECT (Max overlap: 3/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 13: **0.5529** | DIAMOND, GLITTER, CREAM, STORM                                    | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 14: **0.5217** | ROW, CUBE, SEQUIN, MACHINE                                        | INCORRECT (Max overlap: 2/4 with ICE ___)
   - Group 15: **0.5300** | TEMPLE, FENCE, PYRAMID, GARDENS                                   | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 16: **0.5239** | GLITTER, SEQUIN, LIGHTHOUSE, STORM                                | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 17: **0.5369** | GLITTER, TEMPLE, PYRAMID, GARDENS                                 | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 18: **0.5203** | FENCE, SEQUIN, LIGHTHOUSE, STORM                                  | INCORRECT (Max overlap: 1/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 19: **0.5380** | DIAMOND, SEQUIN, PYRAMID, STORM                                   | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 20: **0.5369** | DIAMOND, SEQUIN, PYRAMID, GARDENS                                 | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)

---

## Puzzle 74 (ID: 301)
**Words on Board:** PEANUTS, PIGPEN, SOLID, DUMP, SOUND, PRIZE, DARK, MESS, FIRM, STY, CRAZY, CARAMEL, STABLE, GIFT, POPCORN, CHARLEY

### Ground Truth Categories:
* **Level 0 (DISORDERLY PLACE) [Type: SYNONYM_OR_NEAR]:** DUMP, MESS, PIGPEN, STY
* **Level 1 (STURDY) [Type: SYNONYM_OR_NEAR]:** FIRM, SOLID, SOUND, STABLE
* **Level 2 (FOUND IN CRACKER JACKS) [Type: NAMED_ENTITY_SET]:** CARAMEL, PEANUTS, POPCORN, PRIZE
* **Level 3 (___ HORSE) [Type: FILL_IN_THE_BLANK]:** CHARLEY, CRAZY, DARK, GIFT

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6289** | PEANUTS, DARK, CRAZY, CARAMEL                                     | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)
   - Group 2: **0.6281** | SOUND, DARK, CRAZY, CARAMEL                                       | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 3: **0.6189** | PEANUTS, CRAZY, CARAMEL, POPCORN                                  | INCORRECT (Max overlap: 3/4 with FOUND IN CRACKER JACKS)
   - Group 4: **0.6167** | DARK, MESS, CRAZY, CARAMEL                                        | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 5: **0.6145** | SOUND, DARK, MESS, CRAZY                                          | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 6: **0.6133** | DUMP, SOUND, MESS, CRAZY                                          | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
   - Group 7: **0.6113** | DARK, CRAZY, CARAMEL, POPCORN                                     | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 8: **0.5952** | PEANUTS, DARK, CARAMEL, POPCORN                                   | INCORRECT (Max overlap: 3/4 with FOUND IN CRACKER JACKS)
   - Group 9: **0.5938** | SOUND, DARK, CRAZY, STABLE                                        | INCORRECT (Max overlap: 2/4 with STURDY)
   - Group 10: **0.5928** | PEANUTS, CRAZY, CARAMEL, CHARLEY                                  | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)
   - Group 11: **0.5882** | DUMP, SOUND, CRAZY, STABLE                                        | INCORRECT (Max overlap: 2/4 with STURDY)
   - Group 12: **0.5880** | DUMP, SOUND, DARK, CRAZY                                          | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 13: **0.5839** | MESS, CRAZY, CARAMEL, POPCORN                                     | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)
   - Group 14: **0.5805** | DARK, CRAZY, CARAMEL, CHARLEY                                     | INCORRECT (Max overlap: 3/4 with ___ HORSE)
   - Group 15: **0.5804** | CRAZY, CARAMEL, POPCORN, CHARLEY                                  | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 16: **0.5788** | SOUND, MESS, CRAZY, CARAMEL                                       | INCORRECT (Max overlap: 1/4 with STURDY)
   - Group 17: **0.5782** | PEANUTS, CARAMEL, POPCORN, CHARLEY                                | INCORRECT (Max overlap: 3/4 with FOUND IN CRACKER JACKS)
   - Group 18: **0.5770** | DARK, CRAZY, CARAMEL, STABLE                                      | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 19: **0.5762** | SOUND, DARK, CRAZY, POPCORN                                       | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 20: **0.5754** | SOUND, CRAZY, CARAMEL, POPCORN                                    | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)

---

## Puzzle 75 (ID: 1028)
**Words on Board:** MONKEY, FELLOW, CONTACT, UNEVEN, ASSOCIATE, COLLEAGUE, SPECTACLE, GOGGLE, LOOK, STYLE, PEER, DESIGN, PULL-UP, SCHEME, PARALLEL, SHADE

### Ground Truth Categories:
* **Level 0 (COHORT MEMBER) [Type: SYNONYM_OR_NEAR]:** ASSOCIATE, COLLEAGUE, FELLOW, PEER
* **Level 1 (AESTHETIC) [Type: SYNONYM_OR_NEAR]:** DESIGN, LOOK, SCHEME, STYLE
* **Level 2 (KINDS OF BAR APPARATUSES) [Type: NAMED_ENTITY_SET]:** MONKEY, PARALLEL, PULL-UP, UNEVEN
* **Level 3 (EYEWEAR IN THE SINGULAR) [Type: WORDPLAY_TRANSFORM]:** CONTACT, GOGGLE, SHADE, SPECTACLE

### Top Candidate Partitions:
1. **Partition Score: 0.4917**
   - Group 1: **0.6246** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER)
   - Group 2: **0.5653** | CONTACT, SPECTACLE, GOGGLE, PULL-UP                               | INCORRECT (Max overlap: 3/4 with EYEWEAR IN THE SINGULAR)
   - Group 3: **0.5259** | MONKEY, UNEVEN, STYLE, SHADE                                      | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 4: **0.4378** | LOOK, PEER, DESIGN, PARALLEL                                      | INCORRECT (Max overlap: 2/4 with AESTHETIC)
2. **Partition Score: 0.4841**
   - Group 1: **0.6246** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER)
   - Group 2: **0.5653** | CONTACT, SPECTACLE, GOGGLE, PULL-UP                               | INCORRECT (Max overlap: 3/4 with EYEWEAR IN THE SINGULAR)
   - Group 3: **0.5268** | MONKEY, UNEVEN, PARALLEL, SHADE                                   | INCORRECT (Max overlap: 3/4 with KINDS OF BAR APPARATUSES)
   - Group 4: **0.4223** | LOOK, STYLE, PEER, DESIGN                                         | INCORRECT (Max overlap: 3/4 with AESTHETIC)
3. **Partition Score: 0.4817**
   - Group 1: **0.6246** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER)
   - Group 2: **0.5283** | MONKEY, SPECTACLE, GOGGLE, PULL-UP                                | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 3: **0.5229** | CONTACT, UNEVEN, STYLE, SHADE                                     | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 4: **0.4378** | LOOK, PEER, DESIGN, PARALLEL                                      | INCORRECT (Max overlap: 2/4 with AESTHETIC)
4. **Partition Score: 0.4805**
   - Group 1: **0.8455** | FELLOW, ASSOCIATE, COLLEAGUE, PEER                                | CORRECT GROUP (COHORT MEMBER, Level 0)
   - Group 2: **0.5653** | CONTACT, SPECTACLE, GOGGLE, PULL-UP                               | INCORRECT (Max overlap: 3/4 with EYEWEAR IN THE SINGULAR)
   - Group 3: **0.4875** | MONKEY, UNEVEN, LOOK, SHADE                                       | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 4: **0.4346** | STYLE, DESIGN, SCHEME, PARALLEL                                   | INCORRECT (Max overlap: 3/4 with AESTHETIC)
5. **Partition Score: 0.4787**
   - Group 1: **0.6246** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER)
   - Group 2: **0.5354** | MONKEY, CONTACT, GOGGLE, PULL-UP                                  | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 3: **0.5038** | UNEVEN, SPECTACLE, STYLE, SHADE                                   | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 4: **0.4378** | LOOK, PEER, DESIGN, PARALLEL                                      | INCORRECT (Max overlap: 2/4 with AESTHETIC)

### Top Candidate Groups:
   - Group 1: **0.6246** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER)
   - Group 2: **0.5653** | CONTACT, SPECTACLE, GOGGLE, PULL-UP                               | INCORRECT (Max overlap: 3/4 with EYEWEAR IN THE SINGULAR)
   - Group 3: **0.5259** | MONKEY, UNEVEN, STYLE, SHADE                                      | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 4: **0.4378** | LOOK, PEER, DESIGN, PARALLEL                                      | INCORRECT (Max overlap: 2/4 with AESTHETIC)
   - Group 5: **0.5268** | MONKEY, UNEVEN, PARALLEL, SHADE                                   | INCORRECT (Max overlap: 3/4 with KINDS OF BAR APPARATUSES)
   - Group 6: **0.4223** | LOOK, STYLE, PEER, DESIGN                                         | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 7: **0.5283** | MONKEY, SPECTACLE, GOGGLE, PULL-UP                                | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 8: **0.5229** | CONTACT, UNEVEN, STYLE, SHADE                                     | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 9: **0.8455** | FELLOW, ASSOCIATE, COLLEAGUE, PEER                                | CORRECT GROUP (COHORT MEMBER, Level 0)
   - Group 10: **0.4875** | MONKEY, UNEVEN, LOOK, SHADE                                       | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 11: **0.4346** | STYLE, DESIGN, SCHEME, PARALLEL                                   | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 12: **0.5354** | MONKEY, CONTACT, GOGGLE, PULL-UP                                  | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 13: **0.5038** | UNEVEN, SPECTACLE, STYLE, SHADE                                   | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 14: **0.4045** | LOOK, STYLE, DESIGN, SCHEME                                       | CORRECT GROUP (AESTHETIC, Level 1)
   - Group 15: **0.5030** | CONTACT, UNEVEN, LOOK, SHADE                                      | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 16: **0.5469** | MONKEY, CONTACT, UNEVEN, STYLE                                    | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 17: **0.4695** | SPECTACLE, GOGGLE, PULL-UP, SHADE                                 | INCORRECT (Max overlap: 3/4 with EYEWEAR IN THE SINGULAR)
   - Group 18: **0.5178** | MONKEY, LOOK, PARALLEL, SHADE                                     | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 19: **0.3967** | UNEVEN, STYLE, DESIGN, SCHEME                                     | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 20: **0.4853** | FELLOW, COLLEAGUE, PEER, PARALLEL                                 | INCORRECT (Max overlap: 3/4 with COHORT MEMBER)

---

## Puzzle 76 (ID: 349)
**Words on Board:** SIGN, ENDORSE, BILLBOARD, BANNER, INITIAL, PREMIER, POSTER, USE, HERE, CHAMPION, WEE, SUPPORT, FIRST, MAIDEN, BACK, THEME

### Ground Truth Categories:
* **Level 0 (ADVERTISING FORMAT) [Type: SEMANTIC_SET]:** BANNER, BILLBOARD, POSTER, SIGN
* **Level 1 (INAUGURAL) [Type: SYNONYM_OR_NEAR]:** FIRST, INITIAL, MAIDEN, PREMIER
* **Level 2 (ADVOCATE FOR) [Type: SYNONYM_OR_NEAR]:** BACK, CHAMPION, ENDORSE, SUPPORT
* **Level 3 (PRONOUN PLUS “E”) [Type: WORDPLAY_TRANSFORM]:** HERE, THEME, USE, WEE

### Top Candidate Partitions:
1. **Partition Score: 0.5405**
   - Group 1: **0.5802** | BILLBOARD, BANNER, POSTER, THEME                                  | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT)
   - Group 2: **0.5476** | INITIAL, USE, HERE, FIRST                                         | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 3: **0.5434** | PREMIER, CHAMPION, WEE, MAIDEN                                    | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 4: **0.5355** | SIGN, ENDORSE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR)
2. **Partition Score: 0.5362**
   - Group 1: **0.5601** | BILLBOARD, BANNER, WEE, MAIDEN                                    | INCORRECT (Max overlap: 2/4 with ADVERTISING FORMAT)
   - Group 2: **0.5476** | INITIAL, USE, HERE, FIRST                                         | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 3: **0.5355** | SIGN, ENDORSE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR)
   - Group 4: **0.5309** | PREMIER, POSTER, CHAMPION, THEME                                  | INCORRECT (Max overlap: 1/4 with INAUGURAL)
3. **Partition Score: 0.5329**
   - Group 1: **0.5802** | BILLBOARD, BANNER, POSTER, THEME                                  | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT)
   - Group 2: **0.5801** | HERE, CHAMPION, WEE, MAIDEN                                       | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 3: **0.5355** | SIGN, ENDORSE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR)
   - Group 4: **0.5079** | INITIAL, PREMIER, USE, FIRST                                      | INCORRECT (Max overlap: 3/4 with INAUGURAL)
4. **Partition Score: 0.5310**
   - Group 1: **0.5734** | BILLBOARD, BANNER, POSTER, WEE                                    | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT)
   - Group 2: **0.5476** | INITIAL, USE, HERE, FIRST                                         | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 3: **0.5355** | SIGN, ENDORSE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR)
   - Group 4: **0.5205** | PREMIER, CHAMPION, MAIDEN, THEME                                  | INCORRECT (Max overlap: 2/4 with INAUGURAL)
5. **Partition Score: 0.5291**
   - Group 1: **0.5476** | INITIAL, USE, HERE, FIRST                                         | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 2: **0.5355** | SIGN, ENDORSE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR)
   - Group 3: **0.5312** | BILLBOARD, PREMIER, POSTER, CHAMPION                              | INCORRECT (Max overlap: 2/4 with ADVERTISING FORMAT)
   - Group 4: **0.5248** | BANNER, WEE, MAIDEN, THEME                                        | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)

### Top Candidate Groups:
   - Group 1: **0.5802** | BILLBOARD, BANNER, POSTER, THEME                                  | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT)
   - Group 2: **0.5476** | INITIAL, USE, HERE, FIRST                                         | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 3: **0.5434** | PREMIER, CHAMPION, WEE, MAIDEN                                    | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 4: **0.5355** | SIGN, ENDORSE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR)
   - Group 5: **0.5601** | BILLBOARD, BANNER, WEE, MAIDEN                                    | INCORRECT (Max overlap: 2/4 with ADVERTISING FORMAT)
   - Group 6: **0.5309** | PREMIER, POSTER, CHAMPION, THEME                                  | INCORRECT (Max overlap: 1/4 with INAUGURAL)
   - Group 7: **0.5801** | HERE, CHAMPION, WEE, MAIDEN                                       | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 8: **0.5079** | INITIAL, PREMIER, USE, FIRST                                      | INCORRECT (Max overlap: 3/4 with INAUGURAL)
   - Group 9: **0.5734** | BILLBOARD, BANNER, POSTER, WEE                                    | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT)
   - Group 10: **0.5205** | PREMIER, CHAMPION, MAIDEN, THEME                                  | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 11: **0.5312** | BILLBOARD, PREMIER, POSTER, CHAMPION                              | INCORRECT (Max overlap: 2/4 with ADVERTISING FORMAT)
   - Group 12: **0.5248** | BANNER, WEE, MAIDEN, THEME                                        | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 13: **0.5841** | CHAMPION, WEE, FIRST, MAIDEN                                      | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 14: **0.5000** | INITIAL, PREMIER, USE, HERE                                       | INCORRECT (Max overlap: 2/4 with INAUGURAL)
   - Group 15: **0.5403** | USE, HERE, CHAMPION, THEME                                        | INCORRECT (Max overlap: 3/4 with PRONOUN PLUS “E”)
   - Group 16: **0.5180** | INITIAL, PREMIER, FIRST, MAIDEN                                   | CORRECT GROUP (INAUGURAL, Level 1)
   - Group 17: **0.5722** | POSTER, HERE, CHAMPION, THEME                                     | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 18: **0.5366** | POSTER, CHAMPION, WEE, MAIDEN                                     | INCORRECT (Max overlap: 1/4 with ADVERTISING FORMAT)
   - Group 19: **0.5179** | BILLBOARD, BANNER, PREMIER, THEME                                 | INCORRECT (Max overlap: 2/4 with ADVERTISING FORMAT)
   - Group 20: **0.6068** | BANNER, PREMIER, CHAMPION, THEME                                  | INCORRECT (Max overlap: 1/4 with ADVERTISING FORMAT)

---

## Puzzle 77 (ID: 657)
**Words on Board:** CARGO, CRYSTAL, LINEN, MAN, COMMANDO, SILVER, CANAL, CHINA, BOXER, PLAN, WITNESS, CLUE, BIKE, BERMUDA, BRAZIL, PANAMA

### Ground Truth Categories:
* **Level 0 (MATERIALS ASSOCIATED WITH FANCY DINING) [Type: SEMANTIC_SET]:** CHINA, CRYSTAL, LINEN, SILVER
* **Level 1 (KINDS OF SHORTS) [Type: SEMANTIC_SET]:** BERMUDA, BIKE, BOXER, CARGO
* **Level 2 (NOUNS IN A FAMOUS PALINDROME) [Type: WORDPLAY_TRANSFORM]:** CANAL, MAN, PANAMA, PLAN
* **Level 3 (MOVIES FROM 1985) [Type: NAMED_ENTITY_SET]:** BRAZIL, CLUE, COMMANDO, WITNESS

### Top Candidate Partitions:
1. **Partition Score: 0.4951**
   - Group 1: **0.5818** | MAN, COMMANDO, BOXER, WITNESS                                     | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 2: **0.5301** | CANAL, PLAN, CLUE, PANAMA                                         | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 3: **0.4903** | CARGO, CHINA, BERMUDA, BRAZIL                                     | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 4: **0.4801** | CRYSTAL, LINEN, SILVER, BIKE                                      | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
2. **Partition Score: 0.4933**
   - Group 1: **0.5818** | MAN, COMMANDO, BOXER, WITNESS                                     | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 2: **0.5301** | CANAL, PLAN, CLUE, PANAMA                                         | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 3: **0.4874** | CARGO, LINEN, SILVER, BIKE                                        | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 4: **0.4778** | CRYSTAL, CHINA, BERMUDA, BRAZIL                                   | INCORRECT (Max overlap: 2/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
3. **Partition Score: 0.4922**
   - Group 1: **0.5301** | CANAL, PLAN, CLUE, PANAMA                                         | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 2: **0.5127** | CARGO, LINEN, BOXER, BIKE                                         | INCORRECT (Max overlap: 3/4 with KINDS OF SHORTS)
   - Group 3: **0.5007** | MAN, COMMANDO, SILVER, WITNESS                                    | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 4: **0.4778** | CRYSTAL, CHINA, BERMUDA, BRAZIL                                   | INCORRECT (Max overlap: 2/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
4. **Partition Score: 0.4879**
   - Group 1: **0.5341** | CARGO, LINEN, COMMANDO, BIKE                                      | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 2: **0.5301** | CANAL, PLAN, CLUE, PANAMA                                         | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 3: **0.4778** | CRYSTAL, CHINA, BERMUDA, BRAZIL                                   | INCORRECT (Max overlap: 2/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 4: **0.4720** | MAN, SILVER, BOXER, WITNESS                                       | INCORRECT (Max overlap: 1/4 with NOUNS IN A FAMOUS PALINDROME)
5. **Partition Score: 0.4833**
   - Group 1: **0.5301** | CANAL, PLAN, CLUE, PANAMA                                         | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 2: **0.5148** | CHINA, BOXER, BERMUDA, BRAZIL                                     | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 3: **0.4801** | CRYSTAL, LINEN, SILVER, BIKE                                      | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 4: **0.4692** | CARGO, MAN, COMMANDO, WITNESS                                     | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)

### Top Candidate Groups:
   - Group 1: **0.5818** | MAN, COMMANDO, BOXER, WITNESS                                     | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 2: **0.5301** | CANAL, PLAN, CLUE, PANAMA                                         | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 3: **0.4903** | CARGO, CHINA, BERMUDA, BRAZIL                                     | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 4: **0.4801** | CRYSTAL, LINEN, SILVER, BIKE                                      | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 5: **0.4874** | CARGO, LINEN, SILVER, BIKE                                        | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 6: **0.4778** | CRYSTAL, CHINA, BERMUDA, BRAZIL                                   | INCORRECT (Max overlap: 2/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 7: **0.5127** | CARGO, LINEN, BOXER, BIKE                                         | INCORRECT (Max overlap: 3/4 with KINDS OF SHORTS)
   - Group 8: **0.5007** | MAN, COMMANDO, SILVER, WITNESS                                    | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 9: **0.5341** | CARGO, LINEN, COMMANDO, BIKE                                      | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 10: **0.4720** | MAN, SILVER, BOXER, WITNESS                                       | INCORRECT (Max overlap: 1/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 11: **0.5148** | CHINA, BOXER, BERMUDA, BRAZIL                                     | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 12: **0.4692** | CARGO, MAN, COMMANDO, WITNESS                                     | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 13: **0.4994** | LINEN, MAN, COMMANDO, WITNESS                                     | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 14: **0.4779** | CARGO, SILVER, BOXER, BIKE                                        | INCORRECT (Max overlap: 3/4 with KINDS OF SHORTS)
   - Group 15: **0.4756** | CARGO, CRYSTAL, LINEN, SILVER                                     | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 16: **0.4634** | CHINA, BIKE, BERMUDA, BRAZIL                                      | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 17: **0.4518** | CARGO, CRYSTAL, LINEN, BIKE                                       | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 18: **0.4771** | CRYSTAL, LINEN, BIKE, BERMUDA                                     | INCORRECT (Max overlap: 2/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 19: **0.4676** | CARGO, CHINA, BOXER, BRAZIL                                       | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 20: **0.5056** | CARGO, COMMANDO, BERMUDA, BRAZIL                                  | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)

---

## Puzzle 78 (ID: 788)
**Words on Board:** BORE, GRAF, PUNCH, POKE, DEVIL, DRAG, VULCAN, SCROLL, BATMAN, ELF, HOVER, PIERCE, CLICK, BORG, KING, SINNER

### Ground Truth Categories:
* **Level 0 (MOUSE ACTIONS) [Type: SEMANTIC_SET]:** CLICK, DRAG, HOVER, SCROLL
* **Level 1 (PERFORATE) [Type: SYNONYM_OR_NEAR]:** BORE, PIERCE, POKE, PUNCH
* **Level 2 (ONES WITH POINTY EARS) [Type: NAMED_ENTITY_SET]:** BATMAN, DEVIL, ELF, VULCAN
* **Level 3 (WIMBLEDON WINNERS) [Type: NAMED_ENTITY_SET]:** BORG, GRAF, KING, SINNER

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6863** | DEVIL, BATMAN, KING, SINNER                                       | INCORRECT (Max overlap: 2/4 with ONES WITH POINTY EARS)
   - Group 2: **0.6520** | DRAG, SCROLL, HOVER, CLICK                                        | CORRECT GROUP (MOUSE ACTIONS, Level 0)
   - Group 3: **0.6416** | GRAF, BATMAN, BORG, KING                                          | INCORRECT (Max overlap: 3/4 with WIMBLEDON WINNERS)
   - Group 4: **0.6321** | BATMAN, PIERCE, KING, SINNER                                      | INCORRECT (Max overlap: 2/4 with WIMBLEDON WINNERS)
   - Group 5: **0.6307** | GRAF, DEVIL, BATMAN, KING                                         | INCORRECT (Max overlap: 2/4 with WIMBLEDON WINNERS)
   - Group 6: **0.6305** | BATMAN, PIERCE, BORG, KING                                        | INCORRECT (Max overlap: 2/4 with WIMBLEDON WINNERS)
   - Group 7: **0.6276** | DEVIL, BATMAN, PIERCE, SINNER                                     | INCORRECT (Max overlap: 2/4 with ONES WITH POINTY EARS)
   - Group 8: **0.6267** | DEVIL, BATMAN, PIERCE, KING                                       | INCORRECT (Max overlap: 2/4 with ONES WITH POINTY EARS)
   - Group 9: **0.6214** | SCROLL, ELF, HOVER, CLICK                                         | INCORRECT (Max overlap: 3/4 with MOUSE ACTIONS)
   - Group 10: **0.6195** | DEVIL, BATMAN, ELF, KING                                          | INCORRECT (Max overlap: 3/4 with ONES WITH POINTY EARS)
   - Group 11: **0.6194** | DEVIL, BATMAN, ELF, SINNER                                        | INCORRECT (Max overlap: 3/4 with ONES WITH POINTY EARS)
   - Group 12: **0.6193** | DEVIL, BATMAN, HOVER, SINNER                                      | INCORRECT (Max overlap: 2/4 with ONES WITH POINTY EARS)
   - Group 13: **0.6155** | BATMAN, BORG, KING, SINNER                                        | INCORRECT (Max overlap: 3/4 with WIMBLEDON WINNERS)
   - Group 14: **0.6142** | SCROLL, HOVER, PIERCE, CLICK                                      | INCORRECT (Max overlap: 3/4 with MOUSE ACTIONS)
   - Group 15: **0.6127** | BATMAN, PIERCE, BORG, SINNER                                      | INCORRECT (Max overlap: 2/4 with WIMBLEDON WINNERS)
   - Group 16: **0.6120** | DEVIL, SCROLL, BATMAN, SINNER                                     | INCORRECT (Max overlap: 2/4 with ONES WITH POINTY EARS)
   - Group 17: **0.6112** | DEVIL, SCROLL, HOVER, CLICK                                       | INCORRECT (Max overlap: 3/4 with MOUSE ACTIONS)
   - Group 18: **0.6107** | DEVIL, SCROLL, HOVER, SINNER                                      | INCORRECT (Max overlap: 2/4 with MOUSE ACTIONS)
   - Group 19: **0.6062** | GRAF, BATMAN, PIERCE, KING                                        | INCORRECT (Max overlap: 2/4 with WIMBLEDON WINNERS)
   - Group 20: **0.6052** | PIERCE, BORG, KING, SINNER                                        | INCORRECT (Max overlap: 3/4 with WIMBLEDON WINNERS)

---

## Puzzle 79 (ID: 274)
**Words on Board:** MEOW, PAMPER, EYE, SLIPPERS, MOTHER, CRADLE, ROBE, TOWEL, PAJAMAS, WASHCLOTH, SPOIL, BABY, CAN, BUM, REAR, BOOTY

### Ground Truth Categories:
* **Level 0 (TREAT WITH EXCESSIVE CARE) [Type: SYNONYM_OR_NEAR]:** BABY, MOTHER, PAMPER, SPOIL
* **Level 1 (BACKSIDE) [Type: SYNONYM_OR_NEAR]:** BOOTY, BUM, CAN, REAR
* **Level 2 (THINGS IN A SPA LOCKER ROOM) [Type: SEMANTIC_SET]:** ROBE, SLIPPERS, TOWEL, WASHCLOTH
* **Level 3 (CAT’S ___) [Type: FILL_IN_THE_BLANK]:** CRADLE, EYE, MEOW, PAJAMAS

### Top Candidate Partitions:
1. **Partition Score: 0.5968**
   - Group 1: **0.7147** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE)
   - Group 2: **0.7112** | ROBE, TOWEL, PAJAMAS, WASHCLOTH                                   | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 3: **0.5863** | EYE, SLIPPERS, MOTHER, CRADLE                                     | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 4: **0.5447** | MEOW, CAN, BUM, REAR                                              | INCORRECT (Max overlap: 3/4 with BACKSIDE)
2. **Partition Score: 0.5962**
   - Group 1: **0.7147** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE)
   - Group 2: **0.6791** | SLIPPERS, ROBE, PAJAMAS, WASHCLOTH                                | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 3: **0.6163** | EYE, MOTHER, CRADLE, TOWEL                                        | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 4: **0.5447** | MEOW, CAN, BUM, REAR                                              | INCORRECT (Max overlap: 3/4 with BACKSIDE)
3. **Partition Score: 0.5786**
   - Group 1: **0.7147** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE)
   - Group 2: **0.6483** | SLIPPERS, ROBE, TOWEL, PAJAMAS                                    | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 3: **0.5765** | EYE, MOTHER, CRADLE, WASHCLOTH                                    | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 4: **0.5447** | MEOW, CAN, BUM, REAR                                              | INCORRECT (Max overlap: 3/4 with BACKSIDE)
4. **Partition Score: 0.5777**
   - Group 1: **0.7147** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE)
   - Group 2: **0.6273** | SLIPPERS, ROBE, TOWEL, WASHCLOTH                                  | CORRECT GROUP (THINGS IN A SPA LOCKER ROOM, Level 2)
   - Group 3: **0.5939** | EYE, MOTHER, CRADLE, PAJAMAS                                      | INCORRECT (Max overlap: 3/4 with CAT’S ___)
   - Group 4: **0.5447** | MEOW, CAN, BUM, REAR                                              | INCORRECT (Max overlap: 3/4 with BACKSIDE)
5. **Partition Score: 0.5734**
   - Group 1: **0.7147** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE)
   - Group 2: **0.6262** | EYE, SLIPPERS, MOTHER, WASHCLOTH                                  | INCORRECT (Max overlap: 2/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 3: **0.5781** | CRADLE, ROBE, TOWEL, PAJAMAS                                      | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 4: **0.5447** | MEOW, CAN, BUM, REAR                                              | INCORRECT (Max overlap: 3/4 with BACKSIDE)

### Top Candidate Groups:
   - Group 1: **0.7147** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE)
   - Group 2: **0.7112** | ROBE, TOWEL, PAJAMAS, WASHCLOTH                                   | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 3: **0.5863** | EYE, SLIPPERS, MOTHER, CRADLE                                     | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 4: **0.5447** | MEOW, CAN, BUM, REAR                                              | INCORRECT (Max overlap: 3/4 with BACKSIDE)
   - Group 5: **0.6791** | SLIPPERS, ROBE, PAJAMAS, WASHCLOTH                                | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 6: **0.6163** | EYE, MOTHER, CRADLE, TOWEL                                        | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 7: **0.6483** | SLIPPERS, ROBE, TOWEL, PAJAMAS                                    | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 8: **0.5765** | EYE, MOTHER, CRADLE, WASHCLOTH                                    | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 9: **0.6273** | SLIPPERS, ROBE, TOWEL, WASHCLOTH                                  | CORRECT GROUP (THINGS IN A SPA LOCKER ROOM, Level 2)
   - Group 10: **0.5939** | EYE, MOTHER, CRADLE, PAJAMAS                                      | INCORRECT (Max overlap: 3/4 with CAT’S ___)
   - Group 11: **0.6262** | EYE, SLIPPERS, MOTHER, WASHCLOTH                                  | INCORRECT (Max overlap: 2/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 12: **0.5781** | CRADLE, ROBE, TOWEL, PAJAMAS                                      | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 13: **0.6397** | EYE, MOTHER, TOWEL, WASHCLOTH                                     | INCORRECT (Max overlap: 2/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 14: **0.5508** | SLIPPERS, CRADLE, ROBE, PAJAMAS                                   | INCORRECT (Max overlap: 2/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 15: **0.6289** | EYE, SLIPPERS, MOTHER, PAJAMAS                                    | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 16: **0.5577** | CRADLE, ROBE, TOWEL, WASHCLOTH                                    | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 17: **0.6133** | EYE, SLIPPERS, MOTHER, TOWEL                                      | INCORRECT (Max overlap: 2/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 18: **0.5620** | CRADLE, ROBE, PAJAMAS, WASHCLOTH                                  | INCORRECT (Max overlap: 2/4 with CAT’S ___)
   - Group 19: **0.5855** | EYE, ROBE, TOWEL, WASHCLOTH                                       | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 20: **0.5853** | SLIPPERS, MOTHER, CRADLE, PAJAMAS                                 | INCORRECT (Max overlap: 2/4 with CAT’S ___)

---

## Puzzle 80 (ID: 769)
**Words on Board:** PASS, SPIKE, SNAP, WELL, TACK, DON, LEO, MIC, RAP, PUNT, BRAD, SPRING, PIN, NAIL, TAP, RAIN

### Ground Truth Categories:
* **Level 0 (SOURCES OF DRINKING WATER) [Type: SEMANTIC_SET]:** RAIN, SPRING, TAP, WELL
* **Level 1 (THINGS YOU CAN DO WITH A FOOTBALL) [Type: SEMANTIC_SET]:** PASS, PUNT, SNAP, SPIKE
* **Level 2 (SHARP FASTENERS) [Type: SEMANTIC_SET]:** BRAD, NAIL, PIN, TACK
* **Level 3 (STARTS OF TEENAGE MUTANT NINJA TURTLES) [Type: WORD_FORM]:** DON, LEO, MIC, RAP

### Top Candidate Partitions:
1. **Partition Score: 0.5664**
   - Group 1: **0.8180** | SPIKE, BRAD, PIN, NAIL                                            | INCORRECT (Max overlap: 3/4 with SHARP FASTENERS)
   - Group 2: **0.6656** | DON, LEO, MIC, RAIN                                               | INCORRECT (Max overlap: 3/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
   - Group 3: **0.5371** | PASS, SNAP, WELL, SPRING                                          | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 4: **0.5315** | TACK, RAP, PUNT, TAP                                              | INCORRECT (Max overlap: 1/4 with SHARP FASTENERS)
2. **Partition Score: 0.5574**
   - Group 1: **0.7155** | SPIKE, TACK, BRAD, NAIL                                           | INCORRECT (Max overlap: 3/4 with SHARP FASTENERS)
   - Group 2: **0.6263** | SNAP, RAP, PIN, TAP                                               | INCORRECT (Max overlap: 1/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 3: **0.5426** | WELL, PUNT, SPRING, RAIN                                          | INCORRECT (Max overlap: 3/4 with SOURCES OF DRINKING WATER)
   - Group 4: **0.5304** | PASS, DON, LEO, MIC                                               | INCORRECT (Max overlap: 3/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
3. **Partition Score: 0.5544**
   - Group 1: **0.7155** | SPIKE, TACK, BRAD, NAIL                                           | INCORRECT (Max overlap: 3/4 with SHARP FASTENERS)
   - Group 2: **0.6656** | DON, LEO, MIC, RAIN                                               | INCORRECT (Max overlap: 3/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
   - Group 3: **0.5371** | PASS, SNAP, WELL, SPRING                                          | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 4: **0.5073** | RAP, PUNT, PIN, TAP                                               | INCORRECT (Max overlap: 1/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
4. **Partition Score: 0.5543**
   - Group 1: **0.7785** | TACK, BRAD, PIN, NAIL                                             | CORRECT GROUP (SHARP FASTENERS, Level 2)
   - Group 2: **0.6656** | DON, LEO, MIC, RAIN                                               | INCORRECT (Max overlap: 3/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
   - Group 3: **0.5371** | PASS, SNAP, WELL, SPRING                                          | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 4: **0.5073** | SPIKE, RAP, PUNT, TAP                                             | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
5. **Partition Score: 0.5529**
   - Group 1: **0.6656** | DON, LEO, MIC, RAIN                                               | INCORRECT (Max overlap: 3/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
   - Group 2: **0.5802** | TACK, RAP, NAIL, TAP                                              | INCORRECT (Max overlap: 2/4 with SHARP FASTENERS)
   - Group 3: **0.5572** | SPIKE, PUNT, BRAD, PIN                                            | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 4: **0.5371** | PASS, SNAP, WELL, SPRING                                          | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)

### Top Candidate Groups:
   - Group 1: **0.8180** | SPIKE, BRAD, PIN, NAIL                                            | INCORRECT (Max overlap: 3/4 with SHARP FASTENERS)
   - Group 2: **0.6656** | DON, LEO, MIC, RAIN                                               | INCORRECT (Max overlap: 3/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
   - Group 3: **0.5371** | PASS, SNAP, WELL, SPRING                                          | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 4: **0.5315** | TACK, RAP, PUNT, TAP                                              | INCORRECT (Max overlap: 1/4 with SHARP FASTENERS)
   - Group 5: **0.7155** | SPIKE, TACK, BRAD, NAIL                                           | INCORRECT (Max overlap: 3/4 with SHARP FASTENERS)
   - Group 6: **0.6263** | SNAP, RAP, PIN, TAP                                               | INCORRECT (Max overlap: 1/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 7: **0.5426** | WELL, PUNT, SPRING, RAIN                                          | INCORRECT (Max overlap: 3/4 with SOURCES OF DRINKING WATER)
   - Group 8: **0.5304** | PASS, DON, LEO, MIC                                               | INCORRECT (Max overlap: 3/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
   - Group 9: **0.5073** | RAP, PUNT, PIN, TAP                                               | INCORRECT (Max overlap: 1/4 with STARTS OF TEENAGE MUTANT NINJA TURTLES)
   - Group 10: **0.7785** | TACK, BRAD, PIN, NAIL                                             | CORRECT GROUP (SHARP FASTENERS, Level 2)
   - Group 11: **0.5073** | SPIKE, RAP, PUNT, TAP                                             | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 12: **0.5802** | TACK, RAP, NAIL, TAP                                              | INCORRECT (Max overlap: 2/4 with SHARP FASTENERS)
   - Group 13: **0.5572** | SPIKE, PUNT, BRAD, PIN                                            | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 14: **0.7178** | SPIKE, TACK, BRAD, PIN                                            | INCORRECT (Max overlap: 3/4 with SHARP FASTENERS)
   - Group 15: **0.6022** | SNAP, RAP, NAIL, TAP                                              | INCORRECT (Max overlap: 1/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 16: **0.5852** | TACK, RAP, PIN, TAP                                               | INCORRECT (Max overlap: 2/4 with SHARP FASTENERS)
   - Group 17: **0.5444** | SPIKE, PUNT, BRAD, NAIL                                           | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 18: **0.5747** | SNAP, WELL, SPRING, RAIN                                          | INCORRECT (Max overlap: 3/4 with SOURCES OF DRINKING WATER)
   - Group 19: **0.5842** | SPIKE, SNAP, BRAD, PIN                                            | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)
   - Group 20: **0.5765** | SPIKE, SNAP, BRAD, NAIL                                           | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN DO WITH A FOOTBALL)

---

## Puzzle 81 (ID: 550)
**Words on Board:** FUDGE, GEEZ, TEE (SHIRT), BANK, NUTS, DELTA, COMB, SAW, TEE (GOLF), BED, TEA, GEAR, RATS, TI (MUSICAL NOTE), ZIPPER, MOUTH

### Ground Truth Categories:
* **Level 0 (THINGS THAT SOUND LIKE "T") [Type: SOUND_OR_SPELLING]:** TEA, TEE (GOLF), TEE (SHIRT), TI (MUSICAL NOTE)
* **Level 1 (OBJECTS WITH TEETH) [Type: SEMANTIC_SET]:** COMB, GEAR, SAW, ZIPPER
* **Level 2 (MILD OATHS) [Type: SYNONYM_OR_NEAR]:** FUDGE, GEEZ, NUTS, RATS
* **Level 3 (PARTS OF A RIVER) [Type: SEMANTIC_SET]:** BANK, BED, DELTA, MOUTH

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6208** | NUTS, BED, GEAR, ZIPPER                                           | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)
   - Group 2: **0.6164** | FUDGE, NUTS, SAW, BED                                             | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 3: **0.6151** | NUTS, SAW, BED, GEAR                                              | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)
   - Group 4: **0.6130** | NUTS, GEAR, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)
   - Group 5: **0.6104** | GEEZ, NUTS, GEAR, ZIPPER                                          | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 6: **0.6080** | GEEZ, NUTS, BED, ZIPPER                                           | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 7: **0.6067** | GEEZ, BED, GEAR, ZIPPER                                           | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)
   - Group 8: **0.6042** | FUDGE, NUTS, BED, ZIPPER                                          | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 9: **0.6041** | GEEZ, NUTS, SAW, BED                                              | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 10: **0.6029** | NUTS, SAW, BED, ZIPPER                                            | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)
   - Group 11: **0.5982** | BANK, NUTS, SAW, BED                                              | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 12: **0.5972** | GEEZ, NUTS, BED, GEAR                                             | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 13: **0.5926** | GEEZ, NUTS, SAW, GEAR                                             | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 14: **0.5902** | NUTS, COMB, SAW, ZIPPER                                           | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 15: **0.5885** | GEEZ, SAW, BED, GEAR                                              | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)
   - Group 16: **0.5884** | SAW, BED, GEAR, ZIPPER                                            | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 17: **0.5882** | NUTS, SAW, GEAR, ZIPPER                                           | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 18: **0.5866** | NUTS, COMB, GEAR, ZIPPER                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 19: **0.5812** | FUDGE, NUTS, COMB, ZIPPER                                         | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 20: **0.5783** | NUTS, SAW, GEAR, MOUTH                                            | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)

---

## Puzzle 82 (ID: 907)
**Words on Board:** STATUS, MASTERMIND, SITUATION, SORRY, DELICATE, SMALL, OPERATION, TOUGH, MOUSE TRAP, PILLOW, STORY, SWEET, DEAL, STICKY, COMPLEX, BABY

### Ground Truth Categories:
* **Level 0 (TRICKY) [Type: SYNONYM_OR_NEAR]:** COMPLEX, DELICATE, STICKY, TOUGH
* **Level 1 (STATE OF AFFAIRS) [Type: SYNONYM_OR_NEAR]:** DEAL, SITUATION, STATUS, STORY
* **Level 2 (CLASSIC BOARD GAMES) [Type: NAMED_ENTITY_SET]:** MASTERMIND, MOUSE TRAP, OPERATION, SORRY
* **Level 3 (___ TALK) [Type: FILL_IN_THE_BLANK]:** BABY, PILLOW, SMALL, SWEET

### Top Candidate Partitions:
1. **Partition Score: 0.5060**
   - Group 1: **0.5363** | DELICATE, TOUGH, SWEET, STICKY                                    | INCORRECT (Max overlap: 3/4 with TRICKY)
   - Group 2: **0.5282** | SMALL, MOUSE TRAP, PILLOW, BABY                                   | INCORRECT (Max overlap: 3/4 with ___ TALK)
   - Group 3: **0.5066** | MASTERMIND, SORRY, DEAL, COMPLEX                                  | INCORRECT (Max overlap: 2/4 with CLASSIC BOARD GAMES)
   - Group 4: **0.4945** | STATUS, SITUATION, OPERATION, STORY                               | INCORRECT (Max overlap: 3/4 with STATE OF AFFAIRS)
2. **Partition Score: 0.5054**
   - Group 1: **0.5282** | SMALL, MOUSE TRAP, PILLOW, BABY                                   | INCORRECT (Max overlap: 3/4 with ___ TALK)
   - Group 2: **0.5180** | MASTERMIND, SORRY, STICKY, COMPLEX                                | INCORRECT (Max overlap: 2/4 with CLASSIC BOARD GAMES)
   - Group 3: **0.5148** | DELICATE, TOUGH, SWEET, DEAL                                      | INCORRECT (Max overlap: 2/4 with TRICKY)
   - Group 4: **0.4945** | STATUS, SITUATION, OPERATION, STORY                               | INCORRECT (Max overlap: 3/4 with STATE OF AFFAIRS)
3. **Partition Score: 0.5044**
   - Group 1: **0.5282** | SMALL, MOUSE TRAP, PILLOW, BABY                                   | INCORRECT (Max overlap: 3/4 with ___ TALK)
   - Group 2: **0.5251** | MASTERMIND, DELICATE, STICKY, COMPLEX                             | INCORRECT (Max overlap: 3/4 with TRICKY)
   - Group 3: **0.5035** | SORRY, TOUGH, SWEET, DEAL                                         | INCORRECT (Max overlap: 1/4 with CLASSIC BOARD GAMES)
   - Group 4: **0.4945** | STATUS, SITUATION, OPERATION, STORY                               | INCORRECT (Max overlap: 3/4 with STATE OF AFFAIRS)
4. **Partition Score: 0.4997**
   - Group 1: **0.5282** | SMALL, MOUSE TRAP, PILLOW, BABY                                   | INCORRECT (Max overlap: 3/4 with ___ TALK)
   - Group 2: **0.5184** | SORRY, DELICATE, TOUGH, SWEET                                     | INCORRECT (Max overlap: 2/4 with TRICKY)
   - Group 3: **0.4945** | STATUS, SITUATION, OPERATION, STORY                               | INCORRECT (Max overlap: 3/4 with STATE OF AFFAIRS)
   - Group 4: **0.4929** | MASTERMIND, DEAL, STICKY, COMPLEX                                 | INCORRECT (Max overlap: 2/4 with TRICKY)
5. **Partition Score: 0.4963**
   - Group 1: **0.5363** | DELICATE, TOUGH, SWEET, STICKY                                    | INCORRECT (Max overlap: 3/4 with TRICKY)
   - Group 2: **0.5282** | SMALL, MOUSE TRAP, PILLOW, BABY                                   | INCORRECT (Max overlap: 3/4 with ___ TALK)
   - Group 3: **0.5115** | MASTERMIND, SORRY, OPERATION, DEAL                                | INCORRECT (Max overlap: 3/4 with CLASSIC BOARD GAMES)
   - Group 4: **0.4727** | STATUS, SITUATION, STORY, COMPLEX                                 | INCORRECT (Max overlap: 3/4 with STATE OF AFFAIRS)

### Top Candidate Groups:
   - Group 1: **0.5363** | DELICATE, TOUGH, SWEET, STICKY                                    | INCORRECT (Max overlap: 3/4 with TRICKY)
   - Group 2: **0.5282** | SMALL, MOUSE TRAP, PILLOW, BABY                                   | INCORRECT (Max overlap: 3/4 with ___ TALK)
   - Group 3: **0.5066** | MASTERMIND, SORRY, DEAL, COMPLEX                                  | INCORRECT (Max overlap: 2/4 with CLASSIC BOARD GAMES)
   - Group 4: **0.4945** | STATUS, SITUATION, OPERATION, STORY                               | INCORRECT (Max overlap: 3/4 with STATE OF AFFAIRS)
   - Group 5: **0.5180** | MASTERMIND, SORRY, STICKY, COMPLEX                                | INCORRECT (Max overlap: 2/4 with CLASSIC BOARD GAMES)
   - Group 6: **0.5148** | DELICATE, TOUGH, SWEET, DEAL                                      | INCORRECT (Max overlap: 2/4 with TRICKY)
   - Group 7: **0.5251** | MASTERMIND, DELICATE, STICKY, COMPLEX                             | INCORRECT (Max overlap: 3/4 with TRICKY)
   - Group 8: **0.5035** | SORRY, TOUGH, SWEET, DEAL                                         | INCORRECT (Max overlap: 1/4 with CLASSIC BOARD GAMES)
   - Group 9: **0.5184** | SORRY, DELICATE, TOUGH, SWEET                                     | INCORRECT (Max overlap: 2/4 with TRICKY)
   - Group 10: **0.4929** | MASTERMIND, DEAL, STICKY, COMPLEX                                 | INCORRECT (Max overlap: 2/4 with TRICKY)
   - Group 11: **0.5115** | MASTERMIND, SORRY, OPERATION, DEAL                                | INCORRECT (Max overlap: 3/4 with CLASSIC BOARD GAMES)
   - Group 12: **0.4727** | STATUS, SITUATION, STORY, COMPLEX                                 | INCORRECT (Max overlap: 3/4 with STATE OF AFFAIRS)
   - Group 13: **0.5219** | MASTERMIND, SORRY, OPERATION, COMPLEX                             | INCORRECT (Max overlap: 3/4 with CLASSIC BOARD GAMES)
   - Group 14: **0.4669** | STATUS, SITUATION, STORY, DEAL                                    | CORRECT GROUP (STATE OF AFFAIRS, Level 1)
   - Group 15: **0.5014** | SORRY, TOUGH, SWEET, STICKY                                       | INCORRECT (Max overlap: 2/4 with TRICKY)
   - Group 16: **0.4926** | MASTERMIND, DELICATE, DEAL, COMPLEX                               | INCORRECT (Max overlap: 2/4 with TRICKY)
   - Group 17: **0.5144** | MASTERMIND, SORRY, DELICATE, COMPLEX                              | INCORRECT (Max overlap: 2/4 with CLASSIC BOARD GAMES)
   - Group 18: **0.4852** | TOUGH, SWEET, DEAL, STICKY                                        | INCORRECT (Max overlap: 2/4 with TRICKY)
   - Group 19: **0.5203** | MASTERMIND, OPERATION, STICKY, COMPLEX                            | INCORRECT (Max overlap: 2/4 with CLASSIC BOARD GAMES)
   - Group 20: **0.5146** | STATUS, SITUATION, OPERATION, DEAL                                | INCORRECT (Max overlap: 3/4 with STATE OF AFFAIRS)

---

## Puzzle 83 (ID: 699)
**Words on Board:** COMIC, ENERGY, ABSENT, MINUS, LANDING, WANTING, SANS, SUNSET, LOVE, CHEERS, BEANS, BEST, PEP, BACON, SINCERELY, ZIP

### Ground Truth Categories:
* **Level 0 (LETTER SIGN-OFFS) [Type: SEMANTIC_SET]:** BEST, CHEERS, LOVE, SINCERELY
* **Level 1 (WITHOUT) [Type: SYNONYM_OR_NEAR]:** ABSENT, MINUS, SANS, WANTING
* **Level 2 (VIGOR) [Type: SYNONYM_OR_NEAR]:** BEANS, ENERGY, PEP, ZIP
* **Level 3 (___ STRIP) [Type: FILL_IN_THE_BLANK]:** BACON, COMIC, LANDING, SUNSET

### Top Candidate Partitions:
1. **Partition Score: 0.5021**
   - Group 1: **0.6902** | WANTING, CHEERS, BEST, SINCERELY                                  | INCORRECT (Max overlap: 3/4 with LETTER SIGN-OFFS)
   - Group 2: **0.5586** | ABSENT, MINUS, LANDING, LOVE                                      | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 3: **0.5289** | ENERGY, SUNSET, PEP, ZIP                                          | INCORRECT (Max overlap: 3/4 with VIGOR)
   - Group 4: **0.4605** | COMIC, SANS, BEANS, BACON                                         | INCORRECT (Max overlap: 2/4 with ___ STRIP)
2. **Partition Score: 0.4985**
   - Group 1: **0.6902** | WANTING, CHEERS, BEST, SINCERELY                                  | INCORRECT (Max overlap: 3/4 with LETTER SIGN-OFFS)
   - Group 2: **0.5586** | ABSENT, MINUS, LANDING, LOVE                                      | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 3: **0.4909** | ENERGY, PEP, BACON, ZIP                                           | INCORRECT (Max overlap: 3/4 with VIGOR)
   - Group 4: **0.4722** | COMIC, SANS, SUNSET, BEANS                                        | INCORRECT (Max overlap: 2/4 with ___ STRIP)
3. **Partition Score: 0.4978**
   - Group 1: **0.5534** | ABSENT, LANDING, LOVE, CHEERS                                     | INCORRECT (Max overlap: 2/4 with LETTER SIGN-OFFS)
   - Group 2: **0.5412** | MINUS, WANTING, BEST, SINCERELY                                   | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 3: **0.5289** | ENERGY, SUNSET, PEP, ZIP                                          | INCORRECT (Max overlap: 3/4 with VIGOR)
   - Group 4: **0.4605** | COMIC, SANS, BEANS, BACON                                         | INCORRECT (Max overlap: 2/4 with ___ STRIP)
4. **Partition Score: 0.4972**
   - Group 1: **0.6902** | WANTING, CHEERS, BEST, SINCERELY                                  | INCORRECT (Max overlap: 3/4 with LETTER SIGN-OFFS)
   - Group 2: **0.5586** | ABSENT, MINUS, LANDING, LOVE                                      | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 3: **0.4969** | COMIC, ENERGY, PEP, ZIP                                           | INCORRECT (Max overlap: 3/4 with VIGOR)
   - Group 4: **0.4666** | SANS, SUNSET, BEANS, BACON                                        | INCORRECT (Max overlap: 2/4 with ___ STRIP)
5. **Partition Score: 0.4953**
   - Group 1: **0.6959** | ABSENT, WANTING, BEST, SINCERELY                                  | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 2: **0.5314** | MINUS, LANDING, LOVE, CHEERS                                      | INCORRECT (Max overlap: 2/4 with LETTER SIGN-OFFS)
   - Group 3: **0.5289** | ENERGY, SUNSET, PEP, ZIP                                          | INCORRECT (Max overlap: 3/4 with VIGOR)
   - Group 4: **0.4605** | COMIC, SANS, BEANS, BACON                                         | INCORRECT (Max overlap: 2/4 with ___ STRIP)

### Top Candidate Groups:
   - Group 1: **0.6902** | WANTING, CHEERS, BEST, SINCERELY                                  | INCORRECT (Max overlap: 3/4 with LETTER SIGN-OFFS)
   - Group 2: **0.5586** | ABSENT, MINUS, LANDING, LOVE                                      | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 3: **0.5289** | ENERGY, SUNSET, PEP, ZIP                                          | INCORRECT (Max overlap: 3/4 with VIGOR)
   - Group 4: **0.4605** | COMIC, SANS, BEANS, BACON                                         | INCORRECT (Max overlap: 2/4 with ___ STRIP)
   - Group 5: **0.4909** | ENERGY, PEP, BACON, ZIP                                           | INCORRECT (Max overlap: 3/4 with VIGOR)
   - Group 6: **0.4722** | COMIC, SANS, SUNSET, BEANS                                        | INCORRECT (Max overlap: 2/4 with ___ STRIP)
   - Group 7: **0.5534** | ABSENT, LANDING, LOVE, CHEERS                                     | INCORRECT (Max overlap: 2/4 with LETTER SIGN-OFFS)
   - Group 8: **0.5412** | MINUS, WANTING, BEST, SINCERELY                                   | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 9: **0.4969** | COMIC, ENERGY, PEP, ZIP                                           | INCORRECT (Max overlap: 3/4 with VIGOR)
   - Group 10: **0.4666** | SANS, SUNSET, BEANS, BACON                                        | INCORRECT (Max overlap: 2/4 with ___ STRIP)
   - Group 11: **0.6959** | ABSENT, WANTING, BEST, SINCERELY                                  | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 12: **0.5314** | MINUS, LANDING, LOVE, CHEERS                                      | INCORRECT (Max overlap: 2/4 with LETTER SIGN-OFFS)
   - Group 13: **0.4864** | COMIC, SANS, SUNSET, BACON                                        | INCORRECT (Max overlap: 3/4 with ___ STRIP)
   - Group 14: **0.4560** | ENERGY, BEANS, PEP, ZIP                                           | CORRECT GROUP (VIGOR, Level 2)
   - Group 15: **0.5215** | COMIC, LANDING, SANS, SUNSET                                      | INCORRECT (Max overlap: 3/4 with ___ STRIP)
   - Group 16: **0.4630** | ABSENT, MINUS, LOVE, BEANS                                        | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 17: **0.5675** | MINUS, CHEERS, BEST, SINCERELY                                    | INCORRECT (Max overlap: 3/4 with LETTER SIGN-OFFS)
   - Group 18: **0.4768** | ABSENT, LANDING, WANTING, LOVE                                    | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 19: **0.5299** | ABSENT, MINUS, BEST, SINCERELY                                    | INCORRECT (Max overlap: 2/4 with WITHOUT)
   - Group 20: **0.4696** | LANDING, WANTING, LOVE, CHEERS                                    | INCORRECT (Max overlap: 2/4 with LETTER SIGN-OFFS)

---

## Puzzle 84 (ID: 118)
**Words on Board:** HANNAH, SAVANNA, CLIFF, SHARON, AARON, DREW, ROSE, EVE, WILL, DARREN, OTTO, NATAN, MAY, KAREN, DALE, BROOK

### Ground Truth Categories:
* **Level 0 (RHYMES) [Type: SOUND_OR_SPELLING]:** DARREN, KAREN, SHARON, AARON
* **Level 1 (NATURAL FEATURES) [Type: SEMANTIC_SET]:** DALE, BROOK, SAVANNA, CLIFF
* **Level 2 (IRREGULAR VERBS) [Type: SEMANTIC_SET]:** DREW, ROSE, WILL, MAY
* **Level 3 (PALINDROMES) [Type: WORD_FORM]:** EVE, HANNAH, OTTO, NATAN

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6785** | SAVANNA, DARREN, KAREN, BROOK                                     | INCORRECT (Max overlap: 2/4 with NATURAL FEATURES)
   - Group 2: **0.6780** | SAVANNA, DARREN, NATAN, KAREN                                     | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 3: **0.6738** | HANNAH, SAVANNA, KAREN, BROOK                                     | INCORRECT (Max overlap: 2/4 with NATURAL FEATURES)
   - Group 4: **0.6715** | HANNAH, SAVANNA, DARREN, BROOK                                    | INCORRECT (Max overlap: 2/4 with NATURAL FEATURES)
   - Group 5: **0.6675** | HANNAH, SAVANNA, DARREN, KAREN                                    | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 6: **0.6629** | DARREN, OTTO, KAREN, BROOK                                        | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 7: **0.6616** | SAVANNA, DARREN, NATAN, BROOK                                     | INCORRECT (Max overlap: 2/4 with NATURAL FEATURES)
   - Group 8: **0.6602** | AARON, OTTO, KAREN, BROOK                                         | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 9: **0.6595** | DARREN, OTTO, NATAN, KAREN                                        | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 10: **0.6593** | HANNAH, AARON, OTTO, KAREN                                        | INCORRECT (Max overlap: 2/4 with PALINDROMES)
   - Group 11: **0.6572** | SAVANNA, CLIFF, DARREN, BROOK                                     | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES)
   - Group 12: **0.6560** | AARON, DARREN, OTTO, BROOK                                        | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 13: **0.6555** | HANNAH, AARON, OTTO, BROOK                                        | INCORRECT (Max overlap: 2/4 with PALINDROMES)
   - Group 14: **0.6550** | SAVANNA, NATAN, KAREN, BROOK                                      | INCORRECT (Max overlap: 2/4 with NATURAL FEATURES)
   - Group 15: **0.6545** | HANNAH, AARON, KAREN, BROOK                                       | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 16: **0.6541** | AARON, DARREN, OTTO, KAREN                                        | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 17: **0.6531** | HANNAH, OTTO, KAREN, BROOK                                        | INCORRECT (Max overlap: 2/4 with PALINDROMES)
   - Group 18: **0.6508** | HANNAH, SAVANNA, AARON, KAREN                                     | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 19: **0.6505** | HANNAH, AARON, DARREN, BROOK                                      | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 20: **0.6500** | HANNAH, DARREN, KAREN, BROOK                                      | INCORRECT (Max overlap: 2/4 with RHYMES)

---

## Puzzle 85 (ID: 739)
**Words on Board:** BALL, FOILS, BLOCKS, DESTINATION, GLOVES, MASKS, PAPERS, FINAL, ATTENDANCE, JACKS, HOMEWORK, STOPS, ROUTE, JACKETS, TRAIN, STARTING POINT

### Ground Truth Categories:
* **Level 0 (COMPONENTS OF ONE’S GRADE) [Type: SEMANTIC_SET]:** ATTENDANCE, FINAL, HOMEWORK, PAPERS
* **Level 1 (MAP APP OPTIONS) [Type: SEMANTIC_SET]:** DESTINATION, ROUTE, STARTING POINT, STOPS
* **Level 2 (CLASSIC TOYS) [Type: SEMANTIC_SET]:** BALL, BLOCKS, JACKS, TRAIN
* **Level 3 (FENCING GEAR) [Type: SEMANTIC_SET]:** FOILS, GLOVES, JACKETS, MASKS

### Top Candidate Partitions:
1. **Partition Score: 0.5268**
   - Group 1: **0.5922** | FOILS, BLOCKS, FINAL, STOPS                                       | INCORRECT (Max overlap: 1/4 with FENCING GEAR)
   - Group 2: **0.5628** | MASKS, PAPERS, ATTENDANCE, JACKETS                                | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 3: **0.5175** | DESTINATION, HOMEWORK, ROUTE, STARTING POINT                      | INCORRECT (Max overlap: 3/4 with MAP APP OPTIONS)
   - Group 4: **0.5134** | BALL, GLOVES, JACKS, TRAIN                                        | INCORRECT (Max overlap: 3/4 with CLASSIC TOYS)
2. **Partition Score: 0.5211**
   - Group 1: **0.5734** | MASKS, PAPERS, FINAL, JACKETS                                     | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 2: **0.5599** | FOILS, BLOCKS, STOPS, ROUTE                                       | INCORRECT (Max overlap: 2/4 with MAP APP OPTIONS)
   - Group 3: **0.5134** | BALL, GLOVES, JACKS, TRAIN                                        | INCORRECT (Max overlap: 3/4 with CLASSIC TOYS)
   - Group 4: **0.5056** | DESTINATION, ATTENDANCE, HOMEWORK, STARTING POINT                 | INCORRECT (Max overlap: 2/4 with MAP APP OPTIONS)
3. **Partition Score: 0.5195**
   - Group 1: **0.6303** | MASKS, PAPERS, HOMEWORK, JACKETS                                  | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 2: **0.5922** | FOILS, BLOCKS, FINAL, STOPS                                       | INCORRECT (Max overlap: 1/4 with FENCING GEAR)
   - Group 3: **0.5134** | BALL, GLOVES, JACKS, TRAIN                                        | INCORRECT (Max overlap: 3/4 with CLASSIC TOYS)
   - Group 4: **0.4863** | DESTINATION, ATTENDANCE, ROUTE, STARTING POINT                    | INCORRECT (Max overlap: 3/4 with MAP APP OPTIONS)
4. **Partition Score: 0.5153**
   - Group 1: **0.5441** | FOILS, PAPERS, FINAL, STOPS                                       | INCORRECT (Max overlap: 2/4 with COMPONENTS OF ONE’S GRADE)
   - Group 2: **0.5175** | DESTINATION, HOMEWORK, ROUTE, STARTING POINT                      | INCORRECT (Max overlap: 3/4 with MAP APP OPTIONS)
   - Group 3: **0.5168** | BLOCKS, MASKS, ATTENDANCE, JACKETS                                | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 4: **0.5134** | BALL, GLOVES, JACKS, TRAIN                                        | INCORRECT (Max overlap: 3/4 with CLASSIC TOYS)
5. **Partition Score: 0.5148**
   - Group 1: **0.8065** | FOILS, BLOCKS, MASKS, JACKETS                                     | INCORRECT (Max overlap: 3/4 with FENCING GEAR)
   - Group 2: **0.5175** | DESTINATION, HOMEWORK, ROUTE, STARTING POINT                      | INCORRECT (Max overlap: 3/4 with MAP APP OPTIONS)
   - Group 3: **0.5151** | PAPERS, FINAL, ATTENDANCE, STOPS                                  | INCORRECT (Max overlap: 3/4 with COMPONENTS OF ONE’S GRADE)
   - Group 4: **0.5134** | BALL, GLOVES, JACKS, TRAIN                                        | INCORRECT (Max overlap: 3/4 with CLASSIC TOYS)

### Top Candidate Groups:
   - Group 1: **0.5922** | FOILS, BLOCKS, FINAL, STOPS                                       | INCORRECT (Max overlap: 1/4 with FENCING GEAR)
   - Group 2: **0.5628** | MASKS, PAPERS, ATTENDANCE, JACKETS                                | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 3: **0.5175** | DESTINATION, HOMEWORK, ROUTE, STARTING POINT                      | INCORRECT (Max overlap: 3/4 with MAP APP OPTIONS)
   - Group 4: **0.5134** | BALL, GLOVES, JACKS, TRAIN                                        | INCORRECT (Max overlap: 3/4 with CLASSIC TOYS)
   - Group 5: **0.5734** | MASKS, PAPERS, FINAL, JACKETS                                     | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 6: **0.5599** | FOILS, BLOCKS, STOPS, ROUTE                                       | INCORRECT (Max overlap: 2/4 with MAP APP OPTIONS)
   - Group 7: **0.5056** | DESTINATION, ATTENDANCE, HOMEWORK, STARTING POINT                 | INCORRECT (Max overlap: 2/4 with MAP APP OPTIONS)
   - Group 8: **0.6303** | MASKS, PAPERS, HOMEWORK, JACKETS                                  | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 9: **0.4863** | DESTINATION, ATTENDANCE, ROUTE, STARTING POINT                    | INCORRECT (Max overlap: 3/4 with MAP APP OPTIONS)
   - Group 10: **0.5441** | FOILS, PAPERS, FINAL, STOPS                                       | INCORRECT (Max overlap: 2/4 with COMPONENTS OF ONE’S GRADE)
   - Group 11: **0.5168** | BLOCKS, MASKS, ATTENDANCE, JACKETS                                | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 12: **0.8065** | FOILS, BLOCKS, MASKS, JACKETS                                     | INCORRECT (Max overlap: 3/4 with FENCING GEAR)
   - Group 13: **0.5151** | PAPERS, FINAL, ATTENDANCE, STOPS                                  | INCORRECT (Max overlap: 3/4 with COMPONENTS OF ONE’S GRADE)
   - Group 14: **0.5161** | BLOCKS, MASKS, FINAL, STOPS                                       | INCORRECT (Max overlap: 1/4 with CLASSIC TOYS)
   - Group 15: **0.5145** | FOILS, PAPERS, ATTENDANCE, JACKETS                                | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 16: **0.5703** | FOILS, BLOCKS, HOMEWORK, STOPS                                    | INCORRECT (Max overlap: 1/4 with FENCING GEAR)
   - Group 17: **0.5292** | BLOCKS, MASKS, ROUTE, JACKETS                                     | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 18: **0.5199** | MASKS, PAPERS, ROUTE, JACKETS                                     | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 19: **0.5207** | FOILS, PAPERS, ROUTE, JACKETS                                     | INCORRECT (Max overlap: 2/4 with FENCING GEAR)
   - Group 20: **0.5958** | FOILS, PAPERS, FINAL, JACKETS                                     | INCORRECT (Max overlap: 2/4 with FENCING GEAR)

---

## Puzzle 86 (ID: 978)
**Words on Board:** INFERIORITY, ENCYCLOPEDIA, VESTIGE, ATLAS, CALLIOPE, OEDIPUS, RINGMASTER, REMINDER, SUPERIORITY, DIALECT, ELECTRA, THESAURUS, TRACE, DICTIONARY, BUZZARD, ECHO

### Ground Truth Categories:
* **Level 0 (REFERENCE BOOKS) [Type: SEMANTIC_SET]:** ATLAS, DICTIONARY, ENCYCLOPEDIA, THESAURUS
* **Level 1 (SOMETHING THAT BRINGS BACK MEMORIES) [Type: SYNONYM_OR_NEAR]:** ECHO, REMINDER, TRACE, VESTIGE
* **Level 2 (KINDS OF COMPLEXES) [Type: FILL_IN_THE_BLANK]:** ELECTRA, INFERIORITY, OEDIPUS, SUPERIORITY
* **Level 3 (STARTING WITH WAYS TO REACH SOMEONE VIA PHONE) [Type: WORDPLAY_TRANSFORM]:** BUZZARD, CALLIOPE, DIALECT, RINGMASTER

### Top Candidate Partitions:
1. **Partition Score: 0.4198**
   - Group 1: **0.5174** | ENCYCLOPEDIA, THESAURUS, TRACE, DICTIONARY                        | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 2: **0.5023** | CALLIOPE, RINGMASTER, ELECTRA, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 3: **0.4324** | ATLAS, OEDIPUS, DIALECT, ECHO                                     | INCORRECT (Max overlap: 1/4 with REFERENCE BOOKS)
   - Group 4: **0.3722** | INFERIORITY, VESTIGE, REMINDER, SUPERIORITY                       | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
2. **Partition Score: 0.4151**
   - Group 1: **0.5174** | ENCYCLOPEDIA, THESAURUS, TRACE, DICTIONARY                        | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 2: **0.5023** | CALLIOPE, RINGMASTER, ELECTRA, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 3: **0.4318** | ATLAS, OEDIPUS, REMINDER, ECHO                                    | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 4: **0.3631** | INFERIORITY, VESTIGE, SUPERIORITY, DIALECT                        | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
3. **Partition Score: 0.4145**
   - Group 1: **0.5408** | ENCYCLOPEDIA, ATLAS, THESAURUS, DICTIONARY                        | CORRECT GROUP (REFERENCE BOOKS, Level 0)
   - Group 2: **0.5023** | CALLIOPE, RINGMASTER, ELECTRA, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 3: **0.4349** | OEDIPUS, REMINDER, DIALECT, ECHO                                  | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 4: **0.3604** | INFERIORITY, VESTIGE, SUPERIORITY, TRACE                          | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
4. **Partition Score: 0.4084**
   - Group 1: **0.5023** | CALLIOPE, RINGMASTER, ELECTRA, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 2: **0.4809** | ENCYCLOPEDIA, DIALECT, THESAURUS, DICTIONARY                      | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 3: **0.4318** | ATLAS, OEDIPUS, REMINDER, ECHO                                    | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 4: **0.3604** | INFERIORITY, VESTIGE, SUPERIORITY, TRACE                          | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
5. **Partition Score: 0.4045**
   - Group 1: **0.5023** | CALLIOPE, RINGMASTER, ELECTRA, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 2: **0.4648** | ENCYCLOPEDIA, REMINDER, THESAURUS, DICTIONARY                     | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 3: **0.4324** | ATLAS, OEDIPUS, DIALECT, ECHO                                     | INCORRECT (Max overlap: 1/4 with REFERENCE BOOKS)
   - Group 4: **0.3604** | INFERIORITY, VESTIGE, SUPERIORITY, TRACE                          | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)

### Top Candidate Groups:
   - Group 1: **0.5174** | ENCYCLOPEDIA, THESAURUS, TRACE, DICTIONARY                        | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 2: **0.5023** | CALLIOPE, RINGMASTER, ELECTRA, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 3: **0.4324** | ATLAS, OEDIPUS, DIALECT, ECHO                                     | INCORRECT (Max overlap: 1/4 with REFERENCE BOOKS)
   - Group 4: **0.3722** | INFERIORITY, VESTIGE, REMINDER, SUPERIORITY                       | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
   - Group 5: **0.4318** | ATLAS, OEDIPUS, REMINDER, ECHO                                    | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 6: **0.3631** | INFERIORITY, VESTIGE, SUPERIORITY, DIALECT                        | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
   - Group 7: **0.5408** | ENCYCLOPEDIA, ATLAS, THESAURUS, DICTIONARY                        | CORRECT GROUP (REFERENCE BOOKS, Level 0)
   - Group 8: **0.4349** | OEDIPUS, REMINDER, DIALECT, ECHO                                  | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 9: **0.3604** | INFERIORITY, VESTIGE, SUPERIORITY, TRACE                          | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
   - Group 10: **0.4809** | ENCYCLOPEDIA, DIALECT, THESAURUS, DICTIONARY                      | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 11: **0.4648** | ENCYCLOPEDIA, REMINDER, THESAURUS, DICTIONARY                     | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 12: **0.5082** | CALLIOPE, ELECTRA, BUZZARD, ECHO                                  | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 13: **0.3857** | OEDIPUS, RINGMASTER, REMINDER, DIALECT                            | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 14: **0.3859** | ENCYCLOPEDIA, SUPERIORITY, THESAURUS, DICTIONARY                  | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 15: **0.3799** | INFERIORITY, VESTIGE, REMINDER, TRACE                             | INCORRECT (Max overlap: 3/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 16: **0.4468** | CALLIOPE, OEDIPUS, ELECTRA, BUZZARD                               | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 17: **0.4058** | RINGMASTER, REMINDER, DIALECT, ECHO                               | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 18: **0.3474** | ATLAS, OEDIPUS, RINGMASTER, REMINDER                              | INCORRECT (Max overlap: 1/4 with REFERENCE BOOKS)
   - Group 19: **0.4800** | RINGMASTER, ELECTRA, BUZZARD, ECHO                                | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 20: **0.3541** | ATLAS, CALLIOPE, OEDIPUS, DIALECT                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)

---

## Puzzle 87 (ID: 12)
**Words on Board:** PACK, PRIDE, SIN, TORTOISE, COT, SCHOOL, SLOTH, FLOCK, LUST, POD, GREED, SEC, LORIS, SNAIL, ENVY, TAN

### Ground Truth Categories:
* **Level 0 (ANIMAL GROUP NAMES) [Type: SEMANTIC_SET]:** FLOCK, PACK, POD, SCHOOL
* **Level 1 (DEADLY SINS) [Type: SEMANTIC_SET]:** ENVY, GREED, LUST, PRIDE
* **Level 2 (SLOW ANIMALS) [Type: SEMANTIC_SET]:** LORIS, SLOTH, SNAIL, TORTOISE
* **Level 3 (TRIG FUNCTIONS) [Type: SEMANTIC_SET]:** COT, SEC, SIN, TAN

### Top Candidate Partitions:
1. **Partition Score: 0.6026**
   - Group 1: **0.7544** | SLOTH, LUST, GREED, ENVY                                          | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 2: **0.7406** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 3: **0.5815** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.5442** | PRIDE, SIN, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
2. **Partition Score: 0.5861**
   - Group 1: **0.7574** | PRIDE, SLOTH, LUST, GREED                                         | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 2: **0.7406** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 3: **0.5815** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.5111** | SIN, SEC, ENVY, TAN                                               | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
3. **Partition Score: 0.5728**
   - Group 1: **0.8364** | PRIDE, LUST, GREED, ENVY                                          | CORRECT GROUP (DEADLY SINS, Level 1)
   - Group 2: **0.7406** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 3: **0.5582** | TORTOISE, SLOTH, LORIS, SNAIL                                     | CORRECT GROUP (SLOW ANIMALS, Level 2)
   - Group 4: **0.4962** | SIN, COT, SEC, TAN                                                | CORRECT GROUP (TRIG FUNCTIONS, Level 3)
4. **Partition Score: 0.5630**
   - Group 1: **0.7798** | PACK, PRIDE, SCHOOL, FLOCK                                        | INCORRECT (Max overlap: 3/4 with ANIMAL GROUP NAMES)
   - Group 2: **0.7544** | SLOTH, LUST, GREED, ENVY                                          | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 3: **0.5052** | TORTOISE, POD, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.4962** | SIN, COT, SEC, TAN                                                | CORRECT GROUP (TRIG FUNCTIONS, Level 3)
5. **Partition Score: 0.5486**
   - Group 1: **0.7406** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 2: **0.5644** | PRIDE, LUST, SEC, ENVY                                            | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 3: **0.5595** | TORTOISE, COT, SNAIL, TAN                                         | INCORRECT (Max overlap: 2/4 with SLOW ANIMALS)
   - Group 4: **0.5353** | SIN, SLOTH, GREED, LORIS                                          | INCORRECT (Max overlap: 2/4 with SLOW ANIMALS)

### Top Candidate Groups:
   - Group 1: **0.7544** | SLOTH, LUST, GREED, ENVY                                          | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 2: **0.7406** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 3: **0.5815** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.5442** | PRIDE, SIN, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
   - Group 5: **0.7574** | PRIDE, SLOTH, LUST, GREED                                         | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 6: **0.5111** | SIN, SEC, ENVY, TAN                                               | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
   - Group 7: **0.8364** | PRIDE, LUST, GREED, ENVY                                          | CORRECT GROUP (DEADLY SINS, Level 1)
   - Group 8: **0.5582** | TORTOISE, SLOTH, LORIS, SNAIL                                     | CORRECT GROUP (SLOW ANIMALS, Level 2)
   - Group 9: **0.4962** | SIN, COT, SEC, TAN                                                | CORRECT GROUP (TRIG FUNCTIONS, Level 3)
   - Group 10: **0.7798** | PACK, PRIDE, SCHOOL, FLOCK                                        | INCORRECT (Max overlap: 3/4 with ANIMAL GROUP NAMES)
   - Group 11: **0.5052** | TORTOISE, POD, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 12: **0.5644** | PRIDE, LUST, SEC, ENVY                                            | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 13: **0.5595** | TORTOISE, COT, SNAIL, TAN                                         | INCORRECT (Max overlap: 2/4 with SLOW ANIMALS)
   - Group 14: **0.5353** | SIN, SLOTH, GREED, LORIS                                          | INCORRECT (Max overlap: 2/4 with SLOW ANIMALS)
   - Group 15: **0.5932** | SIN, LUST, SEC, ENVY                                              | INCORRECT (Max overlap: 2/4 with TRIG FUNCTIONS)
   - Group 16: **0.5171** | PRIDE, SLOTH, GREED, LORIS                                        | INCORRECT (Max overlap: 2/4 with DEADLY SINS)
   - Group 17: **0.6163** | PRIDE, SIN, LUST, SEC                                             | INCORRECT (Max overlap: 2/4 with DEADLY SINS)
   - Group 18: **0.4982** | SLOTH, GREED, LORIS, ENVY                                         | INCORRECT (Max overlap: 2/4 with SLOW ANIMALS)
   - Group 19: **0.5362** | PRIDE, GREED, LORIS, ENVY                                         | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 20: **0.5333** | SIN, SLOTH, LUST, SEC                                             | INCORRECT (Max overlap: 2/4 with TRIG FUNCTIONS)

---

## Puzzle 88 (ID: 1019)
**Words on Board:** GRAFFITI, QUESTION, BEAUTY, HUSTLE, PSYCHO, POSTER, ROBOT, RECEIPT, CORPS, COUP, TWIST, CHECK, STRETCH, STENCIL, MASHED POTATO, MURAL

### Ground Truth Categories:
* **Level 0 (IMAGES SEEN ON THE STREET) [Type: SEMANTIC_SET]:** GRAFFITI, MURAL, POSTER, STENCIL
* **Level 1 (RETRO DANCE CRAZES) [Type: NAMED_ENTITY_SET]:** HUSTLE, MASHED POTATO, ROBOT, TWIST
* **Level 2 (SILENT "P") [Type: SOUND_OR_SPELLING]:** CORPS, COUP, PSYCHO, RECEIPT
* **Level 3 (___ MARK) [Type: FILL_IN_THE_BLANK]:** BEAUTY, CHECK, QUESTION, STRETCH

### Top Candidate Partitions:
1. **Partition Score: 0.4878**
   - Group 1: **0.5768** | GRAFFITI, POSTER, STENCIL, MURAL                                  | CORRECT GROUP (IMAGES SEEN ON THE STREET, Level 0)
   - Group 2: **0.5150** | HUSTLE, COUP, TWIST, STRETCH                                      | INCORRECT (Max overlap: 2/4 with RETRO DANCE CRAZES)
   - Group 3: **0.5090** | BEAUTY, PSYCHO, ROBOT, CORPS                                      | INCORRECT (Max overlap: 2/4 with SILENT "P")
   - Group 4: **0.4637** | QUESTION, RECEIPT, CHECK, MASHED POTATO                           | INCORRECT (Max overlap: 2/4 with ___ MARK)
2. **Partition Score: 0.4863**
   - Group 1: **0.5535** | GRAFFITI, CORPS, STENCIL, MURAL                                   | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)
   - Group 2: **0.5150** | HUSTLE, COUP, TWIST, STRETCH                                      | INCORRECT (Max overlap: 2/4 with RETRO DANCE CRAZES)
   - Group 3: **0.5027** | BEAUTY, PSYCHO, POSTER, ROBOT                                     | INCORRECT (Max overlap: 1/4 with ___ MARK)
   - Group 4: **0.4637** | QUESTION, RECEIPT, CHECK, MASHED POTATO                           | INCORRECT (Max overlap: 2/4 with ___ MARK)
3. **Partition Score: 0.4829**
   - Group 1: **0.5150** | HUSTLE, COUP, TWIST, STRETCH                                      | INCORRECT (Max overlap: 2/4 with RETRO DANCE CRAZES)
   - Group 2: **0.5037** | GRAFFITI, BEAUTY, PSYCHO, ROBOT                                   | INCORRECT (Max overlap: 1/4 with IMAGES SEEN ON THE STREET)
   - Group 3: **0.5005** | POSTER, CORPS, STENCIL, MURAL                                     | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)
   - Group 4: **0.4637** | QUESTION, RECEIPT, CHECK, MASHED POTATO                           | INCORRECT (Max overlap: 2/4 with ___ MARK)
4. **Partition Score: 0.4825**
   - Group 1: **0.5768** | GRAFFITI, POSTER, STENCIL, MURAL                                  | CORRECT GROUP (IMAGES SEEN ON THE STREET, Level 0)
   - Group 2: **0.5150** | HUSTLE, COUP, TWIST, STRETCH                                      | INCORRECT (Max overlap: 2/4 with RETRO DANCE CRAZES)
   - Group 3: **0.4757** | QUESTION, RECEIPT, CORPS, MASHED POTATO                           | INCORRECT (Max overlap: 2/4 with SILENT "P")
   - Group 4: **0.4696** | BEAUTY, PSYCHO, ROBOT, CHECK                                      | INCORRECT (Max overlap: 2/4 with ___ MARK)
5. **Partition Score: 0.4817**
   - Group 1: **0.5150** | HUSTLE, COUP, TWIST, STRETCH                                      | INCORRECT (Max overlap: 2/4 with RETRO DANCE CRAZES)
   - Group 2: **0.5102** | QUESTION, POSTER, RECEIPT, CHECK                                  | INCORRECT (Max overlap: 2/4 with ___ MARK)
   - Group 3: **0.5090** | BEAUTY, PSYCHO, ROBOT, CORPS                                      | INCORRECT (Max overlap: 2/4 with SILENT "P")
   - Group 4: **0.4537** | GRAFFITI, STENCIL, MASHED POTATO, MURAL                           | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)

### Top Candidate Groups:
   - Group 1: **0.5768** | GRAFFITI, POSTER, STENCIL, MURAL                                  | CORRECT GROUP (IMAGES SEEN ON THE STREET, Level 0)
   - Group 2: **0.5150** | HUSTLE, COUP, TWIST, STRETCH                                      | INCORRECT (Max overlap: 2/4 with RETRO DANCE CRAZES)
   - Group 3: **0.5090** | BEAUTY, PSYCHO, ROBOT, CORPS                                      | INCORRECT (Max overlap: 2/4 with SILENT "P")
   - Group 4: **0.4637** | QUESTION, RECEIPT, CHECK, MASHED POTATO                           | INCORRECT (Max overlap: 2/4 with ___ MARK)
   - Group 5: **0.5535** | GRAFFITI, CORPS, STENCIL, MURAL                                   | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)
   - Group 6: **0.5027** | BEAUTY, PSYCHO, POSTER, ROBOT                                     | INCORRECT (Max overlap: 1/4 with ___ MARK)
   - Group 7: **0.5037** | GRAFFITI, BEAUTY, PSYCHO, ROBOT                                   | INCORRECT (Max overlap: 1/4 with IMAGES SEEN ON THE STREET)
   - Group 8: **0.5005** | POSTER, CORPS, STENCIL, MURAL                                     | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)
   - Group 9: **0.4757** | QUESTION, RECEIPT, CORPS, MASHED POTATO                           | INCORRECT (Max overlap: 2/4 with SILENT "P")
   - Group 10: **0.4696** | BEAUTY, PSYCHO, ROBOT, CHECK                                      | INCORRECT (Max overlap: 2/4 with ___ MARK)
   - Group 11: **0.5102** | QUESTION, POSTER, RECEIPT, CHECK                                  | INCORRECT (Max overlap: 2/4 with ___ MARK)
   - Group 12: **0.4537** | GRAFFITI, STENCIL, MASHED POTATO, MURAL                           | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)
   - Group 13: **0.4965** | GRAFFITI, ROBOT, STENCIL, MURAL                                   | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)
   - Group 14: **0.4775** | BEAUTY, PSYCHO, POSTER, CHECK                                     | INCORRECT (Max overlap: 2/4 with ___ MARK)
   - Group 15: **0.4735** | GRAFFITI, CHECK, STENCIL, MURAL                                   | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)
   - Group 16: **0.5065** | QUESTION, RECEIPT, CORPS, CHECK                                   | INCORRECT (Max overlap: 2/4 with ___ MARK)
   - Group 17: **0.5311** | GRAFFITI, ROBOT, CORPS, STENCIL                                   | INCORRECT (Max overlap: 2/4 with IMAGES SEEN ON THE STREET)
   - Group 18: **0.4710** | BEAUTY, PSYCHO, POSTER, MURAL                                     | INCORRECT (Max overlap: 2/4 with IMAGES SEEN ON THE STREET)
   - Group 19: **0.5042** | GRAFFITI, PSYCHO, ROBOT, CORPS                                    | INCORRECT (Max overlap: 2/4 with SILENT "P")
   - Group 20: **0.4815** | BEAUTY, POSTER, STENCIL, MURAL                                    | INCORRECT (Max overlap: 3/4 with IMAGES SEEN ON THE STREET)

---

## Puzzle 89 (ID: 984)
**Words on Board:** LATE, MINION, GREAT, INFINITIVE, AUDITS, DODGERS, SOLID, ABSENT, BACKGROUND, PHEW, EXCUSED, PERFECT, HISTORY, LIFE, PRESENT, PAST

### Ground Truth Categories:
* **Level 0 (EXPERIENCE) [Type: SYNONYM_OR_NEAR]:** BACKGROUND, HISTORY, LIFE, PAST
* **Level 1 (ATTENDANCE STATUS) [Type: SEMANTIC_SET]:** ABSENT, EXCUSED, LATE, PRESENT
* **Level 2 (COMMENTARY ABOUT YOUR CONNECTIONS RESULTS) [Type: SEMANTIC_SET]:** GREAT, PERFECT, PHEW, SOLID
* **Level 3 (CAR BRANDS PLUS TWO LETTERS) [Type: WORDPLAY_TRANSFORM]:** AUDITS, DODGERS, INFINITIVE, MINION

### Top Candidate Partitions:
1. **Partition Score: 0.5726**
   - Group 1: **0.6025** | LATE, AUDITS, ABSENT, EXCUSED                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 2: **0.5962** | MINION, DODGERS, PHEW, LIFE                                       | INCORRECT (Max overlap: 2/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 3: **0.5717** | GREAT, INFINITIVE, SOLID, PERFECT                                 | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 4: **0.5613** | BACKGROUND, HISTORY, PRESENT, PAST                                | INCORRECT (Max overlap: 3/4 with EXPERIENCE)
2. **Partition Score: 0.5640**
   - Group 1: **0.5962** | MINION, DODGERS, PHEW, LIFE                                       | INCORRECT (Max overlap: 2/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 2: **0.5874** | AUDITS, ABSENT, EXCUSED, PRESENT                                  | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 3: **0.5717** | GREAT, INFINITIVE, SOLID, PERFECT                                 | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 4: **0.5485** | LATE, BACKGROUND, HISTORY, PAST                                   | INCORRECT (Max overlap: 3/4 with EXPERIENCE)
3. **Partition Score: 0.5636**
   - Group 1: **0.6025** | LATE, AUDITS, ABSENT, EXCUSED                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 2: **0.5709** | GREAT, SOLID, PHEW, PERFECT                                       | CORRECT GROUP (COMMENTARY ABOUT YOUR CONNECTIONS RESULTS, Level 2)
   - Group 3: **0.5613** | BACKGROUND, HISTORY, PRESENT, PAST                                | INCORRECT (Max overlap: 3/4 with EXPERIENCE)
   - Group 4: **0.5610** | MINION, INFINITIVE, DODGERS, LIFE                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
4. **Partition Score: 0.5631**
   - Group 1: **0.6025** | LATE, AUDITS, ABSENT, EXCUSED                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 2: **0.5658** | MINION, INFINITIVE, DODGERS, PHEW                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 3: **0.5639** | GREAT, SOLID, PERFECT, LIFE                                       | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 4: **0.5613** | BACKGROUND, HISTORY, PRESENT, PAST                                | INCORRECT (Max overlap: 3/4 with EXPERIENCE)
5. **Partition Score: 0.5625**
   - Group 1: **0.6338** | LATE, ABSENT, EXCUSED, PRESENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1)
   - Group 2: **0.5962** | MINION, DODGERS, PHEW, LIFE                                       | INCORRECT (Max overlap: 2/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 3: **0.5717** | GREAT, INFINITIVE, SOLID, PERFECT                                 | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 4: **0.5410** | AUDITS, BACKGROUND, HISTORY, PAST                                 | INCORRECT (Max overlap: 3/4 with EXPERIENCE)

### Top Candidate Groups:
   - Group 1: **0.6025** | LATE, AUDITS, ABSENT, EXCUSED                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 2: **0.5962** | MINION, DODGERS, PHEW, LIFE                                       | INCORRECT (Max overlap: 2/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 3: **0.5717** | GREAT, INFINITIVE, SOLID, PERFECT                                 | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 4: **0.5613** | BACKGROUND, HISTORY, PRESENT, PAST                                | INCORRECT (Max overlap: 3/4 with EXPERIENCE)
   - Group 5: **0.5874** | AUDITS, ABSENT, EXCUSED, PRESENT                                  | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 6: **0.5485** | LATE, BACKGROUND, HISTORY, PAST                                   | INCORRECT (Max overlap: 3/4 with EXPERIENCE)
   - Group 7: **0.5709** | GREAT, SOLID, PHEW, PERFECT                                       | CORRECT GROUP (COMMENTARY ABOUT YOUR CONNECTIONS RESULTS, Level 2)
   - Group 8: **0.5610** | MINION, INFINITIVE, DODGERS, LIFE                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 9: **0.5658** | MINION, INFINITIVE, DODGERS, PHEW                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 10: **0.5639** | GREAT, SOLID, PERFECT, LIFE                                       | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 11: **0.6338** | LATE, ABSENT, EXCUSED, PRESENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1)
   - Group 12: **0.5410** | AUDITS, BACKGROUND, HISTORY, PAST                                 | INCORRECT (Max overlap: 3/4 with EXPERIENCE)
   - Group 13: **0.5701** | BACKGROUND, EXCUSED, HISTORY, PAST                                | INCORRECT (Max overlap: 3/4 with EXPERIENCE)
   - Group 14: **0.5462** | LATE, AUDITS, ABSENT, PRESENT                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 15: **0.5619** | INFINITIVE, DODGERS, PHEW, LIFE                                   | INCORRECT (Max overlap: 2/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 16: **0.5400** | MINION, GREAT, SOLID, PERFECT                                     | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 17: **0.6453** | LATE, ABSENT, PRESENT, PAST                                       | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 18: **0.5165** | AUDITS, BACKGROUND, EXCUSED, HISTORY                              | INCORRECT (Max overlap: 2/4 with EXPERIENCE)
   - Group 19: **0.5934** | MINION, DODGERS, SOLID, PHEW                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 20: **0.5099** | GREAT, INFINITIVE, PERFECT, LIFE                                  | INCORRECT (Max overlap: 2/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)

---

## Puzzle 90 (ID: 567)
**Words on Board:** STRAND, MAROON, RUBY, BEACH, BRICK, PAIR, HEAD, LOCATION, FUR, YOU, LOCK, WISP, CHERRY, TIME, DURATION, DATE

### Ground Truth Categories:
* **Level 0 (SHADES OF RED) [Type: SEMANTIC_SET]:** BRICK, CHERRY, MAROON, RUBY
* **Level 1 (APPOINTMENT SPECIFICATIONS) [Type: SEMANTIC_SET]:** DATE, DURATION, LOCATION, TIME
* **Level 2 (DIFFERENT AMOUNTS OF HAIR) [Type: SEMANTIC_SET]:** HEAD, LOCK, STRAND, WISP
* **Level 3 (TREE HOMOPHONES) [Type: SOUND_OR_SPELLING]:** BEACH, FUR, PAIR, YOU

### Top Candidate Partitions:
1. **Partition Score: 0.4542**
   - Group 1: **0.5004** | FUR, YOU, WISP, CHERRY                                            | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 2: **0.4887** | RUBY, BRICK, HEAD, LOCK                                           | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 3: **0.4691** | STRAND, MAROON, BEACH, PAIR                                       | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 4: **0.4295** | LOCATION, TIME, DURATION, DATE                                    | CORRECT GROUP (APPOINTMENT SPECIFICATIONS, Level 1)
2. **Partition Score: 0.4501**
   - Group 1: **0.5278** | BRICK, PAIR, HEAD, LOCK                                           | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 2: **0.5004** | FUR, YOU, WISP, CHERRY                                            | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 3: **0.4408** | STRAND, MAROON, RUBY, BEACH                                       | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 4: **0.4295** | LOCATION, TIME, DURATION, DATE                                    | CORRECT GROUP (APPOINTMENT SPECIFICATIONS, Level 1)
3. **Partition Score: 0.4452**
   - Group 1: **0.5004** | FUR, YOU, WISP, CHERRY                                            | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 2: **0.4902** | STRAND, PAIR, HEAD, LOCK                                          | INCORRECT (Max overlap: 3/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 3: **0.4317** | MAROON, RUBY, BEACH, BRICK                                        | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 4: **0.4295** | LOCATION, TIME, DURATION, DATE                                    | CORRECT GROUP (APPOINTMENT SPECIFICATIONS, Level 1)
4. **Partition Score: 0.4426**
   - Group 1: **0.5004** | FUR, YOU, WISP, CHERRY                                            | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 2: **0.4939** | STRAND, MAROON, BEACH, BRICK                                      | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 3: **0.4295** | LOCATION, TIME, DURATION, DATE                                    | CORRECT GROUP (APPOINTMENT SPECIFICATIONS, Level 1)
   - Group 4: **0.4235** | RUBY, PAIR, HEAD, LOCK                                            | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
5. **Partition Score: 0.4417**
   - Group 1: **0.5004** | FUR, YOU, WISP, CHERRY                                            | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 2: **0.4985** | RUBY, BRICK, PAIR, LOCK                                           | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 3: **0.4295** | LOCATION, TIME, DURATION, DATE                                    | CORRECT GROUP (APPOINTMENT SPECIFICATIONS, Level 1)
   - Group 4: **0.4194** | STRAND, MAROON, BEACH, HEAD                                       | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)

### Top Candidate Groups:
   - Group 1: **0.5004** | FUR, YOU, WISP, CHERRY                                            | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 2: **0.4887** | RUBY, BRICK, HEAD, LOCK                                           | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 3: **0.4691** | STRAND, MAROON, BEACH, PAIR                                       | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 4: **0.4295** | LOCATION, TIME, DURATION, DATE                                    | CORRECT GROUP (APPOINTMENT SPECIFICATIONS, Level 1)
   - Group 5: **0.5278** | BRICK, PAIR, HEAD, LOCK                                           | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 6: **0.4408** | STRAND, MAROON, RUBY, BEACH                                       | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 7: **0.4902** | STRAND, PAIR, HEAD, LOCK                                          | INCORRECT (Max overlap: 3/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 8: **0.4317** | MAROON, RUBY, BEACH, BRICK                                        | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 9: **0.4939** | STRAND, MAROON, BEACH, BRICK                                      | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 10: **0.4235** | RUBY, PAIR, HEAD, LOCK                                            | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 11: **0.4985** | RUBY, BRICK, PAIR, LOCK                                           | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 12: **0.4194** | STRAND, MAROON, BEACH, HEAD                                       | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 13: **0.4648** | STRAND, BEACH, HEAD, LOCATION                                     | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 14: **0.4417** | MAROON, RUBY, BRICK, PAIR                                         | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 15: **0.4287** | LOCK, TIME, DURATION, DATE                                        | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 16: **0.4474** | STRAND, BEACH, HEAD, LOCK                                         | INCORRECT (Max overlap: 3/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 17: **0.4250** | RUBY, BRICK, HEAD, LOCATION                                       | INCORRECT (Max overlap: 2/4 with SHADES OF RED)
   - Group 18: **0.4796** | PAIR, HEAD, LOCK, CHERRY                                          | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 19: **0.4367** | BRICK, FUR, YOU, WISP                                             | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 20: **0.4332** | RUBY, HEAD, LOCK, CHERRY                                          | INCORRECT (Max overlap: 2/4 with SHADES OF RED)

---

## Puzzle 91 (ID: 258)
**Words on Board:** WINE, RIND, HEAVY, WINK, WIND, MILL, SEED, FEATHER, FACTORY, STEM, LIGHT, SHOP, WING, CORE, MIDDLE, PLANT

### Ground Truth Categories:
* **Level 0 (MANUFACTURING LOCATIONS) [Type: SYNONYM_OR_NEAR]:** FACTORY, MILL, PLANT, SHOP
* **Level 1 (WIN + LETTER) [Type: WORDPLAY_TRANSFORM]:** WIND, WINE, WING, WINK
* **Level 2 (PARTS OF FRUIT YOU MIGHT NOT EAT) [Type: SEMANTIC_SET]:** CORE, RIND, SEED, STEM
* **Level 3 (WEIGHTS IN BOXING) [Type: NAMED_ENTITY_SET]:** FEATHER, HEAVY, LIGHT, MIDDLE

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7102** | RIND, WIND, FEATHER, WING                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 2: **0.6765** | WINK, WIND, FEATHER, WING                                         | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 3: **0.6627** | RIND, WINK, WIND, WING                                            | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 4: **0.6466** | WINE, WIND, FEATHER, WING                                         | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 5: **0.6436** | WINE, RIND, WIND, WING                                            | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 6: **0.6102** | RIND, WINK, WIND, FEATHER                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 7: **0.6074** | WINE, RIND, FEATHER, WING                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 8: **0.6059** | RIND, WINK, FEATHER, WING                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 9: **0.5987** | WINE, WINK, WIND, WING                                            | CORRECT GROUP (WIN + LETTER, Level 1)
   - Group 10: **0.5952** | WINE, RIND, WIND, FEATHER                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 11: **0.5922** | WIND, FEATHER, SHOP, WING                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 12: **0.5918** | HEAVY, WIND, FEATHER, WING                                        | INCORRECT (Max overlap: 2/4 with WEIGHTS IN BOXING)
   - Group 13: **0.5896** | WINE, HEAVY, LIGHT, SHOP                                          | INCORRECT (Max overlap: 2/4 with WEIGHTS IN BOXING)
   - Group 14: **0.5805** | SEED, STEM, MIDDLE, PLANT                                         | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 15: **0.5704** | HEAVY, LIGHT, SHOP, MIDDLE                                        | INCORRECT (Max overlap: 3/4 with WEIGHTS IN BOXING)
   - Group 16: **0.5693** | HEAVY, LIGHT, MIDDLE, PLANT                                       | INCORRECT (Max overlap: 3/4 with WEIGHTS IN BOXING)
   - Group 17: **0.5670** | WINE, WIND, SHOP, WING                                            | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 18: **0.5670** | WINE, WINK, WIND, FEATHER                                         | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 19: **0.5670** | WINE, RIND, WINK, WING                                            | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 20: **0.5664** | WINE, RIND, WINK, WIND                                            | INCORRECT (Max overlap: 3/4 with WIN + LETTER)

---

## Puzzle 92 (ID: 1062)
**Words on Board:** HOAGIE, FILTERS, DONUT, ARGUMENT, BELLY, CROP, CAUSE, GROUNDS, BEAN, GRINDER, HERO, MARKUP, ADJUST, BASIS, ROLL, SUB

### Ground Truth Categories:
* **Level 0 (LONG SANDWICH) [Type: SYNONYM_OR_NEAR]:** GRINDER, HERO, HOAGIE, SUB
* **Level 1 (PRETEXT) [Type: SYNONYM_OR_NEAR]:** ARGUMENT, BASIS, CAUSE, GROUNDS
* **Level 2 (SMARTPHONE PHOTO EDITING OPTIONS) [Type: SEMANTIC_SET]:** ADJUST, CROP, FILTERS, MARKUP
* **Level 3 (JELLY ___) [Type: FILL_IN_THE_BLANK]:** BEAN, BELLY, DONUT, ROLL

### Top Candidate Partitions:
1. **Partition Score: 0.5632**
   - Group 1: **0.9564** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0)
   - Group 2: **0.6040** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 3: **0.5517** | DONUT, BELLY, BEAN, ROLL                                          | CORRECT GROUP (JELLY ___, Level 3)
   - Group 4: **0.5486** | FILTERS, CROP, MARKUP, ADJUST                                     | CORRECT GROUP (SMARTPHONE PHOTO EDITING OPTIONS, Level 2)
2. **Partition Score: 0.5344**
   - Group 1: **0.5517** | DONUT, BELLY, BEAN, ROLL                                          | CORRECT GROUP (JELLY ___, Level 3)
   - Group 2: **0.5486** | FILTERS, CROP, MARKUP, ADJUST                                     | CORRECT GROUP (SMARTPHONE PHOTO EDITING OPTIONS, Level 2)
   - Group 3: **0.5364** | HOAGIE, ARGUMENT, GRINDER, HERO                                   | INCORRECT (Max overlap: 3/4 with LONG SANDWICH)
   - Group 4: **0.5262** | CAUSE, GROUNDS, BASIS, SUB                                        | INCORRECT (Max overlap: 3/4 with PRETEXT)
3. **Partition Score: 0.5220**
   - Group 1: **0.6040** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 2: **0.5517** | DONUT, BELLY, BEAN, ROLL                                          | CORRECT GROUP (JELLY ___, Level 3)
   - Group 3: **0.5367** | HOAGIE, HERO, MARKUP, SUB                                         | INCORRECT (Max overlap: 3/4 with LONG SANDWICH)
   - Group 4: **0.4998** | FILTERS, CROP, GRINDER, ADJUST                                    | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
4. **Partition Score: 0.5161**
   - Group 1: **0.9564** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0)
   - Group 2: **0.6040** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 3: **0.5993** | DONUT, BELLY, CROP, BEAN                                          | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 4: **0.4305** | FILTERS, MARKUP, ADJUST, ROLL                                     | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
5. **Partition Score: 0.5153**
   - Group 1: **0.9564** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0)
   - Group 2: **0.6040** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 3: **0.5401** | BELLY, CROP, BEAN, ROLL                                           | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 4: **0.4586** | FILTERS, DONUT, MARKUP, ADJUST                                    | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)

### Top Candidate Groups:
   - Group 1: **0.9564** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0)
   - Group 2: **0.6040** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 3: **0.5517** | DONUT, BELLY, BEAN, ROLL                                          | CORRECT GROUP (JELLY ___, Level 3)
   - Group 4: **0.5486** | FILTERS, CROP, MARKUP, ADJUST                                     | CORRECT GROUP (SMARTPHONE PHOTO EDITING OPTIONS, Level 2)
   - Group 5: **0.5364** | HOAGIE, ARGUMENT, GRINDER, HERO                                   | INCORRECT (Max overlap: 3/4 with LONG SANDWICH)
   - Group 6: **0.5262** | CAUSE, GROUNDS, BASIS, SUB                                        | INCORRECT (Max overlap: 3/4 with PRETEXT)
   - Group 7: **0.5367** | HOAGIE, HERO, MARKUP, SUB                                         | INCORRECT (Max overlap: 3/4 with LONG SANDWICH)
   - Group 8: **0.4998** | FILTERS, CROP, GRINDER, ADJUST                                    | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 9: **0.5993** | DONUT, BELLY, CROP, BEAN                                          | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 10: **0.4305** | FILTERS, MARKUP, ADJUST, ROLL                                     | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 11: **0.5401** | BELLY, CROP, BEAN, ROLL                                           | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 12: **0.4586** | FILTERS, DONUT, MARKUP, ADJUST                                    | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 13: **0.4589** | FILTERS, GRINDER, ADJUST, ROLL                                    | INCORRECT (Max overlap: 2/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 14: **0.5432** | GRINDER, HERO, MARKUP, SUB                                        | INCORRECT (Max overlap: 3/4 with LONG SANDWICH)
   - Group 15: **0.5145** | FILTERS, CROP, ADJUST, ROLL                                       | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 16: **0.4960** | HOAGIE, DONUT, BELLY, BEAN                                        | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 17: **0.4614** | DONUT, BELLY, BEAN, MARKUP                                        | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 18: **0.5795** | HOAGIE, CROP, GRINDER, HERO                                       | INCORRECT (Max overlap: 3/4 with LONG SANDWICH)
   - Group 19: **0.4798** | FILTERS, ARGUMENT, MARKUP, ADJUST                                 | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 20: **0.5475** | DONUT, CROP, BEAN, ROLL                                           | INCORRECT (Max overlap: 3/4 with JELLY ___)

---

## Puzzle 93 (ID: 480)
**Words on Board:** PUNCH, SMITE, STICK, PRUNE, POT, MILK, JUICE, SOCK, SODA, WATER, BOOKEND, FERTILIZE, SKI, PANT, EARBUD, BLOUSE

### Ground Truth Categories:
* **Level 0 (BEVERAGES) [Type: SEMANTIC_SET]:** JUICE, MILK, PUNCH, SODA
* **Level 1 (CARE FOR A PLANT) [Type: SEMANTIC_SET]:** FERTILIZE, POT, PRUNE, WATER
* **Level 2 (ITEM SOLD IN PAIRS) [Type: SEMANTIC_SET]:** BOOKEND, EARBUD, SKI, SOCK
* **Level 3 (BUGS PLUS STARTING LETTER) [Type: WORDPLAY_TRANSFORM]:** BLOUSE, PANT, SMITE, STICK

### Top Candidate Partitions:
1. **Partition Score: 0.4751**
   - Group 1: **0.4802** | SODA, WATER, SKI, PANT                                            | INCORRECT (Max overlap: 1/4 with BEVERAGES)
   - Group 2: **0.4791** | PUNCH, SMITE, JUICE, SOCK                                         | INCORRECT (Max overlap: 2/4 with BEVERAGES)
   - Group 3: **0.4785** | BOOKEND, FERTILIZE, EARBUD, BLOUSE                                | INCORRECT (Max overlap: 2/4 with ITEM SOLD IN PAIRS)
   - Group 4: **0.4714** | STICK, PRUNE, POT, MILK                                           | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)

### Top Candidate Groups:
   - Group 1: **0.4802** | SODA, WATER, SKI, PANT                                            | INCORRECT (Max overlap: 1/4 with BEVERAGES)
   - Group 2: **0.4791** | PUNCH, SMITE, JUICE, SOCK                                         | INCORRECT (Max overlap: 2/4 with BEVERAGES)
   - Group 3: **0.4785** | BOOKEND, FERTILIZE, EARBUD, BLOUSE                                | INCORRECT (Max overlap: 2/4 with ITEM SOLD IN PAIRS)
   - Group 4: **0.4714** | STICK, PRUNE, POT, MILK                                           | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)

---

## Puzzle 94 (ID: 976)
**Words on Board:** LESSON, COLORS, KENT, RESEED, SHEER, STARK, FLAG, STANDARD, CAMEL, BANNER, PURE, SYNC, UTTER, WAYNE, SALEM, PARLIAMENT

### Ground Truth Categories:
* **Level 0 (DOWNRIGHT) [Type: SYNONYM_OR_NEAR]:** PURE, SHEER, STARK, UTTER
* **Level 1 (PENNANT) [Type: SYNONYM_OR_NEAR]:** BANNER, COLORS, FLAG, STANDARD
* **Level 2 (CIGARETTE BRANDS) [Type: NAMED_ENTITY_SET]:** CAMEL, KENT, PARLIAMENT, SALEM
* **Level 3 (HOMOPHONES OF WAYS TO GET SMALLER) [Type: SOUND_OR_SPELLING]:** LESSON, RESEED, SYNC, WAYNE

### Top Candidate Partitions:
1. **Partition Score: 0.5791**
   - Group 1: **0.6853** | SHEER, STARK, PURE, UTTER                                         | CORRECT GROUP (DOWNRIGHT, Level 0)
   - Group 2: **0.6528** | KENT, WAYNE, SALEM, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 3: **0.5637** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1)
   - Group 4: **0.5500** | LESSON, RESEED, CAMEL, SYNC                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
2. **Partition Score: 0.5477**
   - Group 1: **0.7070** | KENT, CAMEL, WAYNE, SALEM                                         | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 2: **0.6853** | SHEER, STARK, PURE, UTTER                                         | CORRECT GROUP (DOWNRIGHT, Level 0)
   - Group 3: **0.5637** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1)
   - Group 4: **0.4708** | LESSON, RESEED, SYNC, PARLIAMENT                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
3. **Partition Score: 0.5441**
   - Group 1: **0.6528** | KENT, WAYNE, SALEM, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 2: **0.5715** | COLORS, STARK, FLAG, BANNER                                       | INCORRECT (Max overlap: 3/4 with PENNANT)
   - Group 3: **0.5500** | LESSON, RESEED, CAMEL, SYNC                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 4: **0.5275** | SHEER, STANDARD, PURE, UTTER                                      | INCORRECT (Max overlap: 3/4 with DOWNRIGHT)
4. **Partition Score: 0.5348**
   - Group 1: **0.6853** | SHEER, STARK, PURE, UTTER                                         | CORRECT GROUP (DOWNRIGHT, Level 0)
   - Group 2: **0.6524** | KENT, CAMEL, SALEM, PARLIAMENT                                    | CORRECT GROUP (CIGARETTE BRANDS, Level 2)
   - Group 3: **0.5637** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1)
   - Group 4: **0.4617** | LESSON, RESEED, SYNC, WAYNE                                       | CORRECT GROUP (HOMOPHONES OF WAYS TO GET SMALLER, Level 3)
5. **Partition Score: 0.5312**
   - Group 1: **0.6853** | SHEER, STARK, PURE, UTTER                                         | CORRECT GROUP (DOWNRIGHT, Level 0)
   - Group 2: **0.6488** | KENT, CAMEL, WAYNE, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 3: **0.5637** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1)
   - Group 4: **0.4562** | LESSON, RESEED, SYNC, SALEM                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)

### Top Candidate Groups:
   - Group 1: **0.6853** | SHEER, STARK, PURE, UTTER                                         | CORRECT GROUP (DOWNRIGHT, Level 0)
   - Group 2: **0.6528** | KENT, WAYNE, SALEM, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 3: **0.5637** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1)
   - Group 4: **0.5500** | LESSON, RESEED, CAMEL, SYNC                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 5: **0.7070** | KENT, CAMEL, WAYNE, SALEM                                         | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 6: **0.4708** | LESSON, RESEED, SYNC, PARLIAMENT                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 7: **0.5715** | COLORS, STARK, FLAG, BANNER                                       | INCORRECT (Max overlap: 3/4 with PENNANT)
   - Group 8: **0.5275** | SHEER, STANDARD, PURE, UTTER                                      | INCORRECT (Max overlap: 3/4 with DOWNRIGHT)
   - Group 9: **0.6524** | KENT, CAMEL, SALEM, PARLIAMENT                                    | CORRECT GROUP (CIGARETTE BRANDS, Level 2)
   - Group 10: **0.4617** | LESSON, RESEED, SYNC, WAYNE                                       | CORRECT GROUP (HOMOPHONES OF WAYS TO GET SMALLER, Level 3)
   - Group 11: **0.6488** | KENT, CAMEL, WAYNE, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 12: **0.4562** | LESSON, RESEED, SYNC, SALEM                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 13: **0.6537** | CAMEL, WAYNE, SALEM, PARLIAMENT                                   | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 14: **0.4455** | LESSON, KENT, RESEED, SYNC                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 15: **0.5955** | LESSON, STARK, CAMEL, SYNC                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 16: **0.4681** | COLORS, RESEED, FLAG, BANNER                                      | INCORRECT (Max overlap: 3/4 with PENNANT)
   - Group 17: **0.6078** | KENT, SYNC, WAYNE, SALEM                                          | INCORRECT (Max overlap: 2/4 with CIGARETTE BRANDS)
   - Group 18: **0.4425** | LESSON, RESEED, CAMEL, PARLIAMENT                                 | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 19: **0.5899** | KENT, SYNC, WAYNE, PARLIAMENT                                     | INCORRECT (Max overlap: 2/4 with CIGARETTE BRANDS)
   - Group 20: **0.4389** | LESSON, RESEED, CAMEL, SALEM                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)

---

## Puzzle 95 (ID: 391)
**Words on Board:** CELL, JUG, BOTTLE, MOBILE, FREEZE, CRIB, ATOM, RATTLE, SAW, PHONE, DOG, PROTEIN, SPOONS, WASHBOARD, MOLECULE, PRICE

### Ground Truth Categories:
* **Level 0 (BIOLOGICAL BUILDING BLOCKS) [Type: SEMANTIC_SET]:** ATOM, CELL, MOLECULE, PROTEIN
* **Level 1 (PURCHASES FOR A BABY) [Type: SEMANTIC_SET]:** BOTTLE, CRIB, MOBILE, RATTLE
* **Level 2 (OBJECTS PLAYED AS INSTRUMENTS) [Type: SEMANTIC_SET]:** JUG, SAW, SPOONS, WASHBOARD
* **Level 3 (___ TAG) [Type: FILL_IN_THE_BLANK]:** DOG, FREEZE, PHONE, PRICE

### Top Candidate Partitions:
1. **Partition Score: 0.5021**
   - Group 1: **0.5285** | CELL, ATOM, PROTEIN, MOLECULE                                     | CORRECT GROUP (BIOLOGICAL BUILDING BLOCKS, Level 0)
   - Group 2: **0.5194** | JUG, BOTTLE, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 3: **0.5193** | RATTLE, SAW, DOG, PRICE                                           | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 4: **0.4849** | MOBILE, FREEZE, CRIB, PHONE                                       | INCORRECT (Max overlap: 2/4 with PURCHASES FOR A BABY)
2. **Partition Score: 0.4907**
   - Group 1: **0.5531** | JUG, BOTTLE, SPOONS, PRICE                                        | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 2: **0.5285** | CELL, ATOM, PROTEIN, MOLECULE                                     | CORRECT GROUP (BIOLOGICAL BUILDING BLOCKS, Level 0)
   - Group 3: **0.4849** | MOBILE, FREEZE, CRIB, PHONE                                       | INCORRECT (Max overlap: 2/4 with PURCHASES FOR A BABY)
   - Group 4: **0.4748** | RATTLE, SAW, DOG, WASHBOARD                                       | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
3. **Partition Score: 0.4872**
   - Group 1: **0.5285** | CELL, ATOM, PROTEIN, MOLECULE                                     | CORRECT GROUP (BIOLOGICAL BUILDING BLOCKS, Level 0)
   - Group 2: **0.5020** | JUG, RATTLE, DOG, PRICE                                           | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 3: **0.4868** | BOTTLE, MOBILE, CRIB, PHONE                                       | INCORRECT (Max overlap: 3/4 with PURCHASES FOR A BABY)
   - Group 4: **0.4801** | FREEZE, SAW, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS)
4. **Partition Score: 0.4847**
   - Group 1: **0.5285** | CELL, ATOM, PROTEIN, MOLECULE                                     | CORRECT GROUP (BIOLOGICAL BUILDING BLOCKS, Level 0)
   - Group 2: **0.5020** | JUG, RATTLE, DOG, PRICE                                           | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 3: **0.4997** | FREEZE, CRIB, SAW, WASHBOARD                                      | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 4: **0.4686** | BOTTLE, MOBILE, PHONE, SPOONS                                     | INCORRECT (Max overlap: 2/4 with PURCHASES FOR A BABY)
5. **Partition Score: 0.4844**
   - Group 1: **0.5285** | CELL, ATOM, PROTEIN, MOLECULE                                     | CORRECT GROUP (BIOLOGICAL BUILDING BLOCKS, Level 0)
   - Group 2: **0.5071** | JUG, SAW, DOG, PRICE                                              | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 3: **0.4868** | BOTTLE, MOBILE, CRIB, PHONE                                       | INCORRECT (Max overlap: 3/4 with PURCHASES FOR A BABY)
   - Group 4: **0.4719** | FREEZE, RATTLE, SPOONS, WASHBOARD                                 | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)

### Top Candidate Groups:
   - Group 1: **0.5285** | CELL, ATOM, PROTEIN, MOLECULE                                     | CORRECT GROUP (BIOLOGICAL BUILDING BLOCKS, Level 0)
   - Group 2: **0.5194** | JUG, BOTTLE, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 3: **0.5193** | RATTLE, SAW, DOG, PRICE                                           | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 4: **0.4849** | MOBILE, FREEZE, CRIB, PHONE                                       | INCORRECT (Max overlap: 2/4 with PURCHASES FOR A BABY)
   - Group 5: **0.5531** | JUG, BOTTLE, SPOONS, PRICE                                        | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 6: **0.4748** | RATTLE, SAW, DOG, WASHBOARD                                       | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 7: **0.5020** | JUG, RATTLE, DOG, PRICE                                           | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 8: **0.4868** | BOTTLE, MOBILE, CRIB, PHONE                                       | INCORRECT (Max overlap: 3/4 with PURCHASES FOR A BABY)
   - Group 9: **0.4801** | FREEZE, SAW, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 10: **0.4997** | FREEZE, CRIB, SAW, WASHBOARD                                      | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 11: **0.4686** | BOTTLE, MOBILE, PHONE, SPOONS                                     | INCORRECT (Max overlap: 2/4 with PURCHASES FOR A BABY)
   - Group 12: **0.5071** | JUG, SAW, DOG, PRICE                                              | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 13: **0.4719** | FREEZE, RATTLE, SPOONS, WASHBOARD                                 | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 14: **0.5242** | FREEZE, RATTLE, SAW, PRICE                                        | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 15: **0.4576** | JUG, DOG, SPOONS, WASHBOARD                                       | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 16: **0.4626** | JUG, CRIB, DOG, WASHBOARD                                         | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 17: **0.4741** | JUG, FREEZE, SPOONS, PRICE                                        | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 18: **0.4854** | RATTLE, SAW, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 19: **0.4694** | JUG, BOTTLE, DOG, PRICE                                           | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 20: **0.5072** | RATTLE, DOG, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)

---

## Puzzle 96 (ID: 395)
**Words on Board:** SASS, BASS, ATTITUDE, PROSPECT, LIP, BRIDGE, LENS, RIM, FORECAST, TEMPLE, FLUKE, PERCH, OUTLOOK, CHANCE, CHEEK, PIKE

### Ground Truth Categories:
* **Level 0 (FUTURE LIKELIHOOD) [Type: SYNONYM_OR_NEAR]:** CHANCE, FORECAST, OUTLOOK, PROSPECT
* **Level 1 (BACK TALK) [Type: SYNONYM_OR_NEAR]:** ATTITUDE, CHEEK, LIP, SASS
* **Level 2 (FISH) [Type: SEMANTIC_SET]:** BASS, FLUKE, PERCH, PIKE
* **Level 3 (COMPONENTS OF EYEGLASSES) [Type: SEMANTIC_SET]:** BRIDGE, LENS, RIM, TEMPLE

### Top Candidate Partitions:
1. **Partition Score: 0.4414**
   - Group 1: **0.7114** | ATTITUDE, PROSPECT, FORECAST, OUTLOOK                             | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD)
   - Group 2: **0.6892** | BASS, BRIDGE, PERCH, PIKE                                         | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 3: **0.4486** | SASS, LIP, FLUKE, CHANCE                                          | INCORRECT (Max overlap: 2/4 with BACK TALK)
   - Group 4: **0.3139** | LENS, RIM, TEMPLE, CHEEK                                          | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES)
2. **Partition Score: 0.4193**
   - Group 1: **0.6892** | BASS, BRIDGE, PERCH, PIKE                                         | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 2: **0.6239** | PROSPECT, FORECAST, OUTLOOK, CHANCE                               | CORRECT GROUP (FUTURE LIKELIHOOD, Level 0)
   - Group 3: **0.4252** | SASS, ATTITUDE, LIP, FLUKE                                        | INCORRECT (Max overlap: 3/4 with BACK TALK)
   - Group 4: **0.3139** | LENS, RIM, TEMPLE, CHEEK                                          | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES)
3. **Partition Score: 0.4189**
   - Group 1: **0.5552** | PROSPECT, FORECAST, FLUKE, CHANCE                                 | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD)
   - Group 2: **0.5354** | BASS, LENS, PERCH, PIKE                                           | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 3: **0.4769** | SASS, ATTITUDE, LIP, OUTLOOK                                      | INCORRECT (Max overlap: 3/4 with BACK TALK)
   - Group 4: **0.3315** | BRIDGE, RIM, TEMPLE, CHEEK                                        | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES)
4. **Partition Score: 0.4155**
   - Group 1: **0.5549** | SASS, ATTITUDE, FORECAST, OUTLOOK                                 | INCORRECT (Max overlap: 2/4 with BACK TALK)
   - Group 2: **0.5354** | BASS, LENS, PERCH, PIKE                                           | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 3: **0.4636** | PROSPECT, LIP, FLUKE, CHANCE                                      | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD)
   - Group 4: **0.3315** | BRIDGE, RIM, TEMPLE, CHEEK                                        | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES)
5. **Partition Score: 0.4150**
   - Group 1: **0.6892** | BASS, BRIDGE, PERCH, PIKE                                         | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 2: **0.5552** | PROSPECT, FORECAST, FLUKE, CHANCE                                 | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD)
   - Group 3: **0.4769** | SASS, ATTITUDE, LIP, OUTLOOK                                      | INCORRECT (Max overlap: 3/4 with BACK TALK)
   - Group 4: **0.3139** | LENS, RIM, TEMPLE, CHEEK                                          | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES)

### Top Candidate Groups:
   - Group 1: **0.7114** | ATTITUDE, PROSPECT, FORECAST, OUTLOOK                             | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD)
   - Group 2: **0.6892** | BASS, BRIDGE, PERCH, PIKE                                         | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 3: **0.4486** | SASS, LIP, FLUKE, CHANCE                                          | INCORRECT (Max overlap: 2/4 with BACK TALK)
   - Group 4: **0.3139** | LENS, RIM, TEMPLE, CHEEK                                          | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES)
   - Group 5: **0.6239** | PROSPECT, FORECAST, OUTLOOK, CHANCE                               | CORRECT GROUP (FUTURE LIKELIHOOD, Level 0)
   - Group 6: **0.4252** | SASS, ATTITUDE, LIP, FLUKE                                        | INCORRECT (Max overlap: 3/4 with BACK TALK)
   - Group 7: **0.5552** | PROSPECT, FORECAST, FLUKE, CHANCE                                 | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD)
   - Group 8: **0.5354** | BASS, LENS, PERCH, PIKE                                           | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 9: **0.4769** | SASS, ATTITUDE, LIP, OUTLOOK                                      | INCORRECT (Max overlap: 3/4 with BACK TALK)
   - Group 10: **0.3315** | BRIDGE, RIM, TEMPLE, CHEEK                                        | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES)
   - Group 11: **0.5549** | SASS, ATTITUDE, FORECAST, OUTLOOK                                 | INCORRECT (Max overlap: 2/4 with BACK TALK)
   - Group 12: **0.4636** | PROSPECT, LIP, FLUKE, CHANCE                                      | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD)
   - Group 13: **0.5991** | ATTITUDE, PROSPECT, FLUKE, CHANCE                                 | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD)
   - Group 14: **0.4330** | SASS, LIP, FORECAST, OUTLOOK                                      | INCORRECT (Max overlap: 2/4 with BACK TALK)
   - Group 15: **0.4970** | ATTITUDE, FORECAST, FLUKE, OUTLOOK                                | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD)
   - Group 16: **0.4753** | SASS, PROSPECT, LIP, CHANCE                                       | INCORRECT (Max overlap: 2/4 with BACK TALK)
   - Group 17: **0.5572** | PROSPECT, FLUKE, OUTLOOK, CHANCE                                  | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD)
   - Group 18: **0.4344** | SASS, ATTITUDE, LIP, FORECAST                                     | INCORRECT (Max overlap: 3/4 with BACK TALK)
   - Group 19: **0.5027** | ATTITUDE, FORECAST, FLUKE, CHANCE                                 | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD)
   - Group 20: **0.4665** | SASS, PROSPECT, LIP, OUTLOOK                                      | INCORRECT (Max overlap: 2/4 with BACK TALK)

---

## Puzzle 97 (ID: 1026)
**Words on Board:** HOLES, HOEDOWN, MALLET, WICKET, HOP, MOLE, CONCERN, OLIVES, CAROUSER, RAVE, EVITE, TIMER, SHARE, CLAIM, STAKE, BALL

### Ground Truth Categories:
* **Level 0 (EVENTS WITH DANCING) [Type: SEMANTIC_SET]:** BALL, HOEDOWN, HOP, RAVE
* **Level 1 (INTEREST) [Type: SYNONYM_OR_NEAR]:** CLAIM, CONCERN, SHARE, STAKE
* **Level 2 (COMPONENTS OF WHAC-A-MOLE) [Type: SEMANTIC_SET]:** HOLES, MALLET, MOLE, TIMER
* **Level 3 (MUSICALS WITH LAST LETTER CHANGED) [Type: WORDPLAY_TRANSFORM]:** CAROUSER, EVITE, OLIVES, WICKET

### Top Candidate Partitions:
1. **Partition Score: 0.4995**
   - Group 1: **0.5908** | CAROUSER, EVITE, TIMER, CLAIM                                     | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 2: **0.5302** | CONCERN, RAVE, SHARE, STAKE                                       | INCORRECT (Max overlap: 3/4 with INTEREST)
   - Group 3: **0.4935** | MALLET, WICKET, HOP, BALL                                         | INCORRECT (Max overlap: 2/4 with EVENTS WITH DANCING)
   - Group 4: **0.4873** | HOLES, HOEDOWN, MOLE, OLIVES                                      | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
2. **Partition Score: 0.4994**
   - Group 1: **0.5929** | MALLET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING)
   - Group 2: **0.5908** | CAROUSER, EVITE, TIMER, CLAIM                                     | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 3: **0.4873** | HOLES, HOEDOWN, MOLE, OLIVES                                      | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 4: **0.4598** | WICKET, CONCERN, SHARE, STAKE                                     | INCORRECT (Max overlap: 3/4 with INTEREST)
3. **Partition Score: 0.4993**
   - Group 1: **0.5711** | HOEDOWN, CAROUSER, TIMER, CLAIM                                   | INCORRECT (Max overlap: 1/4 with EVENTS WITH DANCING)
   - Group 2: **0.5302** | CONCERN, RAVE, SHARE, STAKE                                       | INCORRECT (Max overlap: 3/4 with INTEREST)
   - Group 3: **0.4935** | MALLET, WICKET, HOP, BALL                                         | INCORRECT (Max overlap: 2/4 with EVENTS WITH DANCING)
   - Group 4: **0.4869** | HOLES, MOLE, OLIVES, EVITE                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
4. **Partition Score: 0.4991**
   - Group 1: **0.5932** | HOEDOWN, EVITE, TIMER, CLAIM                                      | INCORRECT (Max overlap: 1/4 with EVENTS WITH DANCING)
   - Group 2: **0.5929** | MALLET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING)
   - Group 3: **0.4840** | HOLES, MOLE, OLIVES, CAROUSER                                     | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 4: **0.4598** | WICKET, CONCERN, SHARE, STAKE                                     | INCORRECT (Max overlap: 3/4 with INTEREST)
5. **Partition Score: 0.4988**
   - Group 1: **0.6041** | HOEDOWN, CAROUSER, EVITE, TIMER                                   | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 2: **0.5929** | MALLET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING)
   - Group 3: **0.4829** | HOLES, MOLE, OLIVES, CLAIM                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 4: **0.4598** | WICKET, CONCERN, SHARE, STAKE                                     | INCORRECT (Max overlap: 3/4 with INTEREST)

### Top Candidate Groups:
   - Group 1: **0.5908** | CAROUSER, EVITE, TIMER, CLAIM                                     | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 2: **0.5302** | CONCERN, RAVE, SHARE, STAKE                                       | INCORRECT (Max overlap: 3/4 with INTEREST)
   - Group 3: **0.4935** | MALLET, WICKET, HOP, BALL                                         | INCORRECT (Max overlap: 2/4 with EVENTS WITH DANCING)
   - Group 4: **0.4873** | HOLES, HOEDOWN, MOLE, OLIVES                                      | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 5: **0.5929** | MALLET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING)
   - Group 6: **0.4598** | WICKET, CONCERN, SHARE, STAKE                                     | INCORRECT (Max overlap: 3/4 with INTEREST)
   - Group 7: **0.5711** | HOEDOWN, CAROUSER, TIMER, CLAIM                                   | INCORRECT (Max overlap: 1/4 with EVENTS WITH DANCING)
   - Group 8: **0.4869** | HOLES, MOLE, OLIVES, EVITE                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 9: **0.5932** | HOEDOWN, EVITE, TIMER, CLAIM                                      | INCORRECT (Max overlap: 1/4 with EVENTS WITH DANCING)
   - Group 10: **0.4840** | HOLES, MOLE, OLIVES, CAROUSER                                     | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 11: **0.6041** | HOEDOWN, CAROUSER, EVITE, TIMER                                   | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 12: **0.4829** | HOLES, MOLE, OLIVES, CLAIM                                        | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 13: **0.5514** | WICKET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING)
   - Group 14: **0.4757** | MALLET, CONCERN, SHARE, STAKE                                     | INCORRECT (Max overlap: 3/4 with INTEREST)
   - Group 15: **0.5152** | MALLET, WICKET, RAVE, BALL                                        | INCORRECT (Max overlap: 2/4 with EVENTS WITH DANCING)
   - Group 16: **0.4958** | HOP, CONCERN, SHARE, STAKE                                        | INCORRECT (Max overlap: 3/4 with INTEREST)
   - Group 17: **0.4800** | CONCERN, SHARE, CLAIM, STAKE                                      | CORRECT GROUP (INTEREST, Level 1)
   - Group 18: **0.4455** | HOLES, WICKET, MOLE, OLIVES                                       | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 19: **0.6147** | HOEDOWN, CAROUSER, EVITE, CLAIM                                   | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 20: **0.4550** | HOLES, MOLE, OLIVES, TIMER                                        | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE)

---

## Puzzle 98 (ID: 611)
**Words on Board:** JACK, KNEE, BOLSTER, TUG, NIGHT, BUB, HUB, YANK, MAN, JERK, BLOCK, BUD, MAD, WRENCH, MAT, STRAP

### Ground Truth Categories:
* **Level 0 (WREST) [Type: SYNONYM_OR_NEAR]:** JERK, TUG, WRENCH, YANK
* **Level 1 (BUSTER) [Type: FILL_IN_THE_BLANK]:** BUB, BUD, JACK, MAN
* **Level 2 (YOGA ACCESSORIES) [Type: SEMANTIC_SET]:** BLOCK, BOLSTER, MAT, STRAP
* **Level 3 (___CAP) [Type: FILL_IN_THE_BLANK]:** HUB, KNEE, MAD, NIGHT

### Top Candidate Partitions:
1. **Partition Score: 0.5873**
   - Group 1: **0.6528** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0)
   - Group 2: **0.6234** | JACK, NIGHT, MAN, MAD                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.6016** | KNEE, BOLSTER, BLOCK, STRAP                                       | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)
   - Group 4: **0.5622** | BUB, HUB, BUD, MAT                                                | INCORRECT (Max overlap: 2/4 with BUSTER)
2. **Partition Score: 0.5830**
   - Group 1: **0.6528** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0)
   - Group 2: **0.6234** | JACK, NIGHT, MAN, MAD                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.6048** | HUB, BLOCK, BUD, MAT                                              | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 4: **0.5519** | KNEE, BOLSTER, BUB, STRAP                                         | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
3. **Partition Score: 0.5816**
   - Group 1: **0.6528** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0)
   - Group 2: **0.6234** | JACK, NIGHT, MAN, MAD                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.6125** | BOLSTER, BUB, BUD, STRAP                                          | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 4: **0.5453** | KNEE, HUB, BLOCK, MAT                                             | INCORRECT (Max overlap: 2/4 with ___CAP)
4. **Partition Score: 0.5794**
   - Group 1: **0.6528** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0)
   - Group 2: **0.6234** | JACK, NIGHT, MAN, MAD                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.5705** | HUB, BUD, MAT, STRAP                                              | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 4: **0.5619** | KNEE, BOLSTER, BUB, BLOCK                                         | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
5. **Partition Score: 0.5737**
   - Group 1: **0.6528** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0)
   - Group 2: **0.6234** | JACK, NIGHT, MAN, MAD                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.5790** | KNEE, BUB, HUB, BLOCK                                             | INCORRECT (Max overlap: 2/4 with ___CAP)
   - Group 4: **0.5461** | BOLSTER, BUD, MAT, STRAP                                          | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)

### Top Candidate Groups:
   - Group 1: **0.6528** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0)
   - Group 2: **0.6234** | JACK, NIGHT, MAN, MAD                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.6016** | KNEE, BOLSTER, BLOCK, STRAP                                       | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)
   - Group 4: **0.5622** | BUB, HUB, BUD, MAT                                                | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 5: **0.6048** | HUB, BLOCK, BUD, MAT                                              | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 6: **0.5519** | KNEE, BOLSTER, BUB, STRAP                                         | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 7: **0.6125** | BOLSTER, BUB, BUD, STRAP                                          | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 8: **0.5453** | KNEE, HUB, BLOCK, MAT                                             | INCORRECT (Max overlap: 2/4 with ___CAP)
   - Group 9: **0.5705** | HUB, BUD, MAT, STRAP                                              | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 10: **0.5619** | KNEE, BOLSTER, BUB, BLOCK                                         | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 11: **0.5790** | KNEE, BUB, HUB, BLOCK                                             | INCORRECT (Max overlap: 2/4 with ___CAP)
   - Group 12: **0.5461** | BOLSTER, BUD, MAT, STRAP                                          | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)
   - Group 13: **0.6266** | BOLSTER, BUB, BLOCK, BUD                                          | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 14: **0.5192** | KNEE, HUB, MAT, STRAP                                             | INCORRECT (Max overlap: 2/4 with ___CAP)
   - Group 15: **0.6525** | BOLSTER, BLOCK, BUD, STRAP                                        | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)
   - Group 16: **0.5053** | KNEE, BUB, HUB, MAT                                               | INCORRECT (Max overlap: 2/4 with ___CAP)
   - Group 17: **0.6017** | BUB, BUD, MAD, MAT                                                | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 18: **0.5359** | JACK, NIGHT, HUB, MAN                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 19: **0.5941** | HUB, BUD, MAD, MAT                                                | INCORRECT (Max overlap: 2/4 with ___CAP)
   - Group 20: **0.5395** | JACK, NIGHT, BUB, MAN                                             | INCORRECT (Max overlap: 3/4 with BUSTER)

---

## Puzzle 99 (ID: 433)
**Words on Board:** TONGUE, PRAIRIE, SPEECH, COTTAGE, TAPE, BANDAGE, RANCH, FRENCH, KISS, DRESSING, CRAFTSMAN, DIALECT, LANGUAGE, NECK, SCISSORS, MAKE OUT

### Ground Truth Categories:
* **Level 0 (SPOKEN COMMUNICATION) [Type: SEMANTIC_SET]:** DIALECT, LANGUAGE, SPEECH, TONGUE
* **Level 1 (CANOODLE) [Type: SYNONYM_OR_NEAR]:** FRENCH, KISS, MAKE OUT, NECK
* **Level 2 (FIRST AID KIT ITEMS) [Type: SEMANTIC_SET]:** BANDAGE, DRESSING, SCISSORS, TAPE
* **Level 3 (HOUSE STYLES) [Type: SEMANTIC_SET]:** COTTAGE, CRAFTSMAN, PRAIRIE, RANCH

### Top Candidate Partitions:
1. **Partition Score: 0.6122**
   - Group 1: **0.7245** | TONGUE, KISS, NECK, MAKE OUT                                      | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 2: **0.6804** | SPEECH, FRENCH, DIALECT, LANGUAGE                                 | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 3: **0.5935** | PRAIRIE, COTTAGE, CRAFTSMAN, SCISSORS                             | INCORRECT (Max overlap: 3/4 with HOUSE STYLES)
   - Group 4: **0.5874** | TAPE, BANDAGE, RANCH, DRESSING                                    | INCORRECT (Max overlap: 3/4 with FIRST AID KIT ITEMS)
2. **Partition Score: 0.6022**
   - Group 1: **0.9036** | TONGUE, SPEECH, DIALECT, LANGUAGE                                 | CORRECT GROUP (SPOKEN COMMUNICATION, Level 0)
   - Group 2: **0.6405** | FRENCH, KISS, NECK, MAKE OUT                                      | CORRECT GROUP (CANOODLE, Level 1)
   - Group 3: **0.5935** | PRAIRIE, COTTAGE, CRAFTSMAN, SCISSORS                             | INCORRECT (Max overlap: 3/4 with HOUSE STYLES)
   - Group 4: **0.5874** | TAPE, BANDAGE, RANCH, DRESSING                                    | INCORRECT (Max overlap: 3/4 with FIRST AID KIT ITEMS)
3. **Partition Score: 0.5902**
   - Group 1: **0.6600** | TONGUE, SPEECH, FRENCH, LANGUAGE                                  | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 2: **0.5935** | PRAIRIE, COTTAGE, CRAFTSMAN, SCISSORS                             | INCORRECT (Max overlap: 3/4 with HOUSE STYLES)
   - Group 3: **0.5925** | KISS, DIALECT, NECK, MAKE OUT                                     | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 4: **0.5874** | TAPE, BANDAGE, RANCH, DRESSING                                    | INCORRECT (Max overlap: 3/4 with FIRST AID KIT ITEMS)
4. **Partition Score: 0.5613**
   - Group 1: **0.5935** | PRAIRIE, COTTAGE, CRAFTSMAN, SCISSORS                             | INCORRECT (Max overlap: 3/4 with HOUSE STYLES)
   - Group 2: **0.5880** | TONGUE, SPEECH, LANGUAGE, NECK                                    | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 3: **0.5874** | TAPE, BANDAGE, RANCH, DRESSING                                    | INCORRECT (Max overlap: 3/4 with FIRST AID KIT ITEMS)
   - Group 4: **0.5349** | FRENCH, KISS, DIALECT, MAKE OUT                                   | INCORRECT (Max overlap: 3/4 with CANOODLE)
5. **Partition Score: 0.5588**
   - Group 1: **0.9036** | TONGUE, SPEECH, DIALECT, LANGUAGE                                 | CORRECT GROUP (SPOKEN COMMUNICATION, Level 0)
   - Group 2: **0.5935** | PRAIRIE, COTTAGE, CRAFTSMAN, SCISSORS                             | INCORRECT (Max overlap: 3/4 with HOUSE STYLES)
   - Group 3: **0.5520** | TAPE, RANCH, FRENCH, DRESSING                                     | INCORRECT (Max overlap: 2/4 with FIRST AID KIT ITEMS)
   - Group 4: **0.5449** | BANDAGE, KISS, NECK, MAKE OUT                                     | INCORRECT (Max overlap: 3/4 with CANOODLE)

### Top Candidate Groups:
   - Group 1: **0.7245** | TONGUE, KISS, NECK, MAKE OUT                                      | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 2: **0.6804** | SPEECH, FRENCH, DIALECT, LANGUAGE                                 | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 3: **0.5935** | PRAIRIE, COTTAGE, CRAFTSMAN, SCISSORS                             | INCORRECT (Max overlap: 3/4 with HOUSE STYLES)
   - Group 4: **0.5874** | TAPE, BANDAGE, RANCH, DRESSING                                    | INCORRECT (Max overlap: 3/4 with FIRST AID KIT ITEMS)
   - Group 5: **0.9036** | TONGUE, SPEECH, DIALECT, LANGUAGE                                 | CORRECT GROUP (SPOKEN COMMUNICATION, Level 0)
   - Group 6: **0.6405** | FRENCH, KISS, NECK, MAKE OUT                                      | CORRECT GROUP (CANOODLE, Level 1)
   - Group 7: **0.6600** | TONGUE, SPEECH, FRENCH, LANGUAGE                                  | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 8: **0.5925** | KISS, DIALECT, NECK, MAKE OUT                                     | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 9: **0.5880** | TONGUE, SPEECH, LANGUAGE, NECK                                    | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 10: **0.5349** | FRENCH, KISS, DIALECT, MAKE OUT                                   | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 11: **0.5520** | TAPE, RANCH, FRENCH, DRESSING                                     | INCORRECT (Max overlap: 2/4 with FIRST AID KIT ITEMS)
   - Group 12: **0.5449** | BANDAGE, KISS, NECK, MAKE OUT                                     | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 13: **0.5734** | TONGUE, FRENCH, KISS, MAKE OUT                                    | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 14: **0.5341** | SPEECH, DIALECT, LANGUAGE, NECK                                   | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 15: **0.5564** | TAPE, KISS, NECK, MAKE OUT                                        | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 16: **0.5392** | BANDAGE, RANCH, FRENCH, DRESSING                                  | INCORRECT (Max overlap: 2/4 with FIRST AID KIT ITEMS)
   - Group 17: **0.7439** | TONGUE, FRENCH, KISS, NECK                                        | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 18: **0.5216** | SPEECH, DIALECT, LANGUAGE, MAKE OUT                               | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 19: **0.5467** | TONGUE, SPEECH, KISS, LANGUAGE                                    | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 20: **0.5395** | FRENCH, DIALECT, NECK, MAKE OUT                                   | INCORRECT (Max overlap: 3/4 with CANOODLE)

---

## Puzzle 100 (ID: 1073)
**Words on Board:** HERB, STRIKE, SHED, MARCH, ITSY, RALLY, STABLE, HISS, DRUM, PEN, MYA, MASK, PICKET, COOP, STAFF, RATTLE

### Ground Truth Categories:
* **Level 0 (FARM FIXTURES) [Type: SEMANTIC_SET]:** COOP, PEN, SHED, STABLE
* **Level 1 (LABOR PROTEST ACTIONS) [Type: SEMANTIC_SET]:** MARCH, PICKET, RALLY, STRIKE
* **Level 2 (OBJECTS USED IN RITUAL PERFORMANCES) [Type: SEMANTIC_SET]:** DRUM, MASK, RATTLE, STAFF
* **Level 3 (POSSESSIVE ADJECTIVES PLUS A LETTER) [Type: WORDPLAY_TRANSFORM]:** HERB, HISS, ITSY, MYA

### Top Candidate Partitions:
1. **Partition Score: 0.4780**
   - Group 1: **0.5823** | HERB, ITSY, MYA, STAFF                                            | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 2: **0.5392** | STRIKE, MARCH, HISS, PICKET                                       | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 3: **0.4637** | SHED, RALLY, STABLE, MASK                                         | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
   - Group 4: **0.4546** | DRUM, PEN, COOP, RATTLE                                           | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
2. **Partition Score: 0.4725**
   - Group 1: **0.4829** | MARCH, HISS, PICKET, RATTLE                                       | INCORRECT (Max overlap: 2/4 with LABOR PROTEST ACTIONS)
   - Group 2: **0.4827** | ITSY, MYA, COOP, STAFF                                            | INCORRECT (Max overlap: 2/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 3: **0.4732** | HERB, SHED, DRUM, PEN                                             | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
   - Group 4: **0.4671** | STRIKE, RALLY, STABLE, MASK                                       | INCORRECT (Max overlap: 2/4 with LABOR PROTEST ACTIONS)
3. **Partition Score: 0.4697**
   - Group 1: **0.5392** | STRIKE, MARCH, HISS, PICKET                                       | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 2: **0.4782** | DRUM, PEN, STAFF, RATTLE                                          | INCORRECT (Max overlap: 3/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 3: **0.4731** | HERB, ITSY, MYA, COOP                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 4: **0.4637** | SHED, RALLY, STABLE, MASK                                         | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
4. **Partition Score: 0.4690**
   - Group 1: **0.4829** | MARCH, HISS, PICKET, RATTLE                                       | INCORRECT (Max overlap: 2/4 with LABOR PROTEST ACTIONS)
   - Group 2: **0.4827** | ITSY, MYA, COOP, STAFF                                            | INCORRECT (Max overlap: 2/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 3: **0.4659** | HERB, STRIKE, DRUM, PEN                                           | INCORRECT (Max overlap: 1/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 4: **0.4637** | SHED, RALLY, STABLE, MASK                                         | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
5. **Partition Score: 0.4681**
   - Group 1: **0.5392** | STRIKE, MARCH, HISS, PICKET                                       | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 2: **0.4759** | ITSY, MYA, STAFF, RATTLE                                          | INCORRECT (Max overlap: 2/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 3: **0.4690** | HERB, DRUM, PEN, COOP                                             | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
   - Group 4: **0.4637** | SHED, RALLY, STABLE, MASK                                         | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)

### Top Candidate Groups:
   - Group 1: **0.5823** | HERB, ITSY, MYA, STAFF                                            | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 2: **0.5392** | STRIKE, MARCH, HISS, PICKET                                       | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 3: **0.4637** | SHED, RALLY, STABLE, MASK                                         | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
   - Group 4: **0.4546** | DRUM, PEN, COOP, RATTLE                                           | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 5: **0.4829** | MARCH, HISS, PICKET, RATTLE                                       | INCORRECT (Max overlap: 2/4 with LABOR PROTEST ACTIONS)
   - Group 6: **0.4827** | ITSY, MYA, COOP, STAFF                                            | INCORRECT (Max overlap: 2/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 7: **0.4732** | HERB, SHED, DRUM, PEN                                             | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
   - Group 8: **0.4671** | STRIKE, RALLY, STABLE, MASK                                       | INCORRECT (Max overlap: 2/4 with LABOR PROTEST ACTIONS)
   - Group 9: **0.4782** | DRUM, PEN, STAFF, RATTLE                                          | INCORRECT (Max overlap: 3/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 10: **0.4731** | HERB, ITSY, MYA, COOP                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 11: **0.4659** | HERB, STRIKE, DRUM, PEN                                           | INCORRECT (Max overlap: 1/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 12: **0.4759** | ITSY, MYA, STAFF, RATTLE                                          | INCORRECT (Max overlap: 2/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 13: **0.4690** | HERB, DRUM, PEN, COOP                                             | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
   - Group 14: **0.4764** | STRIKE, MARCH, HISS, RATTLE                                       | INCORRECT (Max overlap: 2/4 with LABOR PROTEST ACTIONS)
   - Group 15: **0.4754** | HERB, ITSY, DRUM, MYA                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 16: **0.4661** | PEN, PICKET, COOP, STAFF                                          | INCORRECT (Max overlap: 2/4 with FARM FIXTURES)
   - Group 17: **0.4919** | HISS, DRUM, STAFF, RATTLE                                         | INCORRECT (Max overlap: 3/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 18: **0.4643** | STRIKE, MARCH, PEN, PICKET                                        | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 19: **0.4704** | HERB, HISS, DRUM, RATTLE                                          | INCORRECT (Max overlap: 2/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 20: **0.5340** | STRIKE, MARCH, PICKET, RATTLE                                     | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)

---

## Puzzle 101 (ID: 812)
**Words on Board:** FLAME, DRUM, BASH, FIDDLE, PIECES, COORDINATE, FISH, AXES, ROAST, CHOP, CARDS, BOARD, DOES, BASS, DICE, BLAST

### Ground Truth Categories:
* **Level 0 (CRITICIZE HARSHLY) [Type: SYNONYM_OR_NEAR]:** BASH, BLAST, FLAME, ROAST
* **Level 1 (COMMON COMPONENTS OF BOARD GAMES) [Type: SEMANTIC_SET]:** BOARD, CARDS, DICE, PIECES
* **Level 2 (HETERONYMS) [Type: SOUND_OR_SPELLING]:** AXES, BASS, COORDINATE, DOES
* **Level 3 (___STICKS) [Type: FILL_IN_THE_BLANK]:** CHOP, DRUM, FIDDLE, FISH

### Top Candidate Partitions:
1. **Partition Score: 0.5406**
   - Group 1: **0.5801** | FIDDLE, PIECES, CHOP, DOES                                        | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 2: **0.5728** | DRUM, BASH, FISH, BASS                                            | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 3: **0.5327** | AXES, CARDS, BOARD, DICE                                          | INCORRECT (Max overlap: 3/4 with COMMON COMPONENTS OF BOARD GAMES)
   - Group 4: **0.5284** | FLAME, COORDINATE, ROAST, BLAST                                   | INCORRECT (Max overlap: 3/4 with CRITICIZE HARSHLY)
2. **Partition Score: 0.5205**
   - Group 1: **0.6373** | DRUM, FIDDLE, FISH, BASS                                          | INCORRECT (Max overlap: 3/4 with ___STICKS)
   - Group 2: **0.5327** | AXES, CARDS, BOARD, DICE                                          | INCORRECT (Max overlap: 3/4 with COMMON COMPONENTS OF BOARD GAMES)
   - Group 3: **0.5284** | FLAME, COORDINATE, ROAST, BLAST                                   | INCORRECT (Max overlap: 3/4 with CRITICIZE HARSHLY)
   - Group 4: **0.5104** | BASH, PIECES, CHOP, DOES                                          | INCORRECT (Max overlap: 1/4 with CRITICIZE HARSHLY)
3. **Partition Score: 0.5204**
   - Group 1: **0.6373** | DRUM, FIDDLE, FISH, BASS                                          | INCORRECT (Max overlap: 3/4 with ___STICKS)
   - Group 2: **0.5505** | BASH, PIECES, DOES, BLAST                                         | INCORRECT (Max overlap: 2/4 with CRITICIZE HARSHLY)
   - Group 3: **0.5327** | AXES, CARDS, BOARD, DICE                                          | INCORRECT (Max overlap: 3/4 with COMMON COMPONENTS OF BOARD GAMES)
   - Group 4: **0.4993** | FLAME, COORDINATE, ROAST, CHOP                                    | INCORRECT (Max overlap: 2/4 with CRITICIZE HARSHLY)
4. **Partition Score: 0.5147**
   - Group 1: **0.5728** | DRUM, BASH, FISH, BASS                                            | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 2: **0.5472** | AXES, CHOP, DOES, DICE                                            | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 3: **0.5284** | FLAME, COORDINATE, ROAST, BLAST                                   | INCORRECT (Max overlap: 3/4 with CRITICIZE HARSHLY)
   - Group 4: **0.4916** | FIDDLE, PIECES, CARDS, BOARD                                      | INCORRECT (Max overlap: 3/4 with COMMON COMPONENTS OF BOARD GAMES)
5. **Partition Score: 0.5116**
   - Group 1: **0.5728** | DRUM, BASH, FISH, BASS                                            | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 2: **0.5327** | AXES, CARDS, BOARD, DICE                                          | INCORRECT (Max overlap: 3/4 with COMMON COMPONENTS OF BOARD GAMES)
   - Group 3: **0.5152** | FIDDLE, PIECES, DOES, BLAST                                       | INCORRECT (Max overlap: 1/4 with ___STICKS)
   - Group 4: **0.4993** | FLAME, COORDINATE, ROAST, CHOP                                    | INCORRECT (Max overlap: 2/4 with CRITICIZE HARSHLY)

### Top Candidate Groups:
   - Group 1: **0.5801** | FIDDLE, PIECES, CHOP, DOES                                        | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 2: **0.5728** | DRUM, BASH, FISH, BASS                                            | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 3: **0.5327** | AXES, CARDS, BOARD, DICE                                          | INCORRECT (Max overlap: 3/4 with COMMON COMPONENTS OF BOARD GAMES)
   - Group 4: **0.5284** | FLAME, COORDINATE, ROAST, BLAST                                   | INCORRECT (Max overlap: 3/4 with CRITICIZE HARSHLY)
   - Group 5: **0.6373** | DRUM, FIDDLE, FISH, BASS                                          | INCORRECT (Max overlap: 3/4 with ___STICKS)
   - Group 6: **0.5104** | BASH, PIECES, CHOP, DOES                                          | INCORRECT (Max overlap: 1/4 with CRITICIZE HARSHLY)
   - Group 7: **0.5505** | BASH, PIECES, DOES, BLAST                                         | INCORRECT (Max overlap: 2/4 with CRITICIZE HARSHLY)
   - Group 8: **0.4993** | FLAME, COORDINATE, ROAST, CHOP                                    | INCORRECT (Max overlap: 2/4 with CRITICIZE HARSHLY)
   - Group 9: **0.5472** | AXES, CHOP, DOES, DICE                                            | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 10: **0.4916** | FIDDLE, PIECES, CARDS, BOARD                                      | INCORRECT (Max overlap: 3/4 with COMMON COMPONENTS OF BOARD GAMES)
   - Group 11: **0.5152** | FIDDLE, PIECES, DOES, BLAST                                       | INCORRECT (Max overlap: 1/4 with ___STICKS)
   - Group 12: **0.5465** | FLAME, COORDINATE, AXES, ROAST                                    | INCORRECT (Max overlap: 2/4 with CRITICIZE HARSHLY)
   - Group 13: **0.4742** | CHOP, CARDS, BOARD, DICE                                          | INCORRECT (Max overlap: 3/4 with COMMON COMPONENTS OF BOARD GAMES)
   - Group 14: **0.5140** | CHOP, DOES, DICE, BLAST                                           | INCORRECT (Max overlap: 1/4 with ___STICKS)
   - Group 15: **0.5613** | FIDDLE, PIECES, CHOP, DICE                                        | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 16: **0.5127** | DRUM, FISH, CARDS, BOARD                                          | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 17: **0.4911** | BASH, DOES, BASS, BLAST                                           | INCORRECT (Max overlap: 2/4 with CRITICIZE HARSHLY)
   - Group 18: **0.5515** | PIECES, CHOP, DICE, BLAST                                         | INCORRECT (Max overlap: 2/4 with COMMON COMPONENTS OF BOARD GAMES)
   - Group 19: **0.5038** | DRUM, FIDDLE, CARDS, BOARD                                        | INCORRECT (Max overlap: 2/4 with ___STICKS)
   - Group 20: **0.4956** | BASH, FISH, DOES, BASS                                            | INCORRECT (Max overlap: 2/4 with HETERONYMS)

---

## Puzzle 102 (ID: 1049)
**Words on Board:** STRING, ROOM, PHASE, SHADOW, SOCK, ROLL, ORDERS, ROUND, BOOM, HAND, CLAP, RUMBLE, STAGE, LEVEL, JOKE, OVATION

### Ground Truth Categories:
* **Level 0 (STEP IN A PROCESS) [Type: SYNONYM_OR_NEAR]:** LEVEL, PHASE, ROUND, STAGE
* **Level 1 (SOUND LIKE THUNDER) [Type: SEMANTIC_SET]:** BOOM, CLAP, ROLL, RUMBLE
* **Level 2 (KINDS OF PUPPETS) [Type: SEMANTIC_SET]:** HAND, SHADOW, SOCK, STRING
* **Level 3 (STANDING ___) [Type: FILL_IN_THE_BLANK]:** JOKE, ORDERS, OVATION, ROOM

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7253** | STRING, ROOM, SOCK, HAND                                          | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 2: **0.6656** | SOCK, BOOM, CLAP, RUMBLE                                          | INCORRECT (Max overlap: 3/4 with SOUND LIKE THUNDER)
   - Group 3: **0.6581** | SOCK, BOOM, HAND, CLAP                                            | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 4: **0.6565** | ROLL, BOOM, CLAP, RUMBLE                                          | CORRECT GROUP (SOUND LIKE THUNDER, Level 1)
   - Group 5: **0.6348** | ROOM, SOCK, BOOM, HAND                                            | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 6: **0.6340** | ROOM, SOCK, HAND, OVATION                                         | INCORRECT (Max overlap: 2/4 with STANDING ___)
   - Group 7: **0.6314** | STRING, ROOM, HAND, OVATION                                       | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 8: **0.6278** | ROOM, SOCK, BOOM, JOKE                                            | INCORRECT (Max overlap: 2/4 with STANDING ___)
   - Group 9: **0.6277** | ROOM, SOCK, HAND, JOKE                                            | INCORRECT (Max overlap: 2/4 with STANDING ___)
   - Group 10: **0.6264** | STRING, SOCK, BOOM, HAND                                          | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 11: **0.6186** | STRING, ROOM, SHADOW, SOCK                                        | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 12: **0.6158** | STRING, ROOM, SOCK, BOOM                                          | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 13: **0.6121** | SOCK, BOOM, CLAP, JOKE                                            | INCORRECT (Max overlap: 2/4 with SOUND LIKE THUNDER)
   - Group 14: **0.6094** | STRING, SOCK, HAND, OVATION                                       | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 15: **0.6050** | STRING, SOCK, HAND, JOKE                                          | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 16: **0.6032** | STRING, ROOM, SOCK, OVATION                                       | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 17: **0.5995** | STRING, SHADOW, SOCK, HAND                                        | CORRECT GROUP (KINDS OF PUPPETS, Level 2)
   - Group 18: **0.5988** | STRING, ROOM, HAND, JOKE                                          | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 19: **0.5983** | ROOM, SOCK, BOOM, CLAP                                            | INCORRECT (Max overlap: 2/4 with SOUND LIKE THUNDER)
   - Group 20: **0.5942** | STRING, ROOM, SOCK, JOKE                                          | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)

---

## Puzzle 103 (ID: 643)
**Words on Board:** TONIGHT, SUE, PEG, MOVE, STRING, BARB, NEEDLE, SERVE, BRIDGE, BRISTLE, SPINE, MIGHT, NECK, CHARGE, WISH, MAY

### Ground Truth Categories:
* **Level 0 (SHARP PROTRUSION) [Type: SEMANTIC_SET]:** BARB, BRISTLE, NEEDLE, SPINE
* **Level 1 (FEATURES OF STRINGED INSTRUMENTS) [Type: SEMANTIC_SET]:** BRIDGE, NECK, PEG, STRING
* **Level 2 (LITIGATION VERBS) [Type: SEMANTIC_SET]:** CHARGE, MOVE, SERVE, SUE
* **Level 3 (IN “STAR LIGHT, STAR BRIGHT”) [Type: FILL_IN_THE_BLANK]:** MAY, MIGHT, TONIGHT, WISH

### Top Candidate Partitions:
1. **Partition Score: 0.5315**
   - Group 1: **0.6119** | STRING, BARB, BRIDGE, BRISTLE                                     | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 2: **0.5933** | SUE, MOVE, SERVE, CHARGE                                          | CORRECT GROUP (LITIGATION VERBS, Level 2)
   - Group 3: **0.5772** | PEG, NEEDLE, SPINE, NECK                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 4: **0.4777** | TONIGHT, MIGHT, WISH, MAY                                         | CORRECT GROUP (IN “STAR LIGHT, STAR BRIGHT”, Level 3)
2. **Partition Score: 0.5285**
   - Group 1: **0.6263** | STRING, BARB, BRISTLE, CHARGE                                     | INCORRECT (Max overlap: 2/4 with SHARP PROTRUSION)
   - Group 2: **0.5813** | SUE, MOVE, SERVE, BRIDGE                                          | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 3: **0.5772** | PEG, NEEDLE, SPINE, NECK                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 4: **0.4777** | TONIGHT, MIGHT, WISH, MAY                                         | CORRECT GROUP (IN “STAR LIGHT, STAR BRIGHT”, Level 3)
3. **Partition Score: 0.5154**
   - Group 1: **0.5933** | SUE, MOVE, SERVE, CHARGE                                          | CORRECT GROUP (LITIGATION VERBS, Level 2)
   - Group 2: **0.5730** | PEG, STRING, BARB, BRISTLE                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 3: **0.5334** | NEEDLE, BRIDGE, SPINE, NECK                                       | INCORRECT (Max overlap: 2/4 with SHARP PROTRUSION)
   - Group 4: **0.4777** | TONIGHT, MIGHT, WISH, MAY                                         | CORRECT GROUP (IN “STAR LIGHT, STAR BRIGHT”, Level 3)
4. **Partition Score: 0.5066**
   - Group 1: **0.6082** | PEG, STRING, BARB, BRIDGE                                         | INCORRECT (Max overlap: 3/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 2: **0.5933** | SUE, MOVE, SERVE, CHARGE                                          | CORRECT GROUP (LITIGATION VERBS, Level 2)
   - Group 3: **0.4777** | TONIGHT, MIGHT, WISH, MAY                                         | CORRECT GROUP (IN “STAR LIGHT, STAR BRIGHT”, Level 3)
   - Group 4: **0.4777** | NEEDLE, BRISTLE, SPINE, NECK                                      | INCORRECT (Max overlap: 3/4 with SHARP PROTRUSION)
5. **Partition Score: 0.5036**
   - Group 1: **0.6138** | PEG, STRING, BARB, CHARGE                                         | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 2: **0.5813** | SUE, MOVE, SERVE, BRIDGE                                          | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 3: **0.4777** | TONIGHT, MIGHT, WISH, MAY                                         | CORRECT GROUP (IN “STAR LIGHT, STAR BRIGHT”, Level 3)
   - Group 4: **0.4777** | NEEDLE, BRISTLE, SPINE, NECK                                      | INCORRECT (Max overlap: 3/4 with SHARP PROTRUSION)

### Top Candidate Groups:
   - Group 1: **0.6119** | STRING, BARB, BRIDGE, BRISTLE                                     | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 2: **0.5933** | SUE, MOVE, SERVE, CHARGE                                          | CORRECT GROUP (LITIGATION VERBS, Level 2)
   - Group 3: **0.5772** | PEG, NEEDLE, SPINE, NECK                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 4: **0.4777** | TONIGHT, MIGHT, WISH, MAY                                         | CORRECT GROUP (IN “STAR LIGHT, STAR BRIGHT”, Level 3)
   - Group 5: **0.6263** | STRING, BARB, BRISTLE, CHARGE                                     | INCORRECT (Max overlap: 2/4 with SHARP PROTRUSION)
   - Group 6: **0.5813** | SUE, MOVE, SERVE, BRIDGE                                          | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 7: **0.5730** | PEG, STRING, BARB, BRISTLE                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 8: **0.5334** | NEEDLE, BRIDGE, SPINE, NECK                                       | INCORRECT (Max overlap: 2/4 with SHARP PROTRUSION)
   - Group 9: **0.6082** | PEG, STRING, BARB, BRIDGE                                         | INCORRECT (Max overlap: 3/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 10: **0.4777** | NEEDLE, BRISTLE, SPINE, NECK                                      | INCORRECT (Max overlap: 3/4 with SHARP PROTRUSION)
   - Group 11: **0.6138** | PEG, STRING, BARB, CHARGE                                         | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 12: **0.5390** | STRING, BARB, SERVE, BRISTLE                                      | INCORRECT (Max overlap: 2/4 with SHARP PROTRUSION)
   - Group 13: **0.5173** | SUE, MOVE, BRIDGE, CHARGE                                         | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 14: **0.5646** | STRING, NEEDLE, SPINE, NECK                                       | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 15: **0.4876** | PEG, BARB, BRIDGE, BRISTLE                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 16: **0.5139** | SUE, PEG, MOVE, SERVE                                             | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 17: **0.5603** | MOVE, SERVE, BRIDGE, CHARGE                                       | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 18: **0.4857** | SUE, NEEDLE, SPINE, NECK                                          | INCORRECT (Max overlap: 2/4 with SHARP PROTRUSION)
   - Group 19: **0.5304** | STRING, BARB, BRISTLE, NECK                                       | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 20: **0.5106** | PEG, NEEDLE, BRIDGE, SPINE                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)

---

## Puzzle 104 (ID: 157)
**Words on Board:** HAI, WE, O, W, DA, ICK, US, JA, WEE, SI, OK, OUI, EW, PU, UGH, WII

### Ground Truth Categories:
* **Level 0 (“GROSS!”) [Type: SYNONYM_OR_NEAR]:** EW, ICK, PU, UGH
* **Level 1 (MAGAZINES) [Type: NAMED_ENTITY_SET]:** O, OK, US, W
* **Level 2 (“YES” IN DIFFERENT LANGUAGES) [Type: SYNONYM_OR_NEAR]:** HAI, JA, SI, DA
* **Level 3 (HOMOPHONES) [Type: SOUND_OR_SPELLING]:** OUI, WE, WEE, WII

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6802** | HAI, DA, JA, OUI                                                  | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 2: **0.6425** | O, DA, SI, PU                                                     | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 3: **0.6385** | O, US, SI, PU                                                     | INCORRECT (Max overlap: 2/4 with MAGAZINES)
   - Group 4: **0.6253** | HAI, DA, SI, OUI                                                  | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 5: **0.6175** | HAI, DA, JA, SI                                                   | CORRECT GROUP (“YES” IN DIFFERENT LANGUAGES, Level 2)
   - Group 6: **0.6143** | O, W, US, PU                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 7: **0.6121** | O, SI, OUI, PU                                                    | INCORRECT (Max overlap: 1/4 with MAGAZINES)
   - Group 8: **0.6048** | O, DA, SI, OUI                                                    | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 9: **0.6047** | DA, JA, SI, OUI                                                   | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 10: **0.6046** | DA, JA, OK, OUI                                                   | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 11: **0.6019** | HAI, JA, SI, OUI                                                  | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 12: **0.5997** | O, W, DA, US                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 13: **0.5991** | O, DA, OK, OUI                                                    | INCORRECT (Max overlap: 2/4 with MAGAZINES)
   - Group 14: **0.5952** | O, DA, US, SI                                                     | INCORRECT (Max overlap: 2/4 with MAGAZINES)
   - Group 15: **0.5951** | DA, JA, SI, PU                                                    | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 16: **0.5927** | DA, SI, OUI, PU                                                   | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 17: **0.5895** | HAI, JA, OUI, WII                                                 | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 18: **0.5892** | O, DA, OUI, PU                                                    | INCORRECT (Max overlap: 1/4 with MAGAZINES)
   - Group 19: **0.5872** | O, W, US, SI                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 20: **0.5859** | O, SI, OK, PU                                                     | INCORRECT (Max overlap: 2/4 with MAGAZINES)

---

## Puzzle 105 (ID: 113)
**Words on Board:** SALUTE, DOWN, MAPS, FINGER, FUR, STAND, KNEEL, MAIL, NOTES, HINT, CLOCK, SHELL, ARROW, DOG, SCALES, BOW

### Ground Truth Categories:
* **Level 0 (WAYS TO SHOW RESPECT) [Type: SEMANTIC_SET]:** BOW, KNEEL, SALUTE, STAND
* **Level 1 (IPHONE APPS) [Type: NAMED_ENTITY_SET]:** CLOCK, MAIL, MAPS, NOTES
* **Level 2 (ANIMAL COVERINGS) [Type: SEMANTIC_SET]:** DOWN, FUR, SCALES, SHELL
* **Level 3 (“POINTERS”) [Type: SEMANTIC_SET]:** ARROW, DOG, FINGER, HINT

### Top Candidate Partitions:
1. **Partition Score: 0.4897**
   - Group 1: **0.5484** | MAPS, FUR, MAIL, ARROW                                            | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 2: **0.5457** | NOTES, CLOCK, SHELL, SCALES                                       | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 3: **0.4777** | SALUTE, DOWN, FINGER, KNEEL                                       | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 4: **0.4676** | STAND, HINT, DOG, BOW                                             | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
2. **Partition Score: 0.4868**
   - Group 1: **0.5492** | MAPS, FUR, MAIL, SHELL                                            | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 2: **0.4987** | HINT, ARROW, DOG, BOW                                             | INCORRECT (Max overlap: 3/4 with “POINTERS”)
   - Group 3: **0.4932** | STAND, NOTES, CLOCK, SCALES                                       | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 4: **0.4777** | SALUTE, DOWN, FINGER, KNEEL                                       | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
3. **Partition Score: 0.4862**
   - Group 1: **0.4987** | HINT, ARROW, DOG, BOW                                             | INCORRECT (Max overlap: 3/4 with “POINTERS”)
   - Group 2: **0.4976** | MAPS, FUR, MAIL, NOTES                                            | INCORRECT (Max overlap: 3/4 with IPHONE APPS)
   - Group 3: **0.4918** | STAND, CLOCK, SHELL, SCALES                                       | INCORRECT (Max overlap: 2/4 with ANIMAL COVERINGS)
   - Group 4: **0.4777** | SALUTE, DOWN, FINGER, KNEEL                                       | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
4. **Partition Score: 0.4859**
   - Group 1: **0.5654** | FUR, MAIL, SHELL, ARROW                                           | INCORRECT (Max overlap: 2/4 with ANIMAL COVERINGS)
   - Group 2: **0.5305** | MAPS, NOTES, CLOCK, SCALES                                        | INCORRECT (Max overlap: 3/4 with IPHONE APPS)
   - Group 3: **0.4777** | SALUTE, DOWN, FINGER, KNEEL                                       | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 4: **0.4676** | STAND, HINT, DOG, BOW                                             | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
5. **Partition Score: 0.4857**
   - Group 1: **0.5642** | MAPS, MAIL, NOTES, SCALES                                         | INCORRECT (Max overlap: 3/4 with IPHONE APPS)
   - Group 2: **0.5299** | FUR, CLOCK, SHELL, ARROW                                          | INCORRECT (Max overlap: 2/4 with ANIMAL COVERINGS)
   - Group 3: **0.4777** | SALUTE, DOWN, FINGER, KNEEL                                       | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 4: **0.4676** | STAND, HINT, DOG, BOW                                             | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)

### Top Candidate Groups:
   - Group 1: **0.5484** | MAPS, FUR, MAIL, ARROW                                            | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 2: **0.5457** | NOTES, CLOCK, SHELL, SCALES                                       | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 3: **0.4777** | SALUTE, DOWN, FINGER, KNEEL                                       | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 4: **0.4676** | STAND, HINT, DOG, BOW                                             | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 5: **0.5492** | MAPS, FUR, MAIL, SHELL                                            | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 6: **0.4987** | HINT, ARROW, DOG, BOW                                             | INCORRECT (Max overlap: 3/4 with “POINTERS”)
   - Group 7: **0.4932** | STAND, NOTES, CLOCK, SCALES                                       | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 8: **0.4976** | MAPS, FUR, MAIL, NOTES                                            | INCORRECT (Max overlap: 3/4 with IPHONE APPS)
   - Group 9: **0.4918** | STAND, CLOCK, SHELL, SCALES                                       | INCORRECT (Max overlap: 2/4 with ANIMAL COVERINGS)
   - Group 10: **0.5654** | FUR, MAIL, SHELL, ARROW                                           | INCORRECT (Max overlap: 2/4 with ANIMAL COVERINGS)
   - Group 11: **0.5305** | MAPS, NOTES, CLOCK, SCALES                                        | INCORRECT (Max overlap: 3/4 with IPHONE APPS)
   - Group 12: **0.5642** | MAPS, MAIL, NOTES, SCALES                                         | INCORRECT (Max overlap: 3/4 with IPHONE APPS)
   - Group 13: **0.5299** | FUR, CLOCK, SHELL, ARROW                                          | INCORRECT (Max overlap: 2/4 with ANIMAL COVERINGS)
   - Group 14: **0.5424** | MAPS, STAND, NOTES, SCALES                                        | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 15: **0.4838** | FUR, MAIL, CLOCK, SHELL                                           | INCORRECT (Max overlap: 2/4 with ANIMAL COVERINGS)
   - Group 16: **0.5778** | FUR, ARROW, DOG, BOW                                              | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 17: **0.4888** | MAPS, MAIL, HINT, SHELL                                           | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 18: **0.4998** | MAPS, ARROW, DOG, BOW                                             | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 19: **0.4954** | STAND, NOTES, HINT, SCALES                                        | INCORRECT (Max overlap: 1/4 with WAYS TO SHOW RESPECT)
   - Group 20: **0.4872** | MAPS, MAIL, NOTES, HINT                                           | INCORRECT (Max overlap: 3/4 with IPHONE APPS)

---

## Puzzle 106 (ID: 882)
**Words on Board:** SINE, SUB, CONQUERED, AB, DRUM, TRIANGLE, CLEAR, SETTLE, SQUARE, CAME, PRO, RATTLE, PAY, I, SAW, BELL

### Ground Truth Categories:
* **Level 0 (PERCUSSION INSTRUMENTS) [Type: SEMANTIC_SET]:** BELL, DRUM, RATTLE, TRIANGLE
* **Level 1 (SATISFY, AS DEBTS) [Type: SYNONYM_OR_NEAR]:** CLEAR, PAY, SETTLE, SQUARE
* **Level 2 (WORDS IN A FAMOUS QUOTE BY CAESAR) [Type: NAMED_ENTITY_SET]:** CAME, CONQUERED, I, SAW
* **Level 3 (LATIN PREPOSITIONS) [Type: SEMANTIC_SET]:** AB, PRO, SINE, SUB

### Top Candidate Partitions:
1. **Partition Score: 0.5640**
   - Group 1: **0.6492** | DRUM, TRIANGLE, RATTLE, BELL                                      | CORRECT GROUP (PERCUSSION INSTRUMENTS, Level 0)
   - Group 2: **0.5977** | SINE, SUB, AB, PRO                                                | CORRECT GROUP (LATIN PREPOSITIONS, Level 3)
   - Group 3: **0.5763** | CONQUERED, CLEAR, I, SAW                                          | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 4: **0.5411** | SETTLE, SQUARE, CAME, PAY                                         | INCORRECT (Max overlap: 3/4 with SATISFY, AS DEBTS)
2. **Partition Score: 0.5586**
   - Group 1: **0.6492** | DRUM, TRIANGLE, RATTLE, BELL                                      | CORRECT GROUP (PERCUSSION INSTRUMENTS, Level 0)
   - Group 2: **0.6246** | SINE, SUB, AB, I                                                  | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)
   - Group 3: **0.5411** | SETTLE, SQUARE, CAME, PAY                                         | INCORRECT (Max overlap: 3/4 with SATISFY, AS DEBTS)
   - Group 4: **0.5343** | CONQUERED, CLEAR, PRO, SAW                                        | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
3. **Partition Score: 0.5553**
   - Group 1: **0.6492** | DRUM, TRIANGLE, RATTLE, BELL                                      | CORRECT GROUP (PERCUSSION INSTRUMENTS, Level 0)
   - Group 2: **0.6237** | SINE, AB, PRO, I                                                  | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)
   - Group 3: **0.5411** | SETTLE, SQUARE, CAME, PAY                                         | INCORRECT (Max overlap: 3/4 with SATISFY, AS DEBTS)
   - Group 4: **0.5283** | SUB, CONQUERED, CLEAR, SAW                                        | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
4. **Partition Score: 0.5535**
   - Group 1: **0.6492** | DRUM, TRIANGLE, RATTLE, BELL                                      | CORRECT GROUP (PERCUSSION INSTRUMENTS, Level 0)
   - Group 2: **0.5906** | CONQUERED, CLEAR, PRO, I                                          | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 3: **0.5413** | SINE, SUB, AB, SAW                                                | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)
   - Group 4: **0.5411** | SETTLE, SQUARE, CAME, PAY                                         | INCORRECT (Max overlap: 3/4 with SATISFY, AS DEBTS)
5. **Partition Score: 0.5506**
   - Group 1: **0.6492** | DRUM, TRIANGLE, RATTLE, BELL                                      | CORRECT GROUP (PERCUSSION INSTRUMENTS, Level 0)
   - Group 2: **0.5925** | CLEAR, PRO, I, SAW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 3: **0.5411** | SETTLE, SQUARE, CAME, PAY                                         | INCORRECT (Max overlap: 3/4 with SATISFY, AS DEBTS)
   - Group 4: **0.5344** | SINE, SUB, CONQUERED, AB                                          | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)

### Top Candidate Groups:
   - Group 1: **0.6492** | DRUM, TRIANGLE, RATTLE, BELL                                      | CORRECT GROUP (PERCUSSION INSTRUMENTS, Level 0)
   - Group 2: **0.5977** | SINE, SUB, AB, PRO                                                | CORRECT GROUP (LATIN PREPOSITIONS, Level 3)
   - Group 3: **0.5763** | CONQUERED, CLEAR, I, SAW                                          | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 4: **0.5411** | SETTLE, SQUARE, CAME, PAY                                         | INCORRECT (Max overlap: 3/4 with SATISFY, AS DEBTS)
   - Group 5: **0.6246** | SINE, SUB, AB, I                                                  | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)
   - Group 6: **0.5343** | CONQUERED, CLEAR, PRO, SAW                                        | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 7: **0.6237** | SINE, AB, PRO, I                                                  | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)
   - Group 8: **0.5283** | SUB, CONQUERED, CLEAR, SAW                                        | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 9: **0.5906** | CONQUERED, CLEAR, PRO, I                                          | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 10: **0.5413** | SINE, SUB, AB, SAW                                                | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)
   - Group 11: **0.5925** | CLEAR, PRO, I, SAW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 12: **0.5344** | SINE, SUB, CONQUERED, AB                                          | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)
   - Group 13: **0.5961** | SUB, CLEAR, I, SAW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)
   - Group 14: **0.5323** | SINE, CONQUERED, AB, PRO                                          | INCORRECT (Max overlap: 3/4 with LATIN PREPOSITIONS)
   - Group 15: **0.5615** | SUB, CLEAR, PRO, SAW                                              | INCORRECT (Max overlap: 2/4 with LATIN PREPOSITIONS)
   - Group 16: **0.5581** | SINE, CONQUERED, AB, I                                            | INCORRECT (Max overlap: 2/4 with LATIN PREPOSITIONS)
   - Group 17: **0.5686** | SINE, AB, I, SAW                                                  | INCORRECT (Max overlap: 2/4 with LATIN PREPOSITIONS)
   - Group 18: **0.5426** | SUB, CONQUERED, CLEAR, PRO                                        | INCORRECT (Max overlap: 2/4 with LATIN PREPOSITIONS)
   - Group 19: **0.5723** | SINE, DRUM, RATTLE, BELL                                          | INCORRECT (Max overlap: 3/4 with PERCUSSION INSTRUMENTS)
   - Group 20: **0.5514** | AB, TRIANGLE, I, SAW                                              | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS QUOTE BY CAESAR)

---

## Puzzle 107 (ID: 49)
**Words on Board:** DAFFY, WACKY, NEPHEW, ALARM, GRANDFATHER, SCROOGE, BIOLOGICAL, DEWEY, AUNT, DONALD, DAISY, CUCKOO, COUSIN, QUIRKY, KOOKY, MOTHER

### Ground Truth Categories:
* **Level 0 (RELATIVES) [Type: SEMANTIC_SET]:** AUNT, COUSIN, MOTHER, NEPHEW
* **Level 1 (SYNONYMS FOR OFFBEAT) [Type: SYNONYM_OR_NEAR]:** DAFFY, KOOKY, QUIRKY, WACKY
* **Level 2 (DISNEY DUCKS) [Type: NAMED_ENTITY_SET]:** DAISY, DEWEY, DONALD, SCROOGE
* **Level 3 (___ CLOCK) [Type: FILL_IN_THE_BLANK]:** ALARM, BIOLOGICAL, CUCKOO, GRANDFATHER

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7832** | NEPHEW, GRANDFATHER, AUNT, COUSIN                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 2: **0.7661** | NEPHEW, GRANDFATHER, AUNT, MOTHER                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 3: **0.7595** | GRANDFATHER, AUNT, COUSIN, MOTHER                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 4: **0.7555** | NEPHEW, AUNT, COUSIN, MOTHER                                      | CORRECT GROUP (RELATIVES, Level 0)
   - Group 5: **0.7281** | NEPHEW, GRANDFATHER, COUSIN, MOTHER                               | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 6: **0.7273** | GRANDFATHER, AUNT, DAISY, MOTHER                                  | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 7: **0.6994** | DAFFY, SCROOGE, DAISY, CUCKOO                                     | INCORRECT (Max overlap: 2/4 with DISNEY DUCKS)
   - Group 8: **0.6969** | GRANDFATHER, AUNT, DAISY, COUSIN                                  | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 9: **0.6954** | GRANDFATHER, SCROOGE, AUNT, MOTHER                                | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 10: **0.6954** | AUNT, DAISY, COUSIN, MOTHER                                       | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 11: **0.6946** | GRANDFATHER, AUNT, CUCKOO, MOTHER                                 | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
   - Group 12: **0.6909** | NEPHEW, AUNT, DAISY, COUSIN                                       | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 13: **0.6887** | AUNT, DAISY, CUCKOO, MOTHER                                       | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 14: **0.6887** | NEPHEW, GRANDFATHER, SCROOGE, AUNT                                | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 15: **0.6877** | NEPHEW, GRANDFATHER, AUNT, DAISY                                  | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 16: **0.6839** | NEPHEW, SCROOGE, AUNT, COUSIN                                     | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 17: **0.6837** | DAFFY, SCROOGE, DEWEY, DAISY                                      | INCORRECT (Max overlap: 3/4 with DISNEY DUCKS)
   - Group 18: **0.6832** | ALARM, AUNT, DAISY, CUCKOO                                        | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
   - Group 19: **0.6818** | DAFFY, DEWEY, DAISY, CUCKOO                                       | INCORRECT (Max overlap: 2/4 with DISNEY DUCKS)
   - Group 20: **0.6814** | GRANDFATHER, AUNT, DAISY, CUCKOO                                  | INCORRECT (Max overlap: 2/4 with ___ CLOCK)

---

## Puzzle 108 (ID: 774)
**Words on Board:** LUTE, POLE, KNICK, RABE, JET, BACKBOARD, DIP, BOUNCE, TITANIC, MAMMOTH, RIM, SPLIT, STEEL, GREAT, GIANT, NET

### Ground Truth Categories:
* **Level 0 (COLOSSAL) [Type: SYNONYM_OR_NEAR]:** GIANT, GREAT, MAMMOTH, TITANIC
* **Level 1 (LEAVE QUICKLY) [Type: SYNONYM_OR_NEAR]:** BOUNCE, DIP, JET, SPLIT
* **Level 2 (PARTS OF A BASKETBALL HOOP) [Type: SEMANTIC_SET]:** BACKBOARD, NET, POLE, RIM
* **Level 3 (HOMOPHONES OF SYNONYMS FOR “NAB”) [Type: SOUND_OR_SPELLING]:** KNICK, LUTE, RABE, STEEL

### Top Candidate Partitions:
1. **Partition Score: 0.5200**
   - Group 1: **0.6006** | TITANIC, MAMMOTH, GREAT, GIANT                                    | CORRECT GROUP (COLOSSAL, Level 0)
   - Group 2: **0.5642** | JET, DIP, SPLIT, STEEL                                            | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)
   - Group 3: **0.5072** | LUTE, KNICK, RABE, BOUNCE                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF SYNONYMS FOR “NAB”)
   - Group 4: **0.5042** | POLE, BACKBOARD, RIM, NET                                         | CORRECT GROUP (PARTS OF A BASKETBALL HOOP, Level 2)
2. **Partition Score: 0.5199**
   - Group 1: **0.6006** | TITANIC, MAMMOTH, GREAT, GIANT                                    | CORRECT GROUP (COLOSSAL, Level 0)
   - Group 2: **0.5642** | JET, DIP, SPLIT, STEEL                                            | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)
   - Group 3: **0.5380** | POLE, BACKBOARD, BOUNCE, NET                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A BASKETBALL HOOP)
   - Group 4: **0.4886** | LUTE, KNICK, RABE, RIM                                            | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF SYNONYMS FOR “NAB”)
3. **Partition Score: 0.5168**
   - Group 1: **0.6006** | TITANIC, MAMMOTH, GREAT, GIANT                                    | CORRECT GROUP (COLOSSAL, Level 0)
   - Group 2: **0.5465** | DIP, RIM, SPLIT, STEEL                                            | INCORRECT (Max overlap: 2/4 with LEAVE QUICKLY)
   - Group 3: **0.5380** | POLE, BACKBOARD, BOUNCE, NET                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A BASKETBALL HOOP)
   - Group 4: **0.4914** | LUTE, KNICK, RABE, JET                                            | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF SYNONYMS FOR “NAB”)
4. **Partition Score: 0.5132**
   - Group 1: **0.6006** | TITANIC, MAMMOTH, GREAT, GIANT                                    | CORRECT GROUP (COLOSSAL, Level 0)
   - Group 2: **0.5865** | JET, DIP, BOUNCE, SPLIT                                           | CORRECT GROUP (LEAVE QUICKLY, Level 1)
   - Group 3: **0.5042** | POLE, BACKBOARD, RIM, NET                                         | CORRECT GROUP (PARTS OF A BASKETBALL HOOP, Level 2)
   - Group 4: **0.4811** | LUTE, KNICK, RABE, STEEL                                          | CORRECT GROUP (HOMOPHONES OF SYNONYMS FOR “NAB”, Level 3)
5. **Partition Score: 0.5121**
   - Group 1: **0.6006** | TITANIC, MAMMOTH, GREAT, GIANT                                    | CORRECT GROUP (COLOSSAL, Level 0)
   - Group 2: **0.5615** | DIP, BOUNCE, SPLIT, STEEL                                         | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)
   - Group 3: **0.5042** | POLE, BACKBOARD, RIM, NET                                         | CORRECT GROUP (PARTS OF A BASKETBALL HOOP, Level 2)
   - Group 4: **0.4914** | LUTE, KNICK, RABE, JET                                            | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF SYNONYMS FOR “NAB”)

### Top Candidate Groups:
   - Group 1: **0.6006** | TITANIC, MAMMOTH, GREAT, GIANT                                    | CORRECT GROUP (COLOSSAL, Level 0)
   - Group 2: **0.5642** | JET, DIP, SPLIT, STEEL                                            | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)
   - Group 3: **0.5072** | LUTE, KNICK, RABE, BOUNCE                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF SYNONYMS FOR “NAB”)
   - Group 4: **0.5042** | POLE, BACKBOARD, RIM, NET                                         | CORRECT GROUP (PARTS OF A BASKETBALL HOOP, Level 2)
   - Group 5: **0.5380** | POLE, BACKBOARD, BOUNCE, NET                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A BASKETBALL HOOP)
   - Group 6: **0.4886** | LUTE, KNICK, RABE, RIM                                            | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF SYNONYMS FOR “NAB”)
   - Group 7: **0.5465** | DIP, RIM, SPLIT, STEEL                                            | INCORRECT (Max overlap: 2/4 with LEAVE QUICKLY)
   - Group 8: **0.4914** | LUTE, KNICK, RABE, JET                                            | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF SYNONYMS FOR “NAB”)
   - Group 9: **0.5865** | JET, DIP, BOUNCE, SPLIT                                           | CORRECT GROUP (LEAVE QUICKLY, Level 1)
   - Group 10: **0.4811** | LUTE, KNICK, RABE, STEEL                                          | CORRECT GROUP (HOMOPHONES OF SYNONYMS FOR “NAB”, Level 3)
   - Group 11: **0.5615** | DIP, BOUNCE, SPLIT, STEEL                                         | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)
   - Group 12: **0.5340** | JET, DIP, RIM, SPLIT                                              | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)
   - Group 13: **0.5404** | JET, TITANIC, MAMMOTH, GIANT                                      | INCORRECT (Max overlap: 3/4 with COLOSSAL)
   - Group 14: **0.5031** | DIP, SPLIT, STEEL, GREAT                                          | INCORRECT (Max overlap: 2/4 with LEAVE QUICKLY)
   - Group 15: **0.5204** | JET, DIP, RIM, STEEL                                              | INCORRECT (Max overlap: 2/4 with LEAVE QUICKLY)
   - Group 16: **0.4901** | POLE, BACKBOARD, SPLIT, NET                                       | INCORRECT (Max overlap: 3/4 with PARTS OF A BASKETBALL HOOP)
   - Group 17: **0.5339** | JET, DIP, BOUNCE, STEEL                                           | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)
   - Group 18: **0.5209** | TITANIC, MAMMOTH, STEEL, GIANT                                    | INCORRECT (Max overlap: 3/4 with COLOSSAL)
   - Group 19: **0.5077** | DIP, BOUNCE, SPLIT, GREAT                                         | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)
   - Group 20: **0.5420** | JET, DIP, BOUNCE, RIM                                             | INCORRECT (Max overlap: 3/4 with LEAVE QUICKLY)

---
