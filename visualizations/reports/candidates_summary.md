# GCN Subgraph Predictions - All Validation Puzzles

Generated from the current `models/gcn_all_time_best_v14.pt` checkpoint loaded by the training pipeline.

This document summarizes the top 5 candidate partitions built from GCN predictions for all 109 validation puzzles. Each group is labeled with exact correctness or maximum overlap with a ground truth category.

## Aggregate Summary

| Metric | Current | Previous | Change vs Prev | All-Time Best | Change vs All-Time |
|---|---:|---:|---:|---:|---:|
| Validation puzzles | 109 | 109 | 0 | 109 | 0 |
| Overall GCN Candidate MRR | 0.2030 | 0.2036 | 🔴 -0.00 (regressed) | 0.2030 | 0 |
| Overall Pairwise Relation Accuracy | 79.4% | 79.9% | 🔴 -0.5% (regressed) | 79.4% | 0.0% |
| Overall Group Relation Accuracy | 38.8% | 39.7% | 🔴 -0.9% (regressed) | 38.8% | 0.0% |
| Puzzles with complete partition candidates | 107 / 109 (98.2%) | 109 / 109 (100.0%) | 🔴 -1.8% (regressed) | 107 / 109 (98.2%) | 0.0% |
| Top partition solves all 4 groups | 12 / 109 (11.0%) | 11 / 109 (10.1%) | 🟢 +0.9% (improved) | 12 / 109 (11.0%) | 0.0% |
| Any top-5 partition solves all 4 groups | 19 / 109 (17.4%) | 15 / 109 (13.8%) | 🟢 +3.6% (improved) | 19 / 109 (17.4%) | 0.0% |
| Avg correct groups in top partition | 1.21 / 4 | 1.18 / 4 | 🟢 +0.03 (improved) | 1.21 / 4 | 0 |
| Avg best correct groups across top partitions | 1.57 / 4 | 1.47 / 4 | 🟢 +0.10 (improved) | 1.57 / 4 | 0 |
| True groups in top-20 candidates | 202 / 436 (46.3%) | 198 / 436 (45.4%) | 🟢 +0.9% (improved) | 202 / 436 (46.3%) | 0.0% |
| Puzzles with any true group in top-20 | 89 / 109 (81.7%) | 89 / 109 (81.7%) | 0.0% | 89 / 109 (81.7%) | 0.0% |
| Puzzles with all true groups in top-20 | 22 / 109 (20.2%) | 19 / 109 (17.4%) | 🟢 +2.8% (improved) | 22 / 109 (20.2%) | 0.0% |
| Mean rank of true groups found in top-20 | 4.94 | 5.21 | 🟢 -0.27 (improved) | 4.94 | 0 |
| Median rank of true groups found in top-20 | 3.0 | 3.0 | 0 | 3.0 | 0 |
| 3-of-4 near-miss candidates in top-20 | 958 | 937 | 🔴 +21 (regressed) | 958 | 0 |

### Recall By Relation Archetype

| Archetype | True Groups | Hit Top 20 | Recall | Hit Top 5 | Avg Best Rank | Exact MRR | Pairwise Acc | Group Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| COMMON_PHRASE | 3 | 0 | 0.0% | 0 | 0.00 | 0.0021 | 0.0% | 0.0% |
| FILL_IN_THE_BLANK | 56 | 21 | 37.5% | 13 | 6.67 | 0.1053 | 6.5% | 35.7% |
| NAMED_ENTITY_SET | 52 | 18 | 34.6% | 11 | 5.89 | 0.1345 | 12.8% | 53.8% |
| NO_RELATION | 0 | 0 | 0.0% | 0 | 0.00 | 0.0000 | 95.4% | 38.3% |
| SEMANTIC_SET | 139 | 58 | 41.7% | 44 | 4.09 | 0.1847 | 2.8% | 34.5% |
| SOUND_OR_SPELLING | 13 | 3 | 23.1% | 2 | 4.33 | 0.0403 | 23.1% | 23.1% |
| SYNONYM_OR_NEAR | 142 | 90 | 63.4% | 65 | 4.89 | 0.3280 | 32.9% | 71.8% |
| WORDPLAY_TRANSFORM | 17 | 3 | 17.6% | 1 | 9.33 | 0.0272 | 7.8% | 11.8% |
| WORD_FORM | 14 | 9 | 64.3% | 8 | 3.67 | 0.1699 | 20.2% | 0.0% |

---

## Puzzle 0 (ID: 253)
**Words on Board:** BLOW, HINGE, BUMBLE, GRINDER, LOCK, DRILL, KINDLING, SPOIL, LOG, TINDER, SAW, ROUTER, MATCH, HANDLE, FLUFF, FRAME

### Ground Truth Categories:
* **Level 0 (USED IN BUILDING A FIRE) [Type: SEMANTIC_SET]:** KINDLING, LOG, MATCH, TINDER
* **Level 1 (MESS UP) [Type: SYNONYM_OR_NEAR]:** BLOW, BUMBLE, FLUFF, SPOIL
* **Level 2 (WORKSHOP TOOLS) [Type: SEMANTIC_SET]:** DRILL, GRINDER, ROUTER, SAW
* **Level 3 (PARTS OF A DOOR) [Type: SEMANTIC_SET]:** FRAME, HANDLE, HINGE, LOCK

### Top Candidate Partitions:
1. **Partition Score: 0.5382**
   - Group 1: **0.8895** | BLOW, BUMBLE, SPOIL, FLUFF                                        | CORRECT GROUP (MESS UP, Level 1)
   - Group 2: **0.5184** | HINGE, LOCK, HANDLE, FRAME                                        | CORRECT GROUP (PARTS OF A DOOR, Level 3)
   - Group 3: **0.4870** | GRINDER, DRILL, LOG, SAW                                          | INCORRECT (Max overlap: 3/4 with WORKSHOP TOOLS) | [Pred Type: SEMANTIC_SET (47.1%, no-rel 33.6%)]
   - Group 4: **0.4870** | KINDLING, TINDER, ROUTER, MATCH                                   | INCORRECT (Max overlap: 3/4 with USED IN BUILDING A FIRE)
2. **Partition Score: 0.5337**
   - Group 1: **0.8895** | BLOW, BUMBLE, SPOIL, FLUFF                                        | CORRECT GROUP (MESS UP, Level 1)
   - Group 2: **0.5184** | HINGE, LOCK, HANDLE, FRAME                                        | CORRECT GROUP (PARTS OF A DOOR, Level 3)
   - Group 3: **0.5100** | DRILL, LOG, SAW, MATCH                                            | INCORRECT (Max overlap: 2/4 with WORKSHOP TOOLS)
   - Group 4: **0.4698** | GRINDER, KINDLING, TINDER, ROUTER                                 | INCORRECT (Max overlap: 2/4 with WORKSHOP TOOLS)
3. **Partition Score: 0.5256**
   - Group 1: **0.8895** | BLOW, BUMBLE, SPOIL, FLUFF                                        | CORRECT GROUP (MESS UP, Level 1)
   - Group 2: **0.5184** | HINGE, LOCK, HANDLE, FRAME                                        | CORRECT GROUP (PARTS OF A DOOR, Level 3)
   - Group 3: **0.4900** | GRINDER, KINDLING, TINDER, MATCH                                  | INCORRECT (Max overlap: 3/4 with USED IN BUILDING A FIRE)
   - Group 4: **0.4613** | DRILL, LOG, SAW, ROUTER                                           | INCORRECT (Max overlap: 3/4 with WORKSHOP TOOLS)
4. **Partition Score: 0.5105**
   - Group 1: **0.8895** | BLOW, BUMBLE, SPOIL, FLUFF                                        | CORRECT GROUP (MESS UP, Level 1)
   - Group 2: **0.4870** | KINDLING, TINDER, ROUTER, MATCH                                   | INCORRECT (Max overlap: 3/4 with USED IN BUILDING A FIRE)
   - Group 3: **0.4686** | HINGE, GRINDER, HANDLE, FRAME                                     | INCORRECT (Max overlap: 3/4 with PARTS OF A DOOR)
   - Group 4: **0.4512** | LOCK, DRILL, LOG, SAW                                             | INCORRECT (Max overlap: 2/4 with WORKSHOP TOOLS)
5. **Partition Score: 0.5067**
   - Group 1: **0.8895** | BLOW, BUMBLE, SPOIL, FLUFF                                        | CORRECT GROUP (MESS UP, Level 1)
   - Group 2: **0.5184** | HINGE, LOCK, HANDLE, FRAME                                        | CORRECT GROUP (PARTS OF A DOOR, Level 3)
   - Group 3: **0.4445** | DRILL, KINDLING, TINDER, MATCH                                    | INCORRECT (Max overlap: 3/4 with USED IN BUILDING A FIRE)
   - Group 4: **0.4411** | GRINDER, LOG, SAW, ROUTER                                         | INCORRECT (Max overlap: 3/4 with WORKSHOP TOOLS)

### Top Candidate Groups:
   - Group 1: **0.8895** | BLOW, BUMBLE, SPOIL, FLUFF                                        | CORRECT GROUP (MESS UP, Level 1)
   - Group 2: **0.5184** | HINGE, LOCK, HANDLE, FRAME                                        | CORRECT GROUP (PARTS OF A DOOR, Level 3)
   - Group 3: **0.4870** | GRINDER, DRILL, LOG, SAW                                          | INCORRECT (Max overlap: 3/4 with WORKSHOP TOOLS) | [Pred Type: SEMANTIC_SET (47.1%, no-rel 33.6%)]
   - Group 4: **0.4870** | KINDLING, TINDER, ROUTER, MATCH                                   | INCORRECT (Max overlap: 3/4 with USED IN BUILDING A FIRE)
   - Group 5: **0.5100** | DRILL, LOG, SAW, MATCH                                            | INCORRECT (Max overlap: 2/4 with WORKSHOP TOOLS)
   - Group 6: **0.4698** | GRINDER, KINDLING, TINDER, ROUTER                                 | INCORRECT (Max overlap: 2/4 with WORKSHOP TOOLS)
   - Group 7: **0.4900** | GRINDER, KINDLING, TINDER, MATCH                                  | INCORRECT (Max overlap: 3/4 with USED IN BUILDING A FIRE)
   - Group 8: **0.4613** | DRILL, LOG, SAW, ROUTER                                           | INCORRECT (Max overlap: 3/4 with WORKSHOP TOOLS)
   - Group 9: **0.4686** | HINGE, GRINDER, HANDLE, FRAME                                     | INCORRECT (Max overlap: 3/4 with PARTS OF A DOOR)
   - Group 10: **0.4512** | LOCK, DRILL, LOG, SAW                                             | INCORRECT (Max overlap: 2/4 with WORKSHOP TOOLS)
   - Group 11: **0.4445** | DRILL, KINDLING, TINDER, MATCH                                    | INCORRECT (Max overlap: 3/4 with USED IN BUILDING A FIRE)
   - Group 12: **0.4411** | GRINDER, LOG, SAW, ROUTER                                         | INCORRECT (Max overlap: 3/4 with WORKSHOP TOOLS)
   - Group 13: **0.4703** | GRINDER, LOCK, HANDLE, FRAME                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A DOOR)
   - Group 14: **0.4479** | HINGE, KINDLING, TINDER, MATCH                                    | INCORRECT (Max overlap: 3/4 with USED IN BUILDING A FIRE)
   - Group 15: **0.5465** | DRILL, SAW, ROUTER, MATCH                                         | INCORRECT (Max overlap: 3/4 with WORKSHOP TOOLS)
   - Group 16: **0.4376** | HINGE, GRINDER, KINDLING, TINDER                                  | INCORRECT (Max overlap: 2/4 with USED IN BUILDING A FIRE)
   - Group 17: **0.4266** | LOCK, LOG, HANDLE, FRAME                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A DOOR)
   - Group 18: **0.4877** | LOCK, MATCH, HANDLE, FRAME                                        | INCORRECT (Max overlap: 3/4 with PARTS OF A DOOR)
   - Group 19: **0.4522** | DRILL, LOG, SAW, HANDLE                                           | INCORRECT (Max overlap: 2/4 with WORKSHOP TOOLS)
   - Group 20: **0.4446** | HINGE, LOCK, MATCH, FRAME                                         | INCORRECT (Max overlap: 3/4 with PARTS OF A DOOR)

---

## Puzzle 1 (ID: 18)
**Words on Board:** CUP, LAT, RIBBON, QUINN, QUAD, HOUSE, BROWN, GREY, BEAR, BILL, TRI, COMMANDER, TROPHY, HOWSER, PEC, MEDAL

### Ground Truth Categories:
* **Level 0 (MUSCLES, INFORMALLY) [Type: SEMANTIC_SET]:** LAT, PEC, QUAD, TRI
* **Level 1 (AWARDS) [Type: SEMANTIC_SET]:** CUP, MEDAL, RIBBON, TROPHY
* **Level 2 (TITLE TV DOCTORS) [Type: NAMED_ENTITY_SET]:** GREY, HOUSE, HOWSER, QUINN
* **Level 3 (NFL PLAYERS) [Type: NAMED_ENTITY_SET]:** BEAR, BILL, BROWN, COMMANDER

### Top Candidate Partitions:
1. **Partition Score: 0.4930**
   - Group 1: **0.6202** | CUP, RIBBON, TROPHY, MEDAL                                        | CORRECT GROUP (AWARDS, Level 1) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 31.3%)]
   - Group 2: **0.5657** | BROWN, GREY, BEAR, BILL                                           | INCORRECT (Max overlap: 3/4 with NFL PLAYERS)
   - Group 3: **0.4899** | LAT, QUAD, TRI, PEC                                               | CORRECT GROUP (MUSCLES, INFORMALLY, Level 0)
   - Group 4: **0.4396** | QUINN, HOUSE, COMMANDER, HOWSER                                   | INCORRECT (Max overlap: 3/4 with TITLE TV DOCTORS)
2. **Partition Score: 0.4853**
   - Group 1: **0.6202** | CUP, RIBBON, TROPHY, MEDAL                                        | CORRECT GROUP (AWARDS, Level 1) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 31.3%)]
   - Group 2: **0.5498** | HOUSE, BROWN, BEAR, BILL                                          | INCORRECT (Max overlap: 3/4 with NFL PLAYERS)
   - Group 3: **0.4466** | LAT, QUAD, GREY, TRI                                              | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
   - Group 4: **0.4462** | QUINN, COMMANDER, HOWSER, PEC                                     | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS)
3. **Partition Score: 0.4834**
   - Group 1: **0.6202** | CUP, RIBBON, TROPHY, MEDAL                                        | CORRECT GROUP (AWARDS, Level 1) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 31.3%)]
   - Group 2: **0.5371** | LAT, BROWN, GREY, BEAR                                            | INCORRECT (Max overlap: 2/4 with NFL PLAYERS)
   - Group 3: **0.5114** | QUINN, QUAD, TRI, PEC                                             | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
   - Group 4: **0.4234** | HOUSE, BILL, COMMANDER, HOWSER                                    | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS)
4. **Partition Score: 0.4831**
   - Group 1: **0.6202** | CUP, RIBBON, TROPHY, MEDAL                                        | CORRECT GROUP (AWARDS, Level 1) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 31.3%)]
   - Group 2: **0.5657** | BROWN, GREY, BEAR, BILL                                           | INCORRECT (Max overlap: 3/4 with NFL PLAYERS)
   - Group 3: **0.4510** | QUINN, QUAD, HOUSE, COMMANDER                                     | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 24.5%)]
   - Group 4: **0.4346** | LAT, TRI, HOWSER, PEC                                             | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
5. **Partition Score: 0.4831**
   - Group 1: **0.6202** | CUP, RIBBON, TROPHY, MEDAL                                        | CORRECT GROUP (AWARDS, Level 1) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 31.3%)]
   - Group 2: **0.5114** | QUINN, QUAD, TRI, PEC                                             | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
   - Group 3: **0.4880** | LAT, BROWN, GREY, BILL                                            | INCORRECT (Max overlap: 2/4 with NFL PLAYERS)
   - Group 4: **0.4408** | HOUSE, BEAR, COMMANDER, HOWSER                                    | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS)

### Top Candidate Groups:
   - Group 1: **0.6202** | CUP, RIBBON, TROPHY, MEDAL                                        | CORRECT GROUP (AWARDS, Level 1) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 31.3%)]
   - Group 2: **0.5657** | BROWN, GREY, BEAR, BILL                                           | INCORRECT (Max overlap: 3/4 with NFL PLAYERS)
   - Group 3: **0.4899** | LAT, QUAD, TRI, PEC                                               | CORRECT GROUP (MUSCLES, INFORMALLY, Level 0)
   - Group 4: **0.4396** | QUINN, HOUSE, COMMANDER, HOWSER                                   | INCORRECT (Max overlap: 3/4 with TITLE TV DOCTORS)
   - Group 5: **0.5498** | HOUSE, BROWN, BEAR, BILL                                          | INCORRECT (Max overlap: 3/4 with NFL PLAYERS)
   - Group 6: **0.4466** | LAT, QUAD, GREY, TRI                                              | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
   - Group 7: **0.4462** | QUINN, COMMANDER, HOWSER, PEC                                     | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS)
   - Group 8: **0.5371** | LAT, BROWN, GREY, BEAR                                            | INCORRECT (Max overlap: 2/4 with NFL PLAYERS)
   - Group 9: **0.5114** | QUINN, QUAD, TRI, PEC                                             | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
   - Group 10: **0.4234** | HOUSE, BILL, COMMANDER, HOWSER                                    | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS)
   - Group 11: **0.4510** | QUINN, QUAD, HOUSE, COMMANDER                                     | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 24.5%)]
   - Group 12: **0.4346** | LAT, TRI, HOWSER, PEC                                             | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
   - Group 13: **0.4880** | LAT, BROWN, GREY, BILL                                            | INCORRECT (Max overlap: 2/4 with NFL PLAYERS)
   - Group 14: **0.4408** | HOUSE, BEAR, COMMANDER, HOWSER                                    | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS)
   - Group 15: **0.4363** | LAT, QUINN, TRI, HOWSER                                           | INCORRECT (Max overlap: 2/4 with MUSCLES, INFORMALLY)
   - Group 16: **0.4360** | QUAD, HOUSE, COMMANDER, PEC                                       | INCORRECT (Max overlap: 2/4 with MUSCLES, INFORMALLY) | [Pred Type: NAMED_ENTITY_SET (46.3%, no-rel 26.1%)]
   - Group 17: **0.4434** | LAT, QUAD, TRI, HOWSER                                            | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
   - Group 18: **0.4301** | QUINN, HOUSE, COMMANDER, PEC                                      | INCORRECT (Max overlap: 2/4 with TITLE TV DOCTORS) | [Pred Type: NAMED_ENTITY_SET (47.4%, no-rel 23.6%)]
   - Group 19: **0.4280** | LAT, QUAD, HOUSE, TRI                                             | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY)
   - Group 20: **0.4378** | LAT, QUAD, COMMANDER, PEC                                         | INCORRECT (Max overlap: 3/4 with MUSCLES, INFORMALLY) | [Pred Type: NAMED_ENTITY_SET (49.3%, no-rel 21.8%)]

---

## Puzzle 2 (ID: 1078)
**Words on Board:** ATLANTIC, BILLIARD, FATHER, PROTACTINIUM, PUBLIC ADDRESS, DRAWING, BO, PENNSYLVANIA, POWDER, ARCTIC, AMMONIA, READING, DURIAN, WET DOG, PACIFIC, SOUTHERN

### Ground Truth Categories:
* **Level 0 (OCEANS) [Type: NAMED_ENTITY_SET]:** ARCTIC, ATLANTIC, PACIFIC, SOUTHERN
* **Level 1 (SOURCES OF DISTINCTIVE SMELLS) [Type: SEMANTIC_SET]:** AMMONIA, BO, DURIAN, WET DOG
* **Level 2 (KINDS OF ROOMS IN A MANSION) [Type: FILL_IN_THE_BLANK]:** BILLIARD, DRAWING, POWDER, READING
* **Level 3 (WHAT "PA" MIGHT REFER TO) [Type: WORDPLAY_TRANSFORM]:** FATHER, PENNSYLVANIA, PROTACTINIUM, PUBLIC ADDRESS

### Top Candidate Partitions:
1. **Partition Score: 0.4677**
   - Group 1: **0.6880** | ATLANTIC, ARCTIC, PACIFIC, SOUTHERN                               | CORRECT GROUP (OCEANS, Level 0)
   - Group 2: **0.5100** | BILLIARD, DRAWING, POWDER, READING                                | CORRECT GROUP (KINDS OF ROOMS IN A MANSION, Level 2) | [Pred Type: FILL_IN_THE_BLANK (51.6%, no-rel 21.4%)]
   - Group 3: **0.4259** | PROTACTINIUM, PUBLIC ADDRESS, PENNSYLVANIA, AMMONIA               | INCORRECT (Max overlap: 3/4 with WHAT "PA" MIGHT REFER TO)
   - Group 4: **0.4191** | FATHER, BO, DURIAN, WET DOG                                       | INCORRECT (Max overlap: 3/4 with SOURCES OF DISTINCTIVE SMELLS)
2. **Partition Score: 0.4568**
   - Group 1: **0.5130** | ATLANTIC, ARCTIC, WET DOG, PACIFIC                                | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 2: **0.5100** | BILLIARD, DRAWING, POWDER, READING                                | CORRECT GROUP (KINDS OF ROOMS IN A MANSION, Level 2) | [Pred Type: FILL_IN_THE_BLANK (51.6%, no-rel 21.4%)]
   - Group 3: **0.4541** | FATHER, BO, DURIAN, SOUTHERN                                      | INCORRECT (Max overlap: 2/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 4: **0.4259** | PROTACTINIUM, PUBLIC ADDRESS, PENNSYLVANIA, AMMONIA               | INCORRECT (Max overlap: 3/4 with WHAT "PA" MIGHT REFER TO)
3. **Partition Score: 0.4539**
   - Group 1: **0.5303** | ATLANTIC, FATHER, ARCTIC, PACIFIC                                 | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 2: **0.5100** | BILLIARD, DRAWING, POWDER, READING                                | CORRECT GROUP (KINDS OF ROOMS IN A MANSION, Level 2) | [Pred Type: FILL_IN_THE_BLANK (51.6%, no-rel 21.4%)]
   - Group 3: **0.4283** | BO, DURIAN, WET DOG, SOUTHERN                                     | INCORRECT (Max overlap: 3/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 4: **0.4259** | PROTACTINIUM, PUBLIC ADDRESS, PENNSYLVANIA, AMMONIA               | INCORRECT (Max overlap: 3/4 with WHAT "PA" MIGHT REFER TO)
4. **Partition Score: 0.4514**
   - Group 1: **0.5100** | BILLIARD, DRAWING, POWDER, READING                                | CORRECT GROUP (KINDS OF ROOMS IN A MANSION, Level 2) | [Pred Type: FILL_IN_THE_BLANK (51.6%, no-rel 21.4%)]
   - Group 2: **0.4705** | BO, ARCTIC, DURIAN, SOUTHERN                                      | INCORRECT (Max overlap: 2/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 3: **0.4667** | ATLANTIC, FATHER, WET DOG, PACIFIC                                | INCORRECT (Max overlap: 2/4 with OCEANS)
   - Group 4: **0.4259** | PROTACTINIUM, PUBLIC ADDRESS, PENNSYLVANIA, AMMONIA               | INCORRECT (Max overlap: 3/4 with WHAT "PA" MIGHT REFER TO)
5. **Partition Score: 0.4477**
   - Group 1: **0.5100** | BILLIARD, DRAWING, POWDER, READING                                | CORRECT GROUP (KINDS OF ROOMS IN A MANSION, Level 2) | [Pred Type: FILL_IN_THE_BLANK (51.6%, no-rel 21.4%)]
   - Group 2: **0.5054** | ATLANTIC, WET DOG, PACIFIC, SOUTHERN                              | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 3: **0.4259** | PROTACTINIUM, PUBLIC ADDRESS, PENNSYLVANIA, AMMONIA               | INCORRECT (Max overlap: 3/4 with WHAT "PA" MIGHT REFER TO)
   - Group 4: **0.4210** | FATHER, BO, ARCTIC, DURIAN                                        | INCORRECT (Max overlap: 2/4 with SOURCES OF DISTINCTIVE SMELLS)

### Top Candidate Groups:
   - Group 1: **0.6880** | ATLANTIC, ARCTIC, PACIFIC, SOUTHERN                               | CORRECT GROUP (OCEANS, Level 0)
   - Group 2: **0.5100** | BILLIARD, DRAWING, POWDER, READING                                | CORRECT GROUP (KINDS OF ROOMS IN A MANSION, Level 2) | [Pred Type: FILL_IN_THE_BLANK (51.6%, no-rel 21.4%)]
   - Group 3: **0.4259** | PROTACTINIUM, PUBLIC ADDRESS, PENNSYLVANIA, AMMONIA               | INCORRECT (Max overlap: 3/4 with WHAT "PA" MIGHT REFER TO)
   - Group 4: **0.4191** | FATHER, BO, DURIAN, WET DOG                                       | INCORRECT (Max overlap: 3/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 5: **0.5130** | ATLANTIC, ARCTIC, WET DOG, PACIFIC                                | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 6: **0.4541** | FATHER, BO, DURIAN, SOUTHERN                                      | INCORRECT (Max overlap: 2/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 7: **0.5303** | ATLANTIC, FATHER, ARCTIC, PACIFIC                                 | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 8: **0.4283** | BO, DURIAN, WET DOG, SOUTHERN                                     | INCORRECT (Max overlap: 3/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 9: **0.4705** | BO, ARCTIC, DURIAN, SOUTHERN                                      | INCORRECT (Max overlap: 2/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 10: **0.4667** | ATLANTIC, FATHER, WET DOG, PACIFIC                                | INCORRECT (Max overlap: 2/4 with OCEANS)
   - Group 11: **0.5054** | ATLANTIC, WET DOG, PACIFIC, SOUTHERN                              | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 12: **0.4210** | FATHER, BO, ARCTIC, DURIAN                                        | INCORRECT (Max overlap: 2/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 13: **0.4603** | ATLANTIC, ARCTIC, DURIAN, PACIFIC                                 | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 14: **0.4562** | FATHER, BO, WET DOG, SOUTHERN                                     | INCORRECT (Max overlap: 2/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 15: **0.4147** | BO, AMMONIA, DURIAN, WET DOG                                      | CORRECT GROUP (SOURCES OF DISTINCTIVE SMELLS, Level 1)
   - Group 16: **0.4131** | PROTACTINIUM, PUBLIC ADDRESS, PENNSYLVANIA, SOUTHERN              | INCORRECT (Max overlap: 3/4 with WHAT "PA" MIGHT REFER TO) | [Pred Type: NAMED_ENTITY_SET (46.6%, no-rel 16.6%)]
   - Group 17: **0.4234** | FATHER, BO, AMMONIA, DURIAN                                       | INCORRECT (Max overlap: 3/4 with SOURCES OF DISTINCTIVE SMELLS)
   - Group 18: **0.5056** | ATLANTIC, ARCTIC, AMMONIA, PACIFIC                                | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 19: **0.5021** | ATLANTIC, FATHER, ARCTIC, SOUTHERN                                | INCORRECT (Max overlap: 3/4 with OCEANS)
   - Group 20: **0.4171** | PROTACTINIUM, PUBLIC ADDRESS, PENNSYLVANIA, PACIFIC               | INCORRECT (Max overlap: 3/4 with WHAT "PA" MIGHT REFER TO) | [Pred Type: NAMED_ENTITY_SET (45.8%, no-rel 16.6%)]

---

## Puzzle 3 (ID: 190)
**Words on Board:** PARK, FIFTH, HAPPY, CHIEF, BROADWAY, JIFFY, FLASH, MAIN, PRINCIPAL, MADISON, WINK, ELEVENTH, FIRST, AMATEUR, RUSH, SECOND

### Ground Truth Categories:
* **Level 0 (BRIEF MOMENT) [Type: SYNONYM_OR_NEAR]:** FLASH, JIFFY, SECOND, WINK
* **Level 1 (PRIMARY) [Type: SYNONYM_OR_NEAR]:** CHIEF, FIRST, MAIN, PRINCIPAL
* **Level 2 (AVENUES IN N.Y.C.) [Type: NAMED_ENTITY_SET]:** BROADWAY, FIFTH, MADISON, PARK
* **Level 3 (___ HOUR) [Type: FILL_IN_THE_BLANK]:** AMATEUR, ELEVENTH, HAPPY, RUSH

### Top Candidate Partitions:
1. **Partition Score: 0.5506**
   - Group 1: **0.8498** | FIFTH, ELEVENTH, FIRST, SECOND                                    | INCORRECT (Max overlap: 1/4 with AVENUES IN N.Y.C.)
   - Group 2: **0.6363** | CHIEF, MAIN, PRINCIPAL, AMATEUR                                   | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (66.5%, no-rel 22.4%)]
   - Group 3: **0.5591** | JIFFY, FLASH, WINK, RUSH                                          | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (63.3%, no-rel 22.5%)]
   - Group 4: **0.4504** | PARK, HAPPY, BROADWAY, MADISON                                    | INCORRECT (Max overlap: 3/4 with AVENUES IN N.Y.C.)
2. **Partition Score: 0.5425**
   - Group 1: **0.6761** | PARK, FIFTH, FIRST, SECOND                                        | INCORRECT (Max overlap: 2/4 with AVENUES IN N.Y.C.)
   - Group 2: **0.6363** | CHIEF, MAIN, PRINCIPAL, AMATEUR                                   | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (66.5%, no-rel 22.4%)]
   - Group 3: **0.5591** | JIFFY, FLASH, WINK, RUSH                                          | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (63.3%, no-rel 22.5%)]
   - Group 4: **0.4727** | HAPPY, BROADWAY, MADISON, ELEVENTH                                | INCORRECT (Max overlap: 2/4 with ___ HOUR)
3. **Partition Score: 0.5298**
   - Group 1: **0.8498** | FIFTH, ELEVENTH, FIRST, SECOND                                    | INCORRECT (Max overlap: 1/4 with AVENUES IN N.Y.C.)
   - Group 2: **0.5493** | CHIEF, MAIN, PRINCIPAL, RUSH                                      | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (62.2%, no-rel 27.1%)]
   - Group 3: **0.5351** | JIFFY, FLASH, WINK, AMATEUR                                       | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (65.5%, no-rel 19.6%)]
   - Group 4: **0.4504** | PARK, HAPPY, BROADWAY, MADISON                                    | INCORRECT (Max overlap: 3/4 with AVENUES IN N.Y.C.)
4. **Partition Score: 0.5282**
   - Group 1: **0.6761** | PARK, FIFTH, FIRST, SECOND                                        | INCORRECT (Max overlap: 2/4 with AVENUES IN N.Y.C.)
   - Group 2: **0.5591** | JIFFY, FLASH, WINK, RUSH                                          | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (63.3%, no-rel 22.5%)]
   - Group 3: **0.5404** | HAPPY, CHIEF, MAIN, PRINCIPAL                                     | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (63.0%, no-rel 23.0%)]
   - Group 4: **0.4799** | BROADWAY, MADISON, ELEVENTH, AMATEUR                              | INCORRECT (Max overlap: 2/4 with AVENUES IN N.Y.C.)
5. **Partition Score: 0.5259**
   - Group 1: **0.8498** | FIFTH, ELEVENTH, FIRST, SECOND                                    | INCORRECT (Max overlap: 1/4 with AVENUES IN N.Y.C.)
   - Group 2: **0.5591** | JIFFY, FLASH, WINK, RUSH                                          | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (63.3%, no-rel 22.5%)]
   - Group 3: **0.5404** | HAPPY, CHIEF, MAIN, PRINCIPAL                                     | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (63.0%, no-rel 23.0%)]
   - Group 4: **0.4374** | PARK, BROADWAY, MADISON, AMATEUR                                  | INCORRECT (Max overlap: 3/4 with AVENUES IN N.Y.C.)

### Top Candidate Groups:
   - Group 1: **0.8498** | FIFTH, ELEVENTH, FIRST, SECOND                                    | INCORRECT (Max overlap: 1/4 with AVENUES IN N.Y.C.)
   - Group 2: **0.6363** | CHIEF, MAIN, PRINCIPAL, AMATEUR                                   | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (66.5%, no-rel 22.4%)]
   - Group 3: **0.5591** | JIFFY, FLASH, WINK, RUSH                                          | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (63.3%, no-rel 22.5%)]
   - Group 4: **0.4504** | PARK, HAPPY, BROADWAY, MADISON                                    | INCORRECT (Max overlap: 3/4 with AVENUES IN N.Y.C.)
   - Group 5: **0.6761** | PARK, FIFTH, FIRST, SECOND                                        | INCORRECT (Max overlap: 2/4 with AVENUES IN N.Y.C.)
   - Group 6: **0.4727** | HAPPY, BROADWAY, MADISON, ELEVENTH                                | INCORRECT (Max overlap: 2/4 with ___ HOUR)
   - Group 7: **0.5493** | CHIEF, MAIN, PRINCIPAL, RUSH                                      | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (62.2%, no-rel 27.1%)]
   - Group 8: **0.5351** | JIFFY, FLASH, WINK, AMATEUR                                       | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (65.5%, no-rel 19.6%)]
   - Group 9: **0.5404** | HAPPY, CHIEF, MAIN, PRINCIPAL                                     | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (63.0%, no-rel 23.0%)]
   - Group 10: **0.4799** | BROADWAY, MADISON, ELEVENTH, AMATEUR                              | INCORRECT (Max overlap: 2/4 with AVENUES IN N.Y.C.)
   - Group 11: **0.4374** | PARK, BROADWAY, MADISON, AMATEUR                                  | INCORRECT (Max overlap: 3/4 with AVENUES IN N.Y.C.)
   - Group 12: **0.4608** | PARK, FLASH, WINK, RUSH                                           | INCORRECT (Max overlap: 2/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 29.8%)]
   - Group 13: **0.4336** | HAPPY, BROADWAY, JIFFY, MADISON                                   | INCORRECT (Max overlap: 2/4 with AVENUES IN N.Y.C.)
   - Group 14: **0.5250** | HAPPY, JIFFY, FLASH, WINK                                         | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (62.1%, no-rel 17.2%)]
   - Group 15: **0.5107** | PARK, JIFFY, FLASH, WINK                                          | INCORRECT (Max overlap: 3/4 with BRIEF MOMENT) | [Pred Type: SYNONYM_OR_NEAR (56.4%, no-rel 19.5%)]
   - Group 16: **0.4454** | HAPPY, BROADWAY, MADISON, AMATEUR                                 | INCORRECT (Max overlap: 2/4 with ___ HOUR)
   - Group 17: **0.4957** | PARK, CHIEF, MAIN, PRINCIPAL                                      | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 23.4%)]
   - Group 18: **0.4486** | BROADWAY, JIFFY, MADISON, AMATEUR                                 | INCORRECT (Max overlap: 2/4 with AVENUES IN N.Y.C.)
   - Group 19: **0.5506** | CHIEF, MAIN, PRINCIPAL, ELEVENTH                                  | INCORRECT (Max overlap: 3/4 with PRIMARY) | [Pred Type: SYNONYM_OR_NEAR (62.5%, no-rel 20.3%)]
   - Group 20: **0.4602** | HAPPY, FLASH, WINK, RUSH                                          | INCORRECT (Max overlap: 2/4 with ___ HOUR) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 33.3%)]

---

## Puzzle 4 (ID: 104)
**Words on Board:** DIP, SINK, KEYS, SPRING, HEALTHY, FOUNTAIN, TAP, SOUND, SWIFT, DROP, FALL, SUMMER, WELL, STRONG, NICKS, FIT

### Ground Truth Categories:
* **Level 0 (ROBUST) [Type: SYNONYM_OR_NEAR]:** FIT, HEALTHY, SOUND, STRONG
* **Level 1 (DECLINE) [Type: SYNONYM_OR_NEAR]:** DIP, DROP, FALL, SINK
* **Level 2 (WATER SOURCES) [Type: SEMANTIC_SET]:** FOUNTAIN, SPRING, TAP, WELL
* **Level 3 (WOMEN SINGERS) [Type: NAMED_ENTITY_SET]:** KEYS, NICKS, SUMMER, SWIFT

### Top Candidate Partitions:
1. **Partition Score: 0.5129**
   - Group 1: **0.7178** | HEALTHY, SOUND, WELL, STRONG                                      | INCORRECT (Max overlap: 3/4 with ROBUST) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 34.4%)]
   - Group 2: **0.5832** | DIP, SINK, DROP, NICKS                                            | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (64.8%, no-rel 18.9%)]
   - Group 3: **0.4795** | SPRING, FOUNTAIN, FALL, SUMMER                                    | INCORRECT (Max overlap: 2/4 with WATER SOURCES)
   - Group 4: **0.4543** | KEYS, TAP, SWIFT, FIT                                             | INCORRECT (Max overlap: 2/4 with WOMEN SINGERS)
2. **Partition Score: 0.5046**
   - Group 1: **0.7178** | HEALTHY, SOUND, WELL, STRONG                                      | INCORRECT (Max overlap: 3/4 with ROBUST) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 34.4%)]
   - Group 2: **0.4795** | SPRING, FOUNTAIN, FALL, SUMMER                                    | INCORRECT (Max overlap: 2/4 with WATER SOURCES)
   - Group 3: **0.4790** | DIP, SINK, SWIFT, DROP                                            | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (63.6%, no-rel 18.0%)]
   - Group 4: **0.4763** | KEYS, TAP, NICKS, FIT                                             | INCORRECT (Max overlap: 2/4 with WOMEN SINGERS)
3. **Partition Score: 0.5022**
   - Group 1: **0.8220** | HEALTHY, SOUND, WELL, FIT                                         | INCORRECT (Max overlap: 3/4 with ROBUST) | [Pred Type: SYNONYM_OR_NEAR (61.2%, no-rel 31.9%)]
   - Group 2: **0.4885** | DIP, SINK, DROP, STRONG                                           | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (64.3%, no-rel 24.8%)]
   - Group 3: **0.4795** | SPRING, FOUNTAIN, FALL, SUMMER                                    | INCORRECT (Max overlap: 2/4 with WATER SOURCES)
   - Group 4: **0.4454** | KEYS, TAP, SWIFT, NICKS                                           | INCORRECT (Max overlap: 3/4 with WOMEN SINGERS)
4. **Partition Score: 0.5001**
   - Group 1: **0.7178** | HEALTHY, SOUND, WELL, STRONG                                      | INCORRECT (Max overlap: 3/4 with ROBUST) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 34.4%)]
   - Group 2: **0.5397** | DIP, SINK, DROP, FIT                                              | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 26.4%)]
   - Group 3: **0.4795** | SPRING, FOUNTAIN, FALL, SUMMER                                    | INCORRECT (Max overlap: 2/4 with WATER SOURCES)
   - Group 4: **0.4454** | KEYS, TAP, SWIFT, NICKS                                           | INCORRECT (Max overlap: 3/4 with WOMEN SINGERS)
5. **Partition Score: 0.4885**
   - Group 1: **0.7178** | HEALTHY, SOUND, WELL, STRONG                                      | INCORRECT (Max overlap: 3/4 with ROBUST) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 34.4%)]
   - Group 2: **0.5113** | DIP, SINK, KEYS, DROP                                             | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 21.8%)]
   - Group 3: **0.4795** | SPRING, FOUNTAIN, FALL, SUMMER                                    | INCORRECT (Max overlap: 2/4 with WATER SOURCES)
   - Group 4: **0.4331** | TAP, SWIFT, NICKS, FIT                                            | INCORRECT (Max overlap: 2/4 with WOMEN SINGERS)

### Top Candidate Groups:
   - Group 1: **0.7178** | HEALTHY, SOUND, WELL, STRONG                                      | INCORRECT (Max overlap: 3/4 with ROBUST) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 34.4%)]
   - Group 2: **0.5832** | DIP, SINK, DROP, NICKS                                            | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (64.8%, no-rel 18.9%)]
   - Group 3: **0.4795** | SPRING, FOUNTAIN, FALL, SUMMER                                    | INCORRECT (Max overlap: 2/4 with WATER SOURCES)
   - Group 4: **0.4543** | KEYS, TAP, SWIFT, FIT                                             | INCORRECT (Max overlap: 2/4 with WOMEN SINGERS)
   - Group 5: **0.4790** | DIP, SINK, SWIFT, DROP                                            | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (63.6%, no-rel 18.0%)]
   - Group 6: **0.4763** | KEYS, TAP, NICKS, FIT                                             | INCORRECT (Max overlap: 2/4 with WOMEN SINGERS)
   - Group 7: **0.8220** | HEALTHY, SOUND, WELL, FIT                                         | INCORRECT (Max overlap: 3/4 with ROBUST) | [Pred Type: SYNONYM_OR_NEAR (61.2%, no-rel 31.9%)]
   - Group 8: **0.4885** | DIP, SINK, DROP, STRONG                                           | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (64.3%, no-rel 24.8%)]
   - Group 9: **0.4454** | KEYS, TAP, SWIFT, NICKS                                           | INCORRECT (Max overlap: 3/4 with WOMEN SINGERS)
   - Group 10: **0.5397** | DIP, SINK, DROP, FIT                                              | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 26.4%)]
   - Group 11: **0.5113** | DIP, SINK, KEYS, DROP                                             | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 21.8%)]
   - Group 12: **0.4331** | TAP, SWIFT, NICKS, FIT                                            | INCORRECT (Max overlap: 2/4 with WOMEN SINGERS)
   - Group 13: **0.4767** | DIP, SINK, FOUNTAIN, DROP                                         | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (60.6%, no-rel 21.3%)]
   - Group 14: **0.4551** | SPRING, FALL, SUMMER, NICKS                                       | INCORRECT (Max overlap: 2/4 with WOMEN SINGERS) | [Pred Type: SEMANTIC_SET (45.4%, no-rel 21.1%)]
   - Group 15: **0.7394** | HEALTHY, SOUND, STRONG, FIT                                       | CORRECT GROUP (ROBUST, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.0%, no-rel 32.7%)]
   - Group 16: **0.4613** | DIP, SINK, DROP, WELL                                             | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (61.3%, no-rel 26.1%)]
   - Group 17: **0.6844** | HEALTHY, WELL, STRONG, FIT                                        | INCORRECT (Max overlap: 3/4 with ROBUST) | [Pred Type: SYNONYM_OR_NEAR (55.8%, no-rel 35.3%)]
   - Group 18: **0.4833** | DIP, SINK, SOUND, DROP                                            | INCORRECT (Max overlap: 3/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 28.9%)]
   - Group 19: **0.4715** | SINK, FOUNTAIN, DROP, WELL                                        | INCORRECT (Max overlap: 2/4 with DECLINE) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 23.8%)]
   - Group 20: **0.4518** | DIP, SPRING, FALL, SUMMER                                         | INCORRECT (Max overlap: 2/4 with DECLINE)

---

## Puzzle 5 (ID: 1052)
**Words on Board:** TREASURY, OPERA, TIMES TABLES, HERALDRY, EDUCATION, EXTRASENSORY, POST-IT, TELEPATHIC, INTERIOR, PLAY, PSYCHIC, MUSICAL, MENTAL, GLOBETROTTER, STATE, BALLET

### Ground Truth Categories:
* **Level 0 (CLAIRVOYANT) [Type: SYNONYM_OR_NEAR]:** EXTRASENSORY, MENTAL, PSYCHIC, TELEPATHIC
* **Level 1 (STAGED PERFORMANCES) [Type: SEMANTIC_SET]:** BALLET, MUSICAL, OPERA, PLAY
* **Level 2 (U.S. CABINET DEPARTMENTS) [Type: NAMED_ENTITY_SET]:** EDUCATION, INTERIOR, STATE, TREASURY
* **Level 3 (STARTING WITH NEWSPAPER NAMES) [Type: WORD_FORM]:** GLOBETROTTER, HERALDRY, POST-IT, TIMES TABLES

### Top Candidate Partitions:
1. **Partition Score: 0.5866**
   - Group 1: **0.7815** | TREASURY, EDUCATION, INTERIOR, STATE                              | CORRECT GROUP (U.S. CABINET DEPARTMENTS, Level 2)
   - Group 2: **0.6504** | EXTRASENSORY, TELEPATHIC, PSYCHIC, MENTAL                         | CORRECT GROUP (CLAIRVOYANT, Level 0)
   - Group 3: **0.5793** | TIMES TABLES, HERALDRY, POST-IT, GLOBETROTTER                     | CORRECT GROUP (STARTING WITH NEWSPAPER NAMES, Level 3)
   - Group 4: **0.5231** | OPERA, PLAY, MUSICAL, BALLET                                      | CORRECT GROUP (STAGED PERFORMANCES, Level 1) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 23.8%)]
2. **Partition Score: 0.5291**
   - Group 1: **0.7815** | TREASURY, EDUCATION, INTERIOR, STATE                              | CORRECT GROUP (U.S. CABINET DEPARTMENTS, Level 2)
   - Group 2: **0.6504** | EXTRASENSORY, TELEPATHIC, PSYCHIC, MENTAL                         | CORRECT GROUP (CLAIRVOYANT, Level 0)
   - Group 3: **0.4621** | TIMES TABLES, HERALDRY, GLOBETROTTER, BALLET                      | INCORRECT (Max overlap: 3/4 with STARTING WITH NEWSPAPER NAMES)
   - Group 4: **0.4538** | OPERA, POST-IT, PLAY, MUSICAL                                     | INCORRECT (Max overlap: 3/4 with STAGED PERFORMANCES) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 16.6%)]
3. **Partition Score: 0.5201**
   - Group 1: **0.7815** | TREASURY, EDUCATION, INTERIOR, STATE                              | CORRECT GROUP (U.S. CABINET DEPARTMENTS, Level 2)
   - Group 2: **0.5793** | TIMES TABLES, HERALDRY, POST-IT, GLOBETROTTER                     | CORRECT GROUP (STARTING WITH NEWSPAPER NAMES, Level 3)
   - Group 3: **0.4631** | TELEPATHIC, PSYCHIC, MENTAL, BALLET                               | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 4: **0.4620** | OPERA, EXTRASENSORY, PLAY, MUSICAL                                | INCORRECT (Max overlap: 3/4 with STAGED PERFORMANCES) | [Pred Type: SYNONYM_OR_NEAR (63.6%, no-rel 21.2%)]
4. **Partition Score: 0.5198**
   - Group 1: **0.7815** | TREASURY, EDUCATION, INTERIOR, STATE                              | CORRECT GROUP (U.S. CABINET DEPARTMENTS, Level 2)
   - Group 2: **0.5303** | EXTRASENSORY, POST-IT, TELEPATHIC, MENTAL                         | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 3: **0.5231** | OPERA, PLAY, MUSICAL, BALLET                                      | CORRECT GROUP (STAGED PERFORMANCES, Level 1) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 23.8%)]
   - Group 4: **0.4573** | TIMES TABLES, HERALDRY, PSYCHIC, GLOBETROTTER                     | INCORRECT (Max overlap: 3/4 with STARTING WITH NEWSPAPER NAMES)
5. **Partition Score: 0.5166**
   - Group 1: **0.7815** | TREASURY, EDUCATION, INTERIOR, STATE                              | CORRECT GROUP (U.S. CABINET DEPARTMENTS, Level 2)
   - Group 2: **0.5793** | TIMES TABLES, HERALDRY, POST-IT, GLOBETROTTER                     | CORRECT GROUP (STARTING WITH NEWSPAPER NAMES, Level 3)
   - Group 3: **0.4950** | OPERA, TELEPATHIC, PLAY, MUSICAL                                  | INCORRECT (Max overlap: 3/4 with STAGED PERFORMANCES) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 22.4%)]
   - Group 4: **0.4434** | EXTRASENSORY, PSYCHIC, MENTAL, BALLET                             | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)

### Top Candidate Groups:
   - Group 1: **0.7815** | TREASURY, EDUCATION, INTERIOR, STATE                              | CORRECT GROUP (U.S. CABINET DEPARTMENTS, Level 2)
   - Group 2: **0.6504** | EXTRASENSORY, TELEPATHIC, PSYCHIC, MENTAL                         | CORRECT GROUP (CLAIRVOYANT, Level 0)
   - Group 3: **0.5793** | TIMES TABLES, HERALDRY, POST-IT, GLOBETROTTER                     | CORRECT GROUP (STARTING WITH NEWSPAPER NAMES, Level 3)
   - Group 4: **0.5231** | OPERA, PLAY, MUSICAL, BALLET                                      | CORRECT GROUP (STAGED PERFORMANCES, Level 1) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 23.8%)]
   - Group 5: **0.4621** | TIMES TABLES, HERALDRY, GLOBETROTTER, BALLET                      | INCORRECT (Max overlap: 3/4 with STARTING WITH NEWSPAPER NAMES)
   - Group 6: **0.4538** | OPERA, POST-IT, PLAY, MUSICAL                                     | INCORRECT (Max overlap: 3/4 with STAGED PERFORMANCES) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 16.6%)]
   - Group 7: **0.4631** | TELEPATHIC, PSYCHIC, MENTAL, BALLET                               | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 8: **0.4620** | OPERA, EXTRASENSORY, PLAY, MUSICAL                                | INCORRECT (Max overlap: 3/4 with STAGED PERFORMANCES) | [Pred Type: SYNONYM_OR_NEAR (63.6%, no-rel 21.2%)]
   - Group 9: **0.5303** | EXTRASENSORY, POST-IT, TELEPATHIC, MENTAL                         | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 10: **0.4573** | TIMES TABLES, HERALDRY, PSYCHIC, GLOBETROTTER                     | INCORRECT (Max overlap: 3/4 with STARTING WITH NEWSPAPER NAMES)
   - Group 11: **0.4950** | OPERA, TELEPATHIC, PLAY, MUSICAL                                  | INCORRECT (Max overlap: 3/4 with STAGED PERFORMANCES) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 22.4%)]
   - Group 12: **0.4434** | EXTRASENSORY, PSYCHIC, MENTAL, BALLET                             | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 13: **0.5208** | EXTRASENSORY, POST-IT, PSYCHIC, MENTAL                            | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 14: **0.4551** | EXTRASENSORY, TELEPATHIC, PSYCHIC, BALLET                         | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 15: **0.4547** | OPERA, PLAY, MUSICAL, MENTAL                                      | INCORRECT (Max overlap: 3/4 with STAGED PERFORMANCES) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 24.4%)]
   - Group 16: **0.4404** | TIMES TABLES, POST-IT, GLOBETROTTER, BALLET                       | INCORRECT (Max overlap: 3/4 with STARTING WITH NEWSPAPER NAMES)
   - Group 17: **0.4317** | OPERA, HERALDRY, PLAY, MUSICAL                                    | INCORRECT (Max overlap: 3/4 with STAGED PERFORMANCES) | [Pred Type: SYNONYM_OR_NEAR (60.3%, no-rel 15.6%)]
   - Group 18: **0.5392** | POST-IT, TELEPATHIC, PSYCHIC, MENTAL                              | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 19: **0.5212** | HERALDRY, EXTRASENSORY, TELEPATHIC, MENTAL                        | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 20: **0.4418** | TIMES TABLES, POST-IT, PSYCHIC, GLOBETROTTER                      | INCORRECT (Max overlap: 3/4 with STARTING WITH NEWSPAPER NAMES)

---

## Puzzle 6 (ID: 818)
**Words on Board:** BURST, CHORAL, DIVINE, SPLIT, SHADE, BLEW, SPIRIT, FORECAST, READ, BROKE, WIGHT, JAZZ, AMERICANA, SPECTER, CALL, RAP

### Ground Truth Categories:
* **Level 0 (RUPTURED) [Type: SYNONYM_OR_NEAR]:** BLEW, BROKE, BURST, SPLIT
* **Level 1 (APPARITION) [Type: SYNONYM_OR_NEAR]:** SHADE, SPECTER, SPIRIT, WIGHT
* **Level 2 (PREDICT) [Type: SYNONYM_OR_NEAR]:** CALL, DIVINE, FORECAST, READ
* **Level 3 ("BEST ___ PERFORMANCE" GRAMMY AWARD) [Type: FILL_IN_THE_BLANK]:** AMERICANA, CHORAL, JAZZ, RAP

### Top Candidate Partitions:
1. **Partition Score: 0.5095**
   - Group 1: **0.5623** | CHORAL, JAZZ, AMERICANA, RAP                                      | CORRECT GROUP ("BEST ___ PERFORMANCE" GRAMMY AWARD, Level 3)
   - Group 2: **0.5262** | BURST, SPLIT, SHADE, BROKE                                        | INCORRECT (Max overlap: 3/4 with RUPTURED) | [Pred Type: SYNONYM_OR_NEAR (62.3%, no-rel 29.0%)]
   - Group 3: **0.4971** | BLEW, FORECAST, READ, CALL                                        | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 4: **0.4964** | DIVINE, SPIRIT, WIGHT, SPECTER                                    | INCORRECT (Max overlap: 3/4 with APPARITION)
2. **Partition Score: 0.5093**
   - Group 1: **0.6932** | BURST, SPLIT, BLEW, BROKE                                         | CORRECT GROUP (RUPTURED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (70.5%, no-rel 22.2%)]
   - Group 2: **0.5623** | CHORAL, JAZZ, AMERICANA, RAP                                      | CORRECT GROUP ("BEST ___ PERFORMANCE" GRAMMY AWARD, Level 3)
   - Group 3: **0.4964** | DIVINE, SPIRIT, WIGHT, SPECTER                                    | INCORRECT (Max overlap: 3/4 with APPARITION)
   - Group 4: **0.4542** | SHADE, FORECAST, READ, CALL                                       | INCORRECT (Max overlap: 3/4 with PREDICT)
3. **Partition Score: 0.5065**
   - Group 1: **0.6932** | BURST, SPLIT, BLEW, BROKE                                         | CORRECT GROUP (RUPTURED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (70.5%, no-rel 22.2%)]
   - Group 2: **0.5568** | DIVINE, SHADE, SPIRIT, SPECTER                                    | INCORRECT (Max overlap: 3/4 with APPARITION)
   - Group 3: **0.4666** | CHORAL, FORECAST, READ, CALL                                      | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 4: **0.4618** | WIGHT, JAZZ, AMERICANA, RAP                                       | INCORRECT (Max overlap: 3/4 with "BEST ___ PERFORMANCE" GRAMMY AWARD)
4. **Partition Score: 0.4974**
   - Group 1: **0.6932** | BURST, SPLIT, BLEW, BROKE                                         | CORRECT GROUP (RUPTURED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (70.5%, no-rel 22.2%)]
   - Group 2: **0.4912** | SHADE, SPIRIT, WIGHT, SPECTER                                     | CORRECT GROUP (APPARITION, Level 1)
   - Group 3: **0.4702** | DIVINE, JAZZ, AMERICANA, RAP                                      | INCORRECT (Max overlap: 3/4 with "BEST ___ PERFORMANCE" GRAMMY AWARD)
   - Group 4: **0.4666** | CHORAL, FORECAST, READ, CALL                                      | INCORRECT (Max overlap: 3/4 with PREDICT)
5. **Partition Score: 0.4925**
   - Group 1: **0.5623** | CHORAL, JAZZ, AMERICANA, RAP                                      | CORRECT GROUP ("BEST ___ PERFORMANCE" GRAMMY AWARD, Level 3)
   - Group 2: **0.5203** | BURST, FORECAST, READ, CALL                                       | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 3: **0.4964** | DIVINE, SPIRIT, WIGHT, SPECTER                                    | INCORRECT (Max overlap: 3/4 with APPARITION)
   - Group 4: **0.4656** | SPLIT, SHADE, BLEW, BROKE                                         | INCORRECT (Max overlap: 3/4 with RUPTURED) | [Pred Type: SYNONYM_OR_NEAR (52.8%, no-rel 28.1%)]

### Top Candidate Groups:
   - Group 1: **0.5623** | CHORAL, JAZZ, AMERICANA, RAP                                      | CORRECT GROUP ("BEST ___ PERFORMANCE" GRAMMY AWARD, Level 3)
   - Group 2: **0.5262** | BURST, SPLIT, SHADE, BROKE                                        | INCORRECT (Max overlap: 3/4 with RUPTURED) | [Pred Type: SYNONYM_OR_NEAR (62.3%, no-rel 29.0%)]
   - Group 3: **0.4971** | BLEW, FORECAST, READ, CALL                                        | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 4: **0.4964** | DIVINE, SPIRIT, WIGHT, SPECTER                                    | INCORRECT (Max overlap: 3/4 with APPARITION)
   - Group 5: **0.6932** | BURST, SPLIT, BLEW, BROKE                                         | CORRECT GROUP (RUPTURED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (70.5%, no-rel 22.2%)]
   - Group 6: **0.4542** | SHADE, FORECAST, READ, CALL                                       | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 7: **0.5568** | DIVINE, SHADE, SPIRIT, SPECTER                                    | INCORRECT (Max overlap: 3/4 with APPARITION)
   - Group 8: **0.4666** | CHORAL, FORECAST, READ, CALL                                      | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 9: **0.4618** | WIGHT, JAZZ, AMERICANA, RAP                                       | INCORRECT (Max overlap: 3/4 with "BEST ___ PERFORMANCE" GRAMMY AWARD)
   - Group 10: **0.4912** | SHADE, SPIRIT, WIGHT, SPECTER                                     | CORRECT GROUP (APPARITION, Level 1)
   - Group 11: **0.4702** | DIVINE, JAZZ, AMERICANA, RAP                                      | INCORRECT (Max overlap: 3/4 with "BEST ___ PERFORMANCE" GRAMMY AWARD)
   - Group 12: **0.5203** | BURST, FORECAST, READ, CALL                                       | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 13: **0.4656** | SPLIT, SHADE, BLEW, BROKE                                         | INCORRECT (Max overlap: 3/4 with RUPTURED) | [Pred Type: SYNONYM_OR_NEAR (52.8%, no-rel 28.1%)]
   - Group 14: **0.4740** | BURST, DIVINE, SPLIT, BROKE                                       | INCORRECT (Max overlap: 3/4 with RUPTURED) | [Pred Type: SYNONYM_OR_NEAR (73.5%, no-rel 16.0%)]
   - Group 15: **0.4560** | FORECAST, READ, SPECTER, CALL                                     | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 16: **0.4335** | DIVINE, SHADE, SPIRIT, WIGHT                                      | INCORRECT (Max overlap: 3/4 with APPARITION)
   - Group 17: **0.4768** | SPIRIT, FORECAST, READ, CALL                                      | INCORRECT (Max overlap: 3/4 with PREDICT)
   - Group 18: **0.4252** | DIVINE, SHADE, WIGHT, SPECTER                                     | INCORRECT (Max overlap: 3/4 with APPARITION)
   - Group 19: **0.4979** | CHORAL, DIVINE, SPIRIT, SPECTER                                   | INCORRECT (Max overlap: 2/4 with APPARITION)
   - Group 20: **0.5111** | BURST, CHORAL, SPLIT, BROKE                                       | INCORRECT (Max overlap: 3/4 with RUPTURED) | [Pred Type: SYNONYM_OR_NEAR (72.7%, no-rel 12.7%)]

---

## Puzzle 7 (ID: 516)
**Words on Board:** DILL, CAPER, STUNT, KOSHER, SOUR, SUGGESTIVE, MUSTARD, EXPLOIT, ANTIC, DECK, SPICY, BLUE, CORD, CHEESE, ADULT, SWEET

### Ground Truth Categories:
* **Level 0 (ESCAPADE) [Type: SYNONYM_OR_NEAR]:** ANTIC, CAPER, EXPLOIT, STUNT
* **Level 1 (KINDS OF PICKLES) [Type: SEMANTIC_SET]:** DILL, KOSHER, SOUR, SWEET
* **Level 2 (RISQUÉ) [Type: SYNONYM_OR_NEAR]:** ADULT, BLUE, SPICY, SUGGESTIVE
* **Level 3 (CUT THE ___) [Type: FILL_IN_THE_BLANK]:** CHEESE, CORD, DECK, MUSTARD

### Top Candidate Partitions:
1. **Partition Score: 0.4767**
   - Group 1: **0.5317** | STUNT, SUGGESTIVE, EXPLOIT, ADULT                                 | INCORRECT (Max overlap: 2/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 22.9%)]
   - Group 2: **0.4905** | DECK, BLUE, CORD, CHEESE                                          | INCORRECT (Max overlap: 3/4 with CUT THE ___)
   - Group 3: **0.4890** | CAPER, SOUR, ANTIC, SPICY                                         | INCORRECT (Max overlap: 2/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (70.1%, no-rel 19.9%)]
   - Group 4: **0.4550** | DILL, KOSHER, MUSTARD, SWEET                                      | INCORRECT (Max overlap: 3/4 with KINDS OF PICKLES) | [Pred Type: FILL_IN_THE_BLANK (53.4%, no-rel 11.1%)]
2. **Partition Score: 0.4734**
   - Group 1: **0.5095** | STUNT, EXPLOIT, SPICY, ADULT                                      | INCORRECT (Max overlap: 2/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 23.2%)]
   - Group 2: **0.4905** | DECK, BLUE, CORD, CHEESE                                          | INCORRECT (Max overlap: 3/4 with CUT THE ___)
   - Group 3: **0.4848** | CAPER, SOUR, SUGGESTIVE, ANTIC                                    | INCORRECT (Max overlap: 2/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (68.8%, no-rel 19.7%)]
   - Group 4: **0.4550** | DILL, KOSHER, MUSTARD, SWEET                                      | INCORRECT (Max overlap: 3/4 with KINDS OF PICKLES) | [Pred Type: FILL_IN_THE_BLANK (53.4%, no-rel 11.1%)]
3. **Partition Score: 0.4726**
   - Group 1: **0.5531** | SOUR, SUGGESTIVE, SPICY, SWEET                                    | INCORRECT (Max overlap: 2/4 with KINDS OF PICKLES)
   - Group 2: **0.4991** | DILL, KOSHER, MUSTARD, CORD                                       | INCORRECT (Max overlap: 2/4 with KINDS OF PICKLES)
   - Group 3: **0.4854** | CAPER, STUNT, EXPLOIT, ANTIC                                      | CORRECT GROUP (ESCAPADE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (72.2%, no-rel 18.3%)]
   - Group 4: **0.4405** | DECK, BLUE, CHEESE, ADULT                                         | INCORRECT (Max overlap: 2/4 with CUT THE ___)
4. **Partition Score: 0.4711**
   - Group 1: **0.4968** | STUNT, SUGGESTIVE, SPICY, ADULT                                   | INCORRECT (Max overlap: 3/4 with RISQUÉ) | [Pred Type: SYNONYM_OR_NEAR (46.8%, no-rel 24.5%)]
   - Group 2: **0.4905** | DECK, BLUE, CORD, CHEESE                                          | INCORRECT (Max overlap: 3/4 with CUT THE ___)
   - Group 3: **0.4804** | CAPER, SOUR, EXPLOIT, ANTIC                                       | INCORRECT (Max overlap: 3/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (68.6%, no-rel 20.6%)]
   - Group 4: **0.4550** | DILL, KOSHER, MUSTARD, SWEET                                      | INCORRECT (Max overlap: 3/4 with KINDS OF PICKLES) | [Pred Type: FILL_IN_THE_BLANK (53.4%, no-rel 11.1%)]
5. **Partition Score: 0.4709**
   - Group 1: **0.5531** | SOUR, SUGGESTIVE, SPICY, SWEET                                    | INCORRECT (Max overlap: 2/4 with KINDS OF PICKLES)
   - Group 2: **0.4854** | CAPER, STUNT, EXPLOIT, ANTIC                                      | CORRECT GROUP (ESCAPADE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (72.2%, no-rel 18.3%)]
   - Group 3: **0.4752** | DILL, KOSHER, DECK, CORD                                          | INCORRECT (Max overlap: 2/4 with KINDS OF PICKLES)
   - Group 4: **0.4461** | MUSTARD, BLUE, CHEESE, ADULT                                      | INCORRECT (Max overlap: 2/4 with CUT THE ___)

### Top Candidate Groups:
   - Group 1: **0.5317** | STUNT, SUGGESTIVE, EXPLOIT, ADULT                                 | INCORRECT (Max overlap: 2/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 22.9%)]
   - Group 2: **0.4905** | DECK, BLUE, CORD, CHEESE                                          | INCORRECT (Max overlap: 3/4 with CUT THE ___)
   - Group 3: **0.4890** | CAPER, SOUR, ANTIC, SPICY                                         | INCORRECT (Max overlap: 2/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (70.1%, no-rel 19.9%)]
   - Group 4: **0.4550** | DILL, KOSHER, MUSTARD, SWEET                                      | INCORRECT (Max overlap: 3/4 with KINDS OF PICKLES) | [Pred Type: FILL_IN_THE_BLANK (53.4%, no-rel 11.1%)]
   - Group 5: **0.5095** | STUNT, EXPLOIT, SPICY, ADULT                                      | INCORRECT (Max overlap: 2/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 23.2%)]
   - Group 6: **0.4848** | CAPER, SOUR, SUGGESTIVE, ANTIC                                    | INCORRECT (Max overlap: 2/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (68.8%, no-rel 19.7%)]
   - Group 7: **0.5531** | SOUR, SUGGESTIVE, SPICY, SWEET                                    | INCORRECT (Max overlap: 2/4 with KINDS OF PICKLES)
   - Group 8: **0.4991** | DILL, KOSHER, MUSTARD, CORD                                       | INCORRECT (Max overlap: 2/4 with KINDS OF PICKLES)
   - Group 9: **0.4854** | CAPER, STUNT, EXPLOIT, ANTIC                                      | CORRECT GROUP (ESCAPADE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (72.2%, no-rel 18.3%)]
   - Group 10: **0.4405** | DECK, BLUE, CHEESE, ADULT                                         | INCORRECT (Max overlap: 2/4 with CUT THE ___)
   - Group 11: **0.4968** | STUNT, SUGGESTIVE, SPICY, ADULT                                   | INCORRECT (Max overlap: 3/4 with RISQUÉ) | [Pred Type: SYNONYM_OR_NEAR (46.8%, no-rel 24.5%)]
   - Group 12: **0.4804** | CAPER, SOUR, EXPLOIT, ANTIC                                       | INCORRECT (Max overlap: 3/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (68.6%, no-rel 20.6%)]
   - Group 13: **0.4752** | DILL, KOSHER, DECK, CORD                                          | INCORRECT (Max overlap: 2/4 with KINDS OF PICKLES)
   - Group 14: **0.4461** | MUSTARD, BLUE, CHEESE, ADULT                                      | INCORRECT (Max overlap: 2/4 with CUT THE ___)
   - Group 15: **0.5895** | CAPER, SUGGESTIVE, EXPLOIT, ANTIC                                 | INCORRECT (Max overlap: 3/4 with ESCAPADE) | [Pred Type: SYNONYM_OR_NEAR (68.2%, no-rel 22.7%)]
   - Group 16: **0.4964** | DILL, DECK, CORD, CHEESE                                          | INCORRECT (Max overlap: 3/4 with CUT THE ___)
   - Group 17: **0.4956** | STUNT, SPICY, BLUE, ADULT                                         | INCORRECT (Max overlap: 3/4 with RISQUÉ) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 27.8%)]
   - Group 18: **0.4242** | KOSHER, SOUR, MUSTARD, SWEET                                      | INCORRECT (Max overlap: 3/4 with KINDS OF PICKLES)
   - Group 19: **0.4456** | STUNT, SOUR, SPICY, SWEET                                         | INCORRECT (Max overlap: 2/4 with KINDS OF PICKLES)
   - Group 20: **0.4846** | KOSHER, DECK, CORD, CHEESE                                        | INCORRECT (Max overlap: 3/4 with CUT THE ___)

---

## Puzzle 8 (ID: 238)
**Words on Board:** BIT, VANILLA, TEA, DRY, DULL, BORING, COCOA, ACT, MATE, DIRTY, TWIST, ROUTINE, UP, MUNDANE, COFFEE, SET

### Ground Truth Categories:
* **Level 0 (DRINKS WITH CAFFEINE) [Type: SEMANTIC_SET]:** COCOA, COFFEE, MATE, TEA
* **Level 1 (UNEXCITING) [Type: SYNONYM_OR_NEAR]:** BORING, DULL, MUNDANE, VANILLA
* **Level 2 (COMEDIAN’S PERFORMANCE) [Type: SYNONYM_OR_NEAR]:** ACT, BIT, ROUTINE, SET
* **Level 3 (MARTINI SPECIFICATIONS) [Type: SEMANTIC_SET]:** DIRTY, DRY, TWIST, UP

### Top Candidate Partitions:
1. **Partition Score: 0.5361**
   - Group 1: **0.6822** | TEA, COCOA, MATE, COFFEE                                          | CORRECT GROUP (DRINKS WITH CAFFEINE, Level 0)
   - Group 2: **0.6671** | DRY, DIRTY, UP, SET                                               | INCORRECT (Max overlap: 3/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 33.4%)]
   - Group 3: **0.5027** | BIT, ACT, TWIST, ROUTINE                                          | INCORRECT (Max overlap: 3/4 with COMEDIAN’S PERFORMANCE) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 37.8%)]
   - Group 4: **0.4683** | VANILLA, DULL, BORING, MUNDANE                                    | CORRECT GROUP (UNEXCITING, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.1%, no-rel 22.6%)]
2. **Partition Score: 0.5273**
   - Group 1: **0.6822** | TEA, COCOA, MATE, COFFEE                                          | CORRECT GROUP (DRINKS WITH CAFFEINE, Level 0)
   - Group 2: **0.6217** | DRY, DULL, DIRTY, SET                                             | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS)
   - Group 3: **0.4901** | BIT, ACT, TWIST, UP                                               | INCORRECT (Max overlap: 2/4 with COMEDIAN’S PERFORMANCE)
   - Group 4: **0.4723** | VANILLA, BORING, ROUTINE, MUNDANE                                 | INCORRECT (Max overlap: 3/4 with UNEXCITING) | [Pred Type: SYNONYM_OR_NEAR (47.8%, no-rel 25.8%)]
3. **Partition Score: 0.4997**
   - Group 1: **0.6822** | TEA, COCOA, MATE, COFFEE                                          | CORRECT GROUP (DRINKS WITH CAFFEINE, Level 0)
   - Group 2: **0.4847** | DRY, DULL, UP, SET                                                | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 34.7%)]
   - Group 3: **0.4798** | BIT, ACT, DIRTY, TWIST                                            | INCORRECT (Max overlap: 2/4 with COMEDIAN’S PERFORMANCE)
   - Group 4: **0.4723** | VANILLA, BORING, ROUTINE, MUNDANE                                 | INCORRECT (Max overlap: 3/4 with UNEXCITING) | [Pred Type: SYNONYM_OR_NEAR (47.8%, no-rel 25.8%)]
4. **Partition Score: 0.4922**
   - Group 1: **0.6822** | TEA, COCOA, MATE, COFFEE                                          | CORRECT GROUP (DRINKS WITH CAFFEINE, Level 0)
   - Group 2: **0.6671** | DRY, DIRTY, UP, SET                                               | INCORRECT (Max overlap: 3/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 33.4%)]
   - Group 3: **0.4165** | BIT, VANILLA, ACT, ROUTINE                                        | INCORRECT (Max overlap: 3/4 with COMEDIAN’S PERFORMANCE) | [Pred Type: SYNONYM_OR_NEAR (53.3%, no-rel 23.6%)]
   - Group 4: **0.4143** | DULL, BORING, TWIST, MUNDANE                                      | INCORRECT (Max overlap: 3/4 with UNEXCITING) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 35.3%)]
5. **Partition Score: 0.4907**
   - Group 1: **0.6822** | TEA, COCOA, MATE, COFFEE                                          | CORRECT GROUP (DRINKS WITH CAFFEINE, Level 0)
   - Group 2: **0.4901** | BIT, ACT, TWIST, UP                                               | INCORRECT (Max overlap: 2/4 with COMEDIAN’S PERFORMANCE)
   - Group 3: **0.4683** | VANILLA, DULL, BORING, MUNDANE                                    | CORRECT GROUP (UNEXCITING, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.1%, no-rel 22.6%)]
   - Group 4: **0.4572** | DRY, DIRTY, ROUTINE, SET                                          | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS)

### Top Candidate Groups:
   - Group 1: **0.6822** | TEA, COCOA, MATE, COFFEE                                          | CORRECT GROUP (DRINKS WITH CAFFEINE, Level 0)
   - Group 2: **0.6671** | DRY, DIRTY, UP, SET                                               | INCORRECT (Max overlap: 3/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 33.4%)]
   - Group 3: **0.5027** | BIT, ACT, TWIST, ROUTINE                                          | INCORRECT (Max overlap: 3/4 with COMEDIAN’S PERFORMANCE) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 37.8%)]
   - Group 4: **0.4683** | VANILLA, DULL, BORING, MUNDANE                                    | CORRECT GROUP (UNEXCITING, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.1%, no-rel 22.6%)]
   - Group 5: **0.6217** | DRY, DULL, DIRTY, SET                                             | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS)
   - Group 6: **0.4901** | BIT, ACT, TWIST, UP                                               | INCORRECT (Max overlap: 2/4 with COMEDIAN’S PERFORMANCE)
   - Group 7: **0.4723** | VANILLA, BORING, ROUTINE, MUNDANE                                 | INCORRECT (Max overlap: 3/4 with UNEXCITING) | [Pred Type: SYNONYM_OR_NEAR (47.8%, no-rel 25.8%)]
   - Group 8: **0.4847** | DRY, DULL, UP, SET                                                | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 34.7%)]
   - Group 9: **0.4798** | BIT, ACT, DIRTY, TWIST                                            | INCORRECT (Max overlap: 2/4 with COMEDIAN’S PERFORMANCE)
   - Group 10: **0.4165** | BIT, VANILLA, ACT, ROUTINE                                        | INCORRECT (Max overlap: 3/4 with COMEDIAN’S PERFORMANCE) | [Pred Type: SYNONYM_OR_NEAR (53.3%, no-rel 23.6%)]
   - Group 11: **0.4143** | DULL, BORING, TWIST, MUNDANE                                      | INCORRECT (Max overlap: 3/4 with UNEXCITING) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 35.3%)]
   - Group 12: **0.4572** | DRY, DIRTY, ROUTINE, SET                                          | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS)
   - Group 13: **0.6519** | VANILLA, TEA, COCOA, COFFEE                                       | INCORRECT (Max overlap: 3/4 with DRINKS WITH CAFFEINE)
   - Group 14: **0.4198** | BIT, ACT, MATE, ROUTINE                                           | INCORRECT (Max overlap: 3/4 with COMEDIAN’S PERFORMANCE) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 27.8%)]
   - Group 15: **0.3802** | DULL, BORING, MATE, MUNDANE                                       | INCORRECT (Max overlap: 3/4 with UNEXCITING) | [Pred Type: SYNONYM_OR_NEAR (66.6%, no-rel 20.0%)]
   - Group 16: **0.4859** | DIRTY, ROUTINE, MUNDANE, SET                                      | INCORRECT (Max overlap: 2/4 with COMEDIAN’S PERFORMANCE)
   - Group 17: **0.4409** | VANILLA, DRY, DULL, BORING                                        | INCORRECT (Max overlap: 3/4 with UNEXCITING) | [Pred Type: SYNONYM_OR_NEAR (55.9%, no-rel 24.6%)]
   - Group 18: **0.4876** | DULL, DIRTY, UP, SET                                              | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 35.1%)]
   - Group 19: **0.4347** | VANILLA, DRY, BORING, MUNDANE                                     | INCORRECT (Max overlap: 3/4 with UNEXCITING)
   - Group 20: **0.4695** | DIRTY, UP, MUNDANE, SET                                           | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 34.9%)]

---

## Puzzle 9 (ID: 186)
**Words on Board:** NAG, BOWL, LINING, FORK, ARENA, HOUND, FOX, BADGER, SCREEN, SPLIT, BUG, FIELD, DIVIDE, DOME, SPOON, PART

### Ground Truth Categories:
* **Level 0 (PESTER) [Type: SYNONYM_OR_NEAR]:** BADGER, BUG, HOUND, NAG
* **Level 1 (SPORTS VENUES) [Type: SEMANTIC_SET]:** ARENA, BOWL, DOME, FIELD
* **Level 2 (SEPARATE) [Type: SYNONYM_OR_NEAR]:** DIVIDE, FORK, PART, SPLIT
* **Level 3 (SILVER ___) [Type: FILL_IN_THE_BLANK]:** FOX, LINING, SCREEN, SPOON

### Top Candidate Partitions:
1. **Partition Score: 0.5188**
   - Group 1: **0.5987** | BOWL, ARENA, FIELD, DOME                                          | CORRECT GROUP (SPORTS VENUES, Level 1)
   - Group 2: **0.5609** | NAG, HOUND, BADGER, BUG                                           | CORRECT GROUP (PESTER, Level 0)
   - Group 3: **0.5456** | FORK, SPLIT, DIVIDE, PART                                         | CORRECT GROUP (SEPARATE, Level 2) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 24.3%)]
   - Group 4: **0.4760** | LINING, FOX, SCREEN, SPOON                                        | CORRECT GROUP (SILVER ___, Level 3)
2. **Partition Score: 0.4833**
   - Group 1: **0.5194** | NAG, HOUND, FOX, BUG                                              | INCORRECT (Max overlap: 3/4 with PESTER)
   - Group 2: **0.5104** | ARENA, SCREEN, FIELD, DOME                                        | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 3: **0.5039** | BOWL, FORK, BADGER, SPOON                                         | INCORRECT (Max overlap: 1/4 with SPORTS VENUES) | [Pred Type: SEMANTIC_SET (49.9%, no-rel 29.1%)]
   - Group 4: **0.4580** | LINING, SPLIT, DIVIDE, PART                                       | INCORRECT (Max overlap: 3/4 with SEPARATE) | [Pred Type: SYNONYM_OR_NEAR (65.9%, no-rel 22.5%)]
3. **Partition Score: 0.4777**
   - Group 1: **0.5987** | BOWL, ARENA, FIELD, DOME                                          | CORRECT GROUP (SPORTS VENUES, Level 1)
   - Group 2: **0.5194** | NAG, HOUND, FOX, BUG                                              | INCORRECT (Max overlap: 3/4 with PESTER)
   - Group 3: **0.4580** | LINING, SPLIT, DIVIDE, PART                                       | INCORRECT (Max overlap: 3/4 with SEPARATE) | [Pred Type: SYNONYM_OR_NEAR (65.9%, no-rel 22.5%)]
   - Group 4: **0.4430** | FORK, BADGER, SCREEN, SPOON                                       | INCORRECT (Max overlap: 2/4 with SILVER ___) | [Pred Type: SEMANTIC_SET (47.4%, no-rel 25.9%)]
4. **Partition Score: 0.4733**
   - Group 1: **0.5609** | NAG, HOUND, BADGER, BUG                                           | CORRECT GROUP (PESTER, Level 0)
   - Group 2: **0.5454** | SPLIT, FIELD, DIVIDE, PART                                        | INCORRECT (Max overlap: 3/4 with SEPARATE) | [Pred Type: SYNONYM_OR_NEAR (61.2%, no-rel 32.0%)]
   - Group 3: **0.4760** | LINING, FOX, SCREEN, SPOON                                        | CORRECT GROUP (SILVER ___, Level 3)
   - Group 4: **0.4267** | BOWL, FORK, ARENA, DOME                                           | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
5. **Partition Score: 0.4732**
   - Group 1: **0.5987** | BOWL, ARENA, FIELD, DOME                                          | CORRECT GROUP (SPORTS VENUES, Level 1)
   - Group 2: **0.5976** | HOUND, FOX, BADGER, BUG                                           | INCORRECT (Max overlap: 3/4 with PESTER)
   - Group 3: **0.4591** | NAG, SPLIT, DIVIDE, PART                                          | INCORRECT (Max overlap: 3/4 with SEPARATE) | [Pred Type: SYNONYM_OR_NEAR (68.5%, no-rel 23.4%)]
   - Group 4: **0.4054** | LINING, FORK, SCREEN, SPOON                                       | INCORRECT (Max overlap: 3/4 with SILVER ___) | [Pred Type: SEMANTIC_SET (47.5%, no-rel 27.5%)]

### Top Candidate Groups:
   - Group 1: **0.5987** | BOWL, ARENA, FIELD, DOME                                          | CORRECT GROUP (SPORTS VENUES, Level 1)
   - Group 2: **0.5609** | NAG, HOUND, BADGER, BUG                                           | CORRECT GROUP (PESTER, Level 0)
   - Group 3: **0.5456** | FORK, SPLIT, DIVIDE, PART                                         | CORRECT GROUP (SEPARATE, Level 2) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 24.3%)]
   - Group 4: **0.4760** | LINING, FOX, SCREEN, SPOON                                        | CORRECT GROUP (SILVER ___, Level 3)
   - Group 5: **0.5194** | NAG, HOUND, FOX, BUG                                              | INCORRECT (Max overlap: 3/4 with PESTER)
   - Group 6: **0.5104** | ARENA, SCREEN, FIELD, DOME                                        | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 7: **0.5039** | BOWL, FORK, BADGER, SPOON                                         | INCORRECT (Max overlap: 1/4 with SPORTS VENUES) | [Pred Type: SEMANTIC_SET (49.9%, no-rel 29.1%)]
   - Group 8: **0.4580** | LINING, SPLIT, DIVIDE, PART                                       | INCORRECT (Max overlap: 3/4 with SEPARATE) | [Pred Type: SYNONYM_OR_NEAR (65.9%, no-rel 22.5%)]
   - Group 9: **0.4430** | FORK, BADGER, SCREEN, SPOON                                       | INCORRECT (Max overlap: 2/4 with SILVER ___) | [Pred Type: SEMANTIC_SET (47.4%, no-rel 25.9%)]
   - Group 10: **0.5454** | SPLIT, FIELD, DIVIDE, PART                                        | INCORRECT (Max overlap: 3/4 with SEPARATE) | [Pred Type: SYNONYM_OR_NEAR (61.2%, no-rel 32.0%)]
   - Group 11: **0.4267** | BOWL, FORK, ARENA, DOME                                           | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 12: **0.5976** | HOUND, FOX, BADGER, BUG                                           | INCORRECT (Max overlap: 3/4 with PESTER)
   - Group 13: **0.4591** | NAG, SPLIT, DIVIDE, PART                                          | INCORRECT (Max overlap: 3/4 with SEPARATE) | [Pred Type: SYNONYM_OR_NEAR (68.5%, no-rel 23.4%)]
   - Group 14: **0.4054** | LINING, FORK, SCREEN, SPOON                                       | INCORRECT (Max overlap: 3/4 with SILVER ___) | [Pred Type: SEMANTIC_SET (47.5%, no-rel 27.5%)]
   - Group 15: **0.4997** | NAG, HOUND, FOX, BADGER                                           | INCORRECT (Max overlap: 3/4 with PESTER)
   - Group 16: **0.4530** | BOWL, FORK, BUG, SPOON                                            | INCORRECT (Max overlap: 1/4 with SPORTS VENUES) | [Pred Type: SEMANTIC_SET (51.0%, no-rel 31.6%)]
   - Group 17: **0.4289** | FORK, SCREEN, BUG, SPOON                                          | INCORRECT (Max overlap: 2/4 with SILVER ___) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 28.5%)]
   - Group 18: **0.4949** | SPLIT, DIVIDE, DOME, PART                                         | INCORRECT (Max overlap: 3/4 with SEPARATE) | [Pred Type: SYNONYM_OR_NEAR (61.8%, no-rel 27.8%)]
   - Group 19: **0.4321** | BOWL, FORK, ARENA, FIELD                                          | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 20: **0.4370** | BOWL, LINING, ARENA, DOME                                         | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)

---

## Puzzle 10 (ID: 604)
**Words on Board:** FAVORITE, SAND, KEEP, PRESERVE, BUFF, STICKY, LADY, CHICKEN, UNDER, PARLAY, SPREAD, FILE, BUTTER, GRIND, STORE, SAVE

### Ground Truth Categories:
* **Level 0 (CONSERVE) [Type: SYNONYM_OR_NEAR]:** KEEP, PRESERVE, SAVE, STORE
* **Level 1 (SMOOTH USING FRICTION) [Type: SYNONYM_OR_NEAR]:** BUFF, FILE, GRIND, SAND
* **Level 2 (SPORTS GAMBLING TERMS) [Type: SEMANTIC_SET]:** FAVORITE, PARLAY, SPREAD, UNDER
* **Level 3 (WORDS BEFORE “FINGERS”) [Type: FILL_IN_THE_BLANK]:** BUTTER, CHICKEN, LADY, STICKY

### Top Candidate Partitions:
1. **Partition Score: 0.5234**
   - Group 1: **0.8625** | KEEP, PRESERVE, STORE, SAVE                                       | CORRECT GROUP (CONSERVE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 22.2%)]
   - Group 2: **0.5242** | FAVORITE, CHICKEN, UNDER, PARLAY                                  | INCORRECT (Max overlap: 3/4 with SPORTS GAMBLING TERMS)
   - Group 3: **0.4891** | BUFF, STICKY, SPREAD, BUTTER                                      | INCORRECT (Max overlap: 2/4 with WORDS BEFORE “FINGERS”) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 23.9%)]
   - Group 4: **0.4613** | SAND, LADY, FILE, GRIND                                           | INCORRECT (Max overlap: 3/4 with SMOOTH USING FRICTION)
2. **Partition Score: 0.5194**
   - Group 1: **0.8625** | KEEP, PRESERVE, STORE, SAVE                                       | CORRECT GROUP (CONSERVE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 22.2%)]
   - Group 2: **0.5471** | FAVORITE, SAND, LADY, PARLAY                                      | INCORRECT (Max overlap: 2/4 with SPORTS GAMBLING TERMS)
   - Group 3: **0.4877** | BUFF, STICKY, FILE, GRIND                                         | INCORRECT (Max overlap: 3/4 with SMOOTH USING FRICTION)
   - Group 4: **0.4456** | CHICKEN, UNDER, SPREAD, BUTTER                                    | INCORRECT (Max overlap: 2/4 with WORDS BEFORE “FINGERS”)
3. **Partition Score: 0.5183**
   - Group 1: **0.8625** | KEEP, PRESERVE, STORE, SAVE                                       | CORRECT GROUP (CONSERVE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 22.2%)]
   - Group 2: **0.4891** | BUFF, STICKY, SPREAD, BUTTER                                      | INCORRECT (Max overlap: 2/4 with WORDS BEFORE “FINGERS”) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 23.9%)]
   - Group 3: **0.4850** | SAND, CHICKEN, FILE, GRIND                                        | INCORRECT (Max overlap: 3/4 with SMOOTH USING FRICTION)
   - Group 4: **0.4656** | FAVORITE, LADY, UNDER, PARLAY                                     | INCORRECT (Max overlap: 3/4 with SPORTS GAMBLING TERMS)
4. **Partition Score: 0.5159**
   - Group 1: **0.8625** | KEEP, PRESERVE, STORE, SAVE                                       | CORRECT GROUP (CONSERVE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 22.2%)]
   - Group 2: **0.4927** | SAND, BUFF, FILE, GRIND                                           | CORRECT GROUP (SMOOTH USING FRICTION, Level 1)
   - Group 3: **0.4687** | STICKY, CHICKEN, SPREAD, BUTTER                                   | INCORRECT (Max overlap: 3/4 with WORDS BEFORE “FINGERS”)
   - Group 4: **0.4656** | FAVORITE, LADY, UNDER, PARLAY                                     | INCORRECT (Max overlap: 3/4 with SPORTS GAMBLING TERMS)
5. **Partition Score: 0.5121**
   - Group 1: **0.8625** | KEEP, PRESERVE, STORE, SAVE                                       | CORRECT GROUP (CONSERVE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 22.2%)]
   - Group 2: **0.5242** | FAVORITE, CHICKEN, UNDER, PARLAY                                  | INCORRECT (Max overlap: 3/4 with SPORTS GAMBLING TERMS)
   - Group 3: **0.4756** | STICKY, SPREAD, FILE, GRIND                                       | INCORRECT (Max overlap: 2/4 with SMOOTH USING FRICTION)
   - Group 4: **0.4441** | SAND, BUFF, LADY, BUTTER                                          | INCORRECT (Max overlap: 2/4 with SMOOTH USING FRICTION)

### Top Candidate Groups:
   - Group 1: **0.8625** | KEEP, PRESERVE, STORE, SAVE                                       | CORRECT GROUP (CONSERVE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 22.2%)]
   - Group 2: **0.5242** | FAVORITE, CHICKEN, UNDER, PARLAY                                  | INCORRECT (Max overlap: 3/4 with SPORTS GAMBLING TERMS)
   - Group 3: **0.4891** | BUFF, STICKY, SPREAD, BUTTER                                      | INCORRECT (Max overlap: 2/4 with WORDS BEFORE “FINGERS”) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 23.9%)]
   - Group 4: **0.4613** | SAND, LADY, FILE, GRIND                                           | INCORRECT (Max overlap: 3/4 with SMOOTH USING FRICTION)
   - Group 5: **0.5471** | FAVORITE, SAND, LADY, PARLAY                                      | INCORRECT (Max overlap: 2/4 with SPORTS GAMBLING TERMS)
   - Group 6: **0.4877** | BUFF, STICKY, FILE, GRIND                                         | INCORRECT (Max overlap: 3/4 with SMOOTH USING FRICTION)
   - Group 7: **0.4456** | CHICKEN, UNDER, SPREAD, BUTTER                                    | INCORRECT (Max overlap: 2/4 with WORDS BEFORE “FINGERS”)
   - Group 8: **0.4850** | SAND, CHICKEN, FILE, GRIND                                        | INCORRECT (Max overlap: 3/4 with SMOOTH USING FRICTION)
   - Group 9: **0.4656** | FAVORITE, LADY, UNDER, PARLAY                                     | INCORRECT (Max overlap: 3/4 with SPORTS GAMBLING TERMS)
   - Group 10: **0.4927** | SAND, BUFF, FILE, GRIND                                           | CORRECT GROUP (SMOOTH USING FRICTION, Level 1)
   - Group 11: **0.4687** | STICKY, CHICKEN, SPREAD, BUTTER                                   | INCORRECT (Max overlap: 3/4 with WORDS BEFORE “FINGERS”)
   - Group 12: **0.4756** | STICKY, SPREAD, FILE, GRIND                                       | INCORRECT (Max overlap: 2/4 with SMOOTH USING FRICTION)
   - Group 13: **0.4441** | SAND, BUFF, LADY, BUTTER                                          | INCORRECT (Max overlap: 2/4 with SMOOTH USING FRICTION)
   - Group 14: **0.4662** | FAVORITE, BUFF, LADY, PARLAY                                      | INCORRECT (Max overlap: 2/4 with SPORTS GAMBLING TERMS)
   - Group 15: **0.4638** | SAND, CHICKEN, UNDER, BUTTER                                      | INCORRECT (Max overlap: 2/4 with WORDS BEFORE “FINGERS”) | [Pred Type: FILL_IN_THE_BLANK (49.2%, no-rel 21.5%)]
   - Group 16: **0.5635** | FAVORITE, LADY, CHICKEN, PARLAY                                   | INCORRECT (Max overlap: 2/4 with SPORTS GAMBLING TERMS)
   - Group 17: **0.4190** | STICKY, UNDER, SPREAD, BUTTER                                     | INCORRECT (Max overlap: 2/4 with WORDS BEFORE “FINGERS”) | [Pred Type: SYNONYM_OR_NEAR (47.6%, no-rel 18.4%)]
   - Group 18: **0.4758** | FAVORITE, SAND, UNDER, PARLAY                                     | INCORRECT (Max overlap: 3/4 with SPORTS GAMBLING TERMS)
   - Group 19: **0.4553** | BUFF, LADY, CHICKEN, BUTTER                                       | INCORRECT (Max overlap: 3/4 with WORDS BEFORE “FINGERS”)
   - Group 20: **0.4883** | FAVORITE, LADY, CHICKEN, UNDER                                    | INCORRECT (Max overlap: 2/4 with SPORTS GAMBLING TERMS)

---

## Puzzle 11 (ID: 313)
**Words on Board:** LIST, OK, COPY, PLUS, GLUE, CARAT, CLARITY, ROD, CUT, PASTE, STICK, ADHERE, WRITING, WORDS, COLOR, TEXT

### Ground Truth Categories:
* **Level 0 (ATTACH WITH ADHESIVE) [Type: SYNONYM_OR_NEAR]:** ADHERE, GLUE, PASTE, STICK
* **Level 1 (PUBLISHED LINES) [Type: SYNONYM_OR_NEAR]:** COPY, TEXT, WORDS, WRITING
* **Level 2 (DIAMOND QUALITIES) [Type: SEMANTIC_SET]:** CARAT, CLARITY, COLOR, CUT
* **Level 3 (A-___) [Type: FILL_IN_THE_BLANK]:** LIST, OK, PLUS, ROD

### Top Candidate Partitions:
1. **Partition Score: 0.4558**
   - Group 1: **0.6045** | COPY, WRITING, WORDS, TEXT                                        | CORRECT GROUP (PUBLISHED LINES, Level 1)
   - Group 2: **0.5120** | GLUE, ROD, STICK, ADHERE                                          | INCORRECT (Max overlap: 3/4 with ATTACH WITH ADHESIVE) | [Pred Type: SYNONYM_OR_NEAR (58.4%, no-rel 28.9%)]
   - Group 3: **0.4189** | OK, CARAT, CLARITY, COLOR                                         | INCORRECT (Max overlap: 3/4 with DIAMOND QUALITIES)
   - Group 4: **0.4161** | LIST, PLUS, CUT, PASTE                                            | INCORRECT (Max overlap: 2/4 with A-___)
2. **Partition Score: 0.4515**
   - Group 1: **0.5120** | GLUE, ROD, STICK, ADHERE                                          | INCORRECT (Max overlap: 3/4 with ATTACH WITH ADHESIVE) | [Pred Type: SYNONYM_OR_NEAR (58.4%, no-rel 28.9%)]
   - Group 2: **0.5100** | LIST, WRITING, WORDS, TEXT                                        | INCORRECT (Max overlap: 3/4 with PUBLISHED LINES)
   - Group 3: **0.4457** | COPY, PLUS, CUT, PASTE                                            | INCORRECT (Max overlap: 1/4 with PUBLISHED LINES)
   - Group 4: **0.4189** | OK, CARAT, CLARITY, COLOR                                         | INCORRECT (Max overlap: 3/4 with DIAMOND QUALITIES)
3. **Partition Score: 0.4418**
   - Group 1: **0.6045** | COPY, WRITING, WORDS, TEXT                                        | CORRECT GROUP (PUBLISHED LINES, Level 1)
   - Group 2: **0.4299** | LIST, ROD, STICK, ADHERE                                          | INCORRECT (Max overlap: 2/4 with A-___) | [Pred Type: SYNONYM_OR_NEAR (60.8%, no-rel 28.1%)]
   - Group 3: **0.4189** | OK, CARAT, CLARITY, COLOR                                         | INCORRECT (Max overlap: 3/4 with DIAMOND QUALITIES)
   - Group 4: **0.4187** | PLUS, GLUE, CUT, PASTE                                            | INCORRECT (Max overlap: 2/4 with ATTACH WITH ADHESIVE) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 29.0%)]
4. **Partition Score: 0.4395**
   - Group 1: **0.5521** | COPY, CUT, PASTE, ADHERE                                          | INCORRECT (Max overlap: 2/4 with ATTACH WITH ADHESIVE)
   - Group 2: **0.5100** | LIST, WRITING, WORDS, TEXT                                        | INCORRECT (Max overlap: 3/4 with PUBLISHED LINES)
   - Group 3: **0.4189** | OK, CARAT, CLARITY, COLOR                                         | INCORRECT (Max overlap: 3/4 with DIAMOND QUALITIES)
   - Group 4: **0.3965** | PLUS, GLUE, ROD, STICK                                            | INCORRECT (Max overlap: 2/4 with A-___)
5. **Partition Score: 0.4395**
   - Group 1: **0.5100** | LIST, WRITING, WORDS, TEXT                                        | INCORRECT (Max overlap: 3/4 with PUBLISHED LINES)
   - Group 2: **0.4482** | PLUS, GLUE, STICK, ADHERE                                         | INCORRECT (Max overlap: 3/4 with ATTACH WITH ADHESIVE) | [Pred Type: SYNONYM_OR_NEAR (65.7%, no-rel 23.7%)]
   - Group 3: **0.4445** | COPY, ROD, CUT, PASTE                                             | INCORRECT (Max overlap: 1/4 with PUBLISHED LINES)
   - Group 4: **0.4189** | OK, CARAT, CLARITY, COLOR                                         | INCORRECT (Max overlap: 3/4 with DIAMOND QUALITIES)

### Top Candidate Groups:
   - Group 1: **0.6045** | COPY, WRITING, WORDS, TEXT                                        | CORRECT GROUP (PUBLISHED LINES, Level 1)
   - Group 2: **0.5120** | GLUE, ROD, STICK, ADHERE                                          | INCORRECT (Max overlap: 3/4 with ATTACH WITH ADHESIVE) | [Pred Type: SYNONYM_OR_NEAR (58.4%, no-rel 28.9%)]
   - Group 3: **0.4189** | OK, CARAT, CLARITY, COLOR                                         | INCORRECT (Max overlap: 3/4 with DIAMOND QUALITIES)
   - Group 4: **0.4161** | LIST, PLUS, CUT, PASTE                                            | INCORRECT (Max overlap: 2/4 with A-___)
   - Group 5: **0.5100** | LIST, WRITING, WORDS, TEXT                                        | INCORRECT (Max overlap: 3/4 with PUBLISHED LINES)
   - Group 6: **0.4457** | COPY, PLUS, CUT, PASTE                                            | INCORRECT (Max overlap: 1/4 with PUBLISHED LINES)
   - Group 7: **0.4299** | LIST, ROD, STICK, ADHERE                                          | INCORRECT (Max overlap: 2/4 with A-___) | [Pred Type: SYNONYM_OR_NEAR (60.8%, no-rel 28.1%)]
   - Group 8: **0.4187** | PLUS, GLUE, CUT, PASTE                                            | INCORRECT (Max overlap: 2/4 with ATTACH WITH ADHESIVE) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 29.0%)]
   - Group 9: **0.5521** | COPY, CUT, PASTE, ADHERE                                          | INCORRECT (Max overlap: 2/4 with ATTACH WITH ADHESIVE)
   - Group 10: **0.3965** | PLUS, GLUE, ROD, STICK                                            | INCORRECT (Max overlap: 2/4 with A-___)
   - Group 11: **0.4482** | PLUS, GLUE, STICK, ADHERE                                         | INCORRECT (Max overlap: 3/4 with ATTACH WITH ADHESIVE) | [Pred Type: SYNONYM_OR_NEAR (65.7%, no-rel 23.7%)]
   - Group 12: **0.4445** | COPY, ROD, CUT, PASTE                                             | INCORRECT (Max overlap: 1/4 with PUBLISHED LINES)
   - Group 13: **0.5907** | LIST, COPY, CUT, PASTE                                            | INCORRECT (Max overlap: 1/4 with A-___)
   - Group 14: **0.4576** | OK, PLUS, CLARITY, COLOR                                          | INCORRECT (Max overlap: 2/4 with A-___)
   - Group 15: **0.3716** | CARAT, WRITING, WORDS, TEXT                                       | INCORRECT (Max overlap: 3/4 with PUBLISHED LINES)
   - Group 16: **0.3879** | COPY, CARAT, CUT, PASTE                                           | INCORRECT (Max overlap: 2/4 with DIAMOND QUALITIES) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 19.8%)]
   - Group 17: **0.4624** | LIST, ROD, CUT, STICK                                             | INCORRECT (Max overlap: 2/4 with A-___)
   - Group 18: **0.3982** | PLUS, GLUE, PASTE, ADHERE                                         | INCORRECT (Max overlap: 3/4 with ATTACH WITH ADHESIVE) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 30.2%)]
   - Group 19: **0.4633** | LIST, CUT, PASTE, ADHERE                                          | INCORRECT (Max overlap: 2/4 with ATTACH WITH ADHESIVE)
   - Group 20: **0.4010** | LIST, ROD, CUT, PASTE                                             | INCORRECT (Max overlap: 2/4 with A-___)

---

## Puzzle 12 (ID: 77)
**Words on Board:** TENDER, TICKER, HOLE, BREAST, SWIMMING, KICK, SNARE, TOM, STROKE, DRIVER, DRUMSTICK, INFANT, PUB, WING, EAGLE, CYMBAL

### Ground Truth Categories:
* **Level 0 (PIECES OF CHICKEN) [Type: SEMANTIC_SET]:** BREAST, DRUMSTICK, TENDER, WING
* **Level 1 (GOLF TERMS) [Type: SEMANTIC_SET]:** DRIVER, EAGLE, HOLE, STROKE
* **Level 2 (DRUM SET COMPONENTS) [Type: SEMANTIC_SET]:** CYMBAL, KICK, SNARE, TOM
* **Level 3 (ASSOCIATED WITH “CRAWL”) [Type: COMMON_PHRASE]:** INFANT, PUB, SWIMMING, TICKER

### Top Candidate Partitions:
1. **Partition Score: 0.4664**
   - Group 1: **0.4928** | BREAST, DRUMSTICK, WING, CYMBAL                                   | INCORRECT (Max overlap: 3/4 with PIECES OF CHICKEN) | [Pred Type: SEMANTIC_SET (49.8%, no-rel 25.0%)]
   - Group 2: **0.4794** | TENDER, DRIVER, INFANT, EAGLE                                     | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
   - Group 3: **0.4655** | TICKER, HOLE, TOM, PUB                                            | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
   - Group 4: **0.4563** | SWIMMING, KICK, SNARE, STROKE                                     | INCORRECT (Max overlap: 2/4 with DRUM SET COMPONENTS)
2. **Partition Score: 0.4646**
   - Group 1: **0.4824** | SWIMMING, KICK, STROKE, WING                                      | INCORRECT (Max overlap: 1/4 with ASSOCIATED WITH “CRAWL”)
   - Group 2: **0.4794** | TENDER, DRIVER, INFANT, EAGLE                                     | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
   - Group 3: **0.4655** | TICKER, HOLE, TOM, PUB                                            | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
   - Group 4: **0.4549** | BREAST, SNARE, DRUMSTICK, CYMBAL                                  | INCORRECT (Max overlap: 2/4 with PIECES OF CHICKEN) | [Pred Type: SEMANTIC_SET (50.0%, no-rel 22.9%)]
3. **Partition Score: 0.4637**
   - Group 1: **0.4928** | BREAST, DRUMSTICK, WING, CYMBAL                                   | INCORRECT (Max overlap: 3/4 with PIECES OF CHICKEN) | [Pred Type: SEMANTIC_SET (49.8%, no-rel 25.0%)]
   - Group 2: **0.4822** | TENDER, TICKER, DRIVER, INFANT                                    | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
   - Group 3: **0.4563** | SWIMMING, KICK, SNARE, STROKE                                     | INCORRECT (Max overlap: 2/4 with DRUM SET COMPONENTS)
   - Group 4: **0.4533** | HOLE, TOM, PUB, EAGLE                                             | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
4. **Partition Score: 0.4628**
   - Group 1: **0.5119** | TOM, DRIVER, INFANT, EAGLE                                        | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
   - Group 2: **0.4928** | BREAST, DRUMSTICK, WING, CYMBAL                                   | INCORRECT (Max overlap: 3/4 with PIECES OF CHICKEN) | [Pred Type: SEMANTIC_SET (49.8%, no-rel 25.0%)]
   - Group 3: **0.4563** | SWIMMING, KICK, SNARE, STROKE                                     | INCORRECT (Max overlap: 2/4 with DRUM SET COMPONENTS)
   - Group 4: **0.4435** | TENDER, TICKER, HOLE, PUB                                         | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
5. **Partition Score: 0.4623**
   - Group 1: **0.5091** | TENDER, BREAST, DRUMSTICK, WING                                   | CORRECT GROUP (PIECES OF CHICKEN, Level 0)
   - Group 2: **0.4655** | TICKER, HOLE, TOM, PUB                                            | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
   - Group 3: **0.4563** | SWIMMING, KICK, SNARE, STROKE                                     | INCORRECT (Max overlap: 2/4 with DRUM SET COMPONENTS)
   - Group 4: **0.4531** | DRIVER, INFANT, EAGLE, CYMBAL                                     | INCORRECT (Max overlap: 2/4 with GOLF TERMS)

### Top Candidate Groups:
   - Group 1: **0.4928** | BREAST, DRUMSTICK, WING, CYMBAL                                   | INCORRECT (Max overlap: 3/4 with PIECES OF CHICKEN) | [Pred Type: SEMANTIC_SET (49.8%, no-rel 25.0%)]
   - Group 2: **0.4794** | TENDER, DRIVER, INFANT, EAGLE                                     | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
   - Group 3: **0.4655** | TICKER, HOLE, TOM, PUB                                            | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
   - Group 4: **0.4563** | SWIMMING, KICK, SNARE, STROKE                                     | INCORRECT (Max overlap: 2/4 with DRUM SET COMPONENTS)
   - Group 5: **0.4824** | SWIMMING, KICK, STROKE, WING                                      | INCORRECT (Max overlap: 1/4 with ASSOCIATED WITH “CRAWL”)
   - Group 6: **0.4549** | BREAST, SNARE, DRUMSTICK, CYMBAL                                  | INCORRECT (Max overlap: 2/4 with PIECES OF CHICKEN) | [Pred Type: SEMANTIC_SET (50.0%, no-rel 22.9%)]
   - Group 7: **0.4822** | TENDER, TICKER, DRIVER, INFANT                                    | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
   - Group 8: **0.4533** | HOLE, TOM, PUB, EAGLE                                             | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
   - Group 9: **0.5119** | TOM, DRIVER, INFANT, EAGLE                                        | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
   - Group 10: **0.4435** | TENDER, TICKER, HOLE, PUB                                         | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
   - Group 11: **0.5091** | TENDER, BREAST, DRUMSTICK, WING                                   | CORRECT GROUP (PIECES OF CHICKEN, Level 0)
   - Group 12: **0.4531** | DRIVER, INFANT, EAGLE, CYMBAL                                     | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
   - Group 13: **0.4727** | TENDER, SWIMMING, KICK, STROKE                                    | INCORRECT (Max overlap: 1/4 with PIECES OF CHICKEN)
   - Group 14: **0.4707** | BREAST, SNARE, DRUMSTICK, WING                                    | INCORRECT (Max overlap: 3/4 with PIECES OF CHICKEN)
   - Group 15: **0.5604** | HOLE, SWIMMING, KICK, STROKE                                      | INCORRECT (Max overlap: 2/4 with GOLF TERMS)
   - Group 16: **0.4465** | TICKER, TOM, INFANT, PUB                                          | INCORRECT (Max overlap: 3/4 with ASSOCIATED WITH “CRAWL”)
   - Group 17: **0.4432** | TENDER, DRIVER, WING, EAGLE                                       | INCORRECT (Max overlap: 2/4 with PIECES OF CHICKEN)
   - Group 18: **0.3991** | TICKER, SNARE, PUB, CYMBAL                                        | INCORRECT (Max overlap: 2/4 with ASSOCIATED WITH “CRAWL”)
   - Group 19: **0.4565** | TENDER, TICKER, BREAST, WING                                      | INCORRECT (Max overlap: 3/4 with PIECES OF CHICKEN)
   - Group 20: **0.4154** | SNARE, DRUMSTICK, PUB, CYMBAL                                     | INCORRECT (Max overlap: 2/4 with DRUM SET COMPONENTS) | [Pred Type: SEMANTIC_SET (46.4%, no-rel 20.0%)]

---

## Puzzle 13 (ID: 655)
**Words on Board:** PAPER, SWAY, PHONE, CHANGE, DING, WAVE, GREEN, CORRECT, SCRATCH, RIGHT, SCOPE, CHIP, MOVE, BINGO, TOUCH, REACH

### Ground Truth Categories:
* **Level 0 (AFFECT) [Type: SYNONYM_OR_NEAR]:** MOVE, REACH, SWAY, TOUCH
* **Level 1 (YOU GOT IT!) [Type: SYNONYM_OR_NEAR]:** BINGO, CORRECT, DING, RIGHT
* **Level 2 (SLANG FOR MONEY) [Type: SEMANTIC_SET]:** CHANGE, GREEN, PAPER, SCRATCH
* **Level 3 (OBJECTS WITH THE PREFIX “MICRO-”) [Type: FILL_IN_THE_BLANK]:** CHIP, PHONE, SCOPE, WAVE

### Top Candidate Partitions:
1. **Partition Score: 0.4885**
   - Group 1: **0.6019** | CHANGE, CORRECT, RIGHT, MOVE                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 39.0%)]
   - Group 2: **0.5980** | DING, SCRATCH, CHIP, BINGO                                        | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.5092** | PHONE, SCOPE, TOUCH, REACH                                        | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 34.3%)]
   - Group 4: **0.4160** | PAPER, SWAY, WAVE, GREEN                                          | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
2. **Partition Score: 0.4817**
   - Group 1: **0.6019** | CHANGE, CORRECT, RIGHT, MOVE                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 39.0%)]
   - Group 2: **0.5472** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.5092** | PHONE, SCOPE, TOUCH, REACH                                        | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 34.3%)]
   - Group 4: **0.4212** | PAPER, SWAY, WAVE, CHIP                                           | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”)
3. **Partition Score: 0.4783**
   - Group 1: **0.6688** | CHANGE, CORRECT, RIGHT, TOUCH                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 39.9%)]
   - Group 2: **0.5391** | DING, GREEN, CHIP, BINGO                                          | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.4359** | SWAY, SCOPE, MOVE, REACH                                          | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 38.3%)]
   - Group 4: **0.4297** | PAPER, PHONE, WAVE, SCRATCH                                       | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
4. **Partition Score: 0.4759**
   - Group 1: **0.6019** | CHANGE, CORRECT, RIGHT, MOVE                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 39.0%)]
   - Group 2: **0.4799** | PAPER, DING, GREEN, BINGO                                         | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 3: **0.4548** | PHONE, WAVE, SCRATCH, CHIP                                        | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)
   - Group 4: **0.4545** | SWAY, SCOPE, TOUCH, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 38.3%)]
5. **Partition Score: 0.4756**
   - Group 1: **0.6688** | CHANGE, CORRECT, RIGHT, TOUCH                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 39.9%)]
   - Group 2: **0.5472** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.4359** | SWAY, SCOPE, MOVE, REACH                                          | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 38.3%)]
   - Group 4: **0.4215** | PAPER, PHONE, WAVE, CHIP                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)

### Top Candidate Groups:
   - Group 1: **0.6019** | CHANGE, CORRECT, RIGHT, MOVE                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 39.0%)]
   - Group 2: **0.5980** | DING, SCRATCH, CHIP, BINGO                                        | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.5092** | PHONE, SCOPE, TOUCH, REACH                                        | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 34.3%)]
   - Group 4: **0.4160** | PAPER, SWAY, WAVE, GREEN                                          | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 5: **0.5472** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 6: **0.4212** | PAPER, SWAY, WAVE, CHIP                                           | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”)
   - Group 7: **0.6688** | CHANGE, CORRECT, RIGHT, TOUCH                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 39.9%)]
   - Group 8: **0.5391** | DING, GREEN, CHIP, BINGO                                          | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 9: **0.4359** | SWAY, SCOPE, MOVE, REACH                                          | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 38.3%)]
   - Group 10: **0.4297** | PAPER, PHONE, WAVE, SCRATCH                                       | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 11: **0.4799** | PAPER, DING, GREEN, BINGO                                         | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 12: **0.4548** | PHONE, WAVE, SCRATCH, CHIP                                        | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)
   - Group 13: **0.4545** | SWAY, SCOPE, TOUCH, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 38.3%)]
   - Group 14: **0.4215** | PAPER, PHONE, WAVE, CHIP                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)
   - Group 15: **0.4431** | SWAY, WAVE, SCOPE, REACH                                          | INCORRECT (Max overlap: 2/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (55.3%, no-rel 32.5%)]
   - Group 16: **0.4351** | PAPER, PHONE, SCRATCH, TOUCH                                      | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 17: **0.4074** | PAPER, SWAY, WAVE, SCRATCH                                        | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 18: **0.4042** | PHONE, SCOPE, MOVE, REACH                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH THE PREFIX “MICRO-”) | [Pred Type: SYNONYM_OR_NEAR (56.8%, no-rel 28.8%)]
   - Group 19: **0.5416** | SWAY, CHANGE, MOVE, TOUCH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 20: **0.4700** | CORRECT, RIGHT, SCOPE, REACH                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 36.7%)]

---

## Puzzle 14 (ID: 772)
**Words on Board:** CHEEK, CUSHION, STRIPES, CHECKERS, SOFTEN, CHESS, TEMPER, LIP, WHOOPIE, ATTITUDE, HONEYCOMB, DAMPEN, CAMO, CUTIE, HUMBLE, MOUTH

### Ground Truth Categories:
* **Level 0 (SASSINESS) [Type: SYNONYM_OR_NEAR]:** ATTITUDE, CHEEK, LIP, MOUTH
* **Level 1 (MITIGATE) [Type: SYNONYM_OR_NEAR]:** CUSHION, DAMPEN, SOFTEN, TEMPER
* **Level 2 (PATTERNS) [Type: SEMANTIC_SET]:** CAMO, CHECKERS, HONEYCOMB, STRIPES
* **Level 3 (___ PIE) [Type: FILL_IN_THE_BLANK]:** CHESS, CUTIE, HUMBLE, WHOOPIE

### Top Candidate Partitions:
1. **Partition Score: 0.4294**
   - Group 1: **0.6904** | CUSHION, SOFTEN, TEMPER, DAMPEN                                   | CORRECT GROUP (MITIGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (52.3%, no-rel 40.1%)]
   - Group 2: **0.4535** | CHECKERS, CHESS, HONEYCOMB, CAMO                                  | INCORRECT (Max overlap: 3/4 with PATTERNS)
   - Group 3: **0.3977** | CHEEK, STRIPES, ATTITUDE, HUMBLE                                  | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 4: **0.3749** | LIP, WHOOPIE, CUTIE, MOUTH                                        | INCORRECT (Max overlap: 2/4 with SASSINESS)
2. **Partition Score: 0.4241**
   - Group 1: **0.6904** | CUSHION, SOFTEN, TEMPER, DAMPEN                                   | CORRECT GROUP (MITIGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (52.3%, no-rel 40.1%)]
   - Group 2: **0.4462** | LIP, HONEYCOMB, CAMO, MOUTH                                       | INCORRECT (Max overlap: 2/4 with SASSINESS) | [Pred Type: SEMANTIC_SET (47.0%, no-rel 34.3%)]
   - Group 3: **0.3977** | CHEEK, STRIPES, ATTITUDE, HUMBLE                                  | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 4: **0.3672** | CHECKERS, CHESS, WHOOPIE, CUTIE                                   | INCORRECT (Max overlap: 3/4 with ___ PIE)
3. **Partition Score: 0.4222**
   - Group 1: **0.6904** | CUSHION, SOFTEN, TEMPER, DAMPEN                                   | CORRECT GROUP (MITIGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (52.3%, no-rel 40.1%)]
   - Group 2: **0.4877** | WHOOPIE, HONEYCOMB, CAMO, CUTIE                                   | INCORRECT (Max overlap: 2/4 with ___ PIE)
   - Group 3: **0.3977** | CHEEK, STRIPES, ATTITUDE, HUMBLE                                  | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 4: **0.3484** | CHECKERS, CHESS, LIP, MOUTH                                       | INCORRECT (Max overlap: 2/4 with SASSINESS)
4. **Partition Score: 0.4217**
   - Group 1: **0.6904** | CUSHION, SOFTEN, TEMPER, DAMPEN                                   | CORRECT GROUP (MITIGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (52.3%, no-rel 40.1%)]
   - Group 2: **0.3977** | CHEEK, STRIPES, ATTITUDE, HUMBLE                                  | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 3: **0.3904** | CHECKERS, CHESS, WHOOPIE, HONEYCOMB                               | INCORRECT (Max overlap: 2/4 with PATTERNS)
   - Group 4: **0.3830** | LIP, CAMO, CUTIE, MOUTH                                           | INCORRECT (Max overlap: 2/4 with SASSINESS)
5. **Partition Score: 0.4203**
   - Group 1: **0.6904** | CUSHION, SOFTEN, TEMPER, DAMPEN                                   | CORRECT GROUP (MITIGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (52.3%, no-rel 40.1%)]
   - Group 2: **0.3977** | CHEEK, STRIPES, ATTITUDE, HUMBLE                                  | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 3: **0.3944** | LIP, WHOOPIE, HONEYCOMB, MOUTH                                    | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 4: **0.3788** | CHECKERS, CHESS, CAMO, CUTIE                                      | INCORRECT (Max overlap: 2/4 with PATTERNS)

### Top Candidate Groups:
   - Group 1: **0.6904** | CUSHION, SOFTEN, TEMPER, DAMPEN                                   | CORRECT GROUP (MITIGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (52.3%, no-rel 40.1%)]
   - Group 2: **0.4535** | CHECKERS, CHESS, HONEYCOMB, CAMO                                  | INCORRECT (Max overlap: 3/4 with PATTERNS)
   - Group 3: **0.3977** | CHEEK, STRIPES, ATTITUDE, HUMBLE                                  | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 4: **0.3749** | LIP, WHOOPIE, CUTIE, MOUTH                                        | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 5: **0.4462** | LIP, HONEYCOMB, CAMO, MOUTH                                       | INCORRECT (Max overlap: 2/4 with SASSINESS) | [Pred Type: SEMANTIC_SET (47.0%, no-rel 34.3%)]
   - Group 6: **0.3672** | CHECKERS, CHESS, WHOOPIE, CUTIE                                   | INCORRECT (Max overlap: 3/4 with ___ PIE)
   - Group 7: **0.4877** | WHOOPIE, HONEYCOMB, CAMO, CUTIE                                   | INCORRECT (Max overlap: 2/4 with ___ PIE)
   - Group 8: **0.3484** | CHECKERS, CHESS, LIP, MOUTH                                       | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 9: **0.3904** | CHECKERS, CHESS, WHOOPIE, HONEYCOMB                               | INCORRECT (Max overlap: 2/4 with PATTERNS)
   - Group 10: **0.3830** | LIP, CAMO, CUTIE, MOUTH                                           | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 11: **0.3944** | LIP, WHOOPIE, HONEYCOMB, MOUTH                                    | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 12: **0.3788** | CHECKERS, CHESS, CAMO, CUTIE                                      | INCORRECT (Max overlap: 2/4 with PATTERNS)
   - Group 13: **0.3850** | LIP, WHOOPIE, CAMO, MOUTH                                         | INCORRECT (Max overlap: 2/4 with SASSINESS) | [Pred Type: SEMANTIC_SET (46.7%, no-rel 29.7%)]
   - Group 14: **0.3811** | CHECKERS, CHESS, HONEYCOMB, CUTIE                                 | INCORRECT (Max overlap: 2/4 with PATTERNS)
   - Group 15: **0.5860** | CUSHION, SOFTEN, DAMPEN, HUMBLE                                   | INCORRECT (Max overlap: 3/4 with MITIGATE) | [Pred Type: SYNONYM_OR_NEAR (62.3%, no-rel 30.2%)]
   - Group 16: **0.4080** | CHEEK, STRIPES, TEMPER, ATTITUDE                                  | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 17: **0.5122** | CHEEK, TEMPER, ATTITUDE, HUMBLE                                   | INCORRECT (Max overlap: 2/4 with SASSINESS) | [Pred Type: SYNONYM_OR_NEAR (46.2%, no-rel 33.6%)]
   - Group 18: **0.4453** | CUSHION, STRIPES, SOFTEN, DAMPEN                                  | INCORRECT (Max overlap: 3/4 with MITIGATE) | [Pred Type: SYNONYM_OR_NEAR (67.1%, no-rel 21.1%)]
   - Group 19: **0.3837** | LIP, HONEYCOMB, CUTIE, MOUTH                                      | INCORRECT (Max overlap: 2/4 with SASSINESS)
   - Group 20: **0.3778** | CHECKERS, CHESS, WHOOPIE, CAMO                                    | INCORRECT (Max overlap: 2/4 with PATTERNS)

---

## Puzzle 15 (ID: 347)
**Words on Board:** CULTURE, THROUGH, HEYDAY, EXPLOIT, CITY, LEVERAGE, MILK, OVER, SUPPER, USE, HIJINKS, DONE, YOGURT, UP, COPY, SPORTS

### Ground Truth Categories:
* **Level 0 (TAKE ADVANTAGE OF) [Type: SYNONYM_OR_NEAR]:** EXPLOIT, LEVERAGE, MILK, USE
* **Level 1 (FINISHED, AS TIME) [Type: SYNONYM_OR_NEAR]:** DONE, OVER, THROUGH, UP
* **Level 2 (NEWSPAPER DESKS) [Type: SEMANTIC_SET]:** CITY, COPY, CULTURE, SPORTS
* **Level 3 (WORDS BEGINNING WITH GREETINGS) [Type: WORD_FORM]:** HEYDAY, HIJINKS, SUPPER, YOGURT

### Top Candidate Partitions:
1. **Partition Score: 0.5459**
   - Group 1: **0.6006** | THROUGH, DONE, UP, COPY                                           | INCORRECT (Max overlap: 3/4 with FINISHED, AS TIME) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 38.4%)]
   - Group 2: **0.5873** | CITY, OVER, SUPPER, SPORTS                                        | INCORRECT (Max overlap: 2/4 with NEWSPAPER DESKS)
   - Group 3: **0.5493** | EXPLOIT, LEVERAGE, MILK, USE                                      | CORRECT GROUP (TAKE ADVANTAGE OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 31.1%)]
   - Group 4: **0.5174** | CULTURE, HEYDAY, HIJINKS, YOGURT                                  | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH GREETINGS)
2. **Partition Score: 0.5405**
   - Group 1: **0.6006** | THROUGH, DONE, UP, COPY                                           | INCORRECT (Max overlap: 3/4 with FINISHED, AS TIME) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 38.4%)]
   - Group 2: **0.5470** | HEYDAY, SUPPER, HIJINKS, YOGURT                                   | CORRECT GROUP (WORDS BEGINNING WITH GREETINGS, Level 3)
   - Group 3: **0.5360** | CITY, MILK, OVER, SPORTS                                          | INCORRECT (Max overlap: 2/4 with NEWSPAPER DESKS) | [Pred Type: FILL_IN_THE_BLANK (49.0%, no-rel 19.6%)]
   - Group 4: **0.5266** | CULTURE, EXPLOIT, LEVERAGE, USE                                   | INCORRECT (Max overlap: 3/4 with TAKE ADVANTAGE OF) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 26.8%)]
3. **Partition Score: 0.5393**
   - Group 1: **0.6894** | THROUGH, OVER, DONE, UP                                           | CORRECT GROUP (FINISHED, AS TIME, Level 1) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 33.1%)]
   - Group 2: **0.6138** | HEYDAY, CITY, SUPPER, HIJINKS                                     | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 3: **0.5057** | CULTURE, MILK, YOGURT, SPORTS                                     | INCORRECT (Max overlap: 2/4 with NEWSPAPER DESKS)
   - Group 4: **0.4915** | EXPLOIT, LEVERAGE, USE, COPY                                      | INCORRECT (Max overlap: 3/4 with TAKE ADVANTAGE OF)
4. **Partition Score: 0.5354**
   - Group 1: **0.6894** | THROUGH, OVER, DONE, UP                                           | CORRECT GROUP (FINISHED, AS TIME, Level 1) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 33.1%)]
   - Group 2: **0.5922** | HEYDAY, CITY, HIJINKS, SPORTS                                     | INCORRECT (Max overlap: 2/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 3: **0.5063** | CULTURE, MILK, SUPPER, YOGURT                                     | INCORRECT (Max overlap: 2/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 4: **0.4915** | EXPLOIT, LEVERAGE, USE, COPY                                      | INCORRECT (Max overlap: 3/4 with TAKE ADVANTAGE OF)
5. **Partition Score: 0.5327**
   - Group 1: **0.6006** | THROUGH, DONE, UP, COPY                                           | INCORRECT (Max overlap: 3/4 with FINISHED, AS TIME) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 38.4%)]
   - Group 2: **0.5266** | CULTURE, EXPLOIT, LEVERAGE, USE                                   | INCORRECT (Max overlap: 3/4 with TAKE ADVANTAGE OF) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 26.8%)]
   - Group 3: **0.5262** | CITY, MILK, OVER, SUPPER                                          | INCORRECT (Max overlap: 1/4 with NEWSPAPER DESKS) | [Pred Type: FILL_IN_THE_BLANK (53.0%, no-rel 17.2%)]
   - Group 4: **0.5224** | HEYDAY, HIJINKS, YOGURT, SPORTS                                   | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH GREETINGS)

### Top Candidate Groups:
   - Group 1: **0.6006** | THROUGH, DONE, UP, COPY                                           | INCORRECT (Max overlap: 3/4 with FINISHED, AS TIME) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 38.4%)]
   - Group 2: **0.5873** | CITY, OVER, SUPPER, SPORTS                                        | INCORRECT (Max overlap: 2/4 with NEWSPAPER DESKS)
   - Group 3: **0.5493** | EXPLOIT, LEVERAGE, MILK, USE                                      | CORRECT GROUP (TAKE ADVANTAGE OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 31.1%)]
   - Group 4: **0.5174** | CULTURE, HEYDAY, HIJINKS, YOGURT                                  | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 5: **0.5470** | HEYDAY, SUPPER, HIJINKS, YOGURT                                   | CORRECT GROUP (WORDS BEGINNING WITH GREETINGS, Level 3)
   - Group 6: **0.5360** | CITY, MILK, OVER, SPORTS                                          | INCORRECT (Max overlap: 2/4 with NEWSPAPER DESKS) | [Pred Type: FILL_IN_THE_BLANK (49.0%, no-rel 19.6%)]
   - Group 7: **0.5266** | CULTURE, EXPLOIT, LEVERAGE, USE                                   | INCORRECT (Max overlap: 3/4 with TAKE ADVANTAGE OF) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 26.8%)]
   - Group 8: **0.6894** | THROUGH, OVER, DONE, UP                                           | CORRECT GROUP (FINISHED, AS TIME, Level 1) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 33.1%)]
   - Group 9: **0.6138** | HEYDAY, CITY, SUPPER, HIJINKS                                     | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 10: **0.5057** | CULTURE, MILK, YOGURT, SPORTS                                     | INCORRECT (Max overlap: 2/4 with NEWSPAPER DESKS)
   - Group 11: **0.4915** | EXPLOIT, LEVERAGE, USE, COPY                                      | INCORRECT (Max overlap: 3/4 with TAKE ADVANTAGE OF)
   - Group 12: **0.5922** | HEYDAY, CITY, HIJINKS, SPORTS                                     | INCORRECT (Max overlap: 2/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 13: **0.5063** | CULTURE, MILK, SUPPER, YOGURT                                     | INCORRECT (Max overlap: 2/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 14: **0.5262** | CITY, MILK, OVER, SUPPER                                          | INCORRECT (Max overlap: 1/4 with NEWSPAPER DESKS) | [Pred Type: FILL_IN_THE_BLANK (53.0%, no-rel 17.2%)]
   - Group 15: **0.5224** | HEYDAY, HIJINKS, YOGURT, SPORTS                                   | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 16: **0.4879** | MILK, OVER, YOGURT, SPORTS                                        | INCORRECT (Max overlap: 1/4 with TAKE ADVANTAGE OF)
   - Group 17: **0.5332** | MILK, SUPPER, YOGURT, SPORTS                                      | INCORRECT (Max overlap: 2/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 18: **0.5250** | CULTURE, HEYDAY, CITY, HIJINKS                                    | INCORRECT (Max overlap: 2/4 with NEWSPAPER DESKS)
   - Group 19: **0.4871** | MILK, OVER, SUPPER, YOGURT                                        | INCORRECT (Max overlap: 2/4 with WORDS BEGINNING WITH GREETINGS)
   - Group 20: **0.6187** | EXPLOIT, LEVERAGE, USE, UP                                        | INCORRECT (Max overlap: 3/4 with TAKE ADVANTAGE OF) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 35.0%)]

---

## Puzzle 16 (ID: 887)
**Words on Board:** FLAVOR, COMFORT, TIME, SEASON, COLON, METHOD, STAGE, SALT, CHARACTER, FILM, DASH, BUFFER, SPICE, SLASH, PERIOD, TWILIGHT

### Ground Truth Categories:
* **Level 0 (ENHANCE THE TASTE OF) [Type: SEMANTIC_SET]:** FLAVOR, SALT, SEASON, SPICE
* **Level 1 (PUNCTUATION MARKS) [Type: SEMANTIC_SET]:** COLON, DASH, PERIOD, SLASH
* **Level 2 (KINDS OF ACTORS) [Type: FILL_IN_THE_BLANK]:** CHARACTER, FILM, METHOD, STAGE
* **Level 3 (___ ZONE) [Type: FILL_IN_THE_BLANK]:** BUFFER, COMFORT, TIME, TWILIGHT

### Top Candidate Partitions:
1. **Partition Score: 0.5351**
   - Group 1: **0.6944** | FLAVOR, SEASON, SALT, SPICE                                       | CORRECT GROUP (ENHANCE THE TASTE OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 37.9%)]
   - Group 2: **0.5804** | COLON, DASH, SLASH, PERIOD                                        | CORRECT GROUP (PUNCTUATION MARKS, Level 1)
   - Group 3: **0.5010** | TIME, STAGE, CHARACTER, FILM                                      | INCORRECT (Max overlap: 3/4 with KINDS OF ACTORS)
   - Group 4: **0.4961** | COMFORT, METHOD, BUFFER, TWILIGHT                                 | INCORRECT (Max overlap: 3/4 with ___ ZONE)
2. **Partition Score: 0.5324**
   - Group 1: **0.6944** | FLAVOR, SEASON, SALT, SPICE                                       | CORRECT GROUP (ENHANCE THE TASTE OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 37.9%)]
   - Group 2: **0.5804** | COLON, DASH, SLASH, PERIOD                                        | CORRECT GROUP (PUNCTUATION MARKS, Level 1)
   - Group 3: **0.5157** | COMFORT, CHARACTER, BUFFER, TWILIGHT                              | INCORRECT (Max overlap: 3/4 with ___ ZONE)
   - Group 4: **0.4855** | TIME, METHOD, STAGE, FILM                                         | INCORRECT (Max overlap: 3/4 with KINDS OF ACTORS)
3. **Partition Score: 0.5317**
   - Group 1: **0.6944** | FLAVOR, SEASON, SALT, SPICE                                       | CORRECT GROUP (ENHANCE THE TASTE OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 37.9%)]
   - Group 2: **0.5804** | COLON, DASH, SLASH, PERIOD                                        | CORRECT GROUP (PUNCTUATION MARKS, Level 1)
   - Group 3: **0.4936** | TIME, METHOD, STAGE, CHARACTER                                    | INCORRECT (Max overlap: 3/4 with KINDS OF ACTORS)
   - Group 4: **0.4922** | COMFORT, FILM, BUFFER, TWILIGHT                                   | INCORRECT (Max overlap: 3/4 with ___ ZONE)
4. **Partition Score: 0.5268**
   - Group 1: **0.6944** | FLAVOR, SEASON, SALT, SPICE                                       | CORRECT GROUP (ENHANCE THE TASTE OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 37.9%)]
   - Group 2: **0.5616** | TIME, METHOD, STAGE, PERIOD                                       | INCORRECT (Max overlap: 2/4 with KINDS OF ACTORS)
   - Group 3: **0.4922** | COMFORT, FILM, BUFFER, TWILIGHT                                   | INCORRECT (Max overlap: 3/4 with ___ ZONE)
   - Group 4: **0.4899** | COLON, CHARACTER, DASH, SLASH                                     | INCORRECT (Max overlap: 3/4 with PUNCTUATION MARKS)
5. **Partition Score: 0.5162**
   - Group 1: **0.6944** | FLAVOR, SEASON, SALT, SPICE                                       | CORRECT GROUP (ENHANCE THE TASTE OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 37.9%)]
   - Group 2: **0.5616** | TIME, METHOD, STAGE, PERIOD                                       | INCORRECT (Max overlap: 2/4 with KINDS OF ACTORS)
   - Group 3: **0.5157** | COMFORT, CHARACTER, BUFFER, TWILIGHT                              | INCORRECT (Max overlap: 3/4 with ___ ZONE)
   - Group 4: **0.4606** | COLON, FILM, DASH, SLASH                                          | INCORRECT (Max overlap: 3/4 with PUNCTUATION MARKS)

### Top Candidate Groups:
   - Group 1: **0.6944** | FLAVOR, SEASON, SALT, SPICE                                       | CORRECT GROUP (ENHANCE THE TASTE OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 37.9%)]
   - Group 2: **0.5804** | COLON, DASH, SLASH, PERIOD                                        | CORRECT GROUP (PUNCTUATION MARKS, Level 1)
   - Group 3: **0.5010** | TIME, STAGE, CHARACTER, FILM                                      | INCORRECT (Max overlap: 3/4 with KINDS OF ACTORS)
   - Group 4: **0.4961** | COMFORT, METHOD, BUFFER, TWILIGHT                                 | INCORRECT (Max overlap: 3/4 with ___ ZONE)
   - Group 5: **0.5157** | COMFORT, CHARACTER, BUFFER, TWILIGHT                              | INCORRECT (Max overlap: 3/4 with ___ ZONE)
   - Group 6: **0.4855** | TIME, METHOD, STAGE, FILM                                         | INCORRECT (Max overlap: 3/4 with KINDS OF ACTORS)
   - Group 7: **0.4936** | TIME, METHOD, STAGE, CHARACTER                                    | INCORRECT (Max overlap: 3/4 with KINDS OF ACTORS)
   - Group 8: **0.4922** | COMFORT, FILM, BUFFER, TWILIGHT                                   | INCORRECT (Max overlap: 3/4 with ___ ZONE)
   - Group 9: **0.5616** | TIME, METHOD, STAGE, PERIOD                                       | INCORRECT (Max overlap: 2/4 with KINDS OF ACTORS)
   - Group 10: **0.4899** | COLON, CHARACTER, DASH, SLASH                                     | INCORRECT (Max overlap: 3/4 with PUNCTUATION MARKS)
   - Group 11: **0.4606** | COLON, FILM, DASH, SLASH                                          | INCORRECT (Max overlap: 3/4 with PUNCTUATION MARKS)
   - Group 12: **0.5042** | TIME, STAGE, CHARACTER, PERIOD                                    | INCORRECT (Max overlap: 2/4 with KINDS OF ACTORS)
   - Group 13: **0.4832** | COLON, METHOD, DASH, SLASH                                        | INCORRECT (Max overlap: 3/4 with PUNCTUATION MARKS)
   - Group 14: **0.4774** | COMFORT, CHARACTER, FILM, BUFFER                                  | INCORRECT (Max overlap: 2/4 with ___ ZONE)
   - Group 15: **0.4272** | COLON, DASH, SLASH, TWILIGHT                                      | INCORRECT (Max overlap: 3/4 with PUNCTUATION MARKS)
   - Group 16: **0.4708** | COLON, METHOD, SLASH, PERIOD                                      | INCORRECT (Max overlap: 3/4 with PUNCTUATION MARKS)
   - Group 17: **0.4496** | COMFORT, DASH, BUFFER, TWILIGHT                                   | INCORRECT (Max overlap: 3/4 with ___ ZONE)
   - Group 18: **0.4393** | TIME, STAGE, FILM, PERIOD                                         | INCORRECT (Max overlap: 2/4 with KINDS OF ACTORS) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 33.8%)]
   - Group 19: **0.4328** | METHOD, STAGE, CHARACTER, FILM                                    | CORRECT GROUP (KINDS OF ACTORS, Level 2)
   - Group 20: **0.4306** | COMFORT, TIME, BUFFER, TWILIGHT                                   | CORRECT GROUP (___ ZONE, Level 3) | [Pred Type: FILL_IN_THE_BLANK (47.0%, no-rel 16.1%)]

---

## Puzzle 17 (ID: 696)
**Words on Board:** HEAL, EXCEPT, BESIDES, QUARTS, KNIT, CUPS, MEND, PURL, WANDS, PENTACLES, SWORDS, SAVE, CHORAL, RECOVER, OPEL, BUT

### Ground Truth Categories:
* **Level 0 (GET BETTER, AS A BROKEN BONE) [Type: SYNONYM_OR_NEAR]:** HEAL, KNIT, MEND, RECOVER
* **Level 1 (NOT INCLUDING) [Type: SYNONYM_OR_NEAR]:** BESIDES, BUT, EXCEPT, SAVE
* **Level 2 (TAROT MINOR ARCANA SUITS) [Type: NAMED_ENTITY_SET]:** CUPS, PENTACLES, SWORDS, WANDS
* **Level 3 (HOMOPHONES OF GEMSTONES) [Type: SOUND_OR_SPELLING]:** CHORAL, OPEL, PURL, QUARTS

### Top Candidate Partitions:
1. **Partition Score: 0.4665**
   - Group 1: **0.6851** | EXCEPT, BESIDES, SAVE, BUT                                        | CORRECT GROUP (NOT INCLUDING, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 37.3%)]
   - Group 2: **0.5018** | QUARTS, CUPS, CHORAL, OPEL                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF GEMSTONES)
   - Group 3: **0.4734** | HEAL, MEND, PURL, RECOVER                                         | INCORRECT (Max overlap: 3/4 with GET BETTER, AS A BROKEN BONE) | [Pred Type: SYNONYM_OR_NEAR (60.0%, no-rel 30.8%)]
   - Group 4: **0.4030** | KNIT, WANDS, PENTACLES, SWORDS                                    | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
2. **Partition Score: 0.4646**
   - Group 1: **0.6851** | EXCEPT, BESIDES, SAVE, BUT                                        | CORRECT GROUP (NOT INCLUDING, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 37.3%)]
   - Group 2: **0.6289** | WANDS, PENTACLES, SWORDS, OPEL                                    | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
   - Group 3: **0.5286** | HEAL, KNIT, MEND, RECOVER                                         | CORRECT GROUP (GET BETTER, AS A BROKEN BONE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 33.3%)]
   - Group 4: **0.3326** | QUARTS, CUPS, PURL, CHORAL                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF GEMSTONES)
3. **Partition Score: 0.4614**
   - Group 1: **0.6851** | EXCEPT, BESIDES, SAVE, BUT                                        | CORRECT GROUP (NOT INCLUDING, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 37.3%)]
   - Group 2: **0.5286** | HEAL, KNIT, MEND, RECOVER                                         | CORRECT GROUP (GET BETTER, AS A BROKEN BONE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 33.3%)]
   - Group 3: **0.5018** | QUARTS, CUPS, CHORAL, OPEL                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF GEMSTONES)
   - Group 4: **0.3730** | PURL, WANDS, PENTACLES, SWORDS                                    | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
4. **Partition Score: 0.4605**
   - Group 1: **0.6566** | HEAL, MEND, SAVE, RECOVER                                         | INCORRECT (Max overlap: 3/4 with GET BETTER, AS A BROKEN BONE)
   - Group 2: **0.5018** | QUARTS, CUPS, CHORAL, OPEL                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF GEMSTONES)
   - Group 3: **0.4584** | EXCEPT, BESIDES, PURL, BUT                                        | INCORRECT (Max overlap: 3/4 with NOT INCLUDING) | [Pred Type: SYNONYM_OR_NEAR (64.2%, no-rel 25.0%)]
   - Group 4: **0.4030** | KNIT, WANDS, PENTACLES, SWORDS                                    | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
5. **Partition Score: 0.4601**
   - Group 1: **0.6851** | EXCEPT, BESIDES, SAVE, BUT                                        | CORRECT GROUP (NOT INCLUDING, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 37.3%)]
   - Group 2: **0.6289** | WANDS, PENTACLES, SWORDS, OPEL                                    | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
   - Group 3: **0.4691** | HEAL, MEND, CHORAL, RECOVER                                       | INCORRECT (Max overlap: 3/4 with GET BETTER, AS A BROKEN BONE) | [Pred Type: SYNONYM_OR_NEAR (68.9%, no-rel 17.7%)]
   - Group 4: **0.3456** | QUARTS, KNIT, CUPS, PURL                                          | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF GEMSTONES)

### Top Candidate Groups:
   - Group 1: **0.6851** | EXCEPT, BESIDES, SAVE, BUT                                        | CORRECT GROUP (NOT INCLUDING, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 37.3%)]
   - Group 2: **0.5018** | QUARTS, CUPS, CHORAL, OPEL                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF GEMSTONES)
   - Group 3: **0.4734** | HEAL, MEND, PURL, RECOVER                                         | INCORRECT (Max overlap: 3/4 with GET BETTER, AS A BROKEN BONE) | [Pred Type: SYNONYM_OR_NEAR (60.0%, no-rel 30.8%)]
   - Group 4: **0.4030** | KNIT, WANDS, PENTACLES, SWORDS                                    | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
   - Group 5: **0.6289** | WANDS, PENTACLES, SWORDS, OPEL                                    | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
   - Group 6: **0.5286** | HEAL, KNIT, MEND, RECOVER                                         | CORRECT GROUP (GET BETTER, AS A BROKEN BONE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 33.3%)]
   - Group 7: **0.3326** | QUARTS, CUPS, PURL, CHORAL                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF GEMSTONES)
   - Group 8: **0.3730** | PURL, WANDS, PENTACLES, SWORDS                                    | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
   - Group 9: **0.6566** | HEAL, MEND, SAVE, RECOVER                                         | INCORRECT (Max overlap: 3/4 with GET BETTER, AS A BROKEN BONE)
   - Group 10: **0.4584** | EXCEPT, BESIDES, PURL, BUT                                        | INCORRECT (Max overlap: 3/4 with NOT INCLUDING) | [Pred Type: SYNONYM_OR_NEAR (64.2%, no-rel 25.0%)]
   - Group 11: **0.4691** | HEAL, MEND, CHORAL, RECOVER                                       | INCORRECT (Max overlap: 3/4 with GET BETTER, AS A BROKEN BONE) | [Pred Type: SYNONYM_OR_NEAR (68.9%, no-rel 17.7%)]
   - Group 12: **0.3456** | QUARTS, KNIT, CUPS, PURL                                          | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF GEMSTONES)
   - Group 13: **0.5126** | EXCEPT, BESIDES, KNIT, BUT                                        | INCORRECT (Max overlap: 3/4 with NOT INCLUDING) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 33.8%)]
   - Group 14: **0.5915** | WANDS, PENTACLES, SWORDS, CHORAL                                  | INCORRECT (Max overlap: 3/4 with TAROT MINOR ARCANA SUITS)
   - Group 15: **0.3282** | QUARTS, CUPS, PURL, OPEL                                          | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF GEMSTONES)
   - Group 16: **0.5588** | WANDS, SWORDS, CHORAL, OPEL                                       | INCORRECT (Max overlap: 2/4 with TAROT MINOR ARCANA SUITS)
   - Group 17: **0.3392** | QUARTS, CUPS, PURL, PENTACLES                                     | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF GEMSTONES)
   - Group 18: **0.3324** | QUARTS, KNIT, CUPS, CHORAL                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF GEMSTONES)
   - Group 19: **0.4451** | EXCEPT, BESIDES, CHORAL, BUT                                      | INCORRECT (Max overlap: 3/4 with NOT INCLUDING) | [Pred Type: SYNONYM_OR_NEAR (70.2%, no-rel 14.5%)]
   - Group 20: **0.6027** | HEAL, BESIDES, MEND, RECOVER                                      | INCORRECT (Max overlap: 3/4 with GET BETTER, AS A BROKEN BONE) | [Pred Type: SYNONYM_OR_NEAR (52.8%, no-rel 40.4%)]

---

## Puzzle 18 (ID: 228)
**Words on Board:** GLYPH, ASSESS, HANDSOME, HOT, CHARACTER, BIG, ICON, IN, LEVY, FINE, LEGEND, LIPID, HIPPO, POPULAR, CHARGE, SYMBOL

### Ground Truth Categories:
* **Level 0 (OF-THE-MOMENT) [Type: SYNONYM_OR_NEAR]:** BIG, HOT, IN, POPULAR
* **Level 1 (PICTOGRAPH) [Type: SYNONYM_OR_NEAR]:** CHARACTER, GLYPH, ICON, SYMBOL
* **Level 2 (IMPOSE, AS A PENALTY) [Type: SYNONYM_OR_NEAR]:** ASSESS, CHARGE, FINE, LEVY
* **Level 3 (WORDS BEGINNING WITH BODY PARTS) [Type: WORD_FORM]:** HANDSOME, HIPPO, LEGEND, LIPID

### Top Candidate Partitions:
1. **Partition Score: 0.5100**
   - Group 1: **0.6453** | HOT, BIG, IN, POPULAR                                             | CORRECT GROUP (OF-THE-MOMENT, Level 0)
   - Group 2: **0.6308** | ASSESS, LEVY, FINE, CHARGE                                        | CORRECT GROUP (IMPOSE, AS A PENALTY, Level 2)
   - Group 3: **0.5600** | GLYPH, CHARACTER, ICON, SYMBOL                                    | CORRECT GROUP (PICTOGRAPH, Level 1) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 24.4%)]
   - Group 4: **0.4179** | HANDSOME, LEGEND, LIPID, HIPPO                                    | CORRECT GROUP (WORDS BEGINNING WITH BODY PARTS, Level 3)
2. **Partition Score: 0.5090**
   - Group 1: **0.6453** | HOT, BIG, IN, POPULAR                                             | CORRECT GROUP (OF-THE-MOMENT, Level 0)
   - Group 2: **0.6308** | ASSESS, LEVY, FINE, CHARGE                                        | CORRECT GROUP (IMPOSE, AS A PENALTY, Level 2)
   - Group 3: **0.5181** | GLYPH, HANDSOME, CHARACTER, SYMBOL                                | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (60.1%, no-rel 25.0%)]
   - Group 4: **0.4312** | ICON, LEGEND, LIPID, HIPPO                                        | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH BODY PARTS)
3. **Partition Score: 0.4931**
   - Group 1: **0.6584** | HANDSOME, HOT, BIG, POPULAR                                       | INCORRECT (Max overlap: 3/4 with OF-THE-MOMENT)
   - Group 2: **0.6308** | ASSESS, LEVY, FINE, CHARGE                                        | CORRECT GROUP (IMPOSE, AS A PENALTY, Level 2)
   - Group 3: **0.4312** | ICON, LEGEND, LIPID, HIPPO                                        | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH BODY PARTS)
   - Group 4: **0.4291** | GLYPH, CHARACTER, IN, SYMBOL                                      | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 18.0%)]
4. **Partition Score: 0.4917**
   - Group 1: **0.6453** | HOT, BIG, IN, POPULAR                                             | CORRECT GROUP (OF-THE-MOMENT, Level 0)
   - Group 2: **0.5600** | GLYPH, CHARACTER, ICON, SYMBOL                                    | CORRECT GROUP (PICTOGRAPH, Level 1) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 24.4%)]
   - Group 3: **0.5542** | ASSESS, HANDSOME, LEVY, CHARGE                                    | INCORRECT (Max overlap: 3/4 with IMPOSE, AS A PENALTY) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 29.5%)]
   - Group 4: **0.4101** | FINE, LEGEND, LIPID, HIPPO                                        | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH BODY PARTS)
5. **Partition Score: 0.4882**
   - Group 1: **0.6207** | HOT, BIG, IN, FINE                                                | INCORRECT (Max overlap: 3/4 with OF-THE-MOMENT)
   - Group 2: **0.5542** | ASSESS, HANDSOME, LEVY, CHARGE                                    | INCORRECT (Max overlap: 3/4 with IMPOSE, AS A PENALTY) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 29.5%)]
   - Group 3: **0.4985** | GLYPH, CHARACTER, POPULAR, SYMBOL                                 | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 28.5%)]
   - Group 4: **0.4312** | ICON, LEGEND, LIPID, HIPPO                                        | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH BODY PARTS)

### Top Candidate Groups:
   - Group 1: **0.6453** | HOT, BIG, IN, POPULAR                                             | CORRECT GROUP (OF-THE-MOMENT, Level 0)
   - Group 2: **0.6308** | ASSESS, LEVY, FINE, CHARGE                                        | CORRECT GROUP (IMPOSE, AS A PENALTY, Level 2)
   - Group 3: **0.5600** | GLYPH, CHARACTER, ICON, SYMBOL                                    | CORRECT GROUP (PICTOGRAPH, Level 1) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 24.4%)]
   - Group 4: **0.4179** | HANDSOME, LEGEND, LIPID, HIPPO                                    | CORRECT GROUP (WORDS BEGINNING WITH BODY PARTS, Level 3)
   - Group 5: **0.5181** | GLYPH, HANDSOME, CHARACTER, SYMBOL                                | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (60.1%, no-rel 25.0%)]
   - Group 6: **0.4312** | ICON, LEGEND, LIPID, HIPPO                                        | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH BODY PARTS)
   - Group 7: **0.6584** | HANDSOME, HOT, BIG, POPULAR                                       | INCORRECT (Max overlap: 3/4 with OF-THE-MOMENT)
   - Group 8: **0.4291** | GLYPH, CHARACTER, IN, SYMBOL                                      | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 18.0%)]
   - Group 9: **0.5542** | ASSESS, HANDSOME, LEVY, CHARGE                                    | INCORRECT (Max overlap: 3/4 with IMPOSE, AS A PENALTY) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 29.5%)]
   - Group 10: **0.4101** | FINE, LEGEND, LIPID, HIPPO                                        | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH BODY PARTS)
   - Group 11: **0.6207** | HOT, BIG, IN, FINE                                                | INCORRECT (Max overlap: 3/4 with OF-THE-MOMENT)
   - Group 12: **0.4985** | GLYPH, CHARACTER, POPULAR, SYMBOL                                 | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 28.5%)]
   - Group 13: **0.5055** | ASSESS, LEVY, POPULAR, CHARGE                                     | INCORRECT (Max overlap: 3/4 with IMPOSE, AS A PENALTY) | [Pred Type: SYNONYM_OR_NEAR (46.9%, no-rel 32.5%)]
   - Group 14: **0.5142** | HANDSOME, HOT, BIG, IN                                            | INCORRECT (Max overlap: 3/4 with OF-THE-MOMENT)
   - Group 15: **0.5350** | ASSESS, HANDSOME, FINE, CHARGE                                    | INCORRECT (Max overlap: 3/4 with IMPOSE, AS A PENALTY)
   - Group 16: **0.4522** | GLYPH, CHARACTER, LEVY, SYMBOL                                    | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (64.0%, no-rel 22.6%)]
   - Group 17: **0.3872** | LEGEND, LIPID, HIPPO, POPULAR                                     | INCORRECT (Max overlap: 3/4 with WORDS BEGINNING WITH BODY PARTS)
   - Group 18: **0.4251** | GLYPH, CHARACTER, FINE, SYMBOL                                    | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (58.9%, no-rel 25.0%)]
   - Group 19: **0.5149** | HANDSOME, LEVY, FINE, CHARGE                                      | INCORRECT (Max overlap: 3/4 with IMPOSE, AS A PENALTY)
   - Group 20: **0.4531** | GLYPH, ASSESS, CHARACTER, SYMBOL                                  | INCORRECT (Max overlap: 3/4 with PICTOGRAPH) | [Pred Type: SYNONYM_OR_NEAR (64.2%, no-rel 22.8%)]

---

## Puzzle 19 (ID: 956)
**Words on Board:** CHEEK, BUSHEL, METER, LIME, TRAFFIC, TEMPLE, PILOT, ACRE, GARAGE, EYE, VALET, FOOT, STONE, STREET, LIP, FLOOD

### Ground Truth Categories:
* **Level 0 (FACIAL FEATURES) [Type: SEMANTIC_SET]:** CHEEK, EYE, LIP, TEMPLE
* **Level 1 (KINDS OF PARKING) [Type: SEMANTIC_SET]:** GARAGE, METER, STREET, VALET
* **Level 2 (IMPERIAL UNITS) [Type: SEMANTIC_SET]:** ACRE, BUSHEL, FOOT, STONE
* **Level 3 (WORDS BEFORE "LIGHT") [Type: FILL_IN_THE_BLANK]:** FLOOD, LIME, PILOT, TRAFFIC

### Top Candidate Partitions:
1. **Partition Score: 0.4533**
   - Group 1: **0.5913** | LIME, TRAFFIC, STREET, FLOOD                                      | INCORRECT (Max overlap: 3/4 with WORDS BEFORE "LIGHT") | [Pred Type: FILL_IN_THE_BLANK (45.3%, no-rel 25.4%)]
   - Group 2: **0.5087** | BUSHEL, METER, ACRE, FOOT                                         | INCORRECT (Max overlap: 3/4 with IMPERIAL UNITS)
   - Group 3: **0.4334** | PILOT, GARAGE, VALET, STONE                                       | INCORRECT (Max overlap: 2/4 with KINDS OF PARKING)
   - Group 4: **0.4099** | CHEEK, TEMPLE, EYE, LIP                                           | CORRECT GROUP (FACIAL FEATURES, Level 0)
2. **Partition Score: 0.4513**
   - Group 1: **0.5575** | LIME, PILOT, STONE, FLOOD                                         | INCORRECT (Max overlap: 3/4 with WORDS BEFORE "LIGHT") | [Pred Type: FILL_IN_THE_BLANK (47.1%, no-rel 27.6%)]
   - Group 2: **0.5087** | BUSHEL, METER, ACRE, FOOT                                         | INCORRECT (Max overlap: 3/4 with IMPERIAL UNITS)
   - Group 3: **0.4431** | TRAFFIC, GARAGE, VALET, STREET                                    | INCORRECT (Max overlap: 3/4 with KINDS OF PARKING)
   - Group 4: **0.4099** | CHEEK, TEMPLE, EYE, LIP                                           | CORRECT GROUP (FACIAL FEATURES, Level 0)
3. **Partition Score: 0.4508**
   - Group 1: **0.5913** | LIME, TRAFFIC, STREET, FLOOD                                      | INCORRECT (Max overlap: 3/4 with WORDS BEFORE "LIGHT") | [Pred Type: FILL_IN_THE_BLANK (45.3%, no-rel 25.4%)]
   - Group 2: **0.4970** | PILOT, EYE, STONE, LIP                                            | INCORRECT (Max overlap: 2/4 with FACIAL FEATURES)
   - Group 3: **0.4459** | METER, ACRE, VALET, FOOT                                          | INCORRECT (Max overlap: 2/4 with KINDS OF PARKING)
   - Group 4: **0.4049** | CHEEK, BUSHEL, TEMPLE, GARAGE                                     | INCORRECT (Max overlap: 2/4 with FACIAL FEATURES)
4. **Partition Score: 0.4504**
   - Group 1: **0.5913** | LIME, TRAFFIC, STREET, FLOOD                                      | INCORRECT (Max overlap: 3/4 with WORDS BEFORE "LIGHT") | [Pred Type: FILL_IN_THE_BLANK (45.3%, no-rel 25.4%)]
   - Group 2: **0.4806** | METER, ACRE, FOOT, STONE                                          | INCORRECT (Max overlap: 3/4 with IMPERIAL UNITS)
   - Group 3: **0.4461** | BUSHEL, PILOT, GARAGE, VALET                                      | INCORRECT (Max overlap: 2/4 with KINDS OF PARKING)
   - Group 4: **0.4099** | CHEEK, TEMPLE, EYE, LIP                                           | CORRECT GROUP (FACIAL FEATURES, Level 0)
5. **Partition Score: 0.4503**
   - Group 1: **0.5913** | LIME, TRAFFIC, STREET, FLOOD                                      | INCORRECT (Max overlap: 3/4 with WORDS BEFORE "LIGHT") | [Pred Type: FILL_IN_THE_BLANK (45.3%, no-rel 25.4%)]
   - Group 2: **0.4977** | PILOT, ACRE, FOOT, STONE                                          | INCORRECT (Max overlap: 3/4 with IMPERIAL UNITS)
   - Group 3: **0.4284** | BUSHEL, METER, GARAGE, VALET                                      | INCORRECT (Max overlap: 3/4 with KINDS OF PARKING)
   - Group 4: **0.4099** | CHEEK, TEMPLE, EYE, LIP                                           | CORRECT GROUP (FACIAL FEATURES, Level 0)

### Top Candidate Groups:
   - Group 1: **0.5913** | LIME, TRAFFIC, STREET, FLOOD                                      | INCORRECT (Max overlap: 3/4 with WORDS BEFORE "LIGHT") | [Pred Type: FILL_IN_THE_BLANK (45.3%, no-rel 25.4%)]
   - Group 2: **0.5087** | BUSHEL, METER, ACRE, FOOT                                         | INCORRECT (Max overlap: 3/4 with IMPERIAL UNITS)
   - Group 3: **0.4334** | PILOT, GARAGE, VALET, STONE                                       | INCORRECT (Max overlap: 2/4 with KINDS OF PARKING)
   - Group 4: **0.4099** | CHEEK, TEMPLE, EYE, LIP                                           | CORRECT GROUP (FACIAL FEATURES, Level 0)
   - Group 5: **0.5575** | LIME, PILOT, STONE, FLOOD                                         | INCORRECT (Max overlap: 3/4 with WORDS BEFORE "LIGHT") | [Pred Type: FILL_IN_THE_BLANK (47.1%, no-rel 27.6%)]
   - Group 6: **0.4431** | TRAFFIC, GARAGE, VALET, STREET                                    | INCORRECT (Max overlap: 3/4 with KINDS OF PARKING)
   - Group 7: **0.4970** | PILOT, EYE, STONE, LIP                                            | INCORRECT (Max overlap: 2/4 with FACIAL FEATURES)
   - Group 8: **0.4459** | METER, ACRE, VALET, FOOT                                          | INCORRECT (Max overlap: 2/4 with KINDS OF PARKING)
   - Group 9: **0.4049** | CHEEK, BUSHEL, TEMPLE, GARAGE                                     | INCORRECT (Max overlap: 2/4 with FACIAL FEATURES)
   - Group 10: **0.4806** | METER, ACRE, FOOT, STONE                                          | INCORRECT (Max overlap: 3/4 with IMPERIAL UNITS)
   - Group 11: **0.4461** | BUSHEL, PILOT, GARAGE, VALET                                      | INCORRECT (Max overlap: 2/4 with KINDS OF PARKING)
   - Group 12: **0.4977** | PILOT, ACRE, FOOT, STONE                                          | INCORRECT (Max overlap: 3/4 with IMPERIAL UNITS)
   - Group 13: **0.4284** | BUSHEL, METER, GARAGE, VALET                                      | INCORRECT (Max overlap: 3/4 with KINDS OF PARKING)
   - Group 14: **0.5856** | LIME, TRAFFIC, PILOT, FLOOD                                       | CORRECT GROUP (WORDS BEFORE "LIGHT", Level 3) | [Pred Type: FILL_IN_THE_BLANK (56.0%, no-rel 18.4%)]
   - Group 15: **0.4105** | GARAGE, VALET, STONE, STREET                                      | INCORRECT (Max overlap: 3/4 with KINDS OF PARKING) | [Pred Type: NAMED_ENTITY_SET (45.1%, no-rel 11.0%)]
   - Group 16: **0.5283** | LIME, STONE, STREET, FLOOD                                        | INCORRECT (Max overlap: 2/4 with WORDS BEFORE "LIGHT") | [Pred Type: FILL_IN_THE_BLANK (56.4%, no-rel 20.6%)]
   - Group 17: **0.4442** | TRAFFIC, PILOT, GARAGE, VALET                                     | INCORRECT (Max overlap: 2/4 with WORDS BEFORE "LIGHT")
   - Group 18: **0.5607** | TRAFFIC, PILOT, STREET, FLOOD                                     | INCORRECT (Max overlap: 3/4 with WORDS BEFORE "LIGHT")
   - Group 19: **0.4122** | LIME, GARAGE, VALET, STONE                                        | INCORRECT (Max overlap: 2/4 with KINDS OF PARKING)
   - Group 20: **0.4192** | BUSHEL, GARAGE, VALET, STREET                                     | INCORRECT (Max overlap: 3/4 with KINDS OF PARKING)

---

## Puzzle 20 (ID: 124)
**Words on Board:** METER, LUXOR, RAPPER, RHYME, PINTO, KIDNEY, CREATOR, VERSE, LIMERICK, LAGOS, LINCOLN, DUDE, LIMA, FAVA, STALLION, LINE

### Ground Truth Categories:
* **Level 0 (BEANS) [Type: SEMANTIC_SET]:** FAVA, KIDNEY, LIMA, PINTO
* **Level 1 (CITIES BEGINNING WITH “L”) [Type: WORD_FORM]:** LAGOS, LIMERICK, LINCOLN, LUXOR
* **Level 2 (POETRY TERMS) [Type: SEMANTIC_SET]:** LINE, METER, RHYME, VERSE
* **Level 3 (“THE(E) ___” RAPPERS) [Type: FILL_IN_THE_BLANK]:** CREATOR, DUDE, RAPPER, STALLION

### Top Candidate Partitions:
1. **Partition Score: 0.5456**
   - Group 1: **0.7138** | RHYME, VERSE, LIMERICK, LINE                                      | INCORRECT (Max overlap: 3/4 with POETRY TERMS) | [Pred Type: SYNONYM_OR_NEAR (67.7%, no-rel 25.4%)]
   - Group 2: **0.6564** | PINTO, KIDNEY, LIMA, FAVA                                         | CORRECT GROUP (BEANS, Level 0)
   - Group 3: **0.5663** | LUXOR, LAGOS, LINCOLN, STALLION                                   | INCORRECT (Max overlap: 3/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (49.6%, no-rel 24.4%)]
   - Group 4: **0.4606** | METER, RAPPER, CREATOR, DUDE                                      | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS)
2. **Partition Score: 0.5325**
   - Group 1: **0.7138** | RHYME, VERSE, LIMERICK, LINE                                      | INCORRECT (Max overlap: 3/4 with POETRY TERMS) | [Pred Type: SYNONYM_OR_NEAR (67.7%, no-rel 25.4%)]
   - Group 2: **0.6564** | PINTO, KIDNEY, LIMA, FAVA                                         | CORRECT GROUP (BEANS, Level 0)
   - Group 3: **0.4911** | LUXOR, LAGOS, LINCOLN, DUDE                                       | INCORRECT (Max overlap: 3/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (50.9%, no-rel 23.1%)]
   - Group 4: **0.4624** | METER, RAPPER, CREATOR, STALLION                                  | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS)
3. **Partition Score: 0.5312**
   - Group 1: **0.6701** | METER, RHYME, VERSE, LINE                                         | CORRECT GROUP (POETRY TERMS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (61.3%, no-rel 28.3%)]
   - Group 2: **0.6564** | PINTO, KIDNEY, LIMA, FAVA                                         | CORRECT GROUP (BEANS, Level 0)
   - Group 3: **0.5384** | RAPPER, CREATOR, DUDE, STALLION                                   | CORRECT GROUP (“THE(E) ___” RAPPERS, Level 3) | [Pred Type: NAMED_ENTITY_SET (45.0%, no-rel 24.5%)]
   - Group 4: **0.4522** | LUXOR, LIMERICK, LAGOS, LINCOLN                                   | CORRECT GROUP (CITIES BEGINNING WITH “L”, Level 1) | [Pred Type: NAMED_ENTITY_SET (50.1%, no-rel 10.2%)]
4. **Partition Score: 0.5254**
   - Group 1: **0.6701** | METER, RHYME, VERSE, LINE                                         | CORRECT GROUP (POETRY TERMS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (61.3%, no-rel 28.3%)]
   - Group 2: **0.6564** | PINTO, KIDNEY, LIMA, FAVA                                         | CORRECT GROUP (BEANS, Level 0)
   - Group 3: **0.5192** | RAPPER, CREATOR, LINCOLN, DUDE                                    | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS) | [Pred Type: NAMED_ENTITY_SET (49.4%, no-rel 22.0%)]
   - Group 4: **0.4479** | LUXOR, LIMERICK, LAGOS, STALLION                                  | INCORRECT (Max overlap: 3/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 10.6%)]
5. **Partition Score: 0.5245**
   - Group 1: **0.6701** | METER, RHYME, VERSE, LINE                                         | CORRECT GROUP (POETRY TERMS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (61.3%, no-rel 28.3%)]
   - Group 2: **0.6564** | PINTO, KIDNEY, LIMA, FAVA                                         | CORRECT GROUP (BEANS, Level 0)
   - Group 3: **0.4911** | LUXOR, LAGOS, LINCOLN, DUDE                                       | INCORRECT (Max overlap: 3/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (50.9%, no-rel 23.1%)]
   - Group 4: **0.4565** | RAPPER, CREATOR, LIMERICK, STALLION                               | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS)

### Top Candidate Groups:
   - Group 1: **0.7138** | RHYME, VERSE, LIMERICK, LINE                                      | INCORRECT (Max overlap: 3/4 with POETRY TERMS) | [Pred Type: SYNONYM_OR_NEAR (67.7%, no-rel 25.4%)]
   - Group 2: **0.6564** | PINTO, KIDNEY, LIMA, FAVA                                         | CORRECT GROUP (BEANS, Level 0)
   - Group 3: **0.5663** | LUXOR, LAGOS, LINCOLN, STALLION                                   | INCORRECT (Max overlap: 3/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (49.6%, no-rel 24.4%)]
   - Group 4: **0.4606** | METER, RAPPER, CREATOR, DUDE                                      | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS)
   - Group 5: **0.4911** | LUXOR, LAGOS, LINCOLN, DUDE                                       | INCORRECT (Max overlap: 3/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (50.9%, no-rel 23.1%)]
   - Group 6: **0.4624** | METER, RAPPER, CREATOR, STALLION                                  | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS)
   - Group 7: **0.6701** | METER, RHYME, VERSE, LINE                                         | CORRECT GROUP (POETRY TERMS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (61.3%, no-rel 28.3%)]
   - Group 8: **0.5384** | RAPPER, CREATOR, DUDE, STALLION                                   | CORRECT GROUP (“THE(E) ___” RAPPERS, Level 3) | [Pred Type: NAMED_ENTITY_SET (45.0%, no-rel 24.5%)]
   - Group 9: **0.4522** | LUXOR, LIMERICK, LAGOS, LINCOLN                                   | CORRECT GROUP (CITIES BEGINNING WITH “L”, Level 1) | [Pred Type: NAMED_ENTITY_SET (50.1%, no-rel 10.2%)]
   - Group 10: **0.5192** | RAPPER, CREATOR, LINCOLN, DUDE                                    | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS) | [Pred Type: NAMED_ENTITY_SET (49.4%, no-rel 22.0%)]
   - Group 11: **0.4479** | LUXOR, LIMERICK, LAGOS, STALLION                                  | INCORRECT (Max overlap: 3/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 10.6%)]
   - Group 12: **0.4565** | RAPPER, CREATOR, LIMERICK, STALLION                               | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS)
   - Group 13: **0.4856** | LUXOR, LAGOS, DUDE, STALLION                                      | INCORRECT (Max overlap: 2/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (45.1%, no-rel 26.8%)]
   - Group 14: **0.4438** | METER, RAPPER, CREATOR, LINCOLN                                   | INCORRECT (Max overlap: 2/4 with “THE(E) ___” RAPPERS)
   - Group 15: **0.5706** | LUXOR, LAGOS, LIMA, FAVA                                          | INCORRECT (Max overlap: 2/4 with CITIES BEGINNING WITH “L”)
   - Group 16: **0.5244** | PINTO, KIDNEY, LINCOLN, STALLION                                  | INCORRECT (Max overlap: 2/4 with BEANS)
   - Group 17: **0.5374** | LUXOR, CREATOR, LAGOS, LINCOLN                                    | INCORRECT (Max overlap: 3/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (52.2%, no-rel 21.8%)]
   - Group 18: **0.4236** | METER, RAPPER, DUDE, STALLION                                     | INCORRECT (Max overlap: 3/4 with “THE(E) ___” RAPPERS)
   - Group 19: **0.4734** | LAGOS, LINCOLN, DUDE, STALLION                                    | INCORRECT (Max overlap: 2/4 with CITIES BEGINNING WITH “L”) | [Pred Type: NAMED_ENTITY_SET (50.4%, no-rel 23.3%)]
   - Group 20: **0.4447** | METER, LUXOR, RAPPER, CREATOR                                     | INCORRECT (Max overlap: 2/4 with “THE(E) ___” RAPPERS) | [Pred Type: NAMED_ENTITY_SET (45.7%, no-rel 20.3%)]

---

## Puzzle 21 (ID: 746)
**Words on Board:** SUITS, BOJACK, CHEESE, ENIGMA, MCQUEEN, PINBALL, DRESSING, MATLOCK, PROTEIN, LOVELACE, GOLIATH, VENDING, SEWING, LETTUCE, DAMAGES, HAWKING

### Ground Truth Categories:
* **Level 0 (COMPONENTS OF A SALAD) [Type: SEMANTIC_SET]:** CHEESE, DRESSING, LETTUCE, PROTEIN
* **Level 1 (KINDS OF MACHINES) [Type: FILL_IN_THE_BLANK]:** ENIGMA, PINBALL, SEWING, VENDING
* **Level 2 (LEGAL DRAMAS) [Type: NAMED_ENTITY_SET]:** DAMAGES, GOLIATH, MATLOCK, SUITS
* **Level 3 (ENDING WITH PLAYING CARDS) [Type: WORDPLAY_TRANSFORM]:** BOJACK, HAWKING, LOVELACE, MCQUEEN

### Top Candidate Partitions:
1. **Partition Score: 0.4531**
   - Group 1: **0.5600** | BOJACK, MCQUEEN, MATLOCK, LOVELACE                                | INCORRECT (Max overlap: 3/4 with ENDING WITH PLAYING CARDS)
   - Group 2: **0.5126** | ENIGMA, PINBALL, PROTEIN, GOLIATH                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES)
   - Group 3: **0.4219** | VENDING, SEWING, DAMAGES, HAWKING                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 20.6%)]
   - Group 4: **0.4193** | SUITS, CHEESE, DRESSING, LETTUCE                                  | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD) | [Pred Type: SEMANTIC_SET (47.2%, no-rel 16.9%)]
2. **Partition Score: 0.4508**
   - Group 1: **0.5520** | BOJACK, MCQUEEN, MATLOCK, GOLIATH                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH PLAYING CARDS)
   - Group 2: **0.5050** | ENIGMA, PINBALL, PROTEIN, LOVELACE                                | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES)
   - Group 3: **0.4219** | VENDING, SEWING, DAMAGES, HAWKING                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 20.6%)]
   - Group 4: **0.4193** | SUITS, CHEESE, DRESSING, LETTUCE                                  | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD) | [Pred Type: SEMANTIC_SET (47.2%, no-rel 16.9%)]
3. **Partition Score: 0.4507**
   - Group 1: **0.5547** | BOJACK, ENIGMA, MCQUEEN, MATLOCK                                  | INCORRECT (Max overlap: 2/4 with ENDING WITH PLAYING CARDS)
   - Group 2: **0.5028** | PINBALL, PROTEIN, LOVELACE, GOLIATH                               | INCORRECT (Max overlap: 1/4 with KINDS OF MACHINES)
   - Group 3: **0.4219** | VENDING, SEWING, DAMAGES, HAWKING                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 20.6%)]
   - Group 4: **0.4193** | SUITS, CHEESE, DRESSING, LETTUCE                                  | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD) | [Pred Type: SEMANTIC_SET (47.2%, no-rel 16.9%)]
4. **Partition Score: 0.4502**
   - Group 1: **0.5520** | BOJACK, MCQUEEN, MATLOCK, GOLIATH                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH PLAYING CARDS)
   - Group 2: **0.4420** | ENIGMA, PINBALL, LOVELACE, SEWING                                 | INCORRECT (Max overlap: 3/4 with KINDS OF MACHINES)
   - Group 3: **0.4414** | DRESSING, VENDING, DAMAGES, HAWKING                               | INCORRECT (Max overlap: 1/4 with COMPONENTS OF A SALAD) | [Pred Type: SYNONYM_OR_NEAR (68.9%, no-rel 17.8%)]
   - Group 4: **0.4341** | SUITS, CHEESE, PROTEIN, LETTUCE                                   | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD)
5. **Partition Score: 0.4496**
   - Group 1: **0.5462** | BOJACK, MCQUEEN, LOVELACE, GOLIATH                                | INCORRECT (Max overlap: 3/4 with ENDING WITH PLAYING CARDS)
   - Group 2: **0.5022** | ENIGMA, PINBALL, MATLOCK, PROTEIN                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES)
   - Group 3: **0.4219** | VENDING, SEWING, DAMAGES, HAWKING                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 20.6%)]
   - Group 4: **0.4193** | SUITS, CHEESE, DRESSING, LETTUCE                                  | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD) | [Pred Type: SEMANTIC_SET (47.2%, no-rel 16.9%)]

### Top Candidate Groups:
   - Group 1: **0.5600** | BOJACK, MCQUEEN, MATLOCK, LOVELACE                                | INCORRECT (Max overlap: 3/4 with ENDING WITH PLAYING CARDS)
   - Group 2: **0.5126** | ENIGMA, PINBALL, PROTEIN, GOLIATH                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES)
   - Group 3: **0.4219** | VENDING, SEWING, DAMAGES, HAWKING                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 20.6%)]
   - Group 4: **0.4193** | SUITS, CHEESE, DRESSING, LETTUCE                                  | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD) | [Pred Type: SEMANTIC_SET (47.2%, no-rel 16.9%)]
   - Group 5: **0.5520** | BOJACK, MCQUEEN, MATLOCK, GOLIATH                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH PLAYING CARDS)
   - Group 6: **0.5050** | ENIGMA, PINBALL, PROTEIN, LOVELACE                                | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES)
   - Group 7: **0.5547** | BOJACK, ENIGMA, MCQUEEN, MATLOCK                                  | INCORRECT (Max overlap: 2/4 with ENDING WITH PLAYING CARDS)
   - Group 8: **0.5028** | PINBALL, PROTEIN, LOVELACE, GOLIATH                               | INCORRECT (Max overlap: 1/4 with KINDS OF MACHINES)
   - Group 9: **0.4420** | ENIGMA, PINBALL, LOVELACE, SEWING                                 | INCORRECT (Max overlap: 3/4 with KINDS OF MACHINES)
   - Group 10: **0.4414** | DRESSING, VENDING, DAMAGES, HAWKING                               | INCORRECT (Max overlap: 1/4 with COMPONENTS OF A SALAD) | [Pred Type: SYNONYM_OR_NEAR (68.9%, no-rel 17.8%)]
   - Group 11: **0.4341** | SUITS, CHEESE, PROTEIN, LETTUCE                                   | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD)
   - Group 12: **0.5462** | BOJACK, MCQUEEN, LOVELACE, GOLIATH                                | INCORRECT (Max overlap: 3/4 with ENDING WITH PLAYING CARDS)
   - Group 13: **0.5022** | ENIGMA, PINBALL, MATLOCK, PROTEIN                                 | INCORRECT (Max overlap: 2/4 with KINDS OF MACHINES)
   - Group 14: **0.4603** | CHEESE, PROTEIN, GOLIATH, LETTUCE                                 | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD)
   - Group 15: **0.4244** | SUITS, ENIGMA, PINBALL, SEWING                                    | INCORRECT (Max overlap: 3/4 with KINDS OF MACHINES)
   - Group 16: **0.4561** | SUITS, ENIGMA, PINBALL, GOLIATH                                   | INCORRECT (Max overlap: 2/4 with LEGAL DRAMAS)
   - Group 17: **0.4251** | CHEESE, PROTEIN, SEWING, LETTUCE                                  | INCORRECT (Max overlap: 3/4 with COMPONENTS OF A SALAD)
   - Group 18: **0.4967** | BOJACK, ENIGMA, PINBALL, LOVELACE                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH PLAYING CARDS)
   - Group 19: **0.4927** | SUITS, MCQUEEN, MATLOCK, GOLIATH                                  | INCORRECT (Max overlap: 3/4 with LEGAL DRAMAS)
   - Group 20: **0.5058** | BOJACK, MCQUEEN, PINBALL, MATLOCK                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH PLAYING CARDS)

---

## Puzzle 22 (ID: 87)
**Words on Board:** HORSE, PLANT, RABBIT, PETAL, OGRE, GNOME, STALK, MOLE, DRAGON, LEAF, TIGER, GOBLIN, AGENT, TROLL, SPY, BUD

### Ground Truth Categories:
* **Level 0 (CREATURES IN FOLKLORE) [Type: SEMANTIC_SET]:** GNOME, GOBLIN, OGRE, TROLL
* **Level 1 (FLOWER PARTS) [Type: SEMANTIC_SET]:** BUD, LEAF, PETAL, STALK
* **Level 2 (ONE INVOLVED IN ESPIONAGE) [Type: SYNONYM_OR_NEAR]:** AGENT, MOLE, PLANT, SPY
* **Level 3 (CHINESE ZODIAC ANIMALS) [Type: NAMED_ENTITY_SET]:** DRAGON, HORSE, RABBIT, TIGER

### Top Candidate Partitions:
1. **Partition Score: 0.4746**
   - Group 1: **0.5488** | HORSE, RABBIT, MOLE, TIGER                                        | INCORRECT (Max overlap: 3/4 with CHINESE ZODIAC ANIMALS)
   - Group 2: **0.5472** | OGRE, GNOME, DRAGON, GOBLIN                                       | INCORRECT (Max overlap: 3/4 with CREATURES IN FOLKLORE)
   - Group 3: **0.4613** | PETAL, STALK, LEAF, BUD                                           | CORRECT GROUP (FLOWER PARTS, Level 1)
   - Group 4: **0.4366** | PLANT, AGENT, TROLL, SPY                                          | INCORRECT (Max overlap: 3/4 with ONE INVOLVED IN ESPIONAGE) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 29.9%)]
2. **Partition Score: 0.4701**
   - Group 1: **0.5056** | HORSE, RABBIT, OGRE, MOLE                                         | INCORRECT (Max overlap: 2/4 with CHINESE ZODIAC ANIMALS)
   - Group 2: **0.4793** | PLANT, DRAGON, TIGER, TROLL                                       | INCORRECT (Max overlap: 2/4 with CHINESE ZODIAC ANIMALS)
   - Group 3: **0.4635** | GNOME, GOBLIN, AGENT, SPY                                         | INCORRECT (Max overlap: 2/4 with CREATURES IN FOLKLORE) | [Pred Type: SYNONYM_OR_NEAR (66.4%, no-rel 17.3%)]
   - Group 4: **0.4613** | PETAL, STALK, LEAF, BUD                                           | CORRECT GROUP (FLOWER PARTS, Level 1)
3. **Partition Score: 0.4591**
   - Group 1: **0.5006** | HORSE, RABBIT, DRAGON, TIGER                                      | CORRECT GROUP (CHINESE ZODIAC ANIMALS, Level 3)
   - Group 2: **0.4933** | OGRE, GNOME, MOLE, GOBLIN                                         | INCORRECT (Max overlap: 3/4 with CREATURES IN FOLKLORE)
   - Group 3: **0.4613** | PETAL, STALK, LEAF, BUD                                           | CORRECT GROUP (FLOWER PARTS, Level 1)
   - Group 4: **0.4366** | PLANT, AGENT, TROLL, SPY                                          | INCORRECT (Max overlap: 3/4 with ONE INVOLVED IN ESPIONAGE) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 29.9%)]
4. **Partition Score: 0.4576**
   - Group 1: **0.5488** | HORSE, RABBIT, MOLE, TIGER                                        | INCORRECT (Max overlap: 3/4 with CHINESE ZODIAC ANIMALS)
   - Group 2: **0.5158** | OGRE, GNOME, GOBLIN, TROLL                                        | CORRECT GROUP (CREATURES IN FOLKLORE, Level 0)
   - Group 3: **0.4613** | PETAL, STALK, LEAF, BUD                                           | CORRECT GROUP (FLOWER PARTS, Level 1)
   - Group 4: **0.4150** | PLANT, DRAGON, AGENT, SPY                                         | INCORRECT (Max overlap: 3/4 with ONE INVOLVED IN ESPIONAGE) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 27.4%)]
5. **Partition Score: 0.4552**
   - Group 1: **0.5482** | PLANT, PETAL, STALK, LEAF                                         | INCORRECT (Max overlap: 3/4 with FLOWER PARTS)
   - Group 2: **0.5472** | OGRE, GNOME, DRAGON, GOBLIN                                       | INCORRECT (Max overlap: 3/4 with CREATURES IN FOLKLORE)
   - Group 3: **0.4181** | HORSE, RABBIT, TIGER, BUD                                         | INCORRECT (Max overlap: 3/4 with CHINESE ZODIAC ANIMALS)
   - Group 4: **0.4147** | MOLE, AGENT, TROLL, SPY                                           | INCORRECT (Max overlap: 3/4 with ONE INVOLVED IN ESPIONAGE) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 17.7%)]

### Top Candidate Groups:
   - Group 1: **0.5488** | HORSE, RABBIT, MOLE, TIGER                                        | INCORRECT (Max overlap: 3/4 with CHINESE ZODIAC ANIMALS)
   - Group 2: **0.5472** | OGRE, GNOME, DRAGON, GOBLIN                                       | INCORRECT (Max overlap: 3/4 with CREATURES IN FOLKLORE)
   - Group 3: **0.4613** | PETAL, STALK, LEAF, BUD                                           | CORRECT GROUP (FLOWER PARTS, Level 1)
   - Group 4: **0.4366** | PLANT, AGENT, TROLL, SPY                                          | INCORRECT (Max overlap: 3/4 with ONE INVOLVED IN ESPIONAGE) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 29.9%)]
   - Group 5: **0.5056** | HORSE, RABBIT, OGRE, MOLE                                         | INCORRECT (Max overlap: 2/4 with CHINESE ZODIAC ANIMALS)
   - Group 6: **0.4793** | PLANT, DRAGON, TIGER, TROLL                                       | INCORRECT (Max overlap: 2/4 with CHINESE ZODIAC ANIMALS)
   - Group 7: **0.4635** | GNOME, GOBLIN, AGENT, SPY                                         | INCORRECT (Max overlap: 2/4 with CREATURES IN FOLKLORE) | [Pred Type: SYNONYM_OR_NEAR (66.4%, no-rel 17.3%)]
   - Group 8: **0.5006** | HORSE, RABBIT, DRAGON, TIGER                                      | CORRECT GROUP (CHINESE ZODIAC ANIMALS, Level 3)
   - Group 9: **0.4933** | OGRE, GNOME, MOLE, GOBLIN                                         | INCORRECT (Max overlap: 3/4 with CREATURES IN FOLKLORE)
   - Group 10: **0.5158** | OGRE, GNOME, GOBLIN, TROLL                                        | CORRECT GROUP (CREATURES IN FOLKLORE, Level 0)
   - Group 11: **0.4150** | PLANT, DRAGON, AGENT, SPY                                         | INCORRECT (Max overlap: 3/4 with ONE INVOLVED IN ESPIONAGE) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 27.4%)]
   - Group 12: **0.5482** | PLANT, PETAL, STALK, LEAF                                         | INCORRECT (Max overlap: 3/4 with FLOWER PARTS)
   - Group 13: **0.4181** | HORSE, RABBIT, TIGER, BUD                                         | INCORRECT (Max overlap: 3/4 with CHINESE ZODIAC ANIMALS)
   - Group 14: **0.4147** | MOLE, AGENT, TROLL, SPY                                           | INCORRECT (Max overlap: 3/4 with ONE INVOLVED IN ESPIONAGE) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 17.7%)]
   - Group 15: **0.4989** | RABBIT, OGRE, MOLE, TIGER                                         | INCORRECT (Max overlap: 2/4 with CHINESE ZODIAC ANIMALS)
   - Group 16: **0.4713** | HORSE, GNOME, DRAGON, GOBLIN                                      | INCORRECT (Max overlap: 2/4 with CHINESE ZODIAC ANIMALS)
   - Group 17: **0.5375** | HORSE, OGRE, MOLE, TIGER                                          | INCORRECT (Max overlap: 2/4 with CHINESE ZODIAC ANIMALS)
   - Group 18: **0.4448** | RABBIT, GNOME, DRAGON, GOBLIN                                     | INCORRECT (Max overlap: 2/4 with CHINESE ZODIAC ANIMALS)
   - Group 19: **0.4623** | GNOME, DRAGON, TIGER, GOBLIN                                      | INCORRECT (Max overlap: 2/4 with CREATURES IN FOLKLORE)
   - Group 20: **0.5536** | GNOME, DRAGON, GOBLIN, TROLL                                      | INCORRECT (Max overlap: 3/4 with CREATURES IN FOLKLORE)

---

## Puzzle 23 (ID: 357)
**Words on Board:** BUFFALO, FOLLOWERS, BILLINGS, APARTMENT, LIKES, STOCKS, SHARES, MOBILE, INSULTS, EQUITY, SHEEP, PUPPETS, LEMMINGS, PHOENIX, SHOVELS, OPTIONS

### Ground Truth Categories:
* **Level 0 (CONFORMISTS) [Type: SYNONYM_OR_NEAR]:** FOLLOWERS, LEMMINGS, PUPPETS, SHEEP
* **Level 1 (COMPANY OWNERSHIP OFFERS) [Type: SYNONYM_OR_NEAR]:** EQUITY, OPTIONS, SHARES, STOCKS
* **Level 2 (U.S. CITIES) [Type: NAMED_ENTITY_SET]:** BILLINGS, BUFFALO, MOBILE, PHOENIX
* **Level 3 (WHAT “DIGS” MIGHT MEAN) [Type: WORDPLAY_TRANSFORM]:** APARTMENT, INSULTS, LIKES, SHOVELS

### Top Candidate Partitions:
1. **Partition Score: 0.5091**
   - Group 1: **0.5815** | LIKES, STOCKS, SHARES, EQUITY                                     | INCORRECT (Max overlap: 3/4 with COMPANY OWNERSHIP OFFERS) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 24.6%)]
   - Group 2: **0.5761** | BUFFALO, BILLINGS, MOBILE, PHOENIX                                | CORRECT GROUP (U.S. CITIES, Level 2) | [Pred Type: NAMED_ENTITY_SET (51.2%, no-rel 23.9%)]
   - Group 3: **0.5546** | FOLLOWERS, SHEEP, PUPPETS, LEMMINGS                               | CORRECT GROUP (CONFORMISTS, Level 0) | [Pred Type: NAMED_ENTITY_SET (49.4%, no-rel 20.6%)]
   - Group 4: **0.4522** | APARTMENT, INSULTS, SHOVELS, OPTIONS                              | INCORRECT (Max overlap: 3/4 with WHAT “DIGS” MIGHT MEAN)
2. **Partition Score: 0.5086**
   - Group 1: **0.5761** | BUFFALO, BILLINGS, MOBILE, PHOENIX                                | CORRECT GROUP (U.S. CITIES, Level 2) | [Pred Type: NAMED_ENTITY_SET (51.2%, no-rel 23.9%)]
   - Group 2: **0.5546** | FOLLOWERS, SHEEP, PUPPETS, LEMMINGS                               | CORRECT GROUP (CONFORMISTS, Level 0) | [Pred Type: NAMED_ENTITY_SET (49.4%, no-rel 20.6%)]
   - Group 3: **0.5297** | LIKES, SHARES, INSULTS, EQUITY                                    | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 4: **0.4692** | APARTMENT, STOCKS, SHOVELS, OPTIONS                               | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)
3. **Partition Score: 0.5064**
   - Group 1: **0.5761** | BUFFALO, BILLINGS, MOBILE, PHOENIX                                | CORRECT GROUP (U.S. CITIES, Level 2) | [Pred Type: NAMED_ENTITY_SET (51.2%, no-rel 23.9%)]
   - Group 2: **0.5546** | FOLLOWERS, SHEEP, PUPPETS, LEMMINGS                               | CORRECT GROUP (CONFORMISTS, Level 0) | [Pred Type: NAMED_ENTITY_SET (49.4%, no-rel 20.6%)]
   - Group 3: **0.5164** | LIKES, INSULTS, SHOVELS, OPTIONS                                  | INCORRECT (Max overlap: 3/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 4: **0.4698** | APARTMENT, STOCKS, SHARES, EQUITY                                 | INCORRECT (Max overlap: 3/4 with COMPANY OWNERSHIP OFFERS)
4. **Partition Score: 0.5048**
   - Group 1: **0.5815** | LIKES, STOCKS, SHARES, EQUITY                                     | INCORRECT (Max overlap: 3/4 with COMPANY OWNERSHIP OFFERS) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 24.6%)]
   - Group 2: **0.5044** | INSULTS, PUPPETS, SHOVELS, OPTIONS                                | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 3: **0.4940** | BILLINGS, APARTMENT, MOBILE, PHOENIX                              | INCORRECT (Max overlap: 3/4 with U.S. CITIES) | [Pred Type: NAMED_ENTITY_SET (46.5%, no-rel 24.4%)]
   - Group 4: **0.4921** | BUFFALO, FOLLOWERS, SHEEP, LEMMINGS                               | INCORRECT (Max overlap: 3/4 with CONFORMISTS)
5. **Partition Score: 0.5047**
   - Group 1: **0.5815** | LIKES, STOCKS, SHARES, EQUITY                                     | INCORRECT (Max overlap: 3/4 with COMPANY OWNERSHIP OFFERS) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 24.6%)]
   - Group 2: **0.5036** | BUFFALO, MOBILE, SHEEP, PHOENIX                                   | INCORRECT (Max overlap: 3/4 with U.S. CITIES)
   - Group 3: **0.4935** | FOLLOWERS, BILLINGS, APARTMENT, OPTIONS                           | INCORRECT (Max overlap: 1/4 with CONFORMISTS)
   - Group 4: **0.4923** | INSULTS, PUPPETS, LEMMINGS, SHOVELS                               | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)

### Top Candidate Groups:
   - Group 1: **0.5815** | LIKES, STOCKS, SHARES, EQUITY                                     | INCORRECT (Max overlap: 3/4 with COMPANY OWNERSHIP OFFERS) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 24.6%)]
   - Group 2: **0.5761** | BUFFALO, BILLINGS, MOBILE, PHOENIX                                | CORRECT GROUP (U.S. CITIES, Level 2) | [Pred Type: NAMED_ENTITY_SET (51.2%, no-rel 23.9%)]
   - Group 3: **0.5546** | FOLLOWERS, SHEEP, PUPPETS, LEMMINGS                               | CORRECT GROUP (CONFORMISTS, Level 0) | [Pred Type: NAMED_ENTITY_SET (49.4%, no-rel 20.6%)]
   - Group 4: **0.4522** | APARTMENT, INSULTS, SHOVELS, OPTIONS                              | INCORRECT (Max overlap: 3/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 5: **0.5297** | LIKES, SHARES, INSULTS, EQUITY                                    | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 6: **0.4692** | APARTMENT, STOCKS, SHOVELS, OPTIONS                               | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 7: **0.5164** | LIKES, INSULTS, SHOVELS, OPTIONS                                  | INCORRECT (Max overlap: 3/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 8: **0.4698** | APARTMENT, STOCKS, SHARES, EQUITY                                 | INCORRECT (Max overlap: 3/4 with COMPANY OWNERSHIP OFFERS)
   - Group 9: **0.5044** | INSULTS, PUPPETS, SHOVELS, OPTIONS                                | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 10: **0.4940** | BILLINGS, APARTMENT, MOBILE, PHOENIX                              | INCORRECT (Max overlap: 3/4 with U.S. CITIES) | [Pred Type: NAMED_ENTITY_SET (46.5%, no-rel 24.4%)]
   - Group 11: **0.4921** | BUFFALO, FOLLOWERS, SHEEP, LEMMINGS                               | INCORRECT (Max overlap: 3/4 with CONFORMISTS)
   - Group 12: **0.5036** | BUFFALO, MOBILE, SHEEP, PHOENIX                                   | INCORRECT (Max overlap: 3/4 with U.S. CITIES)
   - Group 13: **0.4935** | FOLLOWERS, BILLINGS, APARTMENT, OPTIONS                           | INCORRECT (Max overlap: 1/4 with CONFORMISTS)
   - Group 14: **0.4923** | INSULTS, PUPPETS, LEMMINGS, SHOVELS                               | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 15: **0.5787** | STOCKS, SHARES, EQUITY, OPTIONS                                   | CORRECT GROUP (COMPANY OWNERSHIP OFFERS, Level 1)
   - Group 16: **0.5034** | FOLLOWERS, LIKES, INSULTS, SHOVELS                                | INCORRECT (Max overlap: 3/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 17: **0.4925** | BUFFALO, SHEEP, PUPPETS, LEMMINGS                                 | INCORRECT (Max overlap: 3/4 with CONFORMISTS)
   - Group 18: **0.4968** | FOLLOWERS, INSULTS, SHOVELS, OPTIONS                              | INCORRECT (Max overlap: 2/4 with WHAT “DIGS” MIGHT MEAN)
   - Group 19: **0.4916** | FOLLOWERS, BILLINGS, APARTMENT, PHOENIX                           | INCORRECT (Max overlap: 2/4 with U.S. CITIES) | [Pred Type: NAMED_ENTITY_SET (47.3%, no-rel 21.9%)]
   - Group 20: **0.4898** | BUFFALO, MOBILE, SHEEP, LEMMINGS                                  | INCORRECT (Max overlap: 2/4 with U.S. CITIES)

---

## Puzzle 24 (ID: 953)
**Words on Board:** BROOKLYN, KILLER, WEAVE, GOLDEN GATE, RIALTO, CARPENTER, CRAVEN, WANTON, TWIST, NEEDLE, DESIREE, BUMBLE, TOWER, HONEY, WIND, LACE

### Ground Truth Categories:
* **Level 0 (INTERTWINE) [Type: SYNONYM_OR_NEAR]:** LACE, TWIST, WEAVE, WIND
* **Level 1 (KINDS OF BEES) [Type: NAMED_ENTITY_SET]:** BUMBLE, CARPENTER, HONEY, KILLER
* **Level 2 (FAMOUS BRIDGES) [Type: NAMED_ENTITY_SET]:** BROOKLYN, GOLDEN GATE, RIALTO, TOWER
* **Level 3 (STARTING WITH SYNONYMS FOR "HANKER FOR") [Type: WORDPLAY_TRANSFORM]:** CRAVEN, DESIREE, NEEDLE, WANTON

### Top Candidate Partitions:
1. **Partition Score: 0.5394**
   - Group 1: **0.6411** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 26.3%)]
   - Group 2: **0.5389** | KILLER, CARPENTER, NEEDLE, TOWER                                  | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 3: **0.5233** | CRAVEN, WANTON, BUMBLE, HONEY                                     | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 4: **0.5232** | BROOKLYN, GOLDEN GATE, RIALTO, DESIREE                            | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES) | [Pred Type: NAMED_ENTITY_SET (45.2%, no-rel 21.2%)]
2. **Partition Score: 0.5301**
   - Group 1: **0.6411** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 26.3%)]
   - Group 2: **0.5862** | KILLER, CARPENTER, NEEDLE, HONEY                                  | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 3: **0.5231** | CRAVEN, WANTON, DESIREE, BUMBLE                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 4: **0.4877** | BROOKLYN, GOLDEN GATE, RIALTO, TOWER                              | CORRECT GROUP (FAMOUS BRIDGES, Level 2)
3. **Partition Score: 0.5207**
   - Group 1: **0.6411** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 26.3%)]
   - Group 2: **0.5372** | KILLER, NEEDLE, TOWER, HONEY                                      | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 3: **0.5232** | BROOKLYN, GOLDEN GATE, RIALTO, DESIREE                            | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES) | [Pred Type: NAMED_ENTITY_SET (45.2%, no-rel 21.2%)]
   - Group 4: **0.4873** | CARPENTER, CRAVEN, WANTON, BUMBLE                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
4. **Partition Score: 0.5167**
   - Group 1: **0.6411** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 26.3%)]
   - Group 2: **0.5233** | CRAVEN, WANTON, BUMBLE, HONEY                                     | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 3: **0.5145** | KILLER, CARPENTER, NEEDLE, DESIREE                                | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 4: **0.4877** | BROOKLYN, GOLDEN GATE, RIALTO, TOWER                              | CORRECT GROUP (FAMOUS BRIDGES, Level 2)
5. **Partition Score: 0.5151**
   - Group 1: **0.6411** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 26.3%)]
   - Group 2: **0.5233** | CRAVEN, WANTON, DESIREE, HONEY                                    | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 3: **0.5061** | KILLER, CARPENTER, NEEDLE, BUMBLE                                 | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 4: **0.4877** | BROOKLYN, GOLDEN GATE, RIALTO, TOWER                              | CORRECT GROUP (FAMOUS BRIDGES, Level 2)

### Top Candidate Groups:
   - Group 1: **0.6411** | WEAVE, TWIST, WIND, LACE                                          | CORRECT GROUP (INTERTWINE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 26.3%)]
   - Group 2: **0.5389** | KILLER, CARPENTER, NEEDLE, TOWER                                  | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 3: **0.5233** | CRAVEN, WANTON, BUMBLE, HONEY                                     | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 4: **0.5232** | BROOKLYN, GOLDEN GATE, RIALTO, DESIREE                            | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES) | [Pred Type: NAMED_ENTITY_SET (45.2%, no-rel 21.2%)]
   - Group 5: **0.5862** | KILLER, CARPENTER, NEEDLE, HONEY                                  | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 6: **0.5231** | CRAVEN, WANTON, DESIREE, BUMBLE                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 7: **0.4877** | BROOKLYN, GOLDEN GATE, RIALTO, TOWER                              | CORRECT GROUP (FAMOUS BRIDGES, Level 2)
   - Group 8: **0.5372** | KILLER, NEEDLE, TOWER, HONEY                                      | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 9: **0.4873** | CARPENTER, CRAVEN, WANTON, BUMBLE                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 10: **0.5145** | KILLER, CARPENTER, NEEDLE, DESIREE                                | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 11: **0.5233** | CRAVEN, WANTON, DESIREE, HONEY                                    | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 12: **0.5061** | KILLER, CARPENTER, NEEDLE, BUMBLE                                 | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 13: **0.6249** | KILLER, CARPENTER, BUMBLE, HONEY                                  | CORRECT GROUP (KINDS OF BEES, Level 1)
   - Group 14: **0.4555** | CRAVEN, WANTON, NEEDLE, DESIREE                                   | CORRECT GROUP (STARTING WITH SYNONYMS FOR "HANKER FOR", Level 3)
   - Group 15: **0.5142** | KILLER, CARPENTER, CRAVEN, NEEDLE                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 16: **0.5090** | WANTON, DESIREE, BUMBLE, HONEY                                    | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 17: **0.5272** | KILLER, NEEDLE, BUMBLE, HONEY                                     | INCORRECT (Max overlap: 3/4 with KINDS OF BEES)
   - Group 18: **0.4914** | CARPENTER, CRAVEN, WANTON, DESIREE                                | INCORRECT (Max overlap: 3/4 with STARTING WITH SYNONYMS FOR "HANKER FOR")
   - Group 19: **0.5315** | KILLER, NEEDLE, DESIREE, HONEY                                    | INCORRECT (Max overlap: 2/4 with KINDS OF BEES)
   - Group 20: **0.4712** | BROOKLYN, GOLDEN GATE, RIALTO, CARPENTER                          | INCORRECT (Max overlap: 3/4 with FAMOUS BRIDGES)

---

## Puzzle 25 (ID: 71)
**Words on Board:** MUG, SOPRANO, MONTANA, SPRITE, SQUIRT, COLORADO, YES, STARK, UTAH, NEVADA, CRUSH, ARIZONA, HAWK, KANSAS, GENESIS, RUSH

### Ground Truth Categories:
* **Level 0 (U.S. MOUNTAIN STATES) [Type: NAMED_ENTITY_SET]:** ARIZONA, COLORADO, NEVADA, UTAH
* **Level 1 (SODA BRANDS) [Type: NAMED_ENTITY_SET]:** CRUSH, MUG, SPRITE, SQUIRT
* **Level 2 (CLASSIC ROCK BANDS) [Type: NAMED_ENTITY_SET]:** GENESIS, KANSAS, RUSH, YES
* **Level 3 (TONY ___) [Type: FILL_IN_THE_BLANK]:** HAWK, MONTANA, SOPRANO, STARK

### Top Candidate Partitions:
1. **Partition Score: 0.5168**
   - Group 1: **0.8035** | COLORADO, UTAH, NEVADA, KANSAS                                    | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 2: **0.4865** | MUG, SPRITE, SQUIRT, YES                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 3: **0.4838** | SOPRANO, MONTANA, ARIZONA, GENESIS                                | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (54.7%, no-rel 18.3%)]
   - Group 4: **0.4770** | STARK, CRUSH, HAWK, RUSH                                          | INCORRECT (Max overlap: 2/4 with TONY ___)
2. **Partition Score: 0.5165**
   - Group 1: **0.8275** | MONTANA, COLORADO, UTAH, KANSAS                                   | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 2: **0.4865** | MUG, SPRITE, SQUIRT, YES                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 3: **0.4770** | STARK, CRUSH, HAWK, RUSH                                          | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 4: **0.4736** | SOPRANO, NEVADA, ARIZONA, GENESIS                                 | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (54.8%, no-rel 17.5%)]
3. **Partition Score: 0.5163**
   - Group 1: **0.8035** | COLORADO, UTAH, NEVADA, KANSAS                                    | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 2: **0.5226** | SQUIRT, STARK, CRUSH, RUSH                                        | INCORRECT (Max overlap: 2/4 with SODA BRANDS)
   - Group 3: **0.4838** | SOPRANO, MONTANA, ARIZONA, GENESIS                                | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (54.7%, no-rel 18.3%)]
   - Group 4: **0.4628** | MUG, SPRITE, YES, HAWK                                            | INCORRECT (Max overlap: 2/4 with SODA BRANDS) | [Pred Type: NAMED_ENTITY_SET (46.1%, no-rel 20.2%)]
4. **Partition Score: 0.5162**
   - Group 1: **0.8043** | COLORADO, UTAH, ARIZONA, KANSAS                                   | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 2: **0.4865** | MUG, SPRITE, SQUIRT, YES                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 3: **0.4803** | SOPRANO, MONTANA, NEVADA, GENESIS                                 | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (50.4%, no-rel 20.1%)]
   - Group 4: **0.4770** | STARK, CRUSH, HAWK, RUSH                                          | INCORRECT (Max overlap: 2/4 with TONY ___)
5. **Partition Score: 0.5158**
   - Group 1: **0.8349** | MONTANA, COLORADO, NEVADA, ARIZONA                                | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 2: **0.5357** | MUG, SQUIRT, CRUSH, RUSH                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 3: **0.4733** | SOPRANO, SPRITE, STARK, HAWK                                      | INCORRECT (Max overlap: 3/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (49.3%, no-rel 16.0%)]
   - Group 4: **0.4540** | YES, UTAH, KANSAS, GENESIS                                        | INCORRECT (Max overlap: 3/4 with CLASSIC ROCK BANDS) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 17.5%)]

### Top Candidate Groups:
   - Group 1: **0.8035** | COLORADO, UTAH, NEVADA, KANSAS                                    | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 2: **0.4865** | MUG, SPRITE, SQUIRT, YES                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 3: **0.4838** | SOPRANO, MONTANA, ARIZONA, GENESIS                                | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (54.7%, no-rel 18.3%)]
   - Group 4: **0.4770** | STARK, CRUSH, HAWK, RUSH                                          | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 5: **0.8275** | MONTANA, COLORADO, UTAH, KANSAS                                   | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES)
   - Group 6: **0.4736** | SOPRANO, NEVADA, ARIZONA, GENESIS                                 | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (54.8%, no-rel 17.5%)]
   - Group 7: **0.5226** | SQUIRT, STARK, CRUSH, RUSH                                        | INCORRECT (Max overlap: 2/4 with SODA BRANDS)
   - Group 8: **0.4628** | MUG, SPRITE, YES, HAWK                                            | INCORRECT (Max overlap: 2/4 with SODA BRANDS) | [Pred Type: NAMED_ENTITY_SET (46.1%, no-rel 20.2%)]
   - Group 9: **0.8043** | COLORADO, UTAH, ARIZONA, KANSAS                                   | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 10: **0.4803** | SOPRANO, MONTANA, NEVADA, GENESIS                                 | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (50.4%, no-rel 20.1%)]
   - Group 11: **0.8349** | MONTANA, COLORADO, NEVADA, ARIZONA                                | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 12: **0.5357** | MUG, SQUIRT, CRUSH, RUSH                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 13: **0.4733** | SOPRANO, SPRITE, STARK, HAWK                                      | INCORRECT (Max overlap: 3/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (49.3%, no-rel 16.0%)]
   - Group 14: **0.4540** | YES, UTAH, KANSAS, GENESIS                                        | INCORRECT (Max overlap: 3/4 with CLASSIC ROCK BANDS) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 17.5%)]
   - Group 15: **0.8052** | COLORADO, UTAH, NEVADA, ARIZONA                                   | CORRECT GROUP (U.S. MOUNTAIN STATES, Level 0)
   - Group 16: **0.4596** | MONTANA, YES, KANSAS, GENESIS                                     | INCORRECT (Max overlap: 3/4 with CLASSIC ROCK BANDS) | [Pred Type: NAMED_ENTITY_SET (47.3%, no-rel 20.1%)]
   - Group 17: **0.8167** | MONTANA, COLORADO, UTAH, NEVADA                                   | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 18: **0.4733** | SOPRANO, ARIZONA, KANSAS, GENESIS                                 | INCORRECT (Max overlap: 2/4 with CLASSIC ROCK BANDS) | [Pred Type: NAMED_ENTITY_SET (54.6%, no-rel 18.3%)]
   - Group 19: **0.4584** | SOPRANO, SPRITE, YES, GENESIS                                     | INCORRECT (Max overlap: 2/4 with CLASSIC ROCK BANDS)
   - Group 20: **0.4563** | STARK, UTAH, HAWK, KANSAS                                         | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (45.3%, no-rel 19.3%)]

---

## Puzzle 26 (ID: 563)
**Words on Board:** JENNY, RUDOLPH, ROBIN HOOD, FEY, STRONG, CUPID, VIXEN, SAGITTARIUS, STAR, SHANNON, HAWKEYE, MOON, PLANET, COMET, QUEEN, NANNY

### Ground Truth Categories:
* **Level 0 (CELESTIAL OBJECTS) [Type: SEMANTIC_SET]:** COMET, MOON, PLANET, STAR
* **Level 1 (ARCHERS) [Type: NAMED_ENTITY_SET]:** CUPID, HAWKEYE, ROBIN HOOD, SAGITTARIUS
* **Level 2 (FEMALE ANIMALS) [Type: SEMANTIC_SET]:** JENNY, NANNY, QUEEN, VIXEN
* **Level 3 (“S.N.L.” CAST MEMBERS) [Type: NAMED_ENTITY_SET]:** FEY, RUDOLPH, SHANNON, STRONG

### Top Candidate Partitions:
1. **Partition Score: 0.4881**
   - Group 1: **0.7053** | STAR, MOON, PLANET, COMET                                         | CORRECT GROUP (CELESTIAL OBJECTS, Level 0)
   - Group 2: **0.5206** | JENNY, SHANNON, QUEEN, NANNY                                      | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (46.9%, no-rel 25.1%)]
   - Group 3: **0.4576** | RUDOLPH, ROBIN HOOD, CUPID, HAWKEYE                               | INCORRECT (Max overlap: 3/4 with ARCHERS) | [Pred Type: NAMED_ENTITY_SET (57.4%, no-rel 16.7%)]
   - Group 4: **0.4397** | FEY, STRONG, VIXEN, SAGITTARIUS                                   | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (56.7%, no-rel 14.8%)]
2. **Partition Score: 0.4880**
   - Group 1: **0.7053** | STAR, MOON, PLANET, COMET                                         | CORRECT GROUP (CELESTIAL OBJECTS, Level 0)
   - Group 2: **0.4669** | STRONG, SAGITTARIUS, SHANNON, QUEEN                               | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (56.9%, no-rel 17.1%)]
   - Group 3: **0.4619** | JENNY, FEY, VIXEN, NANNY                                          | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (50.7%, no-rel 21.0%)]
   - Group 4: **0.4576** | RUDOLPH, ROBIN HOOD, CUPID, HAWKEYE                               | INCORRECT (Max overlap: 3/4 with ARCHERS) | [Pred Type: NAMED_ENTITY_SET (57.4%, no-rel 16.7%)]
3. **Partition Score: 0.4850**
   - Group 1: **0.7053** | STAR, MOON, PLANET, COMET                                         | CORRECT GROUP (CELESTIAL OBJECTS, Level 0)
   - Group 2: **0.4894** | FEY, STRONG, VIXEN, QUEEN                                         | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (58.9%, no-rel 15.7%)]
   - Group 3: **0.4509** | JENNY, RUDOLPH, SHANNON, NANNY                                    | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (46.0%, no-rel 25.8%)]
   - Group 4: **0.4474** | ROBIN HOOD, CUPID, SAGITTARIUS, HAWKEYE                           | CORRECT GROUP (ARCHERS, Level 1) | [Pred Type: NAMED_ENTITY_SET (59.8%, no-rel 14.7%)]
4. **Partition Score: 0.4817**
   - Group 1: **0.7053** | STAR, MOON, PLANET, COMET                                         | CORRECT GROUP (CELESTIAL OBJECTS, Level 0)
   - Group 2: **0.4815** | JENNY, FEY, SHANNON, NANNY                                        | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (48.9%, no-rel 22.7%)]
   - Group 3: **0.4576** | RUDOLPH, ROBIN HOOD, CUPID, HAWKEYE                               | INCORRECT (Max overlap: 3/4 with ARCHERS) | [Pred Type: NAMED_ENTITY_SET (57.4%, no-rel 16.7%)]
   - Group 4: **0.4415** | STRONG, VIXEN, SAGITTARIUS, QUEEN                                 | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (59.4%, no-rel 15.4%)]
5. **Partition Score: 0.4814**
   - Group 1: **0.7053** | STAR, MOON, PLANET, COMET                                         | CORRECT GROUP (CELESTIAL OBJECTS, Level 0)
   - Group 2: **0.4716** | JENNY, VIXEN, QUEEN, NANNY                                        | CORRECT GROUP (FEMALE ANIMALS, Level 2) | [Pred Type: NAMED_ENTITY_SET (50.0%, no-rel 21.0%)]
   - Group 3: **0.4499** | RUDOLPH, FEY, STRONG, SHANNON                                     | CORRECT GROUP (“S.N.L.” CAST MEMBERS, Level 3) | [Pred Type: NAMED_ENTITY_SET (52.4%, no-rel 19.3%)]
   - Group 4: **0.4474** | ROBIN HOOD, CUPID, SAGITTARIUS, HAWKEYE                           | CORRECT GROUP (ARCHERS, Level 1) | [Pred Type: NAMED_ENTITY_SET (59.8%, no-rel 14.7%)]

### Top Candidate Groups:
   - Group 1: **0.7053** | STAR, MOON, PLANET, COMET                                         | CORRECT GROUP (CELESTIAL OBJECTS, Level 0)
   - Group 2: **0.5206** | JENNY, SHANNON, QUEEN, NANNY                                      | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (46.9%, no-rel 25.1%)]
   - Group 3: **0.4576** | RUDOLPH, ROBIN HOOD, CUPID, HAWKEYE                               | INCORRECT (Max overlap: 3/4 with ARCHERS) | [Pred Type: NAMED_ENTITY_SET (57.4%, no-rel 16.7%)]
   - Group 4: **0.4397** | FEY, STRONG, VIXEN, SAGITTARIUS                                   | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (56.7%, no-rel 14.8%)]
   - Group 5: **0.4669** | STRONG, SAGITTARIUS, SHANNON, QUEEN                               | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (56.9%, no-rel 17.1%)]
   - Group 6: **0.4619** | JENNY, FEY, VIXEN, NANNY                                          | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (50.7%, no-rel 21.0%)]
   - Group 7: **0.4894** | FEY, STRONG, VIXEN, QUEEN                                         | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (58.9%, no-rel 15.7%)]
   - Group 8: **0.4509** | JENNY, RUDOLPH, SHANNON, NANNY                                    | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (46.0%, no-rel 25.8%)]
   - Group 9: **0.4474** | ROBIN HOOD, CUPID, SAGITTARIUS, HAWKEYE                           | CORRECT GROUP (ARCHERS, Level 1) | [Pred Type: NAMED_ENTITY_SET (59.8%, no-rel 14.7%)]
   - Group 10: **0.4815** | JENNY, FEY, SHANNON, NANNY                                        | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (48.9%, no-rel 22.7%)]
   - Group 11: **0.4415** | STRONG, VIXEN, SAGITTARIUS, QUEEN                                 | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (59.4%, no-rel 15.4%)]
   - Group 12: **0.4716** | JENNY, VIXEN, QUEEN, NANNY                                        | CORRECT GROUP (FEMALE ANIMALS, Level 2) | [Pred Type: NAMED_ENTITY_SET (50.0%, no-rel 21.0%)]
   - Group 13: **0.4499** | RUDOLPH, FEY, STRONG, SHANNON                                     | CORRECT GROUP (“S.N.L.” CAST MEMBERS, Level 3) | [Pred Type: NAMED_ENTITY_SET (52.4%, no-rel 19.3%)]
   - Group 14: **0.4445** | FEY, STRONG, SAGITTARIUS, SHANNON                                 | INCORRECT (Max overlap: 3/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (54.7%, no-rel 17.1%)]
   - Group 15: **0.4676** | RUDOLPH, ROBIN HOOD, SHANNON, HAWKEYE                             | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (49.9%, no-rel 23.0%)]
   - Group 16: **0.4438** | STRONG, CUPID, SAGITTARIUS, QUEEN                                 | INCORRECT (Max overlap: 2/4 with ARCHERS) | [Pred Type: NAMED_ENTITY_SET (58.1%, no-rel 15.8%)]
   - Group 17: **0.4716** | JENNY, CUPID, QUEEN, NANNY                                        | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (49.3%, no-rel 20.6%)]
   - Group 18: **0.4761** | JENNY, VIXEN, SHANNON, NANNY                                      | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (49.0%, no-rel 22.7%)]
   - Group 19: **0.4411** | FEY, STRONG, SAGITTARIUS, QUEEN                                   | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (58.0%, no-rel 15.4%)]
   - Group 20: **0.4495** | ROBIN HOOD, CUPID, SAGITTARIUS, QUEEN                             | INCORRECT (Max overlap: 3/4 with ARCHERS) | [Pred Type: NAMED_ENTITY_SET (59.0%, no-rel 15.5%)]

---

## Puzzle 27 (ID: 17)
**Words on Board:** STARBOARD, GAIN, LOVE, ERA, TIE, STERN, ASCOT, BOLO, TIDE, ALL, SCARF, RIGHT, PORT, BOW, ACUTE, BERMUDA

### Ground Truth Categories:
* **Level 0 (NECKWEAR) [Type: SEMANTIC_SET]:** ASCOT, BOLO, SCARF, TIE
* **Level 1 (SHIP DIRECTIONS) [Type: SEMANTIC_SET]:** BOW, PORT, STARBOARD, STERN
* **Level 2 (DETERGENTS) [Type: NAMED_ENTITY_SET]:** ALL, ERA, GAIN, TIDE
* **Level 3 (___ TRIANGLE) [Type: FILL_IN_THE_BLANK]:** ACUTE, BERMUDA, LOVE, RIGHT

### Top Candidate Partitions:
1. **Partition Score: 0.4664**
   - Group 1: **0.5306** | STARBOARD, STERN, PORT, BOW                                       | CORRECT GROUP (SHIP DIRECTIONS, Level 1)
   - Group 2: **0.5118** | TIE, ASCOT, BOLO, SCARF                                           | CORRECT GROUP (NECKWEAR, Level 0)
   - Group 3: **0.4495** | GAIN, LOVE, ALL, RIGHT                                            | INCORRECT (Max overlap: 2/4 with DETERGENTS)
   - Group 4: **0.4418** | ERA, TIDE, ACUTE, BERMUDA                                         | INCORRECT (Max overlap: 2/4 with DETERGENTS) | [Pred Type: NAMED_ENTITY_SET (47.8%, no-rel 14.3%)]
2. **Partition Score: 0.4603**
   - Group 1: **0.5118** | TIE, ASCOT, BOLO, SCARF                                           | CORRECT GROUP (NECKWEAR, Level 0)
   - Group 2: **0.4738** | LOVE, ALL, RIGHT, BOW                                             | INCORRECT (Max overlap: 2/4 with ___ TRIANGLE)
   - Group 3: **0.4666** | STARBOARD, GAIN, STERN, PORT                                      | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS) | [Pred Type: SYNONYM_OR_NEAR (45.3%, no-rel 32.3%)]
   - Group 4: **0.4418** | ERA, TIDE, ACUTE, BERMUDA                                         | INCORRECT (Max overlap: 2/4 with DETERGENTS) | [Pred Type: NAMED_ENTITY_SET (47.8%, no-rel 14.3%)]
3. **Partition Score: 0.4534**
   - Group 1: **0.5632** | STARBOARD, STERN, RIGHT, PORT                                     | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 34.7%)]
   - Group 2: **0.5118** | TIE, ASCOT, BOLO, SCARF                                           | CORRECT GROUP (NECKWEAR, Level 0)
   - Group 3: **0.4418** | ERA, TIDE, ACUTE, BERMUDA                                         | INCORRECT (Max overlap: 2/4 with DETERGENTS) | [Pred Type: NAMED_ENTITY_SET (47.8%, no-rel 14.3%)]
   - Group 4: **0.4121** | GAIN, LOVE, ALL, BOW                                              | INCORRECT (Max overlap: 2/4 with DETERGENTS)
4. **Partition Score: 0.4468**
   - Group 1: **0.4576** | STARBOARD, STERN, PORT, ACUTE                                     | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS)
   - Group 2: **0.4553** | TIE, BOLO, SCARF, BOW                                             | INCORRECT (Max overlap: 3/4 with NECKWEAR)
   - Group 3: **0.4495** | GAIN, LOVE, ALL, RIGHT                                            | INCORRECT (Max overlap: 2/4 with DETERGENTS)
   - Group 4: **0.4403** | ERA, ASCOT, TIDE, BERMUDA                                         | INCORRECT (Max overlap: 2/4 with DETERGENTS) | [Pred Type: NAMED_ENTITY_SET (49.7%, no-rel 12.6%)]
5. **Partition Score: 0.4466**
   - Group 1: **0.5005** | STARBOARD, STERN, TIDE, PORT                                      | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS)
   - Group 2: **0.4553** | TIE, BOLO, SCARF, BOW                                             | INCORRECT (Max overlap: 3/4 with NECKWEAR)
   - Group 3: **0.4495** | GAIN, LOVE, ALL, RIGHT                                            | INCORRECT (Max overlap: 2/4 with DETERGENTS)
   - Group 4: **0.4305** | ERA, ASCOT, ACUTE, BERMUDA                                        | INCORRECT (Max overlap: 2/4 with ___ TRIANGLE)

### Top Candidate Groups:
   - Group 1: **0.5306** | STARBOARD, STERN, PORT, BOW                                       | CORRECT GROUP (SHIP DIRECTIONS, Level 1)
   - Group 2: **0.5118** | TIE, ASCOT, BOLO, SCARF                                           | CORRECT GROUP (NECKWEAR, Level 0)
   - Group 3: **0.4495** | GAIN, LOVE, ALL, RIGHT                                            | INCORRECT (Max overlap: 2/4 with DETERGENTS)
   - Group 4: **0.4418** | ERA, TIDE, ACUTE, BERMUDA                                         | INCORRECT (Max overlap: 2/4 with DETERGENTS) | [Pred Type: NAMED_ENTITY_SET (47.8%, no-rel 14.3%)]
   - Group 5: **0.4738** | LOVE, ALL, RIGHT, BOW                                             | INCORRECT (Max overlap: 2/4 with ___ TRIANGLE)
   - Group 6: **0.4666** | STARBOARD, GAIN, STERN, PORT                                      | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS) | [Pred Type: SYNONYM_OR_NEAR (45.3%, no-rel 32.3%)]
   - Group 7: **0.5632** | STARBOARD, STERN, RIGHT, PORT                                     | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 34.7%)]
   - Group 8: **0.4121** | GAIN, LOVE, ALL, BOW                                              | INCORRECT (Max overlap: 2/4 with DETERGENTS)
   - Group 9: **0.4576** | STARBOARD, STERN, PORT, ACUTE                                     | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS)
   - Group 10: **0.4553** | TIE, BOLO, SCARF, BOW                                             | INCORRECT (Max overlap: 3/4 with NECKWEAR)
   - Group 11: **0.4403** | ERA, ASCOT, TIDE, BERMUDA                                         | INCORRECT (Max overlap: 2/4 with DETERGENTS) | [Pred Type: NAMED_ENTITY_SET (49.7%, no-rel 12.6%)]
   - Group 12: **0.5005** | STARBOARD, STERN, TIDE, PORT                                      | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS)
   - Group 13: **0.4305** | ERA, ASCOT, ACUTE, BERMUDA                                        | INCORRECT (Max overlap: 2/4 with ___ TRIANGLE)
   - Group 14: **0.5475** | STARBOARD, STERN, RIGHT, BOW                                      | INCORRECT (Max overlap: 3/4 with SHIP DIRECTIONS) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 31.7%)]
   - Group 15: **0.4017** | GAIN, LOVE, ALL, PORT                                             | INCORRECT (Max overlap: 2/4 with DETERGENTS)
   - Group 16: **0.4828** | STARBOARD, GAIN, STERN, RIGHT                                     | INCORRECT (Max overlap: 2/4 with SHIP DIRECTIONS) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 30.5%)]
   - Group 17: **0.4134** | LOVE, ALL, PORT, BOW                                              | INCORRECT (Max overlap: 2/4 with SHIP DIRECTIONS)
   - Group 18: **0.4619** | STARBOARD, TIE, SCARF, BOW                                        | INCORRECT (Max overlap: 2/4 with SHIP DIRECTIONS)
   - Group 19: **0.4347** | ERA, ASCOT, BOLO, BERMUDA                                         | INCORRECT (Max overlap: 2/4 with NECKWEAR)
   - Group 20: **0.4344** | STERN, TIDE, PORT, ACUTE                                          | INCORRECT (Max overlap: 2/4 with SHIP DIRECTIONS)

---

## Puzzle 28 (ID: 260)
**Words on Board:** ROMANTIC, TYPE, CONFRONT, SOUR, KIND, VARIETY, MANNER, BRAVE, BITTER, SWEET, MEET, EXPRESSION, SORT, SURREAL, SALTY, FACE

### Ground Truth Categories:
* **Level 0 (BASIC TASTES) [Type: SEMANTIC_SET]:** BITTER, SALTY, SOUR, SWEET
* **Level 1 (STAND UP TO, AS A CHALLENGE) [Type: SYNONYM_OR_NEAR]:** BRAVE, CONFRONT, FACE, MEET
* **Level 2 (ILK) [Type: SYNONYM_OR_NEAR]:** KIND, SORT, TYPE, VARIETY
* **Level 3 (ART MOVEMENTS, WITH -ISM) [Type: FILL_IN_THE_BLANK]:** EXPRESSION, MANNER, ROMANTIC, SURREAL

### Top Candidate Partitions:
1. **Partition Score: 0.5199**
   - Group 1: **0.8059** | TYPE, KIND, VARIETY, SORT                                         | CORRECT GROUP (ILK, Level 2) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 22.3%)]
   - Group 2: **0.6558** | SOUR, BITTER, SWEET, SALTY                                        | CORRECT GROUP (BASIC TASTES, Level 0)
   - Group 3: **0.5392** | CONFRONT, MEET, EXPRESSION, FACE                                  | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (65.2%, no-rel 27.3%)]
   - Group 4: **0.4004** | ROMANTIC, MANNER, BRAVE, SURREAL                                  | INCORRECT (Max overlap: 3/4 with ART MOVEMENTS, WITH -ISM)
2. **Partition Score: 0.5077**
   - Group 1: **0.8059** | TYPE, KIND, VARIETY, SORT                                         | CORRECT GROUP (ILK, Level 2) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 22.3%)]
   - Group 2: **0.6558** | SOUR, BITTER, SWEET, SALTY                                        | CORRECT GROUP (BASIC TASTES, Level 0)
   - Group 3: **0.4551** | CONFRONT, BRAVE, MEET, FACE                                       | CORRECT GROUP (STAND UP TO, AS A CHALLENGE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (71.2%, no-rel 17.2%)]
   - Group 4: **0.4072** | ROMANTIC, MANNER, EXPRESSION, SURREAL                             | CORRECT GROUP (ART MOVEMENTS, WITH -ISM, Level 3)
3. **Partition Score: 0.5041**
   - Group 1: **0.8059** | TYPE, KIND, VARIETY, SORT                                         | CORRECT GROUP (ILK, Level 2) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 22.3%)]
   - Group 2: **0.5597** | SOUR, BRAVE, BITTER, SWEET                                        | INCORRECT (Max overlap: 3/4 with BASIC TASTES)
   - Group 3: **0.5323** | CONFRONT, MEET, SALTY, FACE                                       | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (65.8%, no-rel 26.6%)]
   - Group 4: **0.4072** | ROMANTIC, MANNER, EXPRESSION, SURREAL                             | CORRECT GROUP (ART MOVEMENTS, WITH -ISM, Level 3)
4. **Partition Score: 0.4800**
   - Group 1: **0.8059** | TYPE, KIND, VARIETY, SORT                                         | CORRECT GROUP (ILK, Level 2) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 22.3%)]
   - Group 2: **0.4913** | CONFRONT, BITTER, MEET, FACE                                      | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (65.5%, no-rel 24.4%)]
   - Group 3: **0.4719** | SOUR, BRAVE, SWEET, SALTY                                         | INCORRECT (Max overlap: 3/4 with BASIC TASTES)
   - Group 4: **0.4072** | ROMANTIC, MANNER, EXPRESSION, SURREAL                             | CORRECT GROUP (ART MOVEMENTS, WITH -ISM, Level 3)
5. **Partition Score: 0.4794**
   - Group 1: **0.6558** | SOUR, BITTER, SWEET, SALTY                                        | CORRECT GROUP (BASIC TASTES, Level 0)
   - Group 2: **0.5392** | CONFRONT, MEET, EXPRESSION, FACE                                  | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (65.2%, no-rel 27.3%)]
   - Group 3: **0.5272** | TYPE, KIND, MANNER, SORT                                          | INCORRECT (Max overlap: 3/4 with ILK) | [Pred Type: SYNONYM_OR_NEAR (61.9%, no-rel 24.0%)]
   - Group 4: **0.4014** | ROMANTIC, VARIETY, BRAVE, SURREAL                                 | INCORRECT (Max overlap: 2/4 with ART MOVEMENTS, WITH -ISM)

### Top Candidate Groups:
   - Group 1: **0.8059** | TYPE, KIND, VARIETY, SORT                                         | CORRECT GROUP (ILK, Level 2) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 22.3%)]
   - Group 2: **0.6558** | SOUR, BITTER, SWEET, SALTY                                        | CORRECT GROUP (BASIC TASTES, Level 0)
   - Group 3: **0.5392** | CONFRONT, MEET, EXPRESSION, FACE                                  | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (65.2%, no-rel 27.3%)]
   - Group 4: **0.4004** | ROMANTIC, MANNER, BRAVE, SURREAL                                  | INCORRECT (Max overlap: 3/4 with ART MOVEMENTS, WITH -ISM)
   - Group 5: **0.4551** | CONFRONT, BRAVE, MEET, FACE                                       | CORRECT GROUP (STAND UP TO, AS A CHALLENGE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (71.2%, no-rel 17.2%)]
   - Group 6: **0.4072** | ROMANTIC, MANNER, EXPRESSION, SURREAL                             | CORRECT GROUP (ART MOVEMENTS, WITH -ISM, Level 3)
   - Group 7: **0.5597** | SOUR, BRAVE, BITTER, SWEET                                        | INCORRECT (Max overlap: 3/4 with BASIC TASTES)
   - Group 8: **0.5323** | CONFRONT, MEET, SALTY, FACE                                       | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (65.8%, no-rel 26.6%)]
   - Group 9: **0.4913** | CONFRONT, BITTER, MEET, FACE                                      | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (65.5%, no-rel 24.4%)]
   - Group 10: **0.4719** | SOUR, BRAVE, SWEET, SALTY                                         | INCORRECT (Max overlap: 3/4 with BASIC TASTES)
   - Group 11: **0.5272** | TYPE, KIND, MANNER, SORT                                          | INCORRECT (Max overlap: 3/4 with ILK) | [Pred Type: SYNONYM_OR_NEAR (61.9%, no-rel 24.0%)]
   - Group 12: **0.4014** | ROMANTIC, VARIETY, BRAVE, SURREAL                                 | INCORRECT (Max overlap: 2/4 with ART MOVEMENTS, WITH -ISM)
   - Group 13: **0.4905** | BRAVE, BITTER, SWEET, SALTY                                       | INCORRECT (Max overlap: 3/4 with BASIC TASTES)
   - Group 14: **0.4696** | CONFRONT, SOUR, MEET, FACE                                        | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 25.4%)]
   - Group 15: **0.4882** | SOUR, BITTER, SWEET, MEET                                         | INCORRECT (Max overlap: 3/4 with BASIC TASTES)
   - Group 16: **0.4572** | CONFRONT, EXPRESSION, SALTY, FACE                                 | INCORRECT (Max overlap: 2/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 30.8%)]
   - Group 17: **0.4199** | ROMANTIC, BRAVE, SURREAL, SALTY                                   | INCORRECT (Max overlap: 2/4 with ART MOVEMENTS, WITH -ISM)
   - Group 18: **0.4131** | CONFRONT, MANNER, EXPRESSION, FACE                                | INCORRECT (Max overlap: 2/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (61.0%, no-rel 26.7%)]
   - Group 19: **0.4841** | SOUR, BRAVE, BITTER, SALTY                                        | INCORRECT (Max overlap: 3/4 with BASIC TASTES)
   - Group 20: **0.4261** | CONFRONT, SWEET, MEET, FACE                                       | INCORRECT (Max overlap: 3/4 with STAND UP TO, AS A CHALLENGE) | [Pred Type: SYNONYM_OR_NEAR (66.7%, no-rel 23.8%)]

---

## Puzzle 29 (ID: 868)
**Words on Board:** KITCHENETTE, TALENT, BEE, DROPLET, FLOAT, STARING, POPULARITY, STING, WIND, PERCUSSION, BRASS, STARLING, BEAUTY, BUTTERFLY, STRING, DOGGY

### Ground Truth Categories:
* **Level 0 (KINDS OF INSTRUMENTS) [Type: SEMANTIC_SET]:** BRASS, PERCUSSION, STRING, WIND
* **Level 1 (WORDS IN A FAMOUS MUHAMMAD ALI QUOTE) [Type: COMMON_PHRASE]:** BEE, BUTTERFLY, FLOAT, STING
* **Level 2 (KINDS OF CONTESTS) [Type: FILL_IN_THE_BLANK]:** BEAUTY, POPULARITY, STARING, TALENT
* **Level 3 (WORDS WITH DIMINUTIVE SUFFIXES) [Type: WORD_FORM]:** DOGGY, DROPLET, KITCHENETTE, STARLING

### Top Candidate Partitions:
1. **Partition Score: 0.4002**
   - Group 1: **0.5047** | KITCHENETTE, DROPLET, STARLING, DOGGY                             | CORRECT GROUP (WORDS WITH DIMINUTIVE SUFFIXES, Level 3)
   - Group 2: **0.4267** | TALENT, STARING, POPULARITY, BEAUTY                               | CORRECT GROUP (KINDS OF CONTESTS, Level 2)
   - Group 3: **0.3859** | FLOAT, WIND, PERCUSSION, BRASS                                    | INCORRECT (Max overlap: 3/4 with KINDS OF INSTRUMENTS)
   - Group 4: **0.3729** | BEE, STING, BUTTERFLY, STRING                                     | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS MUHAMMAD ALI QUOTE)
2. **Partition Score: 0.3922**
   - Group 1: **0.4636** | KITCHENETTE, STARLING, BUTTERFLY, DOGGY                           | INCORRECT (Max overlap: 3/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 2: **0.4267** | TALENT, STARING, POPULARITY, BEAUTY                               | CORRECT GROUP (KINDS OF CONTESTS, Level 2)
   - Group 3: **0.4115** | DROPLET, PERCUSSION, BRASS, STRING                                | INCORRECT (Max overlap: 3/4 with KINDS OF INSTRUMENTS)
   - Group 4: **0.3569** | BEE, FLOAT, STING, WIND                                           | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS MUHAMMAD ALI QUOTE)
3. **Partition Score: 0.3917**
   - Group 1: **0.4520** | TALENT, STARING, POPULARITY, STARLING                             | INCORRECT (Max overlap: 3/4 with KINDS OF CONTESTS)
   - Group 2: **0.4307** | KITCHENETTE, BEAUTY, BUTTERFLY, DOGGY                             | INCORRECT (Max overlap: 2/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 3: **0.4115** | DROPLET, PERCUSSION, BRASS, STRING                                | INCORRECT (Max overlap: 3/4 with KINDS OF INSTRUMENTS)
   - Group 4: **0.3569** | BEE, FLOAT, STING, WIND                                           | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS MUHAMMAD ALI QUOTE)
4. **Partition Score: 0.3915**
   - Group 1: **0.4395** | DROPLET, STARING, POPULARITY, STARLING                            | INCORRECT (Max overlap: 2/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 2: **0.4190** | KITCHENETTE, TALENT, BEAUTY, DOGGY                                | INCORRECT (Max overlap: 2/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 3: **0.3859** | FLOAT, WIND, PERCUSSION, BRASS                                    | INCORRECT (Max overlap: 3/4 with KINDS OF INSTRUMENTS)
   - Group 4: **0.3729** | BEE, STING, BUTTERFLY, STRING                                     | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS MUHAMMAD ALI QUOTE)
5. **Partition Score: 0.3913**
   - Group 1: **0.4311** | TALENT, DROPLET, STARING, POPULARITY                              | INCORRECT (Max overlap: 3/4 with KINDS OF CONTESTS)
   - Group 2: **0.4230** | KITCHENETTE, STARLING, BEAUTY, DOGGY                              | INCORRECT (Max overlap: 3/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 3: **0.3859** | FLOAT, WIND, PERCUSSION, BRASS                                    | INCORRECT (Max overlap: 3/4 with KINDS OF INSTRUMENTS)
   - Group 4: **0.3729** | BEE, STING, BUTTERFLY, STRING                                     | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS MUHAMMAD ALI QUOTE)

### Top Candidate Groups:
   - Group 1: **0.5047** | KITCHENETTE, DROPLET, STARLING, DOGGY                             | CORRECT GROUP (WORDS WITH DIMINUTIVE SUFFIXES, Level 3)
   - Group 2: **0.4267** | TALENT, STARING, POPULARITY, BEAUTY                               | CORRECT GROUP (KINDS OF CONTESTS, Level 2)
   - Group 3: **0.3859** | FLOAT, WIND, PERCUSSION, BRASS                                    | INCORRECT (Max overlap: 3/4 with KINDS OF INSTRUMENTS)
   - Group 4: **0.3729** | BEE, STING, BUTTERFLY, STRING                                     | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS MUHAMMAD ALI QUOTE)
   - Group 5: **0.4636** | KITCHENETTE, STARLING, BUTTERFLY, DOGGY                           | INCORRECT (Max overlap: 3/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 6: **0.4115** | DROPLET, PERCUSSION, BRASS, STRING                                | INCORRECT (Max overlap: 3/4 with KINDS OF INSTRUMENTS)
   - Group 7: **0.3569** | BEE, FLOAT, STING, WIND                                           | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS MUHAMMAD ALI QUOTE)
   - Group 8: **0.4520** | TALENT, STARING, POPULARITY, STARLING                             | INCORRECT (Max overlap: 3/4 with KINDS OF CONTESTS)
   - Group 9: **0.4307** | KITCHENETTE, BEAUTY, BUTTERFLY, DOGGY                             | INCORRECT (Max overlap: 2/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 10: **0.4395** | DROPLET, STARING, POPULARITY, STARLING                            | INCORRECT (Max overlap: 2/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 11: **0.4190** | KITCHENETTE, TALENT, BEAUTY, DOGGY                                | INCORRECT (Max overlap: 2/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 12: **0.4311** | TALENT, DROPLET, STARING, POPULARITY                              | INCORRECT (Max overlap: 3/4 with KINDS OF CONTESTS)
   - Group 13: **0.4230** | KITCHENETTE, STARLING, BEAUTY, DOGGY                              | INCORRECT (Max overlap: 3/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 14: **0.4316** | TALENT, POPULARITY, BEAUTY, DOGGY                                 | INCORRECT (Max overlap: 3/4 with KINDS OF CONTESTS)
   - Group 15: **0.4197** | KITCHENETTE, DROPLET, STARING, STARLING                           | INCORRECT (Max overlap: 3/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 16: **0.4099** | KITCHENETTE, STARING, STARLING, DOGGY                             | INCORRECT (Max overlap: 3/4 with WORDS WITH DIMINUTIVE SUFFIXES)
   - Group 17: **0.3829** | TALENT, BEE, BEAUTY, BUTTERFLY                                    | INCORRECT (Max overlap: 2/4 with KINDS OF CONTESTS)
   - Group 18: **0.3815** | FLOAT, POPULARITY, STING, WIND                                    | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS MUHAMMAD ALI QUOTE)
   - Group 19: **0.4591** | TALENT, POPULARITY, BEAUTY, BUTTERFLY                             | INCORRECT (Max overlap: 3/4 with KINDS OF CONTESTS)
   - Group 20: **0.3511** | STARING, PERCUSSION, BRASS, STRING                                | INCORRECT (Max overlap: 3/4 with KINDS OF INSTRUMENTS)

---

## Puzzle 30 (ID: 851)
**Words on Board:** LEDE, FANCY, LIMESTONE, PRINCESS, CAPTION, INVENTION, HEDGEHOG, FICTION, DATELINE, FIGMENT, PLUMBER, MARBLE, SLATE, FLINT, PHOTO, GORILLA

### Ground Truth Categories:
* **Level 0 (FANTASY) [Type: SYNONYM_OR_NEAR]:** INVENTION, FANCY, FICTION, FIGMENT
* **Level 1 (KINDS OF ROCKS) [Type: SEMANTIC_SET]:** FLINT, LIMESTONE, MARBLE, SLATE
* **Level 2 (NEWS ARTICLE FEATURES) [Type: SEMANTIC_SET]:** CAPTION, DATELINE, LEDE, PHOTO
* **Level 3 (TITLE FIGURES IN CLASSIC VIDEO GAMES) [Type: NAMED_ENTITY_SET]:** GORILLA, HEDGEHOG, PLUMBER, PRINCESS

### Top Candidate Partitions:
1. **Partition Score: 0.4553**
   - Group 1: **0.5679** | CAPTION, INVENTION, FICTION, FIGMENT                              | INCORRECT (Max overlap: 3/4 with FANTASY) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 32.2%)]
   - Group 2: **0.5270** | PRINCESS, HEDGEHOG, PLUMBER, GORILLA                              | CORRECT GROUP (TITLE FIGURES IN CLASSIC VIDEO GAMES, Level 3)
   - Group 3: **0.4516** | LEDE, LIMESTONE, DATELINE, FLINT                                  | INCORRECT (Max overlap: 2/4 with NEWS ARTICLE FEATURES)
   - Group 4: **0.4058** | FANCY, MARBLE, SLATE, PHOTO                                       | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
2. **Partition Score: 0.4521**
   - Group 1: **0.5270** | PRINCESS, HEDGEHOG, PLUMBER, GORILLA                              | CORRECT GROUP (TITLE FIGURES IN CLASSIC VIDEO GAMES, Level 3)
   - Group 2: **0.4652** | FANCY, CAPTION, INVENTION, PHOTO                                  | INCORRECT (Max overlap: 2/4 with FANTASY)
   - Group 3: **0.4516** | LEDE, LIMESTONE, DATELINE, FLINT                                  | INCORRECT (Max overlap: 2/4 with NEWS ARTICLE FEATURES)
   - Group 4: **0.4311** | FICTION, FIGMENT, MARBLE, SLATE                                   | INCORRECT (Max overlap: 2/4 with FANTASY) | [Pred Type: SYNONYM_OR_NEAR (63.7%, no-rel 18.3%)]
3. **Partition Score: 0.4520**
   - Group 1: **0.5679** | CAPTION, INVENTION, FICTION, FIGMENT                              | INCORRECT (Max overlap: 3/4 with FANTASY) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 32.2%)]
   - Group 2: **0.5140** | LEDE, LIMESTONE, PLUMBER, FLINT                                   | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
   - Group 3: **0.4465** | PRINCESS, HEDGEHOG, DATELINE, GORILLA                             | INCORRECT (Max overlap: 3/4 with TITLE FIGURES IN CLASSIC VIDEO GAMES) | [Pred Type: NAMED_ENTITY_SET (49.2%, no-rel 17.1%)]
   - Group 4: **0.4058** | FANCY, MARBLE, SLATE, PHOTO                                       | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
4. **Partition Score: 0.4506**
   - Group 1: **0.5679** | CAPTION, INVENTION, FICTION, FIGMENT                              | INCORRECT (Max overlap: 3/4 with FANTASY) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 32.2%)]
   - Group 2: **0.5487** | LEDE, HEDGEHOG, PLUMBER, GORILLA                                  | INCORRECT (Max overlap: 3/4 with TITLE FIGURES IN CLASSIC VIDEO GAMES)
   - Group 3: **0.4058** | FANCY, MARBLE, SLATE, PHOTO                                       | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
   - Group 4: **0.4054** | LIMESTONE, PRINCESS, DATELINE, FLINT                              | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS) | [Pred Type: NAMED_ENTITY_SET (47.8%, no-rel 16.9%)]
5. **Partition Score: 0.4497**
   - Group 1: **0.5140** | LEDE, LIMESTONE, PLUMBER, FLINT                                   | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
   - Group 2: **0.4652** | FANCY, CAPTION, INVENTION, PHOTO                                  | INCORRECT (Max overlap: 2/4 with FANTASY)
   - Group 3: **0.4465** | PRINCESS, HEDGEHOG, DATELINE, GORILLA                             | INCORRECT (Max overlap: 3/4 with TITLE FIGURES IN CLASSIC VIDEO GAMES) | [Pred Type: NAMED_ENTITY_SET (49.2%, no-rel 17.1%)]
   - Group 4: **0.4311** | FICTION, FIGMENT, MARBLE, SLATE                                   | INCORRECT (Max overlap: 2/4 with FANTASY) | [Pred Type: SYNONYM_OR_NEAR (63.7%, no-rel 18.3%)]

### Top Candidate Groups:
   - Group 1: **0.5679** | CAPTION, INVENTION, FICTION, FIGMENT                              | INCORRECT (Max overlap: 3/4 with FANTASY) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 32.2%)]
   - Group 2: **0.5270** | PRINCESS, HEDGEHOG, PLUMBER, GORILLA                              | CORRECT GROUP (TITLE FIGURES IN CLASSIC VIDEO GAMES, Level 3)
   - Group 3: **0.4516** | LEDE, LIMESTONE, DATELINE, FLINT                                  | INCORRECT (Max overlap: 2/4 with NEWS ARTICLE FEATURES)
   - Group 4: **0.4058** | FANCY, MARBLE, SLATE, PHOTO                                       | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
   - Group 5: **0.4652** | FANCY, CAPTION, INVENTION, PHOTO                                  | INCORRECT (Max overlap: 2/4 with FANTASY)
   - Group 6: **0.4311** | FICTION, FIGMENT, MARBLE, SLATE                                   | INCORRECT (Max overlap: 2/4 with FANTASY) | [Pred Type: SYNONYM_OR_NEAR (63.7%, no-rel 18.3%)]
   - Group 7: **0.5140** | LEDE, LIMESTONE, PLUMBER, FLINT                                   | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
   - Group 8: **0.4465** | PRINCESS, HEDGEHOG, DATELINE, GORILLA                             | INCORRECT (Max overlap: 3/4 with TITLE FIGURES IN CLASSIC VIDEO GAMES) | [Pred Type: NAMED_ENTITY_SET (49.2%, no-rel 17.1%)]
   - Group 9: **0.5487** | LEDE, HEDGEHOG, PLUMBER, GORILLA                                  | INCORRECT (Max overlap: 3/4 with TITLE FIGURES IN CLASSIC VIDEO GAMES)
   - Group 10: **0.4054** | LIMESTONE, PRINCESS, DATELINE, FLINT                              | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS) | [Pred Type: NAMED_ENTITY_SET (47.8%, no-rel 16.9%)]
   - Group 11: **0.5434** | FANCY, INVENTION, FICTION, FIGMENT                                | CORRECT GROUP (FANTASY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 29.6%)]
   - Group 12: **0.3961** | CAPTION, MARBLE, SLATE, PHOTO                                     | INCORRECT (Max overlap: 2/4 with NEWS ARTICLE FEATURES)
   - Group 13: **0.4916** | LIMESTONE, HEDGEHOG, PLUMBER, FLINT                               | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
   - Group 14: **0.4375** | LEDE, PRINCESS, DATELINE, GORILLA                                 | INCORRECT (Max overlap: 2/4 with NEWS ARTICLE FEATURES) | [Pred Type: NAMED_ENTITY_SET (49.8%, no-rel 16.1%)]
   - Group 15: **0.4939** | LEDE, LIMESTONE, FLINT, GORILLA                                   | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
   - Group 16: **0.4306** | PRINCESS, HEDGEHOG, DATELINE, PLUMBER                             | INCORRECT (Max overlap: 3/4 with TITLE FIGURES IN CLASSIC VIDEO GAMES) | [Pred Type: NAMED_ENTITY_SET (48.1%, no-rel 18.2%)]
   - Group 17: **0.4860** | LEDE, LIMESTONE, HEDGEHOG, FLINT                                  | INCORRECT (Max overlap: 2/4 with KINDS OF ROCKS)
   - Group 18: **0.4378** | PRINCESS, DATELINE, PLUMBER, GORILLA                              | INCORRECT (Max overlap: 3/4 with TITLE FIGURES IN CLASSIC VIDEO GAMES) | [Pred Type: NAMED_ENTITY_SET (48.2%, no-rel 16.4%)]
   - Group 19: **0.4751** | LEDE, LIMESTONE, MARBLE, FLINT                                    | INCORRECT (Max overlap: 3/4 with KINDS OF ROCKS)
   - Group 20: **0.4087** | FICTION, DATELINE, FIGMENT, SLATE                                 | INCORRECT (Max overlap: 2/4 with FANTASY) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 17.1%)]

---

## Puzzle 31 (ID: 476)
**Words on Board:** DISCARD, ENERGY, KEEP, FULFILL, UPHOLD, LABOR, HONOR, SHEET, THROW, PLAY, JUSTICE, SHAM, BLANKET, DRAW, PASS, STATE

### Ground Truth Categories:
* **Level 0 (MAKE GOOD ON, AS A PROMISE) [Type: SYNONYM_OR_NEAR]:** FULFILL, HONOR, KEEP, UPHOLD
* **Level 1 (BEDDING) [Type: SEMANTIC_SET]:** BLANKET, SHAM, SHEET, THROW
* **Level 2 (ACTIONS IN CARD GAMES) [Type: SEMANTIC_SET]:** DISCARD, DRAW, PASS, PLAY
* **Level 3 (CABINET DEPARTMENTS) [Type: NAMED_ENTITY_SET]:** ENERGY, JUSTICE, LABOR, STATE

### Top Candidate Partitions:
1. **Partition Score: 0.5038**
   - Group 1: **0.7565** | ENERGY, LABOR, JUSTICE, STATE                                     | CORRECT GROUP (CABINET DEPARTMENTS, Level 3)
   - Group 2: **0.7298** | THROW, PLAY, DRAW, PASS                                           | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES)
   - Group 3: **0.4344** | DISCARD, KEEP, FULFILL, UPHOLD                                    | INCORRECT (Max overlap: 3/4 with MAKE GOOD ON, AS A PROMISE)
   - Group 4: **0.3910** | HONOR, SHEET, SHAM, BLANKET                                       | INCORRECT (Max overlap: 3/4 with BEDDING)
2. **Partition Score: 0.4990**
   - Group 1: **0.7565** | ENERGY, LABOR, JUSTICE, STATE                                     | CORRECT GROUP (CABINET DEPARTMENTS, Level 3)
   - Group 2: **0.6391** | KEEP, PLAY, DRAW, PASS                                            | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES)
   - Group 3: **0.4422** | FULFILL, UPHOLD, HONOR, SHAM                                      | INCORRECT (Max overlap: 3/4 with MAKE GOOD ON, AS A PROMISE)
   - Group 4: **0.4119** | DISCARD, SHEET, THROW, BLANKET                                    | INCORRECT (Max overlap: 3/4 with BEDDING) | [Pred Type: SYNONYM_OR_NEAR (56.5%, no-rel 24.2%)]
3. **Partition Score: 0.4982**
   - Group 1: **0.7565** | ENERGY, LABOR, JUSTICE, STATE                                     | CORRECT GROUP (CABINET DEPARTMENTS, Level 3)
   - Group 2: **0.5887** | DISCARD, THROW, DRAW, PASS                                        | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 33.9%)]
   - Group 3: **0.4422** | FULFILL, UPHOLD, HONOR, SHAM                                      | INCORRECT (Max overlap: 3/4 with MAKE GOOD ON, AS A PROMISE)
   - Group 4: **0.4289** | KEEP, SHEET, PLAY, BLANKET                                        | INCORRECT (Max overlap: 2/4 with BEDDING)
4. **Partition Score: 0.4865**
   - Group 1: **0.7565** | ENERGY, LABOR, JUSTICE, STATE                                     | CORRECT GROUP (CABINET DEPARTMENTS, Level 3)
   - Group 2: **0.6419** | KEEP, THROW, PLAY, PASS                                           | INCORRECT (Max overlap: 2/4 with ACTIONS IN CARD GAMES)
   - Group 3: **0.4299** | DISCARD, FULFILL, UPHOLD, DRAW                                    | INCORRECT (Max overlap: 2/4 with ACTIONS IN CARD GAMES)
   - Group 4: **0.3910** | HONOR, SHEET, SHAM, BLANKET                                       | INCORRECT (Max overlap: 3/4 with BEDDING)
5. **Partition Score: 0.4853**
   - Group 1: **0.7565** | ENERGY, LABOR, JUSTICE, STATE                                     | CORRECT GROUP (CABINET DEPARTMENTS, Level 3)
   - Group 2: **0.5887** | DISCARD, THROW, DRAW, PASS                                        | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 33.9%)]
   - Group 3: **0.4396** | KEEP, FULFILL, UPHOLD, HONOR                                      | CORRECT GROUP (MAKE GOOD ON, AS A PROMISE, Level 0)
   - Group 4: **0.4047** | SHEET, PLAY, SHAM, BLANKET                                        | INCORRECT (Max overlap: 3/4 with BEDDING)

### Top Candidate Groups:
   - Group 1: **0.7565** | ENERGY, LABOR, JUSTICE, STATE                                     | CORRECT GROUP (CABINET DEPARTMENTS, Level 3)
   - Group 2: **0.7298** | THROW, PLAY, DRAW, PASS                                           | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES)
   - Group 3: **0.4344** | DISCARD, KEEP, FULFILL, UPHOLD                                    | INCORRECT (Max overlap: 3/4 with MAKE GOOD ON, AS A PROMISE)
   - Group 4: **0.3910** | HONOR, SHEET, SHAM, BLANKET                                       | INCORRECT (Max overlap: 3/4 with BEDDING)
   - Group 5: **0.6391** | KEEP, PLAY, DRAW, PASS                                            | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES)
   - Group 6: **0.4422** | FULFILL, UPHOLD, HONOR, SHAM                                      | INCORRECT (Max overlap: 3/4 with MAKE GOOD ON, AS A PROMISE)
   - Group 7: **0.4119** | DISCARD, SHEET, THROW, BLANKET                                    | INCORRECT (Max overlap: 3/4 with BEDDING) | [Pred Type: SYNONYM_OR_NEAR (56.5%, no-rel 24.2%)]
   - Group 8: **0.5887** | DISCARD, THROW, DRAW, PASS                                        | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 33.9%)]
   - Group 9: **0.4289** | KEEP, SHEET, PLAY, BLANKET                                        | INCORRECT (Max overlap: 2/4 with BEDDING)
   - Group 10: **0.6419** | KEEP, THROW, PLAY, PASS                                           | INCORRECT (Max overlap: 2/4 with ACTIONS IN CARD GAMES)
   - Group 11: **0.4299** | DISCARD, FULFILL, UPHOLD, DRAW                                    | INCORRECT (Max overlap: 2/4 with ACTIONS IN CARD GAMES)
   - Group 12: **0.4396** | KEEP, FULFILL, UPHOLD, HONOR                                      | CORRECT GROUP (MAKE GOOD ON, AS A PROMISE, Level 0)
   - Group 13: **0.4047** | SHEET, PLAY, SHAM, BLANKET                                        | INCORRECT (Max overlap: 3/4 with BEDDING)
   - Group 14: **0.5648** | DISCARD, KEEP, UPHOLD, THROW                                      | INCORRECT (Max overlap: 2/4 with MAKE GOOD ON, AS A PROMISE) | [Pred Type: SYNONYM_OR_NEAR (53.1%, no-rel 29.2%)]
   - Group 15: **0.4996** | FULFILL, PLAY, DRAW, PASS                                         | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 31.9%)]
   - Group 16: **0.5643** | DISCARD, KEEP, THROW, DRAW                                        | INCORRECT (Max overlap: 2/4 with ACTIONS IN CARD GAMES)
   - Group 17: **0.4098** | SHEET, PLAY, BLANKET, PASS                                        | INCORRECT (Max overlap: 2/4 with BEDDING)
   - Group 18: **0.4911** | SHEET, PLAY, DRAW, PASS                                           | INCORRECT (Max overlap: 3/4 with ACTIONS IN CARD GAMES)
   - Group 19: **0.4329** | DISCARD, KEEP, THROW, BLANKET                                     | INCORRECT (Max overlap: 2/4 with BEDDING) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 32.0%)]
   - Group 20: **0.4482** | KEEP, SHEET, PLAY, DRAW                                           | INCORRECT (Max overlap: 2/4 with ACTIONS IN CARD GAMES)

---

## Puzzle 32 (ID: 6)
**Words on Board:** SIN, CHANCE, COMMON, JAIL, POWDER, ICE CUBE, FUTURE, MIDNIGHT, SISTER, WONDER, Q-TIP, BOARDWALK, BABY, SEA, ROYAL, GO

### Ground Truth Categories:
* **Level 0 (MONOPOLY SQUARES) [Type: NAMED_ENTITY_SET]:** BOARDWALK, CHANCE, GO, JAIL
* **Level 1 (SHADES OF BLUE) [Type: NAMED_ENTITY_SET]:** BABY, MIDNIGHT, POWDER, ROYAL
* **Level 2 (RAPPERS) [Type: NAMED_ENTITY_SET]:** COMMON, FUTURE, ICE CUBE, Q-TIP
* **Level 3 (MEMBERS OF A SEPTET) [Type: FILL_IN_THE_BLANK]:** SEA, SIN, SISTER, WONDER

### Top Candidate Partitions:
1. **Partition Score: 0.4706**
   - Group 1: **0.5524** | CHANCE, FUTURE, WONDER, GO                                        | INCORRECT (Max overlap: 2/4 with MONOPOLY SQUARES)
   - Group 2: **0.5207** | ICE CUBE, MIDNIGHT, Q-TIP, BOARDWALK                              | INCORRECT (Max overlap: 2/4 with RAPPERS)
   - Group 3: **0.4605** | COMMON, POWDER, SEA, ROYAL                                        | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE) | [Pred Type: FILL_IN_THE_BLANK (53.1%, no-rel 14.1%)]
   - Group 4: **0.4380** | SIN, JAIL, SISTER, BABY                                           | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
2. **Partition Score: 0.4622**
   - Group 1: **0.5524** | CHANCE, FUTURE, WONDER, GO                                        | INCORRECT (Max overlap: 2/4 with MONOPOLY SQUARES)
   - Group 2: **0.5207** | ICE CUBE, MIDNIGHT, Q-TIP, BOARDWALK                              | INCORRECT (Max overlap: 2/4 with RAPPERS)
   - Group 3: **0.4848** | COMMON, JAIL, SEA, ROYAL                                          | INCORRECT (Max overlap: 1/4 with RAPPERS)
   - Group 4: **0.4127** | SIN, POWDER, SISTER, BABY                                         | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
3. **Partition Score: 0.4620**
   - Group 1: **0.5207** | ICE CUBE, MIDNIGHT, Q-TIP, BOARDWALK                              | INCORRECT (Max overlap: 2/4 with RAPPERS)
   - Group 2: **0.5201** | SIN, CHANCE, FUTURE, GO                                           | INCORRECT (Max overlap: 2/4 with MONOPOLY SQUARES)
   - Group 3: **0.4434** | POWDER, SISTER, BABY, SEA                                         | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE)
   - Group 4: **0.4348** | COMMON, JAIL, WONDER, ROYAL                                       | INCORRECT (Max overlap: 1/4 with RAPPERS)
4. **Partition Score: 0.4608**
   - Group 1: **0.5207** | ICE CUBE, MIDNIGHT, Q-TIP, BOARDWALK                              | INCORRECT (Max overlap: 2/4 with RAPPERS)
   - Group 2: **0.5201** | SIN, CHANCE, FUTURE, GO                                           | INCORRECT (Max overlap: 2/4 with MONOPOLY SQUARES)
   - Group 3: **0.4555** | JAIL, SISTER, BABY, SEA                                           | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
   - Group 4: **0.4279** | COMMON, POWDER, WONDER, ROYAL                                     | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE)
5. **Partition Score: 0.4599**
   - Group 1: **0.5419** | SIN, CHANCE, WONDER, GO                                           | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
   - Group 2: **0.5207** | ICE CUBE, MIDNIGHT, Q-TIP, BOARDWALK                              | INCORRECT (Max overlap: 2/4 with RAPPERS)
   - Group 3: **0.4434** | POWDER, SISTER, BABY, SEA                                         | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE)
   - Group 4: **0.4256** | COMMON, JAIL, FUTURE, ROYAL                                       | INCORRECT (Max overlap: 2/4 with RAPPERS)

### Top Candidate Groups:
   - Group 1: **0.5524** | CHANCE, FUTURE, WONDER, GO                                        | INCORRECT (Max overlap: 2/4 with MONOPOLY SQUARES)
   - Group 2: **0.5207** | ICE CUBE, MIDNIGHT, Q-TIP, BOARDWALK                              | INCORRECT (Max overlap: 2/4 with RAPPERS)
   - Group 3: **0.4605** | COMMON, POWDER, SEA, ROYAL                                        | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE) | [Pred Type: FILL_IN_THE_BLANK (53.1%, no-rel 14.1%)]
   - Group 4: **0.4380** | SIN, JAIL, SISTER, BABY                                           | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
   - Group 5: **0.4848** | COMMON, JAIL, SEA, ROYAL                                          | INCORRECT (Max overlap: 1/4 with RAPPERS)
   - Group 6: **0.4127** | SIN, POWDER, SISTER, BABY                                         | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
   - Group 7: **0.5201** | SIN, CHANCE, FUTURE, GO                                           | INCORRECT (Max overlap: 2/4 with MONOPOLY SQUARES)
   - Group 8: **0.4434** | POWDER, SISTER, BABY, SEA                                         | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE)
   - Group 9: **0.4348** | COMMON, JAIL, WONDER, ROYAL                                       | INCORRECT (Max overlap: 1/4 with RAPPERS)
   - Group 10: **0.4555** | JAIL, SISTER, BABY, SEA                                           | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
   - Group 11: **0.4279** | COMMON, POWDER, WONDER, ROYAL                                     | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE)
   - Group 12: **0.5419** | SIN, CHANCE, WONDER, GO                                           | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
   - Group 13: **0.4256** | COMMON, JAIL, FUTURE, ROYAL                                       | INCORRECT (Max overlap: 2/4 with RAPPERS)
   - Group 14: **0.4115** | POWDER, SISTER, WONDER, BABY                                      | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE)
   - Group 15: **0.5070** | CHANCE, FUTURE, SEA, GO                                           | INCORRECT (Max overlap: 2/4 with MONOPOLY SQUARES)
   - Group 16: **0.4707** | SIN, SISTER, BABY, SEA                                            | INCORRECT (Max overlap: 3/4 with MEMBERS OF A SEPTET)
   - Group 17: **0.4012** | COMMON, JAIL, POWDER, ROYAL                                       | INCORRECT (Max overlap: 2/4 with SHADES OF BLUE) | [Pred Type: FILL_IN_THE_BLANK (50.9%, no-rel 15.5%)]
   - Group 18: **0.4114** | JAIL, SISTER, WONDER, BABY                                        | INCORRECT (Max overlap: 2/4 with MEMBERS OF A SEPTET)
   - Group 19: **0.4061** | COMMON, POWDER, FUTURE, ROYAL                                     | INCORRECT (Max overlap: 2/4 with RAPPERS)
   - Group 20: **0.4010** | JAIL, FUTURE, SISTER, BABY                                        | INCORRECT (Max overlap: 1/4 with MONOPOLY SQUARES)

---

## Puzzle 33 (ID: 27)
**Words on Board:** COVER, LUNG, BERET, JACKET, POT, LIVER, FEDORA, KIDNEY, ASS, PAGE, BOWLER, FEZ, KNIFE, HEART, SPINE, RABBIT

### Ground Truth Categories:
* **Level 0 (HATS) [Type: SEMANTIC_SET]:** BERET, BOWLER, FEDORA, FEZ
* **Level 1 (ORGANS) [Type: SEMANTIC_SET]:** HEART, KIDNEY, LIVER, LUNG
* **Level 2 (PARTS OF A BOOK) [Type: SEMANTIC_SET]:** COVER, JACKET, PAGE, SPINE
* **Level 3 (JACK ___) [Type: FILL_IN_THE_BLANK]:** ASS, KNIFE, POT, RABBIT

### Top Candidate Partitions:
1. **Partition Score: 0.5169**
   - Group 1: **0.7429** | LUNG, LIVER, KIDNEY, HEART                                        | CORRECT GROUP (ORGANS, Level 1)
   - Group 2: **0.5838** | POT, ASS, KNIFE, RABBIT                                           | CORRECT GROUP (JACK ___, Level 3) | [Pred Type: FILL_IN_THE_BLANK (46.5%, no-rel 32.0%)]
   - Group 3: **0.4984** | BERET, FEDORA, BOWLER, FEZ                                        | CORRECT GROUP (HATS, Level 0)
   - Group 4: **0.4495** | COVER, JACKET, PAGE, SPINE                                        | CORRECT GROUP (PARTS OF A BOOK, Level 2)
2. **Partition Score: 0.4952**
   - Group 1: **0.5078** | LIVER, KIDNEY, HEART, SPINE                                       | INCORRECT (Max overlap: 3/4 with ORGANS)
   - Group 2: **0.5013** | LUNG, ASS, KNIFE, RABBIT                                          | INCORRECT (Max overlap: 3/4 with JACK ___) | [Pred Type: FILL_IN_THE_BLANK (49.0%, no-rel 26.2%)]
   - Group 3: **0.4984** | BERET, FEDORA, BOWLER, FEZ                                        | CORRECT GROUP (HATS, Level 0)
   - Group 4: **0.4890** | COVER, JACKET, POT, PAGE                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A BOOK)
3. **Partition Score: 0.4764**
   - Group 1: **0.5167** | LUNG, LIVER, HEART, SPINE                                         | INCORRECT (Max overlap: 3/4 with ORGANS) | [Pred Type: SEMANTIC_SET (47.1%, no-rel 27.7%)]
   - Group 2: **0.4984** | BERET, FEDORA, BOWLER, FEZ                                        | CORRECT GROUP (HATS, Level 0)
   - Group 3: **0.4890** | COVER, JACKET, POT, PAGE                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A BOOK)
   - Group 4: **0.4550** | KIDNEY, ASS, KNIFE, RABBIT                                        | INCORRECT (Max overlap: 3/4 with JACK ___)
4. **Partition Score: 0.4737**
   - Group 1: **0.5252** | LUNG, LIVER, HEART, RABBIT                                        | INCORRECT (Max overlap: 3/4 with ORGANS)
   - Group 2: **0.4984** | BERET, FEDORA, BOWLER, FEZ                                        | CORRECT GROUP (HATS, Level 0)
   - Group 3: **0.4843** | POT, KIDNEY, ASS, KNIFE                                           | INCORRECT (Max overlap: 3/4 with JACK ___)
   - Group 4: **0.4495** | COVER, JACKET, PAGE, SPINE                                        | CORRECT GROUP (PARTS OF A BOOK, Level 2)
5. **Partition Score: 0.4734**
   - Group 1: **0.7429** | LUNG, LIVER, KIDNEY, HEART                                        | CORRECT GROUP (ORGANS, Level 1)
   - Group 2: **0.4984** | BERET, FEDORA, BOWLER, FEZ                                        | CORRECT GROUP (HATS, Level 0)
   - Group 3: **0.4890** | COVER, JACKET, POT, PAGE                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A BOOK)
   - Group 4: **0.3994** | ASS, KNIFE, SPINE, RABBIT                                         | INCORRECT (Max overlap: 3/4 with JACK ___)

### Top Candidate Groups:
   - Group 1: **0.7429** | LUNG, LIVER, KIDNEY, HEART                                        | CORRECT GROUP (ORGANS, Level 1)
   - Group 2: **0.5838** | POT, ASS, KNIFE, RABBIT                                           | CORRECT GROUP (JACK ___, Level 3) | [Pred Type: FILL_IN_THE_BLANK (46.5%, no-rel 32.0%)]
   - Group 3: **0.4984** | BERET, FEDORA, BOWLER, FEZ                                        | CORRECT GROUP (HATS, Level 0)
   - Group 4: **0.4495** | COVER, JACKET, PAGE, SPINE                                        | CORRECT GROUP (PARTS OF A BOOK, Level 2)
   - Group 5: **0.5078** | LIVER, KIDNEY, HEART, SPINE                                       | INCORRECT (Max overlap: 3/4 with ORGANS)
   - Group 6: **0.5013** | LUNG, ASS, KNIFE, RABBIT                                          | INCORRECT (Max overlap: 3/4 with JACK ___) | [Pred Type: FILL_IN_THE_BLANK (49.0%, no-rel 26.2%)]
   - Group 7: **0.4890** | COVER, JACKET, POT, PAGE                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A BOOK)
   - Group 8: **0.5167** | LUNG, LIVER, HEART, SPINE                                         | INCORRECT (Max overlap: 3/4 with ORGANS) | [Pred Type: SEMANTIC_SET (47.1%, no-rel 27.7%)]
   - Group 9: **0.4550** | KIDNEY, ASS, KNIFE, RABBIT                                        | INCORRECT (Max overlap: 3/4 with JACK ___)
   - Group 10: **0.5252** | LUNG, LIVER, HEART, RABBIT                                        | INCORRECT (Max overlap: 3/4 with ORGANS)
   - Group 11: **0.4843** | POT, KIDNEY, ASS, KNIFE                                           | INCORRECT (Max overlap: 3/4 with JACK ___)
   - Group 12: **0.3994** | ASS, KNIFE, SPINE, RABBIT                                         | INCORRECT (Max overlap: 3/4 with JACK ___)
   - Group 13: **0.5536** | POT, KIDNEY, ASS, RABBIT                                          | INCORRECT (Max overlap: 3/4 with JACK ___)
   - Group 14: **0.4650** | LUNG, LIVER, KNIFE, HEART                                         | INCORRECT (Max overlap: 3/4 with ORGANS)
   - Group 15: **0.4869** | POT, LIVER, KIDNEY, HEART                                         | INCORRECT (Max overlap: 3/4 with ORGANS)
   - Group 16: **0.5038** | LIVER, KIDNEY, HEART, RABBIT                                      | INCORRECT (Max overlap: 3/4 with ORGANS)
   - Group 17: **0.4702** | LUNG, POT, ASS, KNIFE                                             | INCORRECT (Max overlap: 3/4 with JACK ___) | [Pred Type: FILL_IN_THE_BLANK (45.1%, no-rel 25.8%)]
   - Group 18: **0.4617** | COVER, JACKET, PAGE, FEZ                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A BOOK)
   - Group 19: **0.4402** | POT, ASS, KNIFE, SPINE                                            | INCORRECT (Max overlap: 3/4 with JACK ___)
   - Group 20: **0.4185** | BERET, FEDORA, BOWLER, RABBIT                                     | INCORRECT (Max overlap: 3/4 with HATS)

---

## Puzzle 34 (ID: 947)
**Words on Board:** TIGHT, RAINMAKER, PARTNER, MOVIE, MISTLETOE, FAST, TREATMENT, AUCTION, USER, SECURE, FIRM, FROSTY, CLIENT, ACCOUNT, SNOWMAN, CONSUMER

### Ground Truth Categories:
* **Level 0 (FIXED) [Type: SYNONYM_OR_NEAR]:** FAST, FIRM, SECURE, TIGHT
* **Level 1 (RECEIVER OF GOODS OR SERVICES) [Type: SYNONYM_OR_NEAR]:** ACCOUNT, CLIENT, CONSUMER, USER
* **Level 2 (STARTING WITH WEATHER CONDITIONS) [Type: WORD_FORM]:** FROSTY, MISTLETOE, RAINMAKER, SNOWMAN
* **Level 3 (SILENT ___) [Type: FILL_IN_THE_BLANK]:** AUCTION, MOVIE, PARTNER, TREATMENT

### Top Candidate Partitions:
1. **Partition Score: 0.5724**
   - Group 1: **0.8468** | TIGHT, FAST, SECURE, FIRM                                         | CORRECT GROUP (FIXED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 41.3%)]
   - Group 2: **0.5932** | USER, CLIENT, ACCOUNT, CONSUMER                                   | CORRECT GROUP (RECEIVER OF GOODS OR SERVICES, Level 1)
   - Group 3: **0.5541** | RAINMAKER, MISTLETOE, FROSTY, SNOWMAN                             | CORRECT GROUP (STARTING WITH WEATHER CONDITIONS, Level 2)
   - Group 4: **0.5113** | PARTNER, MOVIE, TREATMENT, AUCTION                                | CORRECT GROUP (SILENT ___, Level 3)
2. **Partition Score: 0.5404**
   - Group 1: **0.8468** | TIGHT, FAST, SECURE, FIRM                                         | CORRECT GROUP (FIXED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 41.3%)]
   - Group 2: **0.5541** | RAINMAKER, MISTLETOE, FROSTY, SNOWMAN                             | CORRECT GROUP (STARTING WITH WEATHER CONDITIONS, Level 2)
   - Group 3: **0.5509** | PARTNER, USER, CLIENT, ACCOUNT                                    | INCORRECT (Max overlap: 3/4 with RECEIVER OF GOODS OR SERVICES)
   - Group 4: **0.4643** | MOVIE, TREATMENT, AUCTION, CONSUMER                               | INCORRECT (Max overlap: 3/4 with SILENT ___)
3. **Partition Score: 0.5331**
   - Group 1: **0.8468** | TIGHT, FAST, SECURE, FIRM                                         | CORRECT GROUP (FIXED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 41.3%)]
   - Group 2: **0.5541** | RAINMAKER, MISTLETOE, FROSTY, SNOWMAN                             | CORRECT GROUP (STARTING WITH WEATHER CONDITIONS, Level 2)
   - Group 3: **0.5305** | PARTNER, USER, ACCOUNT, CONSUMER                                  | INCORRECT (Max overlap: 3/4 with RECEIVER OF GOODS OR SERVICES)
   - Group 4: **0.4574** | MOVIE, TREATMENT, AUCTION, CLIENT                                 | INCORRECT (Max overlap: 3/4 with SILENT ___)
4. **Partition Score: 0.5330**
   - Group 1: **0.8468** | TIGHT, FAST, SECURE, FIRM                                         | CORRECT GROUP (FIXED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 41.3%)]
   - Group 2: **0.5932** | USER, CLIENT, ACCOUNT, CONSUMER                                   | CORRECT GROUP (RECEIVER OF GOODS OR SERVICES, Level 1)
   - Group 3: **0.5281** | MOVIE, MISTLETOE, FROSTY, SNOWMAN                                 | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)
   - Group 4: **0.4440** | RAINMAKER, PARTNER, TREATMENT, AUCTION                            | INCORRECT (Max overlap: 3/4 with SILENT ___)
5. **Partition Score: 0.5327**
   - Group 1: **0.8468** | TIGHT, FAST, SECURE, FIRM                                         | CORRECT GROUP (FIXED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 41.3%)]
   - Group 2: **0.5932** | USER, CLIENT, ACCOUNT, CONSUMER                                   | CORRECT GROUP (RECEIVER OF GOODS OR SERVICES, Level 1)
   - Group 3: **0.4761** | RAINMAKER, PARTNER, MOVIE, AUCTION                                | INCORRECT (Max overlap: 3/4 with SILENT ___)
   - Group 4: **0.4623** | MISTLETOE, TREATMENT, FROSTY, SNOWMAN                             | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)

### Top Candidate Groups:
   - Group 1: **0.8468** | TIGHT, FAST, SECURE, FIRM                                         | CORRECT GROUP (FIXED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 41.3%)]
   - Group 2: **0.5932** | USER, CLIENT, ACCOUNT, CONSUMER                                   | CORRECT GROUP (RECEIVER OF GOODS OR SERVICES, Level 1)
   - Group 3: **0.5541** | RAINMAKER, MISTLETOE, FROSTY, SNOWMAN                             | CORRECT GROUP (STARTING WITH WEATHER CONDITIONS, Level 2)
   - Group 4: **0.5113** | PARTNER, MOVIE, TREATMENT, AUCTION                                | CORRECT GROUP (SILENT ___, Level 3)
   - Group 5: **0.5509** | PARTNER, USER, CLIENT, ACCOUNT                                    | INCORRECT (Max overlap: 3/4 with RECEIVER OF GOODS OR SERVICES)
   - Group 6: **0.4643** | MOVIE, TREATMENT, AUCTION, CONSUMER                               | INCORRECT (Max overlap: 3/4 with SILENT ___)
   - Group 7: **0.5305** | PARTNER, USER, ACCOUNT, CONSUMER                                  | INCORRECT (Max overlap: 3/4 with RECEIVER OF GOODS OR SERVICES)
   - Group 8: **0.4574** | MOVIE, TREATMENT, AUCTION, CLIENT                                 | INCORRECT (Max overlap: 3/4 with SILENT ___)
   - Group 9: **0.5281** | MOVIE, MISTLETOE, FROSTY, SNOWMAN                                 | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)
   - Group 10: **0.4440** | RAINMAKER, PARTNER, TREATMENT, AUCTION                            | INCORRECT (Max overlap: 3/4 with SILENT ___)
   - Group 11: **0.4761** | RAINMAKER, PARTNER, MOVIE, AUCTION                                | INCORRECT (Max overlap: 3/4 with SILENT ___)
   - Group 12: **0.4623** | MISTLETOE, TREATMENT, FROSTY, SNOWMAN                             | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)
   - Group 13: **0.5120** | RAINMAKER, PARTNER, MOVIE, TREATMENT                              | INCORRECT (Max overlap: 3/4 with SILENT ___)
   - Group 14: **0.4446** | MISTLETOE, AUCTION, FROSTY, SNOWMAN                               | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)
   - Group 15: **0.4685** | PARTNER, MISTLETOE, FROSTY, SNOWMAN                               | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)
   - Group 16: **0.4596** | RAINMAKER, MOVIE, TREATMENT, AUCTION                              | INCORRECT (Max overlap: 3/4 with SILENT ___)
   - Group 17: **0.5060** | MISTLETOE, FROSTY, SNOWMAN, CONSUMER                              | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)
   - Group 18: **0.5298** | RAINMAKER, FROSTY, SNOWMAN, CONSUMER                              | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)
   - Group 19: **0.4486** | MOVIE, MISTLETOE, TREATMENT, AUCTION                              | INCORRECT (Max overlap: 3/4 with SILENT ___)
   - Group 20: **0.4860** | RAINMAKER, PARTNER, FROSTY, SNOWMAN                               | INCORRECT (Max overlap: 3/4 with STARTING WITH WEATHER CONDITIONS)

---

## Puzzle 35 (ID: 462)
**Words on Board:** EBB, CLOWN, STAY, DWEEB, DWARF, SIN, DROP, DECLINE, SAP, INHABIT, DWELL, WONDER, TURKEY, DWINDLE, SEA, LIVE

### Ground Truth Categories:
* **Level 0 (RESIDE) [Type: SYNONYM_OR_NEAR]:** DWELL, INHABIT, LIVE, STAY
* **Level 1 (DECREASE) [Type: SYNONYM_OR_NEAR]:** DECLINE, DROP, DWINDLE, EBB
* **Level 2 (DOOFUS) [Type: SYNONYM_OR_NEAR]:** CLOWN, DWEEB, SAP, TURKEY
* **Level 3 (MEMBER OF A SEPTET) [Type: NAMED_ENTITY_SET]:** DWARF, SEA, SIN, WONDER

### Top Candidate Partitions:
1. **Partition Score: 0.5341**
   - Group 1: **0.6700** | STAY, INHABIT, DWELL, LIVE                                        | CORRECT GROUP (RESIDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 31.1%)]
   - Group 2: **0.6635** | EBB, DROP, DECLINE, DWINDLE                                       | CORRECT GROUP (DECREASE, Level 1)
   - Group 3: **0.5973** | CLOWN, DWEEB, DWARF, TURKEY                                       | INCORRECT (Max overlap: 3/4 with DOOFUS)
   - Group 4: **0.4339** | SIN, SAP, WONDER, SEA                                             | INCORRECT (Max overlap: 3/4 with MEMBER OF A SEPTET)
2. **Partition Score: 0.5218**
   - Group 1: **0.6700** | STAY, INHABIT, DWELL, LIVE                                        | CORRECT GROUP (RESIDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 31.1%)]
   - Group 2: **0.6635** | EBB, DROP, DECLINE, DWINDLE                                       | CORRECT GROUP (DECREASE, Level 1)
   - Group 3: **0.4945** | CLOWN, DWEEB, WONDER, TURKEY                                      | INCORRECT (Max overlap: 3/4 with DOOFUS)
   - Group 4: **0.4474** | DWARF, SIN, SAP, SEA                                              | INCORRECT (Max overlap: 3/4 with MEMBER OF A SEPTET)
3. **Partition Score: 0.5165**
   - Group 1: **0.6700** | STAY, INHABIT, DWELL, LIVE                                        | CORRECT GROUP (RESIDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 31.1%)]
   - Group 2: **0.6635** | EBB, DROP, DECLINE, DWINDLE                                       | CORRECT GROUP (DECREASE, Level 1)
   - Group 3: **0.6441** | DWARF, SAP, TURKEY, SEA                                           | INCORRECT (Max overlap: 2/4 with MEMBER OF A SEPTET)
   - Group 4: **0.3824** | CLOWN, DWEEB, SIN, WONDER                                         | INCORRECT (Max overlap: 2/4 with DOOFUS)
4. **Partition Score: 0.5162**
   - Group 1: **0.6700** | STAY, INHABIT, DWELL, LIVE                                        | CORRECT GROUP (RESIDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 31.1%)]
   - Group 2: **0.6635** | EBB, DROP, DECLINE, DWINDLE                                       | CORRECT GROUP (DECREASE, Level 1)
   - Group 3: **0.4947** | CLOWN, DWEEB, DWARF, WONDER                                       | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 4: **0.4364** | SIN, SAP, TURKEY, SEA                                             | INCORRECT (Max overlap: 2/4 with MEMBER OF A SEPTET)
5. **Partition Score: 0.5121**
   - Group 1: **0.6700** | STAY, INHABIT, DWELL, LIVE                                        | CORRECT GROUP (RESIDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 31.1%)]
   - Group 2: **0.6635** | EBB, DROP, DECLINE, DWINDLE                                       | CORRECT GROUP (DECREASE, Level 1)
   - Group 3: **0.4719** | DWEEB, DWARF, WONDER, TURKEY                                      | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 4: **0.4367** | CLOWN, SIN, SAP, SEA                                              | INCORRECT (Max overlap: 2/4 with DOOFUS)

### Top Candidate Groups:
   - Group 1: **0.6700** | STAY, INHABIT, DWELL, LIVE                                        | CORRECT GROUP (RESIDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 31.1%)]
   - Group 2: **0.6635** | EBB, DROP, DECLINE, DWINDLE                                       | CORRECT GROUP (DECREASE, Level 1)
   - Group 3: **0.5973** | CLOWN, DWEEB, DWARF, TURKEY                                       | INCORRECT (Max overlap: 3/4 with DOOFUS)
   - Group 4: **0.4339** | SIN, SAP, WONDER, SEA                                             | INCORRECT (Max overlap: 3/4 with MEMBER OF A SEPTET)
   - Group 5: **0.4945** | CLOWN, DWEEB, WONDER, TURKEY                                      | INCORRECT (Max overlap: 3/4 with DOOFUS)
   - Group 6: **0.4474** | DWARF, SIN, SAP, SEA                                              | INCORRECT (Max overlap: 3/4 with MEMBER OF A SEPTET)
   - Group 7: **0.6441** | DWARF, SAP, TURKEY, SEA                                           | INCORRECT (Max overlap: 2/4 with MEMBER OF A SEPTET)
   - Group 8: **0.3824** | CLOWN, DWEEB, SIN, WONDER                                         | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 9: **0.4947** | CLOWN, DWEEB, DWARF, WONDER                                       | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 10: **0.4364** | SIN, SAP, TURKEY, SEA                                             | INCORRECT (Max overlap: 2/4 with MEMBER OF A SEPTET)
   - Group 11: **0.4719** | DWEEB, DWARF, WONDER, TURKEY                                      | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 12: **0.4367** | CLOWN, SIN, SAP, SEA                                              | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 13: **0.5219** | DWEEB, DWARF, TURKEY, SEA                                         | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 14: **0.4166** | CLOWN, SIN, SAP, WONDER                                           | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 15: **0.5263** | CLOWN, DWARF, WONDER, TURKEY                                      | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 16: **0.4097** | DWEEB, SIN, SAP, SEA                                              | INCORRECT (Max overlap: 2/4 with DOOFUS)
   - Group 17: **0.6063** | STAY, DROP, DECLINE, DWINDLE                                      | INCORRECT (Max overlap: 3/4 with DECREASE)
   - Group 18: **0.5569** | EBB, INHABIT, DWELL, LIVE                                         | INCORRECT (Max overlap: 3/4 with RESIDE) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 35.1%)]
   - Group 19: **0.5628** | DWEEB, DWARF, SAP, TURKEY                                         | INCORRECT (Max overlap: 3/4 with DOOFUS)
   - Group 20: **0.3932** | CLOWN, SIN, WONDER, SEA                                           | INCORRECT (Max overlap: 3/4 with MEMBER OF A SEPTET)

---

## Puzzle 36 (ID: 60)
**Words on Board:** ANKLET, CHARM, PLEASE, TICKLE, RING, FIELD, PURGE, DIAMOND, BANGLE, RINK, SCREAM, BROOCH, SAW, PENDANT, COURT, DELIGHT

### Ground Truth Categories:
* **Level 0 (HORROR FRANCHISES) [Type: NAMED_ENTITY_SET]:** PURGE, RING, SAW, SCREAM
* **Level 1 (SPORTS VENUES) [Type: SEMANTIC_SET]:** COURT, DIAMOND, FIELD, RINK
* **Level 2 (MAKE HAPPY) [Type: SYNONYM_OR_NEAR]:** CHARM, DELIGHT, PLEASE, TICKLE
* **Level 3 (JEWELRY) [Type: SEMANTIC_SET]:** ANKLET, BANGLE, BROOCH, PENDANT

### Top Candidate Partitions:
1. **Partition Score: 0.5005**
   - Group 1: **0.6510** | ANKLET, BANGLE, BROOCH, PENDANT                                   | CORRECT GROUP (JEWELRY, Level 3)
   - Group 2: **0.5984** | CHARM, PLEASE, TICKLE, DELIGHT                                    | CORRECT GROUP (MAKE HAPPY, Level 2) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 30.5%)]
   - Group 3: **0.4805** | RING, FIELD, DIAMOND, RINK                                        | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 4: **0.4391** | PURGE, SCREAM, SAW, COURT                                         | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
2. **Partition Score: 0.4953**
   - Group 1: **0.5984** | CHARM, PLEASE, TICKLE, DELIGHT                                    | CORRECT GROUP (MAKE HAPPY, Level 2) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 30.5%)]
   - Group 2: **0.5231** | RING, FIELD, DIAMOND, COURT                                       | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 3: **0.4739** | PURGE, SCREAM, SAW, PENDANT                                       | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 4: **0.4704** | ANKLET, BANGLE, RINK, BROOCH                                      | INCORRECT (Max overlap: 3/4 with JEWELRY)
3. **Partition Score: 0.4948**
   - Group 1: **0.6510** | ANKLET, BANGLE, BROOCH, PENDANT                                   | CORRECT GROUP (JEWELRY, Level 3)
   - Group 2: **0.5629** | CHARM, PLEASE, PURGE, DELIGHT                                     | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (67.7%, no-rel 26.0%)]
   - Group 3: **0.4719** | FIELD, DIAMOND, SAW, COURT                                        | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 4: **0.4439** | TICKLE, RING, RINK, SCREAM                                        | INCORRECT (Max overlap: 2/4 with HORROR FRANCHISES)
4. **Partition Score: 0.4911**
   - Group 1: **0.5629** | CHARM, PLEASE, PURGE, DELIGHT                                     | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (67.7%, no-rel 26.0%)]
   - Group 2: **0.5113** | ANKLET, TICKLE, BROOCH, PENDANT                                   | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 3: **0.4803** | RING, BANGLE, RINK, SCREAM                                        | INCORRECT (Max overlap: 2/4 with HORROR FRANCHISES)
   - Group 4: **0.4719** | FIELD, DIAMOND, SAW, COURT                                        | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
5. **Partition Score: 0.4904**
   - Group 1: **0.6510** | ANKLET, BANGLE, BROOCH, PENDANT                                   | CORRECT GROUP (JEWELRY, Level 3)
   - Group 2: **0.5984** | CHARM, PLEASE, TICKLE, DELIGHT                                    | CORRECT GROUP (MAKE HAPPY, Level 2) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 30.5%)]
   - Group 3: **0.4719** | FIELD, DIAMOND, SAW, COURT                                        | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 4: **0.4224** | RING, PURGE, RINK, SCREAM                                         | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)

### Top Candidate Groups:
   - Group 1: **0.6510** | ANKLET, BANGLE, BROOCH, PENDANT                                   | CORRECT GROUP (JEWELRY, Level 3)
   - Group 2: **0.5984** | CHARM, PLEASE, TICKLE, DELIGHT                                    | CORRECT GROUP (MAKE HAPPY, Level 2) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 30.5%)]
   - Group 3: **0.4805** | RING, FIELD, DIAMOND, RINK                                        | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 4: **0.4391** | PURGE, SCREAM, SAW, COURT                                         | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 5: **0.5231** | RING, FIELD, DIAMOND, COURT                                       | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 6: **0.4739** | PURGE, SCREAM, SAW, PENDANT                                       | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 7: **0.4704** | ANKLET, BANGLE, RINK, BROOCH                                      | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 8: **0.5629** | CHARM, PLEASE, PURGE, DELIGHT                                     | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (67.7%, no-rel 26.0%)]
   - Group 9: **0.4719** | FIELD, DIAMOND, SAW, COURT                                        | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 10: **0.4439** | TICKLE, RING, RINK, SCREAM                                        | INCORRECT (Max overlap: 2/4 with HORROR FRANCHISES)
   - Group 11: **0.5113** | ANKLET, TICKLE, BROOCH, PENDANT                                   | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 12: **0.4803** | RING, BANGLE, RINK, SCREAM                                        | INCORRECT (Max overlap: 2/4 with HORROR FRANCHISES)
   - Group 13: **0.4224** | RING, PURGE, RINK, SCREAM                                         | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 14: **0.4823** | ANKLET, PURGE, BROOCH, PENDANT                                    | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 15: **0.5359** | CHARM, PLEASE, PENDANT, DELIGHT                                   | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (70.3%, no-rel 20.8%)]
   - Group 16: **0.4740** | TICKLE, PURGE, SCREAM, SAW                                        | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 17: **0.4871** | ANKLET, RING, BANGLE, RINK                                        | INCORRECT (Max overlap: 2/4 with JEWELRY)
   - Group 18: **0.4785** | TICKLE, SCREAM, BROOCH, PENDANT                                   | INCORRECT (Max overlap: 2/4 with JEWELRY)
   - Group 19: **0.5359** | ANKLET, SCREAM, BROOCH, PENDANT                                   | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 20: **0.4507** | TICKLE, RING, BANGLE, RINK                                        | INCORRECT (Max overlap: 1/4 with MAKE HAPPY)

---

## Puzzle 37 (ID: 453)
**Words on Board:** EPISODE, NUMBER, COUNT, AMOUNT, BOUNCE, CARD, AFFAIR, TOTAL, LETTER, COIL, GEYSER, CATALOG, SEASON, BILL, EVENT, MATTER

### Ground Truth Categories:
* **Level 0 (QUANTITY) [Type: SYNONYM_OR_NEAR]:** AMOUNT, COUNT, NUMBER, TOTAL
* **Level 1 (INCIDENT) [Type: SYNONYM_OR_NEAR]:** AFFAIR, EPISODE, EVENT, MATTER
* **Level 2 (THINGS RECEIVED IN THE MAIL) [Type: SEMANTIC_SET]:** BILL, CARD, CATALOG, LETTER
* **Level 3 (WHAT “SPRING” MIGHT REFER TO) [Type: WORDPLAY_TRANSFORM]:** BOUNCE, COIL, GEYSER, SEASON

### Top Candidate Partitions:
1. **Partition Score: 0.5098**
   - Group 1: **0.9035** | NUMBER, COUNT, AMOUNT, TOTAL                                      | CORRECT GROUP (QUANTITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.3%, no-rel 26.4%)]
   - Group 2: **0.4842** | CARD, LETTER, CATALOG, BILL                                       | CORRECT GROUP (THINGS RECEIVED IN THE MAIL, Level 2)
   - Group 3: **0.4743** | EPISODE, BOUNCE, COIL, GEYSER                                     | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)
   - Group 4: **0.4458** | AFFAIR, SEASON, EVENT, MATTER                                     | INCORRECT (Max overlap: 3/4 with INCIDENT) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 29.6%)]
2. **Partition Score: 0.5006**
   - Group 1: **0.9035** | NUMBER, COUNT, AMOUNT, TOTAL                                      | CORRECT GROUP (QUANTITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.3%, no-rel 26.4%)]
   - Group 2: **0.5195** | EPISODE, CARD, CATALOG, BILL                                      | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 3: **0.4458** | AFFAIR, SEASON, EVENT, MATTER                                     | INCORRECT (Max overlap: 3/4 with INCIDENT) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 29.6%)]
   - Group 4: **0.4253** | BOUNCE, LETTER, COIL, GEYSER                                      | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)
3. **Partition Score: 0.4964**
   - Group 1: **0.9035** | NUMBER, COUNT, AMOUNT, TOTAL                                      | CORRECT GROUP (QUANTITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.3%, no-rel 26.4%)]
   - Group 2: **0.4842** | CARD, LETTER, CATALOG, BILL                                       | CORRECT GROUP (THINGS RECEIVED IN THE MAIL, Level 2)
   - Group 3: **0.4430** | EPISODE, AFFAIR, SEASON, MATTER                                   | INCORRECT (Max overlap: 3/4 with INCIDENT) | [Pred Type: SYNONYM_OR_NEAR (68.1%, no-rel 21.0%)]
   - Group 4: **0.4310** | BOUNCE, COIL, GEYSER, EVENT                                       | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)
4. **Partition Score: 0.4910**
   - Group 1: **0.7614** | COUNT, AMOUNT, TOTAL, MATTER                                      | INCORRECT (Max overlap: 3/4 with QUANTITY) | [Pred Type: SYNONYM_OR_NEAR (69.0%, no-rel 25.4%)]
   - Group 2: **0.5038** | NUMBER, CARD, CATALOG, BILL                                       | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 3: **0.4956** | EPISODE, AFFAIR, SEASON, EVENT                                    | INCORRECT (Max overlap: 3/4 with INCIDENT)
   - Group 4: **0.4253** | BOUNCE, LETTER, COIL, GEYSER                                      | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)
5. **Partition Score: 0.4907**
   - Group 1: **0.9035** | NUMBER, COUNT, AMOUNT, TOTAL                                      | CORRECT GROUP (QUANTITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.3%, no-rel 26.4%)]
   - Group 2: **0.5116** | EPISODE, CARD, LETTER, BILL                                       | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 3: **0.4458** | AFFAIR, SEASON, EVENT, MATTER                                     | INCORRECT (Max overlap: 3/4 with INCIDENT) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 29.6%)]
   - Group 4: **0.4089** | BOUNCE, COIL, GEYSER, CATALOG                                     | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)

### Top Candidate Groups:
   - Group 1: **0.9035** | NUMBER, COUNT, AMOUNT, TOTAL                                      | CORRECT GROUP (QUANTITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.3%, no-rel 26.4%)]
   - Group 2: **0.4842** | CARD, LETTER, CATALOG, BILL                                       | CORRECT GROUP (THINGS RECEIVED IN THE MAIL, Level 2)
   - Group 3: **0.4743** | EPISODE, BOUNCE, COIL, GEYSER                                     | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)
   - Group 4: **0.4458** | AFFAIR, SEASON, EVENT, MATTER                                     | INCORRECT (Max overlap: 3/4 with INCIDENT) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 29.6%)]
   - Group 5: **0.5195** | EPISODE, CARD, CATALOG, BILL                                      | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 6: **0.4253** | BOUNCE, LETTER, COIL, GEYSER                                      | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)
   - Group 7: **0.4430** | EPISODE, AFFAIR, SEASON, MATTER                                   | INCORRECT (Max overlap: 3/4 with INCIDENT) | [Pred Type: SYNONYM_OR_NEAR (68.1%, no-rel 21.0%)]
   - Group 8: **0.4310** | BOUNCE, COIL, GEYSER, EVENT                                       | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)
   - Group 9: **0.7614** | COUNT, AMOUNT, TOTAL, MATTER                                      | INCORRECT (Max overlap: 3/4 with QUANTITY) | [Pred Type: SYNONYM_OR_NEAR (69.0%, no-rel 25.4%)]
   - Group 10: **0.5038** | NUMBER, CARD, CATALOG, BILL                                       | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 11: **0.4956** | EPISODE, AFFAIR, SEASON, EVENT                                    | INCORRECT (Max overlap: 3/4 with INCIDENT)
   - Group 12: **0.5116** | EPISODE, CARD, LETTER, BILL                                       | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 13: **0.4089** | BOUNCE, COIL, GEYSER, CATALOG                                     | INCORRECT (Max overlap: 3/4 with WHAT “SPRING” MIGHT REFER TO)
   - Group 14: **0.4427** | EPISODE, LETTER, COIL, GEYSER                                     | INCORRECT (Max overlap: 2/4 with WHAT “SPRING” MIGHT REFER TO)
   - Group 15: **0.4242** | BOUNCE, CARD, CATALOG, BILL                                       | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 16: **0.4439** | LETTER, COIL, GEYSER, EVENT                                       | INCORRECT (Max overlap: 2/4 with WHAT “SPRING” MIGHT REFER TO)
   - Group 17: **0.5112** | NUMBER, CARD, LETTER, BILL                                        | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 18: **0.4306** | CARD, CATALOG, BILL, EVENT                                        | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 19: **0.4322** | CARD, GEYSER, CATALOG, BILL                                       | INCORRECT (Max overlap: 3/4 with THINGS RECEIVED IN THE MAIL)
   - Group 20: **0.4219** | BOUNCE, LETTER, COIL, EVENT                                       | INCORRECT (Max overlap: 2/4 with WHAT “SPRING” MIGHT REFER TO)

---

## Puzzle 38 (ID: 1057)
**Words on Board:** THE PENTAGON, FILM NERD, MAKING OUT, LEFT FIELD, THE BLUE, NECKING, FIRST BASE, HOME PLATE, MEMENTO, NOWHERE, THIN AIR, TONSIL HOCKEY, BURGER KING WHOPPER, PITCHER'S MOUND, SCHOOL CROSSING SIGN, JEANS BACK POCKET

### Ground Truth Categories:
* **Level 0 (CANOODLING) [Type: SYNONYM_OR_NEAR]:** FIRST BASE, MAKING OUT, NECKING, TONSIL HOCKEY
* **Level 1 (FIVE-SIDED THINGS) [Type: SEMANTIC_SET]:** HOME PLATE, JEANS BACK POCKET, SCHOOL CROSSING SIGN, THE PENTAGON
* **Level 2 (UNEXPECTED PLACES TO BE "OUT OF") [Type: FILL_IN_THE_BLANK]:** LEFT FIELD, NOWHERE, THE BLUE, THIN AIR
* **Level 3 (ENDING IN CANDY BRANDS MINUS "S") [Type: WORDPLAY_TRANSFORM]:** BURGER KING WHOPPER, FILM NERD, MEMENTO, PITCHER'S MOUND

### Top Candidate Partitions:
1. **Partition Score: 0.4888**
   - Group 1: **0.5379** | THE PENTAGON, LEFT FIELD, FIRST BASE, HOME PLATE                  | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 2: **0.5118** | FILM NERD, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 3: **0.4911** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 4: **0.4688** | MAKING OUT, NECKING, TONSIL HOCKEY, PITCHER'S MOUND               | INCORRECT (Max overlap: 3/4 with CANOODLING) | [Pred Type: SEMANTIC_SET (49.4%, no-rel 12.6%)]
2. **Partition Score: 0.4878**
   - Group 1: **0.5213** | LEFT FIELD, FIRST BASE, HOME PLATE, JEANS BACK POCKET             | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS) | [Pred Type: SEMANTIC_SET (47.4%, no-rel 15.0%)]
   - Group 2: **0.5165** | THE PENTAGON, FILM NERD, BURGER KING WHOPPER, SCHOOL CROSSING SIGN | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 3: **0.4911** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 4: **0.4688** | MAKING OUT, NECKING, TONSIL HOCKEY, PITCHER'S MOUND               | INCORRECT (Max overlap: 3/4 with CANOODLING) | [Pred Type: SEMANTIC_SET (49.4%, no-rel 12.6%)]
3. **Partition Score: 0.4873**
   - Group 1: **0.6228** | LEFT FIELD, FIRST BASE, HOME PLATE, PITCHER'S MOUND               | INCORRECT (Max overlap: 1/4 with UNEXPECTED PLACES TO BE "OUT OF") | [Pred Type: SEMANTIC_SET (49.0%, no-rel 15.9%)]
   - Group 2: **0.5140** | THE PENTAGON, FILM NERD, BURGER KING WHOPPER, JEANS BACK POCKET   | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 3: **0.4911** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 4: **0.4463** | MAKING OUT, NECKING, TONSIL HOCKEY, SCHOOL CROSSING SIGN          | INCORRECT (Max overlap: 3/4 with CANOODLING) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 11.4%)]
4. **Partition Score: 0.4872**
   - Group 1: **0.5195** | LEFT FIELD, FIRST BASE, HOME PLATE, SCHOOL CROSSING SIGN          | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS) | [Pred Type: SEMANTIC_SET (47.8%, no-rel 14.9%)]
   - Group 2: **0.5140** | THE PENTAGON, FILM NERD, BURGER KING WHOPPER, JEANS BACK POCKET   | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 3: **0.4911** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 4: **0.4688** | MAKING OUT, NECKING, TONSIL HOCKEY, PITCHER'S MOUND               | INCORRECT (Max overlap: 3/4 with CANOODLING) | [Pred Type: SEMANTIC_SET (49.4%, no-rel 12.6%)]
5. **Partition Score: 0.4867**
   - Group 1: **0.6228** | LEFT FIELD, FIRST BASE, HOME PLATE, PITCHER'S MOUND               | INCORRECT (Max overlap: 1/4 with UNEXPECTED PLACES TO BE "OUT OF") | [Pred Type: SEMANTIC_SET (49.0%, no-rel 15.9%)]
   - Group 2: **0.5165** | THE PENTAGON, FILM NERD, BURGER KING WHOPPER, SCHOOL CROSSING SIGN | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 3: **0.4911** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 4: **0.4444** | MAKING OUT, NECKING, TONSIL HOCKEY, JEANS BACK POCKET             | INCORRECT (Max overlap: 3/4 with CANOODLING) | [Pred Type: SEMANTIC_SET (50.0%, no-rel 11.6%)]

### Top Candidate Groups:
   - Group 1: **0.5379** | THE PENTAGON, LEFT FIELD, FIRST BASE, HOME PLATE                  | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 2: **0.5118** | FILM NERD, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 3: **0.4911** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 4: **0.4688** | MAKING OUT, NECKING, TONSIL HOCKEY, PITCHER'S MOUND               | INCORRECT (Max overlap: 3/4 with CANOODLING) | [Pred Type: SEMANTIC_SET (49.4%, no-rel 12.6%)]
   - Group 5: **0.5213** | LEFT FIELD, FIRST BASE, HOME PLATE, JEANS BACK POCKET             | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS) | [Pred Type: SEMANTIC_SET (47.4%, no-rel 15.0%)]
   - Group 6: **0.5165** | THE PENTAGON, FILM NERD, BURGER KING WHOPPER, SCHOOL CROSSING SIGN | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 7: **0.6228** | LEFT FIELD, FIRST BASE, HOME PLATE, PITCHER'S MOUND               | INCORRECT (Max overlap: 1/4 with UNEXPECTED PLACES TO BE "OUT OF") | [Pred Type: SEMANTIC_SET (49.0%, no-rel 15.9%)]
   - Group 8: **0.5140** | THE PENTAGON, FILM NERD, BURGER KING WHOPPER, JEANS BACK POCKET   | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 9: **0.4463** | MAKING OUT, NECKING, TONSIL HOCKEY, SCHOOL CROSSING SIGN          | INCORRECT (Max overlap: 3/4 with CANOODLING) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 11.4%)]
   - Group 10: **0.5195** | LEFT FIELD, FIRST BASE, HOME PLATE, SCHOOL CROSSING SIGN          | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS) | [Pred Type: SEMANTIC_SET (47.8%, no-rel 14.9%)]
   - Group 11: **0.4444** | MAKING OUT, NECKING, TONSIL HOCKEY, JEANS BACK POCKET             | INCORRECT (Max overlap: 3/4 with CANOODLING) | [Pred Type: SEMANTIC_SET (50.0%, no-rel 11.6%)]
   - Group 12: **0.5015** | THE PENTAGON, LEFT FIELD, FIRST BASE, PITCHER'S MOUND             | INCORRECT (Max overlap: 1/4 with FIVE-SIDED THINGS)
   - Group 13: **0.4706** | MAKING OUT, NECKING, HOME PLATE, TONSIL HOCKEY                    | INCORRECT (Max overlap: 3/4 with CANOODLING)
   - Group 14: **0.5450** | THE PENTAGON, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 3/4 with FIVE-SIDED THINGS)
   - Group 15: **0.4850** | FILM NERD, LEFT FIELD, FIRST BASE, HOME PLATE                     | INCORRECT (Max overlap: 1/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 16: **0.4742** | FILM NERD, LEFT FIELD, FIRST BASE, PITCHER'S MOUND                | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 17: **0.4905** | LEFT FIELD, FIRST BASE, PITCHER'S MOUND, JEANS BACK POCKET        | INCORRECT (Max overlap: 1/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 18: **0.4812** | LEFT FIELD, THE BLUE, FIRST BASE, HOME PLATE                      | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 19: **0.4810** | FILM NERD, MEMENTO, NOWHERE, THIN AIR                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 20: **0.4948** | THE PENTAGON, NOWHERE, BURGER KING WHOPPER, JEANS BACK POCKET     | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)

---

## Puzzle 39 (ID: 236)
**Words on Board:** BREAK, DRIFT, RECESS, HOLY, HOLLY, DOG, HOLEY, HOLI, BUCKLE, LEAVE, LOOP, HOLIDAY, HOLE, SANDAL, STRAP, WHOLLY

### Ground Truth Categories:
* **Level 0 (TIME OFF) [Type: SYNONYM_OR_NEAR]:** BREAK, HOLIDAY, LEAVE, RECESS
* **Level 1 (FEATURES OF A BELT) [Type: SEMANTIC_SET]:** BUCKLE, HOLE, LOOP, STRAP
* **Level 2 (HOMOPHONES) [Type: SOUND_OR_SPELLING]:** HOLEY, HOLI, HOLY, WHOLLY
* **Level 3 (___WOOD) [Type: FILL_IN_THE_BLANK]:** DOG, DRIFT, HOLLY, SANDAL

### Top Candidate Partitions:
1. **Partition Score: 0.5196**
   - Group 1: **0.5342** | HOLLY, DOG, HOLI, SANDAL                                          | INCORRECT (Max overlap: 3/4 with ___WOOD)
   - Group 2: **0.5272** | BREAK, RECESS, LEAVE, HOLIDAY                                     | CORRECT GROUP (TIME OFF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 30.2%)]
   - Group 3: **0.5256** | HOLY, HOLEY, HOLE, WHOLLY                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 4: **0.5115** | DRIFT, BUCKLE, LOOP, STRAP                                        | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
2. **Partition Score: 0.4973**
   - Group 1: **0.5342** | HOLLY, DOG, HOLI, SANDAL                                          | INCORRECT (Max overlap: 3/4 with ___WOOD)
   - Group 2: **0.5256** | HOLY, HOLEY, HOLE, WHOLLY                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 3: **0.5163** | BREAK, DRIFT, LEAVE, HOLIDAY                                      | INCORRECT (Max overlap: 3/4 with TIME OFF)
   - Group 4: **0.4720** | RECESS, BUCKLE, LOOP, STRAP                                       | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
3. **Partition Score: 0.4797**
   - Group 1: **0.5342** | HOLLY, DOG, HOLI, SANDAL                                          | INCORRECT (Max overlap: 3/4 with ___WOOD)
   - Group 2: **0.5256** | HOLY, HOLEY, HOLE, WHOLLY                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 3: **0.5043** | BREAK, DRIFT, RECESS, LEAVE                                       | INCORRECT (Max overlap: 3/4 with TIME OFF)
   - Group 4: **0.4420** | BUCKLE, LOOP, HOLIDAY, STRAP                                      | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
4. **Partition Score: 0.4786**
   - Group 1: **0.5342** | HOLLY, DOG, HOLI, SANDAL                                          | INCORRECT (Max overlap: 3/4 with ___WOOD)
   - Group 2: **0.5043** | BREAK, DRIFT, RECESS, LEAVE                                       | INCORRECT (Max overlap: 3/4 with TIME OFF)
   - Group 3: **0.4746** | HOLY, HOLEY, HOLIDAY, WHOLLY                                      | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 4: **0.4584** | BUCKLE, LOOP, HOLE, STRAP                                         | CORRECT GROUP (FEATURES OF A BELT, Level 1)
5. **Partition Score: 0.4774**
   - Group 1: **0.5342** | HOLLY, DOG, HOLI, SANDAL                                          | INCORRECT (Max overlap: 3/4 with ___WOOD)
   - Group 2: **0.5115** | DRIFT, BUCKLE, LOOP, STRAP                                        | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
   - Group 3: **0.4746** | HOLY, HOLEY, HOLIDAY, WHOLLY                                      | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 4: **0.4534** | BREAK, RECESS, LEAVE, HOLE                                        | INCORRECT (Max overlap: 3/4 with TIME OFF) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 28.0%)]

### Top Candidate Groups:
   - Group 1: **0.5342** | HOLLY, DOG, HOLI, SANDAL                                          | INCORRECT (Max overlap: 3/4 with ___WOOD)
   - Group 2: **0.5272** | BREAK, RECESS, LEAVE, HOLIDAY                                     | CORRECT GROUP (TIME OFF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 30.2%)]
   - Group 3: **0.5256** | HOLY, HOLEY, HOLE, WHOLLY                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 4: **0.5115** | DRIFT, BUCKLE, LOOP, STRAP                                        | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
   - Group 5: **0.5163** | BREAK, DRIFT, LEAVE, HOLIDAY                                      | INCORRECT (Max overlap: 3/4 with TIME OFF)
   - Group 6: **0.4720** | RECESS, BUCKLE, LOOP, STRAP                                       | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
   - Group 7: **0.5043** | BREAK, DRIFT, RECESS, LEAVE                                       | INCORRECT (Max overlap: 3/4 with TIME OFF)
   - Group 8: **0.4420** | BUCKLE, LOOP, HOLIDAY, STRAP                                      | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
   - Group 9: **0.4746** | HOLY, HOLEY, HOLIDAY, WHOLLY                                      | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 10: **0.4584** | BUCKLE, LOOP, HOLE, STRAP                                         | CORRECT GROUP (FEATURES OF A BELT, Level 1)
   - Group 11: **0.4534** | BREAK, RECESS, LEAVE, HOLE                                        | INCORRECT (Max overlap: 3/4 with TIME OFF) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 28.0%)]
   - Group 12: **0.5420** | HOLEY, BUCKLE, LOOP, STRAP                                        | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
   - Group 13: **0.5310** | DRIFT, DOG, HOLE, SANDAL                                          | INCORRECT (Max overlap: 3/4 with ___WOOD) | [Pred Type: FILL_IN_THE_BLANK (49.0%, no-rel 21.5%)]
   - Group 14: **0.4236** | HOLY, HOLLY, HOLI, WHOLLY                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (54.2%, no-rel 12.9%)]
   - Group 15: **0.4739** | BUCKLE, LEAVE, LOOP, STRAP                                        | INCORRECT (Max overlap: 3/4 with FEATURES OF A BELT)
   - Group 16: **0.4453** | BREAK, DRIFT, RECESS, HOLIDAY                                     | INCORRECT (Max overlap: 3/4 with TIME OFF) | [Pred Type: SYNONYM_OR_NEAR (46.3%, no-rel 29.3%)]
   - Group 17: **0.4779** | DOG, HOLI, HOLE, SANDAL                                           | INCORRECT (Max overlap: 2/4 with ___WOOD)
   - Group 18: **0.4425** | HOLY, HOLLY, HOLEY, WHOLLY                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (49.7%, no-rel 13.9%)]
   - Group 19: **0.5444** | DRIFT, HOLLY, DOG, SANDAL                                         | CORRECT GROUP (___WOOD, Level 3) | [Pred Type: FILL_IN_THE_BLANK (50.6%, no-rel 22.5%)]
   - Group 20: **0.4095** | HOLY, HOLI, HOLE, WHOLLY                                          | INCORRECT (Max overlap: 3/4 with HOMOPHONES)

---

## Puzzle 40 (ID: 160)
**Words on Board:** RIDGE, LEDGE, GANDER, PEAK, PIQUE, GLANCE, ACT, FRONT, PEKE, PEEK, CRAG, GLIMPSE, CHARADE, BLUFF, CLIFF, LOOK

### Ground Truth Categories:
* **Level 0 (QUICK PEEK) [Type: SYNONYM_OR_NEAR]:** GANDER, GLANCE, GLIMPSE, LOOK
* **Level 1 (DECEIT) [Type: SYNONYM_OR_NEAR]:** ACT, BLUFF, CHARADE, FRONT
* **Level 2 (PARTS OF A MOUNTAIN) [Type: SEMANTIC_SET]:** CLIFF, CRAG, LEDGE, RIDGE
* **Level 3 (HOMOPHONES) [Type: SOUND_OR_SPELLING]:** PEAK, PEEK, PEKE, PIQUE

### Top Candidate Partitions:
1. **Partition Score: 0.4989**
   - Group 1: **0.5710** | GANDER, GLANCE, GLIMPSE, CHARADE                                  | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (65.9%, no-rel 24.7%)]
   - Group 2: **0.5362** | ACT, FRONT, BLUFF, LOOK                                           | INCORRECT (Max overlap: 3/4 with DECEIT) | [Pred Type: SYNONYM_OR_NEAR (58.3%, no-rel 33.2%)]
   - Group 3: **0.5106** | RIDGE, LEDGE, CRAG, CLIFF                                         | CORRECT GROUP (PARTS OF A MOUNTAIN, Level 2)
   - Group 4: **0.4650** | PEAK, PIQUE, PEKE, PEEK                                           | CORRECT GROUP (HOMOPHONES, Level 3)
2. **Partition Score: 0.4884**
   - Group 1: **0.5672** | GANDER, GLANCE, GLIMPSE, LOOK                                     | CORRECT GROUP (QUICK PEEK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 28.8%)]
   - Group 2: **0.5106** | RIDGE, LEDGE, CRAG, CLIFF                                         | CORRECT GROUP (PARTS OF A MOUNTAIN, Level 2)
   - Group 3: **0.4826** | ACT, FRONT, CHARADE, BLUFF                                        | CORRECT GROUP (DECEIT, Level 1)
   - Group 4: **0.4650** | PEAK, PIQUE, PEKE, PEEK                                           | CORRECT GROUP (HOMOPHONES, Level 3)
3. **Partition Score: 0.4863**
   - Group 1: **0.8590** | GLANCE, PEEK, GLIMPSE, LOOK                                       | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (65.8%, no-rel 27.9%)]
   - Group 2: **0.4958** | PEAK, PIQUE, PEKE, CRAG                                           | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 3: **0.4402** | GANDER, ACT, FRONT, CHARADE                                       | INCORRECT (Max overlap: 3/4 with DECEIT) | [Pred Type: SYNONYM_OR_NEAR (45.4%, no-rel 28.9%)]
   - Group 4: **0.4180** | RIDGE, LEDGE, BLUFF, CLIFF                                        | INCORRECT (Max overlap: 3/4 with PARTS OF A MOUNTAIN)
4. **Partition Score: 0.4846**
   - Group 1: **0.6335** | GANDER, GLANCE, PEEK, GLIMPSE                                     | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (69.7%, no-rel 23.1%)]
   - Group 2: **0.5660** | ACT, FRONT, CHARADE, LOOK                                         | INCORRECT (Max overlap: 3/4 with DECEIT) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 25.8%)]
   - Group 3: **0.4958** | PEAK, PIQUE, PEKE, CRAG                                           | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 4: **0.4180** | RIDGE, LEDGE, BLUFF, CLIFF                                        | INCORRECT (Max overlap: 3/4 with PARTS OF A MOUNTAIN)
5. **Partition Score: 0.4838**
   - Group 1: **0.6335** | GANDER, GLANCE, PEEK, GLIMPSE                                     | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (69.7%, no-rel 23.1%)]
   - Group 2: **0.5362** | ACT, FRONT, BLUFF, LOOK                                           | INCORRECT (Max overlap: 3/4 with DECEIT) | [Pred Type: SYNONYM_OR_NEAR (58.3%, no-rel 33.2%)]
   - Group 3: **0.5106** | RIDGE, LEDGE, CRAG, CLIFF                                         | CORRECT GROUP (PARTS OF A MOUNTAIN, Level 2)
   - Group 4: **0.4220** | PEAK, PIQUE, PEKE, CHARADE                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES)

### Top Candidate Groups:
   - Group 1: **0.5710** | GANDER, GLANCE, GLIMPSE, CHARADE                                  | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (65.9%, no-rel 24.7%)]
   - Group 2: **0.5362** | ACT, FRONT, BLUFF, LOOK                                           | INCORRECT (Max overlap: 3/4 with DECEIT) | [Pred Type: SYNONYM_OR_NEAR (58.3%, no-rel 33.2%)]
   - Group 3: **0.5106** | RIDGE, LEDGE, CRAG, CLIFF                                         | CORRECT GROUP (PARTS OF A MOUNTAIN, Level 2)
   - Group 4: **0.4650** | PEAK, PIQUE, PEKE, PEEK                                           | CORRECT GROUP (HOMOPHONES, Level 3)
   - Group 5: **0.5672** | GANDER, GLANCE, GLIMPSE, LOOK                                     | CORRECT GROUP (QUICK PEEK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 28.8%)]
   - Group 6: **0.4826** | ACT, FRONT, CHARADE, BLUFF                                        | CORRECT GROUP (DECEIT, Level 1)
   - Group 7: **0.8590** | GLANCE, PEEK, GLIMPSE, LOOK                                       | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (65.8%, no-rel 27.9%)]
   - Group 8: **0.4958** | PEAK, PIQUE, PEKE, CRAG                                           | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 9: **0.4402** | GANDER, ACT, FRONT, CHARADE                                       | INCORRECT (Max overlap: 3/4 with DECEIT) | [Pred Type: SYNONYM_OR_NEAR (45.4%, no-rel 28.9%)]
   - Group 10: **0.4180** | RIDGE, LEDGE, BLUFF, CLIFF                                        | INCORRECT (Max overlap: 3/4 with PARTS OF A MOUNTAIN)
   - Group 11: **0.6335** | GANDER, GLANCE, PEEK, GLIMPSE                                     | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (69.7%, no-rel 23.1%)]
   - Group 12: **0.5660** | ACT, FRONT, CHARADE, LOOK                                         | INCORRECT (Max overlap: 3/4 with DECEIT) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 25.8%)]
   - Group 13: **0.4220** | PEAK, PIQUE, PEKE, CHARADE                                        | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 14: **0.5112** | ACT, CHARADE, BLUFF, LOOK                                         | INCORRECT (Max overlap: 3/4 with DECEIT)
   - Group 15: **0.4707** | GANDER, GLANCE, FRONT, GLIMPSE                                    | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (65.6%, no-rel 25.5%)]
   - Group 16: **0.4550** | GANDER, GLANCE, GLIMPSE, BLUFF                                    | INCORRECT (Max overlap: 3/4 with QUICK PEEK) | [Pred Type: SYNONYM_OR_NEAR (66.7%, no-rel 24.9%)]
   - Group 17: **0.4490** | RIDGE, PEAK, PIQUE, PEKE                                          | INCORRECT (Max overlap: 3/4 with HOMOPHONES)
   - Group 18: **0.4171** | LEDGE, CRAG, BLUFF, CLIFF                                         | INCORRECT (Max overlap: 3/4 with PARTS OF A MOUNTAIN)
   - Group 19: **0.4359** | RIDGE, LEDGE, PEAK, CLIFF                                         | INCORRECT (Max overlap: 3/4 with PARTS OF A MOUNTAIN)
   - Group 20: **0.4352** | PIQUE, PEKE, CRAG, CHARADE                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES)

---

## Puzzle 41 (ID: 672)
**Words on Board:** LATE, CAPER, ELDER, EXCUSED, TYPEWRITER, LOGAN, PRESENT, GOOSE, ABSENT, ROMAN, GOTHIC, POCKET, SANS, SWIPE, PINCH, NICK

### Ground Truth Categories:
* **Level 0 (STEAL) [Type: SYNONYM_OR_NEAR]:** NICK, PINCH, POCKET, SWIPE
* **Level 1 (ATTENDANCE STATUS) [Type: SEMANTIC_SET]:** ABSENT, EXCUSED, LATE, PRESENT
* **Level 2 (FONT-MODIFYING WORDS) [Type: SEMANTIC_SET]:** GOTHIC, ROMAN, SANS, TYPEWRITER
* **Level 3 (___BERRY) [Type: FILL_IN_THE_BLANK]:** CAPER, ELDER, GOOSE, LOGAN

### Top Candidate Partitions:
1. **Partition Score: 0.5142**
   - Group 1: **0.6550** | LATE, EXCUSED, PRESENT, ABSENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 34.9%)]
   - Group 2: **0.5510** | ELDER, TYPEWRITER, LOGAN, GOOSE                                   | INCORRECT (Max overlap: 3/4 with ___BERRY)
   - Group 3: **0.5435** | ROMAN, GOTHIC, SANS, NICK                                         | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 4: **0.4591** | CAPER, POCKET, SWIPE, PINCH                                       | INCORRECT (Max overlap: 3/4 with STEAL)
2. **Partition Score: 0.5023**
   - Group 1: **0.6550** | LATE, EXCUSED, PRESENT, ABSENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 34.9%)]
   - Group 2: **0.5415** | LOGAN, ROMAN, GOTHIC, SANS                                        | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 3: **0.4894** | ELDER, TYPEWRITER, GOOSE, NICK                                    | INCORRECT (Max overlap: 2/4 with ___BERRY)
   - Group 4: **0.4591** | CAPER, POCKET, SWIPE, PINCH                                       | INCORRECT (Max overlap: 3/4 with STEAL)
3. **Partition Score: 0.5017**
   - Group 1: **0.6550** | LATE, EXCUSED, PRESENT, ABSENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 34.9%)]
   - Group 2: **0.5409** | ELDER, LOGAN, GOOSE, ROMAN                                        | INCORRECT (Max overlap: 3/4 with ___BERRY)
   - Group 3: **0.4868** | TYPEWRITER, GOTHIC, SANS, NICK                                    | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 4: **0.4591** | CAPER, POCKET, SWIPE, PINCH                                       | INCORRECT (Max overlap: 3/4 with STEAL)
4. **Partition Score: 0.5014**
   - Group 1: **0.6550** | LATE, EXCUSED, PRESENT, ABSENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 34.9%)]
   - Group 2: **0.5435** | ROMAN, GOTHIC, SANS, NICK                                         | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 3: **0.4670** | TYPEWRITER, POCKET, SWIPE, PINCH                                  | INCORRECT (Max overlap: 3/4 with STEAL)
   - Group 4: **0.4649** | CAPER, ELDER, LOGAN, GOOSE                                        | CORRECT GROUP (___BERRY, Level 3)
5. **Partition Score: 0.5004**
   - Group 1: **0.6550** | LATE, EXCUSED, PRESENT, ABSENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 34.9%)]
   - Group 2: **0.5399** | TYPEWRITER, LOGAN, GOOSE, NICK                                    | INCORRECT (Max overlap: 2/4 with ___BERRY)
   - Group 3: **0.4810** | ELDER, ROMAN, GOTHIC, SANS                                        | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 4: **0.4591** | CAPER, POCKET, SWIPE, PINCH                                       | INCORRECT (Max overlap: 3/4 with STEAL)

### Top Candidate Groups:
   - Group 1: **0.6550** | LATE, EXCUSED, PRESENT, ABSENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 34.9%)]
   - Group 2: **0.5510** | ELDER, TYPEWRITER, LOGAN, GOOSE                                   | INCORRECT (Max overlap: 3/4 with ___BERRY)
   - Group 3: **0.5435** | ROMAN, GOTHIC, SANS, NICK                                         | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 4: **0.4591** | CAPER, POCKET, SWIPE, PINCH                                       | INCORRECT (Max overlap: 3/4 with STEAL)
   - Group 5: **0.5415** | LOGAN, ROMAN, GOTHIC, SANS                                        | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 6: **0.4894** | ELDER, TYPEWRITER, GOOSE, NICK                                    | INCORRECT (Max overlap: 2/4 with ___BERRY)
   - Group 7: **0.5409** | ELDER, LOGAN, GOOSE, ROMAN                                        | INCORRECT (Max overlap: 3/4 with ___BERRY)
   - Group 8: **0.4868** | TYPEWRITER, GOTHIC, SANS, NICK                                    | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 9: **0.4670** | TYPEWRITER, POCKET, SWIPE, PINCH                                  | INCORRECT (Max overlap: 3/4 with STEAL)
   - Group 10: **0.4649** | CAPER, ELDER, LOGAN, GOOSE                                        | CORRECT GROUP (___BERRY, Level 3)
   - Group 11: **0.5399** | TYPEWRITER, LOGAN, GOOSE, NICK                                    | INCORRECT (Max overlap: 2/4 with ___BERRY)
   - Group 12: **0.4810** | ELDER, ROMAN, GOTHIC, SANS                                        | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 13: **0.5342** | ELDER, LOGAN, GOOSE, NICK                                         | INCORRECT (Max overlap: 3/4 with ___BERRY)
   - Group 14: **0.4837** | TYPEWRITER, ROMAN, GOTHIC, SANS                                   | CORRECT GROUP (FONT-MODIFYING WORDS, Level 2)
   - Group 15: **0.5001** | POCKET, SWIPE, PINCH, NICK                                        | CORRECT GROUP (STEAL, Level 0)
   - Group 16: **0.5073** | ELDER, TYPEWRITER, LOGAN, NICK                                    | INCORRECT (Max overlap: 2/4 with ___BERRY)
   - Group 17: **0.4908** | GOOSE, ROMAN, GOTHIC, SANS                                        | INCORRECT (Max overlap: 3/4 with FONT-MODIFYING WORDS)
   - Group 18: **0.4787** | ROMAN, POCKET, SWIPE, PINCH                                       | INCORRECT (Max overlap: 3/4 with STEAL)
   - Group 19: **0.4902** | ELDER, GOOSE, ROMAN, GOTHIC                                       | INCORRECT (Max overlap: 2/4 with ___BERRY)
   - Group 20: **0.4844** | TYPEWRITER, LOGAN, SANS, NICK                                     | INCORRECT (Max overlap: 2/4 with FONT-MODIFYING WORDS)

---

## Puzzle 42 (ID: 196)
**Words on Board:** TORCH, EYELASH, DANDELION, MILD, SHOULDER, CROWN, ROBE, BELLY, MELLOW, CHOP, TABLET, HOCK, DICE, SOFT, CANDLE, LIGHT

### Ground Truth Categories:
* **Level 0 (GENTLE) [Type: SYNONYM_OR_NEAR]:** LIGHT, MELLOW, MILD, SOFT
* **Level 1 (CUTS OF PORK) [Type: SEMANTIC_SET]:** BELLY, CHOP, HOCK, SHOULDER
* **Level 2 (STATUE OF LIBERTY FEATURES) [Type: SEMANTIC_SET]:** CROWN, ROBE, TABLET, TORCH
* **Level 3 (THINGS TO BLOW ON FOR WISHES/LUCK) [Type: SEMANTIC_SET]:** CANDLE, DANDELION, DICE, EYELASH

### Top Candidate Partitions:
1. **Partition Score: 0.4889**
   - Group 1: **0.5684** | TORCH, CROWN, CANDLE, LIGHT                                       | INCORRECT (Max overlap: 2/4 with STATUE OF LIBERTY FEATURES) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 22.8%)]
   - Group 2: **0.5222** | EYELASH, DANDELION, ROBE, TABLET                                  | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK)
   - Group 3: **0.4736** | MILD, MELLOW, DICE, SOFT                                          | INCORRECT (Max overlap: 3/4 with GENTLE) | [Pred Type: SYNONYM_OR_NEAR (51.9%, no-rel 34.8%)]
   - Group 4: **0.4648** | SHOULDER, BELLY, CHOP, HOCK                                       | CORRECT GROUP (CUTS OF PORK, Level 1)
2. **Partition Score: 0.4837**
   - Group 1: **0.5482** | EYELASH, CROWN, ROBE, TABLET                                      | INCORRECT (Max overlap: 3/4 with STATUE OF LIBERTY FEATURES)
   - Group 2: **0.5065** | TORCH, DANDELION, CANDLE, LIGHT                                   | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK) | [Pred Type: SYNONYM_OR_NEAR (50.0%, no-rel 16.7%)]
   - Group 3: **0.4736** | MILD, MELLOW, DICE, SOFT                                          | INCORRECT (Max overlap: 3/4 with GENTLE) | [Pred Type: SYNONYM_OR_NEAR (51.9%, no-rel 34.8%)]
   - Group 4: **0.4648** | SHOULDER, BELLY, CHOP, HOCK                                       | CORRECT GROUP (CUTS OF PORK, Level 1)
3. **Partition Score: 0.4827**
   - Group 1: **0.5078** | EYELASH, ROBE, TABLET, HOCK                                       | INCORRECT (Max overlap: 2/4 with STATUE OF LIBERTY FEATURES)
   - Group 2: **0.5065** | TORCH, DANDELION, CANDLE, LIGHT                                   | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK) | [Pred Type: SYNONYM_OR_NEAR (50.0%, no-rel 16.7%)]
   - Group 3: **0.4736** | MILD, MELLOW, DICE, SOFT                                          | INCORRECT (Max overlap: 3/4 with GENTLE) | [Pred Type: SYNONYM_OR_NEAR (51.9%, no-rel 34.8%)]
   - Group 4: **0.4718** | SHOULDER, CROWN, BELLY, CHOP                                      | INCORRECT (Max overlap: 3/4 with CUTS OF PORK)
4. **Partition Score: 0.4794**
   - Group 1: **0.5268** | EYELASH, DANDELION, CROWN, TABLET                                 | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK)
   - Group 2: **0.4965** | TORCH, ROBE, CANDLE, LIGHT                                        | INCORRECT (Max overlap: 2/4 with STATUE OF LIBERTY FEATURES)
   - Group 3: **0.4736** | MILD, MELLOW, DICE, SOFT                                          | INCORRECT (Max overlap: 3/4 with GENTLE) | [Pred Type: SYNONYM_OR_NEAR (51.9%, no-rel 34.8%)]
   - Group 4: **0.4648** | SHOULDER, BELLY, CHOP, HOCK                                       | CORRECT GROUP (CUTS OF PORK, Level 1)
5. **Partition Score: 0.4742**
   - Group 1: **0.5222** | EYELASH, DANDELION, ROBE, TABLET                                  | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK)
   - Group 2: **0.4770** | MILD, CROWN, MELLOW, SOFT                                         | INCORRECT (Max overlap: 3/4 with GENTLE) | [Pred Type: SYNONYM_OR_NEAR (49.2%, no-rel 32.1%)]
   - Group 3: **0.4680** | TORCH, DICE, CANDLE, LIGHT                                        | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 16.7%)]
   - Group 4: **0.4648** | SHOULDER, BELLY, CHOP, HOCK                                       | CORRECT GROUP (CUTS OF PORK, Level 1)

### Top Candidate Groups:
   - Group 1: **0.5684** | TORCH, CROWN, CANDLE, LIGHT                                       | INCORRECT (Max overlap: 2/4 with STATUE OF LIBERTY FEATURES) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 22.8%)]
   - Group 2: **0.5222** | EYELASH, DANDELION, ROBE, TABLET                                  | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK)
   - Group 3: **0.4736** | MILD, MELLOW, DICE, SOFT                                          | INCORRECT (Max overlap: 3/4 with GENTLE) | [Pred Type: SYNONYM_OR_NEAR (51.9%, no-rel 34.8%)]
   - Group 4: **0.4648** | SHOULDER, BELLY, CHOP, HOCK                                       | CORRECT GROUP (CUTS OF PORK, Level 1)
   - Group 5: **0.5482** | EYELASH, CROWN, ROBE, TABLET                                      | INCORRECT (Max overlap: 3/4 with STATUE OF LIBERTY FEATURES)
   - Group 6: **0.5065** | TORCH, DANDELION, CANDLE, LIGHT                                   | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK) | [Pred Type: SYNONYM_OR_NEAR (50.0%, no-rel 16.7%)]
   - Group 7: **0.5078** | EYELASH, ROBE, TABLET, HOCK                                       | INCORRECT (Max overlap: 2/4 with STATUE OF LIBERTY FEATURES)
   - Group 8: **0.4718** | SHOULDER, CROWN, BELLY, CHOP                                      | INCORRECT (Max overlap: 3/4 with CUTS OF PORK)
   - Group 9: **0.5268** | EYELASH, DANDELION, CROWN, TABLET                                 | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK)
   - Group 10: **0.4965** | TORCH, ROBE, CANDLE, LIGHT                                        | INCORRECT (Max overlap: 2/4 with STATUE OF LIBERTY FEATURES)
   - Group 11: **0.4770** | MILD, CROWN, MELLOW, SOFT                                         | INCORRECT (Max overlap: 3/4 with GENTLE) | [Pred Type: SYNONYM_OR_NEAR (49.2%, no-rel 32.1%)]
   - Group 12: **0.4680** | TORCH, DICE, CANDLE, LIGHT                                        | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 16.7%)]
   - Group 13: **0.4922** | SHOULDER, CROWN, BELLY, HOCK                                      | INCORRECT (Max overlap: 3/4 with CUTS OF PORK)
   - Group 14: **0.4550** | TORCH, CHOP, CANDLE, LIGHT                                        | INCORRECT (Max overlap: 1/4 with STATUE OF LIBERTY FEATURES) | [Pred Type: SYNONYM_OR_NEAR (49.3%, no-rel 19.9%)]
   - Group 15: **0.5256** | EYELASH, SHOULDER, BELLY, HOCK                                    | INCORRECT (Max overlap: 3/4 with CUTS OF PORK)
   - Group 16: **0.4895** | DANDELION, CROWN, ROBE, TABLET                                    | INCORRECT (Max overlap: 3/4 with STATUE OF LIBERTY FEATURES)
   - Group 17: **0.4835** | TORCH, EYELASH, CANDLE, LIGHT                                     | INCORRECT (Max overlap: 2/4 with THINGS TO BLOW ON FOR WISHES/LUCK) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 16.0%)]
   - Group 18: **0.4462** | MILD, MELLOW, HOCK, SOFT                                          | INCORRECT (Max overlap: 3/4 with GENTLE) | [Pred Type: SYNONYM_OR_NEAR (51.4%, no-rel 27.4%)]
   - Group 19: **0.4432** | SHOULDER, BELLY, CHOP, DICE                                       | INCORRECT (Max overlap: 3/4 with CUTS OF PORK) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 18.4%)]
   - Group 20: **0.5826** | MILD, MELLOW, SOFT, LIGHT                                         | CORRECT GROUP (GENTLE, Level 0)

---

## Puzzle 43 (ID: 326)
**Words on Board:** JOKER, SOULMATE, POPCORN, GLADIATOR, JACK, SIGNS, EXPERT, RAPTURE, HER, CRACKERJACK, TIRE, ROCKETRY, ACE, CHOCK, WRENCH, HOTSHOT

### Ground Truth Categories:
* **Level 0 (HIGHLY SKILLED) [Type: SYNONYM_OR_NEAR]:** ACE, CRACKERJACK, EXPERT, HOTSHOT
* **Level 1 (USED TO FIX A FLAT) [Type: SEMANTIC_SET]:** CHOCK, JACK, TIRE, WRENCH
* **Level 2 (JOAQUIN PHOENIX MOVIES) [Type: NAMED_ENTITY_SET]:** GLADIATOR, HER, JOKER, SIGNS
* **Level 3 (WORDS STARTING WITH MUSIC GENRES) [Type: WORD_FORM]:** POPCORN, RAPTURE, ROCKETRY, SOULMATE

### Top Candidate Partitions:
1. **Partition Score: 0.5217**
   - Group 1: **0.6255** | EXPERT, ACE, CHOCK, HOTSHOT                                       | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (74.4%, no-rel 18.1%)]
   - Group 2: **0.5355** | SOULMATE, GLADIATOR, RAPTURE, HER                                 | INCORRECT (Max overlap: 2/4 with WORDS STARTING WITH MUSIC GENRES)
   - Group 3: **0.5162** | SIGNS, TIRE, ROCKETRY, WRENCH                                     | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
   - Group 4: **0.4958** | JOKER, POPCORN, JACK, CRACKERJACK                                 | INCORRECT (Max overlap: 1/4 with JOAQUIN PHOENIX MOVIES)
2. **Partition Score: 0.5180**
   - Group 1: **0.5787** | JOKER, EXPERT, ACE, HOTSHOT                                       | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (76.5%, no-rel 11.8%)]
   - Group 2: **0.5355** | SOULMATE, GLADIATOR, RAPTURE, HER                                 | INCORRECT (Max overlap: 2/4 with WORDS STARTING WITH MUSIC GENRES)
   - Group 3: **0.5162** | SIGNS, TIRE, ROCKETRY, WRENCH                                     | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
   - Group 4: **0.4989** | POPCORN, JACK, CRACKERJACK, CHOCK                                 | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
3. **Partition Score: 0.5138**
   - Group 1: **0.5787** | JOKER, EXPERT, ACE, HOTSHOT                                       | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (76.5%, no-rel 11.8%)]
   - Group 2: **0.5355** | SOULMATE, GLADIATOR, RAPTURE, HER                                 | INCORRECT (Max overlap: 2/4 with WORDS STARTING WITH MUSIC GENRES)
   - Group 3: **0.5032** | SIGNS, TIRE, ROCKETRY, CHOCK                                      | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
   - Group 4: **0.4956** | POPCORN, JACK, CRACKERJACK, WRENCH                                | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
4. **Partition Score: 0.5083**
   - Group 1: **0.5355** | SOULMATE, GLADIATOR, RAPTURE, HER                                 | INCORRECT (Max overlap: 2/4 with WORDS STARTING WITH MUSIC GENRES)
   - Group 2: **0.5231** | SIGNS, EXPERT, ACE, HOTSHOT                                       | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (76.5%, no-rel 14.3%)]
   - Group 3: **0.5056** | JACK, TIRE, CHOCK, WRENCH                                         | CORRECT GROUP (USED TO FIX A FLAT, Level 1)
   - Group 4: **0.4978** | JOKER, POPCORN, CRACKERJACK, ROCKETRY                             | INCORRECT (Max overlap: 2/4 with WORDS STARTING WITH MUSIC GENRES)
5. **Partition Score: 0.5066**
   - Group 1: **0.6255** | EXPERT, ACE, CHOCK, HOTSHOT                                       | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (74.4%, no-rel 18.1%)]
   - Group 2: **0.5355** | SOULMATE, GLADIATOR, RAPTURE, HER                                 | INCORRECT (Max overlap: 2/4 with WORDS STARTING WITH MUSIC GENRES)
   - Group 3: **0.4956** | POPCORN, JACK, CRACKERJACK, WRENCH                                | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
   - Group 4: **0.4739** | JOKER, SIGNS, TIRE, ROCKETRY                                      | INCORRECT (Max overlap: 2/4 with JOAQUIN PHOENIX MOVIES) | [Pred Type: NAMED_ENTITY_SET (50.0%, no-rel 16.3%)]

### Top Candidate Groups:
   - Group 1: **0.6255** | EXPERT, ACE, CHOCK, HOTSHOT                                       | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (74.4%, no-rel 18.1%)]
   - Group 2: **0.5355** | SOULMATE, GLADIATOR, RAPTURE, HER                                 | INCORRECT (Max overlap: 2/4 with WORDS STARTING WITH MUSIC GENRES)
   - Group 3: **0.5162** | SIGNS, TIRE, ROCKETRY, WRENCH                                     | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
   - Group 4: **0.4958** | JOKER, POPCORN, JACK, CRACKERJACK                                 | INCORRECT (Max overlap: 1/4 with JOAQUIN PHOENIX MOVIES)
   - Group 5: **0.5787** | JOKER, EXPERT, ACE, HOTSHOT                                       | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (76.5%, no-rel 11.8%)]
   - Group 6: **0.4989** | POPCORN, JACK, CRACKERJACK, CHOCK                                 | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
   - Group 7: **0.5032** | SIGNS, TIRE, ROCKETRY, CHOCK                                      | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
   - Group 8: **0.4956** | POPCORN, JACK, CRACKERJACK, WRENCH                                | INCORRECT (Max overlap: 2/4 with USED TO FIX A FLAT)
   - Group 9: **0.5231** | SIGNS, EXPERT, ACE, HOTSHOT                                       | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (76.5%, no-rel 14.3%)]
   - Group 10: **0.5056** | JACK, TIRE, CHOCK, WRENCH                                         | CORRECT GROUP (USED TO FIX A FLAT, Level 1)
   - Group 11: **0.4978** | JOKER, POPCORN, CRACKERJACK, ROCKETRY                             | INCORRECT (Max overlap: 2/4 with WORDS STARTING WITH MUSIC GENRES)
   - Group 12: **0.4739** | JOKER, SIGNS, TIRE, ROCKETRY                                      | INCORRECT (Max overlap: 2/4 with JOAQUIN PHOENIX MOVIES) | [Pred Type: NAMED_ENTITY_SET (50.0%, no-rel 16.3%)]
   - Group 13: **0.4921** | SIGNS, HER, TIRE, ROCKETRY                                        | INCORRECT (Max overlap: 2/4 with JOAQUIN PHOENIX MOVIES)
   - Group 14: **0.4886** | JOKER, SOULMATE, GLADIATOR, RAPTURE                               | INCORRECT (Max overlap: 2/4 with JOAQUIN PHOENIX MOVIES) | [Pred Type: NAMED_ENTITY_SET (49.1%, no-rel 23.6%)]
   - Group 15: **0.5267** | JACK, CRACKERJACK, CHOCK, WRENCH                                  | INCORRECT (Max overlap: 3/4 with USED TO FIX A FLAT)
   - Group 16: **0.4870** | SOULMATE, POPCORN, GLADIATOR, RAPTURE                             | INCORRECT (Max overlap: 3/4 with WORDS STARTING WITH MUSIC GENRES)
   - Group 17: **0.5123** | EXPERT, ACE, WRENCH, HOTSHOT                                      | INCORRECT (Max overlap: 3/4 with HIGHLY SKILLED) | [Pred Type: SYNONYM_OR_NEAR (73.8%, no-rel 14.1%)]
   - Group 18: **0.4928** | TIRE, ROCKETRY, CHOCK, WRENCH                                     | INCORRECT (Max overlap: 3/4 with USED TO FIX A FLAT)
   - Group 19: **0.6107** | EXPERT, CRACKERJACK, ACE, HOTSHOT                                 | CORRECT GROUP (HIGHLY SKILLED, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.0%, no-rel 15.2%)]
   - Group 20: **0.4679** | JOKER, POPCORN, SIGNS, ROCKETRY                                   | INCORRECT (Max overlap: 2/4 with JOAQUIN PHOENIX MOVIES) | [Pred Type: NAMED_ENTITY_SET (51.5%, no-rel 15.8%)]

---

## Puzzle 44 (ID: 410)
**Words on Board:** PARCHMENT, BURRITO, WAX, FACULTY, TALENT, MODERATE, FLAIR, PRESENT, GIFT, PAPYRUS, HOST, MUMMY, CLAY, SPRAIN, INSTINCT, ANCHOR

### Ground Truth Categories:
* **Level 0 (ANCIENT WRITING SURFACES) [Type: SEMANTIC_SET]:** CLAY, PAPYRUS, PARCHMENT, WAX
* **Level 1 (LEAD, AS A TV PROGRAM) [Type: SYNONYM_OR_NEAR]:** ANCHOR, HOST, MODERATE, PRESENT
* **Level 2 (NATURAL ABILITY) [Type: SYNONYM_OR_NEAR]:** FACULTY, FLAIR, INSTINCT, TALENT
* **Level 3 (WRAPPED THINGS) [Type: SEMANTIC_SET]:** BURRITO, GIFT, MUMMY, SPRAIN

### Top Candidate Partitions:
1. **Partition Score: 0.5196**
   - Group 1: **0.6663** | TALENT, FLAIR, PRESENT, GIFT                                      | INCORRECT (Max overlap: 2/4 with NATURAL ABILITY) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 36.4%)]
   - Group 2: **0.5316** | PARCHMENT, PAPYRUS, MUMMY, CLAY                                   | INCORRECT (Max overlap: 3/4 with ANCIENT WRITING SURFACES)
   - Group 3: **0.4982** | BURRITO, WAX, SPRAIN, INSTINCT                                    | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 4: **0.4909** | FACULTY, MODERATE, HOST, ANCHOR                                   | INCORRECT (Max overlap: 3/4 with LEAD, AS A TV PROGRAM)
2. **Partition Score: 0.5185**
   - Group 1: **0.6663** | TALENT, FLAIR, PRESENT, GIFT                                      | INCORRECT (Max overlap: 2/4 with NATURAL ABILITY) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 36.4%)]
   - Group 2: **0.5217** | PARCHMENT, PAPYRUS, SPRAIN, INSTINCT                              | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 3: **0.5018** | BURRITO, WAX, MUMMY, CLAY                                         | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 4: **0.4909** | FACULTY, MODERATE, HOST, ANCHOR                                   | INCORRECT (Max overlap: 3/4 with LEAD, AS A TV PROGRAM)
3. **Partition Score: 0.5158**
   - Group 1: **0.6663** | TALENT, FLAIR, PRESENT, GIFT                                      | INCORRECT (Max overlap: 2/4 with NATURAL ABILITY) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 36.4%)]
   - Group 2: **0.5092** | PARCHMENT, BURRITO, PAPYRUS, INSTINCT                             | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 3: **0.5001** | WAX, MUMMY, CLAY, SPRAIN                                          | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 4: **0.4909** | FACULTY, MODERATE, HOST, ANCHOR                                   | INCORRECT (Max overlap: 3/4 with LEAD, AS A TV PROGRAM)
4. **Partition Score: 0.5104**
   - Group 1: **0.6663** | TALENT, FLAIR, PRESENT, GIFT                                      | INCORRECT (Max overlap: 2/4 with NATURAL ABILITY) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 36.4%)]
   - Group 2: **0.4962** | BURRITO, PAPYRUS, SPRAIN, INSTINCT                                | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 3: **0.4909** | FACULTY, MODERATE, HOST, ANCHOR                                   | INCORRECT (Max overlap: 3/4 with LEAD, AS A TV PROGRAM)
   - Group 4: **0.4886** | PARCHMENT, WAX, MUMMY, CLAY                                       | INCORRECT (Max overlap: 3/4 with ANCIENT WRITING SURFACES)
5. **Partition Score: 0.5103**
   - Group 1: **0.6663** | TALENT, FLAIR, PRESENT, GIFT                                      | INCORRECT (Max overlap: 2/4 with NATURAL ABILITY) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 36.4%)]
   - Group 2: **0.4980** | PARCHMENT, BURRITO, PAPYRUS, CLAY                                 | INCORRECT (Max overlap: 3/4 with ANCIENT WRITING SURFACES)
   - Group 3: **0.4909** | FACULTY, MODERATE, HOST, ANCHOR                                   | INCORRECT (Max overlap: 3/4 with LEAD, AS A TV PROGRAM)
   - Group 4: **0.4876** | WAX, MUMMY, SPRAIN, INSTINCT                                      | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)

### Top Candidate Groups:
   - Group 1: **0.6663** | TALENT, FLAIR, PRESENT, GIFT                                      | INCORRECT (Max overlap: 2/4 with NATURAL ABILITY) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 36.4%)]
   - Group 2: **0.5316** | PARCHMENT, PAPYRUS, MUMMY, CLAY                                   | INCORRECT (Max overlap: 3/4 with ANCIENT WRITING SURFACES)
   - Group 3: **0.4982** | BURRITO, WAX, SPRAIN, INSTINCT                                    | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 4: **0.4909** | FACULTY, MODERATE, HOST, ANCHOR                                   | INCORRECT (Max overlap: 3/4 with LEAD, AS A TV PROGRAM)
   - Group 5: **0.5217** | PARCHMENT, PAPYRUS, SPRAIN, INSTINCT                              | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 6: **0.5018** | BURRITO, WAX, MUMMY, CLAY                                         | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 7: **0.5092** | PARCHMENT, BURRITO, PAPYRUS, INSTINCT                             | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 8: **0.5001** | WAX, MUMMY, CLAY, SPRAIN                                          | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 9: **0.4962** | BURRITO, PAPYRUS, SPRAIN, INSTINCT                                | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 10: **0.4886** | PARCHMENT, WAX, MUMMY, CLAY                                       | INCORRECT (Max overlap: 3/4 with ANCIENT WRITING SURFACES)
   - Group 11: **0.4980** | PARCHMENT, BURRITO, PAPYRUS, CLAY                                 | INCORRECT (Max overlap: 3/4 with ANCIENT WRITING SURFACES)
   - Group 12: **0.4876** | WAX, MUMMY, SPRAIN, INSTINCT                                      | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 13: **0.5041** | PARCHMENT, BURRITO, PAPYRUS, SPRAIN                               | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 14: **0.4839** | WAX, MUMMY, CLAY, INSTINCT                                        | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 15: **0.5005** | PARCHMENT, PAPYRUS, CLAY, SPRAIN                                  | INCORRECT (Max overlap: 3/4 with ANCIENT WRITING SURFACES)
   - Group 16: **0.4793** | BURRITO, WAX, MUMMY, INSTINCT                                     | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 17: **0.4970** | BURRITO, PAPYRUS, MUMMY, CLAY                                     | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)
   - Group 18: **0.4758** | PARCHMENT, WAX, SPRAIN, INSTINCT                                  | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 19: **0.5048** | PARCHMENT, PAPYRUS, MUMMY, INSTINCT                               | INCORRECT (Max overlap: 2/4 with ANCIENT WRITING SURFACES)
   - Group 20: **0.4725** | BURRITO, WAX, CLAY, SPRAIN                                        | INCORRECT (Max overlap: 2/4 with WRAPPED THINGS)

---

## Puzzle 45 (ID: 118)
**Words on Board:** HANNAH, SAVANNA, CLIFF, SHARON, AARON, DREW, ROSE, EVE, WILL, DARREN, OTTO, NATAN, MAY, KAREN, DALE, BROOK

### Ground Truth Categories:
* **Level 0 (RHYMES) [Type: SOUND_OR_SPELLING]:** DARREN, KAREN, SHARON, AARON
* **Level 1 (NATURAL FEATURES) [Type: SEMANTIC_SET]:** DALE, BROOK, SAVANNA, CLIFF
* **Level 2 (IRREGULAR VERBS) [Type: SEMANTIC_SET]:** DREW, ROSE, WILL, MAY
* **Level 3 (PALINDROMES) [Type: WORD_FORM]:** EVE, HANNAH, OTTO, NATAN

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.5696** | HANNAH, SAVANNA, SHARON, DARREN                                   | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 2: **0.5629** | SHARON, AARON, DARREN, DALE                                       | INCORRECT (Max overlap: 3/4 with RHYMES) | [Pred Type: NAMED_ENTITY_SET (46.4%, no-rel 24.9%)]
   - Group 3: **0.5618** | SHARON, AARON, DARREN, KAREN                                      | CORRECT GROUP (RHYMES, Level 0)
   - Group 4: **0.5598** | HANNAH, SHARON, AARON, DARREN                                     | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 5: **0.5544** | SAVANNA, SHARON, DARREN, KAREN                                    | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 6: **0.5509** | AARON, DARREN, NATAN, KAREN                                       | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 7: **0.5482** | SAVANNA, DARREN, NATAN, KAREN                                     | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 8: **0.5474** | SAVANNA, SHARON, DARREN, NATAN                                    | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 9: **0.5431** | HANNAH, SAVANNA, AARON, DARREN                                    | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 10: **0.5375** | SHARON, DARREN, NATAN, KAREN                                      | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 11: **0.5373** | AARON, DARREN, OTTO, DALE                                         | INCORRECT (Max overlap: 2/4 with RHYMES) | [Pred Type: NAMED_ENTITY_SET (52.0%, no-rel 18.1%)]
   - Group 12: **0.5373** | HANNAH, SAVANNA, SHARON, AARON                                    | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 13: **0.5362** | SAVANNA, AARON, DARREN, KAREN                                     | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 14: **0.5355** | SHARON, AARON, NATAN, KAREN                                       | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 15: **0.5354** | SAVANNA, SHARON, AARON, DARREN                                    | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 16: **0.5351** | SHARON, AARON, DARREN, NATAN                                      | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 17: **0.5335** | HANNAH, SAVANNA, SHARON, KAREN                                    | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 18: **0.5326** | SAVANNA, CLIFF, DARREN, BROOK                                     | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES) | [Pred Type: NAMED_ENTITY_SET (46.8%, no-rel 20.8%)]
   - Group 19: **0.5317** | HANNAH, AARON, DARREN, KAREN                                      | INCORRECT (Max overlap: 3/4 with RHYMES)
   - Group 20: **0.5302** | HANNAH, SAVANNA, AARON, KAREN                                     | INCORRECT (Max overlap: 2/4 with RHYMES)

---

## Puzzle 46 (ID: 226)
**Words on Board:** POUND, CREATE, PRIME, FINE, INVENT, QUALITY, STERLING, DEVISE, TIME, BAR, DOLLAR, AT, PERCENT, BUCK, COIN, TORCH

### Ground Truth Categories:
* **Level 0 (BRING INTO BEING) [Type: SYNONYM_OR_NEAR]:** COIN, CREATE, DEVISE, INVENT
* **Level 1 (EXCELLENT) [Type: SYNONYM_OR_NEAR]:** FINE, PRIME, QUALITY, STERLING
* **Level 2 (SYMBOLS ABOVE NUMBERS ON A KEYBOARD) [Type: NAMED_ENTITY_SET]:** AT, DOLLAR, PERCENT, POUND
* **Level 3 (PASS THE ___) [Type: FILL_IN_THE_BLANK]:** BAR, BUCK, TIME, TORCH

### Top Candidate Partitions:
1. **Partition Score: 0.4817**
   - Group 1: **0.5022** | PRIME, QUALITY, STERLING, TIME                                    | INCORRECT (Max overlap: 3/4 with EXCELLENT)
   - Group 2: **0.4952** | CREATE, INVENT, DEVISE, COIN                                      | CORRECT GROUP (BRING INTO BEING, Level 0) | [Pred Type: SYNONYM_OR_NEAR (73.2%, no-rel 17.7%)]
   - Group 3: **0.4846** | POUND, DOLLAR, PERCENT, BUCK                                      | INCORRECT (Max overlap: 3/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD)
   - Group 4: **0.4711** | FINE, BAR, AT, TORCH                                              | INCORRECT (Max overlap: 2/4 with PASS THE ___)
2. **Partition Score: 0.4638**
   - Group 1: **0.4952** | CREATE, INVENT, DEVISE, COIN                                      | CORRECT GROUP (BRING INTO BEING, Level 0) | [Pred Type: SYNONYM_OR_NEAR (73.2%, no-rel 17.7%)]
   - Group 2: **0.4952** | TIME, BAR, AT, TORCH                                              | INCORRECT (Max overlap: 3/4 with PASS THE ___)
   - Group 3: **0.4846** | POUND, DOLLAR, PERCENT, BUCK                                      | INCORRECT (Max overlap: 3/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD)
   - Group 4: **0.4379** | PRIME, FINE, QUALITY, STERLING                                    | CORRECT GROUP (EXCELLENT, Level 1)
3. **Partition Score: 0.4614**
   - Group 1: **0.5102** | FINE, TIME, BAR, AT                                               | INCORRECT (Max overlap: 2/4 with PASS THE ___)
   - Group 2: **0.4952** | CREATE, INVENT, DEVISE, COIN                                      | CORRECT GROUP (BRING INTO BEING, Level 0) | [Pred Type: SYNONYM_OR_NEAR (73.2%, no-rel 17.7%)]
   - Group 3: **0.4846** | POUND, DOLLAR, PERCENT, BUCK                                      | INCORRECT (Max overlap: 3/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD)
   - Group 4: **0.4299** | PRIME, QUALITY, STERLING, TORCH                                   | INCORRECT (Max overlap: 3/4 with EXCELLENT)
4. **Partition Score: 0.4613**
   - Group 1: **0.4846** | POUND, DOLLAR, PERCENT, BUCK                                      | INCORRECT (Max overlap: 3/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD)
   - Group 2: **0.4711** | FINE, BAR, AT, TORCH                                              | INCORRECT (Max overlap: 2/4 with PASS THE ___)
   - Group 3: **0.4558** | PRIME, QUALITY, TIME, COIN                                        | INCORRECT (Max overlap: 2/4 with EXCELLENT)
   - Group 4: **0.4547** | CREATE, INVENT, STERLING, DEVISE                                  | INCORRECT (Max overlap: 3/4 with BRING INTO BEING) | [Pred Type: SYNONYM_OR_NEAR (71.5%, no-rel 18.6%)]
5. **Partition Score: 0.4567**
   - Group 1: **0.5876** | POUND, DOLLAR, BUCK, COIN                                         | INCORRECT (Max overlap: 2/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD) | [Pred Type: SYNONYM_OR_NEAR (47.0%, no-rel 23.9%)]
   - Group 2: **0.5500** | PRIME, FINE, QUALITY, TIME                                        | INCORRECT (Max overlap: 3/4 with EXCELLENT)
   - Group 3: **0.4547** | CREATE, INVENT, STERLING, DEVISE                                  | INCORRECT (Max overlap: 3/4 with BRING INTO BEING) | [Pred Type: SYNONYM_OR_NEAR (71.5%, no-rel 18.6%)]
   - Group 4: **0.3945** | BAR, AT, PERCENT, TORCH                                           | INCORRECT (Max overlap: 2/4 with PASS THE ___)

### Top Candidate Groups:
   - Group 1: **0.5022** | PRIME, QUALITY, STERLING, TIME                                    | INCORRECT (Max overlap: 3/4 with EXCELLENT)
   - Group 2: **0.4952** | CREATE, INVENT, DEVISE, COIN                                      | CORRECT GROUP (BRING INTO BEING, Level 0) | [Pred Type: SYNONYM_OR_NEAR (73.2%, no-rel 17.7%)]
   - Group 3: **0.4846** | POUND, DOLLAR, PERCENT, BUCK                                      | INCORRECT (Max overlap: 3/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD)
   - Group 4: **0.4711** | FINE, BAR, AT, TORCH                                              | INCORRECT (Max overlap: 2/4 with PASS THE ___)
   - Group 5: **0.4952** | TIME, BAR, AT, TORCH                                              | INCORRECT (Max overlap: 3/4 with PASS THE ___)
   - Group 6: **0.4379** | PRIME, FINE, QUALITY, STERLING                                    | CORRECT GROUP (EXCELLENT, Level 1)
   - Group 7: **0.5102** | FINE, TIME, BAR, AT                                               | INCORRECT (Max overlap: 2/4 with PASS THE ___)
   - Group 8: **0.4299** | PRIME, QUALITY, STERLING, TORCH                                   | INCORRECT (Max overlap: 3/4 with EXCELLENT)
   - Group 9: **0.4558** | PRIME, QUALITY, TIME, COIN                                        | INCORRECT (Max overlap: 2/4 with EXCELLENT)
   - Group 10: **0.4547** | CREATE, INVENT, STERLING, DEVISE                                  | INCORRECT (Max overlap: 3/4 with BRING INTO BEING) | [Pred Type: SYNONYM_OR_NEAR (71.5%, no-rel 18.6%)]
   - Group 11: **0.5876** | POUND, DOLLAR, BUCK, COIN                                         | INCORRECT (Max overlap: 2/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD) | [Pred Type: SYNONYM_OR_NEAR (47.0%, no-rel 23.9%)]
   - Group 12: **0.5500** | PRIME, FINE, QUALITY, TIME                                        | INCORRECT (Max overlap: 3/4 with EXCELLENT)
   - Group 13: **0.3945** | BAR, AT, PERCENT, TORCH                                           | INCORRECT (Max overlap: 2/4 with PASS THE ___)
   - Group 14: **0.4750** | CREATE, PRIME, INVENT, DEVISE                                     | INCORRECT (Max overlap: 3/4 with BRING INTO BEING) | [Pred Type: SYNONYM_OR_NEAR (68.5%, no-rel 23.8%)]
   - Group 15: **0.4646** | POUND, QUALITY, STERLING, TIME                                    | INCORRECT (Max overlap: 2/4 with EXCELLENT)
   - Group 16: **0.4437** | DOLLAR, PERCENT, BUCK, COIN                                       | INCORRECT (Max overlap: 2/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD)
   - Group 17: **0.5076** | POUND, BAR, DOLLAR, BUCK                                          | INCORRECT (Max overlap: 2/4 with SYMBOLS ABOVE NUMBERS ON A KEYBOARD)
   - Group 18: **0.4368** | TIME, AT, PERCENT, TORCH                                          | INCORRECT (Max overlap: 2/4 with PASS THE ___)
   - Group 19: **0.4823** | POUND, PRIME, QUALITY, TIME                                       | INCORRECT (Max overlap: 2/4 with EXCELLENT)
   - Group 20: **0.4468** | POUND, PRIME, QUALITY, STERLING                                   | INCORRECT (Max overlap: 3/4 with EXCELLENT) | [Pred Type: SYNONYM_OR_NEAR (55.2%, no-rel 26.8%)]

---

## Puzzle 47 (ID: 944)
**Words on Board:** DRAIN, CRASH, TANK, TEAM, PACK, CREW, BIT, FAUCET, DROP, STOPPER, SADDLE, HALTER, CROP, BASIN, CRATER, BAND

### Ground Truth Categories:
* **Level 0 (GROUP) [Type: SYNONYM_OR_NEAR]:** BAND, CREW, PACK, TEAM
* **Level 1 (PLUNGE) [Type: SYNONYM_OR_NEAR]:** CRASH, CRATER, DROP, TANK
* **Level 2 (PARTS OF A SINK) [Type: SEMANTIC_SET]:** BASIN, DRAIN, FAUCET, STOPPER
* **Level 3 (EQUESTRIAN GEAR) [Type: SEMANTIC_SET]:** BIT, CROP, HALTER, SADDLE

### Top Candidate Partitions:
1. **Partition Score: 0.4421**
   - Group 1: **0.4811** | DRAIN, TANK, BASIN, CRATER                                        | INCORRECT (Max overlap: 2/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (47.4%, no-rel 32.0%)]
   - Group 2: **0.4690** | CRASH, BIT, DROP, BAND                                            | INCORRECT (Max overlap: 2/4 with PLUNGE)
   - Group 3: **0.4499** | FAUCET, STOPPER, SADDLE, HALTER                                   | INCORRECT (Max overlap: 2/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (46.9%, no-rel 24.9%)]
   - Group 4: **0.4208** | TEAM, PACK, CREW, CROP                                            | INCORRECT (Max overlap: 3/4 with GROUP) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 28.6%)]
2. **Partition Score: 0.4414**
   - Group 1: **0.4900** | DRAIN, TANK, FAUCET, BASIN                                        | INCORRECT (Max overlap: 3/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (50.1%, no-rel 28.3%)]
   - Group 2: **0.4690** | CRASH, BIT, DROP, BAND                                            | INCORRECT (Max overlap: 2/4 with PLUNGE)
   - Group 3: **0.4409** | STOPPER, SADDLE, HALTER, CRATER                                   | INCORRECT (Max overlap: 2/4 with EQUESTRIAN GEAR)
   - Group 4: **0.4208** | TEAM, PACK, CREW, CROP                                            | INCORRECT (Max overlap: 3/4 with GROUP) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 28.6%)]
3. **Partition Score: 0.4374**
   - Group 1: **0.4900** | DRAIN, TANK, FAUCET, BASIN                                        | INCORRECT (Max overlap: 3/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (50.1%, no-rel 28.3%)]
   - Group 2: **0.4519** | CRASH, BIT, DROP, CRATER                                          | INCORRECT (Max overlap: 3/4 with PLUNGE)
   - Group 3: **0.4365** | STOPPER, SADDLE, HALTER, BAND                                     | INCORRECT (Max overlap: 2/4 with EQUESTRIAN GEAR)
   - Group 4: **0.4208** | TEAM, PACK, CREW, CROP                                            | INCORRECT (Max overlap: 3/4 with GROUP) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 28.6%)]
4. **Partition Score: 0.4355**
   - Group 1: **0.4693** | DRAIN, FAUCET, BASIN, CRATER                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (57.4%, no-rel 19.3%)]
   - Group 2: **0.4690** | CRASH, BIT, DROP, BAND                                            | INCORRECT (Max overlap: 2/4 with PLUNGE)
   - Group 3: **0.4221** | TANK, STOPPER, SADDLE, HALTER                                     | INCORRECT (Max overlap: 2/4 with EQUESTRIAN GEAR)
   - Group 4: **0.4208** | TEAM, PACK, CREW, CROP                                            | INCORRECT (Max overlap: 3/4 with GROUP) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 28.6%)]
5. **Partition Score: 0.4344**
   - Group 1: **0.4642** | DRAIN, CRASH, BIT, DROP                                           | INCORRECT (Max overlap: 2/4 with PLUNGE)
   - Group 2: **0.4518** | TANK, FAUCET, BASIN, CRATER                                       | INCORRECT (Max overlap: 2/4 with PLUNGE) | [Pred Type: SEMANTIC_SET (55.2%, no-rel 22.6%)]
   - Group 3: **0.4365** | STOPPER, SADDLE, HALTER, BAND                                     | INCORRECT (Max overlap: 2/4 with EQUESTRIAN GEAR)
   - Group 4: **0.4208** | TEAM, PACK, CREW, CROP                                            | INCORRECT (Max overlap: 3/4 with GROUP) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 28.6%)]

### Top Candidate Groups:
   - Group 1: **0.4811** | DRAIN, TANK, BASIN, CRATER                                        | INCORRECT (Max overlap: 2/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (47.4%, no-rel 32.0%)]
   - Group 2: **0.4690** | CRASH, BIT, DROP, BAND                                            | INCORRECT (Max overlap: 2/4 with PLUNGE)
   - Group 3: **0.4499** | FAUCET, STOPPER, SADDLE, HALTER                                   | INCORRECT (Max overlap: 2/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (46.9%, no-rel 24.9%)]
   - Group 4: **0.4208** | TEAM, PACK, CREW, CROP                                            | INCORRECT (Max overlap: 3/4 with GROUP) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 28.6%)]
   - Group 5: **0.4900** | DRAIN, TANK, FAUCET, BASIN                                        | INCORRECT (Max overlap: 3/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (50.1%, no-rel 28.3%)]
   - Group 6: **0.4409** | STOPPER, SADDLE, HALTER, CRATER                                   | INCORRECT (Max overlap: 2/4 with EQUESTRIAN GEAR)
   - Group 7: **0.4519** | CRASH, BIT, DROP, CRATER                                          | INCORRECT (Max overlap: 3/4 with PLUNGE)
   - Group 8: **0.4365** | STOPPER, SADDLE, HALTER, BAND                                     | INCORRECT (Max overlap: 2/4 with EQUESTRIAN GEAR)
   - Group 9: **0.4693** | DRAIN, FAUCET, BASIN, CRATER                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (57.4%, no-rel 19.3%)]
   - Group 10: **0.4221** | TANK, STOPPER, SADDLE, HALTER                                     | INCORRECT (Max overlap: 2/4 with EQUESTRIAN GEAR)
   - Group 11: **0.4642** | DRAIN, CRASH, BIT, DROP                                           | INCORRECT (Max overlap: 2/4 with PLUNGE)
   - Group 12: **0.4518** | TANK, FAUCET, BASIN, CRATER                                       | INCORRECT (Max overlap: 2/4 with PLUNGE) | [Pred Type: SEMANTIC_SET (55.2%, no-rel 22.6%)]
   - Group 13: **0.4640** | TEAM, PACK, CREW, BAND                                            | CORRECT GROUP (GROUP, Level 0)
   - Group 14: **0.4067** | CRASH, BIT, DROP, CROP                                            | INCORRECT (Max overlap: 2/4 with PLUNGE)
   - Group 15: **0.4005** | STOPPER, SADDLE, HALTER, CROP                                     | INCORRECT (Max overlap: 3/4 with EQUESTRIAN GEAR)
   - Group 16: **0.4648** | TANK, FAUCET, STOPPER, HALTER                                     | INCORRECT (Max overlap: 2/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (49.2%, no-rel 23.8%)]
   - Group 17: **0.4151** | DRAIN, SADDLE, BASIN, CRATER                                      | INCORRECT (Max overlap: 2/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (49.5%, no-rel 23.9%)]
   - Group 18: **0.4363** | DRAIN, FAUCET, STOPPER, HALTER                                    | INCORRECT (Max overlap: 3/4 with PARTS OF A SINK)
   - Group 19: **0.4216** | TANK, SADDLE, BASIN, CRATER                                       | INCORRECT (Max overlap: 2/4 with PLUNGE) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 26.7%)]
   - Group 20: **0.4439** | DRAIN, TANK, FAUCET, STOPPER                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A SINK) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 25.3%)]

---

## Puzzle 48 (ID: 330)
**Words on Board:** TIE, TOWER, SEVERAL, JOIN, BOTHER, PEST, FOOL, MANY, SOME, HANDFUL, LOVERS, FEW, PAIN, COUPLE, MAGICIAN, LINK

### Ground Truth Categories:
* **Level 0 (CONNECT) [Type: SYNONYM_OR_NEAR]:** COUPLE, JOIN, LINK, TIE
* **Level 1 (NUISANCE) [Type: SYNONYM_OR_NEAR]:** BOTHER, HANDFUL, PAIN, PEST
* **Level 2 (QUANTITY WORDS) [Type: SEMANTIC_SET]:** FEW, MANY, SEVERAL, SOME
* **Level 3 (TAROT CARDS, WITH “THE”) [Type: NAMED_ENTITY_SET]:** FOOL, LOVERS, MAGICIAN, TOWER

### Top Candidate Partitions:
1. **Partition Score: 0.5538**
   - Group 1: **0.8387** | SEVERAL, MANY, SOME, FEW                                          | CORRECT GROUP (QUANTITY WORDS, Level 2)
   - Group 2: **0.6866** | TIE, JOIN, COUPLE, LINK                                           | CORRECT GROUP (CONNECT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 35.5%)]
   - Group 3: **0.4782** | BOTHER, PEST, HANDFUL, PAIN                                       | CORRECT GROUP (NUISANCE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (49.3%, no-rel 21.0%)]
   - Group 4: **0.4703** | TOWER, FOOL, LOVERS, MAGICIAN                                     | CORRECT GROUP (TAROT CARDS, WITH “THE”, Level 3)
2. **Partition Score: 0.5359**
   - Group 1: **0.8387** | SEVERAL, MANY, SOME, FEW                                          | CORRECT GROUP (QUANTITY WORDS, Level 2)
   - Group 2: **0.6866** | TIE, JOIN, COUPLE, LINK                                           | CORRECT GROUP (CONNECT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 35.5%)]
   - Group 3: **0.4711** | BOTHER, PEST, LOVERS, PAIN                                        | INCORRECT (Max overlap: 3/4 with NUISANCE)
   - Group 4: **0.4380** | TOWER, FOOL, HANDFUL, MAGICIAN                                    | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)
3. **Partition Score: 0.5249**
   - Group 1: **0.8387** | SEVERAL, MANY, SOME, FEW                                          | CORRECT GROUP (QUANTITY WORDS, Level 2)
   - Group 2: **0.6866** | TIE, JOIN, COUPLE, LINK                                           | CORRECT GROUP (CONNECT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 35.5%)]
   - Group 3: **0.4317** | TOWER, PEST, FOOL, MAGICIAN                                       | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)
   - Group 4: **0.4309** | BOTHER, HANDFUL, LOVERS, PAIN                                     | INCORRECT (Max overlap: 3/4 with NUISANCE)
4. **Partition Score: 0.5179**
   - Group 1: **0.8387** | SEVERAL, MANY, SOME, FEW                                          | CORRECT GROUP (QUANTITY WORDS, Level 2)
   - Group 2: **0.6866** | TIE, JOIN, COUPLE, LINK                                           | CORRECT GROUP (CONNECT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 35.5%)]
   - Group 3: **0.4567** | FOOL, HANDFUL, LOVERS, MAGICIAN                                   | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)
   - Group 4: **0.4082** | TOWER, BOTHER, PEST, PAIN                                         | INCORRECT (Max overlap: 3/4 with NUISANCE)
5. **Partition Score: 0.5142**
   - Group 1: **0.8387** | SEVERAL, MANY, SOME, FEW                                          | CORRECT GROUP (QUANTITY WORDS, Level 2)
   - Group 2: **0.6866** | TIE, JOIN, COUPLE, LINK                                           | CORRECT GROUP (CONNECT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 35.5%)]
   - Group 3: **0.4613** | BOTHER, PEST, PAIN, MAGICIAN                                      | INCORRECT (Max overlap: 3/4 with NUISANCE)
   - Group 4: **0.3992** | TOWER, FOOL, HANDFUL, LOVERS                                      | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)

### Top Candidate Groups:
   - Group 1: **0.8387** | SEVERAL, MANY, SOME, FEW                                          | CORRECT GROUP (QUANTITY WORDS, Level 2)
   - Group 2: **0.6866** | TIE, JOIN, COUPLE, LINK                                           | CORRECT GROUP (CONNECT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.2%, no-rel 35.5%)]
   - Group 3: **0.4782** | BOTHER, PEST, HANDFUL, PAIN                                       | CORRECT GROUP (NUISANCE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (49.3%, no-rel 21.0%)]
   - Group 4: **0.4703** | TOWER, FOOL, LOVERS, MAGICIAN                                     | CORRECT GROUP (TAROT CARDS, WITH “THE”, Level 3)
   - Group 5: **0.4711** | BOTHER, PEST, LOVERS, PAIN                                        | INCORRECT (Max overlap: 3/4 with NUISANCE)
   - Group 6: **0.4380** | TOWER, FOOL, HANDFUL, MAGICIAN                                    | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)
   - Group 7: **0.4317** | TOWER, PEST, FOOL, MAGICIAN                                       | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)
   - Group 8: **0.4309** | BOTHER, HANDFUL, LOVERS, PAIN                                     | INCORRECT (Max overlap: 3/4 with NUISANCE)
   - Group 9: **0.4567** | FOOL, HANDFUL, LOVERS, MAGICIAN                                   | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)
   - Group 10: **0.4082** | TOWER, BOTHER, PEST, PAIN                                         | INCORRECT (Max overlap: 3/4 with NUISANCE)
   - Group 11: **0.4613** | BOTHER, PEST, PAIN, MAGICIAN                                      | INCORRECT (Max overlap: 3/4 with NUISANCE)
   - Group 12: **0.3992** | TOWER, FOOL, HANDFUL, LOVERS                                      | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)
   - Group 13: **0.4338** | TOWER, BOTHER, PEST, LOVERS                                       | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH “THE”)
   - Group 14: **0.4090** | FOOL, HANDFUL, PAIN, MAGICIAN                                     | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH “THE”)
   - Group 15: **0.4274** | PEST, FOOL, PAIN, MAGICIAN                                        | INCORRECT (Max overlap: 2/4 with NUISANCE)
   - Group 16: **0.4101** | TOWER, BOTHER, HANDFUL, LOVERS                                    | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH “THE”)
   - Group 17: **0.4228** | TOWER, PEST, HANDFUL, LOVERS                                      | INCORRECT (Max overlap: 2/4 with TAROT CARDS, WITH “THE”)
   - Group 18: **0.4102** | BOTHER, FOOL, PAIN, MAGICIAN                                      | INCORRECT (Max overlap: 2/4 with NUISANCE)
   - Group 19: **0.4506** | TOWER, HANDFUL, LOVERS, MAGICIAN                                  | INCORRECT (Max overlap: 3/4 with TAROT CARDS, WITH “THE”)
   - Group 20: **0.3965** | BOTHER, PEST, FOOL, PAIN                                          | INCORRECT (Max overlap: 3/4 with NUISANCE)

---

## Puzzle 49 (ID: 786)
**Words on Board:** HEALTH, MINCE, GRATE, SLICE, DRESS, SECRET, COAL, CARROT, SUBWAY, TUBE, UNDERGROUND, PIPE, CUBE, ZIP, METRO, SCARF

### Ground Truth Categories:
* **Level 0 (SUBTERRANEAN TRANSIT) [Type: SYNONYM_OR_NEAR]:** METRO, SUBWAY, TUBE, UNDERGROUND
* **Level 1 (MAKE INTO SMALLER PIECES WHILE COOKING) [Type: SYNONYM_OR_NEAR]:** CUBE, GRATE, MINCE, SLICE
* **Level 2 (USED TO DECORATE A SNOWMAN) [Type: SEMANTIC_SET]:** CARROT, COAL, PIPE, SCARF
* **Level 3 (___ CODE) [Type: FILL_IN_THE_BLANK]:** DRESS, HEALTH, SECRET, ZIP

### Top Candidate Partitions:
1. **Partition Score: 0.4910**
   - Group 1: **0.9401** | SUBWAY, TUBE, UNDERGROUND, METRO                                  | CORRECT GROUP (SUBTERRANEAN TRANSIT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (79.3%, no-rel 11.6%)]
   - Group 2: **0.5015** | HEALTH, SECRET, CARROT, SCARF                                     | INCORRECT (Max overlap: 2/4 with ___ CODE)
   - Group 3: **0.4402** | MINCE, SLICE, CUBE, ZIP                                           | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 4: **0.4072** | GRATE, DRESS, COAL, PIPE                                          | INCORRECT (Max overlap: 2/4 with USED TO DECORATE A SNOWMAN)
2. **Partition Score: 0.4892**
   - Group 1: **0.9401** | SUBWAY, TUBE, UNDERGROUND, METRO                                  | CORRECT GROUP (SUBTERRANEAN TRANSIT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (79.3%, no-rel 11.6%)]
   - Group 2: **0.5453** | HEALTH, DRESS, SECRET, ZIP                                        | CORRECT GROUP (___ CODE, Level 3) | [Pred Type: FILL_IN_THE_BLANK (54.0%, no-rel 19.0%)]
   - Group 3: **0.4485** | MINCE, GRATE, COAL, PIPE                                          | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 4: **0.3846** | SLICE, CARROT, CUBE, SCARF                                        | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
3. **Partition Score: 0.4889**
   - Group 1: **0.9401** | SUBWAY, TUBE, UNDERGROUND, METRO                                  | CORRECT GROUP (SUBTERRANEAN TRANSIT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (79.3%, no-rel 11.6%)]
   - Group 2: **0.5169** | HEALTH, SECRET, CARROT, ZIP                                       | INCORRECT (Max overlap: 3/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (45.5%, no-rel 20.6%)]
   - Group 3: **0.4133** | MINCE, SLICE, CUBE, SCARF                                         | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 4: **0.4072** | GRATE, DRESS, COAL, PIPE                                          | INCORRECT (Max overlap: 2/4 with USED TO DECORATE A SNOWMAN)
4. **Partition Score: 0.4873**
   - Group 1: **0.9401** | SUBWAY, TUBE, UNDERGROUND, METRO                                  | CORRECT GROUP (SUBTERRANEAN TRANSIT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (79.3%, no-rel 11.6%)]
   - Group 2: **0.5112** | HEALTH, SECRET, ZIP, SCARF                                        | INCORRECT (Max overlap: 3/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (51.8%, no-rel 21.2%)]
   - Group 3: **0.4105** | MINCE, SLICE, CARROT, CUBE                                        | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 4: **0.4072** | GRATE, DRESS, COAL, PIPE                                          | INCORRECT (Max overlap: 2/4 with USED TO DECORATE A SNOWMAN)
5. **Partition Score: 0.4817**
   - Group 1: **0.9401** | SUBWAY, TUBE, UNDERGROUND, METRO                                  | CORRECT GROUP (SUBTERRANEAN TRANSIT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (79.3%, no-rel 11.6%)]
   - Group 2: **0.5124** | HEALTH, DRESS, SECRET, SCARF                                      | INCORRECT (Max overlap: 3/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (49.1%, no-rel 21.5%)]
   - Group 3: **0.4485** | MINCE, GRATE, COAL, PIPE                                          | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 4: **0.3820** | SLICE, CARROT, CUBE, ZIP                                          | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)

### Top Candidate Groups:
   - Group 1: **0.9401** | SUBWAY, TUBE, UNDERGROUND, METRO                                  | CORRECT GROUP (SUBTERRANEAN TRANSIT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (79.3%, no-rel 11.6%)]
   - Group 2: **0.5015** | HEALTH, SECRET, CARROT, SCARF                                     | INCORRECT (Max overlap: 2/4 with ___ CODE)
   - Group 3: **0.4402** | MINCE, SLICE, CUBE, ZIP                                           | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 4: **0.4072** | GRATE, DRESS, COAL, PIPE                                          | INCORRECT (Max overlap: 2/4 with USED TO DECORATE A SNOWMAN)
   - Group 5: **0.5453** | HEALTH, DRESS, SECRET, ZIP                                        | CORRECT GROUP (___ CODE, Level 3) | [Pred Type: FILL_IN_THE_BLANK (54.0%, no-rel 19.0%)]
   - Group 6: **0.4485** | MINCE, GRATE, COAL, PIPE                                          | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 7: **0.3846** | SLICE, CARROT, CUBE, SCARF                                        | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 8: **0.5169** | HEALTH, SECRET, CARROT, ZIP                                       | INCORRECT (Max overlap: 3/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (45.5%, no-rel 20.6%)]
   - Group 9: **0.4133** | MINCE, SLICE, CUBE, SCARF                                         | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 10: **0.5112** | HEALTH, SECRET, ZIP, SCARF                                        | INCORRECT (Max overlap: 3/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (51.8%, no-rel 21.2%)]
   - Group 11: **0.4105** | MINCE, SLICE, CARROT, CUBE                                        | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 12: **0.5124** | HEALTH, DRESS, SECRET, SCARF                                      | INCORRECT (Max overlap: 3/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (49.1%, no-rel 21.5%)]
   - Group 13: **0.3820** | SLICE, CARROT, CUBE, ZIP                                          | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 14: **0.5041** | HEALTH, CARROT, ZIP, SCARF                                        | INCORRECT (Max overlap: 2/4 with ___ CODE)
   - Group 15: **0.3946** | MINCE, SLICE, SECRET, CUBE                                        | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 16: **0.5221** | GRATE, COAL, TUBE, PIPE                                           | INCORRECT (Max overlap: 2/4 with USED TO DECORATE A SNOWMAN) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 33.6%)]
   - Group 17: **0.5162** | CARROT, SUBWAY, UNDERGROUND, METRO                                | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (62.3%, no-rel 13.2%)]
   - Group 18: **0.4475** | HEALTH, DRESS, SECRET, CARROT                                     | INCORRECT (Max overlap: 3/4 with ___ CODE)
   - Group 19: **0.3898** | SLICE, CUBE, ZIP, SCARF                                           | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 20: **0.5645** | SECRET, SUBWAY, UNDERGROUND, METRO                                | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (75.2%, no-rel 13.4%)]

---

## Puzzle 50 (ID: 543)
**Words on Board:** FRONT, LIME, ORACLE, NOSE, OUTSIDE, FLAIR, AMAZON, RHINE, YELLOW, INSTINCT, APPLE, INTUIT, BRIM, SURFACE, GIFT, FACE

### Ground Truth Categories:
* **Level 0 (APTITUDE) [Type: SYNONYM_OR_NEAR]:** FLAIR, GIFT, INSTINCT, NOSE
* **Level 1 (EXTERIOR) [Type: SYNONYM_OR_NEAR]:** FACE, FRONT, OUTSIDE, SURFACE
* **Level 2 (TECH COMPANIES) [Type: NAMED_ENTITY_SET]:** AMAZON, APPLE, INTUIT, ORACLE
* **Level 3 (___STONE) [Type: FILL_IN_THE_BLANK]:** BRIM, LIME, RHINE, YELLOW

### Top Candidate Partitions:
1. **Partition Score: 0.5000**
   - Group 1: **0.6182** | LIME, RHINE, YELLOW, BRIM                                         | CORRECT GROUP (___STONE, Level 3)
   - Group 2: **0.5785** | FRONT, OUTSIDE, SURFACE, FACE                                     | CORRECT GROUP (EXTERIOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 30.2%)]
   - Group 3: **0.4979** | ORACLE, AMAZON, APPLE, INTUIT                                     | CORRECT GROUP (TECH COMPANIES, Level 2)
   - Group 4: **0.4461** | NOSE, FLAIR, INSTINCT, GIFT                                       | CORRECT GROUP (APTITUDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.9%, no-rel 23.3%)]
2. **Partition Score: 0.4898**
   - Group 1: **0.6182** | LIME, RHINE, YELLOW, BRIM                                         | CORRECT GROUP (___STONE, Level 3)
   - Group 2: **0.5273** | FRONT, NOSE, FLAIR, GIFT                                          | INCORRECT (Max overlap: 3/4 with APTITUDE) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 34.5%)]
   - Group 3: **0.4979** | ORACLE, AMAZON, APPLE, INTUIT                                     | CORRECT GROUP (TECH COMPANIES, Level 2)
   - Group 4: **0.4449** | OUTSIDE, INSTINCT, SURFACE, FACE                                  | INCORRECT (Max overlap: 3/4 with EXTERIOR) | [Pred Type: SYNONYM_OR_NEAR (53.3%, no-rel 28.1%)]
3. **Partition Score: 0.4792**
   - Group 1: **0.5785** | FRONT, OUTSIDE, SURFACE, FACE                                     | CORRECT GROUP (EXTERIOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 30.2%)]
   - Group 2: **0.5362** | LIME, AMAZON, YELLOW, APPLE                                       | INCORRECT (Max overlap: 2/4 with ___STONE)
   - Group 3: **0.4534** | ORACLE, RHINE, INTUIT, BRIM                                       | INCORRECT (Max overlap: 2/4 with TECH COMPANIES)
   - Group 4: **0.4461** | NOSE, FLAIR, INSTINCT, GIFT                                       | CORRECT GROUP (APTITUDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.9%, no-rel 23.3%)]
4. **Partition Score: 0.4785**
   - Group 1: **0.5785** | FRONT, OUTSIDE, SURFACE, FACE                                     | CORRECT GROUP (EXTERIOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 30.2%)]
   - Group 2: **0.5255** | ORACLE, AMAZON, YELLOW, APPLE                                     | INCORRECT (Max overlap: 3/4 with TECH COMPANIES)
   - Group 3: **0.4603** | LIME, RHINE, INTUIT, BRIM                                         | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 4: **0.4461** | NOSE, FLAIR, INSTINCT, GIFT                                       | CORRECT GROUP (APTITUDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.9%, no-rel 23.3%)]
5. **Partition Score: 0.4774**
   - Group 1: **0.5785** | FRONT, OUTSIDE, SURFACE, FACE                                     | CORRECT GROUP (EXTERIOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 30.2%)]
   - Group 2: **0.4932** | ORACLE, AMAZON, RHINE, INTUIT                                     | INCORRECT (Max overlap: 3/4 with TECH COMPANIES)
   - Group 3: **0.4863** | LIME, YELLOW, APPLE, BRIM                                         | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 4: **0.4461** | NOSE, FLAIR, INSTINCT, GIFT                                       | CORRECT GROUP (APTITUDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.9%, no-rel 23.3%)]

### Top Candidate Groups:
   - Group 1: **0.6182** | LIME, RHINE, YELLOW, BRIM                                         | CORRECT GROUP (___STONE, Level 3)
   - Group 2: **0.5785** | FRONT, OUTSIDE, SURFACE, FACE                                     | CORRECT GROUP (EXTERIOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 30.2%)]
   - Group 3: **0.4979** | ORACLE, AMAZON, APPLE, INTUIT                                     | CORRECT GROUP (TECH COMPANIES, Level 2)
   - Group 4: **0.4461** | NOSE, FLAIR, INSTINCT, GIFT                                       | CORRECT GROUP (APTITUDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (59.9%, no-rel 23.3%)]
   - Group 5: **0.5273** | FRONT, NOSE, FLAIR, GIFT                                          | INCORRECT (Max overlap: 3/4 with APTITUDE) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 34.5%)]
   - Group 6: **0.4449** | OUTSIDE, INSTINCT, SURFACE, FACE                                  | INCORRECT (Max overlap: 3/4 with EXTERIOR) | [Pred Type: SYNONYM_OR_NEAR (53.3%, no-rel 28.1%)]
   - Group 7: **0.5362** | LIME, AMAZON, YELLOW, APPLE                                       | INCORRECT (Max overlap: 2/4 with ___STONE)
   - Group 8: **0.4534** | ORACLE, RHINE, INTUIT, BRIM                                       | INCORRECT (Max overlap: 2/4 with TECH COMPANIES)
   - Group 9: **0.5255** | ORACLE, AMAZON, YELLOW, APPLE                                     | INCORRECT (Max overlap: 3/4 with TECH COMPANIES)
   - Group 10: **0.4603** | LIME, RHINE, INTUIT, BRIM                                         | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 11: **0.4932** | ORACLE, AMAZON, RHINE, INTUIT                                     | INCORRECT (Max overlap: 3/4 with TECH COMPANIES)
   - Group 12: **0.4863** | LIME, YELLOW, APPLE, BRIM                                         | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 13: **0.5134** | ORACLE, AMAZON, RHINE, APPLE                                      | INCORRECT (Max overlap: 3/4 with TECH COMPANIES)
   - Group 14: **0.4562** | LIME, YELLOW, INTUIT, BRIM                                        | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 15: **0.4925** | LIME, ORACLE, RHINE, BRIM                                         | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 16: **0.4751** | AMAZON, YELLOW, APPLE, INTUIT                                     | INCORRECT (Max overlap: 3/4 with TECH COMPANIES)
   - Group 17: **0.4962** | LIME, ORACLE, AMAZON, APPLE                                       | INCORRECT (Max overlap: 3/4 with TECH COMPANIES)
   - Group 18: **0.4628** | RHINE, YELLOW, INTUIT, BRIM                                       | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 19: **0.5271** | LIME, AMAZON, RHINE, APPLE                                        | INCORRECT (Max overlap: 2/4 with ___STONE)
   - Group 20: **0.4377** | ORACLE, YELLOW, INTUIT, BRIM                                      | INCORRECT (Max overlap: 2/4 with TECH COMPANIES)

---

## Puzzle 51 (ID: 693)
**Words on Board:** SOLO, DRY, BLUTO, JAM, CARS, BOBA, SHRED, DARTH, CHEWY, TEA, STRINGY, NOODLE, SUGAR, MILK, TOUGH, GENUS

### Ground Truth Categories:
* **Level 0 (QUALITIES OF OVERCOOKED MEAT) [Type: SEMANTIC_SET]:** CHEWY, DRY, STRINGY, TOUGH
* **Level 1 (PLAY SOME ELECTRIC GUITAR) [Type: SEMANTIC_SET]:** JAM, NOODLE, SHRED, SOLO
* **Level 2 (INGREDIENTS IN BUBBLE TEA) [Type: SEMANTIC_SET]:** BOBA, MILK, SUGAR, TEA
* **Level 3 (PLANETS/DWARF PLANET WITH FIRST LETTER CHANGED) [Type: WORDPLAY_TRANSFORM]:** BLUTO, CARS, DARTH, GENUS

### Top Candidate Partitions:
1. **Partition Score: 0.5068**
   - Group 1: **0.6832** | TEA, SUGAR, MILK, GENUS                                           | INCORRECT (Max overlap: 3/4 with INGREDIENTS IN BUBBLE TEA)
   - Group 2: **0.5829** | BLUTO, CARS, BOBA, DARTH                                          | INCORRECT (Max overlap: 3/4 with PLANETS/DWARF PLANET WITH FIRST LETTER CHANGED)
   - Group 3: **0.4987** | DRY, CHEWY, STRINGY, TOUGH                                        | CORRECT GROUP (QUALITIES OF OVERCOOKED MEAT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 22.7%)]
   - Group 4: **0.4433** | SOLO, JAM, SHRED, NOODLE                                          | CORRECT GROUP (PLAY SOME ELECTRIC GUITAR, Level 1)
2. **Partition Score: 0.4993**
   - Group 1: **0.6832** | TEA, SUGAR, MILK, GENUS                                           | INCORRECT (Max overlap: 3/4 with INGREDIENTS IN BUBBLE TEA)
   - Group 2: **0.5829** | BLUTO, CARS, BOBA, DARTH                                          | INCORRECT (Max overlap: 3/4 with PLANETS/DWARF PLANET WITH FIRST LETTER CHANGED)
   - Group 3: **0.4709** | DRY, SHRED, CHEWY, TOUGH                                          | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT)
   - Group 4: **0.4387** | SOLO, JAM, STRINGY, NOODLE                                        | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
3. **Partition Score: 0.4980**
   - Group 1: **0.6832** | TEA, SUGAR, MILK, GENUS                                           | INCORRECT (Max overlap: 3/4 with INGREDIENTS IN BUBBLE TEA)
   - Group 2: **0.5829** | BLUTO, CARS, BOBA, DARTH                                          | INCORRECT (Max overlap: 3/4 with PLANETS/DWARF PLANET WITH FIRST LETTER CHANGED)
   - Group 3: **0.4481** | SOLO, JAM, SHRED, STRINGY                                         | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 4: **0.4445** | DRY, CHEWY, NOODLE, TOUGH                                         | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT)
4. **Partition Score: 0.4964**
   - Group 1: **0.6832** | TEA, SUGAR, MILK, GENUS                                           | INCORRECT (Max overlap: 3/4 with INGREDIENTS IN BUBBLE TEA)
   - Group 2: **0.5829** | BLUTO, CARS, BOBA, DARTH                                          | INCORRECT (Max overlap: 3/4 with PLANETS/DWARF PLANET WITH FIRST LETTER CHANGED)
   - Group 3: **0.4438** | SOLO, JAM, CHEWY, TOUGH                                           | INCORRECT (Max overlap: 2/4 with PLAY SOME ELECTRIC GUITAR) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 22.0%)]
   - Group 4: **0.4431** | DRY, SHRED, STRINGY, NOODLE                                       | INCORRECT (Max overlap: 2/4 with QUALITIES OF OVERCOOKED MEAT)
5. **Partition Score: 0.4896**
   - Group 1: **0.6832** | TEA, SUGAR, MILK, GENUS                                           | INCORRECT (Max overlap: 3/4 with INGREDIENTS IN BUBBLE TEA)
   - Group 2: **0.5829** | BLUTO, CARS, BOBA, DARTH                                          | INCORRECT (Max overlap: 3/4 with PLANETS/DWARF PLANET WITH FIRST LETTER CHANGED)
   - Group 3: **0.4339** | SOLO, JAM, SHRED, CHEWY                                           | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 4: **0.4333** | DRY, STRINGY, NOODLE, TOUGH                                       | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT)

### Top Candidate Groups:
   - Group 1: **0.6832** | TEA, SUGAR, MILK, GENUS                                           | INCORRECT (Max overlap: 3/4 with INGREDIENTS IN BUBBLE TEA)
   - Group 2: **0.5829** | BLUTO, CARS, BOBA, DARTH                                          | INCORRECT (Max overlap: 3/4 with PLANETS/DWARF PLANET WITH FIRST LETTER CHANGED)
   - Group 3: **0.4987** | DRY, CHEWY, STRINGY, TOUGH                                        | CORRECT GROUP (QUALITIES OF OVERCOOKED MEAT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 22.7%)]
   - Group 4: **0.4433** | SOLO, JAM, SHRED, NOODLE                                          | CORRECT GROUP (PLAY SOME ELECTRIC GUITAR, Level 1)
   - Group 5: **0.4709** | DRY, SHRED, CHEWY, TOUGH                                          | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT)
   - Group 6: **0.4387** | SOLO, JAM, STRINGY, NOODLE                                        | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 7: **0.4481** | SOLO, JAM, SHRED, STRINGY                                         | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 8: **0.4445** | DRY, CHEWY, NOODLE, TOUGH                                         | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT)
   - Group 9: **0.4438** | SOLO, JAM, CHEWY, TOUGH                                           | INCORRECT (Max overlap: 2/4 with PLAY SOME ELECTRIC GUITAR) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 22.0%)]
   - Group 10: **0.4431** | DRY, SHRED, STRINGY, NOODLE                                       | INCORRECT (Max overlap: 2/4 with QUALITIES OF OVERCOOKED MEAT)
   - Group 11: **0.4339** | SOLO, JAM, SHRED, CHEWY                                           | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 12: **0.4333** | DRY, STRINGY, NOODLE, TOUGH                                       | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT)
   - Group 13: **0.4555** | DRY, CHEWY, STRINGY, NOODLE                                       | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT)
   - Group 14: **0.4234** | SOLO, JAM, SHRED, TOUGH                                           | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 15: **0.4506** | DRY, SHRED, STRINGY, TOUGH                                        | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT)
   - Group 16: **0.4216** | SOLO, JAM, CHEWY, NOODLE                                          | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 17: **0.4359** | JAM, SHRED, STRINGY, NOODLE                                       | INCORRECT (Max overlap: 3/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 18: **0.4243** | SOLO, DRY, CHEWY, TOUGH                                           | INCORRECT (Max overlap: 3/4 with QUALITIES OF OVERCOOKED MEAT) | [Pred Type: SYNONYM_OR_NEAR (47.6%, no-rel 23.2%)]
   - Group 19: **0.4289** | SOLO, JAM, STRINGY, TOUGH                                         | INCORRECT (Max overlap: 2/4 with PLAY SOME ELECTRIC GUITAR)
   - Group 20: **0.4230** | DRY, SHRED, CHEWY, NOODLE                                         | INCORRECT (Max overlap: 2/4 with QUALITIES OF OVERCOOKED MEAT)

---

## Puzzle 52 (ID: 203)
**Words on Board:** CHAMPAGNE, DETAIL, BALL, KISS, GROUP, TOURS, DEFINITION, NICE, CLARITY, FIREWORKS, TEAM, DIJON, RESOLUTION, COUNTDOWN, CLUB, PARTY

### Ground Truth Categories:
* **Level 0 (ORGANIZATION) [Type: SYNONYM_OR_NEAR]:** CLUB, GROUP, PARTY, TEAM
* **Level 1 (SHARPNESS, AS OF AN IMAGE) [Type: SYNONYM_OR_NEAR]:** CLARITY, DEFINITION, DETAIL, RESOLUTION
* **Level 2 (PLACES IN FRANCE) [Type: NAMED_ENTITY_SET]:** CHAMPAGNE, DIJON, NICE, TOURS
* **Level 3 (HAPPY NEW YEAR!) [Type: FILL_IN_THE_BLANK]:** BALL, COUNTDOWN, FIREWORKS, KISS

### Top Candidate Partitions:
1. **Partition Score: 0.4614**
   - Group 1: **0.6631** | GROUP, TEAM, CLUB, PARTY                                          | CORRECT GROUP (ORGANIZATION, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 34.1%)]
   - Group 2: **0.5294** | DETAIL, DEFINITION, CLARITY, RESOLUTION                           | CORRECT GROUP (SHARPNESS, AS OF AN IMAGE, Level 1)
   - Group 3: **0.4986** | KISS, TOURS, NICE, FIREWORKS                                      | INCORRECT (Max overlap: 2/4 with HAPPY NEW YEAR!)
   - Group 4: **0.3786** | CHAMPAGNE, BALL, DIJON, COUNTDOWN                                 | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 15.9%)]
2. **Partition Score: 0.4605**
   - Group 1: **0.6631** | GROUP, TEAM, CLUB, PARTY                                          | CORRECT GROUP (ORGANIZATION, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 34.1%)]
   - Group 2: **0.5758** | CHAMPAGNE, FIREWORKS, DIJON, COUNTDOWN                            | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 3: **0.5294** | DETAIL, DEFINITION, CLARITY, RESOLUTION                           | CORRECT GROUP (SHARPNESS, AS OF AN IMAGE, Level 1)
   - Group 4: **0.3486** | BALL, KISS, TOURS, NICE                                           | INCORRECT (Max overlap: 2/4 with HAPPY NEW YEAR!) | [Pred Type: NAMED_ENTITY_SET (49.6%, no-rel 14.3%)]
3. **Partition Score: 0.4600**
   - Group 1: **0.6631** | GROUP, TEAM, CLUB, PARTY                                          | CORRECT GROUP (ORGANIZATION, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 34.1%)]
   - Group 2: **0.5870** | CHAMPAGNE, TOURS, FIREWORKS, DIJON                                | INCORRECT (Max overlap: 3/4 with PLACES IN FRANCE)
   - Group 3: **0.5294** | DETAIL, DEFINITION, CLARITY, RESOLUTION                           | CORRECT GROUP (SHARPNESS, AS OF AN IMAGE, Level 1)
   - Group 4: **0.3436** | BALL, KISS, NICE, COUNTDOWN                                       | INCORRECT (Max overlap: 3/4 with HAPPY NEW YEAR!) | [Pred Type: NAMED_ENTITY_SET (52.7%, no-rel 14.2%)]
4. **Partition Score: 0.4595**
   - Group 1: **0.6089** | CHAMPAGNE, TOURS, FIREWORKS, COUNTDOWN                            | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 2: **0.4482** | DETAIL, KISS, NICE, DIJON                                         | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 3: **0.4461** | DEFINITION, CLARITY, RESOLUTION, PARTY                            | INCORRECT (Max overlap: 3/4 with SHARPNESS, AS OF AN IMAGE) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 30.6%)]
   - Group 4: **0.4358** | BALL, GROUP, TEAM, CLUB                                           | INCORRECT (Max overlap: 3/4 with ORGANIZATION) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 27.8%)]
5. **Partition Score: 0.4574**
   - Group 1: **0.5758** | CHAMPAGNE, FIREWORKS, DIJON, COUNTDOWN                            | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 2: **0.4566** | DETAIL, KISS, TOURS, NICE                                         | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 3: **0.4461** | DEFINITION, CLARITY, RESOLUTION, PARTY                            | INCORRECT (Max overlap: 3/4 with SHARPNESS, AS OF AN IMAGE) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 30.6%)]
   - Group 4: **0.4358** | BALL, GROUP, TEAM, CLUB                                           | INCORRECT (Max overlap: 3/4 with ORGANIZATION) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 27.8%)]

### Top Candidate Groups:
   - Group 1: **0.6631** | GROUP, TEAM, CLUB, PARTY                                          | CORRECT GROUP (ORGANIZATION, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 34.1%)]
   - Group 2: **0.5294** | DETAIL, DEFINITION, CLARITY, RESOLUTION                           | CORRECT GROUP (SHARPNESS, AS OF AN IMAGE, Level 1)
   - Group 3: **0.4986** | KISS, TOURS, NICE, FIREWORKS                                      | INCORRECT (Max overlap: 2/4 with HAPPY NEW YEAR!)
   - Group 4: **0.3786** | CHAMPAGNE, BALL, DIJON, COUNTDOWN                                 | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 15.9%)]
   - Group 5: **0.5758** | CHAMPAGNE, FIREWORKS, DIJON, COUNTDOWN                            | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 6: **0.3486** | BALL, KISS, TOURS, NICE                                           | INCORRECT (Max overlap: 2/4 with HAPPY NEW YEAR!) | [Pred Type: NAMED_ENTITY_SET (49.6%, no-rel 14.3%)]
   - Group 7: **0.5870** | CHAMPAGNE, TOURS, FIREWORKS, DIJON                                | INCORRECT (Max overlap: 3/4 with PLACES IN FRANCE)
   - Group 8: **0.3436** | BALL, KISS, NICE, COUNTDOWN                                       | INCORRECT (Max overlap: 3/4 with HAPPY NEW YEAR!) | [Pred Type: NAMED_ENTITY_SET (52.7%, no-rel 14.2%)]
   - Group 9: **0.6089** | CHAMPAGNE, TOURS, FIREWORKS, COUNTDOWN                            | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 10: **0.4482** | DETAIL, KISS, NICE, DIJON                                         | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 11: **0.4461** | DEFINITION, CLARITY, RESOLUTION, PARTY                            | INCORRECT (Max overlap: 3/4 with SHARPNESS, AS OF AN IMAGE) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 30.6%)]
   - Group 12: **0.4358** | BALL, GROUP, TEAM, CLUB                                           | INCORRECT (Max overlap: 3/4 with ORGANIZATION) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 27.8%)]
   - Group 13: **0.4566** | DETAIL, KISS, TOURS, NICE                                         | INCORRECT (Max overlap: 2/4 with PLACES IN FRANCE)
   - Group 14: **0.4767** | KISS, NICE, FIREWORKS, COUNTDOWN                                  | INCORRECT (Max overlap: 3/4 with HAPPY NEW YEAR!)
   - Group 15: **0.3787** | CHAMPAGNE, BALL, TOURS, DIJON                                     | INCORRECT (Max overlap: 3/4 with PLACES IN FRANCE) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 15.1%)]
   - Group 16: **0.4727** | BALL, TEAM, CLUB, PARTY                                           | INCORRECT (Max overlap: 3/4 with ORGANIZATION)
   - Group 17: **0.4216** | GROUP, DEFINITION, CLARITY, RESOLUTION                            | INCORRECT (Max overlap: 3/4 with SHARPNESS, AS OF AN IMAGE)
   - Group 18: **0.4428** | DETAIL, KISS, NICE, COUNTDOWN                                     | INCORRECT (Max overlap: 2/4 with HAPPY NEW YEAR!)
   - Group 19: **0.4600** | KISS, TOURS, NICE, DIJON                                          | INCORRECT (Max overlap: 3/4 with PLACES IN FRANCE)
   - Group 20: **0.3814** | CHAMPAGNE, BALL, FIREWORKS, COUNTDOWN                             | INCORRECT (Max overlap: 3/4 with HAPPY NEW YEAR!)

---

## Puzzle 53 (ID: 740)
**Words on Board:** MUSEUM, BUTTON, TAPE, RECORD, SHOOT, SNAKE, HITMAN, UNDERTAKER, ROCK, SEAL, SCISSORS, THREAD, FILM, POETIC, PAPER, NEEDLE

### Ground Truth Categories:
* **Level 0 (ITEMS IN A SEWING KIT) [Type: SEMANTIC_SET]:** BUTTON, NEEDLE, SCISSORS, THREAD
* **Level 1 (CAPTURE ON VIDEO) [Type: SYNONYM_OR_NEAR]:** FILM, RECORD, SHOOT, TAPE
* **Level 2 (PRO WRESTLING ICONS, WITH “THE”) [Type: NAMED_ENTITY_SET]:** HITMAN, ROCK, SNAKE, UNDERTAKER
* **Level 3 (WAX ___) [Type: FILL_IN_THE_BLANK]:** MUSEUM, PAPER, POETIC, SEAL

### Top Candidate Partitions:
1. **Partition Score: 0.5301**
   - Group 1: **0.7367** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 33.5%)]
   - Group 2: **0.6106** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.5463** | BUTTON, ROCK, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 4: **0.4493** | SNAKE, SEAL, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
2. **Partition Score: 0.5271**
   - Group 1: **0.7367** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 33.5%)]
   - Group 2: **0.6106** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.5407** | BUTTON, SNAKE, THREAD, NEEDLE                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT)
   - Group 4: **0.4456** | ROCK, SEAL, SCISSORS, PAPER                                       | INCORRECT (Max overlap: 2/4 with WAX ___)
3. **Partition Score: 0.5259**
   - Group 1: **0.7367** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 33.5%)]
   - Group 2: **0.6106** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.4970** | ROCK, SCISSORS, PAPER, NEEDLE                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (48.9%, no-rel 25.4%)]
   - Group 4: **0.4592** | BUTTON, SNAKE, SEAL, THREAD                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
4. **Partition Score: 0.5115**
   - Group 1: **0.6106** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 2: **0.5415** | BUTTON, ROCK, SCISSORS, NEEDLE                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (45.4%, no-rel 28.4%)]
   - Group 3: **0.5126** | SNAKE, THREAD, FILM, PAPER                                        | INCORRECT (Max overlap: 1/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 4: **0.4783** | TAPE, RECORD, SHOOT, SEAL                                         | INCORRECT (Max overlap: 3/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 29.5%)]
5. **Partition Score: 0.5086**
   - Group 1: **0.7367** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 33.5%)]
   - Group 2: **0.6106** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.4633** | SNAKE, ROCK, SCISSORS, PAPER                                      | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”) | [Pred Type: SEMANTIC_SET (45.7%, no-rel 25.6%)]
   - Group 4: **0.4377** | BUTTON, SEAL, THREAD, NEEDLE                                      | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (45.9%, no-rel 31.2%)]

### Top Candidate Groups:
   - Group 1: **0.7367** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 33.5%)]
   - Group 2: **0.6106** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.5463** | BUTTON, ROCK, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 4: **0.4493** | SNAKE, SEAL, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 5: **0.5407** | BUTTON, SNAKE, THREAD, NEEDLE                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT)
   - Group 6: **0.4456** | ROCK, SEAL, SCISSORS, PAPER                                       | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 7: **0.4970** | ROCK, SCISSORS, PAPER, NEEDLE                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (48.9%, no-rel 25.4%)]
   - Group 8: **0.4592** | BUTTON, SNAKE, SEAL, THREAD                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT)
   - Group 9: **0.5415** | BUTTON, ROCK, SCISSORS, NEEDLE                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (45.4%, no-rel 28.4%)]
   - Group 10: **0.5126** | SNAKE, THREAD, FILM, PAPER                                        | INCORRECT (Max overlap: 1/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 11: **0.4783** | TAPE, RECORD, SHOOT, SEAL                                         | INCORRECT (Max overlap: 3/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 29.5%)]
   - Group 12: **0.4633** | SNAKE, ROCK, SCISSORS, PAPER                                      | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”) | [Pred Type: SEMANTIC_SET (45.7%, no-rel 25.6%)]
   - Group 13: **0.4377** | BUTTON, SEAL, THREAD, NEEDLE                                      | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (45.9%, no-rel 31.2%)]
   - Group 14: **0.4867** | TAPE, RECORD, SEAL, PAPER                                         | INCORRECT (Max overlap: 2/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 31.3%)]
   - Group 15: **0.4799** | SHOOT, SNAKE, THREAD, FILM                                        | INCORRECT (Max overlap: 2/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 25.7%)]
   - Group 16: **0.5234** | TAPE, RECORD, SHOOT, PAPER                                        | INCORRECT (Max overlap: 3/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 33.0%)]
   - Group 17: **0.4660** | SNAKE, SEAL, THREAD, FILM                                         | INCORRECT (Max overlap: 1/4 with PRO WRESTLING ICONS, WITH “THE”)
   - Group 18: **0.4400** | BUTTON, ROCK, SEAL, PAPER                                         | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 19: **0.4388** | SNAKE, SCISSORS, THREAD, NEEDLE                                   | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (50.3%, no-rel 22.5%)]
   - Group 20: **0.5754** | MUSEUM, HITMAN, UNDERTAKER, SCISSORS                              | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”)

---

## Puzzle 54 (ID: 1054)
**Words on Board:** SOFTIE, CHOWDER, HACKY SACK, RADIO, BEANIE BABY, STOVE, EYE PILLOW, DESICCANT PACKET, SWEETHEART, PITTER-PATTER, LABUBU, ETCH A SKETCH, MARSHMALLOW, DOODLEBUG, CONTROL PANEL, TEDDY BEAR

### Ground Truth Categories:
* **Level 0 (TENDER-HEARTED PERSON) [Type: SYNONYM_OR_NEAR]:** MARSHMALLOW, SOFTIE, SWEETHEART, TEDDY BEAR
* **Level 1 (PELLET-FILLED THINGS) [Type: SEMANTIC_SET]:** BEANIE BABY, DESICCANT PACKET, EYE PILLOW, HACKY SACK
* **Level 2 (THINGS WITH KNOBS) [Type: SEMANTIC_SET]:** CONTROL PANEL, ETCH A SKETCH, RADIO, STOVE
* **Level 3 (STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS) [Type: WORD_FORM]:** CHOWDER, DOODLEBUG, LABUBU, PITTER-PATTER

### Top Candidate Partitions:
1. **Partition Score: 0.4692**
   - Group 1: **0.4922** | HACKY SACK, LABUBU, MARSHMALLOW, DOODLEBUG                        | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 2: **0.4868** | BEANIE BABY, EYE PILLOW, ETCH A SKETCH, TEDDY BEAR                | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 3: **0.4857** | SOFTIE, CHOWDER, SWEETHEART, PITTER-PATTER                        | INCORRECT (Max overlap: 2/4 with TENDER-HEARTED PERSON)
   - Group 4: **0.4517** | RADIO, STOVE, DESICCANT PACKET, CONTROL PANEL                     | INCORRECT (Max overlap: 3/4 with THINGS WITH KNOBS)
2. **Partition Score: 0.4687**
   - Group 1: **0.4887** | HACKY SACK, BEANIE BABY, EYE PILLOW, ETCH A SKETCH                | INCORRECT (Max overlap: 3/4 with PELLET-FILLED THINGS)
   - Group 2: **0.4858** | LABUBU, MARSHMALLOW, DOODLEBUG, TEDDY BEAR                        | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 3: **0.4857** | SOFTIE, CHOWDER, SWEETHEART, PITTER-PATTER                        | INCORRECT (Max overlap: 2/4 with TENDER-HEARTED PERSON)
   - Group 4: **0.4517** | RADIO, STOVE, DESICCANT PACKET, CONTROL PANEL                     | INCORRECT (Max overlap: 3/4 with THINGS WITH KNOBS)
3. **Partition Score: 0.4681**
   - Group 1: **0.4866** | BEANIE BABY, LABUBU, MARSHMALLOW, DOODLEBUG                       | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 2: **0.4857** | SOFTIE, CHOWDER, SWEETHEART, PITTER-PATTER                        | INCORRECT (Max overlap: 2/4 with TENDER-HEARTED PERSON)
   - Group 3: **0.4842** | HACKY SACK, EYE PILLOW, ETCH A SKETCH, TEDDY BEAR                 | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 4: **0.4517** | RADIO, STOVE, DESICCANT PACKET, CONTROL PANEL                     | INCORRECT (Max overlap: 3/4 with THINGS WITH KNOBS)
4. **Partition Score: 0.4679**
   - Group 1: **0.5133** | BEANIE BABY, EYE PILLOW, MARSHMALLOW, TEDDY BEAR                  | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 2: **0.4857** | SOFTIE, CHOWDER, SWEETHEART, PITTER-PATTER                        | INCORRECT (Max overlap: 2/4 with TENDER-HEARTED PERSON)
   - Group 3: **0.4669** | HACKY SACK, LABUBU, ETCH A SKETCH, DOODLEBUG                      | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 4: **0.4517** | RADIO, STOVE, DESICCANT PACKET, CONTROL PANEL                     | INCORRECT (Max overlap: 3/4 with THINGS WITH KNOBS)
5. **Partition Score: 0.4673**
   - Group 1: **0.5020** | HACKY SACK, BEANIE BABY, ETCH A SKETCH, TEDDY BEAR                | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 2: **0.4857** | SOFTIE, CHOWDER, SWEETHEART, PITTER-PATTER                        | INCORRECT (Max overlap: 2/4 with TENDER-HEARTED PERSON)
   - Group 3: **0.4705** | EYE PILLOW, LABUBU, MARSHMALLOW, DOODLEBUG                        | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 4: **0.4517** | RADIO, STOVE, DESICCANT PACKET, CONTROL PANEL                     | INCORRECT (Max overlap: 3/4 with THINGS WITH KNOBS)

### Top Candidate Groups:
   - Group 1: **0.4922** | HACKY SACK, LABUBU, MARSHMALLOW, DOODLEBUG                        | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 2: **0.4868** | BEANIE BABY, EYE PILLOW, ETCH A SKETCH, TEDDY BEAR                | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 3: **0.4857** | SOFTIE, CHOWDER, SWEETHEART, PITTER-PATTER                        | INCORRECT (Max overlap: 2/4 with TENDER-HEARTED PERSON)
   - Group 4: **0.4517** | RADIO, STOVE, DESICCANT PACKET, CONTROL PANEL                     | INCORRECT (Max overlap: 3/4 with THINGS WITH KNOBS)
   - Group 5: **0.4887** | HACKY SACK, BEANIE BABY, EYE PILLOW, ETCH A SKETCH                | INCORRECT (Max overlap: 3/4 with PELLET-FILLED THINGS)
   - Group 6: **0.4858** | LABUBU, MARSHMALLOW, DOODLEBUG, TEDDY BEAR                        | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 7: **0.4866** | BEANIE BABY, LABUBU, MARSHMALLOW, DOODLEBUG                       | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 8: **0.4842** | HACKY SACK, EYE PILLOW, ETCH A SKETCH, TEDDY BEAR                 | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 9: **0.5133** | BEANIE BABY, EYE PILLOW, MARSHMALLOW, TEDDY BEAR                  | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 10: **0.4669** | HACKY SACK, LABUBU, ETCH A SKETCH, DOODLEBUG                      | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 11: **0.5020** | HACKY SACK, BEANIE BABY, ETCH A SKETCH, TEDDY BEAR                | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 12: **0.4705** | EYE PILLOW, LABUBU, MARSHMALLOW, DOODLEBUG                        | INCORRECT (Max overlap: 2/4 with STARTING WITH FAMILIAR NAMES FOR KINDS OF DOGS)
   - Group 13: **0.4984** | HACKY SACK, EYE PILLOW, LABUBU, MARSHMALLOW                       | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 14: **0.4726** | BEANIE BABY, ETCH A SKETCH, DOODLEBUG, TEDDY BEAR                 | INCORRECT (Max overlap: 1/4 with PELLET-FILLED THINGS)
   - Group 15: **0.5004** | BEANIE BABY, MARSHMALLOW, DOODLEBUG, TEDDY BEAR                   | INCORRECT (Max overlap: 2/4 with TENDER-HEARTED PERSON)
   - Group 16: **0.4696** | HACKY SACK, EYE PILLOW, LABUBU, ETCH A SKETCH                     | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 17: **0.4911** | BEANIE BABY, EYE PILLOW, LABUBU, MARSHMALLOW                      | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)
   - Group 18: **0.4684** | HACKY SACK, ETCH A SKETCH, DOODLEBUG, TEDDY BEAR                  | INCORRECT (Max overlap: 1/4 with PELLET-FILLED THINGS)
   - Group 19: **0.4873** | EYE PILLOW, LABUBU, MARSHMALLOW, TEDDY BEAR                       | INCORRECT (Max overlap: 2/4 with TENDER-HEARTED PERSON)
   - Group 20: **0.4698** | HACKY SACK, BEANIE BABY, ETCH A SKETCH, DOODLEBUG                 | INCORRECT (Max overlap: 2/4 with PELLET-FILLED THINGS)

---

## Puzzle 55 (ID: 904)
**Words on Board:** GENERAL, FRICK, BROAD, FUDGE, BROW, MOMA, ROUGH, RAY, SUGAR, DADA, BALLPARK, ROYAL, SISI, SHOOT, ANGEL, MET

### Ground Truth Categories:
* **Level 0 (APPROXIMATE) [Type: SYNONYM_OR_NEAR]:** BALLPARK, BROAD, GENERAL, ROUGH
* **Level 1 (MILD OATHS) [Type: SYNONYM_OR_NEAR]:** FRICK, FUDGE, SHOOT, SUGAR
* **Level 2 (MLB PLAYER) [Type: NAMED_ENTITY_SET]:** ANGEL, MET, RAY, ROYAL
* **Level 3 (FAMILY MEMBER NICKNAME PLUS A LETTER) [Type: WORDPLAY_TRANSFORM]:** BROW, DADA, MOMA, SISI

### Top Candidate Partitions:
1. **Partition Score: 0.4900**
   - Group 1: **0.5597** | FRICK, MOMA, DADA, SISI                                           | INCORRECT (Max overlap: 3/4 with FAMILY MEMBER NICKNAME PLUS A LETTER)
   - Group 2: **0.4877** | BROAD, ROUGH, BALLPARK, ROYAL                                     | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
   - Group 3: **0.4814** | GENERAL, FUDGE, BROW, SHOOT                                       | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 4: **0.4788** | RAY, SUGAR, ANGEL, MET                                            | INCORRECT (Max overlap: 3/4 with MLB PLAYER)
2. **Partition Score: 0.4886**
   - Group 1: **0.5597** | FRICK, MOMA, DADA, SISI                                           | INCORRECT (Max overlap: 3/4 with FAMILY MEMBER NICKNAME PLUS A LETTER)
   - Group 2: **0.5031** | GENERAL, BROAD, BALLPARK, ROYAL                                   | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
   - Group 3: **0.4788** | RAY, SUGAR, ANGEL, MET                                            | INCORRECT (Max overlap: 3/4 with MLB PLAYER)
   - Group 4: **0.4713** | FUDGE, BROW, ROUGH, SHOOT                                         | INCORRECT (Max overlap: 2/4 with MILD OATHS)
3. **Partition Score: 0.4849**
   - Group 1: **0.5597** | FRICK, MOMA, DADA, SISI                                           | INCORRECT (Max overlap: 3/4 with FAMILY MEMBER NICKNAME PLUS A LETTER)
   - Group 2: **0.4816** | GENERAL, ROUGH, BALLPARK, ROYAL                                   | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
   - Group 3: **0.4788** | RAY, SUGAR, ANGEL, MET                                            | INCORRECT (Max overlap: 3/4 with MLB PLAYER)
   - Group 4: **0.4720** | BROAD, FUDGE, BROW, SHOOT                                         | INCORRECT (Max overlap: 2/4 with MILD OATHS)
4. **Partition Score: 0.4776**
   - Group 1: **0.5597** | FRICK, MOMA, DADA, SISI                                           | INCORRECT (Max overlap: 3/4 with FAMILY MEMBER NICKNAME PLUS A LETTER)
   - Group 2: **0.4990** | RAY, SUGAR, ROYAL, ANGEL                                          | INCORRECT (Max overlap: 3/4 with MLB PLAYER)
   - Group 3: **0.4713** | FUDGE, BROW, ROUGH, SHOOT                                         | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 4: **0.4541** | GENERAL, BROAD, BALLPARK, MET                                     | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
5. **Partition Score: 0.4775**
   - Group 1: **0.5168** | GENERAL, FUDGE, ROUGH, SHOOT                                      | INCORRECT (Max overlap: 2/4 with APPROXIMATE)
   - Group 2: **0.4990** | RAY, SUGAR, ROYAL, ANGEL                                          | INCORRECT (Max overlap: 3/4 with MLB PLAYER)
   - Group 3: **0.4656** | MOMA, DADA, SISI, MET                                             | INCORRECT (Max overlap: 3/4 with FAMILY MEMBER NICKNAME PLUS A LETTER) | [Pred Type: NAMED_ENTITY_SET (47.9%, no-rel 22.4%)]
   - Group 4: **0.4653** | FRICK, BROAD, BROW, BALLPARK                                      | INCORRECT (Max overlap: 2/4 with APPROXIMATE)

### Top Candidate Groups:
   - Group 1: **0.5597** | FRICK, MOMA, DADA, SISI                                           | INCORRECT (Max overlap: 3/4 with FAMILY MEMBER NICKNAME PLUS A LETTER)
   - Group 2: **0.4877** | BROAD, ROUGH, BALLPARK, ROYAL                                     | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
   - Group 3: **0.4814** | GENERAL, FUDGE, BROW, SHOOT                                       | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 4: **0.4788** | RAY, SUGAR, ANGEL, MET                                            | INCORRECT (Max overlap: 3/4 with MLB PLAYER)
   - Group 5: **0.5031** | GENERAL, BROAD, BALLPARK, ROYAL                                   | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
   - Group 6: **0.4713** | FUDGE, BROW, ROUGH, SHOOT                                         | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 7: **0.4816** | GENERAL, ROUGH, BALLPARK, ROYAL                                   | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
   - Group 8: **0.4720** | BROAD, FUDGE, BROW, SHOOT                                         | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 9: **0.4990** | RAY, SUGAR, ROYAL, ANGEL                                          | INCORRECT (Max overlap: 3/4 with MLB PLAYER)
   - Group 10: **0.4541** | GENERAL, BROAD, BALLPARK, MET                                     | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
   - Group 11: **0.5168** | GENERAL, FUDGE, ROUGH, SHOOT                                      | INCORRECT (Max overlap: 2/4 with APPROXIMATE)
   - Group 12: **0.4656** | MOMA, DADA, SISI, MET                                             | INCORRECT (Max overlap: 3/4 with FAMILY MEMBER NICKNAME PLUS A LETTER) | [Pred Type: NAMED_ENTITY_SET (47.9%, no-rel 22.4%)]
   - Group 13: **0.4653** | FRICK, BROAD, BROW, BALLPARK                                      | INCORRECT (Max overlap: 2/4 with APPROXIMATE)
   - Group 14: **0.5242** | BROAD, FUDGE, ROUGH, SHOOT                                        | INCORRECT (Max overlap: 2/4 with APPROXIMATE)
   - Group 15: **0.4395** | GENERAL, BROW, BALLPARK, ROYAL                                    | INCORRECT (Max overlap: 2/4 with APPROXIMATE)
   - Group 16: **0.4861** | FRICK, BROAD, ROUGH, BALLPARK                                     | INCORRECT (Max overlap: 3/4 with APPROXIMATE)
   - Group 17: **0.4912** | FRICK, RAY, SUGAR, ANGEL                                          | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 18: **0.5258** | GENERAL, BROAD, FUDGE, SHOOT                                      | INCORRECT (Max overlap: 2/4 with APPROXIMATE)
   - Group 19: **0.4583** | FRICK, BROW, ROUGH, BALLPARK                                      | INCORRECT (Max overlap: 2/4 with APPROXIMATE)
   - Group 20: **0.4791** | BROAD, ROUGH, SUGAR, BALLPARK                                     | INCORRECT (Max overlap: 3/4 with APPROXIMATE)

---

## Puzzle 56 (ID: 1091)
**Words on Board:** FORERUNNER, RHINO, VIKING HELMET, STRETCHING, CARDIO, VENO, BRONCHO, WEIGHTS, DEVIL, STRIP, BRASS BAND, TROUPER, BALANCE, PAPAL, ELLE, UCONN

### Ground Truth Categories:
* **Level 0 (PARTS OF A WORKOUT ROUTINE) [Type: SEMANTIC_SET]:** BALANCE, CARDIO, STRETCHING, WEIGHTS
* **Level 1 (THINGS WITH HORNS) [Type: SEMANTIC_SET]:** BRASS BAND, DEVIL, RHINO, VIKING HELMET
* **Level 2 (HOMOPHONES OF SUVS) [Type: SOUND_OR_SPELLING]:** BRONCHO, FORERUNNER, TROUPER, UCONN
* **Level 3 (PAYMENT APPS MINUS A LETTER) [Type: WORDPLAY_TRANSFORM]:** ELLE, PAPAL, STRIP, VENO

### Top Candidate Partitions:
1. **Partition Score: 0.5049**
   - Group 1: **0.5363** | RHINO, CARDIO, VENO, BRONCHO                                      | INCORRECT (Max overlap: 1/4 with THINGS WITH HORNS)
   - Group 2: **0.5208** | STRETCHING, WEIGHTS, STRIP, BALANCE                               | INCORRECT (Max overlap: 3/4 with PARTS OF A WORKOUT ROUTINE)
   - Group 3: **0.5038** | DEVIL, PAPAL, ELLE, UCONN                                         | INCORRECT (Max overlap: 2/4 with PAYMENT APPS MINUS A LETTER)
   - Group 4: **0.4925** | FORERUNNER, VIKING HELMET, BRASS BAND, TROUPER                    | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS)
2. **Partition Score: 0.4966**
   - Group 1: **0.5208** | STRETCHING, WEIGHTS, STRIP, BALANCE                               | INCORRECT (Max overlap: 3/4 with PARTS OF A WORKOUT ROUTINE)
   - Group 2: **0.4963** | RHINO, CARDIO, BRONCHO, BRASS BAND                                | INCORRECT (Max overlap: 2/4 with THINGS WITH HORNS)
   - Group 3: **0.4941** | FORERUNNER, VIKING HELMET, DEVIL, TROUPER                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS)
   - Group 4: **0.4923** | VENO, PAPAL, ELLE, UCONN                                          | INCORRECT (Max overlap: 3/4 with PAYMENT APPS MINUS A LETTER)
3. **Partition Score: 0.4961**
   - Group 1: **0.5208** | STRETCHING, WEIGHTS, STRIP, BALANCE                               | INCORRECT (Max overlap: 3/4 with PARTS OF A WORKOUT ROUTINE)
   - Group 2: **0.5064** | RHINO, CARDIO, BRONCHO, PAPAL                                     | INCORRECT (Max overlap: 1/4 with THINGS WITH HORNS)
   - Group 3: **0.4931** | VIKING HELMET, VENO, ELLE, UCONN                                  | INCORRECT (Max overlap: 2/4 with PAYMENT APPS MINUS A LETTER)
   - Group 4: **0.4880** | FORERUNNER, DEVIL, BRASS BAND, TROUPER                            | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS)
4. **Partition Score: 0.4945**
   - Group 1: **0.5363** | RHINO, CARDIO, VENO, BRONCHO                                      | INCORRECT (Max overlap: 1/4 with THINGS WITH HORNS)
   - Group 2: **0.5208** | STRETCHING, WEIGHTS, STRIP, BALANCE                               | INCORRECT (Max overlap: 3/4 with PARTS OF A WORKOUT ROUTINE)
   - Group 3: **0.4880** | FORERUNNER, DEVIL, BRASS BAND, TROUPER                            | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS)
   - Group 4: **0.4781** | VIKING HELMET, PAPAL, ELLE, UCONN                                 | INCORRECT (Max overlap: 2/4 with PAYMENT APPS MINUS A LETTER)
5. **Partition Score: 0.4914**
   - Group 1: **0.5208** | STRETCHING, WEIGHTS, STRIP, BALANCE                               | INCORRECT (Max overlap: 3/4 with PARTS OF A WORKOUT ROUTINE)
   - Group 2: **0.5007** | VIKING HELMET, BRASS BAND, ELLE, UCONN                            | INCORRECT (Max overlap: 2/4 with THINGS WITH HORNS)
   - Group 3: **0.4869** | CARDIO, VENO, BRONCHO, PAPAL                                      | INCORRECT (Max overlap: 2/4 with PAYMENT APPS MINUS A LETTER)
   - Group 4: **0.4832** | FORERUNNER, RHINO, DEVIL, TROUPER                                 | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS) | [Pred Type: NAMED_ENTITY_SET (53.1%, no-rel 16.5%)]

### Top Candidate Groups:
   - Group 1: **0.5363** | RHINO, CARDIO, VENO, BRONCHO                                      | INCORRECT (Max overlap: 1/4 with THINGS WITH HORNS)
   - Group 2: **0.5208** | STRETCHING, WEIGHTS, STRIP, BALANCE                               | INCORRECT (Max overlap: 3/4 with PARTS OF A WORKOUT ROUTINE)
   - Group 3: **0.5038** | DEVIL, PAPAL, ELLE, UCONN                                         | INCORRECT (Max overlap: 2/4 with PAYMENT APPS MINUS A LETTER)
   - Group 4: **0.4925** | FORERUNNER, VIKING HELMET, BRASS BAND, TROUPER                    | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS)
   - Group 5: **0.4963** | RHINO, CARDIO, BRONCHO, BRASS BAND                                | INCORRECT (Max overlap: 2/4 with THINGS WITH HORNS)
   - Group 6: **0.4941** | FORERUNNER, VIKING HELMET, DEVIL, TROUPER                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS)
   - Group 7: **0.4923** | VENO, PAPAL, ELLE, UCONN                                          | INCORRECT (Max overlap: 3/4 with PAYMENT APPS MINUS A LETTER)
   - Group 8: **0.5064** | RHINO, CARDIO, BRONCHO, PAPAL                                     | INCORRECT (Max overlap: 1/4 with THINGS WITH HORNS)
   - Group 9: **0.4931** | VIKING HELMET, VENO, ELLE, UCONN                                  | INCORRECT (Max overlap: 2/4 with PAYMENT APPS MINUS A LETTER)
   - Group 10: **0.4880** | FORERUNNER, DEVIL, BRASS BAND, TROUPER                            | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS)
   - Group 11: **0.4781** | VIKING HELMET, PAPAL, ELLE, UCONN                                 | INCORRECT (Max overlap: 2/4 with PAYMENT APPS MINUS A LETTER)
   - Group 12: **0.5007** | VIKING HELMET, BRASS BAND, ELLE, UCONN                            | INCORRECT (Max overlap: 2/4 with THINGS WITH HORNS)
   - Group 13: **0.4869** | CARDIO, VENO, BRONCHO, PAPAL                                      | INCORRECT (Max overlap: 2/4 with PAYMENT APPS MINUS A LETTER)
   - Group 14: **0.4832** | FORERUNNER, RHINO, DEVIL, TROUPER                                 | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS) | [Pred Type: NAMED_ENTITY_SET (53.1%, no-rel 16.5%)]
   - Group 15: **0.5047** | RHINO, CARDIO, BRONCHO, UCONN                                     | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS)
   - Group 16: **0.4770** | VENO, DEVIL, PAPAL, ELLE                                          | INCORRECT (Max overlap: 3/4 with PAYMENT APPS MINUS A LETTER)
   - Group 17: **0.4639** | FORERUNNER, DEVIL, TROUPER, PAPAL                                 | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF SUVS) | [Pred Type: NAMED_ENTITY_SET (54.9%, no-rel 16.3%)]
   - Group 18: **0.4794** | RHINO, VIKING HELMET, CARDIO, BRONCHO                             | INCORRECT (Max overlap: 2/4 with THINGS WITH HORNS)
   - Group 19: **0.4742** | VIKING HELMET, VENO, PAPAL, ELLE                                  | INCORRECT (Max overlap: 3/4 with PAYMENT APPS MINUS A LETTER)
   - Group 20: **0.4808** | RHINO, DEVIL, PAPAL, ELLE                                         | INCORRECT (Max overlap: 2/4 with THINGS WITH HORNS) | [Pred Type: NAMED_ENTITY_SET (46.6%, no-rel 21.9%)]

---

## Puzzle 57 (ID: 4)
**Words on Board:** SWEEP, CAROUSEL, BAT, MOP, SPIDER, REEBOK, ADIDAS, DUST, IRON, PUMA, SUPER, CATS, VACUUM, NIKE, CABARET, CHICAGO

### Ground Truth Categories:
* **Level 0 (SNEAKER BRANDS) [Type: NAMED_ENTITY_SET]:** ADIDAS, NIKE, PUMA, REEBOK
* **Level 1 (MUSICALS BEGINNING WITH “C”) [Type: WORD_FORM]:** CABARET, CAROUSEL, CATS, CHICAGO
* **Level 2 (CLEANING VERBS) [Type: SYNONYM_OR_NEAR]:** DUST, MOP, SWEEP, VACUUM
* **Level 3 (___ MAN SUPERHEROES) [Type: FILL_IN_THE_BLANK]:** BAT, IRON, SPIDER, SUPER

### Top Candidate Partitions:
1. **Partition Score: 0.5257**
   - Group 1: **0.6640** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0) | [Pred Type: NAMED_ENTITY_SET (48.3%, no-rel 18.3%)]
   - Group 2: **0.5557** | SWEEP, MOP, DUST, VACUUM                                          | CORRECT GROUP (CLEANING VERBS, Level 2)
   - Group 3: **0.5419** | BAT, SPIDER, IRON, SUPER                                          | CORRECT GROUP (___ MAN SUPERHEROES, Level 3)
   - Group 4: **0.4784** | CAROUSEL, CATS, CABARET, CHICAGO                                  | CORRECT GROUP (MUSICALS BEGINNING WITH “C”, Level 1)
2. **Partition Score: 0.5145**
   - Group 1: **0.5557** | SWEEP, MOP, DUST, VACUUM                                          | CORRECT GROUP (CLEANING VERBS, Level 2)
   - Group 2: **0.5550** | ADIDAS, PUMA, CATS, NIKE                                          | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (51.7%, no-rel 20.4%)]
   - Group 3: **0.5419** | BAT, SPIDER, IRON, SUPER                                          | CORRECT GROUP (___ MAN SUPERHEROES, Level 3)
   - Group 4: **0.4806** | CAROUSEL, REEBOK, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
3. **Partition Score: 0.5088**
   - Group 1: **0.6640** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0) | [Pred Type: NAMED_ENTITY_SET (48.3%, no-rel 18.3%)]
   - Group 2: **0.5669** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 3: **0.4784** | CAROUSEL, CATS, CABARET, CHICAGO                                  | CORRECT GROUP (MUSICALS BEGINNING WITH “C”, Level 1)
   - Group 4: **0.4645** | BAT, MOP, SPIDER, SUPER                                           | INCORRECT (Max overlap: 3/4 with ___ MAN SUPERHEROES)
4. **Partition Score: 0.5035**
   - Group 1: **0.5557** | SWEEP, MOP, DUST, VACUUM                                          | CORRECT GROUP (CLEANING VERBS, Level 2)
   - Group 2: **0.5475** | REEBOK, ADIDAS, NIKE, CHICAGO                                     | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.1%, no-rel 20.6%)]
   - Group 3: **0.5419** | BAT, SPIDER, IRON, SUPER                                          | CORRECT GROUP (___ MAN SUPERHEROES, Level 3)
   - Group 4: **0.4619** | CAROUSEL, PUMA, CATS, CABARET                                     | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (47.0%, no-rel 21.9%)]
5. **Partition Score: 0.5013**
   - Group 1: **0.5557** | SWEEP, MOP, DUST, VACUUM                                          | CORRECT GROUP (CLEANING VERBS, Level 2)
   - Group 2: **0.5419** | BAT, SPIDER, IRON, SUPER                                          | CORRECT GROUP (___ MAN SUPERHEROES, Level 3)
   - Group 3: **0.5150** | REEBOK, PUMA, CATS, NIKE                                          | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (51.1%, no-rel 20.0%)]
   - Group 4: **0.4696** | CAROUSEL, ADIDAS, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)

### Top Candidate Groups:
   - Group 1: **0.6640** | REEBOK, ADIDAS, PUMA, NIKE                                        | CORRECT GROUP (SNEAKER BRANDS, Level 0) | [Pred Type: NAMED_ENTITY_SET (48.3%, no-rel 18.3%)]
   - Group 2: **0.5557** | SWEEP, MOP, DUST, VACUUM                                          | CORRECT GROUP (CLEANING VERBS, Level 2)
   - Group 3: **0.5419** | BAT, SPIDER, IRON, SUPER                                          | CORRECT GROUP (___ MAN SUPERHEROES, Level 3)
   - Group 4: **0.4784** | CAROUSEL, CATS, CABARET, CHICAGO                                  | CORRECT GROUP (MUSICALS BEGINNING WITH “C”, Level 1)
   - Group 5: **0.5550** | ADIDAS, PUMA, CATS, NIKE                                          | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (51.7%, no-rel 20.4%)]
   - Group 6: **0.4806** | CAROUSEL, REEBOK, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
   - Group 7: **0.5669** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 8: **0.4645** | BAT, MOP, SPIDER, SUPER                                           | INCORRECT (Max overlap: 3/4 with ___ MAN SUPERHEROES)
   - Group 9: **0.5475** | REEBOK, ADIDAS, NIKE, CHICAGO                                     | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.1%, no-rel 20.6%)]
   - Group 10: **0.4619** | CAROUSEL, PUMA, CATS, CABARET                                     | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (47.0%, no-rel 21.9%)]
   - Group 11: **0.5150** | REEBOK, PUMA, CATS, NIKE                                          | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (51.1%, no-rel 20.0%)]
   - Group 12: **0.4696** | CAROUSEL, ADIDAS, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
   - Group 13: **0.5599** | BAT, SPIDER, DUST, SUPER                                          | INCORRECT (Max overlap: 3/4 with ___ MAN SUPERHEROES) | [Pred Type: FILL_IN_THE_BLANK (45.5%, no-rel 18.3%)]
   - Group 14: **0.4471** | SWEEP, MOP, IRON, VACUUM                                          | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 15: **0.4772** | CAROUSEL, ADIDAS, CATS, CABARET                                   | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
   - Group 16: **0.4719** | REEBOK, PUMA, NIKE, CHICAGO                                       | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (49.1%, no-rel 17.4%)]
   - Group 17: **0.4948** | REEBOK, ADIDAS, CABARET, CHICAGO                                  | INCORRECT (Max overlap: 2/4 with SNEAKER BRANDS)
   - Group 18: **0.4636** | CAROUSEL, PUMA, CATS, NIKE                                        | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (51.3%, no-rel 19.0%)]
   - Group 19: **0.4760** | ADIDAS, PUMA, NIKE, CHICAGO                                       | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (49.8%, no-rel 18.0%)]
   - Group 20: **0.4690** | CAROUSEL, REEBOK, CATS, CABARET                                   | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)

---

## Puzzle 58 (ID: 906)
**Words on Board:** IKEA FURNITURE, MODEL, ROSTRUM, PUZZLE, SWILL, SPOON, NUZZLE, POUND DOWN, MUZZLE, PROBOSCIS, HOLD TIGHT, KNOCK BACK, BEAK, LEGO SET, GUZZLE, DRAW CLOSE

### Ground Truth Categories:
* **Level 0 (CUDDLE) [Type: SYNONYM_OR_NEAR]:** DRAW CLOSE, HOLD TIGHT, NUZZLE, SPOON
* **Level 1 (IMBIBE) [Type: SYNONYM_OR_NEAR]:** GUZZLE, KNOCK BACK, POUND DOWN, SWILL
* **Level 2 (THINGS YOU ASSEMBLE) [Type: SEMANTIC_SET]:** IKEA FURNITURE, LEGO SET, MODEL, PUZZLE
* **Level 3 (SNOUTS) [Type: SYNONYM_OR_NEAR]:** BEAK, MUZZLE, PROBOSCIS, ROSTRUM

### Top Candidate Partitions:
1. **Partition Score: 0.4663**
   - Group 1: **0.6089** | POUND DOWN, HOLD TIGHT, KNOCK BACK, DRAW CLOSE                    | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 2: **0.5598** | SWILL, NUZZLE, MUZZLE, GUZZLE                                     | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 3: **0.4321** | ROSTRUM, SPOON, PROBOSCIS, BEAK                                   | INCORRECT (Max overlap: 3/4 with SNOUTS)
   - Group 4: **0.4133** | IKEA FURNITURE, MODEL, PUZZLE, LEGO SET                           | CORRECT GROUP (THINGS YOU ASSEMBLE, Level 2)
2. **Partition Score: 0.4654**
   - Group 1: **0.6089** | POUND DOWN, HOLD TIGHT, KNOCK BACK, DRAW CLOSE                    | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 2: **0.5360** | ROSTRUM, MUZZLE, PROBOSCIS, BEAK                                  | CORRECT GROUP (SNOUTS, Level 3) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 26.7%)]
   - Group 3: **0.4363** | MODEL, SWILL, NUZZLE, GUZZLE                                      | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 4: **0.4187** | IKEA FURNITURE, PUZZLE, SPOON, LEGO SET                           | INCORRECT (Max overlap: 3/4 with THINGS YOU ASSEMBLE)
3. **Partition Score: 0.4648**
   - Group 1: **0.6089** | POUND DOWN, HOLD TIGHT, KNOCK BACK, DRAW CLOSE                    | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 2: **0.5059** | PUZZLE, NUZZLE, MUZZLE, GUZZLE                                    | INCORRECT (Max overlap: 1/4 with THINGS YOU ASSEMBLE)
   - Group 3: **0.4361** | ROSTRUM, SWILL, PROBOSCIS, BEAK                                   | INCORRECT (Max overlap: 3/4 with SNOUTS)
   - Group 4: **0.4287** | IKEA FURNITURE, MODEL, SPOON, LEGO SET                            | INCORRECT (Max overlap: 3/4 with THINGS YOU ASSEMBLE)
4. **Partition Score: 0.4646**
   - Group 1: **0.6089** | POUND DOWN, HOLD TIGHT, KNOCK BACK, DRAW CLOSE                    | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 2: **0.5360** | ROSTRUM, MUZZLE, PROBOSCIS, BEAK                                  | CORRECT GROUP (SNOUTS, Level 3) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 26.7%)]
   - Group 3: **0.4287** | IKEA FURNITURE, MODEL, SPOON, LEGO SET                            | INCORRECT (Max overlap: 3/4 with THINGS YOU ASSEMBLE)
   - Group 4: **0.4200** | PUZZLE, SWILL, NUZZLE, GUZZLE                                     | INCORRECT (Max overlap: 2/4 with IMBIBE) | [Pred Type: SYNONYM_OR_NEAR (45.5%, no-rel 24.0%)]
5. **Partition Score: 0.4633**
   - Group 1: **0.6089** | POUND DOWN, HOLD TIGHT, KNOCK BACK, DRAW CLOSE                    | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 2: **0.5598** | SWILL, NUZZLE, MUZZLE, GUZZLE                                     | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 3: **0.4287** | IKEA FURNITURE, MODEL, SPOON, LEGO SET                            | INCORRECT (Max overlap: 3/4 with THINGS YOU ASSEMBLE)
   - Group 4: **0.4087** | ROSTRUM, PUZZLE, PROBOSCIS, BEAK                                  | INCORRECT (Max overlap: 3/4 with SNOUTS) | [Pred Type: SYNONYM_OR_NEAR (45.9%, no-rel 17.7%)]

### Top Candidate Groups:
   - Group 1: **0.6089** | POUND DOWN, HOLD TIGHT, KNOCK BACK, DRAW CLOSE                    | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 2: **0.5598** | SWILL, NUZZLE, MUZZLE, GUZZLE                                     | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 3: **0.4321** | ROSTRUM, SPOON, PROBOSCIS, BEAK                                   | INCORRECT (Max overlap: 3/4 with SNOUTS)
   - Group 4: **0.4133** | IKEA FURNITURE, MODEL, PUZZLE, LEGO SET                           | CORRECT GROUP (THINGS YOU ASSEMBLE, Level 2)
   - Group 5: **0.5360** | ROSTRUM, MUZZLE, PROBOSCIS, BEAK                                  | CORRECT GROUP (SNOUTS, Level 3) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 26.7%)]
   - Group 6: **0.4363** | MODEL, SWILL, NUZZLE, GUZZLE                                      | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 7: **0.4187** | IKEA FURNITURE, PUZZLE, SPOON, LEGO SET                           | INCORRECT (Max overlap: 3/4 with THINGS YOU ASSEMBLE)
   - Group 8: **0.5059** | PUZZLE, NUZZLE, MUZZLE, GUZZLE                                    | INCORRECT (Max overlap: 1/4 with THINGS YOU ASSEMBLE)
   - Group 9: **0.4361** | ROSTRUM, SWILL, PROBOSCIS, BEAK                                   | INCORRECT (Max overlap: 3/4 with SNOUTS)
   - Group 10: **0.4287** | IKEA FURNITURE, MODEL, SPOON, LEGO SET                            | INCORRECT (Max overlap: 3/4 with THINGS YOU ASSEMBLE)
   - Group 11: **0.4200** | PUZZLE, SWILL, NUZZLE, GUZZLE                                     | INCORRECT (Max overlap: 2/4 with IMBIBE) | [Pred Type: SYNONYM_OR_NEAR (45.5%, no-rel 24.0%)]
   - Group 12: **0.4087** | ROSTRUM, PUZZLE, PROBOSCIS, BEAK                                  | INCORRECT (Max overlap: 3/4 with SNOUTS) | [Pred Type: SYNONYM_OR_NEAR (45.9%, no-rel 17.7%)]
   - Group 13: **0.4000** | MODEL, ROSTRUM, PROBOSCIS, BEAK                                   | INCORRECT (Max overlap: 3/4 with SNOUTS)
   - Group 14: **0.4927** | IKEA FURNITURE, POUND DOWN, HOLD TIGHT, DRAW CLOSE                | INCORRECT (Max overlap: 2/4 with CUDDLE)
   - Group 15: **0.4735** | ROSTRUM, PROBOSCIS, KNOCK BACK, BEAK                              | INCORRECT (Max overlap: 3/4 with SNOUTS)
   - Group 16: **0.4108** | MODEL, PUZZLE, SPOON, LEGO SET                                    | INCORRECT (Max overlap: 3/4 with THINGS YOU ASSEMBLE)
   - Group 17: **0.4022** | SWILL, SPOON, NUZZLE, GUZZLE                                      | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 18: **0.4773** | ROSTRUM, PROBOSCIS, BEAK, DRAW CLOSE                              | INCORRECT (Max overlap: 3/4 with SNOUTS)
   - Group 19: **0.4724** | IKEA FURNITURE, POUND DOWN, HOLD TIGHT, KNOCK BACK                | INCORRECT (Max overlap: 2/4 with IMBIBE)
   - Group 20: **0.4843** | ROSTRUM, PROBOSCIS, HOLD TIGHT, BEAK                              | INCORRECT (Max overlap: 3/4 with SNOUTS) | [Pred Type: SYNONYM_OR_NEAR (46.1%, no-rel 22.5%)]

---

## Puzzle 59 (ID: 1036)
**Words on Board:** FAN, AUTO, HEAT, RIDE, CLAWS, BODYSUIT, ROAST, COOL, BRA, NEEDLE, WHEELS, RIB, MASK, DAY, WHIP, CAMP

### Ground Truth Categories:
* **Level 0 (TEASE) [Type: SYNONYM_OR_NEAR]:** NEEDLE, RIB, RIDE, ROAST
* **Level 1 (THERMOSTAT SETTINGS) [Type: SEMANTIC_SET]:** AUTO, COOL, FAN, HEAT
* **Level 2 (FEATURES OF A CATWOMAN COSTUME) [Type: SEMANTIC_SET]:** BODYSUIT, CLAWS, MASK, WHIP
* **Level 3 (TRAINING ___) [Type: FILL_IN_THE_BLANK]:** BRA, CAMP, DAY, WHEELS

### Top Candidate Partitions:
1. **Partition Score: 0.4837**
   - Group 1: **0.5089** | HEAT, ROAST, COOL, MASK                                           | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 2: **0.4889** | BRA, NEEDLE, RIB, WHIP                                            | INCORRECT (Max overlap: 2/4 with TEASE)
   - Group 3: **0.4862** | AUTO, CLAWS, BODYSUIT, WHEELS                                     | INCORRECT (Max overlap: 2/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 4: **0.4755** | FAN, RIDE, DAY, CAMP                                              | INCORRECT (Max overlap: 2/4 with TRAINING ___)
2. **Partition Score: 0.4795**
   - Group 1: **0.5303** | CLAWS, NEEDLE, RIB, WHIP                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 2: **0.5089** | HEAT, ROAST, COOL, MASK                                           | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 3: **0.4755** | FAN, RIDE, DAY, CAMP                                              | INCORRECT (Max overlap: 2/4 with TRAINING ___)
   - Group 4: **0.4592** | AUTO, BODYSUIT, BRA, WHEELS                                       | INCORRECT (Max overlap: 2/4 with TRAINING ___)
3. **Partition Score: 0.4735**
   - Group 1: **0.4889** | BRA, NEEDLE, RIB, WHIP                                            | INCORRECT (Max overlap: 2/4 with TEASE)
   - Group 2: **0.4862** | AUTO, CLAWS, BODYSUIT, WHEELS                                     | INCORRECT (Max overlap: 2/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 3: **0.4717** | HEAT, RIDE, ROAST, COOL                                           | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 4: **0.4661** | FAN, MASK, DAY, CAMP                                              | INCORRECT (Max overlap: 2/4 with TRAINING ___)
4. **Partition Score: 0.4708**
   - Group 1: **0.5303** | CLAWS, NEEDLE, RIB, WHIP                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 2: **0.4717** | HEAT, RIDE, ROAST, COOL                                           | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 3: **0.4661** | FAN, MASK, DAY, CAMP                                              | INCORRECT (Max overlap: 2/4 with TRAINING ___)
   - Group 4: **0.4592** | AUTO, BODYSUIT, BRA, WHEELS                                       | INCORRECT (Max overlap: 2/4 with TRAINING ___)
5. **Partition Score: 0.4669**
   - Group 1: **0.5039** | CLAWS, NEEDLE, MASK, WHIP                                         | INCORRECT (Max overlap: 3/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 2: **0.4916** | HEAT, RIDE, ROAST, RIB                                            | INCORRECT (Max overlap: 3/4 with TEASE)
   - Group 3: **0.4592** | AUTO, BODYSUIT, BRA, WHEELS                                       | INCORRECT (Max overlap: 2/4 with TRAINING ___)
   - Group 4: **0.4526** | FAN, COOL, DAY, CAMP                                              | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)

### Top Candidate Groups:
   - Group 1: **0.5089** | HEAT, ROAST, COOL, MASK                                           | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 2: **0.4889** | BRA, NEEDLE, RIB, WHIP                                            | INCORRECT (Max overlap: 2/4 with TEASE)
   - Group 3: **0.4862** | AUTO, CLAWS, BODYSUIT, WHEELS                                     | INCORRECT (Max overlap: 2/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 4: **0.4755** | FAN, RIDE, DAY, CAMP                                              | INCORRECT (Max overlap: 2/4 with TRAINING ___)
   - Group 5: **0.5303** | CLAWS, NEEDLE, RIB, WHIP                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 6: **0.4592** | AUTO, BODYSUIT, BRA, WHEELS                                       | INCORRECT (Max overlap: 2/4 with TRAINING ___)
   - Group 7: **0.4717** | HEAT, RIDE, ROAST, COOL                                           | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 8: **0.4661** | FAN, MASK, DAY, CAMP                                              | INCORRECT (Max overlap: 2/4 with TRAINING ___)
   - Group 9: **0.5039** | CLAWS, NEEDLE, MASK, WHIP                                         | INCORRECT (Max overlap: 3/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 10: **0.4916** | HEAT, RIDE, ROAST, RIB                                            | INCORRECT (Max overlap: 3/4 with TEASE)
   - Group 11: **0.4526** | FAN, COOL, DAY, CAMP                                              | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 12: **0.5214** | FAN, NEEDLE, RIB, WHIP                                            | INCORRECT (Max overlap: 2/4 with TEASE)
   - Group 13: **0.4409** | RIDE, CLAWS, DAY, CAMP                                            | INCORRECT (Max overlap: 2/4 with TRAINING ___)
   - Group 14: **0.5134** | CLAWS, NEEDLE, WHEELS, WHIP                                       | INCORRECT (Max overlap: 2/4 with FEATURES OF A CATWOMAN COSTUME)
   - Group 15: **0.5023** | FAN, COOL, MASK, CAMP                                             | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 16: **0.4316** | AUTO, BODYSUIT, BRA, DAY                                          | INCORRECT (Max overlap: 2/4 with TRAINING ___)
   - Group 17: **0.5655** | HEAT, COOL, MASK, CAMP                                            | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 18: **0.4369** | RIDE, CLAWS, ROAST, WHEELS                                        | INCORRECT (Max overlap: 2/4 with TEASE)
   - Group 19: **0.5103** | HEAT, ROAST, COOL, CAMP                                           | INCORRECT (Max overlap: 2/4 with THERMOSTAT SETTINGS)
   - Group 20: **0.4701** | RIDE, CLAWS, WHEELS, MASK                                         | INCORRECT (Max overlap: 2/4 with FEATURES OF A CATWOMAN COSTUME)

---

## Puzzle 60 (ID: 894)
**Words on Board:** CHAYOTE, SPLASH, DROP, SWEETHEART, SWAB, BITTER MELON, PLEA, SOURSOP, DAB, TOUCH, SKIPPER, DURIAN, BIG, SALTY DOG, TAR, RAW

### Ground Truth Categories:
* **Level 0 (LITTLE BIT) [Type: SYNONYM_OR_NEAR]:** DAB, DROP, SPLASH, TOUCH
* **Level 1 (SAILOR) [Type: SYNONYM_OR_NEAR]:** SALTY DOG, SKIPPER, SWAB, TAR
* **Level 2 (TROPICAL FRUITS/VEGETABLES) [Type: NAMED_ENTITY_SET]:** BITTER MELON, CHAYOTE, DURIAN, SOURSOP
* **Level 3 (___ DEAL) [Type: FILL_IN_THE_BLANK]:** BIG, PLEA, RAW, SWEETHEART

### Top Candidate Partitions:
1. **Partition Score: 0.5004**
   - Group 1: **0.6359** | SPLASH, DROP, SWAB, DAB                                           | INCORRECT (Max overlap: 3/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (61.2%, no-rel 31.1%)]
   - Group 2: **0.6024** | CHAYOTE, BITTER MELON, SOURSOP, DURIAN                            | CORRECT GROUP (TROPICAL FRUITS/VEGETABLES, Level 2)
   - Group 3: **0.4570** | TOUCH, BIG, TAR, RAW                                              | INCORRECT (Max overlap: 2/4 with ___ DEAL)
   - Group 4: **0.4493** | SWEETHEART, PLEA, SKIPPER, SALTY DOG                              | INCORRECT (Max overlap: 2/4 with ___ DEAL)
2. **Partition Score: 0.4959**
   - Group 1: **0.5308** | SPLASH, SWAB, PLEA, DAB                                           | INCORRECT (Max overlap: 2/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (69.8%, no-rel 20.4%)]
   - Group 2: **0.5089** | DROP, TOUCH, BIG, RAW                                             | INCORRECT (Max overlap: 2/4 with LITTLE BIT)
   - Group 3: **0.4908** | CHAYOTE, SOURSOP, DURIAN, TAR                                     | INCORRECT (Max overlap: 3/4 with TROPICAL FRUITS/VEGETABLES)
   - Group 4: **0.4853** | SWEETHEART, BITTER MELON, SKIPPER, SALTY DOG                      | INCORRECT (Max overlap: 2/4 with SAILOR)
3. **Partition Score: 0.4933**
   - Group 1: **0.5308** | SPLASH, SWAB, PLEA, DAB                                           | INCORRECT (Max overlap: 2/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (69.8%, no-rel 20.4%)]
   - Group 2: **0.5089** | DROP, TOUCH, BIG, RAW                                             | INCORRECT (Max overlap: 2/4 with LITTLE BIT)
   - Group 3: **0.4843** | BITTER MELON, SOURSOP, DURIAN, TAR                                | INCORRECT (Max overlap: 3/4 with TROPICAL FRUITS/VEGETABLES)
   - Group 4: **0.4826** | CHAYOTE, SWEETHEART, SKIPPER, SALTY DOG                           | INCORRECT (Max overlap: 2/4 with SAILOR)
4. **Partition Score: 0.4909**
   - Group 1: **0.6327** | SPLASH, SWAB, DAB, TOUCH                                          | INCORRECT (Max overlap: 3/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (64.0%, no-rel 27.9%)]
   - Group 2: **0.6024** | CHAYOTE, BITTER MELON, SOURSOP, DURIAN                            | CORRECT GROUP (TROPICAL FRUITS/VEGETABLES, Level 2)
   - Group 3: **0.4493** | SWEETHEART, PLEA, SKIPPER, SALTY DOG                              | INCORRECT (Max overlap: 2/4 with ___ DEAL)
   - Group 4: **0.4342** | DROP, BIG, TAR, RAW                                               | INCORRECT (Max overlap: 2/4 with ___ DEAL)
5. **Partition Score: 0.4883**
   - Group 1: **0.6024** | CHAYOTE, BITTER MELON, SOURSOP, DURIAN                            | CORRECT GROUP (TROPICAL FRUITS/VEGETABLES, Level 2)
   - Group 2: **0.5308** | SPLASH, SWAB, PLEA, DAB                                           | INCORRECT (Max overlap: 2/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (69.8%, no-rel 20.4%)]
   - Group 3: **0.5089** | DROP, TOUCH, BIG, RAW                                             | INCORRECT (Max overlap: 2/4 with LITTLE BIT)
   - Group 4: **0.4401** | SWEETHEART, SKIPPER, SALTY DOG, TAR                               | INCORRECT (Max overlap: 3/4 with SAILOR)

### Top Candidate Groups:
   - Group 1: **0.6359** | SPLASH, DROP, SWAB, DAB                                           | INCORRECT (Max overlap: 3/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (61.2%, no-rel 31.1%)]
   - Group 2: **0.6024** | CHAYOTE, BITTER MELON, SOURSOP, DURIAN                            | CORRECT GROUP (TROPICAL FRUITS/VEGETABLES, Level 2)
   - Group 3: **0.4570** | TOUCH, BIG, TAR, RAW                                              | INCORRECT (Max overlap: 2/4 with ___ DEAL)
   - Group 4: **0.4493** | SWEETHEART, PLEA, SKIPPER, SALTY DOG                              | INCORRECT (Max overlap: 2/4 with ___ DEAL)
   - Group 5: **0.5308** | SPLASH, SWAB, PLEA, DAB                                           | INCORRECT (Max overlap: 2/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (69.8%, no-rel 20.4%)]
   - Group 6: **0.5089** | DROP, TOUCH, BIG, RAW                                             | INCORRECT (Max overlap: 2/4 with LITTLE BIT)
   - Group 7: **0.4908** | CHAYOTE, SOURSOP, DURIAN, TAR                                     | INCORRECT (Max overlap: 3/4 with TROPICAL FRUITS/VEGETABLES)
   - Group 8: **0.4853** | SWEETHEART, BITTER MELON, SKIPPER, SALTY DOG                      | INCORRECT (Max overlap: 2/4 with SAILOR)
   - Group 9: **0.4843** | BITTER MELON, SOURSOP, DURIAN, TAR                                | INCORRECT (Max overlap: 3/4 with TROPICAL FRUITS/VEGETABLES)
   - Group 10: **0.4826** | CHAYOTE, SWEETHEART, SKIPPER, SALTY DOG                           | INCORRECT (Max overlap: 2/4 with SAILOR)
   - Group 11: **0.6327** | SPLASH, SWAB, DAB, TOUCH                                          | INCORRECT (Max overlap: 3/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (64.0%, no-rel 27.9%)]
   - Group 12: **0.4342** | DROP, BIG, TAR, RAW                                               | INCORRECT (Max overlap: 2/4 with ___ DEAL)
   - Group 13: **0.4401** | SWEETHEART, SKIPPER, SALTY DOG, TAR                               | INCORRECT (Max overlap: 3/4 with SAILOR)
   - Group 14: **0.5043** | CHAYOTE, SWEETHEART, BITTER MELON, SALTY DOG                      | INCORRECT (Max overlap: 2/4 with TROPICAL FRUITS/VEGETABLES)
   - Group 15: **0.4547** | SOURSOP, SKIPPER, DURIAN, TAR                                     | INCORRECT (Max overlap: 2/4 with TROPICAL FRUITS/VEGETABLES)
   - Group 16: **0.5575** | SPLASH, SWAB, DAB, SALTY DOG                                      | INCORRECT (Max overlap: 2/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (69.3%, no-rel 20.0%)]
   - Group 17: **0.4153** | SWEETHEART, PLEA, SKIPPER, TAR                                    | INCORRECT (Max overlap: 2/4 with ___ DEAL)
   - Group 18: **0.4994** | SPLASH, SWAB, DAB, BIG                                            | INCORRECT (Max overlap: 2/4 with LITTLE BIT) | [Pred Type: SYNONYM_OR_NEAR (65.5%, no-rel 25.8%)]
   - Group 19: **0.4613** | DROP, TOUCH, TAR, RAW                                             | INCORRECT (Max overlap: 2/4 with LITTLE BIT)
   - Group 20: **0.4127** | DROP, PLEA, BIG, RAW                                              | INCORRECT (Max overlap: 3/4 with ___ DEAL)

---

## Puzzle 61 (ID: 623)
**Words on Board:** SYRUP, JAM, SCRAPE, CAN, GUTS, FERMENT, PICKLE, BUTTER, GNASH, HOT SAUCE, MILK, TEA, BEANS, GRIND, FREEZE, GRATE

### Ground Truth Categories:
* **Level 0 (RUB TOGETHER) [Type: SYNONYM_OR_NEAR]:** GNASH, GRATE, GRIND, SCRAPE
* **Level 1 (WAYS TO PRESERVE FOOD) [Type: SEMANTIC_SET]:** CAN, FERMENT, FREEZE, PICKLE
* **Level 2 (BREAKFAST CONDIMENTS) [Type: SEMANTIC_SET]:** BUTTER, HOT SAUCE, JAM, SYRUP
* **Level 3 (PROVERBIAL THINGS THAT ARE SPILLED) [Type: FILL_IN_THE_BLANK]:** BEANS, GUTS, MILK, TEA

### Top Candidate Partitions:
1. **Partition Score: 0.4661**
   - Group 1: **0.6582** | SCRAPE, GNASH, GRIND, GRATE                                       | CORRECT GROUP (RUB TOGETHER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 29.5%)]
   - Group 2: **0.4764** | SYRUP, GUTS, HOT SAUCE, BEANS                                     | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 3: **0.4327** | CAN, BUTTER, MILK, TEA                                            | INCORRECT (Max overlap: 2/4 with PROVERBIAL THINGS THAT ARE SPILLED)
   - Group 4: **0.4325** | JAM, FERMENT, PICKLE, FREEZE                                      | INCORRECT (Max overlap: 3/4 with WAYS TO PRESERVE FOOD)
2. **Partition Score: 0.4621**
   - Group 1: **0.6582** | SCRAPE, GNASH, GRIND, GRATE                                       | CORRECT GROUP (RUB TOGETHER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 29.5%)]
   - Group 2: **0.6107** | SYRUP, BUTTER, MILK, TEA                                          | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 3: **0.4160** | GUTS, FERMENT, HOT SAUCE, FREEZE                                  | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
   - Group 4: **0.3815** | JAM, CAN, PICKLE, BEANS                                           | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
3. **Partition Score: 0.4595**
   - Group 1: **0.6582** | SCRAPE, GNASH, GRIND, GRATE                                       | CORRECT GROUP (RUB TOGETHER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 29.5%)]
   - Group 2: **0.6107** | SYRUP, BUTTER, MILK, TEA                                          | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 3: **0.4014** | JAM, GUTS, FERMENT, FREEZE                                        | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
   - Group 4: **0.3818** | CAN, PICKLE, HOT SAUCE, BEANS                                     | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
4. **Partition Score: 0.4577**
   - Group 1: **0.5158** | SYRUP, BUTTER, HOT SAUCE, MILK                                    | INCORRECT (Max overlap: 3/4 with BREAKFAST CONDIMENTS)
   - Group 2: **0.4625** | SCRAPE, CAN, GRIND, GRATE                                         | INCORRECT (Max overlap: 3/4 with RUB TOGETHER) | [Pred Type: SYNONYM_OR_NEAR (60.3%, no-rel 27.6%)]
   - Group 3: **0.4498** | JAM, PICKLE, TEA, BEANS                                           | INCORRECT (Max overlap: 2/4 with PROVERBIAL THINGS THAT ARE SPILLED)
   - Group 4: **0.4461** | GUTS, FERMENT, GNASH, FREEZE                                      | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
5. **Partition Score: 0.4565**
   - Group 1: **0.6582** | SCRAPE, GNASH, GRIND, GRATE                                       | CORRECT GROUP (RUB TOGETHER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 29.5%)]
   - Group 2: **0.5257** | SYRUP, HOT SAUCE, TEA, BEANS                                      | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 3: **0.4169** | CAN, PICKLE, BUTTER, MILK                                         | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD) | [Pred Type: SEMANTIC_SET (45.7%, no-rel 33.1%)]
   - Group 4: **0.4014** | JAM, GUTS, FERMENT, FREEZE                                        | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)

### Top Candidate Groups:
   - Group 1: **0.6582** | SCRAPE, GNASH, GRIND, GRATE                                       | CORRECT GROUP (RUB TOGETHER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 29.5%)]
   - Group 2: **0.4764** | SYRUP, GUTS, HOT SAUCE, BEANS                                     | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 3: **0.4327** | CAN, BUTTER, MILK, TEA                                            | INCORRECT (Max overlap: 2/4 with PROVERBIAL THINGS THAT ARE SPILLED)
   - Group 4: **0.4325** | JAM, FERMENT, PICKLE, FREEZE                                      | INCORRECT (Max overlap: 3/4 with WAYS TO PRESERVE FOOD)
   - Group 5: **0.6107** | SYRUP, BUTTER, MILK, TEA                                          | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 6: **0.4160** | GUTS, FERMENT, HOT SAUCE, FREEZE                                  | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
   - Group 7: **0.3815** | JAM, CAN, PICKLE, BEANS                                           | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
   - Group 8: **0.4014** | JAM, GUTS, FERMENT, FREEZE                                        | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
   - Group 9: **0.3818** | CAN, PICKLE, HOT SAUCE, BEANS                                     | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
   - Group 10: **0.5158** | SYRUP, BUTTER, HOT SAUCE, MILK                                    | INCORRECT (Max overlap: 3/4 with BREAKFAST CONDIMENTS)
   - Group 11: **0.4625** | SCRAPE, CAN, GRIND, GRATE                                         | INCORRECT (Max overlap: 3/4 with RUB TOGETHER) | [Pred Type: SYNONYM_OR_NEAR (60.3%, no-rel 27.6%)]
   - Group 12: **0.4498** | JAM, PICKLE, TEA, BEANS                                           | INCORRECT (Max overlap: 2/4 with PROVERBIAL THINGS THAT ARE SPILLED)
   - Group 13: **0.4461** | GUTS, FERMENT, GNASH, FREEZE                                      | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD)
   - Group 14: **0.5257** | SYRUP, HOT SAUCE, TEA, BEANS                                      | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 15: **0.4169** | CAN, PICKLE, BUTTER, MILK                                         | INCORRECT (Max overlap: 2/4 with WAYS TO PRESERVE FOOD) | [Pred Type: SEMANTIC_SET (45.7%, no-rel 33.1%)]
   - Group 16: **0.4726** | JAM, PICKLE, BUTTER, TEA                                          | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 17: **0.4677** | SYRUP, HOT SAUCE, MILK, BEANS                                     | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 18: **0.5359** | SYRUP, HOT SAUCE, MILK, TEA                                       | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 19: **0.4363** | JAM, PICKLE, BUTTER, BEANS                                        | INCORRECT (Max overlap: 2/4 with BREAKFAST CONDIMENTS)
   - Group 20: **0.4964** | SYRUP, BUTTER, HOT SAUCE, TEA                                     | INCORRECT (Max overlap: 3/4 with BREAKFAST CONDIMENTS)

---

## Puzzle 62 (ID: 36)
**Words on Board:** DOUGH, MARS, STACKS, CRUNCH, WOMBAT, MOUNDS, TRUTH, WALLABY, CHEDDAR, GUN, KOALA, CHUNKY, EYE, MOLE RAT, KANGAROO, PAPER

### Ground Truth Categories:
* **Level 0 (MARSUPIALS) [Type: SEMANTIC_SET]:** KANGAROO, KOALA, WALLABY, WOMBAT
* **Level 1 (CHOCOLATE BARS) [Type: NAMED_ENTITY_SET]:** CHUNKY, CRUNCH, MARS, MOUNDS
* **Level 2 (SLANG FOR MONEY) [Type: SYNONYM_OR_NEAR]:** CHEDDAR, DOUGH, PAPER, STACKS
* **Level 3 (NAKED ___) [Type: FILL_IN_THE_BLANK]:** EYE, GUN, MOLE RAT, TRUTH

### Top Candidate Partitions:
1. **Partition Score: 0.5339**
   - Group 1: **0.7748** | WOMBAT, WALLABY, KOALA, KANGAROO                                  | CORRECT GROUP (MARSUPIALS, Level 0)
   - Group 2: **0.5276** | MARS, STACKS, MOUNDS, TRUTH                                       | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
   - Group 3: **0.5062** | DOUGH, CRUNCH, CHEDDAR, CHUNKY                                    | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 4: **0.4935** | GUN, EYE, MOLE RAT, PAPER                                         | INCORRECT (Max overlap: 3/4 with NAKED ___)
2. **Partition Score: 0.5323**
   - Group 1: **0.7748** | WOMBAT, WALLABY, KOALA, KANGAROO                                  | CORRECT GROUP (MARSUPIALS, Level 0)
   - Group 2: **0.5691** | TRUTH, GUN, EYE, PAPER                                            | INCORRECT (Max overlap: 3/4 with NAKED ___) | [Pred Type: FILL_IN_THE_BLANK (50.4%, no-rel 23.9%)]
   - Group 3: **0.5062** | DOUGH, CRUNCH, CHEDDAR, CHUNKY                                    | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 4: **0.4752** | MARS, STACKS, MOUNDS, MOLE RAT                                    | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
3. **Partition Score: 0.5184**
   - Group 1: **0.7748** | WOMBAT, WALLABY, KOALA, KANGAROO                                  | CORRECT GROUP (MARSUPIALS, Level 0)
   - Group 2: **0.5238** | MARS, GUN, EYE, PAPER                                             | INCORRECT (Max overlap: 2/4 with NAKED ___)
   - Group 3: **0.5062** | DOUGH, CRUNCH, CHEDDAR, CHUNKY                                    | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 4: **0.4645** | STACKS, MOUNDS, TRUTH, MOLE RAT                                   | INCORRECT (Max overlap: 2/4 with NAKED ___)
4. **Partition Score: 0.5178**
   - Group 1: **0.7748** | WOMBAT, WALLABY, KOALA, KANGAROO                                  | CORRECT GROUP (MARSUPIALS, Level 0)
   - Group 2: **0.5691** | TRUTH, GUN, EYE, PAPER                                            | INCORRECT (Max overlap: 3/4 with NAKED ___) | [Pred Type: FILL_IN_THE_BLANK (50.4%, no-rel 23.9%)]
   - Group 3: **0.4983** | DOUGH, STACKS, CRUNCH, CHUNKY                                     | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 4: **0.4497** | MARS, MOUNDS, CHEDDAR, MOLE RAT                                   | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
5. **Partition Score: 0.5162**
   - Group 1: **0.7748** | WOMBAT, WALLABY, KOALA, KANGAROO                                  | CORRECT GROUP (MARSUPIALS, Level 0)
   - Group 2: **0.5062** | DOUGH, CRUNCH, CHEDDAR, CHUNKY                                    | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 3: **0.4957** | TRUTH, GUN, EYE, MOLE RAT                                         | CORRECT GROUP (NAKED ___, Level 3) | [Pred Type: FILL_IN_THE_BLANK (45.4%, no-rel 24.2%)]
   - Group 4: **0.4707** | MARS, STACKS, MOUNDS, PAPER                                       | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)

### Top Candidate Groups:
   - Group 1: **0.7748** | WOMBAT, WALLABY, KOALA, KANGAROO                                  | CORRECT GROUP (MARSUPIALS, Level 0)
   - Group 2: **0.5276** | MARS, STACKS, MOUNDS, TRUTH                                       | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
   - Group 3: **0.5062** | DOUGH, CRUNCH, CHEDDAR, CHUNKY                                    | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 4: **0.4935** | GUN, EYE, MOLE RAT, PAPER                                         | INCORRECT (Max overlap: 3/4 with NAKED ___)
   - Group 5: **0.5691** | TRUTH, GUN, EYE, PAPER                                            | INCORRECT (Max overlap: 3/4 with NAKED ___) | [Pred Type: FILL_IN_THE_BLANK (50.4%, no-rel 23.9%)]
   - Group 6: **0.4752** | MARS, STACKS, MOUNDS, MOLE RAT                                    | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
   - Group 7: **0.5238** | MARS, GUN, EYE, PAPER                                             | INCORRECT (Max overlap: 2/4 with NAKED ___)
   - Group 8: **0.4645** | STACKS, MOUNDS, TRUTH, MOLE RAT                                   | INCORRECT (Max overlap: 2/4 with NAKED ___)
   - Group 9: **0.4983** | DOUGH, STACKS, CRUNCH, CHUNKY                                     | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 10: **0.4497** | MARS, MOUNDS, CHEDDAR, MOLE RAT                                   | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
   - Group 11: **0.4957** | TRUTH, GUN, EYE, MOLE RAT                                         | CORRECT GROUP (NAKED ___, Level 3) | [Pred Type: FILL_IN_THE_BLANK (45.4%, no-rel 24.2%)]
   - Group 12: **0.4707** | MARS, STACKS, MOUNDS, PAPER                                       | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
   - Group 13: **0.5348** | DOUGH, CRUNCH, MOUNDS, CHUNKY                                     | INCORRECT (Max overlap: 3/4 with CHOCOLATE BARS)
   - Group 14: **0.4332** | MARS, STACKS, CHEDDAR, MOLE RAT                                   | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)
   - Group 15: **0.4871** | DOUGH, CRUNCH, TRUTH, CHUNKY                                      | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
   - Group 16: **0.4778** | MARS, STACKS, MOUNDS, CHEDDAR                                     | INCORRECT (Max overlap: 2/4 with CHOCOLATE BARS)
   - Group 17: **0.5545** | STACKS, CRUNCH, MOUNDS, CHUNKY                                    | INCORRECT (Max overlap: 3/4 with CHOCOLATE BARS)
   - Group 18: **0.4672** | MARS, GUN, EYE, MOLE RAT                                          | INCORRECT (Max overlap: 3/4 with NAKED ___)
   - Group 19: **0.4550** | DOUGH, TRUTH, CHEDDAR, PAPER                                      | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 20: **0.4580** | STACKS, MOUNDS, CHEDDAR, MOLE RAT                                 | INCORRECT (Max overlap: 2/4 with SLANG FOR MONEY)

---

## Puzzle 63 (ID: 787)
**Words on Board:** SHAMMY, BADGE, UPPERCUT, CROSS, PIN, RAG, SPEC, BAIT, BROOCH, STRAP, NEEDLE, BUTTON, SQUAD, JAB, RIB, HOOK

### Ground Truth Categories:
* **Level 0 (ACCESSORY WITH A POINTY FASTENER) [Type: SEMANTIC_SET]:** BADGE, BROOCH, BUTTON, PIN
* **Level 1 (TEASE) [Type: SYNONYM_OR_NEAR]:** BAIT, NEEDLE, RAG, RIB
* **Level 2 (BOXING PUNCHES) [Type: NAMED_ENTITY_SET]:** CROSS, HOOK, JAB, UPPERCUT
* **Level 3 (MUSCLE NICKNAMES PLUS “S”) [Type: WORDPLAY_TRANSFORM]:** SHAMMY, SPEC, SQUAD, STRAP

### Top Candidate Partitions:
1. **Partition Score: 0.5306**
   - Group 1: **0.6455** | BADGE, PIN, BROOCH, BUTTON                                        | CORRECT GROUP (ACCESSORY WITH A POINTY FASTENER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.6%, no-rel 32.7%)]
   - Group 2: **0.5599** | CROSS, STRAP, NEEDLE, HOOK                                        | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES)
   - Group 3: **0.5198** | SHAMMY, UPPERCUT, SPEC, SQUAD                                     | INCORRECT (Max overlap: 3/4 with MUSCLE NICKNAMES PLUS “S”)
   - Group 4: **0.4986** | RAG, BAIT, JAB, RIB                                               | INCORRECT (Max overlap: 3/4 with TEASE)
2. **Partition Score: 0.5123**
   - Group 1: **0.6455** | BADGE, PIN, BROOCH, BUTTON                                        | CORRECT GROUP (ACCESSORY WITH A POINTY FASTENER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.6%, no-rel 32.7%)]
   - Group 2: **0.5198** | SHAMMY, UPPERCUT, SPEC, SQUAD                                     | INCORRECT (Max overlap: 3/4 with MUSCLE NICKNAMES PLUS “S”)
   - Group 3: **0.4901** | CROSS, RAG, STRAP, NEEDLE                                         | INCORRECT (Max overlap: 2/4 with TEASE)
   - Group 4: **0.4885** | BAIT, JAB, RIB, HOOK                                              | INCORRECT (Max overlap: 2/4 with TEASE) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 31.5%)]
3. **Partition Score: 0.5108**
   - Group 1: **0.5747** | BADGE, BROOCH, STRAP, BUTTON                                      | INCORRECT (Max overlap: 3/4 with ACCESSORY WITH A POINTY FASTENER)
   - Group 2: **0.5198** | SHAMMY, UPPERCUT, SPEC, SQUAD                                     | INCORRECT (Max overlap: 3/4 with MUSCLE NICKNAMES PLUS “S”)
   - Group 3: **0.4986** | RAG, BAIT, JAB, RIB                                               | INCORRECT (Max overlap: 3/4 with TEASE)
   - Group 4: **0.4980** | CROSS, PIN, NEEDLE, HOOK                                          | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES)
4. **Partition Score: 0.5046**
   - Group 1: **0.7300** | PIN, BROOCH, STRAP, BUTTON                                        | INCORRECT (Max overlap: 3/4 with ACCESSORY WITH A POINTY FASTENER)
   - Group 2: **0.5198** | SHAMMY, UPPERCUT, SPEC, SQUAD                                     | INCORRECT (Max overlap: 3/4 with MUSCLE NICKNAMES PLUS “S”)
   - Group 3: **0.4937** | CROSS, RAG, NEEDLE, RIB                                           | INCORRECT (Max overlap: 3/4 with TEASE)
   - Group 4: **0.4536** | BADGE, BAIT, JAB, HOOK                                            | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 31.7%)]
5. **Partition Score: 0.5031**
   - Group 1: **0.5739** | BADGE, PIN, BROOCH, STRAP                                         | INCORRECT (Max overlap: 3/4 with ACCESSORY WITH A POINTY FASTENER) | [Pred Type: SYNONYM_OR_NEAR (50.6%, no-rel 26.0%)]
   - Group 2: **0.5198** | SHAMMY, UPPERCUT, SPEC, SQUAD                                     | INCORRECT (Max overlap: 3/4 with MUSCLE NICKNAMES PLUS “S”)
   - Group 3: **0.4986** | RAG, BAIT, JAB, RIB                                               | INCORRECT (Max overlap: 3/4 with TEASE)
   - Group 4: **0.4831** | CROSS, NEEDLE, BUTTON, HOOK                                       | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES)

### Top Candidate Groups:
   - Group 1: **0.6455** | BADGE, PIN, BROOCH, BUTTON                                        | CORRECT GROUP (ACCESSORY WITH A POINTY FASTENER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.6%, no-rel 32.7%)]
   - Group 2: **0.5599** | CROSS, STRAP, NEEDLE, HOOK                                        | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES)
   - Group 3: **0.5198** | SHAMMY, UPPERCUT, SPEC, SQUAD                                     | INCORRECT (Max overlap: 3/4 with MUSCLE NICKNAMES PLUS “S”)
   - Group 4: **0.4986** | RAG, BAIT, JAB, RIB                                               | INCORRECT (Max overlap: 3/4 with TEASE)
   - Group 5: **0.4901** | CROSS, RAG, STRAP, NEEDLE                                         | INCORRECT (Max overlap: 2/4 with TEASE)
   - Group 6: **0.4885** | BAIT, JAB, RIB, HOOK                                              | INCORRECT (Max overlap: 2/4 with TEASE) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 31.5%)]
   - Group 7: **0.5747** | BADGE, BROOCH, STRAP, BUTTON                                      | INCORRECT (Max overlap: 3/4 with ACCESSORY WITH A POINTY FASTENER)
   - Group 8: **0.4980** | CROSS, PIN, NEEDLE, HOOK                                          | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES)
   - Group 9: **0.7300** | PIN, BROOCH, STRAP, BUTTON                                        | INCORRECT (Max overlap: 3/4 with ACCESSORY WITH A POINTY FASTENER)
   - Group 10: **0.4937** | CROSS, RAG, NEEDLE, RIB                                           | INCORRECT (Max overlap: 3/4 with TEASE)
   - Group 11: **0.4536** | BADGE, BAIT, JAB, HOOK                                            | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 31.7%)]
   - Group 12: **0.5739** | BADGE, PIN, BROOCH, STRAP                                         | INCORRECT (Max overlap: 3/4 with ACCESSORY WITH A POINTY FASTENER) | [Pred Type: SYNONYM_OR_NEAR (50.6%, no-rel 26.0%)]
   - Group 13: **0.4831** | CROSS, NEEDLE, BUTTON, HOOK                                       | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES)
   - Group 14: **0.4758** | CROSS, RAG, BAIT, RIB                                             | INCORRECT (Max overlap: 3/4 with TEASE)
   - Group 15: **0.4725** | STRAP, NEEDLE, JAB, HOOK                                          | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES)
   - Group 16: **0.5167** | RAG, BAIT, JAB, HOOK                                              | INCORRECT (Max overlap: 2/4 with TEASE) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 33.0%)]
   - Group 17: **0.4571** | CROSS, STRAP, NEEDLE, RIB                                         | INCORRECT (Max overlap: 2/4 with TEASE)
   - Group 18: **0.4783** | BAIT, BUTTON, JAB, HOOK                                           | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES) | [Pred Type: SYNONYM_OR_NEAR (52.4%, no-rel 33.7%)]
   - Group 19: **0.4752** | PIN, BAIT, JAB, HOOK                                              | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES) | [Pred Type: SYNONYM_OR_NEAR (50.3%, no-rel 34.7%)]
   - Group 20: **0.4873** | PIN, NEEDLE, JAB, HOOK                                            | INCORRECT (Max overlap: 2/4 with BOXING PUNCHES)

---

## Puzzle 64 (ID: 842)
**Words on Board:** FOGHORN, WOODEN, CREATE, CHUCK, WOODSTOCK, GUTHRIE, AWKWARD, WOOD, WOODY, CLASSICS, COULD, STIFF, SCROOGE, THEREFORE, WOODCHUCK, STILTED

### Ground Truth Categories:
* **Level 0 (UNNATURAL, AS MANNERISMS) [Type: SYNONYM_OR_NEAR]:** AWKWARD, STIFF, STILTED, WOODEN
* **Level 1 (WORDS IN A FAMOUS TONGUE TWISTER) [Type: COMMON_PHRASE]:** CHUCK, COULD, WOOD, WOODCHUCK
* **Level 2 (CARTOON BIRDS) [Type: NAMED_ENTITY_SET]:** FOGHORN, SCROOGE, WOODSTOCK, WOODY
* **Level 3 (ENDING WITH NUMBER HOMOPHONES) [Type: SOUND_OR_SPELLING]:** CLASSICS, CREATE, GUTHRIE, THEREFORE

### Top Candidate Partitions:
1. **Partition Score: 0.4955**
   - Group 1: **0.6340** | AWKWARD, STIFF, THEREFORE, STILTED                                | INCORRECT (Max overlap: 3/4 with UNNATURAL, AS MANNERISMS)
   - Group 2: **0.6120** | WOODEN, WOOD, WOODY, WOODCHUCK                                    | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER)
   - Group 3: **0.4851** | FOGHORN, WOODSTOCK, GUTHRIE, SCROOGE                              | INCORRECT (Max overlap: 3/4 with CARTOON BIRDS)
   - Group 4: **0.4263** | CREATE, CHUCK, CLASSICS, COULD                                    | INCORRECT (Max overlap: 2/4 with ENDING WITH NUMBER HOMOPHONES)
2. **Partition Score: 0.4925**
   - Group 1: **0.6340** | AWKWARD, STIFF, THEREFORE, STILTED                                | INCORRECT (Max overlap: 3/4 with UNNATURAL, AS MANNERISMS)
   - Group 2: **0.4851** | FOGHORN, WOODSTOCK, GUTHRIE, SCROOGE                              | INCORRECT (Max overlap: 3/4 with CARTOON BIRDS)
   - Group 3: **0.4754** | WOODEN, WOOD, CLASSICS, WOODCHUCK                                 | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER)
   - Group 4: **0.4704** | CREATE, CHUCK, WOODY, COULD                                       | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER)
3. **Partition Score: 0.4921**
   - Group 1: **0.6238** | CREATE, AWKWARD, STIFF, STILTED                                   | INCORRECT (Max overlap: 3/4 with UNNATURAL, AS MANNERISMS)
   - Group 2: **0.5819** | WOODEN, CHUCK, WOOD, WOODY                                        | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER) | [Pred Type: SYNONYM_OR_NEAR (48.4%, no-rel 30.5%)]
   - Group 3: **0.5100** | FOGHORN, GUTHRIE, SCROOGE, WOODCHUCK                              | INCORRECT (Max overlap: 2/4 with CARTOON BIRDS)
   - Group 4: **0.4239** | WOODSTOCK, CLASSICS, COULD, THEREFORE                             | INCORRECT (Max overlap: 2/4 with ENDING WITH NUMBER HOMOPHONES)
4. **Partition Score: 0.4913**
   - Group 1: **0.6805** | WOODEN, AWKWARD, STIFF, STILTED                                   | CORRECT GROUP (UNNATURAL, AS MANNERISMS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (45.4%, no-rel 32.1%)]
   - Group 2: **0.4851** | FOGHORN, WOODSTOCK, GUTHRIE, SCROOGE                              | INCORRECT (Max overlap: 3/4 with CARTOON BIRDS)
   - Group 3: **0.4703** | CREATE, CLASSICS, COULD, THEREFORE                                | INCORRECT (Max overlap: 3/4 with ENDING WITH NUMBER HOMOPHONES)
   - Group 4: **0.4597** | CHUCK, WOOD, WOODY, WOODCHUCK                                     | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS TONGUE TWISTER)
5. **Partition Score: 0.4896**
   - Group 1: **0.6120** | WOODEN, WOOD, WOODY, WOODCHUCK                                    | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER)
   - Group 2: **0.5740** | CREATE, AWKWARD, COULD, THEREFORE                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH NUMBER HOMOPHONES)
   - Group 3: **0.4851** | FOGHORN, WOODSTOCK, GUTHRIE, SCROOGE                              | INCORRECT (Max overlap: 3/4 with CARTOON BIRDS)
   - Group 4: **0.4335** | CHUCK, CLASSICS, STIFF, STILTED                                   | INCORRECT (Max overlap: 2/4 with UNNATURAL, AS MANNERISMS)

### Top Candidate Groups:
   - Group 1: **0.6340** | AWKWARD, STIFF, THEREFORE, STILTED                                | INCORRECT (Max overlap: 3/4 with UNNATURAL, AS MANNERISMS)
   - Group 2: **0.6120** | WOODEN, WOOD, WOODY, WOODCHUCK                                    | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER)
   - Group 3: **0.4851** | FOGHORN, WOODSTOCK, GUTHRIE, SCROOGE                              | INCORRECT (Max overlap: 3/4 with CARTOON BIRDS)
   - Group 4: **0.4263** | CREATE, CHUCK, CLASSICS, COULD                                    | INCORRECT (Max overlap: 2/4 with ENDING WITH NUMBER HOMOPHONES)
   - Group 5: **0.4754** | WOODEN, WOOD, CLASSICS, WOODCHUCK                                 | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER)
   - Group 6: **0.4704** | CREATE, CHUCK, WOODY, COULD                                       | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER)
   - Group 7: **0.6238** | CREATE, AWKWARD, STIFF, STILTED                                   | INCORRECT (Max overlap: 3/4 with UNNATURAL, AS MANNERISMS)
   - Group 8: **0.5819** | WOODEN, CHUCK, WOOD, WOODY                                        | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER) | [Pred Type: SYNONYM_OR_NEAR (48.4%, no-rel 30.5%)]
   - Group 9: **0.5100** | FOGHORN, GUTHRIE, SCROOGE, WOODCHUCK                              | INCORRECT (Max overlap: 2/4 with CARTOON BIRDS)
   - Group 10: **0.4239** | WOODSTOCK, CLASSICS, COULD, THEREFORE                             | INCORRECT (Max overlap: 2/4 with ENDING WITH NUMBER HOMOPHONES)
   - Group 11: **0.6805** | WOODEN, AWKWARD, STIFF, STILTED                                   | CORRECT GROUP (UNNATURAL, AS MANNERISMS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (45.4%, no-rel 32.1%)]
   - Group 12: **0.4703** | CREATE, CLASSICS, COULD, THEREFORE                                | INCORRECT (Max overlap: 3/4 with ENDING WITH NUMBER HOMOPHONES)
   - Group 13: **0.4597** | CHUCK, WOOD, WOODY, WOODCHUCK                                     | INCORRECT (Max overlap: 3/4 with WORDS IN A FAMOUS TONGUE TWISTER)
   - Group 14: **0.5740** | CREATE, AWKWARD, COULD, THEREFORE                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH NUMBER HOMOPHONES)
   - Group 15: **0.4335** | CHUCK, CLASSICS, STIFF, STILTED                                   | INCORRECT (Max overlap: 2/4 with UNNATURAL, AS MANNERISMS)
   - Group 16: **0.4741** | CREATE, CHUCK, COULD, THEREFORE                                   | INCORRECT (Max overlap: 2/4 with ENDING WITH NUMBER HOMOPHONES)
   - Group 17: **0.4680** | AWKWARD, CLASSICS, STIFF, STILTED                                 | INCORRECT (Max overlap: 3/4 with UNNATURAL, AS MANNERISMS)
   - Group 18: **0.4876** | FOGHORN, WOODSTOCK, CLASSICS, SCROOGE                             | INCORRECT (Max overlap: 3/4 with CARTOON BIRDS)
   - Group 19: **0.4506** | GUTHRIE, WOOD, WOODY, WOODCHUCK                                   | INCORRECT (Max overlap: 2/4 with WORDS IN A FAMOUS TONGUE TWISTER)
   - Group 20: **0.4648** | CHUCK, AWKWARD, STIFF, STILTED                                    | INCORRECT (Max overlap: 3/4 with UNNATURAL, AS MANNERISMS)

---

## Puzzle 65 (ID: 96)
**Words on Board:** HORSE, BEAM, CUTIE, SHINE, GOAT, SEEDY, ENVY, FLOOR, BUFFALO, EXCEL, COW, SHEEP, RADIATE, RINGS, GLOW, VAULT

### Ground Truth Categories:
* **Level 0 (BOVIDS) [Type: SEMANTIC_SET]:** BUFFALO, COW, GOAT, SHEEP
* **Level 1 (EMIT LIGHT) [Type: SYNONYM_OR_NEAR]:** BEAM, GLOW, RADIATE, SHINE
* **Level 2 (GYMNASTICS APPARATUS) [Type: SEMANTIC_SET]:** FLOOR, HORSE, RINGS, VAULT
* **Level 3 (WORDS THAT SOUND LIKE TWO LETTERS) [Type: SOUND_OR_SPELLING]:** CUTIE, ENVY, EXCEL, SEEDY

### Top Candidate Partitions:
1. **Partition Score: 0.5325**
   - Group 1: **0.6852** | GOAT, BUFFALO, COW, SHEEP                                         | CORRECT GROUP (BOVIDS, Level 0)
   - Group 2: **0.6659** | SHINE, EXCEL, RADIATE, GLOW                                       | INCORRECT (Max overlap: 3/4 with EMIT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (71.9%, no-rel 22.4%)]
   - Group 3: **0.5800** | HORSE, BEAM, RINGS, VAULT                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 4: **0.4328** | CUTIE, SEEDY, ENVY, FLOOR                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
2. **Partition Score: 0.5236**
   - Group 1: **0.6852** | GOAT, BUFFALO, COW, SHEEP                                         | CORRECT GROUP (BOVIDS, Level 0)
   - Group 2: **0.6659** | SHINE, EXCEL, RADIATE, GLOW                                       | INCORRECT (Max overlap: 3/4 with EMIT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (71.9%, no-rel 22.4%)]
   - Group 3: **0.5384** | HORSE, BEAM, FLOOR, RINGS                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 4: **0.4307** | CUTIE, SEEDY, ENVY, VAULT                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
3. **Partition Score: 0.5223**
   - Group 1: **0.6852** | GOAT, BUFFALO, COW, SHEEP                                         | CORRECT GROUP (BOVIDS, Level 0)
   - Group 2: **0.6659** | SHINE, EXCEL, RADIATE, GLOW                                       | INCORRECT (Max overlap: 3/4 with EMIT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (71.9%, no-rel 22.4%)]
   - Group 3: **0.5486** | HORSE, BEAM, FLOOR, VAULT                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 4: **0.4244** | CUTIE, SEEDY, ENVY, RINGS                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
4. **Partition Score: 0.5172**
   - Group 1: **0.6659** | SHINE, EXCEL, RADIATE, GLOW                                       | INCORRECT (Max overlap: 3/4 with EMIT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (71.9%, no-rel 22.4%)]
   - Group 2: **0.6049** | HORSE, GOAT, COW, SHEEP                                           | INCORRECT (Max overlap: 3/4 with BOVIDS)
   - Group 3: **0.5291** | BEAM, FLOOR, RINGS, VAULT                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 4: **0.4481** | CUTIE, SEEDY, ENVY, BUFFALO                                       | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
5. **Partition Score: 0.5134**
   - Group 1: **0.9816** | BEAM, SHINE, RADIATE, GLOW                                        | CORRECT GROUP (EMIT LIGHT, Level 1) | [Pred Type: SYNONYM_OR_NEAR (70.4%, no-rel 24.8%)]
   - Group 2: **0.6049** | HORSE, GOAT, COW, SHEEP                                           | INCORRECT (Max overlap: 3/4 with BOVIDS)
   - Group 3: **0.4481** | CUTIE, SEEDY, ENVY, BUFFALO                                       | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 4: **0.4009** | FLOOR, EXCEL, RINGS, VAULT                                        | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)

### Top Candidate Groups:
   - Group 1: **0.6852** | GOAT, BUFFALO, COW, SHEEP                                         | CORRECT GROUP (BOVIDS, Level 0)
   - Group 2: **0.6659** | SHINE, EXCEL, RADIATE, GLOW                                       | INCORRECT (Max overlap: 3/4 with EMIT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (71.9%, no-rel 22.4%)]
   - Group 3: **0.5800** | HORSE, BEAM, RINGS, VAULT                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 4: **0.4328** | CUTIE, SEEDY, ENVY, FLOOR                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 5: **0.5384** | HORSE, BEAM, FLOOR, RINGS                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 6: **0.4307** | CUTIE, SEEDY, ENVY, VAULT                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 7: **0.5486** | HORSE, BEAM, FLOOR, VAULT                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 8: **0.4244** | CUTIE, SEEDY, ENVY, RINGS                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 9: **0.6049** | HORSE, GOAT, COW, SHEEP                                           | INCORRECT (Max overlap: 3/4 with BOVIDS)
   - Group 10: **0.5291** | BEAM, FLOOR, RINGS, VAULT                                         | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 11: **0.4481** | CUTIE, SEEDY, ENVY, BUFFALO                                       | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 12: **0.9816** | BEAM, SHINE, RADIATE, GLOW                                        | CORRECT GROUP (EMIT LIGHT, Level 1) | [Pred Type: SYNONYM_OR_NEAR (70.4%, no-rel 24.8%)]
   - Group 13: **0.4009** | FLOOR, EXCEL, RINGS, VAULT                                        | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 14: **0.5200** | CUTIE, GOAT, BUFFALO, SHEEP                                       | INCORRECT (Max overlap: 3/4 with BOVIDS)
   - Group 15: **0.4528** | HORSE, FLOOR, COW, RINGS                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 16: **0.4200** | SEEDY, ENVY, EXCEL, VAULT                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 17: **0.4921** | HORSE, FLOOR, COW, VAULT                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 18: **0.4038** | SEEDY, ENVY, EXCEL, RINGS                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)
   - Group 19: **0.5775** | HORSE, GOAT, BUFFALO, COW                                         | INCORRECT (Max overlap: 3/4 with BOVIDS)
   - Group 20: **0.4372** | CUTIE, SEEDY, ENVY, SHEEP                                         | INCORRECT (Max overlap: 3/4 with WORDS THAT SOUND LIKE TWO LETTERS)

---

## Puzzle 66 (ID: 387)
**Words on Board:** ERGO, VOX, CAVEAT, STASH, LIQUID, BLAME, TOXIC, FIXED, FROZEN, QUID, SQUID, STORE, ARCADE, SQUIRREL, STOW, NUMBERS

### Ground Truth Categories:
* **Level 0 (PACK (AWAY) FOR FUTURE USE) [Type: SYNONYM_OR_NEAR]:** SQUIRREL, STASH, STORE, STOW
* **Level 1 (ADJECTIVES FOR ASSETS) [Type: FILL_IN_THE_BLANK]:** FIXED, FROZEN, LIQUID, TOXIC
* **Level 2 (LATIN WORDS) [Type: SEMANTIC_SET]:** CAVEAT, ERGO, QUID, VOX
* **Level 3 (___ GAME) [Type: FILL_IN_THE_BLANK]:** ARCADE, BLAME, NUMBERS, SQUID

### Top Candidate Partitions:
1. **Partition Score: 0.4839**
   - Group 1: **0.5711** | STASH, STORE, SQUIRREL, STOW                                      | CORRECT GROUP (PACK (AWAY) FOR FUTURE USE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 29.3%)]
   - Group 2: **0.5109** | LIQUID, TOXIC, ARCADE, NUMBERS                                    | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS)
   - Group 3: **0.4658** | ERGO, VOX, CAVEAT, SQUID                                          | INCORRECT (Max overlap: 3/4 with LATIN WORDS)
   - Group 4: **0.4614** | BLAME, FIXED, FROZEN, QUID                                        | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS) | [Pred Type: SYNONYM_OR_NEAR (71.2%, no-rel 20.7%)]
2. **Partition Score: 0.4831**
   - Group 1: **0.5711** | STASH, STORE, SQUIRREL, STOW                                      | CORRECT GROUP (PACK (AWAY) FOR FUTURE USE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 29.3%)]
   - Group 2: **0.4887** | ERGO, CAVEAT, TOXIC, SQUID                                        | INCORRECT (Max overlap: 2/4 with LATIN WORDS)
   - Group 3: **0.4838** | VOX, LIQUID, ARCADE, NUMBERS                                      | INCORRECT (Max overlap: 2/4 with ___ GAME)
   - Group 4: **0.4614** | BLAME, FIXED, FROZEN, QUID                                        | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS) | [Pred Type: SYNONYM_OR_NEAR (71.2%, no-rel 20.7%)]
3. **Partition Score: 0.4809**
   - Group 1: **0.5711** | STASH, STORE, SQUIRREL, STOW                                      | CORRECT GROUP (PACK (AWAY) FOR FUTURE USE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 29.3%)]
   - Group 2: **0.4925** | CAVEAT, BLAME, FIXED, FROZEN                                      | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS) | [Pred Type: SYNONYM_OR_NEAR (71.1%, no-rel 16.5%)]
   - Group 3: **0.4838** | VOX, LIQUID, ARCADE, NUMBERS                                      | INCORRECT (Max overlap: 2/4 with ___ GAME)
   - Group 4: **0.4558** | ERGO, TOXIC, QUID, SQUID                                          | INCORRECT (Max overlap: 2/4 with LATIN WORDS)
4. **Partition Score: 0.4785**
   - Group 1: **0.5711** | STASH, STORE, SQUIRREL, STOW                                      | CORRECT GROUP (PACK (AWAY) FOR FUTURE USE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 29.3%)]
   - Group 2: **0.4867** | ERGO, VOX, CAVEAT, TOXIC                                          | INCORRECT (Max overlap: 3/4 with LATIN WORDS)
   - Group 3: **0.4616** | LIQUID, SQUID, ARCADE, NUMBERS                                    | INCORRECT (Max overlap: 3/4 with ___ GAME)
   - Group 4: **0.4614** | BLAME, FIXED, FROZEN, QUID                                        | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS) | [Pred Type: SYNONYM_OR_NEAR (71.2%, no-rel 20.7%)]
5. **Partition Score: 0.4773**
   - Group 1: **0.5711** | STASH, STORE, SQUIRREL, STOW                                      | CORRECT GROUP (PACK (AWAY) FOR FUTURE USE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 29.3%)]
   - Group 2: **0.4958** | ERGO, CAVEAT, QUID, SQUID                                         | INCORRECT (Max overlap: 3/4 with LATIN WORDS)
   - Group 3: **0.4838** | VOX, LIQUID, ARCADE, NUMBERS                                      | INCORRECT (Max overlap: 2/4 with ___ GAME)
   - Group 4: **0.4476** | BLAME, TOXIC, FIXED, FROZEN                                       | INCORRECT (Max overlap: 3/4 with ADJECTIVES FOR ASSETS) | [Pred Type: SYNONYM_OR_NEAR (74.0%, no-rel 15.1%)]

### Top Candidate Groups:
   - Group 1: **0.5711** | STASH, STORE, SQUIRREL, STOW                                      | CORRECT GROUP (PACK (AWAY) FOR FUTURE USE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 29.3%)]
   - Group 2: **0.5109** | LIQUID, TOXIC, ARCADE, NUMBERS                                    | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS)
   - Group 3: **0.4658** | ERGO, VOX, CAVEAT, SQUID                                          | INCORRECT (Max overlap: 3/4 with LATIN WORDS)
   - Group 4: **0.4614** | BLAME, FIXED, FROZEN, QUID                                        | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS) | [Pred Type: SYNONYM_OR_NEAR (71.2%, no-rel 20.7%)]
   - Group 5: **0.4887** | ERGO, CAVEAT, TOXIC, SQUID                                        | INCORRECT (Max overlap: 2/4 with LATIN WORDS)
   - Group 6: **0.4838** | VOX, LIQUID, ARCADE, NUMBERS                                      | INCORRECT (Max overlap: 2/4 with ___ GAME)
   - Group 7: **0.4925** | CAVEAT, BLAME, FIXED, FROZEN                                      | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS) | [Pred Type: SYNONYM_OR_NEAR (71.1%, no-rel 16.5%)]
   - Group 8: **0.4558** | ERGO, TOXIC, QUID, SQUID                                          | INCORRECT (Max overlap: 2/4 with LATIN WORDS)
   - Group 9: **0.4867** | ERGO, VOX, CAVEAT, TOXIC                                          | INCORRECT (Max overlap: 3/4 with LATIN WORDS)
   - Group 10: **0.4616** | LIQUID, SQUID, ARCADE, NUMBERS                                    | INCORRECT (Max overlap: 3/4 with ___ GAME)
   - Group 11: **0.4958** | ERGO, CAVEAT, QUID, SQUID                                         | INCORRECT (Max overlap: 3/4 with LATIN WORDS)
   - Group 12: **0.4476** | BLAME, TOXIC, FIXED, FROZEN                                       | INCORRECT (Max overlap: 3/4 with ADJECTIVES FOR ASSETS) | [Pred Type: SYNONYM_OR_NEAR (74.0%, no-rel 15.1%)]
   - Group 13: **0.5348** | VOX, LIQUID, TOXIC, ARCADE                                        | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS)
   - Group 14: **0.4254** | BLAME, FIXED, FROZEN, NUMBERS                                     | INCORRECT (Max overlap: 2/4 with ___ GAME) | [Pred Type: SYNONYM_OR_NEAR (68.0%, no-rel 19.4%)]
   - Group 15: **0.5042** | VOX, LIQUID, TOXIC, NUMBERS                                       | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS)
   - Group 16: **0.4457** | ERGO, CAVEAT, SQUID, ARCADE                                       | INCORRECT (Max overlap: 2/4 with LATIN WORDS)
   - Group 17: **0.5312** | VOX, LIQUID, SQUID, ARCADE                                        | INCORRECT (Max overlap: 2/4 with ___ GAME)
   - Group 18: **0.4355** | ERGO, CAVEAT, TOXIC, NUMBERS                                      | INCORRECT (Max overlap: 2/4 with LATIN WORDS)
   - Group 19: **0.4950** | ERGO, LIQUID, TOXIC, SQUID                                        | INCORRECT (Max overlap: 2/4 with ADJECTIVES FOR ASSETS)
   - Group 20: **0.4474** | VOX, CAVEAT, ARCADE, NUMBERS                                      | INCORRECT (Max overlap: 2/4 with LATIN WORDS)

---

## Puzzle 67 (ID: 376)
**Words on Board:** TAILGATE, GO-AHEAD, RUMPELSTILTSKIN, TILT-A-WHIRL, FERRIS WHEEL, BUTTERMILK, DAVID-AND-GOLIATH, UNDERDOG, GREEN LIGHT, MERRY-GO-ROUND, CINDERELLA, RAGS-TO-RICHES, ROLLER COASTER, CLEARANCE, THUMBS-UP, BUMPER-TO-BUMPER

### Ground Truth Categories:
* **Level 0 (AMUSEMENT PARK RIDES) [Type: SEMANTIC_SET]:** FERRIS WHEEL, MERRY-GO-ROUND, ROLLER COASTER, TILT-A-WHIRL
* **Level 1 (APPROVAL) [Type: SYNONYM_OR_NEAR]:** CLEARANCE, GO-AHEAD, GREEN LIGHT, THUMBS-UP
* **Level 2 (TYPES OF COME-FROM-BEHIND STORIES) [Type: SEMANTIC_SET]:** CINDERELLA, DAVID-AND-GOLIATH, RAGS-TO-RICHES, UNDERDOG
* **Level 3 (BEGINNING WITH SYNONYMS FOR REAR END) [Type: WORDPLAY_TRANSFORM]:** BUMPER-TO-BUMPER, BUTTERMILK, RUMPELSTILTSKIN, TAILGATE

### Top Candidate Partitions:
1. **Partition Score: 0.4955**
   - Group 1: **0.5437** | RUMPELSTILTSKIN, BUTTERMILK, UNDERDOG, CINDERELLA                 | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END) | [Pred Type: NAMED_ENTITY_SET (46.1%, no-rel 16.1%)]
   - Group 2: **0.4950** | DAVID-AND-GOLIATH, GREEN LIGHT, MERRY-GO-ROUND, RAGS-TO-RICHES    | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 3: **0.4880** | GO-AHEAD, CLEARANCE, THUMBS-UP, BUMPER-TO-BUMPER                  | INCORRECT (Max overlap: 3/4 with APPROVAL)
   - Group 4: **0.4878** | TAILGATE, TILT-A-WHIRL, FERRIS WHEEL, ROLLER COASTER              | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
2. **Partition Score: 0.4928**
   - Group 1: **0.5745** | TILT-A-WHIRL, FERRIS WHEEL, GREEN LIGHT, ROLLER COASTER           | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 2: **0.5437** | RUMPELSTILTSKIN, BUTTERMILK, UNDERDOG, CINDERELLA                 | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END) | [Pred Type: NAMED_ENTITY_SET (46.1%, no-rel 16.1%)]
   - Group 3: **0.4900** | DAVID-AND-GOLIATH, MERRY-GO-ROUND, RAGS-TO-RICHES, BUMPER-TO-BUMPER | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 4: **0.4572** | TAILGATE, GO-AHEAD, CLEARANCE, THUMBS-UP                          | INCORRECT (Max overlap: 3/4 with APPROVAL)
3. **Partition Score: 0.4893**
   - Group 1: **0.5437** | RUMPELSTILTSKIN, BUTTERMILK, UNDERDOG, CINDERELLA                 | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END) | [Pred Type: NAMED_ENTITY_SET (46.1%, no-rel 16.1%)]
   - Group 2: **0.5204** | TILT-A-WHIRL, FERRIS WHEEL, ROLLER COASTER, THUMBS-UP             | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 3: **0.4950** | DAVID-AND-GOLIATH, GREEN LIGHT, MERRY-GO-ROUND, RAGS-TO-RICHES    | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 4: **0.4639** | TAILGATE, GO-AHEAD, CLEARANCE, BUMPER-TO-BUMPER                   | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END)
4. **Partition Score: 0.4888**
   - Group 1: **0.5437** | RUMPELSTILTSKIN, BUTTERMILK, UNDERDOG, CINDERELLA                 | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END) | [Pred Type: NAMED_ENTITY_SET (46.1%, no-rel 16.1%)]
   - Group 2: **0.5360** | TILT-A-WHIRL, FERRIS WHEEL, ROLLER COASTER, BUMPER-TO-BUMPER      | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 3: **0.4950** | DAVID-AND-GOLIATH, GREEN LIGHT, MERRY-GO-ROUND, RAGS-TO-RICHES    | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 4: **0.4572** | TAILGATE, GO-AHEAD, CLEARANCE, THUMBS-UP                          | INCORRECT (Max overlap: 3/4 with APPROVAL)
5. **Partition Score: 0.4861**
   - Group 1: **0.5521** | FERRIS WHEEL, GREEN LIGHT, MERRY-GO-ROUND, ROLLER COASTER         | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 2: **0.5437** | RUMPELSTILTSKIN, BUTTERMILK, UNDERDOG, CINDERELLA                 | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END) | [Pred Type: NAMED_ENTITY_SET (46.1%, no-rel 16.1%)]
   - Group 3: **0.4681** | TILT-A-WHIRL, DAVID-AND-GOLIATH, RAGS-TO-RICHES, BUMPER-TO-BUMPER | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 4: **0.4572** | TAILGATE, GO-AHEAD, CLEARANCE, THUMBS-UP                          | INCORRECT (Max overlap: 3/4 with APPROVAL)

### Top Candidate Groups:
   - Group 1: **0.5437** | RUMPELSTILTSKIN, BUTTERMILK, UNDERDOG, CINDERELLA                 | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END) | [Pred Type: NAMED_ENTITY_SET (46.1%, no-rel 16.1%)]
   - Group 2: **0.4950** | DAVID-AND-GOLIATH, GREEN LIGHT, MERRY-GO-ROUND, RAGS-TO-RICHES    | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 3: **0.4880** | GO-AHEAD, CLEARANCE, THUMBS-UP, BUMPER-TO-BUMPER                  | INCORRECT (Max overlap: 3/4 with APPROVAL)
   - Group 4: **0.4878** | TAILGATE, TILT-A-WHIRL, FERRIS WHEEL, ROLLER COASTER              | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 5: **0.5745** | TILT-A-WHIRL, FERRIS WHEEL, GREEN LIGHT, ROLLER COASTER           | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 6: **0.4900** | DAVID-AND-GOLIATH, MERRY-GO-ROUND, RAGS-TO-RICHES, BUMPER-TO-BUMPER | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 7: **0.4572** | TAILGATE, GO-AHEAD, CLEARANCE, THUMBS-UP                          | INCORRECT (Max overlap: 3/4 with APPROVAL)
   - Group 8: **0.5204** | TILT-A-WHIRL, FERRIS WHEEL, ROLLER COASTER, THUMBS-UP             | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 9: **0.4639** | TAILGATE, GO-AHEAD, CLEARANCE, BUMPER-TO-BUMPER                   | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END)
   - Group 10: **0.5360** | TILT-A-WHIRL, FERRIS WHEEL, ROLLER COASTER, BUMPER-TO-BUMPER      | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 11: **0.5521** | FERRIS WHEEL, GREEN LIGHT, MERRY-GO-ROUND, ROLLER COASTER         | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 12: **0.4681** | TILT-A-WHIRL, DAVID-AND-GOLIATH, RAGS-TO-RICHES, BUMPER-TO-BUMPER | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 13: **0.6528** | TILT-A-WHIRL, FERRIS WHEEL, MERRY-GO-ROUND, ROLLER COASTER        | CORRECT GROUP (AMUSEMENT PARK RIDES, Level 0)
   - Group 14: **0.4702** | GO-AHEAD, RUMPELSTILTSKIN, UNDERDOG, CINDERELLA                   | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 15: **0.4665** | TAILGATE, CLEARANCE, THUMBS-UP, BUMPER-TO-BUMPER                  | INCORRECT (Max overlap: 2/4 with BEGINNING WITH SYNONYMS FOR REAR END)
   - Group 16: **0.4625** | BUTTERMILK, DAVID-AND-GOLIATH, GREEN LIGHT, RAGS-TO-RICHES        | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)
   - Group 17: **0.5162** | FERRIS WHEEL, GREEN LIGHT, RAGS-TO-RICHES, ROLLER COASTER         | INCORRECT (Max overlap: 2/4 with AMUSEMENT PARK RIDES)
   - Group 18: **0.4913** | TILT-A-WHIRL, DAVID-AND-GOLIATH, MERRY-GO-ROUND, BUMPER-TO-BUMPER | INCORRECT (Max overlap: 2/4 with AMUSEMENT PARK RIDES)
   - Group 19: **0.5172** | TILT-A-WHIRL, MERRY-GO-ROUND, ROLLER COASTER, BUMPER-TO-BUMPER    | INCORRECT (Max overlap: 3/4 with AMUSEMENT PARK RIDES)
   - Group 20: **0.4894** | FERRIS WHEEL, DAVID-AND-GOLIATH, GREEN LIGHT, RAGS-TO-RICHES      | INCORRECT (Max overlap: 2/4 with TYPES OF COME-FROM-BEHIND STORIES)

---

## Puzzle 68 (ID: 931)
**Words on Board:** TRIATHLON, OUTIE, COURSE, TIDE, GENE, INFINITY, DIRECTION, OPAL, CELL, TREND, TISSUE, EQUESTRIAN, ATHLETICS, SWIMMING, PROTEIN, MINNIE

### Ground Truth Categories:
* **Level 0 (TENDENCY) [Type: SYNONYM_OR_NEAR]:** COURSE, DIRECTION, TIDE, TREND
* **Level 1 (BIOLOGICAL STRUCTURES) [Type: SEMANTIC_SET]:** CELL, GENE, PROTEIN, TISSUE
* **Level 2 (SUMMER OLYMPIC EVENTS) [Type: SEMANTIC_SET]:** ATHLETICS, EQUESTRIAN, SWIMMING, TRIATHLON
* **Level 3 (CAR BRAND HOMOPHONES) [Type: SOUND_OR_SPELLING]:** INFINITY, MINNIE, OPAL, OUTIE

### Top Candidate Partitions:
1. **Partition Score: 0.5529**
   - Group 1: **0.6521** | TRIATHLON, EQUESTRIAN, ATHLETICS, SWIMMING                        | CORRECT GROUP (SUMMER OLYMPIC EVENTS, Level 2)
   - Group 2: **0.5951** | OPAL, CELL, TISSUE, PROTEIN                                       | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 3: **0.5288** | OUTIE, GENE, INFINITY, MINNIE                                     | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 4: **0.5246** | COURSE, TIDE, DIRECTION, TREND                                    | CORRECT GROUP (TENDENCY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 23.6%)]
2. **Partition Score: 0.5416**
   - Group 1: **0.6521** | TRIATHLON, EQUESTRIAN, ATHLETICS, SWIMMING                        | CORRECT GROUP (SUMMER OLYMPIC EVENTS, Level 2)
   - Group 2: **0.5921** | GENE, CELL, TISSUE, PROTEIN                                       | CORRECT GROUP (BIOLOGICAL STRUCTURES, Level 1)
   - Group 3: **0.5246** | COURSE, TIDE, DIRECTION, TREND                                    | CORRECT GROUP (TENDENCY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 23.6%)]
   - Group 4: **0.5051** | OUTIE, INFINITY, OPAL, MINNIE                                     | CORRECT GROUP (CAR BRAND HOMOPHONES, Level 3)
3. **Partition Score: 0.5397**
   - Group 1: **0.6521** | TRIATHLON, EQUESTRIAN, ATHLETICS, SWIMMING                        | CORRECT GROUP (SUMMER OLYMPIC EVENTS, Level 2)
   - Group 2: **0.5434** | OUTIE, GENE, OPAL, MINNIE                                         | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 3: **0.5246** | COURSE, TIDE, DIRECTION, TREND                                    | CORRECT GROUP (TENDENCY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 23.6%)]
   - Group 4: **0.5193** | INFINITY, CELL, TISSUE, PROTEIN                                   | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
4. **Partition Score: 0.5310**
   - Group 1: **0.5436** | TRIATHLON, ATHLETICS, SWIMMING, PROTEIN                           | INCORRECT (Max overlap: 3/4 with SUMMER OLYMPIC EVENTS)
   - Group 2: **0.5405** | OUTIE, INFINITY, EQUESTRIAN, MINNIE                               | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 3: **0.5317** | GENE, OPAL, CELL, TISSUE                                          | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 4: **0.5246** | COURSE, TIDE, DIRECTION, TREND                                    | CORRECT GROUP (TENDENCY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 23.6%)]
5. **Partition Score: 0.5231**
   - Group 1: **0.5951** | OPAL, CELL, TISSUE, PROTEIN                                       | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 2: **0.5246** | COURSE, TIDE, DIRECTION, TREND                                    | CORRECT GROUP (TENDENCY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 23.6%)]
   - Group 3: **0.5153** | TRIATHLON, INFINITY, ATHLETICS, SWIMMING                          | INCORRECT (Max overlap: 3/4 with SUMMER OLYMPIC EVENTS)
   - Group 4: **0.5096** | OUTIE, GENE, EQUESTRIAN, MINNIE                                   | INCORRECT (Max overlap: 2/4 with CAR BRAND HOMOPHONES)

### Top Candidate Groups:
   - Group 1: **0.6521** | TRIATHLON, EQUESTRIAN, ATHLETICS, SWIMMING                        | CORRECT GROUP (SUMMER OLYMPIC EVENTS, Level 2)
   - Group 2: **0.5951** | OPAL, CELL, TISSUE, PROTEIN                                       | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 3: **0.5288** | OUTIE, GENE, INFINITY, MINNIE                                     | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 4: **0.5246** | COURSE, TIDE, DIRECTION, TREND                                    | CORRECT GROUP (TENDENCY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 23.6%)]
   - Group 5: **0.5921** | GENE, CELL, TISSUE, PROTEIN                                       | CORRECT GROUP (BIOLOGICAL STRUCTURES, Level 1)
   - Group 6: **0.5051** | OUTIE, INFINITY, OPAL, MINNIE                                     | CORRECT GROUP (CAR BRAND HOMOPHONES, Level 3)
   - Group 7: **0.5434** | OUTIE, GENE, OPAL, MINNIE                                         | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 8: **0.5193** | INFINITY, CELL, TISSUE, PROTEIN                                   | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 9: **0.5436** | TRIATHLON, ATHLETICS, SWIMMING, PROTEIN                           | INCORRECT (Max overlap: 3/4 with SUMMER OLYMPIC EVENTS)
   - Group 10: **0.5405** | OUTIE, INFINITY, EQUESTRIAN, MINNIE                               | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 11: **0.5317** | GENE, OPAL, CELL, TISSUE                                          | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 12: **0.5153** | TRIATHLON, INFINITY, ATHLETICS, SWIMMING                          | INCORRECT (Max overlap: 3/4 with SUMMER OLYMPIC EVENTS)
   - Group 13: **0.5096** | OUTIE, GENE, EQUESTRIAN, MINNIE                                   | INCORRECT (Max overlap: 2/4 with CAR BRAND HOMOPHONES)
   - Group 14: **0.5443** | CELL, TISSUE, PROTEIN, MINNIE                                     | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 15: **0.4786** | OUTIE, GENE, INFINITY, OPAL                                       | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 16: **0.6136** | GENE, OPAL, CELL, PROTEIN                                         | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 17: **0.4527** | OUTIE, INFINITY, TISSUE, MINNIE                                   | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 18: **0.5110** | CELL, TISSUE, EQUESTRIAN, PROTEIN                                 | INCORRECT (Max overlap: 3/4 with BIOLOGICAL STRUCTURES)
   - Group 19: **0.4973** | OUTIE, OPAL, EQUESTRIAN, MINNIE                                   | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)
   - Group 20: **0.4962** | GENE, INFINITY, OPAL, MINNIE                                      | INCORRECT (Max overlap: 3/4 with CAR BRAND HOMOPHONES)

---

## Puzzle 69 (ID: 698)
**Words on Board:** FAINT, BRIGHTNESS, QUOTIENT, TINT, COLOR, PRODUCT, DRAPE, BLIND, SHUTTER, DIM, DIFFERENCE, CONTRAST, SHADE, REMOTE, VAGUE, SUM

### Ground Truth Categories:
* **Level 0 (TV DISPLAY SETTINGS) [Type: SEMANTIC_SET]:** BRIGHTNESS, COLOR, CONTRAST, TINT
* **Level 1 (FUZZY, AS A MEMORY) [Type: SYNONYM_OR_NEAR]:** DIM, FAINT, REMOTE, VAGUE
* **Level 2 (RESULTS OF SOME ARITHMETIC) [Type: SEMANTIC_SET]:** DIFFERENCE, PRODUCT, QUOTIENT, SUM
* **Level 3 (WINDOW TREATMENTS IN THE SINGULAR) [Type: SEMANTIC_SET]:** BLIND, DRAPE, SHADE, SHUTTER

### Top Candidate Partitions:
1. **Partition Score: 0.4517**
   - Group 1: **0.5782** | BRIGHTNESS, TINT, COLOR, SHADE                                    | INCORRECT (Max overlap: 3/4 with TV DISPLAY SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (52.4%, no-rel 25.2%)]
   - Group 2: **0.4702** | FAINT, DRAPE, BLIND, SHUTTER                                      | INCORRECT (Max overlap: 3/4 with WINDOW TREATMENTS IN THE SINGULAR)
   - Group 3: **0.4527** | QUOTIENT, PRODUCT, DIFFERENCE, CONTRAST                           | INCORRECT (Max overlap: 3/4 with RESULTS OF SOME ARITHMETIC) | [Pred Type: SYNONYM_OR_NEAR (46.4%, no-rel 33.5%)]
   - Group 4: **0.4168** | DIM, REMOTE, VAGUE, SUM                                           | INCORRECT (Max overlap: 3/4 with FUZZY, AS A MEMORY)
2. **Partition Score: 0.4462**
   - Group 1: **0.4748** | BRIGHTNESS, DIM, REMOTE, VAGUE                                    | INCORRECT (Max overlap: 3/4 with FUZZY, AS A MEMORY)
   - Group 2: **0.4702** | FAINT, DRAPE, BLIND, SHUTTER                                      | INCORRECT (Max overlap: 3/4 with WINDOW TREATMENTS IN THE SINGULAR)
   - Group 3: **0.4527** | QUOTIENT, PRODUCT, DIFFERENCE, CONTRAST                           | INCORRECT (Max overlap: 3/4 with RESULTS OF SOME ARITHMETIC) | [Pred Type: SYNONYM_OR_NEAR (46.4%, no-rel 33.5%)]
   - Group 4: **0.4288** | TINT, COLOR, SHADE, SUM                                           | INCORRECT (Max overlap: 2/4 with TV DISPLAY SETTINGS)
3. **Partition Score: 0.4448**
   - Group 1: **0.4933** | TINT, COLOR, PRODUCT, SHADE                                       | INCORRECT (Max overlap: 2/4 with TV DISPLAY SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (51.1%, no-rel 25.7%)]
   - Group 2: **0.4702** | FAINT, DRAPE, BLIND, SHUTTER                                      | INCORRECT (Max overlap: 3/4 with WINDOW TREATMENTS IN THE SINGULAR)
   - Group 3: **0.4671** | BRIGHTNESS, QUOTIENT, DIFFERENCE, CONTRAST                        | INCORRECT (Max overlap: 2/4 with TV DISPLAY SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 24.4%)]
   - Group 4: **0.4168** | DIM, REMOTE, VAGUE, SUM                                           | INCORRECT (Max overlap: 3/4 with FUZZY, AS A MEMORY)
4. **Partition Score: 0.4444**
   - Group 1: **0.5757** | FAINT, BLIND, DIM, SHADE                                          | INCORRECT (Max overlap: 2/4 with FUZZY, AS A MEMORY) | [Pred Type: SYNONYM_OR_NEAR (55.0%, no-rel 33.0%)]
   - Group 2: **0.5274** | BRIGHTNESS, TINT, COLOR, CONTRAST                                 | CORRECT GROUP (TV DISPLAY SETTINGS, Level 0)
   - Group 3: **0.4096** | QUOTIENT, DRAPE, SHUTTER, DIFFERENCE                              | INCORRECT (Max overlap: 2/4 with RESULTS OF SOME ARITHMETIC)
   - Group 4: **0.3979** | PRODUCT, REMOTE, VAGUE, SUM                                       | INCORRECT (Max overlap: 2/4 with RESULTS OF SOME ARITHMETIC)
5. **Partition Score: 0.4443**
   - Group 1: **0.6750** | TINT, COLOR, BLIND, SHADE                                         | INCORRECT (Max overlap: 2/4 with TV DISPLAY SETTINGS)
   - Group 2: **0.4527** | QUOTIENT, PRODUCT, DIFFERENCE, CONTRAST                           | INCORRECT (Max overlap: 3/4 with RESULTS OF SOME ARITHMETIC) | [Pred Type: SYNONYM_OR_NEAR (46.4%, no-rel 33.5%)]
   - Group 3: **0.4168** | DIM, REMOTE, VAGUE, SUM                                           | INCORRECT (Max overlap: 3/4 with FUZZY, AS A MEMORY)
   - Group 4: **0.4007** | FAINT, BRIGHTNESS, DRAPE, SHUTTER                                 | INCORRECT (Max overlap: 2/4 with WINDOW TREATMENTS IN THE SINGULAR)

### Top Candidate Groups:
   - Group 1: **0.5782** | BRIGHTNESS, TINT, COLOR, SHADE                                    | INCORRECT (Max overlap: 3/4 with TV DISPLAY SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (52.4%, no-rel 25.2%)]
   - Group 2: **0.4702** | FAINT, DRAPE, BLIND, SHUTTER                                      | INCORRECT (Max overlap: 3/4 with WINDOW TREATMENTS IN THE SINGULAR)
   - Group 3: **0.4527** | QUOTIENT, PRODUCT, DIFFERENCE, CONTRAST                           | INCORRECT (Max overlap: 3/4 with RESULTS OF SOME ARITHMETIC) | [Pred Type: SYNONYM_OR_NEAR (46.4%, no-rel 33.5%)]
   - Group 4: **0.4168** | DIM, REMOTE, VAGUE, SUM                                           | INCORRECT (Max overlap: 3/4 with FUZZY, AS A MEMORY)
   - Group 5: **0.4748** | BRIGHTNESS, DIM, REMOTE, VAGUE                                    | INCORRECT (Max overlap: 3/4 with FUZZY, AS A MEMORY)
   - Group 6: **0.4288** | TINT, COLOR, SHADE, SUM                                           | INCORRECT (Max overlap: 2/4 with TV DISPLAY SETTINGS)
   - Group 7: **0.4933** | TINT, COLOR, PRODUCT, SHADE                                       | INCORRECT (Max overlap: 2/4 with TV DISPLAY SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (51.1%, no-rel 25.7%)]
   - Group 8: **0.4671** | BRIGHTNESS, QUOTIENT, DIFFERENCE, CONTRAST                        | INCORRECT (Max overlap: 2/4 with TV DISPLAY SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 24.4%)]
   - Group 9: **0.5757** | FAINT, BLIND, DIM, SHADE                                          | INCORRECT (Max overlap: 2/4 with FUZZY, AS A MEMORY) | [Pred Type: SYNONYM_OR_NEAR (55.0%, no-rel 33.0%)]
   - Group 10: **0.5274** | BRIGHTNESS, TINT, COLOR, CONTRAST                                 | CORRECT GROUP (TV DISPLAY SETTINGS, Level 0)
   - Group 11: **0.4096** | QUOTIENT, DRAPE, SHUTTER, DIFFERENCE                              | INCORRECT (Max overlap: 2/4 with RESULTS OF SOME ARITHMETIC)
   - Group 12: **0.3979** | PRODUCT, REMOTE, VAGUE, SUM                                       | INCORRECT (Max overlap: 2/4 with RESULTS OF SOME ARITHMETIC)
   - Group 13: **0.6750** | TINT, COLOR, BLIND, SHADE                                         | INCORRECT (Max overlap: 2/4 with TV DISPLAY SETTINGS)
   - Group 14: **0.4007** | FAINT, BRIGHTNESS, DRAPE, SHUTTER                                 | INCORRECT (Max overlap: 2/4 with WINDOW TREATMENTS IN THE SINGULAR)
   - Group 15: **0.6342** | TINT, COLOR, CONTRAST, SHADE                                      | INCORRECT (Max overlap: 3/4 with TV DISPLAY SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (54.0%, no-rel 28.4%)]
   - Group 16: **0.4827** | FAINT, BRIGHTNESS, BLIND, DIM                                     | INCORRECT (Max overlap: 2/4 with FUZZY, AS A MEMORY) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 28.0%)]
   - Group 17: **0.6067** | FAINT, DIM, REMOTE, VAGUE                                         | CORRECT GROUP (FUZZY, AS A MEMORY, Level 1)
   - Group 18: **0.4076** | BRIGHTNESS, DRAPE, BLIND, SHUTTER                                 | INCORRECT (Max overlap: 3/4 with WINDOW TREATMENTS IN THE SINGULAR)
   - Group 19: **0.4740** | FAINT, DRAPE, SHUTTER, VAGUE                                      | INCORRECT (Max overlap: 2/4 with FUZZY, AS A MEMORY) | [Pred Type: SYNONYM_OR_NEAR (45.8%, no-rel 32.0%)]
   - Group 20: **0.4474** | BRIGHTNESS, BLIND, DIM, REMOTE                                    | INCORRECT (Max overlap: 2/4 with FUZZY, AS A MEMORY)

---

## Puzzle 70 (ID: 495)
**Words on Board:** CREDIT, BUST, FLOP, CHANCE, TIME, TURN, KINDLE, PRIME, PLASTIC, RIVER, RAINFOREST, CHARGE, DUD, CARD, MISS, SHOT

### Ground Truth Categories:
* **Level 0 (CLUNKER) [Type: SYNONYM_OR_NEAR]:** BUST, DUD, FLOP, MISS
* **Level 1 (OPPORTUNITY) [Type: SYNONYM_OR_NEAR]:** CHANCE, SHOT, TIME, TURN
* **Level 2 (NON-CASH WAY TO PAY) [Type: SYNONYM_OR_NEAR]:** CARD, CHARGE, CREDIT, PLASTIC
* **Level 3 (AMAZON ___) [Type: FILL_IN_THE_BLANK]:** KINDLE, PRIME, RAINFOREST, RIVER

### Top Candidate Partitions:
1. **Partition Score: 0.4676**
   - Group 1: **0.5293** | BUST, FLOP, DUD, MISS                                             | CORRECT GROUP (CLUNKER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 19.5%)]
   - Group 2: **0.4837** | CHANCE, KINDLE, RIVER, RAINFOREST                                 | INCORRECT (Max overlap: 3/4 with AMAZON ___)
   - Group 3: **0.4712** | TURN, PRIME, CHARGE, SHOT                                         | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
   - Group 4: **0.4469** | CREDIT, TIME, PLASTIC, CARD                                       | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY)
2. **Partition Score: 0.4664**
   - Group 1: **0.5293** | BUST, FLOP, DUD, MISS                                             | CORRECT GROUP (CLUNKER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 19.5%)]
   - Group 2: **0.4837** | CHANCE, KINDLE, RIVER, RAINFOREST                                 | INCORRECT (Max overlap: 3/4 with AMAZON ___)
   - Group 3: **0.4612** | CREDIT, PLASTIC, CARD, SHOT                                       | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 26.1%)]
   - Group 4: **0.4482** | TIME, TURN, PRIME, CHARGE                                         | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
3. **Partition Score: 0.4664**
   - Group 1: **0.5293** | BUST, FLOP, DUD, MISS                                             | CORRECT GROUP (CLUNKER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 19.5%)]
   - Group 2: **0.4792** | CREDIT, PRIME, CHARGE, CARD                                       | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY)
   - Group 3: **0.4678** | CHANCE, TIME, TURN, SHOT                                          | CORRECT GROUP (OPPORTUNITY, Level 1)
   - Group 4: **0.4473** | KINDLE, PLASTIC, RIVER, RAINFOREST                                | INCORRECT (Max overlap: 3/4 with AMAZON ___)
4. **Partition Score: 0.4641**
   - Group 1: **0.5471** | BUST, FLOP, DUD, SHOT                                             | INCORRECT (Max overlap: 3/4 with CLUNKER) | [Pred Type: SYNONYM_OR_NEAR (66.0%, no-rel 24.5%)]
   - Group 2: **0.4837** | CHANCE, KINDLE, RIVER, RAINFOREST                                 | INCORRECT (Max overlap: 3/4 with AMAZON ___)
   - Group 3: **0.4482** | TIME, TURN, PRIME, CHARGE                                         | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
   - Group 4: **0.4446** | CREDIT, PLASTIC, CARD, MISS                                       | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY)
5. **Partition Score: 0.4634**
   - Group 1: **0.5293** | BUST, FLOP, DUD, MISS                                             | CORRECT GROUP (CLUNKER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 19.5%)]
   - Group 2: **0.5057** | CREDIT, CHANCE, PLASTIC, CARD                                     | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY)
   - Group 3: **0.4979** | TIME, PRIME, CHARGE, SHOT                                         | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
   - Group 4: **0.4210** | TURN, KINDLE, RIVER, RAINFOREST                                   | INCORRECT (Max overlap: 3/4 with AMAZON ___)

### Top Candidate Groups:
   - Group 1: **0.5293** | BUST, FLOP, DUD, MISS                                             | CORRECT GROUP (CLUNKER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 19.5%)]
   - Group 2: **0.4837** | CHANCE, KINDLE, RIVER, RAINFOREST                                 | INCORRECT (Max overlap: 3/4 with AMAZON ___)
   - Group 3: **0.4712** | TURN, PRIME, CHARGE, SHOT                                         | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
   - Group 4: **0.4469** | CREDIT, TIME, PLASTIC, CARD                                       | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY)
   - Group 5: **0.4612** | CREDIT, PLASTIC, CARD, SHOT                                       | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 26.1%)]
   - Group 6: **0.4482** | TIME, TURN, PRIME, CHARGE                                         | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
   - Group 7: **0.4792** | CREDIT, PRIME, CHARGE, CARD                                       | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY)
   - Group 8: **0.4678** | CHANCE, TIME, TURN, SHOT                                          | CORRECT GROUP (OPPORTUNITY, Level 1)
   - Group 9: **0.4473** | KINDLE, PLASTIC, RIVER, RAINFOREST                                | INCORRECT (Max overlap: 3/4 with AMAZON ___)
   - Group 10: **0.5471** | BUST, FLOP, DUD, SHOT                                             | INCORRECT (Max overlap: 3/4 with CLUNKER) | [Pred Type: SYNONYM_OR_NEAR (66.0%, no-rel 24.5%)]
   - Group 11: **0.4446** | CREDIT, PLASTIC, CARD, MISS                                       | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY)
   - Group 12: **0.5057** | CREDIT, CHANCE, PLASTIC, CARD                                     | INCORRECT (Max overlap: 3/4 with NON-CASH WAY TO PAY)
   - Group 13: **0.4979** | TIME, PRIME, CHARGE, SHOT                                         | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
   - Group 14: **0.4210** | TURN, KINDLE, RIVER, RAINFOREST                                   | INCORRECT (Max overlap: 3/4 with AMAZON ___)
   - Group 15: **0.5999** | CREDIT, PLASTIC, CHARGE, CARD                                     | CORRECT GROUP (NON-CASH WAY TO PAY, Level 2)
   - Group 16: **0.4292** | CHANCE, TIME, PRIME, SHOT                                         | INCORRECT (Max overlap: 3/4 with OPPORTUNITY)
   - Group 17: **0.5226** | TURN, CHARGE, MISS, SHOT                                          | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
   - Group 18: **0.4482** | BUST, FLOP, PRIME, DUD                                            | INCORRECT (Max overlap: 3/4 with CLUNKER) | [Pred Type: SYNONYM_OR_NEAR (68.4%, no-rel 21.6%)]
   - Group 19: **0.4635** | BUST, FLOP, TURN, DUD                                             | INCORRECT (Max overlap: 3/4 with CLUNKER) | [Pred Type: SYNONYM_OR_NEAR (68.6%, no-rel 20.8%)]
   - Group 20: **0.4714** | CREDIT, CHANCE, CARD, SHOT                                        | INCORRECT (Max overlap: 2/4 with NON-CASH WAY TO PAY)

---

## Puzzle 71 (ID: 269)
**Words on Board:** TORCH, COMPLAINT, TARMAC, GUMSHOE, TURNCOAT, LAWSUIT, BEANBAG, RING, CLAIM, TERMINAL, ACTION, CLUB, FOXGLOVE, WINDSOCK, HANGAR, RUNWAY

### Ground Truth Categories:
* **Level 0 (PARTS OF AN AIRPORT) [Type: SEMANTIC_SET]:** HANGAR, RUNWAY, TARMAC, TERMINAL
* **Level 1 (LEGAL TERMS) [Type: SEMANTIC_SET]:** ACTION, CLAIM, COMPLAINT, LAWSUIT
* **Level 2 (THINGS A JUGGLER JUGGLES) [Type: SEMANTIC_SET]:** BEANBAG, CLUB, RING, TORCH
* **Level 3 (WORDS ENDING IN CLOTHING) [Type: WORD_FORM]:** FOXGLOVE, GUMSHOE, TURNCOAT, WINDSOCK

### Top Candidate Partitions:
1. **Partition Score: 0.5454**
   - Group 1: **0.7109** | COMPLAINT, LAWSUIT, CLAIM, ACTION                                 | CORRECT GROUP (LEGAL TERMS, Level 1)
   - Group 2: **0.6766** | GUMSHOE, TURNCOAT, FOXGLOVE, WINDSOCK                             | CORRECT GROUP (WORDS ENDING IN CLOTHING, Level 3)
   - Group 3: **0.5521** | TORCH, BEANBAG, TERMINAL, HANGAR                                  | INCORRECT (Max overlap: 2/4 with THINGS A JUGGLER JUGGLES)
   - Group 4: **0.4585** | TARMAC, RING, CLUB, RUNWAY                                        | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
2. **Partition Score: 0.5446**
   - Group 1: **0.7109** | COMPLAINT, LAWSUIT, CLAIM, ACTION                                 | CORRECT GROUP (LEGAL TERMS, Level 1)
   - Group 2: **0.6588** | TORCH, GUMSHOE, FOXGLOVE, WINDSOCK                                | INCORRECT (Max overlap: 3/4 with WORDS ENDING IN CLOTHING)
   - Group 3: **0.5660** | TURNCOAT, BEANBAG, TERMINAL, HANGAR                               | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 4: **0.4585** | TARMAC, RING, CLUB, RUNWAY                                        | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
3. **Partition Score: 0.5445**
   - Group 1: **0.7109** | COMPLAINT, LAWSUIT, CLAIM, ACTION                                 | CORRECT GROUP (LEGAL TERMS, Level 1)
   - Group 2: **0.6845** | TORCH, GUMSHOE, TURNCOAT, FOXGLOVE                                | INCORRECT (Max overlap: 3/4 with WORDS ENDING IN CLOTHING)
   - Group 3: **0.5394** | BEANBAG, TERMINAL, WINDSOCK, HANGAR                               | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 4: **0.4585** | TARMAC, RING, CLUB, RUNWAY                                        | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
4. **Partition Score: 0.5428**
   - Group 1: **0.7109** | COMPLAINT, LAWSUIT, CLAIM, ACTION                                 | CORRECT GROUP (LEGAL TERMS, Level 1)
   - Group 2: **0.6594** | TORCH, TURNCOAT, FOXGLOVE, WINDSOCK                               | INCORRECT (Max overlap: 3/4 with WORDS ENDING IN CLOTHING)
   - Group 3: **0.5556** | GUMSHOE, BEANBAG, TERMINAL, HANGAR                                | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 4: **0.4585** | TARMAC, RING, CLUB, RUNWAY                                        | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
5. **Partition Score: 0.5424**
   - Group 1: **0.7109** | COMPLAINT, LAWSUIT, CLAIM, ACTION                                 | CORRECT GROUP (LEGAL TERMS, Level 1)
   - Group 2: **0.6384** | TURNCOAT, BEANBAG, WINDSOCK, HANGAR                               | INCORRECT (Max overlap: 2/4 with WORDS ENDING IN CLOTHING)
   - Group 3: **0.5743** | TORCH, GUMSHOE, TERMINAL, FOXGLOVE                                | INCORRECT (Max overlap: 2/4 with WORDS ENDING IN CLOTHING)
   - Group 4: **0.4585** | TARMAC, RING, CLUB, RUNWAY                                        | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)

### Top Candidate Groups:
   - Group 1: **0.7109** | COMPLAINT, LAWSUIT, CLAIM, ACTION                                 | CORRECT GROUP (LEGAL TERMS, Level 1)
   - Group 2: **0.6766** | GUMSHOE, TURNCOAT, FOXGLOVE, WINDSOCK                             | CORRECT GROUP (WORDS ENDING IN CLOTHING, Level 3)
   - Group 3: **0.5521** | TORCH, BEANBAG, TERMINAL, HANGAR                                  | INCORRECT (Max overlap: 2/4 with THINGS A JUGGLER JUGGLES)
   - Group 4: **0.4585** | TARMAC, RING, CLUB, RUNWAY                                        | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 5: **0.6588** | TORCH, GUMSHOE, FOXGLOVE, WINDSOCK                                | INCORRECT (Max overlap: 3/4 with WORDS ENDING IN CLOTHING)
   - Group 6: **0.5660** | TURNCOAT, BEANBAG, TERMINAL, HANGAR                               | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 7: **0.6845** | TORCH, GUMSHOE, TURNCOAT, FOXGLOVE                                | INCORRECT (Max overlap: 3/4 with WORDS ENDING IN CLOTHING)
   - Group 8: **0.5394** | BEANBAG, TERMINAL, WINDSOCK, HANGAR                               | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 9: **0.6594** | TORCH, TURNCOAT, FOXGLOVE, WINDSOCK                               | INCORRECT (Max overlap: 3/4 with WORDS ENDING IN CLOTHING)
   - Group 10: **0.5556** | GUMSHOE, BEANBAG, TERMINAL, HANGAR                                | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 11: **0.6384** | TURNCOAT, BEANBAG, WINDSOCK, HANGAR                               | INCORRECT (Max overlap: 2/4 with WORDS ENDING IN CLOTHING)
   - Group 12: **0.5743** | TORCH, GUMSHOE, TERMINAL, FOXGLOVE                                | INCORRECT (Max overlap: 2/4 with WORDS ENDING IN CLOTHING)
   - Group 13: **0.6557** | TORCH, GUMSHOE, BEANBAG, WINDSOCK                                 | INCORRECT (Max overlap: 2/4 with THINGS A JUGGLER JUGGLES)
   - Group 14: **0.5557** | TURNCOAT, TERMINAL, FOXGLOVE, HANGAR                              | INCORRECT (Max overlap: 2/4 with WORDS ENDING IN CLOTHING)
   - Group 15: **0.6678** | GUMSHOE, TURNCOAT, BEANBAG, WINDSOCK                              | INCORRECT (Max overlap: 3/4 with WORDS ENDING IN CLOTHING)
   - Group 16: **0.5365** | TORCH, TERMINAL, FOXGLOVE, HANGAR                                 | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 17: **0.6735** | TORCH, GUMSHOE, TURNCOAT, BEANBAG                                 | INCORRECT (Max overlap: 2/4 with THINGS A JUGGLER JUGGLES)
   - Group 18: **0.5301** | TERMINAL, FOXGLOVE, WINDSOCK, HANGAR                              | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)
   - Group 19: **0.6390** | GUMSHOE, BEANBAG, FOXGLOVE, WINDSOCK                              | INCORRECT (Max overlap: 3/4 with WORDS ENDING IN CLOTHING)
   - Group 20: **0.5645** | TORCH, TURNCOAT, TERMINAL, HANGAR                                 | INCORRECT (Max overlap: 2/4 with PARTS OF AN AIRPORT)

---

## Puzzle 72 (ID: 599)
**Words on Board:** VIBE, WINGS, DWELL, RIGATONI, PARISH, LINGER, INSIST, BERNIE, HALO, BEER, AIR, PIZZA, HARP, ROMEO, DIP, AURA

### Ground Truth Categories:
* **Level 0 (INTANGIBLE QUALITY) [Type: SYNONYM_OR_NEAR]:** AIR, AURA, HALO, VIBE
* **Level 1 (GAME DAY FARE) [Type: SEMANTIC_SET]:** BEER, DIP, PIZZA, WINGS
* **Level 2 (KEEP GOING ON ABOUT, WITH “ON”) [Type: FILL_IN_THE_BLANK]:** DWELL, HARP, INSIST, LINGER
* **Level 3 (STARTING WITH EUROPEAN CAPITALS) [Type: WORD_FORM]:** BERNIE, PARISH, RIGATONI, ROMEO

### Top Candidate Partitions:
1. **Partition Score: 0.5977**
   - Group 1: **0.6529** | DWELL, LINGER, INSIST, HARP                                       | CORRECT GROUP (KEEP GOING ON ABOUT, WITH “ON”, Level 2) | [Pred Type: SYNONYM_OR_NEAR (59.3%, no-rel 34.2%)]
   - Group 2: **0.6509** | RIGATONI, PARISH, BERNIE, ROMEO                                   | CORRECT GROUP (STARTING WITH EUROPEAN CAPITALS, Level 3)
   - Group 3: **0.6077** | WINGS, BEER, PIZZA, DIP                                           | CORRECT GROUP (GAME DAY FARE, Level 1)
   - Group 4: **0.5624** | VIBE, HALO, AIR, AURA                                             | CORRECT GROUP (INTANGIBLE QUALITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.4%, no-rel 21.8%)]
2. **Partition Score: 0.5769**
   - Group 1: **0.6529** | DWELL, LINGER, INSIST, HARP                                       | CORRECT GROUP (KEEP GOING ON ABOUT, WITH “ON”, Level 2) | [Pred Type: SYNONYM_OR_NEAR (59.3%, no-rel 34.2%)]
   - Group 2: **0.6082** | RIGATONI, PARISH, BERNIE, BEER                                    | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 3: **0.5624** | VIBE, HALO, AIR, AURA                                             | CORRECT GROUP (INTANGIBLE QUALITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.4%, no-rel 21.8%)]
   - Group 4: **0.5540** | WINGS, PIZZA, ROMEO, DIP                                          | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)
3. **Partition Score: 0.5734**
   - Group 1: **0.6529** | DWELL, LINGER, INSIST, HARP                                       | CORRECT GROUP (KEEP GOING ON ABOUT, WITH “ON”, Level 2) | [Pred Type: SYNONYM_OR_NEAR (59.3%, no-rel 34.2%)]
   - Group 2: **0.5712** | WINGS, RIGATONI, PARISH, BERNIE                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 3: **0.5624** | VIBE, HALO, AIR, AURA                                             | CORRECT GROUP (INTANGIBLE QUALITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.4%, no-rel 21.8%)]
   - Group 4: **0.5608** | BEER, PIZZA, ROMEO, DIP                                           | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)
4. **Partition Score: 0.5684**
   - Group 1: **0.6529** | DWELL, LINGER, INSIST, HARP                                       | CORRECT GROUP (KEEP GOING ON ABOUT, WITH “ON”, Level 2) | [Pred Type: SYNONYM_OR_NEAR (59.3%, no-rel 34.2%)]
   - Group 2: **0.6060** | RIGATONI, PARISH, BERNIE, PIZZA                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 3: **0.5624** | VIBE, HALO, AIR, AURA                                             | CORRECT GROUP (INTANGIBLE QUALITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.4%, no-rel 21.8%)]
   - Group 4: **0.5382** | WINGS, BEER, ROMEO, DIP                                           | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)
5. **Partition Score: 0.5584**
   - Group 1: **0.6529** | DWELL, LINGER, INSIST, HARP                                       | CORRECT GROUP (KEEP GOING ON ABOUT, WITH “ON”, Level 2) | [Pred Type: SYNONYM_OR_NEAR (59.3%, no-rel 34.2%)]
   - Group 2: **0.5700** | WINGS, PARISH, BERNIE, BEER                                       | INCORRECT (Max overlap: 2/4 with GAME DAY FARE)
   - Group 3: **0.5624** | VIBE, HALO, AIR, AURA                                             | CORRECT GROUP (INTANGIBLE QUALITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.4%, no-rel 21.8%)]
   - Group 4: **0.5320** | RIGATONI, PIZZA, ROMEO, DIP                                       | INCORRECT (Max overlap: 2/4 with STARTING WITH EUROPEAN CAPITALS)

### Top Candidate Groups:
   - Group 1: **0.6529** | DWELL, LINGER, INSIST, HARP                                       | CORRECT GROUP (KEEP GOING ON ABOUT, WITH “ON”, Level 2) | [Pred Type: SYNONYM_OR_NEAR (59.3%, no-rel 34.2%)]
   - Group 2: **0.6509** | RIGATONI, PARISH, BERNIE, ROMEO                                   | CORRECT GROUP (STARTING WITH EUROPEAN CAPITALS, Level 3)
   - Group 3: **0.6077** | WINGS, BEER, PIZZA, DIP                                           | CORRECT GROUP (GAME DAY FARE, Level 1)
   - Group 4: **0.5624** | VIBE, HALO, AIR, AURA                                             | CORRECT GROUP (INTANGIBLE QUALITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (71.4%, no-rel 21.8%)]
   - Group 5: **0.6082** | RIGATONI, PARISH, BERNIE, BEER                                    | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 6: **0.5540** | WINGS, PIZZA, ROMEO, DIP                                          | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)
   - Group 7: **0.5712** | WINGS, RIGATONI, PARISH, BERNIE                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 8: **0.5608** | BEER, PIZZA, ROMEO, DIP                                           | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)
   - Group 9: **0.6060** | RIGATONI, PARISH, BERNIE, PIZZA                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 10: **0.5382** | WINGS, BEER, ROMEO, DIP                                           | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)
   - Group 11: **0.5700** | WINGS, PARISH, BERNIE, BEER                                       | INCORRECT (Max overlap: 2/4 with GAME DAY FARE)
   - Group 12: **0.5320** | RIGATONI, PIZZA, ROMEO, DIP                                       | INCORRECT (Max overlap: 2/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 13: **0.5796** | DWELL, LINGER, INSIST, AIR                                        | INCORRECT (Max overlap: 3/4 with KEEP GOING ON ABOUT, WITH “ON”)
   - Group 14: **0.5101** | VIBE, HALO, HARP, AURA                                            | INCORRECT (Max overlap: 3/4 with INTANGIBLE QUALITY) | [Pred Type: SYNONYM_OR_NEAR (68.9%, no-rel 23.0%)]
   - Group 15: **0.6104** | PARISH, BERNIE, BEER, ROMEO                                       | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 16: **0.5149** | WINGS, RIGATONI, PIZZA, DIP                                       | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)
   - Group 17: **0.5781** | WINGS, PARISH, BERNIE, ROMEO                                      | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 18: **0.5264** | RIGATONI, BEER, PIZZA, DIP                                        | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)
   - Group 19: **0.6304** | RIGATONI, BERNIE, BEER, ROMEO                                     | INCORRECT (Max overlap: 3/4 with STARTING WITH EUROPEAN CAPITALS)
   - Group 20: **0.5050** | WINGS, PARISH, PIZZA, DIP                                         | INCORRECT (Max overlap: 3/4 with GAME DAY FARE)

---

## Puzzle 73 (ID: 710)
**Words on Board:** BLOCK, PATCH, MUSIC, COMPACT, LAPTOP, PICTURES, DENY, BAR, DESKTOP, WAFFLE IRON, REFUSE, TABLET, TRASH, CREAM, SPRAY, CLAM

### Ground Truth Categories:
* **Level 0 (PROHIBIT, AS ENTRY) [Type: SYNONYM_OR_NEAR]:** BAR, BLOCK, DENY, REFUSE
* **Level 1 (FOLDERS ON A MAC) [Type: NAMED_ENTITY_SET]:** DESKTOP, MUSIC, PICTURES, TRASH
* **Level 2 (MEDICINE FORMATS) [Type: SEMANTIC_SET]:** CREAM, PATCH, SPRAY, TABLET
* **Level 3 (THINGS THAT OPEN LIKE A CLAM) [Type: SEMANTIC_SET]:** CLAM, COMPACT, LAPTOP, WAFFLE IRON

### Top Candidate Partitions:
1. **Partition Score: 0.5073**
   - Group 1: **0.5506** | BLOCK, DENY, REFUSE, TRASH                                        | INCORRECT (Max overlap: 3/4 with PROHIBIT, AS ENTRY) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 29.4%)]
   - Group 2: **0.5166** | LAPTOP, DESKTOP, WAFFLE IRON, TABLET                              | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 3: **0.5021** | PATCH, BAR, CREAM, SPRAY                                          | INCORRECT (Max overlap: 3/4 with MEDICINE FORMATS)
   - Group 4: **0.4963** | MUSIC, COMPACT, PICTURES, CLAM                                    | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC)
2. **Partition Score: 0.5036**
   - Group 1: **0.5442** | BLOCK, PATCH, BAR, SPRAY                                          | INCORRECT (Max overlap: 2/4 with PROHIBIT, AS ENTRY)
   - Group 2: **0.5292** | MUSIC, PICTURES, CREAM, CLAM                                      | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC)
   - Group 3: **0.5166** | LAPTOP, DESKTOP, WAFFLE IRON, TABLET                              | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 4: **0.4806** | COMPACT, DENY, REFUSE, TRASH                                      | INCORRECT (Max overlap: 2/4 with PROHIBIT, AS ENTRY) | [Pred Type: SYNONYM_OR_NEAR (70.5%, no-rel 18.6%)]
3. **Partition Score: 0.4991**
   - Group 1: **0.5506** | BLOCK, DENY, REFUSE, TRASH                                        | INCORRECT (Max overlap: 3/4 with PROHIBIT, AS ENTRY) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 29.4%)]
   - Group 2: **0.5399** | PATCH, COMPACT, CREAM, SPRAY                                      | INCORRECT (Max overlap: 3/4 with MEDICINE FORMATS)
   - Group 3: **0.5166** | LAPTOP, DESKTOP, WAFFLE IRON, TABLET                              | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 4: **0.4665** | MUSIC, PICTURES, BAR, CLAM                                        | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC) | [Pred Type: FILL_IN_THE_BLANK (62.0%, no-rel 14.9%)]
4. **Partition Score: 0.4970**
   - Group 1: **0.5506** | BLOCK, DENY, REFUSE, TRASH                                        | INCORRECT (Max overlap: 3/4 with PROHIBIT, AS ENTRY) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 29.4%)]
   - Group 2: **0.5166** | LAPTOP, DESKTOP, WAFFLE IRON, TABLET                              | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 3: **0.4856** | PATCH, BAR, CREAM, CLAM                                           | INCORRECT (Max overlap: 2/4 with MEDICINE FORMATS)
   - Group 4: **0.4823** | MUSIC, COMPACT, PICTURES, SPRAY                                   | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC)
5. **Partition Score: 0.4961**
   - Group 1: **0.5506** | BLOCK, DENY, REFUSE, TRASH                                        | INCORRECT (Max overlap: 3/4 with PROHIBIT, AS ENTRY) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 29.4%)]
   - Group 2: **0.5166** | LAPTOP, DESKTOP, WAFFLE IRON, TABLET                              | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 3: **0.4918** | MUSIC, BAR, CREAM, CLAM                                           | INCORRECT (Max overlap: 1/4 with FOLDERS ON A MAC) | [Pred Type: FILL_IN_THE_BLANK (55.7%, no-rel 17.3%)]
   - Group 4: **0.4782** | PATCH, COMPACT, PICTURES, SPRAY                                   | INCORRECT (Max overlap: 2/4 with MEDICINE FORMATS)

### Top Candidate Groups:
   - Group 1: **0.5506** | BLOCK, DENY, REFUSE, TRASH                                        | INCORRECT (Max overlap: 3/4 with PROHIBIT, AS ENTRY) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 29.4%)]
   - Group 2: **0.5166** | LAPTOP, DESKTOP, WAFFLE IRON, TABLET                              | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 3: **0.5021** | PATCH, BAR, CREAM, SPRAY                                          | INCORRECT (Max overlap: 3/4 with MEDICINE FORMATS)
   - Group 4: **0.4963** | MUSIC, COMPACT, PICTURES, CLAM                                    | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC)
   - Group 5: **0.5442** | BLOCK, PATCH, BAR, SPRAY                                          | INCORRECT (Max overlap: 2/4 with PROHIBIT, AS ENTRY)
   - Group 6: **0.5292** | MUSIC, PICTURES, CREAM, CLAM                                      | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC)
   - Group 7: **0.4806** | COMPACT, DENY, REFUSE, TRASH                                      | INCORRECT (Max overlap: 2/4 with PROHIBIT, AS ENTRY) | [Pred Type: SYNONYM_OR_NEAR (70.5%, no-rel 18.6%)]
   - Group 8: **0.5399** | PATCH, COMPACT, CREAM, SPRAY                                      | INCORRECT (Max overlap: 3/4 with MEDICINE FORMATS)
   - Group 9: **0.4665** | MUSIC, PICTURES, BAR, CLAM                                        | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC) | [Pred Type: FILL_IN_THE_BLANK (62.0%, no-rel 14.9%)]
   - Group 10: **0.4856** | PATCH, BAR, CREAM, CLAM                                           | INCORRECT (Max overlap: 2/4 with MEDICINE FORMATS)
   - Group 11: **0.4823** | MUSIC, COMPACT, PICTURES, SPRAY                                   | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC)
   - Group 12: **0.4918** | MUSIC, BAR, CREAM, CLAM                                           | INCORRECT (Max overlap: 1/4 with FOLDERS ON A MAC) | [Pred Type: FILL_IN_THE_BLANK (55.7%, no-rel 17.3%)]
   - Group 13: **0.4782** | PATCH, COMPACT, PICTURES, SPRAY                                   | INCORRECT (Max overlap: 2/4 with MEDICINE FORMATS)
   - Group 14: **0.5398** | MUSIC, COMPACT, CREAM, CLAM                                       | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 15: **0.4597** | PATCH, PICTURES, BAR, SPRAY                                       | INCORRECT (Max overlap: 2/4 with MEDICINE FORMATS)
   - Group 16: **0.5037** | LAPTOP, PICTURES, DESKTOP, TABLET                                 | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC)
   - Group 17: **0.4887** | MUSIC, WAFFLE IRON, CREAM, CLAM                                   | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 18: **0.5274** | MUSIC, LAPTOP, DESKTOP, TABLET                                    | INCORRECT (Max overlap: 2/4 with FOLDERS ON A MAC)
   - Group 19: **0.4748** | PICTURES, WAFFLE IRON, CREAM, CLAM                                | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)
   - Group 20: **0.5199** | COMPACT, PICTURES, CREAM, CLAM                                    | INCORRECT (Max overlap: 2/4 with THINGS THAT OPEN LIKE A CLAM)

---

## Puzzle 74 (ID: 800)
**Words on Board:** FLYWHEEL, WINDBAG, PRATTLER, PLYMOUTH, SHERRY, MARSALA, CHATTERBOX, THE, DASHBOARD, PORT, CLASSIC, DARTMOUTH, VERMOUTH, BLABBERMOUTH, LITTLE, RUSHMORE

### Ground Truth Categories:
* **Level 0 (QUITE THE TALKER) [Type: SYNONYM_OR_NEAR]:** BLABBERMOUTH, CHATTERBOX, PRATTLER, WINDBAG
* **Level 1 (FORTIFIED WINES) [Type: SEMANTIC_SET]:** MARSALA, PORT, SHERRY, VERMOUTH
* **Level 2 (___ ROCK) [Type: FILL_IN_THE_BLANK]:** CLASSIC, LITTLE, PLYMOUTH, THE
* **Level 3 (STARTING WITH WAYS TO MOVE QUICKLY) [Type: WORDPLAY_TRANSFORM]:** DARTMOUTH, DASHBOARD, FLYWHEEL, RUSHMORE

### Top Candidate Partitions:
1. **Partition Score: 0.4851**
   - Group 1: **0.6399** | WINDBAG, PRATTLER, CHATTERBOX, BLABBERMOUTH                       | CORRECT GROUP (QUITE THE TALKER, Level 0)
   - Group 2: **0.5710** | SHERRY, MARSALA, PORT, VERMOUTH                                   | CORRECT GROUP (FORTIFIED WINES, Level 1)
   - Group 3: **0.4482** | FLYWHEEL, DASHBOARD, DARTMOUTH, RUSHMORE                          | CORRECT GROUP (STARTING WITH WAYS TO MOVE QUICKLY, Level 3)
   - Group 4: **0.4332** | PLYMOUTH, THE, CLASSIC, LITTLE                                    | CORRECT GROUP (___ ROCK, Level 2) | [Pred Type: FILL_IN_THE_BLANK (48.4%, no-rel 14.5%)]
2. **Partition Score: 0.4670**
   - Group 1: **0.5710** | SHERRY, MARSALA, PORT, VERMOUTH                                   | CORRECT GROUP (FORTIFIED WINES, Level 1)
   - Group 2: **0.5297** | PRATTLER, CHATTERBOX, DASHBOARD, BLABBERMOUTH                     | INCORRECT (Max overlap: 3/4 with QUITE THE TALKER)
   - Group 3: **0.4343** | FLYWHEEL, WINDBAG, DARTMOUTH, RUSHMORE                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 4: **0.4332** | PLYMOUTH, THE, CLASSIC, LITTLE                                    | CORRECT GROUP (___ ROCK, Level 2) | [Pred Type: FILL_IN_THE_BLANK (48.4%, no-rel 14.5%)]
3. **Partition Score: 0.4647**
   - Group 1: **0.5710** | SHERRY, MARSALA, PORT, VERMOUTH                                   | CORRECT GROUP (FORTIFIED WINES, Level 1)
   - Group 2: **0.4727** | PRATTLER, CHATTERBOX, CLASSIC, BLABBERMOUTH                       | INCORRECT (Max overlap: 3/4 with QUITE THE TALKER)
   - Group 3: **0.4481** | FLYWHEEL, WINDBAG, DASHBOARD, RUSHMORE                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 4: **0.4445** | PLYMOUTH, THE, DARTMOUTH, LITTLE                                  | INCORRECT (Max overlap: 3/4 with ___ ROCK)
4. **Partition Score: 0.4600**
   - Group 1: **0.5710** | SHERRY, MARSALA, PORT, VERMOUTH                                   | CORRECT GROUP (FORTIFIED WINES, Level 1)
   - Group 2: **0.4827** | FLYWHEEL, PRATTLER, CHATTERBOX, BLABBERMOUTH                      | INCORRECT (Max overlap: 3/4 with QUITE THE TALKER)
   - Group 3: **0.4440** | WINDBAG, DASHBOARD, DARTMOUTH, RUSHMORE                           | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 4: **0.4332** | PLYMOUTH, THE, CLASSIC, LITTLE                                    | CORRECT GROUP (___ ROCK, Level 2) | [Pred Type: FILL_IN_THE_BLANK (48.4%, no-rel 14.5%)]
5. **Partition Score: 0.4577**
   - Group 1: **0.4865** | SHERRY, MARSALA, VERMOUTH, RUSHMORE                               | INCORRECT (Max overlap: 3/4 with FORTIFIED WINES)
   - Group 2: **0.4827** | FLYWHEEL, PRATTLER, CHATTERBOX, BLABBERMOUTH                      | INCORRECT (Max overlap: 3/4 with QUITE THE TALKER)
   - Group 3: **0.4515** | WINDBAG, DASHBOARD, PORT, CLASSIC                                 | INCORRECT (Max overlap: 1/4 with QUITE THE TALKER)
   - Group 4: **0.4445** | PLYMOUTH, THE, DARTMOUTH, LITTLE                                  | INCORRECT (Max overlap: 3/4 with ___ ROCK)

### Top Candidate Groups:
   - Group 1: **0.6399** | WINDBAG, PRATTLER, CHATTERBOX, BLABBERMOUTH                       | CORRECT GROUP (QUITE THE TALKER, Level 0)
   - Group 2: **0.5710** | SHERRY, MARSALA, PORT, VERMOUTH                                   | CORRECT GROUP (FORTIFIED WINES, Level 1)
   - Group 3: **0.4482** | FLYWHEEL, DASHBOARD, DARTMOUTH, RUSHMORE                          | CORRECT GROUP (STARTING WITH WAYS TO MOVE QUICKLY, Level 3)
   - Group 4: **0.4332** | PLYMOUTH, THE, CLASSIC, LITTLE                                    | CORRECT GROUP (___ ROCK, Level 2) | [Pred Type: FILL_IN_THE_BLANK (48.4%, no-rel 14.5%)]
   - Group 5: **0.5297** | PRATTLER, CHATTERBOX, DASHBOARD, BLABBERMOUTH                     | INCORRECT (Max overlap: 3/4 with QUITE THE TALKER)
   - Group 6: **0.4343** | FLYWHEEL, WINDBAG, DARTMOUTH, RUSHMORE                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 7: **0.4727** | PRATTLER, CHATTERBOX, CLASSIC, BLABBERMOUTH                       | INCORRECT (Max overlap: 3/4 with QUITE THE TALKER)
   - Group 8: **0.4481** | FLYWHEEL, WINDBAG, DASHBOARD, RUSHMORE                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 9: **0.4445** | PLYMOUTH, THE, DARTMOUTH, LITTLE                                  | INCORRECT (Max overlap: 3/4 with ___ ROCK)
   - Group 10: **0.4827** | FLYWHEEL, PRATTLER, CHATTERBOX, BLABBERMOUTH                      | INCORRECT (Max overlap: 3/4 with QUITE THE TALKER)
   - Group 11: **0.4440** | WINDBAG, DASHBOARD, DARTMOUTH, RUSHMORE                           | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 12: **0.4865** | SHERRY, MARSALA, VERMOUTH, RUSHMORE                               | INCORRECT (Max overlap: 3/4 with FORTIFIED WINES)
   - Group 13: **0.4515** | WINDBAG, DASHBOARD, PORT, CLASSIC                                 | INCORRECT (Max overlap: 1/4 with QUITE THE TALKER)
   - Group 14: **0.5072** | SHERRY, MARSALA, DASHBOARD, PORT                                  | INCORRECT (Max overlap: 3/4 with FORTIFIED WINES)
   - Group 15: **0.4082** | FLYWHEEL, DARTMOUTH, VERMOUTH, RUSHMORE                           | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 16: **0.4524** | FLYWHEEL, SHERRY, MARSALA, PORT                                   | INCORRECT (Max overlap: 3/4 with FORTIFIED WINES)
   - Group 17: **0.4204** | DASHBOARD, DARTMOUTH, VERMOUTH, RUSHMORE                          | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 18: **0.4348** | WINDBAG, DARTMOUTH, VERMOUTH, RUSHMORE                            | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO MOVE QUICKLY)
   - Group 19: **0.4868** | WINDBAG, SHERRY, MARSALA, VERMOUTH                                | INCORRECT (Max overlap: 3/4 with FORTIFIED WINES)
   - Group 20: **0.4697** | PRATTLER, CHATTERBOX, PORT, BLABBERMOUTH                          | INCORRECT (Max overlap: 3/4 with QUITE THE TALKER)

---

## Puzzle 75 (ID: 133)
**Words on Board:** PICKLE, LOUNGE, TRIFLE, BANGER, SCONE, LOAF, GROOVE, HANG, CHILL, MASH, BIND, ROAST, SCRAPE, JAM, BOP, SPOT

### Ground Truth Categories:
* **Level 0 (RELAX) [Type: SYNONYM_OR_NEAR]:** CHILL, HANG, LOAF, LOUNGE
* **Level 1 (CATCHY SONG) [Type: SYNONYM_OR_NEAR]:** BANGER, BOP, GROOVE, JAM
* **Level 2 (BRITISH CUISINE) [Type: NAMED_ENTITY_SET]:** MASH, ROAST, SCONE, TRIFLE
* **Level 3 (STICKY SITUATION) [Type: SYNONYM_OR_NEAR]:** BIND, PICKLE, SCRAPE, SPOT

### Top Candidate Partitions:
1. **Partition Score: 0.5078**
   - Group 1: **0.6164** | HANG, CHILL, BIND, ROAST                                          | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 2: **0.5695** | PICKLE, BANGER, MASH, JAM                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 3: **0.4826** | LOUNGE, TRIFLE, SCONE, LOAF                                       | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 4: **0.4707** | GROOVE, SCRAPE, BOP, SPOT                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
2. **Partition Score: 0.5002**
   - Group 1: **0.6164** | HANG, CHILL, BIND, ROAST                                          | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 2: **0.5145** | BANGER, GROOVE, MASH, BOP                                         | INCORRECT (Max overlap: 3/4 with CATCHY SONG)
   - Group 3: **0.4826** | LOUNGE, TRIFLE, SCONE, LOAF                                       | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 4: **0.4758** | PICKLE, SCRAPE, JAM, SPOT                                         | INCORRECT (Max overlap: 3/4 with STICKY SITUATION)
3. **Partition Score: 0.4978**
   - Group 1: **0.6164** | HANG, CHILL, BIND, ROAST                                          | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 2: **0.5405** | PICKLE, BANGER, MASH, BOP                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 3: **0.4826** | LOUNGE, TRIFLE, SCONE, LOAF                                       | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 4: **0.4617** | GROOVE, SCRAPE, JAM, SPOT                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
4. **Partition Score: 0.4955**
   - Group 1: **0.6164** | HANG, CHILL, BIND, ROAST                                          | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 2: **0.5080** | PICKLE, TRIFLE, MASH, JAM                                         | INCORRECT (Max overlap: 2/4 with BRITISH CUISINE)
   - Group 3: **0.4784** | LOUNGE, BANGER, SCONE, LOAF                                       | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 4: **0.4707** | GROOVE, SCRAPE, BOP, SPOT                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
5. **Partition Score: 0.4955**
   - Group 1: **0.6164** | HANG, CHILL, BIND, ROAST                                          | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 2: **0.4998** | BANGER, GROOVE, SCRAPE, BOP                                       | INCORRECT (Max overlap: 3/4 with CATCHY SONG)
   - Group 3: **0.4826** | LOUNGE, TRIFLE, SCONE, LOAF                                       | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 4: **0.4721** | PICKLE, MASH, JAM, SPOT                                           | INCORRECT (Max overlap: 2/4 with STICKY SITUATION)

### Top Candidate Groups:
   - Group 1: **0.6164** | HANG, CHILL, BIND, ROAST                                          | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 2: **0.5695** | PICKLE, BANGER, MASH, JAM                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 3: **0.4826** | LOUNGE, TRIFLE, SCONE, LOAF                                       | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 4: **0.4707** | GROOVE, SCRAPE, BOP, SPOT                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 5: **0.5145** | BANGER, GROOVE, MASH, BOP                                         | INCORRECT (Max overlap: 3/4 with CATCHY SONG)
   - Group 6: **0.4758** | PICKLE, SCRAPE, JAM, SPOT                                         | INCORRECT (Max overlap: 3/4 with STICKY SITUATION)
   - Group 7: **0.5405** | PICKLE, BANGER, MASH, BOP                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 8: **0.4617** | GROOVE, SCRAPE, JAM, SPOT                                         | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 9: **0.5080** | PICKLE, TRIFLE, MASH, JAM                                         | INCORRECT (Max overlap: 2/4 with BRITISH CUISINE)
   - Group 10: **0.4784** | LOUNGE, BANGER, SCONE, LOAF                                       | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 11: **0.4998** | BANGER, GROOVE, SCRAPE, BOP                                       | INCORRECT (Max overlap: 3/4 with CATCHY SONG)
   - Group 12: **0.4721** | PICKLE, MASH, JAM, SPOT                                           | INCORRECT (Max overlap: 2/4 with STICKY SITUATION)
   - Group 13: **0.5384** | PICKLE, TRIFLE, BANGER, SCONE                                     | INCORRECT (Max overlap: 2/4 with BRITISH CUISINE)
   - Group 14: **0.4691** | LOUNGE, LOAF, MASH, BOP                                           | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 15: **0.5648** | PICKLE, MASH, JAM, BOP                                            | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 16: **0.4454** | BANGER, GROOVE, SCRAPE, SPOT                                      | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 17: **0.4961** | TRIFLE, BANGER, GROOVE, BOP                                       | INCORRECT (Max overlap: 3/4 with CATCHY SONG)
   - Group 18: **0.4726** | LOUNGE, SCONE, LOAF, MASH                                         | INCORRECT (Max overlap: 2/4 with RELAX)
   - Group 19: **0.5032** | PICKLE, TRIFLE, BANGER, JAM                                       | INCORRECT (Max overlap: 2/4 with CATCHY SONG)
   - Group 20: **0.4819** | TRIFLE, GROOVE, MASH, BOP                                         | INCORRECT (Max overlap: 2/4 with BRITISH CUISINE)

---

## Puzzle 76 (ID: 216)
**Words on Board:** DIRECT, STALL, TICKET, CENTER, PUNT, END, CHAIR, INVITE, TABLE, BADGE, HOLD, RUN, TACKLE, PASS, SAFETY, LEAD

### Ground Truth Categories:
* **Level 0 (CREDENTIALS FOR ENTRY) [Type: SEMANTIC_SET]:** BADGE, INVITE, PASS, TICKET
* **Level 1 (PRESIDE OVER) [Type: SYNONYM_OR_NEAR]:** CHAIR, DIRECT, LEAD, RUN
* **Level 2 (AMERICAN FOOTBALL POSITIONS) [Type: NAMED_ENTITY_SET]:** CENTER, END, SAFETY, TACKLE
* **Level 3 (POSTPONE) [Type: SYNONYM_OR_NEAR]:** HOLD, PUNT, STALL, TABLE

### Top Candidate Partitions:
1. **Partition Score: 0.4672**
   - Group 1: **0.5044** | CENTER, PUNT, TACKLE, SAFETY                                      | INCORRECT (Max overlap: 3/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 2: **0.4991** | TICKET, END, RUN, PASS                                            | INCORRECT (Max overlap: 2/4 with CREDENTIALS FOR ENTRY) | [Pred Type: SYNONYM_OR_NEAR (52.5%, no-rel 37.0%)]
   - Group 3: **0.4697** | DIRECT, INVITE, HOLD, LEAD                                        | INCORRECT (Max overlap: 2/4 with PRESIDE OVER) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 32.1%)]
   - Group 4: **0.4464** | STALL, CHAIR, TABLE, BADGE                                        | INCORRECT (Max overlap: 2/4 with POSTPONE) | [Pred Type: SEMANTIC_SET (53.0%, no-rel 31.9%)]
2. **Partition Score: 0.4665**
   - Group 1: **0.4789** | TICKET, BADGE, TACKLE, PASS                                       | INCORRECT (Max overlap: 3/4 with CREDENTIALS FOR ENTRY)
   - Group 2: **0.4697** | DIRECT, INVITE, HOLD, LEAD                                        | INCORRECT (Max overlap: 2/4 with PRESIDE OVER) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 32.1%)]
   - Group 3: **0.4684** | STALL, END, CHAIR, TABLE                                          | INCORRECT (Max overlap: 2/4 with POSTPONE)
   - Group 4: **0.4618** | CENTER, PUNT, RUN, SAFETY                                         | INCORRECT (Max overlap: 2/4 with AMERICAN FOOTBALL POSITIONS)
3. **Partition Score: 0.4603**
   - Group 1: **0.5055** | TICKET, END, TACKLE, PASS                                         | INCORRECT (Max overlap: 2/4 with CREDENTIALS FOR ENTRY)
   - Group 2: **0.4697** | DIRECT, INVITE, HOLD, LEAD                                        | INCORRECT (Max overlap: 2/4 with PRESIDE OVER) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 32.1%)]
   - Group 3: **0.4618** | CENTER, PUNT, RUN, SAFETY                                         | INCORRECT (Max overlap: 2/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 4: **0.4464** | STALL, CHAIR, TABLE, BADGE                                        | INCORRECT (Max overlap: 2/4 with POSTPONE) | [Pred Type: SEMANTIC_SET (53.0%, no-rel 31.9%)]
4. **Partition Score: 0.4576**
   - Group 1: **0.5044** | CENTER, PUNT, TACKLE, SAFETY                                      | INCORRECT (Max overlap: 3/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 2: **0.4697** | DIRECT, INVITE, HOLD, LEAD                                        | INCORRECT (Max overlap: 2/4 with PRESIDE OVER) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 32.1%)]
   - Group 3: **0.4684** | STALL, END, CHAIR, TABLE                                          | INCORRECT (Max overlap: 2/4 with POSTPONE)
   - Group 4: **0.4389** | TICKET, BADGE, RUN, PASS                                          | INCORRECT (Max overlap: 3/4 with CREDENTIALS FOR ENTRY) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 25.5%)]
5. **Partition Score: 0.4564**
   - Group 1: **0.4697** | DIRECT, INVITE, HOLD, LEAD                                        | INCORRECT (Max overlap: 2/4 with PRESIDE OVER) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 32.1%)]
   - Group 2: **0.4684** | STALL, END, CHAIR, TABLE                                          | INCORRECT (Max overlap: 2/4 with POSTPONE)
   - Group 3: **0.4514** | PUNT, BADGE, TACKLE, SAFETY                                       | INCORRECT (Max overlap: 2/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 4: **0.4509** | TICKET, CENTER, RUN, PASS                                         | INCORRECT (Max overlap: 2/4 with CREDENTIALS FOR ENTRY) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 35.3%)]

### Top Candidate Groups:
   - Group 1: **0.5044** | CENTER, PUNT, TACKLE, SAFETY                                      | INCORRECT (Max overlap: 3/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 2: **0.4991** | TICKET, END, RUN, PASS                                            | INCORRECT (Max overlap: 2/4 with CREDENTIALS FOR ENTRY) | [Pred Type: SYNONYM_OR_NEAR (52.5%, no-rel 37.0%)]
   - Group 3: **0.4697** | DIRECT, INVITE, HOLD, LEAD                                        | INCORRECT (Max overlap: 2/4 with PRESIDE OVER) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 32.1%)]
   - Group 4: **0.4464** | STALL, CHAIR, TABLE, BADGE                                        | INCORRECT (Max overlap: 2/4 with POSTPONE) | [Pred Type: SEMANTIC_SET (53.0%, no-rel 31.9%)]
   - Group 5: **0.4789** | TICKET, BADGE, TACKLE, PASS                                       | INCORRECT (Max overlap: 3/4 with CREDENTIALS FOR ENTRY)
   - Group 6: **0.4684** | STALL, END, CHAIR, TABLE                                          | INCORRECT (Max overlap: 2/4 with POSTPONE)
   - Group 7: **0.4618** | CENTER, PUNT, RUN, SAFETY                                         | INCORRECT (Max overlap: 2/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 8: **0.5055** | TICKET, END, TACKLE, PASS                                         | INCORRECT (Max overlap: 2/4 with CREDENTIALS FOR ENTRY)
   - Group 9: **0.4389** | TICKET, BADGE, RUN, PASS                                          | INCORRECT (Max overlap: 3/4 with CREDENTIALS FOR ENTRY) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 25.5%)]
   - Group 10: **0.4514** | PUNT, BADGE, TACKLE, SAFETY                                       | INCORRECT (Max overlap: 2/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 11: **0.4509** | TICKET, CENTER, RUN, PASS                                         | INCORRECT (Max overlap: 2/4 with CREDENTIALS FOR ENTRY) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 35.3%)]
   - Group 12: **0.5080** | TICKET, RUN, TACKLE, PASS                                         | INCORRECT (Max overlap: 2/4 with CREDENTIALS FOR ENTRY) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 33.2%)]
   - Group 13: **0.4871** | PUNT, BADGE, SAFETY, LEAD                                         | INCORRECT (Max overlap: 1/4 with POSTPONE)
   - Group 14: **0.4265** | DIRECT, CENTER, INVITE, HOLD                                      | INCORRECT (Max overlap: 1/4 with PRESIDE OVER)
   - Group 15: **0.4682** | TICKET, CENTER, END, PASS                                         | INCORRECT (Max overlap: 2/4 with CREDENTIALS FOR ENTRY)
   - Group 16: **0.4552** | PUNT, RUN, TACKLE, SAFETY                                         | INCORRECT (Max overlap: 2/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 17: **0.4526** | CENTER, END, RUN, SAFETY                                          | INCORRECT (Max overlap: 3/4 with AMERICAN FOOTBALL POSITIONS)
   - Group 18: **0.4444** | STALL, PUNT, CHAIR, TABLE                                         | INCORRECT (Max overlap: 3/4 with POSTPONE)
   - Group 19: **0.4822** | PUNT, RUN, SAFETY, LEAD                                           | INCORRECT (Max overlap: 2/4 with PRESIDE OVER)
   - Group 20: **0.5038** | CENTER, RUN, TACKLE, SAFETY                                       | INCORRECT (Max overlap: 3/4 with AMERICAN FOOTBALL POSITIONS)

---

## Puzzle 77 (ID: 974)
**Words on Board:** DERBY, RINK, NET, GAIN, SWOON, PINE, YEARN, YIELD, RETURN, MOON, PUCK, COASTER, BAG, BRICK, BLOCK, CAKE

### Ground Truth Categories:
* **Level 0 (ACT LOVESTRUCK) [Type: SYNONYM_OR_NEAR]:** MOON, PINE, SWOON, YEARN
* **Level 1 (EARNINGS) [Type: SYNONYM_OR_NEAR]:** GAIN, NET, RETURN, YIELD
* **Level 2 (COMPACT MASS) [Type: SEMANTIC_SET]:** BLOCK, BRICK, CAKE, PUCK
* **Level 3 (ROLLER ___) [Type: FILL_IN_THE_BLANK]:** BAG, COASTER, DERBY, RINK

### Top Candidate Partitions:
1. **Partition Score: 0.4623**
   - Group 1: **0.6153** | NET, GAIN, YIELD, RETURN                                          | CORRECT GROUP (EARNINGS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.6%, no-rel 32.4%)]
   - Group 2: **0.4676** | BAG, BRICK, BLOCK, CAKE                                           | INCORRECT (Max overlap: 3/4 with COMPACT MASS)
   - Group 3: **0.4487** | DERBY, RINK, PUCK, COASTER                                        | INCORRECT (Max overlap: 3/4 with ROLLER ___)
   - Group 4: **0.4318** | SWOON, PINE, YEARN, MOON                                          | CORRECT GROUP (ACT LOVESTRUCK, Level 0)
2. **Partition Score: 0.4599**
   - Group 1: **0.5197** | DERBY, PINE, MOON, COASTER                                        | INCORRECT (Max overlap: 2/4 with ROLLER ___)
   - Group 2: **0.4833** | RINK, PUCK, BAG, BRICK                                            | INCORRECT (Max overlap: 2/4 with ROLLER ___)
   - Group 3: **0.4752** | GAIN, YEARN, YIELD, RETURN                                        | INCORRECT (Max overlap: 3/4 with EARNINGS) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 29.0%)]
   - Group 4: **0.4325** | NET, SWOON, BLOCK, CAKE                                           | INCORRECT (Max overlap: 2/4 with COMPACT MASS)
3. **Partition Score: 0.4594**
   - Group 1: **0.6153** | NET, GAIN, YIELD, RETURN                                          | CORRECT GROUP (EARNINGS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.6%, no-rel 32.4%)]
   - Group 2: **0.4447** | DERBY, PINE, YEARN, MOON                                          | INCORRECT (Max overlap: 3/4 with ACT LOVESTRUCK)
   - Group 3: **0.4397** | SWOON, BRICK, BLOCK, CAKE                                         | INCORRECT (Max overlap: 3/4 with COMPACT MASS)
   - Group 4: **0.4378** | RINK, PUCK, COASTER, BAG                                          | INCORRECT (Max overlap: 3/4 with ROLLER ___) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 21.6%)]
4. **Partition Score: 0.4570**
   - Group 1: **0.6153** | NET, GAIN, YIELD, RETURN                                          | CORRECT GROUP (EARNINGS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.6%, no-rel 32.4%)]
   - Group 2: **0.4612** | RINK, PUCK, COASTER, BRICK                                        | INCORRECT (Max overlap: 2/4 with ROLLER ___)
   - Group 3: **0.4447** | DERBY, PINE, YEARN, MOON                                          | INCORRECT (Max overlap: 3/4 with ACT LOVESTRUCK)
   - Group 4: **0.4252** | SWOON, BAG, BLOCK, CAKE                                           | INCORRECT (Max overlap: 2/4 with COMPACT MASS)
5. **Partition Score: 0.4564**
   - Group 1: **0.6153** | NET, GAIN, YIELD, RETURN                                          | CORRECT GROUP (EARNINGS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.6%, no-rel 32.4%)]
   - Group 2: **0.5197** | DERBY, PINE, MOON, COASTER                                        | INCORRECT (Max overlap: 2/4 with ROLLER ___)
   - Group 3: **0.4833** | RINK, PUCK, BAG, BRICK                                            | INCORRECT (Max overlap: 2/4 with ROLLER ___)
   - Group 4: **0.3886** | SWOON, YEARN, BLOCK, CAKE                                         | INCORRECT (Max overlap: 2/4 with ACT LOVESTRUCK)

### Top Candidate Groups:
   - Group 1: **0.6153** | NET, GAIN, YIELD, RETURN                                          | CORRECT GROUP (EARNINGS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.6%, no-rel 32.4%)]
   - Group 2: **0.4676** | BAG, BRICK, BLOCK, CAKE                                           | INCORRECT (Max overlap: 3/4 with COMPACT MASS)
   - Group 3: **0.4487** | DERBY, RINK, PUCK, COASTER                                        | INCORRECT (Max overlap: 3/4 with ROLLER ___)
   - Group 4: **0.4318** | SWOON, PINE, YEARN, MOON                                          | CORRECT GROUP (ACT LOVESTRUCK, Level 0)
   - Group 5: **0.5197** | DERBY, PINE, MOON, COASTER                                        | INCORRECT (Max overlap: 2/4 with ROLLER ___)
   - Group 6: **0.4833** | RINK, PUCK, BAG, BRICK                                            | INCORRECT (Max overlap: 2/4 with ROLLER ___)
   - Group 7: **0.4752** | GAIN, YEARN, YIELD, RETURN                                        | INCORRECT (Max overlap: 3/4 with EARNINGS) | [Pred Type: SYNONYM_OR_NEAR (63.8%, no-rel 29.0%)]
   - Group 8: **0.4325** | NET, SWOON, BLOCK, CAKE                                           | INCORRECT (Max overlap: 2/4 with COMPACT MASS)
   - Group 9: **0.4447** | DERBY, PINE, YEARN, MOON                                          | INCORRECT (Max overlap: 3/4 with ACT LOVESTRUCK)
   - Group 10: **0.4397** | SWOON, BRICK, BLOCK, CAKE                                         | INCORRECT (Max overlap: 3/4 with COMPACT MASS)
   - Group 11: **0.4378** | RINK, PUCK, COASTER, BAG                                          | INCORRECT (Max overlap: 3/4 with ROLLER ___) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 21.6%)]
   - Group 12: **0.4612** | RINK, PUCK, COASTER, BRICK                                        | INCORRECT (Max overlap: 2/4 with ROLLER ___)
   - Group 13: **0.4252** | SWOON, BAG, BLOCK, CAKE                                           | INCORRECT (Max overlap: 2/4 with COMPACT MASS)
   - Group 14: **0.3886** | SWOON, YEARN, BLOCK, CAKE                                         | INCORRECT (Max overlap: 2/4 with ACT LOVESTRUCK)
   - Group 15: **0.5234** | NET, SWOON, YIELD, RETURN                                         | INCORRECT (Max overlap: 3/4 with EARNINGS) | [Pred Type: SYNONYM_OR_NEAR (53.3%, no-rel 37.9%)]
   - Group 16: **0.4416** | GAIN, BAG, BLOCK, CAKE                                            | INCORRECT (Max overlap: 2/4 with COMPACT MASS)
   - Group 17: **0.4829** | SWOON, YEARN, YIELD, RETURN                                       | INCORRECT (Max overlap: 2/4 with ACT LOVESTRUCK) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 35.3%)]
   - Group 18: **0.4174** | NET, GAIN, BLOCK, CAKE                                            | INCORRECT (Max overlap: 2/4 with EARNINGS)
   - Group 19: **0.5396** | DERBY, PINE, MOON, BRICK                                          | INCORRECT (Max overlap: 2/4 with ACT LOVESTRUCK)
   - Group 20: **0.4286** | RINK, MOON, PUCK, COASTER                                         | INCORRECT (Max overlap: 2/4 with ROLLER ___)

---

## Puzzle 78 (ID: 515)
**Words on Board:** DIAL, ARTIST, YOGA, STEW, YEAR, MEDIUM, NAME, TITLE, EGADS, REPUTATION, HASH, SALAD, SCRAMBLE, MONTE, CHARACTER, IMAGE

### Ground Truth Categories:
* **Level 0 (FOOD-RELATED JUMBLES) [Type: SEMANTIC_SET]:** HASH, SALAD, SCRAMBLE, STEW
* **Level 1 (PUBLIC STANDING) [Type: SYNONYM_OR_NEAR]:** CHARACTER, IMAGE, NAME, REPUTATION
* **Level 2 (INFO ON A MUSEUM PLACARD) [Type: SEMANTIC_SET]:** ARTIST, MEDIUM, TITLE, YEAR
* **Level 3 (ANAGRAMS OF FAMOUS PAINTERS) [Type: WORDPLAY_TRANSFORM]:** DIAL, EGADS, MONTE, YOGA

### Top Candidate Partitions:
1. **Partition Score: 0.5327**
   - Group 1: **0.6093** | NAME, TITLE, REPUTATION, CHARACTER                                | INCORRECT (Max overlap: 3/4 with PUBLIC STANDING)
   - Group 2: **0.5832** | STEW, HASH, SALAD, SCRAMBLE                                       | CORRECT GROUP (FOOD-RELATED JUMBLES, Level 0)
   - Group 3: **0.5324** | YOGA, YEAR, EGADS, MONTE                                          | INCORRECT (Max overlap: 3/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 4: **0.4975** | DIAL, ARTIST, MEDIUM, IMAGE                                       | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
2. **Partition Score: 0.5270**
   - Group 1: **0.6093** | NAME, TITLE, REPUTATION, CHARACTER                                | INCORRECT (Max overlap: 3/4 with PUBLIC STANDING)
   - Group 2: **0.5408** | DIAL, STEW, HASH, SALAD                                           | INCORRECT (Max overlap: 3/4 with FOOD-RELATED JUMBLES)
   - Group 3: **0.5324** | YOGA, YEAR, EGADS, MONTE                                          | INCORRECT (Max overlap: 3/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 4: **0.5020** | ARTIST, MEDIUM, SCRAMBLE, IMAGE                                   | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
3. **Partition Score: 0.5245**
   - Group 1: **0.6093** | NAME, TITLE, REPUTATION, CHARACTER                                | INCORRECT (Max overlap: 3/4 with PUBLIC STANDING)
   - Group 2: **0.5389** | ARTIST, YOGA, YEAR, EGADS                                         | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
   - Group 3: **0.5173** | DIAL, MEDIUM, SCRAMBLE, MONTE                                     | INCORRECT (Max overlap: 2/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 4: **0.5032** | STEW, HASH, SALAD, IMAGE                                          | INCORRECT (Max overlap: 3/4 with FOOD-RELATED JUMBLES)
4. **Partition Score: 0.5236**
   - Group 1: **0.6093** | NAME, TITLE, REPUTATION, CHARACTER                                | INCORRECT (Max overlap: 3/4 with PUBLIC STANDING)
   - Group 2: **0.5324** | YOGA, YEAR, EGADS, MONTE                                          | INCORRECT (Max overlap: 3/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 3: **0.5190** | DIAL, ARTIST, MEDIUM, SCRAMBLE                                    | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
   - Group 4: **0.5032** | STEW, HASH, SALAD, IMAGE                                          | INCORRECT (Max overlap: 3/4 with FOOD-RELATED JUMBLES)
5. **Partition Score: 0.5207**
   - Group 1: **0.6093** | NAME, TITLE, REPUTATION, CHARACTER                                | INCORRECT (Max overlap: 3/4 with PUBLIC STANDING)
   - Group 2: **0.5202** | DIAL, EGADS, SCRAMBLE, MONTE                                      | INCORRECT (Max overlap: 3/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 3: **0.5161** | ARTIST, YOGA, YEAR, MEDIUM                                        | INCORRECT (Max overlap: 3/4 with INFO ON A MUSEUM PLACARD)
   - Group 4: **0.5032** | STEW, HASH, SALAD, IMAGE                                          | INCORRECT (Max overlap: 3/4 with FOOD-RELATED JUMBLES)

### Top Candidate Groups:
   - Group 1: **0.6093** | NAME, TITLE, REPUTATION, CHARACTER                                | INCORRECT (Max overlap: 3/4 with PUBLIC STANDING)
   - Group 2: **0.5832** | STEW, HASH, SALAD, SCRAMBLE                                       | CORRECT GROUP (FOOD-RELATED JUMBLES, Level 0)
   - Group 3: **0.5324** | YOGA, YEAR, EGADS, MONTE                                          | INCORRECT (Max overlap: 3/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 4: **0.4975** | DIAL, ARTIST, MEDIUM, IMAGE                                       | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
   - Group 5: **0.5408** | DIAL, STEW, HASH, SALAD                                           | INCORRECT (Max overlap: 3/4 with FOOD-RELATED JUMBLES)
   - Group 6: **0.5020** | ARTIST, MEDIUM, SCRAMBLE, IMAGE                                   | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
   - Group 7: **0.5389** | ARTIST, YOGA, YEAR, EGADS                                         | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
   - Group 8: **0.5173** | DIAL, MEDIUM, SCRAMBLE, MONTE                                     | INCORRECT (Max overlap: 2/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 9: **0.5032** | STEW, HASH, SALAD, IMAGE                                          | INCORRECT (Max overlap: 3/4 with FOOD-RELATED JUMBLES)
   - Group 10: **0.5190** | DIAL, ARTIST, MEDIUM, SCRAMBLE                                    | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
   - Group 11: **0.5202** | DIAL, EGADS, SCRAMBLE, MONTE                                      | INCORRECT (Max overlap: 3/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 12: **0.5161** | ARTIST, YOGA, YEAR, MEDIUM                                        | INCORRECT (Max overlap: 3/4 with INFO ON A MUSEUM PLACARD)
   - Group 13: **0.5248** | ARTIST, YOGA, YEAR, MONTE                                         | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
   - Group 14: **0.5101** | DIAL, MEDIUM, EGADS, SCRAMBLE                                     | INCORRECT (Max overlap: 2/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 15: **0.5100** | YOGA, YEAR, MEDIUM, MONTE                                         | INCORRECT (Max overlap: 2/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 16: **0.5094** | DIAL, ARTIST, EGADS, SCRAMBLE                                     | INCORRECT (Max overlap: 2/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 17: **0.5191** | DIAL, MEDIUM, EGADS, MONTE                                        | INCORRECT (Max overlap: 3/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 18: **0.4724** | ARTIST, YOGA, YEAR, IMAGE                                         | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)
   - Group 19: **0.4926** | DIAL, ARTIST, YOGA, IMAGE                                         | INCORRECT (Max overlap: 2/4 with ANAGRAMS OF FAMOUS PAINTERS)
   - Group 20: **0.4819** | YEAR, MEDIUM, EGADS, MONTE                                        | INCORRECT (Max overlap: 2/4 with INFO ON A MUSEUM PLACARD)

---

## Puzzle 79 (ID: 732)
**Words on Board:** SNUGGLING, MISSING, DISHING, CUDDLING, WHISPERING, BOWLING, BUZZING, ACUPUNCTURING, HUGGING, SIRING, WRESTLING, DOCTORING, SEWING, SPILLING, LORDING, SPOONING

### Ground Truth Categories:
* **Level 0 (GETTING COZY) [Type: SYNONYM_OR_NEAR]:** CUDDLING, HUGGING, SNUGGLING, SPOONING
* **Level 1 (GOSSIPING) [Type: SYNONYM_OR_NEAR]:** BUZZING, DISHING, SPILLING, WHISPERING
* **Level 2 (ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES) [Type: SEMANTIC_SET]:** ACUPUNCTURING, BOWLING, SEWING, WRESTLING
* **Level 3 (STARTING WITH TITLES) [Type: WORD_FORM]:** DOCTORING, LORDING, MISSING, SIRING

### Top Candidate Partitions:
1. **Partition Score: 0.5693**
   - Group 1: **0.7585** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5572** | DISHING, ACUPUNCTURING, SIRING, LORDING                           | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 3: **0.5426** | BOWLING, WRESTLING, DOCTORING, SEWING                             | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 4: **0.5420** | MISSING, WHISPERING, BUZZING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
2. **Partition Score: 0.5640**
   - Group 1: **0.7585** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5485** | ACUPUNCTURING, SIRING, DOCTORING, LORDING                         | INCORRECT (Max overlap: 3/4 with STARTING WITH TITLES)
   - Group 3: **0.5420** | MISSING, WHISPERING, BUZZING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 4: **0.5351** | DISHING, BOWLING, WRESTLING, SEWING                               | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
3. **Partition Score: 0.5605**
   - Group 1: **0.7585** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5974** | MISSING, DISHING, WHISPERING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 3: **0.5426** | BOWLING, WRESTLING, DOCTORING, SEWING                             | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 4: **0.5101** | BUZZING, ACUPUNCTURING, SIRING, LORDING                           | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
4. **Partition Score: 0.5603**
   - Group 1: **0.7585** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5457** | DISHING, ACUPUNCTURING, SIRING, DOCTORING                         | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 3: **0.5420** | MISSING, WHISPERING, BUZZING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 4: **0.5289** | BOWLING, WRESTLING, SEWING, LORDING                               | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
5. **Partition Score: 0.5602**
   - Group 1: **0.7585** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5748** | MISSING, DISHING, WHISPERING, BUZZING                             | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 3: **0.5426** | BOWLING, WRESTLING, DOCTORING, SEWING                             | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 4: **0.5177** | ACUPUNCTURING, SIRING, SPILLING, LORDING                          | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)

### Top Candidate Groups:
   - Group 1: **0.7585** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5572** | DISHING, ACUPUNCTURING, SIRING, LORDING                           | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 3: **0.5426** | BOWLING, WRESTLING, DOCTORING, SEWING                             | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 4: **0.5420** | MISSING, WHISPERING, BUZZING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 5: **0.5485** | ACUPUNCTURING, SIRING, DOCTORING, LORDING                         | INCORRECT (Max overlap: 3/4 with STARTING WITH TITLES)
   - Group 6: **0.5351** | DISHING, BOWLING, WRESTLING, SEWING                               | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 7: **0.5974** | MISSING, DISHING, WHISPERING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 8: **0.5101** | BUZZING, ACUPUNCTURING, SIRING, LORDING                           | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 9: **0.5457** | DISHING, ACUPUNCTURING, SIRING, DOCTORING                         | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 10: **0.5289** | BOWLING, WRESTLING, SEWING, LORDING                               | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 11: **0.5748** | MISSING, DISHING, WHISPERING, BUZZING                             | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 12: **0.5177** | ACUPUNCTURING, SIRING, SPILLING, LORDING                          | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 13: **0.5459** | DISHING, BOWLING, WRESTLING, DOCTORING                            | INCORRECT (Max overlap: 2/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 14: **0.5254** | ACUPUNCTURING, SIRING, SEWING, LORDING                            | INCORRECT (Max overlap: 2/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 15: **0.5362** | MISSING, WHISPERING, BUZZING, SIRING                              | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 16: **0.5258** | DISHING, ACUPUNCTURING, SPILLING, LORDING                         | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 17: **0.5447** | MISSING, DISHING, BUZZING, SPILLING                               | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 18: **0.5216** | WHISPERING, ACUPUNCTURING, SIRING, LORDING                        | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 19: **0.5289** | DISHING, ACUPUNCTURING, DOCTORING, SPILLING                       | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 20: **0.5993** | SNUGGLING, CUDDLING, ACUPUNCTURING, HUGGING                       | INCORRECT (Max overlap: 3/4 with GETTING COZY) | [Pred Type: SYNONYM_OR_NEAR (45.4%, no-rel 29.3%)]

---

## Puzzle 80 (ID: 940)
**Words on Board:** CIDER, INTEREST, MIRROR, SHARE, RINGER, WINE, STAKE, CRESCENT, GARLIC, CROSS, TROUSERS, STAR, DOUBLE, CLONE, CONCERN, STRIPE

### Ground Truth Categories:
* **Level 0 (DOPPELGÄNGER) [Type: SYNONYM_OR_NEAR]:** CLONE, DOUBLE, MIRROR, RINGER
* **Level 1 (PORTION) [Type: SYNONYM_OR_NEAR]:** CONCERN, INTEREST, SHARE, STAKE
* **Level 2 (COMMON FLAG SYMBOLS) [Type: SEMANTIC_SET]:** CRESCENT, CROSS, STAR, STRIPE
* **Level 3 (PRESSED USING A PRESS) [Type: FILL_IN_THE_BLANK]:** CIDER, GARLIC, TROUSERS, WINE

### Top Candidate Partitions:
1. **Partition Score: 0.5068**
   - Group 1: **0.6004** | CIDER, WINE, GARLIC, TROUSERS                                     | CORRECT GROUP (PRESSED USING A PRESS, Level 3)
   - Group 2: **0.5934** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 33.9%)]
   - Group 3: **0.4834** | MIRROR, CRESCENT, STAR, STRIPE                                    | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 4: **0.4631** | RINGER, CROSS, DOUBLE, CLONE                                      | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 19.5%)]
2. **Partition Score: 0.5044**
   - Group 1: **0.6004** | CIDER, WINE, GARLIC, TROUSERS                                     | CORRECT GROUP (PRESSED USING A PRESS, Level 3)
   - Group 2: **0.5934** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 33.9%)]
   - Group 3: **0.4927** | MIRROR, CRESCENT, CROSS, STAR                                     | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 4: **0.4550** | RINGER, DOUBLE, CLONE, STRIPE                                     | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER) | [Pred Type: SYNONYM_OR_NEAR (70.3%, no-rel 14.2%)]
3. **Partition Score: 0.4998**
   - Group 1: **0.6004** | CIDER, WINE, GARLIC, TROUSERS                                     | CORRECT GROUP (PRESSED USING A PRESS, Level 3)
   - Group 2: **0.5934** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 33.9%)]
   - Group 3: **0.5391** | CRESCENT, CROSS, STAR, STRIPE                                     | CORRECT GROUP (COMMON FLAG SYMBOLS, Level 2)
   - Group 4: **0.4291** | MIRROR, RINGER, DOUBLE, CLONE                                     | CORRECT GROUP (DOPPELGÄNGER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (66.1%, no-rel 14.9%)]
4. **Partition Score: 0.4990**
   - Group 1: **0.6004** | CIDER, WINE, GARLIC, TROUSERS                                     | CORRECT GROUP (PRESSED USING A PRESS, Level 3)
   - Group 2: **0.5934** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 33.9%)]
   - Group 3: **0.4648** | MIRROR, CRESCENT, STAR, DOUBLE                                    | INCORRECT (Max overlap: 2/4 with DOPPELGÄNGER)
   - Group 4: **0.4547** | RINGER, CROSS, CLONE, STRIPE                                      | INCORRECT (Max overlap: 2/4 with DOPPELGÄNGER) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 13.9%)]
5. **Partition Score: 0.4984**
   - Group 1: **0.5934** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 33.9%)]
   - Group 2: **0.5310** | CIDER, MIRROR, GARLIC, TROUSERS                                   | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 3: **0.5275** | WINE, CRESCENT, CROSS, STAR                                       | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 4: **0.4550** | RINGER, DOUBLE, CLONE, STRIPE                                     | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER) | [Pred Type: SYNONYM_OR_NEAR (70.3%, no-rel 14.2%)]

### Top Candidate Groups:
   - Group 1: **0.6004** | CIDER, WINE, GARLIC, TROUSERS                                     | CORRECT GROUP (PRESSED USING A PRESS, Level 3)
   - Group 2: **0.5934** | INTEREST, SHARE, STAKE, CONCERN                                   | CORRECT GROUP (PORTION, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 33.9%)]
   - Group 3: **0.4834** | MIRROR, CRESCENT, STAR, STRIPE                                    | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 4: **0.4631** | RINGER, CROSS, DOUBLE, CLONE                                      | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 19.5%)]
   - Group 5: **0.4927** | MIRROR, CRESCENT, CROSS, STAR                                     | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 6: **0.4550** | RINGER, DOUBLE, CLONE, STRIPE                                     | INCORRECT (Max overlap: 3/4 with DOPPELGÄNGER) | [Pred Type: SYNONYM_OR_NEAR (70.3%, no-rel 14.2%)]
   - Group 7: **0.5391** | CRESCENT, CROSS, STAR, STRIPE                                     | CORRECT GROUP (COMMON FLAG SYMBOLS, Level 2)
   - Group 8: **0.4291** | MIRROR, RINGER, DOUBLE, CLONE                                     | CORRECT GROUP (DOPPELGÄNGER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (66.1%, no-rel 14.9%)]
   - Group 9: **0.4648** | MIRROR, CRESCENT, STAR, DOUBLE                                    | INCORRECT (Max overlap: 2/4 with DOPPELGÄNGER)
   - Group 10: **0.4547** | RINGER, CROSS, CLONE, STRIPE                                      | INCORRECT (Max overlap: 2/4 with DOPPELGÄNGER) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 13.9%)]
   - Group 11: **0.5310** | CIDER, MIRROR, GARLIC, TROUSERS                                   | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 12: **0.5275** | WINE, CRESCENT, CROSS, STAR                                       | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 13: **0.5639** | CIDER, WINE, CRESCENT, GARLIC                                     | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 14: **0.4640** | MIRROR, TROUSERS, STAR, STRIPE                                    | INCORRECT (Max overlap: 2/4 with COMMON FLAG SYMBOLS)
   - Group 15: **0.5270** | CIDER, MIRROR, WINE, GARLIC                                       | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 16: **0.4694** | CRESCENT, TROUSERS, STAR, STRIPE                                  | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 17: **0.4774** | CRESCENT, CROSS, TROUSERS, STAR                                   | INCORRECT (Max overlap: 3/4 with COMMON FLAG SYMBOLS)
   - Group 18: **0.5330** | CIDER, WINE, CRESCENT, TROUSERS                                   | INCORRECT (Max overlap: 3/4 with PRESSED USING A PRESS)
   - Group 19: **0.4659** | MIRROR, GARLIC, STAR, DOUBLE                                      | INCORRECT (Max overlap: 2/4 with DOPPELGÄNGER) | [Pred Type: FILL_IN_THE_BLANK (45.4%, no-rel 17.9%)]
   - Group 20: **0.5059** | CIDER, MIRROR, CRESCENT, TROUSERS                                 | INCORRECT (Max overlap: 2/4 with PRESSED USING A PRESS)

---

## Puzzle 81 (ID: 85)
**Words on Board:** BRUSH, LAWN, EASEL, COMB, FOLDING, FIRST, DRIVE, HIGH, REVERSE, SAW, PALETTE, NEUTRAL, CANVAS, GEAR, ZIPPER, PARK

### Ground Truth Categories:
* **Level 0 (PAINTING ACCESSORIES) [Type: SEMANTIC_SET]:** BRUSH, CANVAS, EASEL, PALETTE
* **Level 1 (AUTOMATIC TRANSMISSION SETTINGS) [Type: SEMANTIC_SET]:** DRIVE, NEUTRAL, PARK, REVERSE
* **Level 2 (THINGS WITH TEETH) [Type: SEMANTIC_SET]:** COMB, GEAR, SAW, ZIPPER
* **Level 3 (___ CHAIR) [Type: FILL_IN_THE_BLANK]:** FIRST, FOLDING, HIGH, LAWN

### Top Candidate Partitions:
1. **Partition Score: 0.4919**
   - Group 1: **0.7013** | FIRST, DRIVE, GEAR, PARK                                          | INCORRECT (Max overlap: 2/4 with AUTOMATIC TRANSMISSION SETTINGS)
   - Group 2: **0.4907** | LAWN, EASEL, PALETTE, ZIPPER                                      | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES)
   - Group 3: **0.4634** | BRUSH, COMB, SAW, CANVAS                                          | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES)
   - Group 4: **0.4568** | FOLDING, HIGH, REVERSE, NEUTRAL                                   | INCORRECT (Max overlap: 2/4 with ___ CHAIR)
2. **Partition Score: 0.4910**
   - Group 1: **0.7013** | FIRST, DRIVE, GEAR, PARK                                          | INCORRECT (Max overlap: 2/4 with AUTOMATIC TRANSMISSION SETTINGS)
   - Group 2: **0.4885** | LAWN, EASEL, PALETTE, CANVAS                                      | INCORRECT (Max overlap: 3/4 with PAINTING ACCESSORIES) | [Pred Type: SEMANTIC_SET (50.3%, no-rel 19.8%)]
   - Group 3: **0.4605** | BRUSH, COMB, SAW, ZIPPER                                          | INCORRECT (Max overlap: 3/4 with THINGS WITH TEETH) | [Pred Type: SEMANTIC_SET (47.8%, no-rel 27.3%)]
   - Group 4: **0.4568** | FOLDING, HIGH, REVERSE, NEUTRAL                                   | INCORRECT (Max overlap: 2/4 with ___ CHAIR)
3. **Partition Score: 0.4750**
   - Group 1: **0.4940** | FIRST, DRIVE, HIGH, PARK                                          | INCORRECT (Max overlap: 2/4 with ___ CHAIR)
   - Group 2: **0.4907** | LAWN, EASEL, PALETTE, ZIPPER                                      | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES)
   - Group 3: **0.4795** | FOLDING, REVERSE, NEUTRAL, GEAR                                   | INCORRECT (Max overlap: 2/4 with AUTOMATIC TRANSMISSION SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (54.1%, no-rel 28.3%)]
   - Group 4: **0.4634** | BRUSH, COMB, SAW, CANVAS                                          | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES)
4. **Partition Score: 0.4731**
   - Group 1: **0.4940** | FIRST, DRIVE, HIGH, PARK                                          | INCORRECT (Max overlap: 2/4 with ___ CHAIR)
   - Group 2: **0.4885** | LAWN, EASEL, PALETTE, CANVAS                                      | INCORRECT (Max overlap: 3/4 with PAINTING ACCESSORIES) | [Pred Type: SEMANTIC_SET (50.3%, no-rel 19.8%)]
   - Group 3: **0.4795** | FOLDING, REVERSE, NEUTRAL, GEAR                                   | INCORRECT (Max overlap: 2/4 with AUTOMATIC TRANSMISSION SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (54.1%, no-rel 28.3%)]
   - Group 4: **0.4605** | BRUSH, COMB, SAW, ZIPPER                                          | INCORRECT (Max overlap: 3/4 with THINGS WITH TEETH) | [Pred Type: SEMANTIC_SET (47.8%, no-rel 27.3%)]
5. **Partition Score: 0.4728**
   - Group 1: **0.7013** | FIRST, DRIVE, GEAR, PARK                                          | INCORRECT (Max overlap: 2/4 with AUTOMATIC TRANSMISSION SETTINGS)
   - Group 2: **0.4568** | FOLDING, HIGH, REVERSE, NEUTRAL                                   | INCORRECT (Max overlap: 2/4 with ___ CHAIR)
   - Group 3: **0.4503** | LAWN, PALETTE, CANVAS, ZIPPER                                     | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES)
   - Group 4: **0.4368** | BRUSH, EASEL, COMB, SAW                                           | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES) | [Pred Type: SEMANTIC_SET (48.7%, no-rel 25.6%)]

### Top Candidate Groups:
   - Group 1: **0.7013** | FIRST, DRIVE, GEAR, PARK                                          | INCORRECT (Max overlap: 2/4 with AUTOMATIC TRANSMISSION SETTINGS)
   - Group 2: **0.4907** | LAWN, EASEL, PALETTE, ZIPPER                                      | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES)
   - Group 3: **0.4634** | BRUSH, COMB, SAW, CANVAS                                          | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES)
   - Group 4: **0.4568** | FOLDING, HIGH, REVERSE, NEUTRAL                                   | INCORRECT (Max overlap: 2/4 with ___ CHAIR)
   - Group 5: **0.4885** | LAWN, EASEL, PALETTE, CANVAS                                      | INCORRECT (Max overlap: 3/4 with PAINTING ACCESSORIES) | [Pred Type: SEMANTIC_SET (50.3%, no-rel 19.8%)]
   - Group 6: **0.4605** | BRUSH, COMB, SAW, ZIPPER                                          | INCORRECT (Max overlap: 3/4 with THINGS WITH TEETH) | [Pred Type: SEMANTIC_SET (47.8%, no-rel 27.3%)]
   - Group 7: **0.4940** | FIRST, DRIVE, HIGH, PARK                                          | INCORRECT (Max overlap: 2/4 with ___ CHAIR)
   - Group 8: **0.4795** | FOLDING, REVERSE, NEUTRAL, GEAR                                   | INCORRECT (Max overlap: 2/4 with AUTOMATIC TRANSMISSION SETTINGS) | [Pred Type: SYNONYM_OR_NEAR (54.1%, no-rel 28.3%)]
   - Group 9: **0.4503** | LAWN, PALETTE, CANVAS, ZIPPER                                     | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES)
   - Group 10: **0.4368** | BRUSH, EASEL, COMB, SAW                                           | INCORRECT (Max overlap: 2/4 with PAINTING ACCESSORIES) | [Pred Type: SEMANTIC_SET (48.7%, no-rel 25.6%)]
   - Group 11: **0.7137** | FIRST, HIGH, REVERSE, GEAR                                        | INCORRECT (Max overlap: 2/4 with ___ CHAIR) | [Pred Type: SYNONYM_OR_NEAR (55.8%, no-rel 31.4%)]
   - Group 12: **0.4403** | BRUSH, COMB, FOLDING, SAW                                         | INCORRECT (Max overlap: 2/4 with THINGS WITH TEETH)
   - Group 13: **0.4187** | DRIVE, NEUTRAL, ZIPPER, PARK                                      | INCORRECT (Max overlap: 3/4 with AUTOMATIC TRANSMISSION SETTINGS) | [Pred Type: SEMANTIC_SET (55.3%, no-rel 23.4%)]
   - Group 14: **0.6231** | FIRST, HIGH, REVERSE, PARK                                        | INCORRECT (Max overlap: 2/4 with ___ CHAIR)
   - Group 15: **0.4357** | DRIVE, NEUTRAL, GEAR, ZIPPER                                      | INCORRECT (Max overlap: 2/4 with AUTOMATIC TRANSMISSION SETTINGS) | [Pred Type: SEMANTIC_SET (49.9%, no-rel 19.9%)]
   - Group 16: **0.5628** | FIRST, DRIVE, REVERSE, PARK                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC TRANSMISSION SETTINGS)
   - Group 17: **0.5511** | BRUSH, EASEL, COMB, CANVAS                                        | INCORRECT (Max overlap: 3/4 with PAINTING ACCESSORIES) | [Pred Type: SEMANTIC_SET (54.6%, no-rel 26.2%)]
   - Group 18: **0.4432** | HIGH, SAW, NEUTRAL, GEAR                                          | INCORRECT (Max overlap: 2/4 with THINGS WITH TEETH) | [Pred Type: SYNONYM_OR_NEAR (45.1%, no-rel 32.2%)]
   - Group 19: **0.4247** | LAWN, FOLDING, PALETTE, ZIPPER                                    | INCORRECT (Max overlap: 2/4 with ___ CHAIR) | [Pred Type: SEMANTIC_SET (45.3%, no-rel 22.1%)]
   - Group 20: **0.4381** | LAWN, COMB, PALETTE, ZIPPER                                       | INCORRECT (Max overlap: 2/4 with THINGS WITH TEETH)

---

## Puzzle 82 (ID: 311)
**Words on Board:** MIND, SHARE, INFORMATION, PERCENTAGE, DIRT, POST, SECRETS, COLUMN, INTELLIGENCE, POLE, REGARD, OBSERVE, PILLAR, STAKE, FOLLOW, INTEREST

### Ground Truth Categories:
* **Level 0 (UPRIGHT SUPPORT) [Type: SYNONYM_OR_NEAR]:** COLUMN, PILLAR, POLE, POST
* **Level 1 (HEED, AS RULES) [Type: SYNONYM_OR_NEAR]:** FOLLOW, MIND, OBSERVE, REGARD
* **Level 2 (ALLOTMENT) [Type: SYNONYM_OR_NEAR]:** INTEREST, PERCENTAGE, SHARE, STAKE
* **Level 3 (GATHERED BY SPIES) [Type: SYNONYM_OR_NEAR]:** DIRT, INFORMATION, INTELLIGENCE, SECRETS

### Top Candidate Partitions:
1. **Partition Score: 0.4431**
   - Group 1: **0.5943** | SHARE, PERCENTAGE, STAKE, INTEREST                                | CORRECT GROUP (ALLOTMENT, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.8%, no-rel 35.6%)]
   - Group 2: **0.5573** | POST, COLUMN, POLE, PILLAR                                        | CORRECT GROUP (UPRIGHT SUPPORT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 32.2%)]
   - Group 3: **0.4834** | MIND, REGARD, OBSERVE, FOLLOW                                     | CORRECT GROUP (HEED, AS RULES, Level 1) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 36.2%)]
   - Group 4: **0.3535** | INFORMATION, DIRT, SECRETS, INTELLIGENCE                          | CORRECT GROUP (GATHERED BY SPIES, Level 3) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 13.6%)]
2. **Partition Score: 0.4431**
   - Group 1: **0.5943** | SHARE, PERCENTAGE, STAKE, INTEREST                                | CORRECT GROUP (ALLOTMENT, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.8%, no-rel 35.6%)]
   - Group 2: **0.5573** | POST, COLUMN, POLE, PILLAR                                        | CORRECT GROUP (UPRIGHT SUPPORT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 32.2%)]
   - Group 3: **0.4667** | MIND, INFORMATION, SECRETS, INTELLIGENCE                          | INCORRECT (Max overlap: 3/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (64.1%, no-rel 15.1%)]
   - Group 4: **0.3594** | DIRT, REGARD, OBSERVE, FOLLOW                                     | INCORRECT (Max overlap: 3/4 with HEED, AS RULES) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 15.7%)]
3. **Partition Score: 0.4354**
   - Group 1: **0.5943** | SHARE, PERCENTAGE, STAKE, INTEREST                                | CORRECT GROUP (ALLOTMENT, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.8%, no-rel 35.6%)]
   - Group 2: **0.5573** | POST, COLUMN, POLE, PILLAR                                        | CORRECT GROUP (UPRIGHT SUPPORT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 32.2%)]
   - Group 3: **0.3812** | SECRETS, REGARD, OBSERVE, FOLLOW                                  | INCORRECT (Max overlap: 3/4 with HEED, AS RULES) | [Pred Type: SYNONYM_OR_NEAR (56.5%, no-rel 21.6%)]
   - Group 4: **0.3757** | MIND, INFORMATION, DIRT, INTELLIGENCE                             | INCORRECT (Max overlap: 3/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 15.5%)]
4. **Partition Score: 0.4268**
   - Group 1: **0.5943** | SHARE, PERCENTAGE, STAKE, INTEREST                                | CORRECT GROUP (ALLOTMENT, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.8%, no-rel 35.6%)]
   - Group 2: **0.4834** | MIND, REGARD, OBSERVE, FOLLOW                                     | CORRECT GROUP (HEED, AS RULES, Level 1) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 36.2%)]
   - Group 3: **0.4275** | INFORMATION, POST, SECRETS, INTELLIGENCE                          | INCORRECT (Max overlap: 3/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 24.4%)]
   - Group 4: **0.3691** | DIRT, COLUMN, POLE, PILLAR                                        | INCORRECT (Max overlap: 3/4 with UPRIGHT SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (52.1%, no-rel 23.7%)]
5. **Partition Score: 0.4256**
   - Group 1: **0.6024** | MIND, INFORMATION, INTELLIGENCE, INTEREST                         | INCORRECT (Max overlap: 2/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 33.4%)]
   - Group 2: **0.5573** | POST, COLUMN, POLE, PILLAR                                        | CORRECT GROUP (UPRIGHT SUPPORT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 32.2%)]
   - Group 3: **0.3685** | SHARE, PERCENTAGE, SECRETS, STAKE                                 | INCORRECT (Max overlap: 3/4 with ALLOTMENT) | [Pred Type: SYNONYM_OR_NEAR (56.5%, no-rel 24.5%)]
   - Group 4: **0.3594** | DIRT, REGARD, OBSERVE, FOLLOW                                     | INCORRECT (Max overlap: 3/4 with HEED, AS RULES) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 15.7%)]

### Top Candidate Groups:
   - Group 1: **0.5943** | SHARE, PERCENTAGE, STAKE, INTEREST                                | CORRECT GROUP (ALLOTMENT, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.8%, no-rel 35.6%)]
   - Group 2: **0.5573** | POST, COLUMN, POLE, PILLAR                                        | CORRECT GROUP (UPRIGHT SUPPORT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 32.2%)]
   - Group 3: **0.4834** | MIND, REGARD, OBSERVE, FOLLOW                                     | CORRECT GROUP (HEED, AS RULES, Level 1) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 36.2%)]
   - Group 4: **0.3535** | INFORMATION, DIRT, SECRETS, INTELLIGENCE                          | CORRECT GROUP (GATHERED BY SPIES, Level 3) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 13.6%)]
   - Group 5: **0.4667** | MIND, INFORMATION, SECRETS, INTELLIGENCE                          | INCORRECT (Max overlap: 3/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (64.1%, no-rel 15.1%)]
   - Group 6: **0.3594** | DIRT, REGARD, OBSERVE, FOLLOW                                     | INCORRECT (Max overlap: 3/4 with HEED, AS RULES) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 15.7%)]
   - Group 7: **0.3812** | SECRETS, REGARD, OBSERVE, FOLLOW                                  | INCORRECT (Max overlap: 3/4 with HEED, AS RULES) | [Pred Type: SYNONYM_OR_NEAR (56.5%, no-rel 21.6%)]
   - Group 8: **0.3757** | MIND, INFORMATION, DIRT, INTELLIGENCE                             | INCORRECT (Max overlap: 3/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 15.5%)]
   - Group 9: **0.4275** | INFORMATION, POST, SECRETS, INTELLIGENCE                          | INCORRECT (Max overlap: 3/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 24.4%)]
   - Group 10: **0.3691** | DIRT, COLUMN, POLE, PILLAR                                        | INCORRECT (Max overlap: 3/4 with UPRIGHT SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (52.1%, no-rel 23.7%)]
   - Group 11: **0.6024** | MIND, INFORMATION, INTELLIGENCE, INTEREST                         | INCORRECT (Max overlap: 2/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 33.4%)]
   - Group 12: **0.3685** | SHARE, PERCENTAGE, SECRETS, STAKE                                 | INCORRECT (Max overlap: 3/4 with ALLOTMENT) | [Pred Type: SYNONYM_OR_NEAR (56.5%, no-rel 24.5%)]
   - Group 13: **0.4282** | REGARD, OBSERVE, STAKE, FOLLOW                                    | INCORRECT (Max overlap: 3/4 with HEED, AS RULES) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 38.5%)]
   - Group 14: **0.3773** | SHARE, PERCENTAGE, DIRT, INTEREST                                 | INCORRECT (Max overlap: 3/4 with ALLOTMENT) | [Pred Type: SYNONYM_OR_NEAR (62.2%, no-rel 16.8%)]
   - Group 15: **0.5229** | REGARD, OBSERVE, FOLLOW, INTEREST                                 | INCORRECT (Max overlap: 3/4 with HEED, AS RULES)
   - Group 16: **0.4876** | MIND, INFORMATION, POST, INTELLIGENCE                             | INCORRECT (Max overlap: 2/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 32.6%)]
   - Group 17: **0.3331** | SHARE, PERCENTAGE, DIRT, STAKE                                    | INCORRECT (Max overlap: 3/4 with ALLOTMENT) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 19.1%)]
   - Group 18: **0.4350** | DIRT, POST, COLUMN, PILLAR                                        | INCORRECT (Max overlap: 3/4 with UPRIGHT SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 28.4%)]
   - Group 19: **0.3931** | MIND, INFORMATION, INTELLIGENCE, POLE                             | INCORRECT (Max overlap: 2/4 with GATHERED BY SPIES) | [Pred Type: SYNONYM_OR_NEAR (64.3%, no-rel 21.0%)]
   - Group 20: **0.3965** | PERCENTAGE, REGARD, OBSERVE, FOLLOW                               | INCORRECT (Max overlap: 3/4 with HEED, AS RULES) | [Pred Type: SYNONYM_OR_NEAR (54.5%, no-rel 31.7%)]

---

## Puzzle 83 (ID: 375)
**Words on Board:** BOLT, NAIL, CHAIR, STRIKE, BUG, DRYER, NUT, ROD, MIRROR, FLY, SCREW, LINE, SINK, WASHER, HOOK, SINKER

### Ground Truth Categories:
* **Level 0 (BITS OF HARDWARE) [Type: SEMANTIC_SET]:** NAIL, NUT, SCREW, WASHER
* **Level 1 (FISHING GEAR) [Type: SEMANTIC_SET]:** FLY, HOOK, LINE, SINKER
* **Level 2 (HAIR SALON FIXTURES) [Type: SEMANTIC_SET]:** CHAIR, DRYER, MIRROR, SINK
* **Level 3 (LIGHTNING ___) [Type: FILL_IN_THE_BLANK]:** BOLT, BUG, ROD, STRIKE

### Top Candidate Partitions:
1. **Partition Score: 0.5407**
   - Group 1: **0.7210** | BOLT, NAIL, NUT, SCREW                                            | INCORRECT (Max overlap: 3/4 with BITS OF HARDWARE)
   - Group 2: **0.5845** | CHAIR, DRYER, MIRROR, WASHER                                      | INCORRECT (Max overlap: 3/4 with HAIR SALON FIXTURES)
   - Group 3: **0.5434** | STRIKE, LINE, SINK, SINKER                                        | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 4: **0.4841** | BUG, ROD, FLY, HOOK                                               | INCORRECT (Max overlap: 2/4 with LIGHTNING ___)
2. **Partition Score: 0.5400**
   - Group 1: **0.7210** | BOLT, NAIL, NUT, SCREW                                            | INCORRECT (Max overlap: 3/4 with BITS OF HARDWARE)
   - Group 2: **0.5845** | CHAIR, DRYER, MIRROR, WASHER                                      | INCORRECT (Max overlap: 3/4 with HAIR SALON FIXTURES)
   - Group 3: **0.5249** | STRIKE, FLY, SINK, SINKER                                         | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 4: **0.4896** | BUG, ROD, LINE, HOOK                                              | INCORRECT (Max overlap: 2/4 with LIGHTNING ___)
3. **Partition Score: 0.5382**
   - Group 1: **0.7210** | BOLT, NAIL, NUT, SCREW                                            | INCORRECT (Max overlap: 3/4 with BITS OF HARDWARE)
   - Group 2: **0.5845** | CHAIR, DRYER, MIRROR, WASHER                                      | INCORRECT (Max overlap: 3/4 with HAIR SALON FIXTURES)
   - Group 3: **0.5188** | ROD, LINE, SINK, SINKER                                           | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 4: **0.4882** | STRIKE, BUG, FLY, HOOK                                            | INCORRECT (Max overlap: 2/4 with LIGHTNING ___)
4. **Partition Score: 0.5342**
   - Group 1: **0.5513** | NAIL, NUT, SCREW, HOOK                                            | INCORRECT (Max overlap: 3/4 with BITS OF HARDWARE)
   - Group 2: **0.5418** | CHAIR, ROD, MIRROR, LINE                                          | INCORRECT (Max overlap: 2/4 with HAIR SALON FIXTURES)
   - Group 3: **0.5386** | DRYER, SINK, WASHER, SINKER                                       | INCORRECT (Max overlap: 2/4 with HAIR SALON FIXTURES)
   - Group 4: **0.5261** | BOLT, STRIKE, BUG, FLY                                            | INCORRECT (Max overlap: 3/4 with LIGHTNING ___)
5. **Partition Score: 0.5340**
   - Group 1: **0.7210** | BOLT, NAIL, NUT, SCREW                                            | INCORRECT (Max overlap: 3/4 with BITS OF HARDWARE)
   - Group 2: **0.5576** | ROD, MIRROR, LINE, SINKER                                         | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 3: **0.5235** | CHAIR, DRYER, SINK, WASHER                                        | INCORRECT (Max overlap: 3/4 with HAIR SALON FIXTURES)
   - Group 4: **0.4882** | STRIKE, BUG, FLY, HOOK                                            | INCORRECT (Max overlap: 2/4 with LIGHTNING ___)

### Top Candidate Groups:
   - Group 1: **0.7210** | BOLT, NAIL, NUT, SCREW                                            | INCORRECT (Max overlap: 3/4 with BITS OF HARDWARE)
   - Group 2: **0.5845** | CHAIR, DRYER, MIRROR, WASHER                                      | INCORRECT (Max overlap: 3/4 with HAIR SALON FIXTURES)
   - Group 3: **0.5434** | STRIKE, LINE, SINK, SINKER                                        | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 4: **0.4841** | BUG, ROD, FLY, HOOK                                               | INCORRECT (Max overlap: 2/4 with LIGHTNING ___)
   - Group 5: **0.5249** | STRIKE, FLY, SINK, SINKER                                         | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 6: **0.4896** | BUG, ROD, LINE, HOOK                                              | INCORRECT (Max overlap: 2/4 with LIGHTNING ___)
   - Group 7: **0.5188** | ROD, LINE, SINK, SINKER                                           | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 8: **0.4882** | STRIKE, BUG, FLY, HOOK                                            | INCORRECT (Max overlap: 2/4 with LIGHTNING ___)
   - Group 9: **0.5513** | NAIL, NUT, SCREW, HOOK                                            | INCORRECT (Max overlap: 3/4 with BITS OF HARDWARE)
   - Group 10: **0.5418** | CHAIR, ROD, MIRROR, LINE                                          | INCORRECT (Max overlap: 2/4 with HAIR SALON FIXTURES)
   - Group 11: **0.5386** | DRYER, SINK, WASHER, SINKER                                       | INCORRECT (Max overlap: 2/4 with HAIR SALON FIXTURES)
   - Group 12: **0.5261** | BOLT, STRIKE, BUG, FLY                                            | INCORRECT (Max overlap: 3/4 with LIGHTNING ___)
   - Group 13: **0.5576** | ROD, MIRROR, LINE, SINKER                                         | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 14: **0.5235** | CHAIR, DRYER, SINK, WASHER                                        | INCORRECT (Max overlap: 3/4 with HAIR SALON FIXTURES)
   - Group 15: **0.5756** | CHAIR, DRYER, WASHER, SINKER                                      | INCORRECT (Max overlap: 2/4 with HAIR SALON FIXTURES)
   - Group 16: **0.4874** | ROD, MIRROR, LINE, SINK                                           | INCORRECT (Max overlap: 2/4 with HAIR SALON FIXTURES)
   - Group 17: **0.5309** | BOLT, NAIL, FLY, SCREW                                            | INCORRECT (Max overlap: 2/4 with BITS OF HARDWARE)
   - Group 18: **0.5094** | BUG, NUT, ROD, HOOK                                               | INCORRECT (Max overlap: 2/4 with LIGHTNING ___)
   - Group 19: **0.5434** | CHAIR, ROD, LINE, SINKER                                          | INCORRECT (Max overlap: 2/4 with FISHING GEAR)
   - Group 20: **0.5067** | DRYER, MIRROR, SINK, WASHER                                       | INCORRECT (Max overlap: 3/4 with HAIR SALON FIXTURES)

---

## Puzzle 84 (ID: 975)
**Words on Board:** MAKE, PRODUCE, TIGHT, FIRM, MOLD, DANCING, FROZEN, FAST, DAIRY, A, CARD, JAY, FORM, DRAG, YANK, MAY

### Ground Truth Categories:
* **Level 0 (CONSTRUCT) [Type: SYNONYM_OR_NEAR]:** FORM, MAKE, MOLD, PRODUCE
* **Level 1 (FIXED IN PLACE) [Type: SYNONYM_OR_NEAR]:** FAST, FIRM, FROZEN, TIGHT
* **Level 2 (MLB PLAYER, FOR SHORT) [Type: NAMED_ENTITY_SET]:** A, CARD, JAY, YANK
* **Level 3 (___ QUEEN) [Type: FILL_IN_THE_BLANK]:** DAIRY, DANCING, DRAG, MAY

### Top Candidate Partitions:
1. **Partition Score: 0.5313**
   - Group 1: **0.7590** | MAKE, PRODUCE, MOLD, FORM                                         | CORRECT GROUP (CONSTRUCT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 26.0%)]
   - Group 2: **0.5527** | DAIRY, A, JAY, MAY                                                | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 3: **0.5393** | DANCING, CARD, DRAG, YANK                                         | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 4: **0.4706** | TIGHT, FIRM, FROZEN, FAST                                         | CORRECT GROUP (FIXED IN PLACE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 32.4%)]
2. **Partition Score: 0.5294**
   - Group 1: **0.7590** | MAKE, PRODUCE, MOLD, FORM                                         | CORRECT GROUP (CONSTRUCT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 26.0%)]
   - Group 2: **0.5592** | DANCING, FROZEN, DAIRY, CARD                                      | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 3: **0.5538** | A, JAY, YANK, MAY                                                 | INCORRECT (Max overlap: 3/4 with MLB PLAYER, FOR SHORT)
   - Group 4: **0.4592** | TIGHT, FIRM, FAST, DRAG                                           | INCORRECT (Max overlap: 3/4 with FIXED IN PLACE) | [Pred Type: SYNONYM_OR_NEAR (48.9%, no-rel 38.8%)]
3. **Partition Score: 0.5256**
   - Group 1: **0.7590** | MAKE, PRODUCE, MOLD, FORM                                         | CORRECT GROUP (CONSTRUCT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 26.0%)]
   - Group 2: **0.5775** | A, CARD, JAY, MAY                                                 | INCORRECT (Max overlap: 3/4 with MLB PLAYER, FOR SHORT)
   - Group 3: **0.4839** | DANCING, DAIRY, DRAG, YANK                                        | INCORRECT (Max overlap: 3/4 with ___ QUEEN)
   - Group 4: **0.4706** | TIGHT, FIRM, FROZEN, FAST                                         | CORRECT GROUP (FIXED IN PLACE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 32.4%)]
4. **Partition Score: 0.5230**
   - Group 1: **0.7590** | MAKE, PRODUCE, MOLD, FORM                                         | CORRECT GROUP (CONSTRUCT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 26.0%)]
   - Group 2: **0.5797** | DAIRY, A, CARD, MAY                                               | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 3: **0.4706** | TIGHT, FIRM, FROZEN, FAST                                         | CORRECT GROUP (FIXED IN PLACE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 32.4%)]
   - Group 4: **0.4696** | DANCING, JAY, DRAG, YANK                                          | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
5. **Partition Score: 0.5226**
   - Group 1: **0.7590** | MAKE, PRODUCE, MOLD, FORM                                         | CORRECT GROUP (CONSTRUCT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 26.0%)]
   - Group 2: **0.5629** | DANCING, A, JAY, MAY                                              | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 3: **0.4828** | DAIRY, CARD, DRAG, YANK                                           | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 4: **0.4706** | TIGHT, FIRM, FROZEN, FAST                                         | CORRECT GROUP (FIXED IN PLACE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 32.4%)]

### Top Candidate Groups:
   - Group 1: **0.7590** | MAKE, PRODUCE, MOLD, FORM                                         | CORRECT GROUP (CONSTRUCT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (65.3%, no-rel 26.0%)]
   - Group 2: **0.5527** | DAIRY, A, JAY, MAY                                                | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 3: **0.5393** | DANCING, CARD, DRAG, YANK                                         | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 4: **0.4706** | TIGHT, FIRM, FROZEN, FAST                                         | CORRECT GROUP (FIXED IN PLACE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 32.4%)]
   - Group 5: **0.5592** | DANCING, FROZEN, DAIRY, CARD                                      | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 6: **0.5538** | A, JAY, YANK, MAY                                                 | INCORRECT (Max overlap: 3/4 with MLB PLAYER, FOR SHORT)
   - Group 7: **0.4592** | TIGHT, FIRM, FAST, DRAG                                           | INCORRECT (Max overlap: 3/4 with FIXED IN PLACE) | [Pred Type: SYNONYM_OR_NEAR (48.9%, no-rel 38.8%)]
   - Group 8: **0.5775** | A, CARD, JAY, MAY                                                 | INCORRECT (Max overlap: 3/4 with MLB PLAYER, FOR SHORT)
   - Group 9: **0.4839** | DANCING, DAIRY, DRAG, YANK                                        | INCORRECT (Max overlap: 3/4 with ___ QUEEN)
   - Group 10: **0.5797** | DAIRY, A, CARD, MAY                                               | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 11: **0.4696** | DANCING, JAY, DRAG, YANK                                          | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 12: **0.5629** | DANCING, A, JAY, MAY                                              | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 13: **0.4828** | DAIRY, CARD, DRAG, YANK                                           | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 14: **0.4933** | DANCING, FROZEN, DAIRY, YANK                                      | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 15: **0.4776** | TIGHT, FIRM, DANCING, FAST                                        | INCORRECT (Max overlap: 3/4 with FIXED IN PLACE) | [Pred Type: SYNONYM_OR_NEAR (45.8%, no-rel 26.3%)]
   - Group 16: **0.4646** | FROZEN, DAIRY, DRAG, YANK                                         | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 17: **0.5504** | DAIRY, CARD, JAY, MAY                                             | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 18: **0.4874** | DANCING, A, DRAG, YANK                                            | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 19: **0.5615** | DAIRY, JAY, YANK, MAY                                             | INCORRECT (Max overlap: 2/4 with ___ QUEEN)
   - Group 20: **0.4744** | DANCING, A, CARD, DRAG                                            | INCORRECT (Max overlap: 2/4 with ___ QUEEN)

---

## Puzzle 85 (ID: 445)
**Words on Board:** ELECTRONIC, BROWN, YOUNG, REGARD, COUNT, NOBLE, DUKE, PLAYER, SMITH, GAMBLE, CONSIDER, HOWARD, JUDGE, GRAND, UPRIGHT, JOHNSON

### Ground Truth Categories:
* **Level 0 (KINDS OF PIANOS) [Type: SEMANTIC_SET]:** ELECTRONIC, GRAND, PLAYER, UPRIGHT
* **Level 1 (DEEM) [Type: SYNONYM_OR_NEAR]:** CONSIDER, COUNT, JUDGE, REGARD
* **Level 2 (U.S. COLLEGES/UNIVERSITIES) [Type: NAMED_ENTITY_SET]:** BROWN, DUKE, HOWARD, SMITH
* **Level 3 (SECOND NAMES IN COMPANIES WITH AMPERSANDS) [Type: NAMED_ENTITY_SET]:** GAMBLE, JOHNSON, NOBLE, YOUNG

### Top Candidate Partitions:
1. **Partition Score: 0.5199**
   - Group 1: **0.6787** | REGARD, COUNT, CONSIDER, JUDGE                                    | CORRECT GROUP (DEEM, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.9%, no-rel 32.6%)]
   - Group 2: **0.5410** | NOBLE, GAMBLE, GRAND, UPRIGHT                                     | INCORRECT (Max overlap: 2/4 with SECOND NAMES IN COMPANIES WITH AMPERSANDS) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 27.6%)]
   - Group 3: **0.5181** | DUKE, SMITH, HOWARD, JOHNSON                                      | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES) | [Pred Type: NAMED_ENTITY_SET (52.5%, no-rel 22.2%)]
   - Group 4: **0.4780** | ELECTRONIC, BROWN, YOUNG, PLAYER                                  | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
2. **Partition Score: 0.5150**
   - Group 1: **0.6787** | REGARD, COUNT, CONSIDER, JUDGE                                    | CORRECT GROUP (DEEM, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.9%, no-rel 32.6%)]
   - Group 2: **0.5410** | NOBLE, GAMBLE, GRAND, UPRIGHT                                     | INCORRECT (Max overlap: 2/4 with SECOND NAMES IN COMPANIES WITH AMPERSANDS) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 27.6%)]
   - Group 3: **0.5109** | ELECTRONIC, PLAYER, SMITH, HOWARD                                 | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
   - Group 4: **0.4711** | BROWN, YOUNG, DUKE, JOHNSON                                       | INCORRECT (Max overlap: 2/4 with U.S. COLLEGES/UNIVERSITIES) | [Pred Type: NAMED_ENTITY_SET (45.1%, no-rel 22.7%)]
3. **Partition Score: 0.5118**
   - Group 1: **0.6787** | REGARD, COUNT, CONSIDER, JUDGE                                    | CORRECT GROUP (DEEM, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.9%, no-rel 32.6%)]
   - Group 2: **0.5638** | BROWN, DUKE, HOWARD, JOHNSON                                      | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES)
   - Group 3: **0.5410** | NOBLE, GAMBLE, GRAND, UPRIGHT                                     | INCORRECT (Max overlap: 2/4 with SECOND NAMES IN COMPANIES WITH AMPERSANDS) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 27.6%)]
   - Group 4: **0.4455** | ELECTRONIC, YOUNG, PLAYER, SMITH                                  | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
4. **Partition Score: 0.5102**
   - Group 1: **0.6787** | REGARD, COUNT, CONSIDER, JUDGE                                    | CORRECT GROUP (DEEM, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.9%, no-rel 32.6%)]
   - Group 2: **0.5410** | NOBLE, GAMBLE, GRAND, UPRIGHT                                     | INCORRECT (Max overlap: 2/4 with SECOND NAMES IN COMPANIES WITH AMPERSANDS) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 27.6%)]
   - Group 3: **0.5363** | BROWN, DUKE, SMITH, JOHNSON                                       | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES) | [Pred Type: NAMED_ENTITY_SET (45.6%, no-rel 27.2%)]
   - Group 4: **0.4525** | ELECTRONIC, YOUNG, PLAYER, HOWARD                                 | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
5. **Partition Score: 0.5100**
   - Group 1: **0.6787** | REGARD, COUNT, CONSIDER, JUDGE                                    | CORRECT GROUP (DEEM, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.9%, no-rel 32.6%)]
   - Group 2: **0.5410** | NOBLE, GAMBLE, GRAND, UPRIGHT                                     | INCORRECT (Max overlap: 2/4 with SECOND NAMES IN COMPANIES WITH AMPERSANDS) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 27.6%)]
   - Group 3: **0.5199** | ELECTRONIC, PLAYER, SMITH, JOHNSON                                | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
   - Group 4: **0.4580** | BROWN, YOUNG, DUKE, HOWARD                                        | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES)

### Top Candidate Groups:
   - Group 1: **0.6787** | REGARD, COUNT, CONSIDER, JUDGE                                    | CORRECT GROUP (DEEM, Level 1) | [Pred Type: SYNONYM_OR_NEAR (60.9%, no-rel 32.6%)]
   - Group 2: **0.5410** | NOBLE, GAMBLE, GRAND, UPRIGHT                                     | INCORRECT (Max overlap: 2/4 with SECOND NAMES IN COMPANIES WITH AMPERSANDS) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 27.6%)]
   - Group 3: **0.5181** | DUKE, SMITH, HOWARD, JOHNSON                                      | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES) | [Pred Type: NAMED_ENTITY_SET (52.5%, no-rel 22.2%)]
   - Group 4: **0.4780** | ELECTRONIC, BROWN, YOUNG, PLAYER                                  | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
   - Group 5: **0.5109** | ELECTRONIC, PLAYER, SMITH, HOWARD                                 | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
   - Group 6: **0.4711** | BROWN, YOUNG, DUKE, JOHNSON                                       | INCORRECT (Max overlap: 2/4 with U.S. COLLEGES/UNIVERSITIES) | [Pred Type: NAMED_ENTITY_SET (45.1%, no-rel 22.7%)]
   - Group 7: **0.5638** | BROWN, DUKE, HOWARD, JOHNSON                                      | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES)
   - Group 8: **0.4455** | ELECTRONIC, YOUNG, PLAYER, SMITH                                  | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
   - Group 9: **0.5363** | BROWN, DUKE, SMITH, JOHNSON                                       | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES) | [Pred Type: NAMED_ENTITY_SET (45.6%, no-rel 27.2%)]
   - Group 10: **0.4525** | ELECTRONIC, YOUNG, PLAYER, HOWARD                                 | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
   - Group 11: **0.5199** | ELECTRONIC, PLAYER, SMITH, JOHNSON                                | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
   - Group 12: **0.4580** | BROWN, YOUNG, DUKE, HOWARD                                        | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES)
   - Group 13: **0.5328** | ELECTRONIC, PLAYER, HOWARD, JOHNSON                               | INCORRECT (Max overlap: 2/4 with KINDS OF PIANOS)
   - Group 14: **0.4518** | BROWN, YOUNG, DUKE, SMITH                                         | INCORRECT (Max overlap: 3/4 with U.S. COLLEGES/UNIVERSITIES)
   - Group 15: **0.4912** | YOUNG, NOBLE, GAMBLE, GRAND                                       | INCORRECT (Max overlap: 3/4 with SECOND NAMES IN COMPANIES WITH AMPERSANDS) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 25.5%)]
   - Group 16: **0.4741** | ELECTRONIC, BROWN, PLAYER, UPRIGHT                                | INCORRECT (Max overlap: 3/4 with KINDS OF PIANOS)
   - Group 17: **0.4732** | ELECTRONIC, BROWN, DUKE, JOHNSON                                  | INCORRECT (Max overlap: 2/4 with U.S. COLLEGES/UNIVERSITIES)
   - Group 18: **0.4688** | YOUNG, PLAYER, SMITH, HOWARD                                      | INCORRECT (Max overlap: 2/4 with U.S. COLLEGES/UNIVERSITIES) | [Pred Type: NAMED_ENTITY_SET (50.6%, no-rel 19.7%)]
   - Group 19: **0.5753** | YOUNG, NOBLE, GRAND, UPRIGHT                                      | INCORRECT (Max overlap: 2/4 with SECOND NAMES IN COMPANIES WITH AMPERSANDS) | [Pred Type: SYNONYM_OR_NEAR (46.1%, no-rel 29.2%)]
   - Group 20: **0.5160** | BROWN, DUKE, SMITH, HOWARD                                        | CORRECT GROUP (U.S. COLLEGES/UNIVERSITIES, Level 2)

---

## Puzzle 86 (ID: 1067)
**Words on Board:** EARP, RED, WIKI, CHEAP, PARE, TWIN, PÈRE, SPLIT, CRACK, PADRE, ROYAL, LUMP, PEAR, POP, BLOW, PAIR

### Ground Truth Categories:
* **Level 0 (HOMOPHONES) [Type: SOUND_OR_SPELLING]:** PAIR, PARE, PEAR, PÈRE
* **Level 1 (RUPTURE) [Type: SYNONYM_OR_NEAR]:** BLOW, CRACK, POP, SPLIT
* **Level 2 (MLB PLAYER) [Type: NAMED_ENTITY_SET]:** PADRE, RED, ROYAL, TWIN
* **Level 3 (FRUIT ANAGRAMS) [Type: WORDPLAY_TRANSFORM]:** CHEAP, EARP, LUMP, WIKI

### Top Candidate Partitions:
1. **Partition Score: 0.4635**
   - Group 1: **0.5315** | CHEAP, CRACK, POP, BLOW                                           | INCORRECT (Max overlap: 3/4 with RUPTURE)
   - Group 2: **0.4787** | RED, PARE, ROYAL, PEAR                                            | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
   - Group 3: **0.4576** | TWIN, SPLIT, LUMP, PAIR                                           | INCORRECT (Max overlap: 1/4 with MLB PLAYER) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 25.6%)]
   - Group 4: **0.4452** | EARP, WIKI, PÈRE, PADRE                                           | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
2. **Partition Score: 0.4624**
   - Group 1: **0.5100** | CHEAP, SPLIT, CRACK, BLOW                                         | INCORRECT (Max overlap: 3/4 with RUPTURE)
   - Group 2: **0.4787** | RED, PARE, ROYAL, PEAR                                            | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
   - Group 3: **0.4646** | TWIN, LUMP, POP, PAIR                                             | INCORRECT (Max overlap: 1/4 with MLB PLAYER)
   - Group 4: **0.4452** | EARP, WIKI, PÈRE, PADRE                                           | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
3. **Partition Score: 0.4617**
   - Group 1: **0.5232** | CHEAP, SPLIT, CRACK, POP                                          | INCORRECT (Max overlap: 3/4 with RUPTURE)
   - Group 2: **0.4787** | RED, PARE, ROYAL, PEAR                                            | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
   - Group 3: **0.4531** | TWIN, LUMP, BLOW, PAIR                                            | INCORRECT (Max overlap: 1/4 with MLB PLAYER)
   - Group 4: **0.4452** | EARP, WIKI, PÈRE, PADRE                                           | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
4. **Partition Score: 0.4610**
   - Group 1: **0.6607** | SPLIT, CRACK, POP, BLOW                                           | CORRECT GROUP (RUPTURE, Level 1)
   - Group 2: **0.5086** | EARP, WIKI, PÈRE, PEAR                                            | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
   - Group 3: **0.4237** | PARE, TWIN, PADRE, PAIR                                           | INCORRECT (Max overlap: 2/4 with HOMOPHONES)
   - Group 4: **0.4133** | RED, CHEAP, ROYAL, LUMP                                           | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
5. **Partition Score: 0.4595**
   - Group 1: **0.6607** | SPLIT, CRACK, POP, BLOW                                           | CORRECT GROUP (RUPTURE, Level 1)
   - Group 2: **0.5525** | EARP, WIKI, PARE, PEAR                                            | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
   - Group 3: **0.4026** | CHEAP, TWIN, LUMP, PAIR                                           | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS) | [Pred Type: SYNONYM_OR_NEAR (46.9%, no-rel 24.8%)]
   - Group 4: **0.4022** | RED, PÈRE, PADRE, ROYAL                                           | INCORRECT (Max overlap: 3/4 with MLB PLAYER)

### Top Candidate Groups:
   - Group 1: **0.5315** | CHEAP, CRACK, POP, BLOW                                           | INCORRECT (Max overlap: 3/4 with RUPTURE)
   - Group 2: **0.4787** | RED, PARE, ROYAL, PEAR                                            | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
   - Group 3: **0.4576** | TWIN, SPLIT, LUMP, PAIR                                           | INCORRECT (Max overlap: 1/4 with MLB PLAYER) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 25.6%)]
   - Group 4: **0.4452** | EARP, WIKI, PÈRE, PADRE                                           | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
   - Group 5: **0.5100** | CHEAP, SPLIT, CRACK, BLOW                                         | INCORRECT (Max overlap: 3/4 with RUPTURE)
   - Group 6: **0.4646** | TWIN, LUMP, POP, PAIR                                             | INCORRECT (Max overlap: 1/4 with MLB PLAYER)
   - Group 7: **0.5232** | CHEAP, SPLIT, CRACK, POP                                          | INCORRECT (Max overlap: 3/4 with RUPTURE)
   - Group 8: **0.4531** | TWIN, LUMP, BLOW, PAIR                                            | INCORRECT (Max overlap: 1/4 with MLB PLAYER)
   - Group 9: **0.6607** | SPLIT, CRACK, POP, BLOW                                           | CORRECT GROUP (RUPTURE, Level 1)
   - Group 10: **0.5086** | EARP, WIKI, PÈRE, PEAR                                            | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
   - Group 11: **0.4237** | PARE, TWIN, PADRE, PAIR                                           | INCORRECT (Max overlap: 2/4 with HOMOPHONES)
   - Group 12: **0.4133** | RED, CHEAP, ROYAL, LUMP                                           | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
   - Group 13: **0.5525** | EARP, WIKI, PARE, PEAR                                            | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
   - Group 14: **0.4026** | CHEAP, TWIN, LUMP, PAIR                                           | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS) | [Pred Type: SYNONYM_OR_NEAR (46.9%, no-rel 24.8%)]
   - Group 15: **0.4022** | RED, PÈRE, PADRE, ROYAL                                           | INCORRECT (Max overlap: 3/4 with MLB PLAYER)
   - Group 16: **0.4428** | RED, CHEAP, PARE, ROYAL                                           | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
   - Group 17: **0.4022** | TWIN, PADRE, LUMP, PAIR                                           | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
   - Group 18: **0.5145** | EARP, WIKI, PARE, PÈRE                                            | INCORRECT (Max overlap: 2/4 with FRUIT ANAGRAMS)
   - Group 19: **0.4366** | RED, CHEAP, ROYAL, PEAR                                           | INCORRECT (Max overlap: 2/4 with MLB PLAYER)
   - Group 20: **0.4736** | TWIN, SPLIT, CRACK, PAIR                                          | INCORRECT (Max overlap: 2/4 with RUPTURE)

---

## Puzzle 87 (ID: 86)
**Words on Board:** PIE, PERK, GRAPH, STUFFING, MAP, I RAN, ICING, BONUS, MONTERO, DIAGRAM, SATISFACTION, TURKEY, EXTRA, ISTANBUL, GRAVY, CHART

### Ground Truth Categories:
* **Level 0 (INFORMATION DISPLAYS) [Type: SEMANTIC_SET]:** CHART, DIAGRAM, GRAPH, MAP
* **Level 1 (ADDITIONAL BENEFIT) [Type: SYNONYM_OR_NEAR]:** BONUS, EXTRA, ICING, PERK
* **Level 2 (THANKSGIVING FOOD) [Type: SEMANTIC_SET]:** GRAVY, PIE, STUFFING, TURKEY
* **Level 3 (SONG TITLES WITH PARENTHESES) [Type: WORD_FORM]:** I RAN, ISTANBUL, MONTERO, SATISFACTION

### Top Candidate Partitions:
1. **Partition Score: 0.5192**
   - Group 1: **0.7546** | GRAPH, MAP, DIAGRAM, CHART                                        | CORRECT GROUP (INFORMATION DISPLAYS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 31.2%)]
   - Group 2: **0.6166** | PERK, BONUS, SATISFACTION, EXTRA                                  | INCORRECT (Max overlap: 3/4 with ADDITIONAL BENEFIT) | [Pred Type: SYNONYM_OR_NEAR (67.6%, no-rel 23.0%)]
   - Group 3: **0.4738** | STUFFING, ICING, TURKEY, GRAVY                                    | INCORRECT (Max overlap: 3/4 with THANKSGIVING FOOD)
   - Group 4: **0.4486** | PIE, I RAN, MONTERO, ISTANBUL                                     | INCORRECT (Max overlap: 3/4 with SONG TITLES WITH PARENTHESES)
2. **Partition Score: 0.5023**
   - Group 1: **0.7546** | GRAPH, MAP, DIAGRAM, CHART                                        | CORRECT GROUP (INFORMATION DISPLAYS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 31.2%)]
   - Group 2: **0.6166** | PERK, BONUS, SATISFACTION, EXTRA                                  | INCORRECT (Max overlap: 3/4 with ADDITIONAL BENEFIT) | [Pred Type: SYNONYM_OR_NEAR (67.6%, no-rel 23.0%)]
   - Group 3: **0.4701** | PIE, I RAN, MONTERO, GRAVY                                        | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 4: **0.4169** | STUFFING, ICING, TURKEY, ISTANBUL                                 | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
3. **Partition Score: 0.4955**
   - Group 1: **0.7546** | GRAPH, MAP, DIAGRAM, CHART                                        | CORRECT GROUP (INFORMATION DISPLAYS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 31.2%)]
   - Group 2: **0.6166** | PERK, BONUS, SATISFACTION, EXTRA                                  | INCORRECT (Max overlap: 3/4 with ADDITIONAL BENEFIT) | [Pred Type: SYNONYM_OR_NEAR (67.6%, no-rel 23.0%)]
   - Group 3: **0.4484** | PIE, I RAN, ICING, MONTERO                                        | INCORRECT (Max overlap: 2/4 with SONG TITLES WITH PARENTHESES)
   - Group 4: **0.4116** | STUFFING, TURKEY, ISTANBUL, GRAVY                                 | INCORRECT (Max overlap: 3/4 with THANKSGIVING FOOD)
4. **Partition Score: 0.4935**
   - Group 1: **0.7546** | GRAPH, MAP, DIAGRAM, CHART                                        | CORRECT GROUP (INFORMATION DISPLAYS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 31.2%)]
   - Group 2: **0.6166** | PERK, BONUS, SATISFACTION, EXTRA                                  | INCORRECT (Max overlap: 3/4 with ADDITIONAL BENEFIT) | [Pred Type: SYNONYM_OR_NEAR (67.6%, no-rel 23.0%)]
   - Group 3: **0.4881** | PIE, I RAN, ICING, GRAVY                                          | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 4: **0.3932** | STUFFING, MONTERO, TURKEY, ISTANBUL                               | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
5. **Partition Score: 0.4917**
   - Group 1: **0.7546** | GRAPH, MAP, DIAGRAM, CHART                                        | CORRECT GROUP (INFORMATION DISPLAYS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 31.2%)]
   - Group 2: **0.6166** | PERK, BONUS, SATISFACTION, EXTRA                                  | INCORRECT (Max overlap: 3/4 with ADDITIONAL BENEFIT) | [Pred Type: SYNONYM_OR_NEAR (67.6%, no-rel 23.0%)]
   - Group 3: **0.4476** | PIE, ICING, MONTERO, GRAVY                                        | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 4: **0.4044** | STUFFING, I RAN, TURKEY, ISTANBUL                                 | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)

### Top Candidate Groups:
   - Group 1: **0.7546** | GRAPH, MAP, DIAGRAM, CHART                                        | CORRECT GROUP (INFORMATION DISPLAYS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 31.2%)]
   - Group 2: **0.6166** | PERK, BONUS, SATISFACTION, EXTRA                                  | INCORRECT (Max overlap: 3/4 with ADDITIONAL BENEFIT) | [Pred Type: SYNONYM_OR_NEAR (67.6%, no-rel 23.0%)]
   - Group 3: **0.4738** | STUFFING, ICING, TURKEY, GRAVY                                    | INCORRECT (Max overlap: 3/4 with THANKSGIVING FOOD)
   - Group 4: **0.4486** | PIE, I RAN, MONTERO, ISTANBUL                                     | INCORRECT (Max overlap: 3/4 with SONG TITLES WITH PARENTHESES)
   - Group 5: **0.4701** | PIE, I RAN, MONTERO, GRAVY                                        | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 6: **0.4169** | STUFFING, ICING, TURKEY, ISTANBUL                                 | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 7: **0.4484** | PIE, I RAN, ICING, MONTERO                                        | INCORRECT (Max overlap: 2/4 with SONG TITLES WITH PARENTHESES)
   - Group 8: **0.4116** | STUFFING, TURKEY, ISTANBUL, GRAVY                                 | INCORRECT (Max overlap: 3/4 with THANKSGIVING FOOD)
   - Group 9: **0.4881** | PIE, I RAN, ICING, GRAVY                                          | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 10: **0.3932** | STUFFING, MONTERO, TURKEY, ISTANBUL                               | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 11: **0.4476** | PIE, ICING, MONTERO, GRAVY                                        | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 12: **0.4044** | STUFFING, I RAN, TURKEY, ISTANBUL                                 | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 13: **0.4624** | PIE, MONTERO, TURKEY, ISTANBUL                                    | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD) | [Pred Type: NAMED_ENTITY_SET (45.7%, no-rel 19.3%)]
   - Group 14: **0.3794** | STUFFING, I RAN, ICING, GRAVY                                     | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 15: **0.5046** | PIE, I RAN, TURKEY, GRAVY                                         | INCORRECT (Max overlap: 3/4 with THANKSGIVING FOOD)
   - Group 16: **0.3520** | STUFFING, ICING, MONTERO, ISTANBUL                                | INCORRECT (Max overlap: 2/4 with SONG TITLES WITH PARENTHESES)
   - Group 17: **0.4683** | PIE, I RAN, TURKEY, ISTANBUL                                      | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 18: **0.3651** | STUFFING, ICING, MONTERO, GRAVY                                   | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 19: **0.4527** | PIE, I RAN, MONTERO, TURKEY                                       | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)
   - Group 20: **0.3701** | STUFFING, ICING, ISTANBUL, GRAVY                                  | INCORRECT (Max overlap: 2/4 with THANKSGIVING FOOD)

---

## Puzzle 88 (ID: 411)
**Words on Board:** CON, STRIKE, RIGHT, LIAR, BACK, LOOT, LEFT, SYMBOL, SUPPORT, MINUS, BASE, DING, UP, CHAMPION, DOWN, ENDORSE

### Ground Truth Categories:
* **Level 0 (BASIC DIRECTIONS) [Type: SEMANTIC_SET]:** DOWN, LEFT, RIGHT, UP
* **Level 1 (ADVOCATE FOR) [Type: SYNONYM_OR_NEAR]:** BACK, CHAMPION, ENDORSE, SUPPORT
* **Level 2 (DRAWBACK) [Type: SYNONYM_OR_NEAR]:** CON, DING, MINUS, STRIKE
* **Level 3 (INSTRUMENT HOMOPHONES) [Type: SOUND_OR_SPELLING]:** BASE, LIAR, LOOT, SYMBOL

### Top Candidate Partitions:
1. **Partition Score: 0.4963**
   - Group 1: **0.6455** | BACK, SUPPORT, BASE, ENDORSE                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 32.0%)]
   - Group 2: **0.5072** | RIGHT, LOOT, LEFT, CHAMPION                                       | INCORRECT (Max overlap: 2/4 with BASIC DIRECTIONS)
   - Group 3: **0.4778** | STRIKE, DING, UP, DOWN                                            | INCORRECT (Max overlap: 2/4 with DRAWBACK) | [Pred Type: SEMANTIC_SET (51.5%, no-rel 36.3%)]
   - Group 4: **0.4662** | CON, LIAR, SYMBOL, MINUS                                          | INCORRECT (Max overlap: 2/4 with DRAWBACK)
2. **Partition Score: 0.4941**
   - Group 1: **0.6455** | BACK, SUPPORT, BASE, ENDORSE                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 32.0%)]
   - Group 2: **0.5148** | CON, DING, UP, DOWN                                               | INCORRECT (Max overlap: 2/4 with DRAWBACK)
   - Group 3: **0.4728** | STRIKE, RIGHT, LOOT, LEFT                                         | INCORRECT (Max overlap: 2/4 with BASIC DIRECTIONS)
   - Group 4: **0.4610** | LIAR, SYMBOL, MINUS, CHAMPION                                     | INCORRECT (Max overlap: 2/4 with INSTRUMENT HOMOPHONES)
3. **Partition Score: 0.4923**
   - Group 1: **0.6455** | BACK, SUPPORT, BASE, ENDORSE                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 32.0%)]
   - Group 2: **0.5937** | STRIKE, RIGHT, LEFT, DOWN                                         | INCORRECT (Max overlap: 3/4 with BASIC DIRECTIONS)
   - Group 3: **0.4610** | LIAR, SYMBOL, MINUS, CHAMPION                                     | INCORRECT (Max overlap: 2/4 with INSTRUMENT HOMOPHONES)
   - Group 4: **0.4331** | CON, LOOT, DING, UP                                               | INCORRECT (Max overlap: 2/4 with DRAWBACK)
4. **Partition Score: 0.4881**
   - Group 1: **0.6455** | BACK, SUPPORT, BASE, ENDORSE                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 32.0%)]
   - Group 2: **0.5072** | RIGHT, LOOT, LEFT, CHAMPION                                       | INCORRECT (Max overlap: 2/4 with BASIC DIRECTIONS)
   - Group 3: **0.4635** | CON, STRIKE, UP, DOWN                                             | INCORRECT (Max overlap: 2/4 with DRAWBACK)
   - Group 4: **0.4556** | LIAR, SYMBOL, MINUS, DING                                         | INCORRECT (Max overlap: 2/4 with INSTRUMENT HOMOPHONES)
5. **Partition Score: 0.4862**
   - Group 1: **0.6455** | BACK, SUPPORT, BASE, ENDORSE                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 32.0%)]
   - Group 2: **0.5937** | STRIKE, RIGHT, LEFT, DOWN                                         | INCORRECT (Max overlap: 3/4 with BASIC DIRECTIONS)
   - Group 3: **0.4405** | LIAR, LOOT, SYMBOL, MINUS                                         | INCORRECT (Max overlap: 3/4 with INSTRUMENT HOMOPHONES)
   - Group 4: **0.4287** | CON, DING, UP, CHAMPION                                           | INCORRECT (Max overlap: 2/4 with DRAWBACK)

### Top Candidate Groups:
   - Group 1: **0.6455** | BACK, SUPPORT, BASE, ENDORSE                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 32.0%)]
   - Group 2: **0.5072** | RIGHT, LOOT, LEFT, CHAMPION                                       | INCORRECT (Max overlap: 2/4 with BASIC DIRECTIONS)
   - Group 3: **0.4778** | STRIKE, DING, UP, DOWN                                            | INCORRECT (Max overlap: 2/4 with DRAWBACK) | [Pred Type: SEMANTIC_SET (51.5%, no-rel 36.3%)]
   - Group 4: **0.4662** | CON, LIAR, SYMBOL, MINUS                                          | INCORRECT (Max overlap: 2/4 with DRAWBACK)
   - Group 5: **0.5148** | CON, DING, UP, DOWN                                               | INCORRECT (Max overlap: 2/4 with DRAWBACK)
   - Group 6: **0.4728** | STRIKE, RIGHT, LOOT, LEFT                                         | INCORRECT (Max overlap: 2/4 with BASIC DIRECTIONS)
   - Group 7: **0.4610** | LIAR, SYMBOL, MINUS, CHAMPION                                     | INCORRECT (Max overlap: 2/4 with INSTRUMENT HOMOPHONES)
   - Group 8: **0.5937** | STRIKE, RIGHT, LEFT, DOWN                                         | INCORRECT (Max overlap: 3/4 with BASIC DIRECTIONS)
   - Group 9: **0.4331** | CON, LOOT, DING, UP                                               | INCORRECT (Max overlap: 2/4 with DRAWBACK)
   - Group 10: **0.4635** | CON, STRIKE, UP, DOWN                                             | INCORRECT (Max overlap: 2/4 with DRAWBACK)
   - Group 11: **0.4556** | LIAR, SYMBOL, MINUS, DING                                         | INCORRECT (Max overlap: 2/4 with INSTRUMENT HOMOPHONES)
   - Group 12: **0.4405** | LIAR, LOOT, SYMBOL, MINUS                                         | INCORRECT (Max overlap: 3/4 with INSTRUMENT HOMOPHONES)
   - Group 13: **0.4287** | CON, DING, UP, CHAMPION                                           | INCORRECT (Max overlap: 2/4 with DRAWBACK)
   - Group 14: **0.6506** | BACK, SUPPORT, CHAMPION, ENDORSE                                  | CORRECT GROUP (ADVOCATE FOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (69.7%, no-rel 19.9%)]
   - Group 15: **0.4825** | CON, BASE, UP, DOWN                                               | INCORRECT (Max overlap: 2/4 with BASIC DIRECTIONS)
   - Group 16: **0.5588** | RIGHT, BACK, LOOT, LEFT                                           | INCORRECT (Max overlap: 2/4 with BASIC DIRECTIONS)
   - Group 17: **0.5028** | SUPPORT, BASE, CHAMPION, ENDORSE                                  | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 26.5%)]
   - Group 18: **0.5786** | RIGHT, BACK, LEFT, UP                                             | INCORRECT (Max overlap: 3/4 with BASIC DIRECTIONS)
   - Group 19: **0.4648** | STRIKE, LOOT, DING, DOWN                                          | INCORRECT (Max overlap: 2/4 with DRAWBACK)
   - Group 20: **0.6034** | STRIKE, RIGHT, BACK, LEFT                                         | INCORRECT (Max overlap: 2/4 with BASIC DIRECTIONS)

---

## Puzzle 89 (ID: 468)
**Words on Board:** COLLECTIBLE, WELL DONE, BLOODY, IMPRESSIVE, PSYCHIC, EXCLUSIVE, AWFUL, RARE, PROPS, REAL, ORACLE, MYSTIC, NICE, MEDIUM, WAY, LIMITED

### Ground Truth Categories:
* **Level 0 (CLAIRVOYANT) [Type: SYNONYM_OR_NEAR]:** MEDIUM, MYSTIC, ORACLE, PSYCHIC
* **Level 1 (SPECIAL EDITION ADJECTIVES) [Type: SYNONYM_OR_NEAR]:** COLLECTIBLE, EXCLUSIVE, LIMITED, RARE
* **Level 2 (“GREAT JOB!”) [Type: SYNONYM_OR_NEAR]:** IMPRESSIVE, NICE, PROPS, WELL DONE
* **Level 3 (EXTREMELY) [Type: SYNONYM_OR_NEAR]:** AWFUL, BLOODY, REAL, WAY

### Top Candidate Partitions:
1. **Partition Score: 0.5392**
   - Group 1: **0.6119** | IMPRESSIVE, EXCLUSIVE, AWFUL, NICE                                | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 2: **0.5448** | WELL DONE, RARE, MEDIUM, LIMITED                                  | INCORRECT (Max overlap: 2/4 with SPECIAL EDITION ADJECTIVES)
   - Group 3: **0.5445** | COLLECTIBLE, PSYCHIC, ORACLE, MYSTIC                              | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 4: **0.5194** | BLOODY, PROPS, REAL, WAY                                          | INCORRECT (Max overlap: 3/4 with EXTREMELY)
2. **Partition Score: 0.5280**
   - Group 1: **0.5806** | EXCLUSIVE, AWFUL, RARE, NICE                                      | INCORRECT (Max overlap: 2/4 with SPECIAL EDITION ADJECTIVES)
   - Group 2: **0.5445** | COLLECTIBLE, PSYCHIC, ORACLE, MYSTIC                              | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 3: **0.5194** | BLOODY, PROPS, REAL, WAY                                          | INCORRECT (Max overlap: 3/4 with EXTREMELY)
   - Group 4: **0.5135** | WELL DONE, IMPRESSIVE, MEDIUM, LIMITED                            | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
3. **Partition Score: 0.5235**
   - Group 1: **0.6119** | IMPRESSIVE, EXCLUSIVE, AWFUL, NICE                                | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 2: **0.5445** | COLLECTIBLE, PSYCHIC, ORACLE, MYSTIC                              | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 3: **0.5142** | RARE, PROPS, REAL, WAY                                            | INCORRECT (Max overlap: 2/4 with EXTREMELY)
   - Group 4: **0.4999** | WELL DONE, BLOODY, MEDIUM, LIMITED                                | INCORRECT (Max overlap: 1/4 with “GREAT JOB!”) | [Pred Type: SYNONYM_OR_NEAR (45.0%, no-rel 25.0%)]
4. **Partition Score: 0.5221**
   - Group 1: **0.6119** | IMPRESSIVE, EXCLUSIVE, AWFUL, NICE                                | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 2: **0.5445** | COLLECTIBLE, PSYCHIC, ORACLE, MYSTIC                              | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 3: **0.5197** | BLOODY, RARE, REAL, WAY                                           | INCORRECT (Max overlap: 3/4 with EXTREMELY)
   - Group 4: **0.4950** | WELL DONE, PROPS, MEDIUM, LIMITED                                 | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
5. **Partition Score: 0.5188**
   - Group 1: **0.5445** | COLLECTIBLE, PSYCHIC, ORACLE, MYSTIC                              | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 2: **0.5261** | WELL DONE, IMPRESSIVE, RARE, MEDIUM                               | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 3: **0.5194** | BLOODY, PROPS, REAL, WAY                                          | INCORRECT (Max overlap: 3/4 with EXTREMELY)
   - Group 4: **0.5103** | EXCLUSIVE, AWFUL, NICE, LIMITED                                   | INCORRECT (Max overlap: 2/4 with SPECIAL EDITION ADJECTIVES)

### Top Candidate Groups:
   - Group 1: **0.6119** | IMPRESSIVE, EXCLUSIVE, AWFUL, NICE                                | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 2: **0.5448** | WELL DONE, RARE, MEDIUM, LIMITED                                  | INCORRECT (Max overlap: 2/4 with SPECIAL EDITION ADJECTIVES)
   - Group 3: **0.5445** | COLLECTIBLE, PSYCHIC, ORACLE, MYSTIC                              | INCORRECT (Max overlap: 3/4 with CLAIRVOYANT)
   - Group 4: **0.5194** | BLOODY, PROPS, REAL, WAY                                          | INCORRECT (Max overlap: 3/4 with EXTREMELY)
   - Group 5: **0.5806** | EXCLUSIVE, AWFUL, RARE, NICE                                      | INCORRECT (Max overlap: 2/4 with SPECIAL EDITION ADJECTIVES)
   - Group 6: **0.5135** | WELL DONE, IMPRESSIVE, MEDIUM, LIMITED                            | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 7: **0.5142** | RARE, PROPS, REAL, WAY                                            | INCORRECT (Max overlap: 2/4 with EXTREMELY)
   - Group 8: **0.4999** | WELL DONE, BLOODY, MEDIUM, LIMITED                                | INCORRECT (Max overlap: 1/4 with “GREAT JOB!”) | [Pred Type: SYNONYM_OR_NEAR (45.0%, no-rel 25.0%)]
   - Group 9: **0.5197** | BLOODY, RARE, REAL, WAY                                           | INCORRECT (Max overlap: 3/4 with EXTREMELY)
   - Group 10: **0.4950** | WELL DONE, PROPS, MEDIUM, LIMITED                                 | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 11: **0.5261** | WELL DONE, IMPRESSIVE, RARE, MEDIUM                               | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 12: **0.5103** | EXCLUSIVE, AWFUL, NICE, LIMITED                                   | INCORRECT (Max overlap: 2/4 with SPECIAL EDITION ADJECTIVES)
   - Group 13: **0.5672** | BLOODY, IMPRESSIVE, EXCLUSIVE, AWFUL                              | INCORRECT (Max overlap: 2/4 with EXTREMELY)
   - Group 14: **0.5064** | RARE, REAL, NICE, WAY                                             | INCORRECT (Max overlap: 2/4 with EXTREMELY)
   - Group 15: **0.5863** | EXCLUSIVE, AWFUL, REAL, NICE                                      | INCORRECT (Max overlap: 2/4 with EXTREMELY)
   - Group 16: **0.4816** | BLOODY, PROPS, WAY, LIMITED                                       | INCORRECT (Max overlap: 2/4 with EXTREMELY)
   - Group 17: **0.4987** | WELL DONE, RARE, PROPS, MEDIUM                                    | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 18: **0.4852** | BLOODY, REAL, WAY, LIMITED                                        | INCORRECT (Max overlap: 3/4 with EXTREMELY)
   - Group 19: **0.4772** | PROPS, REAL, NICE, WAY                                            | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)
   - Group 20: **0.5914** | IMPRESSIVE, EXCLUSIVE, RARE, NICE                                 | INCORRECT (Max overlap: 2/4 with “GREAT JOB!”)

---

## Puzzle 90 (ID: 232)
**Words on Board:** ITEM, DRAGON, THING, PASSION, PITCH, ALL, LOVE, PAIR, PROMOTE, DEUCE, COUPLE, BREAD, JACK, PUSH, PLUG, AD

### Ground Truth Categories:
* **Level 0 (DO SOME MARKETING FOR) [Type: SYNONYM_OR_NEAR]:** PITCH, PLUG, PROMOTE, PUSH
* **Level 1 (ROMANTIC TWOSOME) [Type: SYNONYM_OR_NEAR]:** COUPLE, ITEM, PAIR, THING
* **Level 2 (TENNIS SCORING TERMS) [Type: SEMANTIC_SET]:** AD, ALL, DEUCE, LOVE
* **Level 3 (WORDS WITH “FRUIT”) [Type: FILL_IN_THE_BLANK]:** BREAD, DRAGON, JACK, PASSION

### Top Candidate Partitions:
1. **Partition Score: 0.4833**
   - Group 1: **0.6191** | ITEM, THING, PAIR, COUPLE                                         | CORRECT GROUP (ROMANTIC TWOSOME, Level 1) | [Pred Type: SYNONYM_OR_NEAR (64.9%, no-rel 28.3%)]
   - Group 2: **0.4861** | PASSION, LOVE, PROMOTE, PUSH                                      | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 29.2%)]
   - Group 3: **0.4702** | DRAGON, DEUCE, BREAD, JACK                                        | INCORRECT (Max overlap: 3/4 with WORDS WITH “FRUIT”)
   - Group 4: **0.4573** | PITCH, ALL, PLUG, AD                                              | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR)
2. **Partition Score: 0.4724**
   - Group 1: **0.4794** | PITCH, ALL, PUSH, AD                                              | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR)
   - Group 2: **0.4754** | THING, PASSION, LOVE, PROMOTE                                     | INCORRECT (Max overlap: 1/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (65.4%, no-rel 25.6%)]
   - Group 3: **0.4715** | ITEM, PAIR, COUPLE, PLUG                                          | INCORRECT (Max overlap: 3/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (67.3%, no-rel 24.4%)]
   - Group 4: **0.4702** | DRAGON, DEUCE, BREAD, JACK                                        | INCORRECT (Max overlap: 3/4 with WORDS WITH “FRUIT”)
3. **Partition Score: 0.4695**
   - Group 1: **0.6191** | ITEM, THING, PAIR, COUPLE                                         | CORRECT GROUP (ROMANTIC TWOSOME, Level 1) | [Pred Type: SYNONYM_OR_NEAR (64.9%, no-rel 28.3%)]
   - Group 2: **0.4861** | PASSION, LOVE, PROMOTE, PUSH                                      | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 29.2%)]
   - Group 3: **0.4647** | DRAGON, BREAD, JACK, PLUG                                         | INCORRECT (Max overlap: 3/4 with WORDS WITH “FRUIT”)
   - Group 4: **0.4323** | PITCH, ALL, DEUCE, AD                                             | INCORRECT (Max overlap: 3/4 with TENNIS SCORING TERMS)
4. **Partition Score: 0.4687**
   - Group 1: **0.5042** | ITEM, THING, PASSION, LOVE                                        | INCORRECT (Max overlap: 2/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (63.2%, no-rel 28.5%)]
   - Group 2: **0.4773** | PAIR, PROMOTE, COUPLE, PUSH                                       | INCORRECT (Max overlap: 2/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (61.4%, no-rel 30.5%)]
   - Group 3: **0.4702** | DRAGON, DEUCE, BREAD, JACK                                        | INCORRECT (Max overlap: 3/4 with WORDS WITH “FRUIT”)
   - Group 4: **0.4573** | PITCH, ALL, PLUG, AD                                              | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR)
5. **Partition Score: 0.4684**
   - Group 1: **0.6191** | ITEM, THING, PAIR, COUPLE                                         | CORRECT GROUP (ROMANTIC TWOSOME, Level 1) | [Pred Type: SYNONYM_OR_NEAR (64.9%, no-rel 28.3%)]
   - Group 2: **0.4861** | PASSION, LOVE, PROMOTE, PUSH                                      | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 29.2%)]
   - Group 3: **0.4615** | PITCH, BREAD, JACK, PLUG                                          | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR)
   - Group 4: **0.4314** | DRAGON, ALL, DEUCE, AD                                            | INCORRECT (Max overlap: 3/4 with TENNIS SCORING TERMS)

### Top Candidate Groups:
   - Group 1: **0.6191** | ITEM, THING, PAIR, COUPLE                                         | CORRECT GROUP (ROMANTIC TWOSOME, Level 1) | [Pred Type: SYNONYM_OR_NEAR (64.9%, no-rel 28.3%)]
   - Group 2: **0.4861** | PASSION, LOVE, PROMOTE, PUSH                                      | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 29.2%)]
   - Group 3: **0.4702** | DRAGON, DEUCE, BREAD, JACK                                        | INCORRECT (Max overlap: 3/4 with WORDS WITH “FRUIT”)
   - Group 4: **0.4573** | PITCH, ALL, PLUG, AD                                              | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR)
   - Group 5: **0.4794** | PITCH, ALL, PUSH, AD                                              | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR)
   - Group 6: **0.4754** | THING, PASSION, LOVE, PROMOTE                                     | INCORRECT (Max overlap: 1/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (65.4%, no-rel 25.6%)]
   - Group 7: **0.4715** | ITEM, PAIR, COUPLE, PLUG                                          | INCORRECT (Max overlap: 3/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (67.3%, no-rel 24.4%)]
   - Group 8: **0.4647** | DRAGON, BREAD, JACK, PLUG                                         | INCORRECT (Max overlap: 3/4 with WORDS WITH “FRUIT”)
   - Group 9: **0.4323** | PITCH, ALL, DEUCE, AD                                             | INCORRECT (Max overlap: 3/4 with TENNIS SCORING TERMS)
   - Group 10: **0.5042** | ITEM, THING, PASSION, LOVE                                        | INCORRECT (Max overlap: 2/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (63.2%, no-rel 28.5%)]
   - Group 11: **0.4773** | PAIR, PROMOTE, COUPLE, PUSH                                       | INCORRECT (Max overlap: 2/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (61.4%, no-rel 30.5%)]
   - Group 12: **0.4615** | PITCH, BREAD, JACK, PLUG                                          | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR)
   - Group 13: **0.4314** | DRAGON, ALL, DEUCE, AD                                            | INCORRECT (Max overlap: 3/4 with TENNIS SCORING TERMS)
   - Group 14: **0.4463** | DEUCE, BREAD, JACK, PLUG                                          | INCORRECT (Max overlap: 2/4 with WORDS WITH “FRUIT”)
   - Group 15: **0.4341** | DRAGON, PITCH, ALL, AD                                            | INCORRECT (Max overlap: 2/4 with TENNIS SCORING TERMS)
   - Group 16: **0.4894** | PITCH, BREAD, PLUG, AD                                            | INCORRECT (Max overlap: 2/4 with DO SOME MARKETING FOR)
   - Group 17: **0.4167** | DRAGON, ALL, DEUCE, JACK                                          | INCORRECT (Max overlap: 2/4 with WORDS WITH “FRUIT”)
   - Group 18: **0.4767** | ITEM, PAIR, COUPLE, PUSH                                          | INCORRECT (Max overlap: 3/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (64.0%, no-rel 29.0%)]
   - Group 19: **0.4853** | ITEM, THING, PROMOTE, PUSH                                        | INCORRECT (Max overlap: 2/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 30.2%)]
   - Group 20: **0.4695** | PASSION, LOVE, PAIR, COUPLE                                       | INCORRECT (Max overlap: 2/4 with ROMANTIC TWOSOME) | [Pred Type: SYNONYM_OR_NEAR (65.8%, no-rel 26.6%)]

---

## Puzzle 91 (ID: 946)
**Words on Board:** CANE, BOWTIE, RIBBON, PARCH, WHEEL, BOW, SHOULDER, GIFT WRAP, PRESS, RANKLE, SHOVE, ELBOW, OTOE, MONEYBAG, TOP HAT, CARD

### Ground Truth Categories:
* **Level 0 (PRESENT GO-WITHS) [Type: SEMANTIC_SET]:** BOW, CARD, GIFT WRAP, RIBBON
* **Level 1 (JOSTLE) [Type: SYNONYM_OR_NEAR]:** ELBOW, PRESS, SHOULDER, SHOVE
* **Level 2 (ACCESSORIES FOR MR. MONOPOLY) [Type: NAMED_ENTITY_SET]:** BOWTIE, CANE, MONEYBAG, TOP HAT
* **Level 3 (PARTS OF THE FOOT PLUS STARTING LETTER) [Type: WORDPLAY_TRANSFORM]:** OTOE, PARCH, RANKLE, WHEEL

### Top Candidate Partitions:
1. **Partition Score: 0.4834**
   - Group 1: **0.5540** | SHOULDER, PRESS, ELBOW, CARD                                      | INCORRECT (Max overlap: 3/4 with JOSTLE)
   - Group 2: **0.4830** | PARCH, RANKLE, SHOVE, MONEYBAG                                    | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 3: **0.4751** | BOWTIE, GIFT WRAP, OTOE, TOP HAT                                  | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 4: **0.4711** | CANE, RIBBON, WHEEL, BOW                                          | INCORRECT (Max overlap: 2/4 with PRESENT GO-WITHS)
2. **Partition Score: 0.4807**
   - Group 1: **0.5069** | SHOULDER, PRESS, SHOVE, ELBOW                                     | CORRECT GROUP (JOSTLE, Level 1)
   - Group 2: **0.4967** | BOWTIE, RIBBON, BOW, RANKLE                                       | INCORRECT (Max overlap: 2/4 with PRESENT GO-WITHS)
   - Group 3: **0.4934** | CANE, PARCH, WHEEL, CARD                                          | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 4: **0.4645** | GIFT WRAP, OTOE, MONEYBAG, TOP HAT                                | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
3. **Partition Score: 0.4806**
   - Group 1: **0.5540** | SHOULDER, PRESS, ELBOW, CARD                                      | INCORRECT (Max overlap: 3/4 with JOSTLE)
   - Group 2: **0.4830** | PARCH, RANKLE, SHOVE, MONEYBAG                                    | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 3: **0.4756** | CANE, WHEEL, OTOE, TOP HAT                                        | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 4: **0.4655** | BOWTIE, RIBBON, BOW, GIFT WRAP                                    | INCORRECT (Max overlap: 3/4 with PRESENT GO-WITHS) | [Pred Type: SEMANTIC_SET (46.0%, no-rel 20.8%)]
4. **Partition Score: 0.4797**
   - Group 1: **0.5310** | PARCH, GIFT WRAP, OTOE, TOP HAT                                   | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 2: **0.4913** | CANE, BOWTIE, RIBBON, BOW                                         | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 3: **0.4742** | WHEEL, SHOULDER, ELBOW, CARD                                      | INCORRECT (Max overlap: 2/4 with JOSTLE)
   - Group 4: **0.4662** | PRESS, RANKLE, SHOVE, MONEYBAG                                    | INCORRECT (Max overlap: 2/4 with JOSTLE)
5. **Partition Score: 0.4794**
   - Group 1: **0.5362** | PARCH, PRESS, RANKLE, SHOVE                                       | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 2: **0.4913** | CANE, BOWTIE, RIBBON, BOW                                         | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 3: **0.4742** | WHEEL, SHOULDER, ELBOW, CARD                                      | INCORRECT (Max overlap: 2/4 with JOSTLE)
   - Group 4: **0.4645** | GIFT WRAP, OTOE, MONEYBAG, TOP HAT                                | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)

### Top Candidate Groups:
   - Group 1: **0.5540** | SHOULDER, PRESS, ELBOW, CARD                                      | INCORRECT (Max overlap: 3/4 with JOSTLE)
   - Group 2: **0.4830** | PARCH, RANKLE, SHOVE, MONEYBAG                                    | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 3: **0.4751** | BOWTIE, GIFT WRAP, OTOE, TOP HAT                                  | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 4: **0.4711** | CANE, RIBBON, WHEEL, BOW                                          | INCORRECT (Max overlap: 2/4 with PRESENT GO-WITHS)
   - Group 5: **0.5069** | SHOULDER, PRESS, SHOVE, ELBOW                                     | CORRECT GROUP (JOSTLE, Level 1)
   - Group 6: **0.4967** | BOWTIE, RIBBON, BOW, RANKLE                                       | INCORRECT (Max overlap: 2/4 with PRESENT GO-WITHS)
   - Group 7: **0.4934** | CANE, PARCH, WHEEL, CARD                                          | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 8: **0.4645** | GIFT WRAP, OTOE, MONEYBAG, TOP HAT                                | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 9: **0.4756** | CANE, WHEEL, OTOE, TOP HAT                                        | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 10: **0.4655** | BOWTIE, RIBBON, BOW, GIFT WRAP                                    | INCORRECT (Max overlap: 3/4 with PRESENT GO-WITHS) | [Pred Type: SEMANTIC_SET (46.0%, no-rel 20.8%)]
   - Group 11: **0.5310** | PARCH, GIFT WRAP, OTOE, TOP HAT                                   | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 12: **0.4913** | CANE, BOWTIE, RIBBON, BOW                                         | INCORRECT (Max overlap: 2/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 13: **0.4742** | WHEEL, SHOULDER, ELBOW, CARD                                      | INCORRECT (Max overlap: 2/4 with JOSTLE)
   - Group 14: **0.4662** | PRESS, RANKLE, SHOVE, MONEYBAG                                    | INCORRECT (Max overlap: 2/4 with JOSTLE)
   - Group 15: **0.5362** | PARCH, PRESS, RANKLE, SHOVE                                       | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 16: **0.5512** | CANE, WHEEL, ELBOW, CARD                                          | INCORRECT (Max overlap: 1/4 with ACCESSORIES FOR MR. MONOPOLY)
   - Group 17: **0.4795** | PARCH, OTOE, MONEYBAG, TOP HAT                                    | INCORRECT (Max overlap: 2/4 with PARTS OF THE FOOT PLUS STARTING LETTER)
   - Group 18: **0.4732** | SHOULDER, PRESS, RANKLE, SHOVE                                    | INCORRECT (Max overlap: 3/4 with JOSTLE)
   - Group 19: **0.4476** | BOWTIE, RIBBON, BOW, SHOULDER                                     | INCORRECT (Max overlap: 2/4 with PRESENT GO-WITHS)
   - Group 20: **0.4787** | BOWTIE, RIBBON, PARCH, BOW                                        | INCORRECT (Max overlap: 2/4 with PRESENT GO-WITHS)

---

## Puzzle 92 (ID: 427)
**Words on Board:** ABOUT, MUSSEL, HARE, VESSEL, ON, GOAT, TOWARD, CRAFT, BEST, SHIP, BARGE, NAVAL, LEGEND, I, CONCERNING, CHAMP

### Ground Truth Categories:
* **Level 0 (LARGE BOAT) [Type: SYNONYM_OR_NEAR]:** BARGE, CRAFT, SHIP, VESSEL
* **Level 1 (ALL-TIME GREAT) [Type: SYNONYM_OR_NEAR]:** BEST, CHAMP, GOAT, LEGEND
* **Level 2 (REGARDING) [Type: SYNONYM_OR_NEAR]:** ABOUT, CONCERNING, ON, TOWARD
* **Level 3 (HOMOPHONES OF BODY FEATURES) [Type: SOUND_OR_SPELLING]:** HARE, I, MUSSEL, NAVAL

### Top Candidate Partitions:
1. **Partition Score: 0.4858**
   - Group 1: **0.6730** | VESSEL, CRAFT, SHIP, BARGE                                        | CORRECT GROUP (LARGE BOAT, Level 0)
   - Group 2: **0.5012** | MUSSEL, TOWARD, NAVAL, LEGEND                                     | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES)
   - Group 3: **0.4531** | HARE, GOAT, BEST, I                                               | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES) | [Pred Type: NAMED_ENTITY_SET (50.1%, no-rel 16.2%)]
   - Group 4: **0.4510** | ABOUT, ON, CONCERNING, CHAMP                                      | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (61.9%, no-rel 15.6%)]
2. **Partition Score: 0.4842**
   - Group 1: **0.6730** | VESSEL, CRAFT, SHIP, BARGE                                        | CORRECT GROUP (LARGE BOAT, Level 0)
   - Group 2: **0.4793** | MUSSEL, HARE, TOWARD, NAVAL                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF BODY FEATURES)
   - Group 3: **0.4667** | GOAT, BEST, LEGEND, I                                             | INCORRECT (Max overlap: 3/4 with ALL-TIME GREAT) | [Pred Type: NAMED_ENTITY_SET (49.5%, no-rel 16.3%)]
   - Group 4: **0.4510** | ABOUT, ON, CONCERNING, CHAMP                                      | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (61.9%, no-rel 15.6%)]
3. **Partition Score: 0.4787**
   - Group 1: **0.6730** | VESSEL, CRAFT, SHIP, BARGE                                        | CORRECT GROUP (LARGE BOAT, Level 0)
   - Group 2: **0.4793** | MUSSEL, HARE, TOWARD, NAVAL                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF BODY FEATURES)
   - Group 3: **0.4549** | GOAT, BEST, I, CHAMP                                              | INCORRECT (Max overlap: 3/4 with ALL-TIME GREAT)
   - Group 4: **0.4446** | ABOUT, ON, LEGEND, CONCERNING                                     | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (61.0%, no-rel 12.4%)]
4. **Partition Score: 0.4780**
   - Group 1: **0.6730** | VESSEL, CRAFT, SHIP, BARGE                                        | CORRECT GROUP (LARGE BOAT, Level 0)
   - Group 2: **0.4736** | HARE, GOAT, BEST, LEGEND                                          | INCORRECT (Max overlap: 3/4 with ALL-TIME GREAT) | [Pred Type: NAMED_ENTITY_SET (52.5%, no-rel 14.9%)]
   - Group 3: **0.4510** | ABOUT, ON, CONCERNING, CHAMP                                      | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (61.9%, no-rel 15.6%)]
   - Group 4: **0.4467** | MUSSEL, TOWARD, NAVAL, I                                          | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF BODY FEATURES)
5. **Partition Score: 0.4757**
   - Group 1: **0.6730** | VESSEL, CRAFT, SHIP, BARGE                                        | CORRECT GROUP (LARGE BOAT, Level 0)
   - Group 2: **0.4653** | MUSSEL, TOWARD, NAVAL, CHAMP                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES)
   - Group 3: **0.4531** | HARE, GOAT, BEST, I                                               | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES) | [Pred Type: NAMED_ENTITY_SET (50.1%, no-rel 16.2%)]
   - Group 4: **0.4446** | ABOUT, ON, LEGEND, CONCERNING                                     | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (61.0%, no-rel 12.4%)]

### Top Candidate Groups:
   - Group 1: **0.6730** | VESSEL, CRAFT, SHIP, BARGE                                        | CORRECT GROUP (LARGE BOAT, Level 0)
   - Group 2: **0.5012** | MUSSEL, TOWARD, NAVAL, LEGEND                                     | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES)
   - Group 3: **0.4531** | HARE, GOAT, BEST, I                                               | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES) | [Pred Type: NAMED_ENTITY_SET (50.1%, no-rel 16.2%)]
   - Group 4: **0.4510** | ABOUT, ON, CONCERNING, CHAMP                                      | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (61.9%, no-rel 15.6%)]
   - Group 5: **0.4793** | MUSSEL, HARE, TOWARD, NAVAL                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF BODY FEATURES)
   - Group 6: **0.4667** | GOAT, BEST, LEGEND, I                                             | INCORRECT (Max overlap: 3/4 with ALL-TIME GREAT) | [Pred Type: NAMED_ENTITY_SET (49.5%, no-rel 16.3%)]
   - Group 7: **0.4549** | GOAT, BEST, I, CHAMP                                              | INCORRECT (Max overlap: 3/4 with ALL-TIME GREAT)
   - Group 8: **0.4446** | ABOUT, ON, LEGEND, CONCERNING                                     | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (61.0%, no-rel 12.4%)]
   - Group 9: **0.4736** | HARE, GOAT, BEST, LEGEND                                          | INCORRECT (Max overlap: 3/4 with ALL-TIME GREAT) | [Pred Type: NAMED_ENTITY_SET (52.5%, no-rel 14.9%)]
   - Group 10: **0.4467** | MUSSEL, TOWARD, NAVAL, I                                          | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF BODY FEATURES)
   - Group 11: **0.4653** | MUSSEL, TOWARD, NAVAL, CHAMP                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES)
   - Group 12: **0.4620** | HARE, GOAT, BEST, CHAMP                                           | INCORRECT (Max overlap: 3/4 with ALL-TIME GREAT) | [Pred Type: NAMED_ENTITY_SET (50.4%, no-rel 14.5%)]
   - Group 13: **0.4817** | ABOUT, ON, SHIP, CONCERNING                                       | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 16.1%)]
   - Group 14: **0.4711** | VESSEL, CRAFT, BARGE, CHAMP                                       | INCORRECT (Max overlap: 3/4 with LARGE BOAT)
   - Group 15: **0.5917** | VESSEL, SHIP, BARGE, NAVAL                                        | INCORRECT (Max overlap: 3/4 with LARGE BOAT) | [Pred Type: SEMANTIC_SET (53.1%, no-rel 19.4%)]
   - Group 16: **0.4711** | MUSSEL, HARE, TOWARD, LEGEND                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES)
   - Group 17: **0.4462** | ABOUT, ON, CRAFT, CONCERNING                                      | INCORRECT (Max overlap: 3/4 with REGARDING) | [Pred Type: SYNONYM_OR_NEAR (63.3%, no-rel 18.1%)]
   - Group 18: **0.4924** | VESSEL, CRAFT, BARGE, LEGEND                                      | INCORRECT (Max overlap: 3/4 with LARGE BOAT)
   - Group 19: **0.4719** | MUSSEL, TOWARD, LEGEND, CHAMP                                     | INCORRECT (Max overlap: 2/4 with ALL-TIME GREAT)
   - Group 20: **0.4451** | MUSSEL, GOAT, BEST, I                                             | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODY FEATURES)

---

## Puzzle 93 (ID: 798)
**Words on Board:** HANDY, WELCOME, ASSEMBLY, EXIT, PUSH, OPEN, ENVELOPE, CLOSE, STAMP, PRESS, NEARBY, SPEECH, ACCESSIBLE, NAME, ADDRESS, PETITION

### Ground Truth Categories:
* **Level 0 (CONVENIENTLY LOCATED) [Type: SYNONYM_OR_NEAR]:** ACCESSIBLE, CLOSE, HANDY, NEARBY
* **Level 1 (NEEDS FOR SENDING A LETTER) [Type: SEMANTIC_SET]:** ADDRESS, ENVELOPE, NAME, STAMP
* **Level 2 (WORDS ON A DOOR) [Type: SEMANTIC_SET]:** EXIT, OPEN, PUSH, WELCOME
* **Level 3 (FIRST AMENDMENT FREEDOMS) [Type: SEMANTIC_SET]:** ASSEMBLY, PETITION, PRESS, SPEECH

### Top Candidate Partitions:
1. **Partition Score: 0.4736**
   - Group 1: **0.5285** | HANDY, WELCOME, NEARBY, ACCESSIBLE                                | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 2: **0.5175** | EXIT, PUSH, OPEN, CLOSE                                           | INCORRECT (Max overlap: 3/4 with WORDS ON A DOOR)
   - Group 3: **0.5119** | SPEECH, NAME, ADDRESS, PETITION                                   | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 34.4%)]
   - Group 4: **0.4314** | ASSEMBLY, ENVELOPE, STAMP, PRESS                                  | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS)
2. **Partition Score: 0.4684**
   - Group 1: **0.5119** | SPEECH, NAME, ADDRESS, PETITION                                   | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 34.4%)]
   - Group 2: **0.5089** | PUSH, OPEN, PRESS, ACCESSIBLE                                     | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 37.5%)]
   - Group 3: **0.5082** | HANDY, EXIT, CLOSE, NEARBY                                        | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 24.7%)]
   - Group 4: **0.4295** | WELCOME, ASSEMBLY, ENVELOPE, STAMP                                | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
3. **Partition Score: 0.4680**
   - Group 1: **0.5285** | HANDY, WELCOME, NEARBY, ACCESSIBLE                                | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 2: **0.5175** | EXIT, PUSH, OPEN, CLOSE                                           | INCORRECT (Max overlap: 3/4 with WORDS ON A DOOR)
   - Group 3: **0.4754** | ENVELOPE, SPEECH, NAME, ADDRESS                                   | INCORRECT (Max overlap: 3/4 with NEEDS FOR SENDING A LETTER) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 27.0%)]
   - Group 4: **0.4340** | ASSEMBLY, STAMP, PRESS, PETITION                                  | INCORRECT (Max overlap: 3/4 with FIRST AMENDMENT FREEDOMS)
4. **Partition Score: 0.4670**
   - Group 1: **0.5309** | HANDY, OPEN, NEARBY, ACCESSIBLE                                   | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 28.8%)]
   - Group 2: **0.5119** | SPEECH, NAME, ADDRESS, PETITION                                   | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 34.4%)]
   - Group 3: **0.4863** | EXIT, PUSH, CLOSE, PRESS                                          | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR) | [Pred Type: SYNONYM_OR_NEAR (54.8%, no-rel 31.0%)]
   - Group 4: **0.4295** | WELCOME, ASSEMBLY, ENVELOPE, STAMP                                | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
5. **Partition Score: 0.4649**
   - Group 1: **0.5285** | HANDY, WELCOME, NEARBY, ACCESSIBLE                                | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 2: **0.5119** | SPEECH, NAME, ADDRESS, PETITION                                   | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 34.4%)]
   - Group 3: **0.4847** | EXIT, OPEN, ENVELOPE, CLOSE                                       | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR) | [Pred Type: SEMANTIC_SET (46.1%, no-rel 35.3%)]
   - Group 4: **0.4265** | ASSEMBLY, PUSH, STAMP, PRESS                                      | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 29.5%)]

### Top Candidate Groups:
   - Group 1: **0.5285** | HANDY, WELCOME, NEARBY, ACCESSIBLE                                | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED)
   - Group 2: **0.5175** | EXIT, PUSH, OPEN, CLOSE                                           | INCORRECT (Max overlap: 3/4 with WORDS ON A DOOR)
   - Group 3: **0.5119** | SPEECH, NAME, ADDRESS, PETITION                                   | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 34.4%)]
   - Group 4: **0.4314** | ASSEMBLY, ENVELOPE, STAMP, PRESS                                  | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS)
   - Group 5: **0.5089** | PUSH, OPEN, PRESS, ACCESSIBLE                                     | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 37.5%)]
   - Group 6: **0.5082** | HANDY, EXIT, CLOSE, NEARBY                                        | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 24.7%)]
   - Group 7: **0.4295** | WELCOME, ASSEMBLY, ENVELOPE, STAMP                                | INCORRECT (Max overlap: 2/4 with NEEDS FOR SENDING A LETTER)
   - Group 8: **0.4754** | ENVELOPE, SPEECH, NAME, ADDRESS                                   | INCORRECT (Max overlap: 3/4 with NEEDS FOR SENDING A LETTER) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 27.0%)]
   - Group 9: **0.4340** | ASSEMBLY, STAMP, PRESS, PETITION                                  | INCORRECT (Max overlap: 3/4 with FIRST AMENDMENT FREEDOMS)
   - Group 10: **0.5309** | HANDY, OPEN, NEARBY, ACCESSIBLE                                   | INCORRECT (Max overlap: 3/4 with CONVENIENTLY LOCATED) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 28.8%)]
   - Group 11: **0.4863** | EXIT, PUSH, CLOSE, PRESS                                          | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR) | [Pred Type: SYNONYM_OR_NEAR (54.8%, no-rel 31.0%)]
   - Group 12: **0.4847** | EXIT, OPEN, ENVELOPE, CLOSE                                       | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR) | [Pred Type: SEMANTIC_SET (46.1%, no-rel 35.3%)]
   - Group 13: **0.4265** | ASSEMBLY, PUSH, STAMP, PRESS                                      | INCORRECT (Max overlap: 2/4 with FIRST AMENDMENT FREEDOMS) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 29.5%)]
   - Group 14: **0.5678** | EXIT, OPEN, CLOSE, ACCESSIBLE                                     | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)
   - Group 15: **0.4498** | HANDY, PUSH, PRESS, NEARBY                                        | INCORRECT (Max overlap: 2/4 with CONVENIENTLY LOCATED) | [Pred Type: SYNONYM_OR_NEAR (61.5%, no-rel 28.3%)]
   - Group 16: **0.5144** | PUSH, CLOSE, PRESS, NEARBY                                        | INCORRECT (Max overlap: 2/4 with CONVENIENTLY LOCATED) | [Pred Type: SYNONYM_OR_NEAR (52.8%, no-rel 36.2%)]
   - Group 17: **0.4795** | HANDY, EXIT, OPEN, ACCESSIBLE                                     | INCORRECT (Max overlap: 2/4 with CONVENIENTLY LOCATED) | [Pred Type: SYNONYM_OR_NEAR (53.8%, no-rel 26.5%)]
   - Group 18: **0.4700** | ENVELOPE, NAME, ADDRESS, PETITION                                 | INCORRECT (Max overlap: 3/4 with NEEDS FOR SENDING A LETTER) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 28.7%)]
   - Group 19: **0.4268** | ASSEMBLY, STAMP, PRESS, SPEECH                                    | INCORRECT (Max overlap: 3/4 with FIRST AMENDMENT FREEDOMS)
   - Group 20: **0.5808** | EXIT, OPEN, CLOSE, NEARBY                                         | INCORRECT (Max overlap: 2/4 with WORDS ON A DOOR)

---

## Puzzle 94 (ID: 324)
**Words on Board:** EXAMINE, RANCH, ANCESTRY, RECEIPT, MARINARA, INVOICE, AIOLI, MERCHANDISE, PROBE, BILL, BARBECUE, QUESTION, CATTLE, BROTH, STATEMENT, GRILL

### Ground Truth Categories:
* **Level 0 (DIPPING SAUCES) [Type: SEMANTIC_SET]:** AIOLI, BARBECUE, MARINARA, RANCH
* **Level 1 (INTERROGATE) [Type: SYNONYM_OR_NEAR]:** EXAMINE, GRILL, PROBE, QUESTION
* **Level 2 (TRANSACTION RECORD) [Type: SYNONYM_OR_NEAR]:** BILL, INVOICE, RECEIPT, STATEMENT
* **Level 3 (WHAT “STOCK” MIGHT MEAN) [Type: WORDPLAY_TRANSFORM]:** ANCESTRY, BROTH, CATTLE, MERCHANDISE

### Top Candidate Partitions:
1. **Partition Score: 0.5780**
   - Group 1: **0.6549** | RECEIPT, INVOICE, BILL, STATEMENT                                 | CORRECT GROUP (TRANSACTION RECORD, Level 2) | [Pred Type: SYNONYM_OR_NEAR (58.9%, no-rel 29.2%)]
   - Group 2: **0.5933** | RANCH, ANCESTRY, MERCHANDISE, CATTLE                              | INCORRECT (Max overlap: 3/4 with WHAT “STOCK” MIGHT MEAN)
   - Group 3: **0.5908** | EXAMINE, PROBE, QUESTION, GRILL                                   | CORRECT GROUP (INTERROGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 26.0%)]
   - Group 4: **0.5509** | MARINARA, AIOLI, BARBECUE, BROTH                                  | INCORRECT (Max overlap: 3/4 with DIPPING SAUCES)
2. **Partition Score: 0.5621**
   - Group 1: **0.6549** | RECEIPT, INVOICE, BILL, STATEMENT                                 | CORRECT GROUP (TRANSACTION RECORD, Level 2) | [Pred Type: SYNONYM_OR_NEAR (58.9%, no-rel 29.2%)]
   - Group 2: **0.6188** | RANCH, ANCESTRY, CATTLE, BROTH                                    | INCORRECT (Max overlap: 3/4 with WHAT “STOCK” MIGHT MEAN)
   - Group 3: **0.5908** | EXAMINE, PROBE, QUESTION, GRILL                                   | CORRECT GROUP (INTERROGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 26.0%)]
   - Group 4: **0.5105** | MARINARA, AIOLI, MERCHANDISE, BARBECUE                            | INCORRECT (Max overlap: 3/4 with DIPPING SAUCES)
3. **Partition Score: 0.5400**
   - Group 1: **0.6549** | RECEIPT, INVOICE, BILL, STATEMENT                                 | CORRECT GROUP (TRANSACTION RECORD, Level 2) | [Pred Type: SYNONYM_OR_NEAR (58.9%, no-rel 29.2%)]
   - Group 2: **0.5908** | EXAMINE, PROBE, QUESTION, GRILL                                   | CORRECT GROUP (INTERROGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 26.0%)]
   - Group 3: **0.5093** | RANCH, BARBECUE, CATTLE, BROTH                                    | INCORRECT (Max overlap: 2/4 with DIPPING SAUCES)
   - Group 4: **0.5074** | ANCESTRY, MARINARA, AIOLI, MERCHANDISE                            | INCORRECT (Max overlap: 2/4 with WHAT “STOCK” MIGHT MEAN)
4. **Partition Score: 0.5393**
   - Group 1: **0.6549** | RECEIPT, INVOICE, BILL, STATEMENT                                 | CORRECT GROUP (TRANSACTION RECORD, Level 2) | [Pred Type: SYNONYM_OR_NEAR (58.9%, no-rel 29.2%)]
   - Group 2: **0.5996** | RANCH, MERCHANDISE, CATTLE, BROTH                                 | INCORRECT (Max overlap: 3/4 with WHAT “STOCK” MIGHT MEAN)
   - Group 3: **0.5908** | EXAMINE, PROBE, QUESTION, GRILL                                   | CORRECT GROUP (INTERROGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 26.0%)]
   - Group 4: **0.4730** | ANCESTRY, MARINARA, AIOLI, BARBECUE                               | INCORRECT (Max overlap: 3/4 with DIPPING SAUCES)
5. **Partition Score: 0.5360**
   - Group 1: **0.6549** | RECEIPT, INVOICE, BILL, STATEMENT                                 | CORRECT GROUP (TRANSACTION RECORD, Level 2) | [Pred Type: SYNONYM_OR_NEAR (58.9%, no-rel 29.2%)]
   - Group 2: **0.5936** | ANCESTRY, MERCHANDISE, CATTLE, BROTH                              | CORRECT GROUP (WHAT “STOCK” MIGHT MEAN, Level 3)
   - Group 3: **0.5908** | EXAMINE, PROBE, QUESTION, GRILL                                   | CORRECT GROUP (INTERROGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 26.0%)]
   - Group 4: **0.4689** | RANCH, MARINARA, AIOLI, BARBECUE                                  | CORRECT GROUP (DIPPING SAUCES, Level 0)

### Top Candidate Groups:
   - Group 1: **0.6549** | RECEIPT, INVOICE, BILL, STATEMENT                                 | CORRECT GROUP (TRANSACTION RECORD, Level 2) | [Pred Type: SYNONYM_OR_NEAR (58.9%, no-rel 29.2%)]
   - Group 2: **0.5933** | RANCH, ANCESTRY, MERCHANDISE, CATTLE                              | INCORRECT (Max overlap: 3/4 with WHAT “STOCK” MIGHT MEAN)
   - Group 3: **0.5908** | EXAMINE, PROBE, QUESTION, GRILL                                   | CORRECT GROUP (INTERROGATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (63.4%, no-rel 26.0%)]
   - Group 4: **0.5509** | MARINARA, AIOLI, BARBECUE, BROTH                                  | INCORRECT (Max overlap: 3/4 with DIPPING SAUCES)
   - Group 5: **0.6188** | RANCH, ANCESTRY, CATTLE, BROTH                                    | INCORRECT (Max overlap: 3/4 with WHAT “STOCK” MIGHT MEAN)
   - Group 6: **0.5105** | MARINARA, AIOLI, MERCHANDISE, BARBECUE                            | INCORRECT (Max overlap: 3/4 with DIPPING SAUCES)
   - Group 7: **0.5093** | RANCH, BARBECUE, CATTLE, BROTH                                    | INCORRECT (Max overlap: 2/4 with DIPPING SAUCES)
   - Group 8: **0.5074** | ANCESTRY, MARINARA, AIOLI, MERCHANDISE                            | INCORRECT (Max overlap: 2/4 with WHAT “STOCK” MIGHT MEAN)
   - Group 9: **0.5996** | RANCH, MERCHANDISE, CATTLE, BROTH                                 | INCORRECT (Max overlap: 3/4 with WHAT “STOCK” MIGHT MEAN)
   - Group 10: **0.4730** | ANCESTRY, MARINARA, AIOLI, BARBECUE                               | INCORRECT (Max overlap: 3/4 with DIPPING SAUCES)
   - Group 11: **0.5936** | ANCESTRY, MERCHANDISE, CATTLE, BROTH                              | CORRECT GROUP (WHAT “STOCK” MIGHT MEAN, Level 3)
   - Group 12: **0.4689** | RANCH, MARINARA, AIOLI, BARBECUE                                  | CORRECT GROUP (DIPPING SAUCES, Level 0)
   - Group 13: **0.5039** | MARINARA, AIOLI, BARBECUE, GRILL                                  | INCORRECT (Max overlap: 3/4 with DIPPING SAUCES) | [Pred Type: SEMANTIC_SET (59.3%, no-rel 19.9%)]
   - Group 14: **0.4881** | EXAMINE, MERCHANDISE, PROBE, QUESTION                             | INCORRECT (Max overlap: 3/4 with INTERROGATE) | [Pred Type: SYNONYM_OR_NEAR (66.5%, no-rel 18.1%)]
   - Group 15: **0.5528** | RANCH, ANCESTRY, MARINARA, CATTLE                                 | INCORRECT (Max overlap: 2/4 with DIPPING SAUCES)
   - Group 16: **0.4752** | AIOLI, MERCHANDISE, BARBECUE, BROTH                               | INCORRECT (Max overlap: 2/4 with DIPPING SAUCES)
   - Group 17: **0.5237** | RANCH, ANCESTRY, MARINARA, MERCHANDISE                            | INCORRECT (Max overlap: 2/4 with DIPPING SAUCES)
   - Group 18: **0.4838** | AIOLI, BARBECUE, CATTLE, BROTH                                    | INCORRECT (Max overlap: 2/4 with DIPPING SAUCES) | [Pred Type: FILL_IN_THE_BLANK (46.0%, no-rel 19.5%)]
   - Group 19: **0.5536** | RANCH, ANCESTRY, MERCHANDISE, BROTH                               | INCORRECT (Max overlap: 3/4 with WHAT “STOCK” MIGHT MEAN)
   - Group 20: **0.4723** | MARINARA, AIOLI, BARBECUE, CATTLE                                 | INCORRECT (Max overlap: 3/4 with DIPPING SAUCES)

---

## Puzzle 95 (ID: 1014)
**Words on Board:** BOW, LOW, FOOD, KISS, DUMP, SOW, ROW, VOW, MEAN, FIRE, TOW, RING, WIND, CAKE, VILE, BASE

### Ground Truth Categories:
* **Level 0 (DESPICABLE) [Type: SYNONYM_OR_NEAR]:** BASE, LOW, MEAN, VILE
* **Level 1 (FEATURES OF A WEDDING) [Type: SEMANTIC_SET]:** CAKE, KISS, RING, VOW
* **Level 2 (KINDS OF TRUCKS) [Type: FILL_IN_THE_BLANK]:** DUMP, FIRE, FOOD, TOW
* **Level 3 (HETERONYMS) [Type: SOUND_OR_SPELLING]:** BOW, ROW, SOW, WIND

### Top Candidate Partitions:
1. **Partition Score: 0.6061**
   - Group 1: **0.8077** | LOW, MEAN, VILE, BASE                                             | CORRECT GROUP (DESPICABLE, Level 0)
   - Group 2: **0.5960** | SOW, ROW, VOW, TOW                                                | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 3: **0.5936** | FOOD, KISS, RING, CAKE                                            | INCORRECT (Max overlap: 3/4 with FEATURES OF A WEDDING)
   - Group 4: **0.5701** | BOW, DUMP, FIRE, WIND                                             | INCORRECT (Max overlap: 2/4 with HETERONYMS)
2. **Partition Score: 0.5929**
   - Group 1: **0.8077** | LOW, MEAN, VILE, BASE                                             | CORRECT GROUP (DESPICABLE, Level 0)
   - Group 2: **0.5960** | SOW, ROW, VOW, TOW                                                | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 3: **0.5871** | FOOD, FIRE, RING, CAKE                                            | INCORRECT (Max overlap: 2/4 with KINDS OF TRUCKS)
   - Group 4: **0.5468** | BOW, KISS, DUMP, WIND                                             | INCORRECT (Max overlap: 2/4 with HETERONYMS)
3. **Partition Score: 0.5787**
   - Group 1: **0.8077** | LOW, MEAN, VILE, BASE                                             | CORRECT GROUP (DESPICABLE, Level 0)
   - Group 2: **0.5936** | FOOD, KISS, RING, CAKE                                            | INCORRECT (Max overlap: 3/4 with FEATURES OF A WEDDING)
   - Group 3: **0.5550** | DUMP, ROW, VOW, TOW                                               | INCORRECT (Max overlap: 2/4 with KINDS OF TRUCKS)
   - Group 4: **0.5317** | BOW, SOW, FIRE, WIND                                              | INCORRECT (Max overlap: 3/4 with HETERONYMS)
4. **Partition Score: 0.5785**
   - Group 1: **0.8077** | LOW, MEAN, VILE, BASE                                             | CORRECT GROUP (DESPICABLE, Level 0)
   - Group 2: **0.5936** | FOOD, KISS, RING, CAKE                                            | INCORRECT (Max overlap: 3/4 with FEATURES OF A WEDDING)
   - Group 3: **0.5536** | BOW, FIRE, TOW, WIND                                              | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 4: **0.5318** | DUMP, SOW, ROW, VOW                                               | INCORRECT (Max overlap: 2/4 with HETERONYMS)
5. **Partition Score: 0.5775**
   - Group 1: **0.8077** | LOW, MEAN, VILE, BASE                                             | CORRECT GROUP (DESPICABLE, Level 0)
   - Group 2: **0.6036** | FOOD, KISS, FIRE, CAKE                                            | INCORRECT (Max overlap: 2/4 with KINDS OF TRUCKS)
   - Group 3: **0.5960** | SOW, ROW, VOW, TOW                                                | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 4: **0.5107** | BOW, DUMP, RING, WIND                                             | INCORRECT (Max overlap: 2/4 with HETERONYMS)

### Top Candidate Groups:
   - Group 1: **0.8077** | LOW, MEAN, VILE, BASE                                             | CORRECT GROUP (DESPICABLE, Level 0)
   - Group 2: **0.5960** | SOW, ROW, VOW, TOW                                                | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 3: **0.5936** | FOOD, KISS, RING, CAKE                                            | INCORRECT (Max overlap: 3/4 with FEATURES OF A WEDDING)
   - Group 4: **0.5701** | BOW, DUMP, FIRE, WIND                                             | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 5: **0.5871** | FOOD, FIRE, RING, CAKE                                            | INCORRECT (Max overlap: 2/4 with KINDS OF TRUCKS)
   - Group 6: **0.5468** | BOW, KISS, DUMP, WIND                                             | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 7: **0.5550** | DUMP, ROW, VOW, TOW                                               | INCORRECT (Max overlap: 2/4 with KINDS OF TRUCKS)
   - Group 8: **0.5317** | BOW, SOW, FIRE, WIND                                              | INCORRECT (Max overlap: 3/4 with HETERONYMS)
   - Group 9: **0.5536** | BOW, FIRE, TOW, WIND                                              | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 10: **0.5318** | DUMP, SOW, ROW, VOW                                               | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 11: **0.6036** | FOOD, KISS, FIRE, CAKE                                            | INCORRECT (Max overlap: 2/4 with KINDS OF TRUCKS)
   - Group 12: **0.5107** | BOW, DUMP, RING, WIND                                             | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 13: **0.5901** | BOW, SOW, ROW, VOW                                                | INCORRECT (Max overlap: 3/4 with HETERONYMS)
   - Group 14: **0.5111** | DUMP, FIRE, TOW, WIND                                             | INCORRECT (Max overlap: 3/4 with KINDS OF TRUCKS)
   - Group 15: **0.5847** | BOW, KISS, FIRE, WIND                                             | INCORRECT (Max overlap: 2/4 with HETERONYMS)
   - Group 16: **0.5753** | DUMP, SOW, ROW, TOW                                               | INCORRECT (Max overlap: 2/4 with KINDS OF TRUCKS)
   - Group 17: **0.5157** | FOOD, VOW, RING, CAKE                                             | INCORRECT (Max overlap: 3/4 with FEATURES OF A WEDDING)
   - Group 18: **0.5342** | BOW, SOW, TOW, WIND                                               | INCORRECT (Max overlap: 3/4 with HETERONYMS)
   - Group 19: **0.5219** | DUMP, ROW, VOW, RING                                              | INCORRECT (Max overlap: 2/4 with FEATURES OF A WEDDING)
   - Group 20: **0.5268** | BOW, KISS, TOW, WIND                                              | INCORRECT (Max overlap: 2/4 with HETERONYMS)

---

## Puzzle 96 (ID: 801)
**Words on Board:** KNITTING NEEDLES, CROCHET HOOK, DOMINO, CROOK, BARBER POLE, CHOPSTICKS, CAROUSEL, YIN-YANG SYMBOL, CEILING FAN, LAZY SUSAN, CANDY CANE, SKI POLES, PIANO KEYS, CLAVES, CROWBAR, ZEBRA

### Ground Truth Categories:
* **Level 0 (BLACK-AND-WHITE THINGS) [Type: SEMANTIC_SET]:** DOMINO, PIANO KEYS, YIN-YANG SYMBOL, ZEBRA
* **Level 1 (PAIRS OF RODS) [Type: SEMANTIC_SET]:** CHOPSTICKS, CLAVES, KNITTING NEEDLES, SKI POLES
* **Level 2 (THINGS THAT ROTATE ABOUT A VERTICAL AXIS) [Type: SEMANTIC_SET]:** BARBER POLE, CAROUSEL, CEILING FAN, LAZY SUSAN
* **Level 3 (RODS THAT CURVE AT ONE END) [Type: SEMANTIC_SET]:** CANDY CANE, CROCHET HOOK, CROOK, CROWBAR

### Top Candidate Partitions:
1. **Partition Score: 0.5185**
   - Group 1: **0.5785** | BARBER POLE, LAZY SUSAN, CANDY CANE, CROWBAR                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 2: **0.5382** | KNITTING NEEDLES, CROCHET HOOK, YIN-YANG SYMBOL, CEILING FAN      | INCORRECT (Max overlap: 1/4 with PAIRS OF RODS)
   - Group 3: **0.5120** | DOMINO, CROOK, CAROUSEL, ZEBRA                                    | INCORRECT (Max overlap: 2/4 with BLACK-AND-WHITE THINGS)
   - Group 4: **0.5004** | CHOPSTICKS, SKI POLES, PIANO KEYS, CLAVES                         | INCORRECT (Max overlap: 3/4 with PAIRS OF RODS)
2. **Partition Score: 0.5151**
   - Group 1: **0.5453** | CROCHET HOOK, LAZY SUSAN, CANDY CANE, CROWBAR                     | INCORRECT (Max overlap: 3/4 with RODS THAT CURVE AT ONE END)
   - Group 2: **0.5400** | KNITTING NEEDLES, BARBER POLE, YIN-YANG SYMBOL, CEILING FAN       | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 3: **0.5120** | DOMINO, CROOK, CAROUSEL, ZEBRA                                    | INCORRECT (Max overlap: 2/4 with BLACK-AND-WHITE THINGS)
   - Group 4: **0.5004** | CHOPSTICKS, SKI POLES, PIANO KEYS, CLAVES                         | INCORRECT (Max overlap: 3/4 with PAIRS OF RODS)
3. **Partition Score: 0.5136**
   - Group 1: **0.5538** | YIN-YANG SYMBOL, LAZY SUSAN, CANDY CANE, CROWBAR                  | INCORRECT (Max overlap: 2/4 with RODS THAT CURVE AT ONE END)
   - Group 2: **0.5271** | KNITTING NEEDLES, CROCHET HOOK, BARBER POLE, CEILING FAN          | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 3: **0.5120** | DOMINO, CROOK, CAROUSEL, ZEBRA                                    | INCORRECT (Max overlap: 2/4 with BLACK-AND-WHITE THINGS)
   - Group 4: **0.5004** | CHOPSTICKS, SKI POLES, PIANO KEYS, CLAVES                         | INCORRECT (Max overlap: 3/4 with PAIRS OF RODS)
4. **Partition Score: 0.5132**
   - Group 1: **0.5390** | KNITTING NEEDLES, CROCHET HOOK, BARBER POLE, YIN-YANG SYMBOL      | INCORRECT (Max overlap: 1/4 with PAIRS OF RODS)
   - Group 2: **0.5337** | CEILING FAN, LAZY SUSAN, CANDY CANE, CROWBAR                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 3: **0.5120** | DOMINO, CROOK, CAROUSEL, ZEBRA                                    | INCORRECT (Max overlap: 2/4 with BLACK-AND-WHITE THINGS)
   - Group 4: **0.5004** | CHOPSTICKS, SKI POLES, PIANO KEYS, CLAVES                         | INCORRECT (Max overlap: 3/4 with PAIRS OF RODS)
5. **Partition Score: 0.5130**
   - Group 1: **0.5460** | BARBER POLE, CHOPSTICKS, LAZY SUSAN, CROWBAR                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 2: **0.5382** | KNITTING NEEDLES, CROCHET HOOK, YIN-YANG SYMBOL, CEILING FAN      | INCORRECT (Max overlap: 1/4 with PAIRS OF RODS)
   - Group 3: **0.5120** | DOMINO, CROOK, CAROUSEL, ZEBRA                                    | INCORRECT (Max overlap: 2/4 with BLACK-AND-WHITE THINGS)
   - Group 4: **0.4968** | CANDY CANE, SKI POLES, PIANO KEYS, CLAVES                         | INCORRECT (Max overlap: 2/4 with PAIRS OF RODS)

### Top Candidate Groups:
   - Group 1: **0.5785** | BARBER POLE, LAZY SUSAN, CANDY CANE, CROWBAR                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 2: **0.5382** | KNITTING NEEDLES, CROCHET HOOK, YIN-YANG SYMBOL, CEILING FAN      | INCORRECT (Max overlap: 1/4 with PAIRS OF RODS)
   - Group 3: **0.5120** | DOMINO, CROOK, CAROUSEL, ZEBRA                                    | INCORRECT (Max overlap: 2/4 with BLACK-AND-WHITE THINGS)
   - Group 4: **0.5004** | CHOPSTICKS, SKI POLES, PIANO KEYS, CLAVES                         | INCORRECT (Max overlap: 3/4 with PAIRS OF RODS)
   - Group 5: **0.5453** | CROCHET HOOK, LAZY SUSAN, CANDY CANE, CROWBAR                     | INCORRECT (Max overlap: 3/4 with RODS THAT CURVE AT ONE END)
   - Group 6: **0.5400** | KNITTING NEEDLES, BARBER POLE, YIN-YANG SYMBOL, CEILING FAN       | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 7: **0.5538** | YIN-YANG SYMBOL, LAZY SUSAN, CANDY CANE, CROWBAR                  | INCORRECT (Max overlap: 2/4 with RODS THAT CURVE AT ONE END)
   - Group 8: **0.5271** | KNITTING NEEDLES, CROCHET HOOK, BARBER POLE, CEILING FAN          | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 9: **0.5390** | KNITTING NEEDLES, CROCHET HOOK, BARBER POLE, YIN-YANG SYMBOL      | INCORRECT (Max overlap: 1/4 with PAIRS OF RODS)
   - Group 10: **0.5337** | CEILING FAN, LAZY SUSAN, CANDY CANE, CROWBAR                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 11: **0.5460** | BARBER POLE, CHOPSTICKS, LAZY SUSAN, CROWBAR                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 12: **0.4968** | CANDY CANE, SKI POLES, PIANO KEYS, CLAVES                         | INCORRECT (Max overlap: 2/4 with PAIRS OF RODS)
   - Group 13: **0.5605** | CROCHET HOOK, BARBER POLE, CANDY CANE, CROWBAR                    | INCORRECT (Max overlap: 3/4 with RODS THAT CURVE AT ONE END)
   - Group 14: **0.5158** | KNITTING NEEDLES, YIN-YANG SYMBOL, CEILING FAN, LAZY SUSAN        | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 15: **0.5347** | BARBER POLE, LAZY SUSAN, CANDY CANE, PIANO KEYS                   | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 16: **0.4978** | CHOPSTICKS, SKI POLES, CLAVES, CROWBAR                            | INCORRECT (Max overlap: 3/4 with PAIRS OF RODS)
   - Group 17: **0.5403** | YIN-YANG SYMBOL, LAZY SUSAN, CANDY CANE, PIANO KEYS               | INCORRECT (Max overlap: 2/4 with BLACK-AND-WHITE THINGS)
   - Group 18: **0.5613** | BARBER POLE, CHOPSTICKS, SKI POLES, CROWBAR                       | INCORRECT (Max overlap: 2/4 with PAIRS OF RODS)
   - Group 19: **0.4883** | LAZY SUSAN, CANDY CANE, PIANO KEYS, CLAVES                        | INCORRECT (Max overlap: 1/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)
   - Group 20: **0.5549** | BARBER POLE, YIN-YANG SYMBOL, LAZY SUSAN, CROWBAR                 | INCORRECT (Max overlap: 2/4 with THINGS THAT ROTATE ABOUT A VERTICAL AXIS)

---

## Puzzle 97 (ID: 171)
**Words on Board:** TOE, COME, ARCH, STAY, HARP, HEEL, SNAKE, BASS, JERK, SOLE, SIT, ORGAN, DOWN, BALL, HORN, DOG

### Ground Truth Categories:
* **Level 0 (FOOT PARTS) [Type: SEMANTIC_SET]:** ARCH, BALL, SOLE, TOE
* **Level 1 (MUSICAL INSTRUMENTS) [Type: SEMANTIC_SET]:** BASS, HARP, HORN, ORGAN
* **Level 2 (DOG COMMANDS) [Type: SEMANTIC_SET]:** COME, DOWN, SIT, STAY
* **Level 3 (BADDIE) [Type: SYNONYM_OR_NEAR]:** DOG, HEEL, JERK, SNAKE

### Top Candidate Partitions:
1. **Partition Score: 0.5536**
   - Group 1: **0.6997** | HARP, BASS, ORGAN, HORN                                           | CORRECT GROUP (MUSICAL INSTRUMENTS, Level 1)
   - Group 2: **0.6496** | COME, STAY, SIT, DOWN                                             | CORRECT GROUP (DOG COMMANDS, Level 2)
   - Group 3: **0.5785** | TOE, ARCH, HEEL, SOLE                                             | INCORRECT (Max overlap: 3/4 with FOOT PARTS) | [Pred Type: SEMANTIC_SET (48.6%, no-rel 32.4%)]
   - Group 4: **0.4774** | SNAKE, JERK, BALL, DOG                                            | INCORRECT (Max overlap: 3/4 with BADDIE)
2. **Partition Score: 0.5533**
   - Group 1: **0.6496** | COME, STAY, SIT, DOWN                                             | CORRECT GROUP (DOG COMMANDS, Level 2)
   - Group 2: **0.6297** | SNAKE, BASS, BALL, DOG                                            | INCORRECT (Max overlap: 2/4 with BADDIE)
   - Group 3: **0.5785** | TOE, ARCH, HEEL, SOLE                                             | INCORRECT (Max overlap: 3/4 with FOOT PARTS) | [Pred Type: SEMANTIC_SET (48.6%, no-rel 32.4%)]
   - Group 4: **0.4951** | HARP, JERK, ORGAN, HORN                                           | INCORRECT (Max overlap: 3/4 with MUSICAL INSTRUMENTS)
3. **Partition Score: 0.5480**
   - Group 1: **0.6496** | COME, STAY, SIT, DOWN                                             | CORRECT GROUP (DOG COMMANDS, Level 2)
   - Group 2: **0.5886** | SNAKE, ORGAN, BALL, DOG                                           | INCORRECT (Max overlap: 2/4 with BADDIE)
   - Group 3: **0.5785** | TOE, ARCH, HEEL, SOLE                                             | INCORRECT (Max overlap: 3/4 with FOOT PARTS) | [Pred Type: SEMANTIC_SET (48.6%, no-rel 32.4%)]
   - Group 4: **0.4996** | HARP, BASS, JERK, HORN                                            | INCORRECT (Max overlap: 3/4 with MUSICAL INSTRUMENTS)
4. **Partition Score: 0.5440**
   - Group 1: **0.6496** | COME, STAY, SIT, DOWN                                             | CORRECT GROUP (DOG COMMANDS, Level 2)
   - Group 2: **0.5785** | TOE, ARCH, HEEL, SOLE                                             | INCORRECT (Max overlap: 3/4 with FOOT PARTS) | [Pred Type: SEMANTIC_SET (48.6%, no-rel 32.4%)]
   - Group 3: **0.5255** | HARP, ORGAN, BALL, DOG                                            | INCORRECT (Max overlap: 2/4 with MUSICAL INSTRUMENTS)
   - Group 4: **0.5150** | SNAKE, BASS, JERK, HORN                                           | INCORRECT (Max overlap: 2/4 with BADDIE)
5. **Partition Score: 0.5398**
   - Group 1: **0.6496** | COME, STAY, SIT, DOWN                                             | CORRECT GROUP (DOG COMMANDS, Level 2)
   - Group 2: **0.5871** | HARP, BASS, ORGAN, DOG                                            | INCORRECT (Max overlap: 3/4 with MUSICAL INSTRUMENTS)
   - Group 3: **0.5785** | TOE, ARCH, HEEL, SOLE                                             | INCORRECT (Max overlap: 3/4 with FOOT PARTS) | [Pred Type: SEMANTIC_SET (48.6%, no-rel 32.4%)]
   - Group 4: **0.4842** | SNAKE, JERK, BALL, HORN                                           | INCORRECT (Max overlap: 2/4 with BADDIE)

### Top Candidate Groups:
   - Group 1: **0.6997** | HARP, BASS, ORGAN, HORN                                           | CORRECT GROUP (MUSICAL INSTRUMENTS, Level 1)
   - Group 2: **0.6496** | COME, STAY, SIT, DOWN                                             | CORRECT GROUP (DOG COMMANDS, Level 2)
   - Group 3: **0.5785** | TOE, ARCH, HEEL, SOLE                                             | INCORRECT (Max overlap: 3/4 with FOOT PARTS) | [Pred Type: SEMANTIC_SET (48.6%, no-rel 32.4%)]
   - Group 4: **0.4774** | SNAKE, JERK, BALL, DOG                                            | INCORRECT (Max overlap: 3/4 with BADDIE)
   - Group 5: **0.6297** | SNAKE, BASS, BALL, DOG                                            | INCORRECT (Max overlap: 2/4 with BADDIE)
   - Group 6: **0.4951** | HARP, JERK, ORGAN, HORN                                           | INCORRECT (Max overlap: 3/4 with MUSICAL INSTRUMENTS)
   - Group 7: **0.5886** | SNAKE, ORGAN, BALL, DOG                                           | INCORRECT (Max overlap: 2/4 with BADDIE)
   - Group 8: **0.4996** | HARP, BASS, JERK, HORN                                            | INCORRECT (Max overlap: 3/4 with MUSICAL INSTRUMENTS)
   - Group 9: **0.5255** | HARP, ORGAN, BALL, DOG                                            | INCORRECT (Max overlap: 2/4 with MUSICAL INSTRUMENTS)
   - Group 10: **0.5150** | SNAKE, BASS, JERK, HORN                                           | INCORRECT (Max overlap: 2/4 with BADDIE)
   - Group 11: **0.5871** | HARP, BASS, ORGAN, DOG                                            | INCORRECT (Max overlap: 3/4 with MUSICAL INSTRUMENTS)
   - Group 12: **0.4842** | SNAKE, JERK, BALL, HORN                                           | INCORRECT (Max overlap: 2/4 with BADDIE)
   - Group 13: **0.6035** | HARP, ORGAN, HORN, DOG                                            | INCORRECT (Max overlap: 3/4 with MUSICAL INSTRUMENTS)
   - Group 14: **0.4743** | SNAKE, BASS, JERK, BALL                                           | INCORRECT (Max overlap: 2/4 with BADDIE)
   - Group 15: **0.6118** | SNAKE, BALL, HORN, DOG                                            | INCORRECT (Max overlap: 2/4 with BADDIE)
   - Group 16: **0.4984** | ARCH, HARP, BASS, ORGAN                                           | INCORRECT (Max overlap: 3/4 with MUSICAL INSTRUMENTS)
   - Group 17: **0.4943** | TOE, HEEL, JERK, SOLE                                             | INCORRECT (Max overlap: 2/4 with FOOT PARTS)
   - Group 18: **0.4847** | TOE, SNAKE, BALL, DOG                                             | INCORRECT (Max overlap: 2/4 with FOOT PARTS)
   - Group 19: **0.4693** | ARCH, HEEL, JERK, SOLE                                            | INCORRECT (Max overlap: 2/4 with FOOT PARTS)
   - Group 20: **0.6067** | SNAKE, BASS, ORGAN, BALL                                          | INCORRECT (Max overlap: 2/4 with MUSICAL INSTRUMENTS)

---

## Puzzle 98 (ID: 877)
**Words on Board:** BOTCH, FOREST, FRANKLIN, KNIFE, BAKER, SPOIL, KNIGHT, FLACK, BLOW, CANDLESTICK, MAKER, BUTCHER, ROPE, COAT, BOW, WRENCH

### Ground Truth Categories:
* **Level 0 (MAKE A HASH OF) [Type: SYNONYM_OR_NEAR]:** BLOW, BOTCH, BUTCHER, SPOIL
* **Level 1 (WEAPONS IN THE GAME CLUE) [Type: NAMED_ENTITY_SET]:** CANDLESTICK, KNIFE, ROPE, WRENCH
* **Level 2 (ICONIC SOUL SINGERS) [Type: NAMED_ENTITY_SET]:** BAKER, FRANKLIN, FLACK, KNIGHT
* **Level 3 (RAIN___) [Type: FILL_IN_THE_BLANK]:** BOW, COAT, FOREST, MAKER

### Top Candidate Partitions:
1. **Partition Score: 0.4588**
   - Group 1: **0.5637** | BOTCH, SPOIL, BLOW, WRENCH                                        | INCORRECT (Max overlap: 3/4 with MAKE A HASH OF) | [Pred Type: SYNONYM_OR_NEAR (64.7%, no-rel 25.9%)]
   - Group 2: **0.4999** | KNIFE, ROPE, COAT, BOW                                            | INCORRECT (Max overlap: 2/4 with WEAPONS IN THE GAME CLUE)
   - Group 3: **0.4996** | FOREST, FRANKLIN, KNIGHT, CANDLESTICK                             | INCORRECT (Max overlap: 2/4 with ICONIC SOUL SINGERS)
   - Group 4: **0.4059** | BAKER, FLACK, MAKER, BUTCHER                                      | INCORRECT (Max overlap: 2/4 with ICONIC SOUL SINGERS) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 15.8%)]
2. **Partition Score: 0.4583**
   - Group 1: **0.6142** | BOTCH, SPOIL, BLOW, BUTCHER                                       | CORRECT GROUP (MAKE A HASH OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 27.4%)]
   - Group 2: **0.5018** | KNIFE, COAT, BOW, WRENCH                                          | INCORRECT (Max overlap: 2/4 with WEAPONS IN THE GAME CLUE)
   - Group 3: **0.4779** | FOREST, KNIGHT, CANDLESTICK, ROPE                                 | INCORRECT (Max overlap: 2/4 with WEAPONS IN THE GAME CLUE)
   - Group 4: **0.4010** | FRANKLIN, BAKER, FLACK, MAKER                                     | INCORRECT (Max overlap: 3/4 with ICONIC SOUL SINGERS)
3. **Partition Score: 0.4559**
   - Group 1: **0.6142** | BOTCH, SPOIL, BLOW, BUTCHER                                       | CORRECT GROUP (MAKE A HASH OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 27.4%)]
   - Group 2: **0.5277** | FOREST, ROPE, COAT, BOW                                           | INCORRECT (Max overlap: 3/4 with RAIN___)
   - Group 3: **0.4528** | KNIFE, FLACK, CANDLESTICK, WRENCH                                 | INCORRECT (Max overlap: 3/4 with WEAPONS IN THE GAME CLUE) | [Pred Type: SEMANTIC_SET (46.3%, no-rel 18.9%)]
   - Group 4: **0.3961** | FRANKLIN, BAKER, KNIGHT, MAKER                                    | INCORRECT (Max overlap: 3/4 with ICONIC SOUL SINGERS)
4. **Partition Score: 0.4557**
   - Group 1: **0.6142** | BOTCH, SPOIL, BLOW, BUTCHER                                       | CORRECT GROUP (MAKE A HASH OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 27.4%)]
   - Group 2: **0.5066** | KNIFE, ROPE, BOW, WRENCH                                          | INCORRECT (Max overlap: 3/4 with WEAPONS IN THE GAME CLUE)
   - Group 3: **0.4591** | FOREST, KNIGHT, CANDLESTICK, COAT                                 | INCORRECT (Max overlap: 2/4 with RAIN___)
   - Group 4: **0.4010** | FRANKLIN, BAKER, FLACK, MAKER                                     | INCORRECT (Max overlap: 3/4 with ICONIC SOUL SINGERS)
5. **Partition Score: 0.4552**
   - Group 1: **0.5831** | BOTCH, SPOIL, BLOW, BOW                                           | INCORRECT (Max overlap: 3/4 with MAKE A HASH OF) | [Pred Type: SYNONYM_OR_NEAR (67.5%, no-rel 22.5%)]
   - Group 2: **0.4996** | FOREST, FRANKLIN, KNIGHT, CANDLESTICK                             | INCORRECT (Max overlap: 2/4 with ICONIC SOUL SINGERS)
   - Group 3: **0.4688** | KNIFE, ROPE, COAT, WRENCH                                         | INCORRECT (Max overlap: 3/4 with WEAPONS IN THE GAME CLUE)
   - Group 4: **0.4059** | BAKER, FLACK, MAKER, BUTCHER                                      | INCORRECT (Max overlap: 2/4 with ICONIC SOUL SINGERS) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 15.8%)]

### Top Candidate Groups:
   - Group 1: **0.5637** | BOTCH, SPOIL, BLOW, WRENCH                                        | INCORRECT (Max overlap: 3/4 with MAKE A HASH OF) | [Pred Type: SYNONYM_OR_NEAR (64.7%, no-rel 25.9%)]
   - Group 2: **0.4999** | KNIFE, ROPE, COAT, BOW                                            | INCORRECT (Max overlap: 2/4 with WEAPONS IN THE GAME CLUE)
   - Group 3: **0.4996** | FOREST, FRANKLIN, KNIGHT, CANDLESTICK                             | INCORRECT (Max overlap: 2/4 with ICONIC SOUL SINGERS)
   - Group 4: **0.4059** | BAKER, FLACK, MAKER, BUTCHER                                      | INCORRECT (Max overlap: 2/4 with ICONIC SOUL SINGERS) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 15.8%)]
   - Group 5: **0.6142** | BOTCH, SPOIL, BLOW, BUTCHER                                       | CORRECT GROUP (MAKE A HASH OF, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 27.4%)]
   - Group 6: **0.5018** | KNIFE, COAT, BOW, WRENCH                                          | INCORRECT (Max overlap: 2/4 with WEAPONS IN THE GAME CLUE)
   - Group 7: **0.4779** | FOREST, KNIGHT, CANDLESTICK, ROPE                                 | INCORRECT (Max overlap: 2/4 with WEAPONS IN THE GAME CLUE)
   - Group 8: **0.4010** | FRANKLIN, BAKER, FLACK, MAKER                                     | INCORRECT (Max overlap: 3/4 with ICONIC SOUL SINGERS)
   - Group 9: **0.5277** | FOREST, ROPE, COAT, BOW                                           | INCORRECT (Max overlap: 3/4 with RAIN___)
   - Group 10: **0.4528** | KNIFE, FLACK, CANDLESTICK, WRENCH                                 | INCORRECT (Max overlap: 3/4 with WEAPONS IN THE GAME CLUE) | [Pred Type: SEMANTIC_SET (46.3%, no-rel 18.9%)]
   - Group 11: **0.3961** | FRANKLIN, BAKER, KNIGHT, MAKER                                    | INCORRECT (Max overlap: 3/4 with ICONIC SOUL SINGERS)
   - Group 12: **0.5066** | KNIFE, ROPE, BOW, WRENCH                                          | INCORRECT (Max overlap: 3/4 with WEAPONS IN THE GAME CLUE)
   - Group 13: **0.4591** | FOREST, KNIGHT, CANDLESTICK, COAT                                 | INCORRECT (Max overlap: 2/4 with RAIN___)
   - Group 14: **0.5831** | BOTCH, SPOIL, BLOW, BOW                                           | INCORRECT (Max overlap: 3/4 with MAKE A HASH OF) | [Pred Type: SYNONYM_OR_NEAR (67.5%, no-rel 22.5%)]
   - Group 15: **0.4688** | KNIFE, ROPE, COAT, WRENCH                                         | INCORRECT (Max overlap: 3/4 with WEAPONS IN THE GAME CLUE)
   - Group 16: **0.4537** | FOREST, KNIGHT, MAKER, COAT                                       | INCORRECT (Max overlap: 3/4 with RAIN___)
   - Group 17: **0.4019** | FRANKLIN, BAKER, FLACK, CANDLESTICK                               | INCORRECT (Max overlap: 3/4 with ICONIC SOUL SINGERS) | [Pred Type: NAMED_ENTITY_SET (45.7%, no-rel 9.4%)]
   - Group 18: **0.5057** | FOREST, KNIGHT, ROPE, COAT                                        | INCORRECT (Max overlap: 2/4 with RAIN___)
   - Group 19: **0.4760** | KNIFE, FLACK, BOW, WRENCH                                         | INCORRECT (Max overlap: 2/4 with WEAPONS IN THE GAME CLUE)
   - Group 20: **0.3940** | FRANKLIN, BAKER, CANDLESTICK, MAKER                               | INCORRECT (Max overlap: 2/4 with ICONIC SOUL SINGERS)

---

## Puzzle 99 (ID: 608)
**Words on Board:** FINGER, SOUL, BIO, STAT, PLAYER, LATER, RUFFLE, GATHER, FAST, NOW, JUNK, PUCKER, THEN, TEAM, SOON, BUNCH

### Ground Truth Categories:
* **Level 0 (INFO ON A BASEBALL CARD) [Type: SEMANTIC_SET]:** BIO, PLAYER, STAT, TEAM
* **Level 1 (SCRUNCH, AS FABRIC) [Type: SYNONYM_OR_NEAR]:** BUNCH, GATHER, RUFFLE, PUCKER
* **Level 2 (TIME ADVERBS) [Type: SEMANTIC_SET]:** LATER, NOW, SOON, THEN
* **Level 3 (___ FOOD) [Type: FILL_IN_THE_BLANK]:** FAST, FINGER, JUNK, SOUL

### Top Candidate Partitions:
1. **Partition Score: 0.4504**
   - Group 1: **0.6525** | LATER, NOW, THEN, SOON                                            | CORRECT GROUP (TIME ADVERBS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 31.9%)]
   - Group 2: **0.5290** | FINGER, GATHER, PUCKER, BUNCH                                     | INCORRECT (Max overlap: 3/4 with SCRUNCH, AS FABRIC) | [Pred Type: SYNONYM_OR_NEAR (60.4%, no-rel 27.6%)]
   - Group 3: **0.4743** | SOUL, BIO, FAST, JUNK                                             | INCORRECT (Max overlap: 3/4 with ___ FOOD)
   - Group 4: **0.3685** | STAT, PLAYER, RUFFLE, TEAM                                        | INCORRECT (Max overlap: 3/4 with INFO ON A BASEBALL CARD) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 23.4%)]
2. **Partition Score: 0.4504**
   - Group 1: **0.6525** | LATER, NOW, THEN, SOON                                            | CORRECT GROUP (TIME ADVERBS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 31.9%)]
   - Group 2: **0.5689** | RUFFLE, GATHER, PUCKER, BUNCH                                     | CORRECT GROUP (SCRUNCH, AS FABRIC, Level 1) | [Pred Type: SYNONYM_OR_NEAR (68.0%, no-rel 23.5%)]
   - Group 3: **0.4309** | FINGER, STAT, FAST, JUNK                                          | INCORRECT (Max overlap: 3/4 with ___ FOOD)
   - Group 4: **0.3698** | SOUL, BIO, PLAYER, TEAM                                           | INCORRECT (Max overlap: 3/4 with INFO ON A BASEBALL CARD)
3. **Partition Score: 0.4454**
   - Group 1: **0.6525** | LATER, NOW, THEN, SOON                                            | CORRECT GROUP (TIME ADVERBS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 31.9%)]
   - Group 2: **0.5689** | RUFFLE, GATHER, PUCKER, BUNCH                                     | CORRECT GROUP (SCRUNCH, AS FABRIC, Level 1) | [Pred Type: SYNONYM_OR_NEAR (68.0%, no-rel 23.5%)]
   - Group 3: **0.3809** | FINGER, SOUL, PLAYER, TEAM                                        | INCORRECT (Max overlap: 2/4 with ___ FOOD)
   - Group 4: **0.3784** | BIO, STAT, FAST, JUNK                                             | INCORRECT (Max overlap: 2/4 with INFO ON A BASEBALL CARD)
4. **Partition Score: 0.4417**
   - Group 1: **0.6525** | LATER, NOW, THEN, SOON                                            | CORRECT GROUP (TIME ADVERBS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 31.9%)]
   - Group 2: **0.5689** | RUFFLE, GATHER, PUCKER, BUNCH                                     | CORRECT GROUP (SCRUNCH, AS FABRIC, Level 1) | [Pred Type: SYNONYM_OR_NEAR (68.0%, no-rel 23.5%)]
   - Group 3: **0.3748** | SOUL, STAT, PLAYER, TEAM                                          | INCORRECT (Max overlap: 3/4 with INFO ON A BASEBALL CARD)
   - Group 4: **0.3733** | FINGER, BIO, FAST, JUNK                                           | INCORRECT (Max overlap: 3/4 with ___ FOOD)
5. **Partition Score: 0.4360**
   - Group 1: **0.6525** | LATER, NOW, THEN, SOON                                            | CORRECT GROUP (TIME ADVERBS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 31.9%)]
   - Group 2: **0.4961** | STAT, GATHER, PUCKER, BUNCH                                       | INCORRECT (Max overlap: 3/4 with SCRUNCH, AS FABRIC) | [Pred Type: SYNONYM_OR_NEAR (67.5%, no-rel 22.1%)]
   - Group 3: **0.4271** | FINGER, RUFFLE, FAST, JUNK                                        | INCORRECT (Max overlap: 3/4 with ___ FOOD)
   - Group 4: **0.3698** | SOUL, BIO, PLAYER, TEAM                                           | INCORRECT (Max overlap: 3/4 with INFO ON A BASEBALL CARD)

### Top Candidate Groups:
   - Group 1: **0.6525** | LATER, NOW, THEN, SOON                                            | CORRECT GROUP (TIME ADVERBS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (54.2%, no-rel 31.9%)]
   - Group 2: **0.5290** | FINGER, GATHER, PUCKER, BUNCH                                     | INCORRECT (Max overlap: 3/4 with SCRUNCH, AS FABRIC) | [Pred Type: SYNONYM_OR_NEAR (60.4%, no-rel 27.6%)]
   - Group 3: **0.4743** | SOUL, BIO, FAST, JUNK                                             | INCORRECT (Max overlap: 3/4 with ___ FOOD)
   - Group 4: **0.3685** | STAT, PLAYER, RUFFLE, TEAM                                        | INCORRECT (Max overlap: 3/4 with INFO ON A BASEBALL CARD) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 23.4%)]
   - Group 5: **0.5689** | RUFFLE, GATHER, PUCKER, BUNCH                                     | CORRECT GROUP (SCRUNCH, AS FABRIC, Level 1) | [Pred Type: SYNONYM_OR_NEAR (68.0%, no-rel 23.5%)]
   - Group 6: **0.4309** | FINGER, STAT, FAST, JUNK                                          | INCORRECT (Max overlap: 3/4 with ___ FOOD)
   - Group 7: **0.3698** | SOUL, BIO, PLAYER, TEAM                                           | INCORRECT (Max overlap: 3/4 with INFO ON A BASEBALL CARD)
   - Group 8: **0.3809** | FINGER, SOUL, PLAYER, TEAM                                        | INCORRECT (Max overlap: 2/4 with ___ FOOD)
   - Group 9: **0.3784** | BIO, STAT, FAST, JUNK                                             | INCORRECT (Max overlap: 2/4 with INFO ON A BASEBALL CARD)
   - Group 10: **0.3748** | SOUL, STAT, PLAYER, TEAM                                          | INCORRECT (Max overlap: 3/4 with INFO ON A BASEBALL CARD)
   - Group 11: **0.3733** | FINGER, BIO, FAST, JUNK                                           | INCORRECT (Max overlap: 3/4 with ___ FOOD)
   - Group 12: **0.4961** | STAT, GATHER, PUCKER, BUNCH                                       | INCORRECT (Max overlap: 3/4 with SCRUNCH, AS FABRIC) | [Pred Type: SYNONYM_OR_NEAR (67.5%, no-rel 22.1%)]
   - Group 13: **0.4271** | FINGER, RUFFLE, FAST, JUNK                                        | INCORRECT (Max overlap: 3/4 with ___ FOOD)
   - Group 14: **0.3836** | STAT, RUFFLE, FAST, JUNK                                          | INCORRECT (Max overlap: 2/4 with ___ FOOD)
   - Group 15: **0.3696** | SOUL, PLAYER, RUFFLE, TEAM                                        | INCORRECT (Max overlap: 2/4 with INFO ON A BASEBALL CARD)
   - Group 16: **0.4269** | FINGER, STAT, RUFFLE, BUNCH                                       | INCORRECT (Max overlap: 2/4 with SCRUNCH, AS FABRIC)
   - Group 17: **0.3698** | PLAYER, GATHER, PUCKER, TEAM                                      | INCORRECT (Max overlap: 2/4 with INFO ON A BASEBALL CARD) | [Pred Type: SYNONYM_OR_NEAR (71.6%, no-rel 15.8%)]
   - Group 18: **0.5283** | STAT, LATER, NOW, THEN                                            | INCORRECT (Max overlap: 3/4 with TIME ADVERBS) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 33.7%)]
   - Group 19: **0.4213** | FINGER, FAST, JUNK, SOON                                          | INCORRECT (Max overlap: 3/4 with ___ FOOD)
   - Group 20: **0.5337** | LATER, GATHER, PUCKER, BUNCH                                      | INCORRECT (Max overlap: 3/4 with SCRUNCH, AS FABRIC) | [Pred Type: SYNONYM_OR_NEAR (67.8%, no-rel 23.3%)]

---

## Puzzle 100 (ID: 995)
**Words on Board:** VIDEO GAME, HOUND, SQUARE, BOOK, TAIL, BIKE, WORKING, SHADOW, NEW, SPORTING, TRACK, TOY, GONE, FAIR, GOSSIP, HONEST

### Ground Truth Categories:
* **Level 0 (PURSUE) [Type: SYNONYM_OR_NEAR]:** HOUND, SHADOW, TAIL, TRACK
* **Level 1 (SPORTSMANLIKE) [Type: SYNONYM_OR_NEAR]:** FAIR, HONEST, SPORTING, SQUARE
* **Level 2 (CLASSIC KID GIFTS) [Type: SEMANTIC_SET]:** BIKE, BOOK, TOY, VIDEO GAME
* **Level 3 ("___ GIRL" TITLES) [Type: FILL_IN_THE_BLANK]:** GONE, GOSSIP, NEW, WORKING

### Top Candidate Partitions:
1. **Partition Score: 0.5005**
   - Group 1: **0.5556** | TAIL, SHADOW, TRACK, GOSSIP                                       | INCORRECT (Max overlap: 3/4 with PURSUE)
   - Group 2: **0.5254** | BOOK, NEW, FAIR, HONEST                                           | INCORRECT (Max overlap: 2/4 with SPORTSMANLIKE) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 28.0%)]
   - Group 3: **0.5086** | VIDEO GAME, HOUND, BIKE, SPORTING                                 | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 4: **0.4764** | SQUARE, WORKING, TOY, GONE                                        | INCORRECT (Max overlap: 2/4 with "___ GIRL" TITLES)
2. **Partition Score: 0.4994**
   - Group 1: **0.6007** | SQUARE, NEW, FAIR, HONEST                                         | INCORRECT (Max overlap: 3/4 with SPORTSMANLIKE) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 36.3%)]
   - Group 2: **0.5556** | TAIL, SHADOW, TRACK, GOSSIP                                       | INCORRECT (Max overlap: 3/4 with PURSUE)
   - Group 3: **0.5086** | VIDEO GAME, HOUND, BIKE, SPORTING                                 | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 4: **0.4532** | BOOK, WORKING, TOY, GONE                                          | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
3. **Partition Score: 0.4971**
   - Group 1: **0.6007** | SQUARE, NEW, FAIR, HONEST                                         | INCORRECT (Max overlap: 3/4 with SPORTSMANLIKE) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 36.3%)]
   - Group 2: **0.5086** | VIDEO GAME, HOUND, BIKE, SPORTING                                 | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 3: **0.4998** | BOOK, TRACK, TOY, GOSSIP                                          | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 4: **0.4693** | TAIL, WORKING, SHADOW, GONE                                       | INCORRECT (Max overlap: 2/4 with PURSUE) | [Pred Type: SYNONYM_OR_NEAR (56.0%, no-rel 28.8%)]
4. **Partition Score: 0.4962**
   - Group 1: **0.6007** | SQUARE, NEW, FAIR, HONEST                                         | INCORRECT (Max overlap: 3/4 with SPORTSMANLIKE) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 36.3%)]
   - Group 2: **0.5099** | BOOK, TAIL, TRACK, GOSSIP                                         | INCORRECT (Max overlap: 2/4 with PURSUE)
   - Group 3: **0.5086** | VIDEO GAME, HOUND, BIKE, SPORTING                                 | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 4: **0.4637** | WORKING, SHADOW, TOY, GONE                                        | INCORRECT (Max overlap: 2/4 with "___ GIRL" TITLES)
5. **Partition Score: 0.4921**
   - Group 1: **0.6007** | SQUARE, NEW, FAIR, HONEST                                         | INCORRECT (Max overlap: 3/4 with SPORTSMANLIKE) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 36.3%)]
   - Group 2: **0.5086** | VIDEO GAME, HOUND, BIKE, SPORTING                                 | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 3: **0.4915** | BOOK, WORKING, TRACK, TOY                                         | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 4: **0.4625** | TAIL, SHADOW, GONE, GOSSIP                                        | INCORRECT (Max overlap: 2/4 with PURSUE) | [Pred Type: SYNONYM_OR_NEAR (49.3%, no-rel 30.8%)]

### Top Candidate Groups:
   - Group 1: **0.5556** | TAIL, SHADOW, TRACK, GOSSIP                                       | INCORRECT (Max overlap: 3/4 with PURSUE)
   - Group 2: **0.5254** | BOOK, NEW, FAIR, HONEST                                           | INCORRECT (Max overlap: 2/4 with SPORTSMANLIKE) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 28.0%)]
   - Group 3: **0.5086** | VIDEO GAME, HOUND, BIKE, SPORTING                                 | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 4: **0.4764** | SQUARE, WORKING, TOY, GONE                                        | INCORRECT (Max overlap: 2/4 with "___ GIRL" TITLES)
   - Group 5: **0.6007** | SQUARE, NEW, FAIR, HONEST                                         | INCORRECT (Max overlap: 3/4 with SPORTSMANLIKE) | [Pred Type: SYNONYM_OR_NEAR (55.6%, no-rel 36.3%)]
   - Group 6: **0.4532** | BOOK, WORKING, TOY, GONE                                          | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 7: **0.4998** | BOOK, TRACK, TOY, GOSSIP                                          | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 8: **0.4693** | TAIL, WORKING, SHADOW, GONE                                       | INCORRECT (Max overlap: 2/4 with PURSUE) | [Pred Type: SYNONYM_OR_NEAR (56.0%, no-rel 28.8%)]
   - Group 9: **0.5099** | BOOK, TAIL, TRACK, GOSSIP                                         | INCORRECT (Max overlap: 2/4 with PURSUE)
   - Group 10: **0.4637** | WORKING, SHADOW, TOY, GONE                                        | INCORRECT (Max overlap: 2/4 with "___ GIRL" TITLES)
   - Group 11: **0.4915** | BOOK, WORKING, TRACK, TOY                                         | INCORRECT (Max overlap: 2/4 with CLASSIC KID GIFTS)
   - Group 12: **0.4625** | TAIL, SHADOW, GONE, GOSSIP                                        | INCORRECT (Max overlap: 2/4 with PURSUE) | [Pred Type: SYNONYM_OR_NEAR (49.3%, no-rel 30.8%)]
   - Group 13: **0.5177** | BOOK, TAIL, SHADOW, TRACK                                         | INCORRECT (Max overlap: 3/4 with PURSUE)
   - Group 14: **0.4514** | WORKING, TOY, GONE, GOSSIP                                        | INCORRECT (Max overlap: 3/4 with "___ GIRL" TITLES)
   - Group 15: **0.4922** | BOOK, TAIL, SHADOW, GOSSIP                                        | INCORRECT (Max overlap: 2/4 with PURSUE)
   - Group 16: **0.4600** | WORKING, TRACK, TOY, GONE                                         | INCORRECT (Max overlap: 2/4 with "___ GIRL" TITLES)
   - Group 17: **0.6014** | TAIL, TRACK, TOY, GOSSIP                                          | INCORRECT (Max overlap: 2/4 with PURSUE)
   - Group 18: **0.4185** | BOOK, WORKING, SHADOW, GONE                                       | INCORRECT (Max overlap: 2/4 with "___ GIRL" TITLES)
   - Group 19: **0.5092** | VIDEO GAME, HOUND, SPORTING, GOSSIP                               | INCORRECT (Max overlap: 1/4 with CLASSIC KID GIFTS)
   - Group 20: **0.4651** | BOOK, BIKE, TRACK, TOY                                            | INCORRECT (Max overlap: 3/4 with CLASSIC KID GIFTS)

---

## Puzzle 101 (ID: 1092)
**Words on Board:** COPY EDITOR, PACK RAT, MIRROR SELFIE, BED HEAD, BANK TELLER, CHARM BRACELET, SCHOOL DAYS, PRIDE ROCK, CURSE WORD, QUOTE UNQUOTE, ECHO PARK, DELTA AIRLINES, HEX KEY, SPELL CHECKER, MURDER MYSTERY, MOUTH GUARD

### Ground Truth Categories:
* **Level 0 (STARTING WITH INCANTATIONS) [Type: FILL_IN_THE_BLANK]:** CHARM BRACELET, CURSE WORD, HEX KEY, SPELL CHECKER
* **Level 1 (STARTING WITH ANIMAL GROUP NAMES) [Type: FILL_IN_THE_BLANK]:** MURDER MYSTERY, PACK RAT, PRIDE ROCK, SCHOOL DAYS
* **Level 2 (STARTING WITH SYNONYMS FOR "REPEAT") [Type: FILL_IN_THE_BLANK]:** COPY EDITOR, ECHO PARK, MIRROR SELFIE, QUOTE UNQUOTE
* **Level 3 (STARTING WITH PARTS OF A RIVER) [Type: FILL_IN_THE_BLANK]:** BANK TELLER, BED HEAD, DELTA AIRLINES, MOUTH GUARD

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6219** | MIRROR SELFIE, QUOTE UNQUOTE, HEX KEY, MURDER MYSTERY             | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 2: **0.6174** | CURSE WORD, QUOTE UNQUOTE, HEX KEY, MURDER MYSTERY                | INCORRECT (Max overlap: 2/4 with STARTING WITH INCANTATIONS)
   - Group 3: **0.5945** | CURSE WORD, HEX KEY, SPELL CHECKER, MURDER MYSTERY                | INCORRECT (Max overlap: 3/4 with STARTING WITH INCANTATIONS)
   - Group 4: **0.5934** | QUOTE UNQUOTE, ECHO PARK, HEX KEY, MURDER MYSTERY                 | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 5: **0.5916** | QUOTE UNQUOTE, HEX KEY, SPELL CHECKER, MURDER MYSTERY             | INCORRECT (Max overlap: 2/4 with STARTING WITH INCANTATIONS)
   - Group 6: **0.5896** | MIRROR SELFIE, CURSE WORD, QUOTE UNQUOTE, MURDER MYSTERY          | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 7: **0.5890** | PRIDE ROCK, CURSE WORD, QUOTE UNQUOTE, HEX KEY                    | INCORRECT (Max overlap: 2/4 with STARTING WITH INCANTATIONS)
   - Group 8: **0.5873** | MIRROR SELFIE, CURSE WORD, HEX KEY, MURDER MYSTERY                | INCORRECT (Max overlap: 2/4 with STARTING WITH INCANTATIONS)
   - Group 9: **0.5839** | PRIDE ROCK, QUOTE UNQUOTE, ECHO PARK, HEX KEY                     | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 10: **0.5837** | MIRROR SELFIE, CURSE WORD, QUOTE UNQUOTE, HEX KEY                 | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 11: **0.5828** | CURSE WORD, QUOTE UNQUOTE, SPELL CHECKER, MURDER MYSTERY          | INCORRECT (Max overlap: 2/4 with STARTING WITH INCANTATIONS)
   - Group 12: **0.5827** | MIRROR SELFIE, PRIDE ROCK, QUOTE UNQUOTE, HEX KEY                 | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 13: **0.5824** | MIRROR SELFIE, HEX KEY, SPELL CHECKER, MURDER MYSTERY             | INCORRECT (Max overlap: 2/4 with STARTING WITH INCANTATIONS)
   - Group 14: **0.5809** | CURSE WORD, QUOTE UNQUOTE, HEX KEY, SPELL CHECKER                 | INCORRECT (Max overlap: 3/4 with STARTING WITH INCANTATIONS)
   - Group 15: **0.5796** | MIRROR SELFIE, QUOTE UNQUOTE, SPELL CHECKER, MURDER MYSTERY       | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 16: **0.5775** | QUOTE UNQUOTE, DELTA AIRLINES, HEX KEY, MURDER MYSTERY            | INCORRECT (Max overlap: 1/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 17: **0.5773** | CHARM BRACELET, QUOTE UNQUOTE, HEX KEY, MURDER MYSTERY            | INCORRECT (Max overlap: 2/4 with STARTING WITH INCANTATIONS)
   - Group 18: **0.5763** | MIRROR SELFIE, PRIDE ROCK, CURSE WORD, QUOTE UNQUOTE              | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 19: **0.5759** | MIRROR SELFIE, CHARM BRACELET, QUOTE UNQUOTE, MURDER MYSTERY      | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")
   - Group 20: **0.5745** | MIRROR SELFIE, QUOTE UNQUOTE, HEX KEY, SPELL CHECKER              | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "REPEAT")

---

## Puzzle 102 (ID: 111)
**Words on Board:** ACHE, LONG, CLUB, DIAMOND, IRON, LOW, SHORT, THIRST, HEART, PINE, WANTING, SPADE, WOOD, PUTTER, SHY, WEDGE

### Ground Truth Categories:
* **Level 0 (PLAYING CARD SUITS) [Type: NAMED_ENTITY_SET]:** CLUB, DIAMOND, HEART, SPADE
* **Level 1 (GOLF CLUBS) [Type: NAMED_ENTITY_SET]:** IRON, PUTTER, WEDGE, WOOD
* **Level 2 (YEARN) [Type: SYNONYM_OR_NEAR]:** ACHE, LONG, PINE, THIRST
* **Level 3 (INSUFFICIENT) [Type: SYNONYM_OR_NEAR]:** LOW, SHORT, SHY, WANTING

### Top Candidate Partitions:
1. **Partition Score: 0.5241**
   - Group 1: **0.6875** | CLUB, DIAMOND, HEART, SPADE                                       | CORRECT GROUP (PLAYING CARD SUITS, Level 0)
   - Group 2: **0.5343** | LOW, SHORT, WANTING, SHY                                          | CORRECT GROUP (INSUFFICIENT, Level 3) | [Pred Type: SYNONYM_OR_NEAR (48.5%, no-rel 29.8%)]
   - Group 3: **0.5069** | IRON, WOOD, PUTTER, WEDGE                                         | CORRECT GROUP (GOLF CLUBS, Level 1)
   - Group 4: **0.4908** | ACHE, LONG, THIRST, PINE                                          | CORRECT GROUP (YEARN, Level 2) | [Pred Type: SYNONYM_OR_NEAR (69.4%, no-rel 19.7%)]
2. **Partition Score: 0.5160**
   - Group 1: **0.6875** | CLUB, DIAMOND, HEART, SPADE                                       | CORRECT GROUP (PLAYING CARD SUITS, Level 0)
   - Group 2: **0.5599** | LONG, LOW, SHORT, SHY                                             | INCORRECT (Max overlap: 3/4 with INSUFFICIENT)
   - Group 3: **0.5069** | IRON, WOOD, PUTTER, WEDGE                                         | CORRECT GROUP (GOLF CLUBS, Level 1)
   - Group 4: **0.4657** | ACHE, THIRST, PINE, WANTING                                       | INCORRECT (Max overlap: 3/4 with YEARN) | [Pred Type: SYNONYM_OR_NEAR (71.8%, no-rel 18.0%)]
3. **Partition Score: 0.4920**
   - Group 1: **0.6875** | CLUB, DIAMOND, HEART, SPADE                                       | CORRECT GROUP (PLAYING CARD SUITS, Level 0)
   - Group 2: **0.5884** | LONG, LOW, SHORT, WANTING                                         | INCORRECT (Max overlap: 3/4 with INSUFFICIENT)
   - Group 3: **0.5069** | IRON, WOOD, PUTTER, WEDGE                                         | CORRECT GROUP (GOLF CLUBS, Level 1)
   - Group 4: **0.4084** | ACHE, THIRST, PINE, SHY                                           | INCORRECT (Max overlap: 3/4 with YEARN) | [Pred Type: SYNONYM_OR_NEAR (70.2%, no-rel 15.9%)]
4. **Partition Score: 0.4886**
   - Group 1: **0.6875** | CLUB, DIAMOND, HEART, SPADE                                       | CORRECT GROUP (PLAYING CARD SUITS, Level 0)
   - Group 2: **0.5884** | LONG, LOW, SHORT, WANTING                                         | INCORRECT (Max overlap: 3/4 with INSUFFICIENT)
   - Group 3: **0.4339** | ACHE, THIRST, PINE, WOOD                                          | INCORRECT (Max overlap: 3/4 with YEARN) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 18.0%)]
   - Group 4: **0.4285** | IRON, PUTTER, SHY, WEDGE                                          | INCORRECT (Max overlap: 3/4 with GOLF CLUBS) | [Pred Type: SYNONYM_OR_NEAR (46.3%, no-rel 26.8%)]
5. **Partition Score: 0.4869**
   - Group 1: **0.6875** | CLUB, DIAMOND, HEART, SPADE                                       | CORRECT GROUP (PLAYING CARD SUITS, Level 0)
   - Group 2: **0.5599** | LONG, LOW, SHORT, SHY                                             | INCORRECT (Max overlap: 3/4 with INSUFFICIENT)
   - Group 3: **0.4383** | IRON, WANTING, PUTTER, WEDGE                                      | INCORRECT (Max overlap: 3/4 with GOLF CLUBS) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 28.6%)]
   - Group 4: **0.4339** | ACHE, THIRST, PINE, WOOD                                          | INCORRECT (Max overlap: 3/4 with YEARN) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 18.0%)]

### Top Candidate Groups:
   - Group 1: **0.6875** | CLUB, DIAMOND, HEART, SPADE                                       | CORRECT GROUP (PLAYING CARD SUITS, Level 0)
   - Group 2: **0.5343** | LOW, SHORT, WANTING, SHY                                          | CORRECT GROUP (INSUFFICIENT, Level 3) | [Pred Type: SYNONYM_OR_NEAR (48.5%, no-rel 29.8%)]
   - Group 3: **0.5069** | IRON, WOOD, PUTTER, WEDGE                                         | CORRECT GROUP (GOLF CLUBS, Level 1)
   - Group 4: **0.4908** | ACHE, LONG, THIRST, PINE                                          | CORRECT GROUP (YEARN, Level 2) | [Pred Type: SYNONYM_OR_NEAR (69.4%, no-rel 19.7%)]
   - Group 5: **0.5599** | LONG, LOW, SHORT, SHY                                             | INCORRECT (Max overlap: 3/4 with INSUFFICIENT)
   - Group 6: **0.4657** | ACHE, THIRST, PINE, WANTING                                       | INCORRECT (Max overlap: 3/4 with YEARN) | [Pred Type: SYNONYM_OR_NEAR (71.8%, no-rel 18.0%)]
   - Group 7: **0.5884** | LONG, LOW, SHORT, WANTING                                         | INCORRECT (Max overlap: 3/4 with INSUFFICIENT)
   - Group 8: **0.4084** | ACHE, THIRST, PINE, SHY                                           | INCORRECT (Max overlap: 3/4 with YEARN) | [Pred Type: SYNONYM_OR_NEAR (70.2%, no-rel 15.9%)]
   - Group 9: **0.4339** | ACHE, THIRST, PINE, WOOD                                          | INCORRECT (Max overlap: 3/4 with YEARN) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 18.0%)]
   - Group 10: **0.4285** | IRON, PUTTER, SHY, WEDGE                                          | INCORRECT (Max overlap: 3/4 with GOLF CLUBS) | [Pred Type: SYNONYM_OR_NEAR (46.3%, no-rel 26.8%)]
   - Group 11: **0.4383** | IRON, WANTING, PUTTER, WEDGE                                      | INCORRECT (Max overlap: 3/4 with GOLF CLUBS) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 28.6%)]
   - Group 12: **0.5046** | IRON, SPADE, PUTTER, WEDGE                                        | INCORRECT (Max overlap: 3/4 with GOLF CLUBS)
   - Group 13: **0.4684** | CLUB, DIAMOND, HEART, WOOD                                        | INCORRECT (Max overlap: 3/4 with PLAYING CARD SUITS) | [Pred Type: SEMANTIC_SET (48.7%, no-rel 28.0%)]
   - Group 14: **0.5587** | CLUB, IRON, PUTTER, WEDGE                                         | INCORRECT (Max overlap: 3/4 with GOLF CLUBS)
   - Group 15: **0.4518** | DIAMOND, HEART, SPADE, WOOD                                       | INCORRECT (Max overlap: 3/4 with PLAYING CARD SUITS)
   - Group 16: **0.5085** | CLUB, IRON, WOOD, PUTTER                                          | INCORRECT (Max overlap: 3/4 with GOLF CLUBS)
   - Group 17: **0.4593** | DIAMOND, HEART, SPADE, WEDGE                                      | INCORRECT (Max overlap: 3/4 with PLAYING CARD SUITS)
   - Group 18: **0.4943** | ACHE, LONG, PINE, WANTING                                         | INCORRECT (Max overlap: 3/4 with YEARN) | [Pred Type: SYNONYM_OR_NEAR (65.4%, no-rel 23.3%)]
   - Group 19: **0.4237** | LOW, SHORT, THIRST, SHY                                           | INCORRECT (Max overlap: 3/4 with INSUFFICIENT)
   - Group 20: **0.4579** | LOW, SHORT, THIRST, WANTING                                       | INCORRECT (Max overlap: 3/4 with INSUFFICIENT) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 31.2%)]

---

## Puzzle 103 (ID: 29)
**Words on Board:** LAP, SUBTRACT, SKATE, SOLE, ALLEY, FLY, WASP, MULTIPLY, COPY, TANG, GNAT, ADD, COOL, TETRA, DIVIDE, MOTH

### Ground Truth Categories:
* **Level 0 (WINGED INSECTS) [Type: SEMANTIC_SET]:** FLY, GNAT, MOTH, WASP
* **Level 1 (ARITHMETIC OPERATIONS) [Type: SEMANTIC_SET]:** ADD, DIVIDE, MULTIPLY, SUBTRACT
* **Level 2 (FISH) [Type: SEMANTIC_SET]:** TANG, TETRA, SKATE, SOLE
* **Level 3 (___ CAT) [Type: FILL_IN_THE_BLANK]:** ALLEY, COOL, COPY, LAP

### Top Candidate Partitions:
1. **Partition Score: 0.4918**
   - Group 1: **0.8509** | SUBTRACT, MULTIPLY, ADD, DIVIDE                                   | CORRECT GROUP (ARITHMETIC OPERATIONS, Level 1)
   - Group 2: **0.5082** | ALLEY, WASP, TANG, TETRA                                          | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 3: **0.4384** | LAP, FLY, GNAT, MOTH                                              | INCORRECT (Max overlap: 3/4 with WINGED INSECTS)
   - Group 4: **0.4265** | SKATE, SOLE, COPY, COOL                                           | INCORRECT (Max overlap: 2/4 with FISH)
2. **Partition Score: 0.4883**
   - Group 1: **0.8509** | SUBTRACT, MULTIPLY, ADD, DIVIDE                                   | CORRECT GROUP (ARITHMETIC OPERATIONS, Level 1)
   - Group 2: **0.4826** | ALLEY, TANG, TETRA, MOTH                                          | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 3: **0.4455** | LAP, FLY, WASP, GNAT                                              | INCORRECT (Max overlap: 3/4 with WINGED INSECTS)
   - Group 4: **0.4265** | SKATE, SOLE, COPY, COOL                                           | INCORRECT (Max overlap: 2/4 with FISH)
3. **Partition Score: 0.4860**
   - Group 1: **0.8509** | SUBTRACT, MULTIPLY, ADD, DIVIDE                                   | CORRECT GROUP (ARITHMETIC OPERATIONS, Level 1)
   - Group 2: **0.5904** | FLY, WASP, GNAT, MOTH                                             | CORRECT GROUP (WINGED INSECTS, Level 0) | [Pred Type: SEMANTIC_SET (48.8%, no-rel 20.2%)]
   - Group 3: **0.4265** | SKATE, SOLE, COPY, COOL                                           | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 4: **0.3895** | LAP, ALLEY, TANG, TETRA                                           | INCORRECT (Max overlap: 2/4 with ___ CAT)
4. **Partition Score: 0.4857**
   - Group 1: **0.8509** | SUBTRACT, MULTIPLY, ADD, DIVIDE                                   | CORRECT GROUP (ARITHMETIC OPERATIONS, Level 1)
   - Group 2: **0.4967** | TANG, GNAT, TETRA, MOTH                                           | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 3: **0.4265** | SKATE, SOLE, COPY, COOL                                           | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 4: **0.4232** | LAP, ALLEY, FLY, WASP                                             | INCORRECT (Max overlap: 2/4 with ___ CAT)
5. **Partition Score: 0.4785**
   - Group 1: **0.8509** | SUBTRACT, MULTIPLY, ADD, DIVIDE                                   | CORRECT GROUP (ARITHMETIC OPERATIONS, Level 1)
   - Group 2: **0.4987** | WASP, TANG, TETRA, MOTH                                           | INCORRECT (Max overlap: 2/4 with WINGED INSECTS)
   - Group 3: **0.4265** | SKATE, SOLE, COPY, COOL                                           | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 4: **0.4083** | LAP, ALLEY, FLY, GNAT                                             | INCORRECT (Max overlap: 2/4 with ___ CAT)

### Top Candidate Groups:
   - Group 1: **0.8509** | SUBTRACT, MULTIPLY, ADD, DIVIDE                                   | CORRECT GROUP (ARITHMETIC OPERATIONS, Level 1)
   - Group 2: **0.5082** | ALLEY, WASP, TANG, TETRA                                          | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 3: **0.4384** | LAP, FLY, GNAT, MOTH                                              | INCORRECT (Max overlap: 3/4 with WINGED INSECTS)
   - Group 4: **0.4265** | SKATE, SOLE, COPY, COOL                                           | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 5: **0.4826** | ALLEY, TANG, TETRA, MOTH                                          | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 6: **0.4455** | LAP, FLY, WASP, GNAT                                              | INCORRECT (Max overlap: 3/4 with WINGED INSECTS)
   - Group 7: **0.5904** | FLY, WASP, GNAT, MOTH                                             | CORRECT GROUP (WINGED INSECTS, Level 0) | [Pred Type: SEMANTIC_SET (48.8%, no-rel 20.2%)]
   - Group 8: **0.3895** | LAP, ALLEY, TANG, TETRA                                           | INCORRECT (Max overlap: 2/4 with ___ CAT)
   - Group 9: **0.4967** | TANG, GNAT, TETRA, MOTH                                           | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 10: **0.4232** | LAP, ALLEY, FLY, WASP                                             | INCORRECT (Max overlap: 2/4 with ___ CAT)
   - Group 11: **0.4987** | WASP, TANG, TETRA, MOTH                                           | INCORRECT (Max overlap: 2/4 with WINGED INSECTS)
   - Group 12: **0.4083** | LAP, ALLEY, FLY, GNAT                                             | INCORRECT (Max overlap: 2/4 with ___ CAT)
   - Group 13: **0.4813** | ALLEY, TANG, GNAT, TETRA                                          | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 14: **0.4116** | LAP, FLY, WASP, MOTH                                              | INCORRECT (Max overlap: 3/4 with WINGED INSECTS)
   - Group 15: **0.5430** | SUBTRACT, MULTIPLY, COPY, ADD                                     | INCORRECT (Max overlap: 3/4 with ARITHMETIC OPERATIONS)
   - Group 16: **0.4493** | SKATE, SOLE, COOL, DIVIDE                                         | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 17: **0.3946** | FLY, GNAT, COOL, MOTH                                             | INCORRECT (Max overlap: 3/4 with WINGED INSECTS) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 16.8%)]
   - Group 18: **0.3890** | LAP, SKATE, SOLE, COPY                                            | INCORRECT (Max overlap: 2/4 with ___ CAT)
   - Group 19: **0.4040** | FLY, WASP, GNAT, COOL                                             | INCORRECT (Max overlap: 3/4 with WINGED INSECTS)
   - Group 20: **0.5200** | SUBTRACT, ADD, COOL, DIVIDE                                       | INCORRECT (Max overlap: 3/4 with ARITHMETIC OPERATIONS)

---

## Puzzle 104 (ID: 512)
**Words on Board:** BEING, STOCK, SHELL, WERE, CONSOLE, CHEST, OUTFIT, CANT, VANITY, WARDROBE, EGO, CHARACTER, PROVISION, SELF, ID, FURNISH

### Ground Truth Categories:
* **Level 0 (EQUIP) [Type: SYNONYM_OR_NEAR]:** FURNISH, OUTFIT, PROVISION, STOCK
* **Level 1 (INDIVIDUALITY) [Type: SYNONYM_OR_NEAR]:** BEING, CHARACTER, EGO, SELF
* **Level 2 (FURNITURE) [Type: SEMANTIC_SET]:** CHEST, CONSOLE, VANITY, WARDROBE
* **Level 3 (WORDS WITH APOSTROPHES REMOVED) [Type: WORDPLAY_TRANSFORM]:** CANT, ID, SHELL, WERE

### Top Candidate Partitions:
1. **Partition Score: 0.5074**
   - Group 1: **0.8198** | STOCK, OUTFIT, PROVISION, FURNISH                                 | CORRECT GROUP (EQUIP, Level 0)
   - Group 2: **0.5043** | SHELL, CONSOLE, CHEST, WARDROBE                                   | INCORRECT (Max overlap: 3/4 with FURNITURE)
   - Group 3: **0.5008** | BEING, WERE, VANITY, CHARACTER                                    | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (56.4%, no-rel 26.5%)]
   - Group 4: **0.4424** | CANT, EGO, SELF, ID                                               | INCORRECT (Max overlap: 2/4 with WORDS WITH APOSTROPHES REMOVED) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 17.3%)]
2. **Partition Score: 0.5005**
   - Group 1: **0.8198** | STOCK, OUTFIT, PROVISION, FURNISH                                 | CORRECT GROUP (EQUIP, Level 0)
   - Group 2: **0.5043** | SHELL, CONSOLE, CHEST, WARDROBE                                   | INCORRECT (Max overlap: 3/4 with FURNITURE)
   - Group 3: **0.4702** | EGO, CHARACTER, SELF, ID                                          | INCORRECT (Max overlap: 3/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 27.7%)]
   - Group 4: **0.4401** | BEING, WERE, CANT, VANITY                                         | INCORRECT (Max overlap: 2/4 with WORDS WITH APOSTROPHES REMOVED) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 20.7%)]
3. **Partition Score: 0.4991**
   - Group 1: **0.8198** | STOCK, OUTFIT, PROVISION, FURNISH                                 | CORRECT GROUP (EQUIP, Level 0)
   - Group 2: **0.5043** | SHELL, CONSOLE, CHEST, WARDROBE                                   | INCORRECT (Max overlap: 3/4 with FURNITURE)
   - Group 3: **0.4881** | VANITY, EGO, SELF, ID                                             | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 19.5%)]
   - Group 4: **0.4308** | BEING, WERE, CANT, CHARACTER                                      | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 21.9%)]
4. **Partition Score: 0.4947**
   - Group 1: **0.8198** | STOCK, OUTFIT, PROVISION, FURNISH                                 | CORRECT GROUP (EQUIP, Level 0)
   - Group 2: **0.5043** | SHELL, CONSOLE, CHEST, WARDROBE                                   | INCORRECT (Max overlap: 3/4 with FURNITURE)
   - Group 3: **0.4536** | VANITY, EGO, CHARACTER, ID                                        | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY)
   - Group 4: **0.4348** | BEING, WERE, CANT, SELF                                           | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 18.4%)]
5. **Partition Score: 0.4915**
   - Group 1: **0.8198** | STOCK, OUTFIT, PROVISION, FURNISH                                 | CORRECT GROUP (EQUIP, Level 0)
   - Group 2: **0.4702** | EGO, CHARACTER, SELF, ID                                          | INCORRECT (Max overlap: 3/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 27.7%)]
   - Group 3: **0.4598** | SHELL, CONSOLE, CHEST, CANT                                       | INCORRECT (Max overlap: 2/4 with WORDS WITH APOSTROPHES REMOVED)
   - Group 4: **0.4388** | BEING, WERE, VANITY, WARDROBE                                     | INCORRECT (Max overlap: 2/4 with FURNITURE) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 18.4%)]

### Top Candidate Groups:
   - Group 1: **0.8198** | STOCK, OUTFIT, PROVISION, FURNISH                                 | CORRECT GROUP (EQUIP, Level 0)
   - Group 2: **0.5043** | SHELL, CONSOLE, CHEST, WARDROBE                                   | INCORRECT (Max overlap: 3/4 with FURNITURE)
   - Group 3: **0.5008** | BEING, WERE, VANITY, CHARACTER                                    | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (56.4%, no-rel 26.5%)]
   - Group 4: **0.4424** | CANT, EGO, SELF, ID                                               | INCORRECT (Max overlap: 2/4 with WORDS WITH APOSTROPHES REMOVED) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 17.3%)]
   - Group 5: **0.4702** | EGO, CHARACTER, SELF, ID                                          | INCORRECT (Max overlap: 3/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 27.7%)]
   - Group 6: **0.4401** | BEING, WERE, CANT, VANITY                                         | INCORRECT (Max overlap: 2/4 with WORDS WITH APOSTROPHES REMOVED) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 20.7%)]
   - Group 7: **0.4881** | VANITY, EGO, SELF, ID                                             | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 19.5%)]
   - Group 8: **0.4308** | BEING, WERE, CANT, CHARACTER                                      | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 21.9%)]
   - Group 9: **0.4536** | VANITY, EGO, CHARACTER, ID                                        | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY)
   - Group 10: **0.4348** | BEING, WERE, CANT, SELF                                           | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 18.4%)]
   - Group 11: **0.4598** | SHELL, CONSOLE, CHEST, CANT                                       | INCORRECT (Max overlap: 2/4 with WORDS WITH APOSTROPHES REMOVED)
   - Group 12: **0.4388** | BEING, WERE, VANITY, WARDROBE                                     | INCORRECT (Max overlap: 2/4 with FURNITURE) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 18.4%)]
   - Group 13: **0.4273** | WARDROBE, EGO, SELF, ID                                           | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (47.3%, no-rel 18.0%)]
   - Group 14: **0.4313** | BEING, WERE, WARDROBE, CHARACTER                                  | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 18.9%)]
   - Group 15: **0.4392** | WERE, EGO, SELF, ID                                               | INCORRECT (Max overlap: 2/4 with WORDS WITH APOSTROPHES REMOVED) | [Pred Type: SYNONYM_OR_NEAR (62.8%, no-rel 18.8%)]
   - Group 16: **0.4325** | BEING, CANT, VANITY, CHARACTER                                    | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 21.3%)]
   - Group 17: **0.4479** | BEING, VANITY, WARDROBE, CHARACTER                                | INCORRECT (Max overlap: 2/4 with INDIVIDUALITY)
   - Group 18: **0.4816** | BEING, WERE, CHARACTER, SELF                                      | INCORRECT (Max overlap: 3/4 with INDIVIDUALITY) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 26.1%)]
   - Group 19: **0.4245** | VANITY, WARDROBE, EGO, ID                                         | INCORRECT (Max overlap: 2/4 with FURNITURE) | [Pred Type: SEMANTIC_SET (51.4%, no-rel 16.9%)]
   - Group 20: **0.4671** | SHELL, CONSOLE, CANT, WARDROBE                                    | INCORRECT (Max overlap: 2/4 with WORDS WITH APOSTROPHES REMOVED)

---

## Puzzle 105 (ID: 1081)
**Words on Board:** ONION, TREE, CEILING, MENAGERIE, ROBE, WALL, PIPE, SLIPPERS, WINDOW, TATTOO, DOOR, CAT, STREETCAR, NEWSPAPER, KEY, WEDDING

### Ground Truth Categories:
* **Level 0 (ROOM FEATURES) [Type: SEMANTIC_SET]:** CEILING, DOOR, WALL, WINDOW
* **Level 1 (OLD-TIMEY LOUNGING ACCESSORIES) [Type: SEMANTIC_SET]:** NEWSPAPER, PIPE, ROBE, SLIPPERS
* **Level 2 (SUBJECTS IN TENNESSEE WILLIAMS TITLES) [Type: NAMED_ENTITY_SET]:** STREETCAR, CAT, MENAGERIE, TATTOO
* **Level 3 (___ RING) [Type: FILL_IN_THE_BLANK]:** KEY, ONION, TREE, WEDDING

### Top Candidate Partitions:
1. **Partition Score: 0.4400**
   - Group 1: **0.5281** | CEILING, WALL, WINDOW, DOOR                                       | CORRECT GROUP (ROOM FEATURES, Level 0) | [Pred Type: SEMANTIC_SET (53.7%, no-rel 30.3%)]
   - Group 2: **0.4804** | ONION, TREE, PIPE, CAT                                            | INCORRECT (Max overlap: 2/4 with ___ RING)
   - Group 3: **0.4200** | MENAGERIE, SLIPPERS, STREETCAR, NEWSPAPER                         | INCORRECT (Max overlap: 2/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
   - Group 4: **0.4131** | ROBE, TATTOO, KEY, WEDDING                                        | INCORRECT (Max overlap: 2/4 with ___ RING)
2. **Partition Score: 0.4362**
   - Group 1: **0.5281** | CEILING, WALL, WINDOW, DOOR                                       | CORRECT GROUP (ROOM FEATURES, Level 0) | [Pred Type: SEMANTIC_SET (53.7%, no-rel 30.3%)]
   - Group 2: **0.4338** | ONION, MENAGERIE, SLIPPERS, NEWSPAPER                             | INCORRECT (Max overlap: 2/4 with OLD-TIMEY LOUNGING ACCESSORIES)
   - Group 3: **0.4334** | TREE, ROBE, KEY, WEDDING                                          | INCORRECT (Max overlap: 3/4 with ___ RING)
   - Group 4: **0.4179** | PIPE, TATTOO, CAT, STREETCAR                                      | INCORRECT (Max overlap: 3/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
3. **Partition Score: 0.4355**
   - Group 1: **0.4804** | ONION, TREE, PIPE, CAT                                            | INCORRECT (Max overlap: 2/4 with ___ RING)
   - Group 2: **0.4656** | WALL, WINDOW, DOOR, KEY                                           | INCORRECT (Max overlap: 3/4 with ROOM FEATURES)
   - Group 3: **0.4212** | CEILING, ROBE, TATTOO, WEDDING                                    | INCORRECT (Max overlap: 1/4 with ROOM FEATURES)
   - Group 4: **0.4200** | MENAGERIE, SLIPPERS, STREETCAR, NEWSPAPER                         | INCORRECT (Max overlap: 2/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
4. **Partition Score: 0.4304**
   - Group 1: **0.5281** | CEILING, WALL, WINDOW, DOOR                                       | CORRECT GROUP (ROOM FEATURES, Level 0) | [Pred Type: SEMANTIC_SET (53.7%, no-rel 30.3%)]
   - Group 2: **0.4338** | ONION, MENAGERIE, SLIPPERS, NEWSPAPER                             | INCORRECT (Max overlap: 2/4 with OLD-TIMEY LOUNGING ACCESSORIES)
   - Group 3: **0.4156** | TREE, PIPE, CAT, STREETCAR                                        | INCORRECT (Max overlap: 2/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
   - Group 4: **0.4131** | ROBE, TATTOO, KEY, WEDDING                                        | INCORRECT (Max overlap: 2/4 with ___ RING)
5. **Partition Score: 0.4298**
   - Group 1: **0.4804** | ONION, TREE, PIPE, CAT                                            | INCORRECT (Max overlap: 2/4 with ___ RING)
   - Group 2: **0.4569** | WALL, WINDOW, DOOR, NEWSPAPER                                     | INCORRECT (Max overlap: 3/4 with ROOM FEATURES) | [Pred Type: SEMANTIC_SET (46.6%, no-rel 32.1%)]
   - Group 3: **0.4179** | CEILING, MENAGERIE, SLIPPERS, STREETCAR                           | INCORRECT (Max overlap: 2/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
   - Group 4: **0.4131** | ROBE, TATTOO, KEY, WEDDING                                        | INCORRECT (Max overlap: 2/4 with ___ RING)

### Top Candidate Groups:
   - Group 1: **0.5281** | CEILING, WALL, WINDOW, DOOR                                       | CORRECT GROUP (ROOM FEATURES, Level 0) | [Pred Type: SEMANTIC_SET (53.7%, no-rel 30.3%)]
   - Group 2: **0.4804** | ONION, TREE, PIPE, CAT                                            | INCORRECT (Max overlap: 2/4 with ___ RING)
   - Group 3: **0.4200** | MENAGERIE, SLIPPERS, STREETCAR, NEWSPAPER                         | INCORRECT (Max overlap: 2/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
   - Group 4: **0.4131** | ROBE, TATTOO, KEY, WEDDING                                        | INCORRECT (Max overlap: 2/4 with ___ RING)
   - Group 5: **0.4338** | ONION, MENAGERIE, SLIPPERS, NEWSPAPER                             | INCORRECT (Max overlap: 2/4 with OLD-TIMEY LOUNGING ACCESSORIES)
   - Group 6: **0.4334** | TREE, ROBE, KEY, WEDDING                                          | INCORRECT (Max overlap: 3/4 with ___ RING)
   - Group 7: **0.4179** | PIPE, TATTOO, CAT, STREETCAR                                      | INCORRECT (Max overlap: 3/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
   - Group 8: **0.4656** | WALL, WINDOW, DOOR, KEY                                           | INCORRECT (Max overlap: 3/4 with ROOM FEATURES)
   - Group 9: **0.4212** | CEILING, ROBE, TATTOO, WEDDING                                    | INCORRECT (Max overlap: 1/4 with ROOM FEATURES)
   - Group 10: **0.4156** | TREE, PIPE, CAT, STREETCAR                                        | INCORRECT (Max overlap: 2/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
   - Group 11: **0.4569** | WALL, WINDOW, DOOR, NEWSPAPER                                     | INCORRECT (Max overlap: 3/4 with ROOM FEATURES) | [Pred Type: SEMANTIC_SET (46.6%, no-rel 32.1%)]
   - Group 12: **0.4179** | CEILING, MENAGERIE, SLIPPERS, STREETCAR                           | INCORRECT (Max overlap: 2/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
   - Group 13: **0.4556** | WALL, WINDOW, DOOR, STREETCAR                                     | INCORRECT (Max overlap: 3/4 with ROOM FEATURES) | [Pred Type: SEMANTIC_SET (59.3%, no-rel 20.9%)]
   - Group 14: **0.4297** | TREE, PIPE, CAT, KEY                                              | INCORRECT (Max overlap: 2/4 with ___ RING)
   - Group 15: **0.4074** | ONION, PIPE, TATTOO, CAT                                          | INCORRECT (Max overlap: 2/4 with SUBJECTS IN TENNESSEE WILLIAMS TITLES)
   - Group 16: **0.4431** | TREE, CEILING, PIPE, CAT                                          | INCORRECT (Max overlap: 1/4 with ___ RING)
   - Group 17: **0.4764** | WALL, PIPE, WINDOW, DOOR                                          | INCORRECT (Max overlap: 3/4 with ROOM FEATURES) | [Pred Type: SEMANTIC_SET (48.2%, no-rel 33.5%)]
   - Group 18: **0.4440** | ONION, TREE, CEILING, CAT                                         | INCORRECT (Max overlap: 2/4 with ___ RING)
   - Group 19: **0.5021** | WALL, WINDOW, DOOR, CAT                                           | INCORRECT (Max overlap: 3/4 with ROOM FEATURES)
   - Group 20: **0.4268** | ONION, TREE, CEILING, PIPE                                        | INCORRECT (Max overlap: 2/4 with ___ RING) | [Pred Type: FILL_IN_THE_BLANK (46.7%, no-rel 15.9%)]

---

## Puzzle 106 (ID: 254)
**Words on Board:** DRIP, LEAK, BEAT, DRAG, CHARRED, DROP, WIND, PEE, BORE, DUD, RHYTHM, GLOB, STRING, BRASS, BEAD, TEAR

### Ground Truth Categories:
* **Level 0 (PARTY POOPER) [Type: SYNONYM_OR_NEAR]:** BORE, DRAG, DRIP, DUD
* **Level 1 (MUSICAL SECTIONS) [Type: SEMANTIC_SET]:** BRASS, RHYTHM, STRING, WIND
* **Level 2 (BIT OF LIQUID) [Type: SYNONYM_OR_NEAR]:** BEAD, DROP, GLOB, TEAR
* **Level 3 (VEGETABLE HOMOPHONES) [Type: SOUND_OR_SPELLING]:** BEAT, CHARRED, LEAK, PEE

### Top Candidate Partitions:
1. **Partition Score: 0.4485**
   - Group 1: **0.4656** | CHARRED, DUD, GLOB, BRASS                                         | INCORRECT (Max overlap: 1/4 with VEGETABLE HOMOPHONES)
   - Group 2: **0.4521** | DROP, WIND, STRING, BEAD                                          | INCORRECT (Max overlap: 2/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (46.4%, no-rel 31.2%)]
   - Group 3: **0.4508** | BEAT, DRAG, BORE, RHYTHM                                          | INCORRECT (Max overlap: 2/4 with PARTY POOPER) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 27.8%)]
   - Group 4: **0.4426** | DRIP, LEAK, PEE, TEAR                                             | INCORRECT (Max overlap: 2/4 with VEGETABLE HOMOPHONES)
2. **Partition Score: 0.4389**
   - Group 1: **0.6251** | DRIP, LEAK, DROP, TEAR                                            | INCORRECT (Max overlap: 2/4 with BIT OF LIQUID)
   - Group 2: **0.4508** | BEAT, DRAG, BORE, RHYTHM                                          | INCORRECT (Max overlap: 2/4 with PARTY POOPER) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 27.8%)]
   - Group 3: **0.4388** | CHARRED, PEE, DUD, GLOB                                           | INCORRECT (Max overlap: 2/4 with VEGETABLE HOMOPHONES)
   - Group 4: **0.3937** | WIND, STRING, BRASS, BEAD                                         | INCORRECT (Max overlap: 3/4 with MUSICAL SECTIONS)
3. **Partition Score: 0.4381**
   - Group 1: **0.4541** | DROP, GLOB, BEAD, TEAR                                            | CORRECT GROUP (BIT OF LIQUID, Level 2) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 25.8%)]
   - Group 2: **0.4508** | BEAT, DRAG, BORE, RHYTHM                                          | INCORRECT (Max overlap: 2/4 with PARTY POOPER) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 27.8%)]
   - Group 3: **0.4322** | CHARRED, WIND, STRING, BRASS                                      | INCORRECT (Max overlap: 3/4 with MUSICAL SECTIONS)
   - Group 4: **0.4322** | DRIP, LEAK, PEE, DUD                                              | INCORRECT (Max overlap: 2/4 with PARTY POOPER)
4. **Partition Score: 0.4366**
   - Group 1: **0.4951** | DRIP, DROP, BEAD, TEAR                                            | INCORRECT (Max overlap: 3/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 33.3%)]
   - Group 2: **0.4508** | BEAT, DRAG, BORE, RHYTHM                                          | INCORRECT (Max overlap: 2/4 with PARTY POOPER) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 27.8%)]
   - Group 3: **0.4322** | CHARRED, WIND, STRING, BRASS                                      | INCORRECT (Max overlap: 3/4 with MUSICAL SECTIONS)
   - Group 4: **0.4202** | LEAK, PEE, DUD, GLOB                                              | INCORRECT (Max overlap: 2/4 with VEGETABLE HOMOPHONES)
5. **Partition Score: 0.4360**
   - Group 1: **0.4508** | BEAT, DRAG, BORE, RHYTHM                                          | INCORRECT (Max overlap: 2/4 with PARTY POOPER) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 27.8%)]
   - Group 2: **0.4426** | DRIP, LEAK, PEE, TEAR                                             | INCORRECT (Max overlap: 2/4 with VEGETABLE HOMOPHONES)
   - Group 3: **0.4366** | DROP, GLOB, STRING, BEAD                                          | INCORRECT (Max overlap: 3/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (55.7%, no-rel 19.7%)]
   - Group 4: **0.4301** | CHARRED, WIND, DUD, BRASS                                         | INCORRECT (Max overlap: 2/4 with MUSICAL SECTIONS)

### Top Candidate Groups:
   - Group 1: **0.4656** | CHARRED, DUD, GLOB, BRASS                                         | INCORRECT (Max overlap: 1/4 with VEGETABLE HOMOPHONES)
   - Group 2: **0.4521** | DROP, WIND, STRING, BEAD                                          | INCORRECT (Max overlap: 2/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (46.4%, no-rel 31.2%)]
   - Group 3: **0.4508** | BEAT, DRAG, BORE, RHYTHM                                          | INCORRECT (Max overlap: 2/4 with PARTY POOPER) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 27.8%)]
   - Group 4: **0.4426** | DRIP, LEAK, PEE, TEAR                                             | INCORRECT (Max overlap: 2/4 with VEGETABLE HOMOPHONES)
   - Group 5: **0.6251** | DRIP, LEAK, DROP, TEAR                                            | INCORRECT (Max overlap: 2/4 with BIT OF LIQUID)
   - Group 6: **0.4388** | CHARRED, PEE, DUD, GLOB                                           | INCORRECT (Max overlap: 2/4 with VEGETABLE HOMOPHONES)
   - Group 7: **0.3937** | WIND, STRING, BRASS, BEAD                                         | INCORRECT (Max overlap: 3/4 with MUSICAL SECTIONS)
   - Group 8: **0.4541** | DROP, GLOB, BEAD, TEAR                                            | CORRECT GROUP (BIT OF LIQUID, Level 2) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 25.8%)]
   - Group 9: **0.4322** | CHARRED, WIND, STRING, BRASS                                      | INCORRECT (Max overlap: 3/4 with MUSICAL SECTIONS)
   - Group 10: **0.4322** | DRIP, LEAK, PEE, DUD                                              | INCORRECT (Max overlap: 2/4 with PARTY POOPER)
   - Group 11: **0.4951** | DRIP, DROP, BEAD, TEAR                                            | INCORRECT (Max overlap: 3/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 33.3%)]
   - Group 12: **0.4202** | LEAK, PEE, DUD, GLOB                                              | INCORRECT (Max overlap: 2/4 with VEGETABLE HOMOPHONES)
   - Group 13: **0.4366** | DROP, GLOB, STRING, BEAD                                          | INCORRECT (Max overlap: 3/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (55.7%, no-rel 19.7%)]
   - Group 14: **0.4301** | CHARRED, WIND, DUD, BRASS                                         | INCORRECT (Max overlap: 2/4 with MUSICAL SECTIONS)
   - Group 15: **0.4621** | DROP, WIND, BEAD, TEAR                                            | INCORRECT (Max overlap: 3/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 33.3%)]
   - Group 16: **0.4232** | CHARRED, GLOB, STRING, BRASS                                      | INCORRECT (Max overlap: 2/4 with MUSICAL SECTIONS)
   - Group 17: **0.4219** | DROP, DUD, GLOB, BEAD                                             | INCORRECT (Max overlap: 3/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (59.3%, no-rel 13.8%)]
   - Group 18: **0.4544** | DRAG, DROP, WIND, BEAD                                            | INCORRECT (Max overlap: 2/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (54.0%, no-rel 28.2%)]
   - Group 19: **0.4262** | BEAT, BORE, DUD, RHYTHM                                           | INCORRECT (Max overlap: 2/4 with PARTY POOPER) | [Pred Type: SYNONYM_OR_NEAR (61.9%, no-rel 22.9%)]
   - Group 20: **0.4991** | DROP, STRING, BEAD, TEAR                                          | INCORRECT (Max overlap: 3/4 with BIT OF LIQUID) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 32.3%)]

---

## Puzzle 107 (ID: 637)
**Words on Board:** MICKEY, CENTERFOLD, SERVICE, SOLID, FAVOR, KINDNESS, CONCRETE, ABRACADABRA, MOUSE, METAL, STONE, MICROPHONE, SCANNER, BRICK, TABLET, PHYSICAL

### Ground Truth Categories:
* **Level 0 (COMPUTER INPUT DEVICES) [Type: SEMANTIC_SET]:** MICROPHONE, MOUSE, SCANNER, TABLET
* **Level 1 (BUILDING MATERIALS) [Type: SEMANTIC_SET]:** BRICK, CONCRETE, METAL, STONE
* **Level 2 (HELPFUL DEED) [Type: SYNONYM_OR_NEAR]:** FAVOR, KINDNESS, SERVICE, SOLID
* **Level 3 (#1 SONGS FROM 1982) [Type: NAMED_ENTITY_SET]:** ABRACADABRA, CENTERFOLD, MICKEY, PHYSICAL

### Top Candidate Partitions:
1. **Partition Score: 0.4650**
   - Group 1: **0.7178** | SOLID, CONCRETE, METAL, PHYSICAL                                  | INCORRECT (Max overlap: 2/4 with BUILDING MATERIALS)
   - Group 2: **0.5324** | ABRACADABRA, MICROPHONE, SCANNER, TABLET                          | INCORRECT (Max overlap: 3/4 with COMPUTER INPUT DEVICES)
   - Group 3: **0.4177** | CENTERFOLD, SERVICE, FAVOR, KINDNESS                              | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (54.0%, no-rel 16.9%)]
   - Group 4: **0.4021** | MICKEY, MOUSE, STONE, BRICK                                       | INCORRECT (Max overlap: 2/4 with BUILDING MATERIALS)
2. **Partition Score: 0.4554**
   - Group 1: **0.7178** | SOLID, CONCRETE, METAL, PHYSICAL                                  | INCORRECT (Max overlap: 2/4 with BUILDING MATERIALS)
   - Group 2: **0.5420** | CENTERFOLD, ABRACADABRA, MICROPHONE, SCANNER                      | INCORRECT (Max overlap: 2/4 with #1 SONGS FROM 1982)
   - Group 3: **0.4014** | SERVICE, FAVOR, KINDNESS, MOUSE                                   | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 26.1%)]
   - Group 4: **0.3858** | MICKEY, STONE, BRICK, TABLET                                      | INCORRECT (Max overlap: 2/4 with BUILDING MATERIALS)
3. **Partition Score: 0.4491**
   - Group 1: **0.5708** | CONCRETE, METAL, STONE, BRICK                                     | CORRECT GROUP (BUILDING MATERIALS, Level 1)
   - Group 2: **0.4594** | SERVICE, SOLID, FAVOR, PHYSICAL                                   | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (48.9%, no-rel 35.5%)]
   - Group 3: **0.4420** | MICKEY, MOUSE, SCANNER, TABLET                                    | INCORRECT (Max overlap: 3/4 with COMPUTER INPUT DEVICES)
   - Group 4: **0.4212** | CENTERFOLD, KINDNESS, ABRACADABRA, MICROPHONE                     | INCORRECT (Max overlap: 2/4 with #1 SONGS FROM 1982)
4. **Partition Score: 0.4477**
   - Group 1: **0.5324** | ABRACADABRA, MICROPHONE, SCANNER, TABLET                          | INCORRECT (Max overlap: 3/4 with COMPUTER INPUT DEVICES)
   - Group 2: **0.4739** | MICKEY, CONCRETE, STONE, BRICK                                    | INCORRECT (Max overlap: 3/4 with BUILDING MATERIALS)
   - Group 3: **0.4524** | SOLID, MOUSE, METAL, PHYSICAL                                     | INCORRECT (Max overlap: 1/4 with HELPFUL DEED)
   - Group 4: **0.4177** | CENTERFOLD, SERVICE, FAVOR, KINDNESS                              | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (54.0%, no-rel 16.9%)]
5. **Partition Score: 0.4472**
   - Group 1: **0.7178** | SOLID, CONCRETE, METAL, PHYSICAL                                  | INCORRECT (Max overlap: 2/4 with BUILDING MATERIALS)
   - Group 2: **0.5420** | CENTERFOLD, ABRACADABRA, MICROPHONE, SCANNER                      | INCORRECT (Max overlap: 2/4 with #1 SONGS FROM 1982)
   - Group 3: **0.3895** | MICKEY, MOUSE, STONE, TABLET                                      | INCORRECT (Max overlap: 2/4 with COMPUTER INPUT DEVICES)
   - Group 4: **0.3742** | SERVICE, FAVOR, KINDNESS, BRICK                                   | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 24.0%)]

### Top Candidate Groups:
   - Group 1: **0.7178** | SOLID, CONCRETE, METAL, PHYSICAL                                  | INCORRECT (Max overlap: 2/4 with BUILDING MATERIALS)
   - Group 2: **0.5324** | ABRACADABRA, MICROPHONE, SCANNER, TABLET                          | INCORRECT (Max overlap: 3/4 with COMPUTER INPUT DEVICES)
   - Group 3: **0.4177** | CENTERFOLD, SERVICE, FAVOR, KINDNESS                              | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (54.0%, no-rel 16.9%)]
   - Group 4: **0.4021** | MICKEY, MOUSE, STONE, BRICK                                       | INCORRECT (Max overlap: 2/4 with BUILDING MATERIALS)
   - Group 5: **0.5420** | CENTERFOLD, ABRACADABRA, MICROPHONE, SCANNER                      | INCORRECT (Max overlap: 2/4 with #1 SONGS FROM 1982)
   - Group 6: **0.4014** | SERVICE, FAVOR, KINDNESS, MOUSE                                   | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 26.1%)]
   - Group 7: **0.3858** | MICKEY, STONE, BRICK, TABLET                                      | INCORRECT (Max overlap: 2/4 with BUILDING MATERIALS)
   - Group 8: **0.5708** | CONCRETE, METAL, STONE, BRICK                                     | CORRECT GROUP (BUILDING MATERIALS, Level 1)
   - Group 9: **0.4594** | SERVICE, SOLID, FAVOR, PHYSICAL                                   | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (48.9%, no-rel 35.5%)]
   - Group 10: **0.4420** | MICKEY, MOUSE, SCANNER, TABLET                                    | INCORRECT (Max overlap: 3/4 with COMPUTER INPUT DEVICES)
   - Group 11: **0.4212** | CENTERFOLD, KINDNESS, ABRACADABRA, MICROPHONE                     | INCORRECT (Max overlap: 2/4 with #1 SONGS FROM 1982)
   - Group 12: **0.4739** | MICKEY, CONCRETE, STONE, BRICK                                    | INCORRECT (Max overlap: 3/4 with BUILDING MATERIALS)
   - Group 13: **0.4524** | SOLID, MOUSE, METAL, PHYSICAL                                     | INCORRECT (Max overlap: 1/4 with HELPFUL DEED)
   - Group 14: **0.3895** | MICKEY, MOUSE, STONE, TABLET                                      | INCORRECT (Max overlap: 2/4 with COMPUTER INPUT DEVICES)
   - Group 15: **0.3742** | SERVICE, FAVOR, KINDNESS, BRICK                                   | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 24.0%)]
   - Group 16: **0.5371** | CONCRETE, METAL, BRICK, PHYSICAL                                  | INCORRECT (Max overlap: 3/4 with BUILDING MATERIALS)
   - Group 17: **0.4503** | SERVICE, SOLID, FAVOR, KINDNESS                                   | CORRECT GROUP (HELPFUL DEED, Level 2) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 28.6%)]
   - Group 18: **0.5816** | CENTERFOLD, ABRACADABRA, MICROPHONE, TABLET                       | INCORRECT (Max overlap: 2/4 with #1 SONGS FROM 1982)
   - Group 19: **0.3439** | SERVICE, FAVOR, KINDNESS, SCANNER                                 | INCORRECT (Max overlap: 3/4 with HELPFUL DEED) | [Pred Type: SYNONYM_OR_NEAR (53.8%, no-rel 16.4%)]
   - Group 20: **0.5298** | CENTERFOLD, ABRACADABRA, SCANNER, TABLET                          | INCORRECT (Max overlap: 2/4 with #1 SONGS FROM 1982)

---

## Puzzle 108 (ID: 142)
**Words on Board:** VIOLET, ASTER, FARMER, CRAVEN, CARPENTER, LIFE, SPORTS, ROSE, DAISY, DUST, WAN, CHICKEN, BARN, TRACTOR, TULIP, YELLOW

### Ground Truth Categories:
* **Level 0 (FLOWERS) [Type: SEMANTIC_SET]:** DAISY, ROSE, TULIP, VIOLET
* **Level 1 (SEEN ON A FARM) [Type: SEMANTIC_SET]:** BARN, CHICKEN, FARMER, TRACTOR
* **Level 2 (HORROR DIRECTORS) [Type: NAMED_ENTITY_SET]:** ASTER, CARPENTER, CRAVEN, WAN
* **Level 3 (___ JACKET) [Type: FILL_IN_THE_BLANK]:** DUST, LIFE, SPORTS, YELLOW

### Top Candidate Partitions:
1. **Partition Score: 0.4770**
   - Group 1: **0.6160** | FARMER, CHICKEN, BARN, TRACTOR                                    | CORRECT GROUP (SEEN ON A FARM, Level 1)
   - Group 2: **0.5123** | CRAVEN, CARPENTER, ROSE, WAN                                      | INCORRECT (Max overlap: 3/4 with HORROR DIRECTORS)
   - Group 3: **0.4882** | LIFE, SPORTS, DUST, YELLOW                                        | CORRECT GROUP (___ JACKET, Level 3)
   - Group 4: **0.4295** | VIOLET, ASTER, DAISY, TULIP                                       | INCORRECT (Max overlap: 3/4 with FLOWERS)
2. **Partition Score: 0.4708**
   - Group 1: **0.6189** | VIOLET, ROSE, DAISY, TULIP                                        | CORRECT GROUP (FLOWERS, Level 0)
   - Group 2: **0.4882** | LIFE, SPORTS, DUST, YELLOW                                        | CORRECT GROUP (___ JACKET, Level 3)
   - Group 3: **0.4751** | CRAVEN, CARPENTER, WAN, CHICKEN                                   | INCORRECT (Max overlap: 3/4 with HORROR DIRECTORS)
   - Group 4: **0.4304** | ASTER, FARMER, BARN, TRACTOR                                      | INCORRECT (Max overlap: 3/4 with SEEN ON A FARM)
3. **Partition Score: 0.4705**
   - Group 1: **0.6189** | VIOLET, ROSE, DAISY, TULIP                                        | CORRECT GROUP (FLOWERS, Level 0)
   - Group 2: **0.4882** | LIFE, SPORTS, DUST, YELLOW                                        | CORRECT GROUP (___ JACKET, Level 3)
   - Group 3: **0.4423** | ASTER, FARMER, CHICKEN, BARN                                      | INCORRECT (Max overlap: 3/4 with SEEN ON A FARM)
   - Group 4: **0.4417** | CRAVEN, CARPENTER, WAN, TRACTOR                                   | INCORRECT (Max overlap: 3/4 with HORROR DIRECTORS)
4. **Partition Score: 0.4657**
   - Group 1: **0.5908** | FARMER, CARPENTER, BARN, TRACTOR                                  | INCORRECT (Max overlap: 3/4 with SEEN ON A FARM)
   - Group 2: **0.4882** | LIFE, SPORTS, DUST, YELLOW                                        | CORRECT GROUP (___ JACKET, Level 3)
   - Group 3: **0.4673** | CRAVEN, ROSE, WAN, CHICKEN                                        | INCORRECT (Max overlap: 2/4 with HORROR DIRECTORS)
   - Group 4: **0.4295** | VIOLET, ASTER, DAISY, TULIP                                       | INCORRECT (Max overlap: 3/4 with FLOWERS)
5. **Partition Score: 0.4653**
   - Group 1: **0.6189** | VIOLET, ROSE, DAISY, TULIP                                        | CORRECT GROUP (FLOWERS, Level 0)
   - Group 2: **0.4882** | LIFE, SPORTS, DUST, YELLOW                                        | CORRECT GROUP (___ JACKET, Level 3)
   - Group 3: **0.4603** | CRAVEN, CARPENTER, WAN, BARN                                      | INCORRECT (Max overlap: 3/4 with HORROR DIRECTORS)
   - Group 4: **0.4250** | ASTER, FARMER, CHICKEN, TRACTOR                                   | INCORRECT (Max overlap: 3/4 with SEEN ON A FARM)

### Top Candidate Groups:
   - Group 1: **0.6160** | FARMER, CHICKEN, BARN, TRACTOR                                    | CORRECT GROUP (SEEN ON A FARM, Level 1)
   - Group 2: **0.5123** | CRAVEN, CARPENTER, ROSE, WAN                                      | INCORRECT (Max overlap: 3/4 with HORROR DIRECTORS)
   - Group 3: **0.4882** | LIFE, SPORTS, DUST, YELLOW                                        | CORRECT GROUP (___ JACKET, Level 3)
   - Group 4: **0.4295** | VIOLET, ASTER, DAISY, TULIP                                       | INCORRECT (Max overlap: 3/4 with FLOWERS)
   - Group 5: **0.6189** | VIOLET, ROSE, DAISY, TULIP                                        | CORRECT GROUP (FLOWERS, Level 0)
   - Group 6: **0.4751** | CRAVEN, CARPENTER, WAN, CHICKEN                                   | INCORRECT (Max overlap: 3/4 with HORROR DIRECTORS)
   - Group 7: **0.4304** | ASTER, FARMER, BARN, TRACTOR                                      | INCORRECT (Max overlap: 3/4 with SEEN ON A FARM)
   - Group 8: **0.4423** | ASTER, FARMER, CHICKEN, BARN                                      | INCORRECT (Max overlap: 3/4 with SEEN ON A FARM)
   - Group 9: **0.4417** | CRAVEN, CARPENTER, WAN, TRACTOR                                   | INCORRECT (Max overlap: 3/4 with HORROR DIRECTORS)
   - Group 10: **0.5908** | FARMER, CARPENTER, BARN, TRACTOR                                  | INCORRECT (Max overlap: 3/4 with SEEN ON A FARM)
   - Group 11: **0.4673** | CRAVEN, ROSE, WAN, CHICKEN                                        | INCORRECT (Max overlap: 2/4 with HORROR DIRECTORS)
   - Group 12: **0.4603** | CRAVEN, CARPENTER, WAN, BARN                                      | INCORRECT (Max overlap: 3/4 with HORROR DIRECTORS)
   - Group 13: **0.4250** | ASTER, FARMER, CHICKEN, TRACTOR                                   | INCORRECT (Max overlap: 3/4 with SEEN ON A FARM)
   - Group 14: **0.4650** | CRAVEN, WAN, CHICKEN, BARN                                        | INCORRECT (Max overlap: 2/4 with HORROR DIRECTORS)
   - Group 15: **0.4225** | ASTER, FARMER, CARPENTER, TRACTOR                                 | INCORRECT (Max overlap: 2/4 with HORROR DIRECTORS)
   - Group 16: **0.4237** | CRAVEN, LIFE, SPORTS, DUST                                        | INCORRECT (Max overlap: 3/4 with ___ JACKET)
   - Group 17: **0.3992** | ASTER, WAN, CHICKEN, YELLOW                                       | INCORRECT (Max overlap: 2/4 with HORROR DIRECTORS)
   - Group 18: **0.4125** | LIFE, SPORTS, DUST, WAN                                           | INCORRECT (Max overlap: 3/4 with ___ JACKET)
   - Group 19: **0.3983** | ASTER, CRAVEN, CHICKEN, YELLOW                                    | INCORRECT (Max overlap: 2/4 with HORROR DIRECTORS)
   - Group 20: **0.5280** | CRAVEN, ROSE, WAN, YELLOW                                         | INCORRECT (Max overlap: 2/4 with HORROR DIRECTORS)

---
