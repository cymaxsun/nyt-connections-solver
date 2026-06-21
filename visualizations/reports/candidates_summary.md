# GCN Subgraph Predictions - All Validation Puzzles

Generated from the current `models/gcn_best.pt` checkpoint loaded by the training pipeline.

This document summarizes the top 5 candidate partitions built from GCN predictions for all 109 validation puzzles. Each group is labeled with exact correctness or maximum overlap with a ground truth category.

## Aggregate Summary

| Metric | Current | Previous | Change vs Prev | All-Time Best | Change vs All-Time |
|---|---:|---:|---:|---:|---:|
| Validation puzzles | 109 | 109 | 0 | 109 | 0 |
| Overall GCN Candidate MRR | 0.1565 | 0.0829 | 🟢 +0.07 (improved) | 0.1565 | 0 |
| Overall Pairwise Relation Accuracy | 77.3% | 80.0% | 🔴 -2.7% (regressed) | 77.3% | 0.0% |
| Overall Group Relation Accuracy | 32.3% | 82.5% | 🔴 -50.2% (regressed) | 32.3% | 0.0% |
| Puzzles with complete partition candidates | 99 / 109 (90.8%) | 50 / 109 (45.9%) | 🟢 +44.9% (improved) | 99 / 109 (90.8%) | 0.0% |
| Top partition solves all 4 groups | 2 / 109 (1.8%) | 2 / 109 (1.8%) | 0.0% | 2 / 109 (1.8%) | 0.0% |
| Any top-5 partition solves all 4 groups | 4 / 109 (3.7%) | 2 / 109 (1.8%) | 🟢 +1.9% (improved) | 4 / 109 (3.7%) | 0.0% |
| Avg correct groups in top partition | 0.61 / 4 | 0.29 / 4 | 🟢 +0.32 (improved) | 0.61 / 4 | 0 |
| Avg best correct groups across top partitions | 0.91 / 4 | 0.38 / 4 | 🟢 +0.53 (improved) | 0.91 / 4 | 0 |
| True groups in top-20 candidates | 134 / 436 (30.7%) | 75 / 436 (17.2%) | 🟢 +13.5% (improved) | 134 / 436 (30.7%) | 0.0% |
| Puzzles with any true group in top-20 | 80 / 109 (73.4%) | 50 / 109 (45.9%) | 🟢 +27.5% (improved) | 80 / 109 (73.4%) | 0.0% |
| Puzzles with all true groups in top-20 | 5 / 109 (4.6%) | 3 / 109 (2.8%) | 🟢 +1.8% (improved) | 5 / 109 (4.6%) | 0.0% |
| Mean rank of true groups found in top-20 | 6.11 | 5.88 | 🔴 +0.23 (regressed) | 6.11 | 0 |
| Median rank of true groups found in top-20 | 3.5 | 3.0 | 🔴 +0.50 (regressed) | 3.5 | 0 |
| 3-of-4 near-miss candidates in top-20 | 859 | 633 | 🟢 +226 (improved) | 859 | 0 |

### Recall By Relation Archetype

| Archetype | True Groups | Hit Top 20 | Recall | Hit Top 5 | Avg Best Rank | Exact MRR | Pairwise Acc | Group Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| COMMON_PHRASE | 3 | 0 | 0.0% | 0 | 0.00 | 0.0038 | 0.0% | 0.0% |
| FILL_IN_THE_BLANK | 44 | 4 | 9.1% | 1 | 7.25 | 0.0052 | 1.9% | 38.6% |
| NAMED_ENTITY_SET | 64 | 8 | 12.5% | 4 | 7.88 | 0.0729 | 2.9% | 39.1% |
| NO_RELATION | 0 | 0 | 0.0% | 0 | 0.00 | 0.0000 | 92.8% | 31.2% |
| SEMANTIC_SET | 142 | 47 | 33.1% | 26 | 7.17 | 0.1332 | 4.1% | 49.3% |
| SOUND_OR_SPELLING | 17 | 3 | 17.6% | 1 | 7.00 | 0.0612 | 18.6% | 17.6% |
| SYNONYM_OR_NEAR | 127 | 68 | 53.5% | 50 | 4.78 | 0.3312 | 41.3% | 78.0% |
| WORDPLAY_TRANSFORM | 29 | 2 | 6.9% | 1 | 10.00 | 0.0388 | 4.0% | 24.1% |
| WORD_FORM | 10 | 2 | 20.0% | 0 | 12.00 | 0.0193 | 18.3% | 20.0% |

---

## Puzzle 0 (ID: 667)
**Words on Board:** PIERCE, JOB, NUMBERS, ROGER, SUGAR, SURE, JAB, POKE, SEAN, COPY, NEGATIVE, SIOBHAN, JUDGES, OVER, DANIEL, STICK

### Ground Truth Categories:
* **Level 0 (PRICK) [Type: SYNONYM_OR_NEAR]:** JAB, PIERCE, POKE, STICK
* **Level 1 (RADIO LINGO) [Type: SEMANTIC_SET]:** COPY, NEGATIVE, OVER, ROGER
* **Level 2 (OLD TESTAMENT BOOKS) [Type: NAMED_ENTITY_SET]:** DANIEL, JOB, JUDGES, NUMBERS
* **Level 3 (WORDS PRONOUNCED “SH” WITHOUT AN “SH”) [Type: SOUND_OR_SPELLING]:** SEAN, SIOBHAN, SUGAR, SURE

### Top Candidate Partitions:
1. **Partition Score: 0.4365**
   - Group 1: **0.6718** | ROGER, SEAN, SIOBHAN, DANIEL                                      | INCORRECT (Max overlap: 2/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”)
   - Group 2: **0.4569** | JOB, NUMBERS, SUGAR, COPY                                         | INCORRECT (Max overlap: 2/4 with OLD TESTAMENT BOOKS) | [Pred Type: FILL_IN_THE_BLANK (49.6%, no-rel 23.8%)]
   - Group 3: **0.4352** | SURE, NEGATIVE, JUDGES, OVER                                      | INCORRECT (Max overlap: 2/4 with RADIO LINGO)
   - Group 4: **0.4270** | PIERCE, JAB, POKE, STICK                                          | CORRECT GROUP (PRICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.1%, no-rel 16.4%)]
2. **Partition Score: 0.4247**
   - Group 1: **0.4834** | ROGER, SUGAR, SEAN, SIOBHAN                                       | INCORRECT (Max overlap: 3/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”)
   - Group 2: **0.4305** | NUMBERS, SURE, NEGATIVE, OVER                                     | INCORRECT (Max overlap: 2/4 with RADIO LINGO)
   - Group 3: **0.4270** | PIERCE, JAB, POKE, STICK                                          | CORRECT GROUP (PRICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.1%, no-rel 16.4%)]
   - Group 4: **0.4207** | JOB, COPY, JUDGES, DANIEL                                         | INCORRECT (Max overlap: 3/4 with OLD TESTAMENT BOOKS)
3. **Partition Score: 0.4233**
   - Group 1: **0.4834** | ROGER, SUGAR, SEAN, SIOBHAN                                       | INCORRECT (Max overlap: 3/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”)
   - Group 2: **0.4746** | JOB, NUMBERS, JUDGES, DANIEL                                      | CORRECT GROUP (OLD TESTAMENT BOOKS, Level 2) | [Pred Type: FILL_IN_THE_BLANK (46.5%, no-rel 14.4%)]
   - Group 3: **0.4270** | PIERCE, JAB, POKE, STICK                                          | CORRECT GROUP (PRICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.1%, no-rel 16.4%)]
   - Group 4: **0.3957** | SURE, COPY, NEGATIVE, OVER                                        | INCORRECT (Max overlap: 3/4 with RADIO LINGO)
4. **Partition Score: 0.4228**
   - Group 1: **0.6718** | ROGER, SEAN, SIOBHAN, DANIEL                                      | INCORRECT (Max overlap: 2/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”)
   - Group 2: **0.4273** | JOB, SURE, COPY, JUDGES                                           | INCORRECT (Max overlap: 2/4 with OLD TESTAMENT BOOKS)
   - Group 3: **0.4270** | PIERCE, JAB, POKE, STICK                                          | CORRECT GROUP (PRICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.1%, no-rel 16.4%)]
   - Group 4: **0.4184** | NUMBERS, SUGAR, NEGATIVE, OVER                                    | INCORRECT (Max overlap: 2/4 with RADIO LINGO)
5. **Partition Score: 0.4219**
   - Group 1: **0.6718** | ROGER, SEAN, SIOBHAN, DANIEL                                      | INCORRECT (Max overlap: 2/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”)
   - Group 2: **0.4305** | NUMBERS, SURE, NEGATIVE, OVER                                     | INCORRECT (Max overlap: 2/4 with RADIO LINGO)
   - Group 3: **0.4270** | PIERCE, JAB, POKE, STICK                                          | CORRECT GROUP (PRICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.1%, no-rel 16.4%)]
   - Group 4: **0.4150** | JOB, SUGAR, COPY, JUDGES                                          | INCORRECT (Max overlap: 2/4 with OLD TESTAMENT BOOKS)

### Top Candidate Groups:
   - Group 1: **0.6718** | ROGER, SEAN, SIOBHAN, DANIEL                                      | INCORRECT (Max overlap: 2/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”)
   - Group 2: **0.4569** | JOB, NUMBERS, SUGAR, COPY                                         | INCORRECT (Max overlap: 2/4 with OLD TESTAMENT BOOKS) | [Pred Type: FILL_IN_THE_BLANK (49.6%, no-rel 23.8%)]
   - Group 3: **0.4352** | SURE, NEGATIVE, JUDGES, OVER                                      | INCORRECT (Max overlap: 2/4 with RADIO LINGO)
   - Group 4: **0.4270** | PIERCE, JAB, POKE, STICK                                          | CORRECT GROUP (PRICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.1%, no-rel 16.4%)]
   - Group 5: **0.4834** | ROGER, SUGAR, SEAN, SIOBHAN                                       | INCORRECT (Max overlap: 3/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”)
   - Group 6: **0.4305** | NUMBERS, SURE, NEGATIVE, OVER                                     | INCORRECT (Max overlap: 2/4 with RADIO LINGO)
   - Group 7: **0.4207** | JOB, COPY, JUDGES, DANIEL                                         | INCORRECT (Max overlap: 3/4 with OLD TESTAMENT BOOKS)
   - Group 8: **0.4746** | JOB, NUMBERS, JUDGES, DANIEL                                      | CORRECT GROUP (OLD TESTAMENT BOOKS, Level 2) | [Pred Type: FILL_IN_THE_BLANK (46.5%, no-rel 14.4%)]
   - Group 9: **0.3957** | SURE, COPY, NEGATIVE, OVER                                        | INCORRECT (Max overlap: 3/4 with RADIO LINGO)
   - Group 10: **0.4273** | JOB, SURE, COPY, JUDGES                                           | INCORRECT (Max overlap: 2/4 with OLD TESTAMENT BOOKS)
   - Group 11: **0.4184** | NUMBERS, SUGAR, NEGATIVE, OVER                                    | INCORRECT (Max overlap: 2/4 with RADIO LINGO)
   - Group 12: **0.4150** | JOB, SUGAR, COPY, JUDGES                                          | INCORRECT (Max overlap: 2/4 with OLD TESTAMENT BOOKS)
   - Group 13: **0.4562** | ROGER, SEAN, SIOBHAN, JUDGES                                      | INCORRECT (Max overlap: 2/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”) | [Pred Type: NAMED_ENTITY_SET (47.6%, no-rel 14.3%)]
   - Group 14: **0.4125** | JOB, SUGAR, COPY, DANIEL                                          | INCORRECT (Max overlap: 2/4 with OLD TESTAMENT BOOKS) | [Pred Type: FILL_IN_THE_BLANK (49.3%, no-rel 17.9%)]
   - Group 15: **0.4210** | JOB, SURE, NEGATIVE, JUDGES                                       | INCORRECT (Max overlap: 2/4 with OLD TESTAMENT BOOKS)
   - Group 16: **0.4171** | NUMBERS, SUGAR, COPY, OVER                                        | INCORRECT (Max overlap: 2/4 with RADIO LINGO) | [Pred Type: FILL_IN_THE_BLANK (51.0%, no-rel 16.9%)]
   - Group 17: **0.4663** | JOB, NUMBERS, COPY, JUDGES                                        | INCORRECT (Max overlap: 3/4 with OLD TESTAMENT BOOKS)
   - Group 18: **0.3933** | SUGAR, SURE, NEGATIVE, OVER                                       | INCORRECT (Max overlap: 2/4 with WORDS PRONOUNCED “SH” WITHOUT AN “SH”)
   - Group 19: **0.4530** | JOB, NUMBERS, SUGAR, JUDGES                                       | INCORRECT (Max overlap: 3/4 with OLD TESTAMENT BOOKS) | [Pred Type: FILL_IN_THE_BLANK (45.3%, no-rel 22.6%)]
   - Group 20: **0.4526** | JOB, NUMBERS, SUGAR, DANIEL                                       | INCORRECT (Max overlap: 3/4 with OLD TESTAMENT BOOKS) | [Pred Type: FILL_IN_THE_BLANK (64.8%, no-rel 11.8%)]

---

## Puzzle 1 (ID: 689)
**Words on Board:** TONGUE, REGARD, ROOM, CAPACITY, STANDING, SOLE, DYNASTY, UPPER, GIMMICK, FACE, IMAGE, SEATING, HEEL, MILDEW, ENGROSS, CHAIRS

### Ground Truth Categories:
* **Level 0 (PARTS OF A SHOE) [Type: SEMANTIC_SET]:** HEEL, SOLE, TONGUE, UPPER
* **Level 1 (ACCOMMODATION) [Type: SEMANTIC_SET]:** CAPACITY, CHAIRS, ROOM, SEATING
* **Level 2 (REPUTATION) [Type: SYNONYM_OR_NEAR]:** FACE, IMAGE, REGARD, STANDING
* **Level 3 (ENDING WITH SYNONYMS FOR “YUCK”) [Type: WORD_FORM]:** DYNASTY, ENGROSS, GIMMICK, MILDEW

### Top Candidate Partitions:
1. **Partition Score: 0.3841**
   - Group 1: **0.4615** | ROOM, STANDING, SEATING, CHAIRS                                   | INCORRECT (Max overlap: 3/4 with ACCOMMODATION) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 29.5%)]
   - Group 2: **0.4194** | SOLE, FACE, IMAGE, HEEL                                           | INCORRECT (Max overlap: 2/4 with PARTS OF A SHOE)
   - Group 3: **0.4170** | TONGUE, DYNASTY, GIMMICK, MILDEW                                  | INCORRECT (Max overlap: 3/4 with ENDING WITH SYNONYMS FOR “YUCK”)
   - Group 4: **0.3500** | REGARD, CAPACITY, UPPER, ENGROSS                                  | INCORRECT (Max overlap: 1/4 with REPUTATION)
2. **Partition Score: 0.3808**
   - Group 1: **0.4615** | ROOM, STANDING, SEATING, CHAIRS                                   | INCORRECT (Max overlap: 3/4 with ACCOMMODATION) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 29.5%)]
   - Group 2: **0.3903** | TONGUE, SOLE, UPPER, ENGROSS                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A SHOE) | [Pred Type: SEMANTIC_SET (56.2%, no-rel 19.5%)]
   - Group 3: **0.3800** | REGARD, FACE, IMAGE, HEEL                                         | INCORRECT (Max overlap: 3/4 with REPUTATION)
   - Group 4: **0.3765** | CAPACITY, DYNASTY, GIMMICK, MILDEW                                | INCORRECT (Max overlap: 3/4 with ENDING WITH SYNONYMS FOR “YUCK”)
3. **Partition Score: 0.3766**
   - Group 1: **0.4615** | ROOM, STANDING, SEATING, CHAIRS                                   | INCORRECT (Max overlap: 3/4 with ACCOMMODATION) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 29.5%)]
   - Group 2: **0.4220** | CAPACITY, DYNASTY, MILDEW, ENGROSS                                | INCORRECT (Max overlap: 3/4 with ENDING WITH SYNONYMS FOR “YUCK”)
   - Group 3: **0.3800** | REGARD, FACE, IMAGE, HEEL                                         | INCORRECT (Max overlap: 3/4 with REPUTATION)
   - Group 4: **0.3522** | TONGUE, SOLE, UPPER, GIMMICK                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A SHOE) | [Pred Type: SEMANTIC_SET (47.4%, no-rel 23.8%)]
4. **Partition Score: 0.3722**
   - Group 1: **0.4194** | SOLE, FACE, IMAGE, HEEL                                           | INCORRECT (Max overlap: 2/4 with PARTS OF A SHOE)
   - Group 2: **0.3926** | REGARD, STANDING, SEATING, CHAIRS                                 | INCORRECT (Max overlap: 2/4 with REPUTATION)
   - Group 3: **0.3709** | CAPACITY, DYNASTY, UPPER, ENGROSS                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH SYNONYMS FOR “YUCK”)
   - Group 4: **0.3626** | TONGUE, ROOM, GIMMICK, MILDEW                                     | INCORRECT (Max overlap: 2/4 with ENDING WITH SYNONYMS FOR “YUCK”)
5. **Partition Score: 0.3696**
   - Group 1: **0.4615** | ROOM, STANDING, SEATING, CHAIRS                                   | INCORRECT (Max overlap: 3/4 with ACCOMMODATION) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 29.5%)]
   - Group 2: **0.4018** | DYNASTY, GIMMICK, MILDEW, ENGROSS                                 | CORRECT GROUP (ENDING WITH SYNONYMS FOR “YUCK”, Level 3)
   - Group 3: **0.3898** | TONGUE, SOLE, FACE, HEEL                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A SHOE)
   - Group 4: **0.3434** | REGARD, CAPACITY, UPPER, IMAGE                                    | INCORRECT (Max overlap: 2/4 with REPUTATION)

### Top Candidate Groups:
   - Group 1: **0.4615** | ROOM, STANDING, SEATING, CHAIRS                                   | INCORRECT (Max overlap: 3/4 with ACCOMMODATION) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 29.5%)]
   - Group 2: **0.4194** | SOLE, FACE, IMAGE, HEEL                                           | INCORRECT (Max overlap: 2/4 with PARTS OF A SHOE)
   - Group 3: **0.4170** | TONGUE, DYNASTY, GIMMICK, MILDEW                                  | INCORRECT (Max overlap: 3/4 with ENDING WITH SYNONYMS FOR “YUCK”)
   - Group 4: **0.3500** | REGARD, CAPACITY, UPPER, ENGROSS                                  | INCORRECT (Max overlap: 1/4 with REPUTATION)
   - Group 5: **0.3903** | TONGUE, SOLE, UPPER, ENGROSS                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A SHOE) | [Pred Type: SEMANTIC_SET (56.2%, no-rel 19.5%)]
   - Group 6: **0.3800** | REGARD, FACE, IMAGE, HEEL                                         | INCORRECT (Max overlap: 3/4 with REPUTATION)
   - Group 7: **0.3765** | CAPACITY, DYNASTY, GIMMICK, MILDEW                                | INCORRECT (Max overlap: 3/4 with ENDING WITH SYNONYMS FOR “YUCK”)
   - Group 8: **0.4220** | CAPACITY, DYNASTY, MILDEW, ENGROSS                                | INCORRECT (Max overlap: 3/4 with ENDING WITH SYNONYMS FOR “YUCK”)
   - Group 9: **0.3522** | TONGUE, SOLE, UPPER, GIMMICK                                      | INCORRECT (Max overlap: 3/4 with PARTS OF A SHOE) | [Pred Type: SEMANTIC_SET (47.4%, no-rel 23.8%)]
   - Group 10: **0.3926** | REGARD, STANDING, SEATING, CHAIRS                                 | INCORRECT (Max overlap: 2/4 with REPUTATION)
   - Group 11: **0.3709** | CAPACITY, DYNASTY, UPPER, ENGROSS                                 | INCORRECT (Max overlap: 2/4 with ENDING WITH SYNONYMS FOR “YUCK”)
   - Group 12: **0.3626** | TONGUE, ROOM, GIMMICK, MILDEW                                     | INCORRECT (Max overlap: 2/4 with ENDING WITH SYNONYMS FOR “YUCK”)
   - Group 13: **0.4018** | DYNASTY, GIMMICK, MILDEW, ENGROSS                                 | CORRECT GROUP (ENDING WITH SYNONYMS FOR “YUCK”, Level 3)
   - Group 14: **0.3898** | TONGUE, SOLE, FACE, HEEL                                          | INCORRECT (Max overlap: 3/4 with PARTS OF A SHOE)
   - Group 15: **0.3434** | REGARD, CAPACITY, UPPER, IMAGE                                    | INCORRECT (Max overlap: 2/4 with REPUTATION)
   - Group 16: **0.4448** | ROOM, CAPACITY, SEATING, CHAIRS                                   | CORRECT GROUP (ACCOMMODATION, Level 1) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 25.8%)]
   - Group 17: **0.3638** | TONGUE, SOLE, UPPER, HEEL                                         | CORRECT GROUP (PARTS OF A SHOE, Level 0) | [Pred Type: SEMANTIC_SET (47.0%, no-rel 25.5%)]
   - Group 18: **0.3531** | REGARD, STANDING, FACE, IMAGE                                     | CORRECT GROUP (REPUTATION, Level 2)
   - Group 19: **0.3982** | ROOM, CAPACITY, STANDING, SEATING                                 | INCORRECT (Max overlap: 3/4 with ACCOMMODATION) | [Pred Type: SYNONYM_OR_NEAR (62.5%, no-rel 27.6%)]
   - Group 20: **0.3525** | REGARD, FACE, IMAGE, CHAIRS                                       | INCORRECT (Max overlap: 3/4 with REPUTATION)

---

## Puzzle 2 (ID: 993)
**Words on Board:** BEAM, POPCORN, STATION, POSITION, FUNKY, STRIKE, STANDING, SAFE, VAULT, FOUL, RANK, BALL, RINGS, SPRING, RUBBER, HORSE

### Ground Truth Categories:
* **Level 0 (GYMNASTICS APPARATUS) [Type: SEMANTIC_SET]:** BEAM, HORSE, RINGS, VAULT
* **Level 1 (STATUS) [Type: SYNONYM_OR_NEAR]:** POSITION, RANK, STANDING, STATION
* **Level 2 (BASEBALL CALLS) [Type: SEMANTIC_SET]:** BALL, FOUL, SAFE, STRIKE
* **Level 3 (___ CHICKEN) [Type: FILL_IN_THE_BLANK]:** FUNKY, POPCORN, RUBBER, SPRING

### Top Candidate Partitions:
1. **Partition Score: 0.4205**
   - Group 1: **0.6666** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 30.7%)]
   - Group 2: **0.4994** | POPCORN, RINGS, RUBBER, HORSE                                     | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 3: **0.4091** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 28.7%)]
   - Group 4: **0.3868** | BEAM, SAFE, VAULT, SPRING                                         | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
2. **Partition Score: 0.4193**
   - Group 1: **0.6666** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 30.7%)]
   - Group 2: **0.5131** | BEAM, VAULT, SPRING, HORSE                                        | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 3: **0.4091** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 28.7%)]
   - Group 4: **0.3775** | POPCORN, SAFE, RINGS, RUBBER                                      | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
3. **Partition Score: 0.4162**
   - Group 1: **0.6666** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 30.7%)]
   - Group 2: **0.4293** | BEAM, SAFE, VAULT, HORSE                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 3: **0.4173** | POPCORN, RINGS, SPRING, RUBBER                                    | INCORRECT (Max overlap: 3/4 with ___ CHICKEN)
   - Group 4: **0.4091** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 28.7%)]
4. **Partition Score: 0.4149**
   - Group 1: **0.6666** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 30.7%)]
   - Group 2: **0.4211** | SAFE, RINGS, RUBBER, HORSE                                        | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 3: **0.4203** | BEAM, POPCORN, VAULT, SPRING                                      | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 4: **0.4091** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 28.7%)]
5. **Partition Score: 0.4131**
   - Group 1: **0.6666** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 30.7%)]
   - Group 2: **0.5483** | BEAM, POPCORN, RINGS, HORSE                                       | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS) | [Pred Type: SEMANTIC_SET (45.8%, no-rel 34.2%)]
   - Group 3: **0.4091** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 28.7%)]
   - Group 4: **0.3474** | SAFE, VAULT, SPRING, RUBBER                                       | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)

### Top Candidate Groups:
   - Group 1: **0.6666** | STATION, POSITION, STANDING, RANK                                 | CORRECT GROUP (STATUS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 30.7%)]
   - Group 2: **0.4994** | POPCORN, RINGS, RUBBER, HORSE                                     | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 3: **0.4091** | FUNKY, STRIKE, FOUL, BALL                                         | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 28.7%)]
   - Group 4: **0.3868** | BEAM, SAFE, VAULT, SPRING                                         | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 5: **0.5131** | BEAM, VAULT, SPRING, HORSE                                        | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 6: **0.3775** | POPCORN, SAFE, RINGS, RUBBER                                      | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 7: **0.4293** | BEAM, SAFE, VAULT, HORSE                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 8: **0.4173** | POPCORN, RINGS, SPRING, RUBBER                                    | INCORRECT (Max overlap: 3/4 with ___ CHICKEN)
   - Group 9: **0.4211** | SAFE, RINGS, RUBBER, HORSE                                        | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 10: **0.4203** | BEAM, POPCORN, VAULT, SPRING                                      | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 11: **0.5483** | BEAM, POPCORN, RINGS, HORSE                                       | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS) | [Pred Type: SEMANTIC_SET (45.8%, no-rel 34.2%)]
   - Group 12: **0.3474** | SAFE, VAULT, SPRING, RUBBER                                       | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 13: **0.4330** | POSITION, STRIKE, FOUL, BALL                                      | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS)
   - Group 14: **0.3972** | STATION, FUNKY, STANDING, RANK                                    | INCORRECT (Max overlap: 3/4 with STATUS) | [Pred Type: SYNONYM_OR_NEAR (55.0%, no-rel 31.8%)]
   - Group 15: **0.4609** | POPCORN, VAULT, SPRING, HORSE                                     | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 16: **0.3852** | BEAM, SAFE, RINGS, RUBBER                                         | INCORRECT (Max overlap: 2/4 with GYMNASTICS APPARATUS)
   - Group 17: **0.5385** | BEAM, RINGS, SPRING, HORSE                                        | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS)
   - Group 18: **0.3430** | POPCORN, SAFE, VAULT, RUBBER                                      | INCORRECT (Max overlap: 2/4 with ___ CHICKEN)
   - Group 19: **0.4310** | POPCORN, SPRING, RUBBER, HORSE                                    | INCORRECT (Max overlap: 3/4 with ___ CHICKEN)
   - Group 20: **0.3952** | BEAM, SAFE, VAULT, RINGS                                          | INCORRECT (Max overlap: 3/4 with GYMNASTICS APPARATUS) | [Pred Type: SEMANTIC_SET (47.3%, no-rel 30.2%)]

---

## Puzzle 3 (ID: 320)
**Words on Board:** SIGHT, IMPACT, TASTE, TOUCH, BAKE, ELEGANCE, STYLE, SUN, SEN, BASK, SOUR, TAN, GRACE, MOVE, AFFECT, SINE

### Ground Truth Categories:
* **Level 0 (REFINED SENSIBILITY) [Type: SYNONYM_OR_NEAR]:** ELEGANCE, GRACE, STYLE, TASTE
* **Level 1 (CATCH SOME RAYS) [Type: SYNONYM_OR_NEAR]:** BAKE, BASK, SUN, TAN
* **Level 2 (EMOTIONALLY SWAY ) [Type: SYNONYM_OR_NEAR]:** AFFECT, IMPACT, MOVE, TOUCH
* **Level 3 (NUMBERS WITH FIRST LETTERS REPLACED BY “S”) [Type: WORDPLAY_TRANSFORM]:** SEN, SIGHT, SINE, SOUR

### Top Candidate Partitions:
1. **Partition Score: 0.4383**
   - Group 1: **0.6062** | SIGHT, TASTE, TOUCH, STYLE                                        | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 2: **0.5857** | SUN, SEN, TAN, SINE                                               | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS) | [Pred Type: SOUND_OR_SPELLING (46.4%, no-rel 10.8%)]
   - Group 3: **0.4326** | IMPACT, SOUR, MOVE, AFFECT                                        | INCORRECT (Max overlap: 3/4 with EMOTIONALLY SWAY ) | [Pred Type: SYNONYM_OR_NEAR (64.3%, no-rel 27.7%)]
   - Group 4: **0.3674** | BAKE, ELEGANCE, BASK, GRACE                                       | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS)
2. **Partition Score: 0.4335**
   - Group 1: **0.7143** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 24.1%)]
   - Group 2: **0.5857** | SUN, SEN, TAN, SINE                                               | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS) | [Pred Type: SOUND_OR_SPELLING (46.4%, no-rel 10.8%)]
   - Group 3: **0.4134** | SIGHT, TASTE, STYLE, SOUR                                         | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 4: **0.3674** | BAKE, ELEGANCE, BASK, GRACE                                       | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS)
3. **Partition Score: 0.4238**
   - Group 1: **0.6095** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 2: **0.6062** | SIGHT, TASTE, TOUCH, STYLE                                        | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 3: **0.4326** | IMPACT, SOUR, MOVE, AFFECT                                        | INCORRECT (Max overlap: 3/4 with EMOTIONALLY SWAY ) | [Pred Type: SYNONYM_OR_NEAR (64.3%, no-rel 27.7%)]
   - Group 4: **0.3281** | BAKE, ELEGANCE, SEN, GRACE                                        | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
4. **Partition Score: 0.4198**
   - Group 1: **0.7143** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 24.1%)]
   - Group 2: **0.6095** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 3: **0.4134** | SIGHT, TASTE, STYLE, SOUR                                         | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 4: **0.3281** | BAKE, ELEGANCE, SEN, GRACE                                        | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
5. **Partition Score: 0.4040**
   - Group 1: **0.5857** | SUN, SEN, TAN, SINE                                               | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS) | [Pred Type: SOUND_OR_SPELLING (46.4%, no-rel 10.8%)]
   - Group 2: **0.4326** | IMPACT, SOUR, MOVE, AFFECT                                        | INCORRECT (Max overlap: 3/4 with EMOTIONALLY SWAY ) | [Pred Type: SYNONYM_OR_NEAR (64.3%, no-rel 27.7%)]
   - Group 3: **0.4234** | ELEGANCE, STYLE, BASK, GRACE                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 4: **0.3800** | SIGHT, TASTE, TOUCH, BAKE                                         | INCORRECT (Max overlap: 1/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)

### Top Candidate Groups:
   - Group 1: **0.6062** | SIGHT, TASTE, TOUCH, STYLE                                        | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 2: **0.5857** | SUN, SEN, TAN, SINE                                               | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS) | [Pred Type: SOUND_OR_SPELLING (46.4%, no-rel 10.8%)]
   - Group 3: **0.4326** | IMPACT, SOUR, MOVE, AFFECT                                        | INCORRECT (Max overlap: 3/4 with EMOTIONALLY SWAY ) | [Pred Type: SYNONYM_OR_NEAR (64.3%, no-rel 27.7%)]
   - Group 4: **0.3674** | BAKE, ELEGANCE, BASK, GRACE                                       | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS)
   - Group 5: **0.7143** | IMPACT, TOUCH, MOVE, AFFECT                                       | CORRECT GROUP (EMOTIONALLY SWAY , Level 2) | [Pred Type: SYNONYM_OR_NEAR (69.6%, no-rel 24.1%)]
   - Group 6: **0.4134** | SIGHT, TASTE, STYLE, SOUR                                         | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 7: **0.6095** | SUN, BASK, TAN, SINE                                              | INCORRECT (Max overlap: 3/4 with CATCH SOME RAYS)
   - Group 8: **0.3281** | BAKE, ELEGANCE, SEN, GRACE                                        | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 9: **0.4234** | ELEGANCE, STYLE, BASK, GRACE                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 10: **0.3800** | SIGHT, TASTE, TOUCH, BAKE                                         | INCORRECT (Max overlap: 1/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 11: **0.3771** | BAKE, STYLE, BASK, GRACE                                          | INCORRECT (Max overlap: 2/4 with CATCH SOME RAYS)
   - Group 12: **0.3257** | SIGHT, TASTE, ELEGANCE, SOUR                                      | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 13: **0.4199** | SIGHT, TASTE, TOUCH, ELEGANCE                                     | INCORRECT (Max overlap: 2/4 with REFINED SENSIBILITY)
   - Group 14: **0.4654** | SIGHT, TASTE, TOUCH, SOUR                                         | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 15: **0.4385** | BAKE, ELEGANCE, STYLE, GRACE                                      | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)
   - Group 16: **0.3487** | IMPACT, SEN, MOVE, AFFECT                                         | INCORRECT (Max overlap: 3/4 with EMOTIONALLY SWAY ) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 24.3%)]
   - Group 17: **0.3610** | SIGHT, TASTE, TOUCH, SEN                                          | INCORRECT (Max overlap: 2/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 18: **0.3875** | IMPACT, STYLE, MOVE, AFFECT                                       | INCORRECT (Max overlap: 3/4 with EMOTIONALLY SWAY ) | [Pred Type: SYNONYM_OR_NEAR (65.7%, no-rel 26.4%)]
   - Group 19: **0.3582** | SIGHT, TASTE, TOUCH, BASK                                         | INCORRECT (Max overlap: 1/4 with NUMBERS WITH FIRST LETTERS REPLACED BY “S”)
   - Group 20: **0.3876** | ELEGANCE, STYLE, SEN, GRACE                                       | INCORRECT (Max overlap: 3/4 with REFINED SENSIBILITY)

---

## Puzzle 4 (ID: 732)
**Words on Board:** SNUGGLING, MISSING, DISHING, CUDDLING, WHISPERING, BOWLING, BUZZING, ACUPUNCTURING, HUGGING, SIRING, WRESTLING, DOCTORING, SEWING, SPILLING, LORDING, SPOONING

### Ground Truth Categories:
* **Level 0 (GETTING COZY) [Type: SYNONYM_OR_NEAR]:** CUDDLING, HUGGING, SNUGGLING, SPOONING
* **Level 1 (GOSSIPING) [Type: SYNONYM_OR_NEAR]:** BUZZING, DISHING, SPILLING, WHISPERING
* **Level 2 (ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES) [Type: SEMANTIC_SET]:** ACUPUNCTURING, BOWLING, SEWING, WRESTLING
* **Level 3 (STARTING WITH TITLES) [Type: WORD_FORM]:** DOCTORING, LORDING, MISSING, SIRING

### Top Candidate Partitions:
1. **Partition Score: 0.4793**
   - Group 1: **0.7631** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5668** | DISHING, SIRING, DOCTORING, LORDING                               | INCORRECT (Max overlap: 3/4 with STARTING WITH TITLES)
   - Group 3: **0.4771** | MISSING, WHISPERING, BUZZING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 4: **0.4366** | BOWLING, ACUPUNCTURING, WRESTLING, SEWING                         | CORRECT GROUP (ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES, Level 2) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 27.9%)]
2. **Partition Score: 0.4684**
   - Group 1: **0.7631** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5307** | MISSING, WHISPERING, BUZZING, SIRING                              | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 3: **0.4698** | DISHING, DOCTORING, SPILLING, LORDING                             | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 4: **0.4366** | BOWLING, ACUPUNCTURING, WRESTLING, SEWING                         | CORRECT GROUP (ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES, Level 2) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 27.9%)]
3. **Partition Score: 0.4665**
   - Group 1: **0.7631** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5363** | MISSING, DISHING, WHISPERING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 3: **0.4565** | BUZZING, SIRING, DOCTORING, LORDING                               | INCORRECT (Max overlap: 3/4 with STARTING WITH TITLES)
   - Group 4: **0.4366** | BOWLING, ACUPUNCTURING, WRESTLING, SEWING                         | CORRECT GROUP (ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES, Level 2) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 27.9%)]
4. **Partition Score: 0.4656**
   - Group 1: **0.7631** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5286** | DISHING, WHISPERING, DOCTORING, LORDING                           | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 3: **0.4605** | MISSING, BUZZING, SIRING, SPILLING                                | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 4: **0.4366** | BOWLING, ACUPUNCTURING, WRESTLING, SEWING                         | CORRECT GROUP (ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES, Level 2) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 27.9%)]
5. **Partition Score: 0.4630**
   - Group 1: **0.7631** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.4902** | DISHING, BUZZING, DOCTORING, LORDING                              | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 3: **0.4885** | MISSING, WHISPERING, SIRING, SPILLING                             | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 4: **0.4366** | BOWLING, ACUPUNCTURING, WRESTLING, SEWING                         | CORRECT GROUP (ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES, Level 2) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 27.9%)]

### Top Candidate Groups:
   - Group 1: **0.7631** | SNUGGLING, CUDDLING, HUGGING, SPOONING                            | CORRECT GROUP (GETTING COZY, Level 0)
   - Group 2: **0.5668** | DISHING, SIRING, DOCTORING, LORDING                               | INCORRECT (Max overlap: 3/4 with STARTING WITH TITLES)
   - Group 3: **0.4771** | MISSING, WHISPERING, BUZZING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 4: **0.4366** | BOWLING, ACUPUNCTURING, WRESTLING, SEWING                         | CORRECT GROUP (ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES, Level 2) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 27.9%)]
   - Group 5: **0.5307** | MISSING, WHISPERING, BUZZING, SIRING                              | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 6: **0.4698** | DISHING, DOCTORING, SPILLING, LORDING                             | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 7: **0.5363** | MISSING, DISHING, WHISPERING, SPILLING                            | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 8: **0.4565** | BUZZING, SIRING, DOCTORING, LORDING                               | INCORRECT (Max overlap: 3/4 with STARTING WITH TITLES)
   - Group 9: **0.5286** | DISHING, WHISPERING, DOCTORING, LORDING                           | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 10: **0.4605** | MISSING, BUZZING, SIRING, SPILLING                                | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 11: **0.4902** | DISHING, BUZZING, DOCTORING, LORDING                              | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 12: **0.4885** | MISSING, WHISPERING, SIRING, SPILLING                             | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 13: **0.4978** | MISSING, DISHING, SIRING, SPILLING                                | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 14: **0.4669** | WHISPERING, BUZZING, DOCTORING, LORDING                           | INCORRECT (Max overlap: 2/4 with GOSSIPING)
   - Group 15: **0.4658** | SNUGGLING, CUDDLING, ACUPUNCTURING, HUGGING                       | INCORRECT (Max overlap: 3/4 with GETTING COZY) | [Pred Type: SEMANTIC_SET (47.0%, no-rel 19.8%)]
   - Group 16: **0.4642** | DISHING, SIRING, LORDING, SPOONING                                | INCORRECT (Max overlap: 2/4 with STARTING WITH TITLES)
   - Group 17: **0.4538** | BOWLING, WRESTLING, DOCTORING, SEWING                             | INCORRECT (Max overlap: 3/4 with ENGAGING IN AN ACTIVITY WITH PINS OR NEEDLES)
   - Group 18: **0.4862** | WHISPERING, SIRING, DOCTORING, LORDING                            | INCORRECT (Max overlap: 3/4 with STARTING WITH TITLES)
   - Group 19: **0.4754** | MISSING, DISHING, BUZZING, SPILLING                               | INCORRECT (Max overlap: 3/4 with GOSSIPING)
   - Group 20: **0.4757** | DISHING, SIRING, SPILLING, SPOONING                               | INCORRECT (Max overlap: 2/4 with GOSSIPING)

---

## Puzzle 5 (ID: 206)
**Words on Board:** CHECK, TIP, MIKE, PAIN, COLE, TAP, WIRE, TICK, MARK, 40, GLIDE, SOAR, X, BUG, FLY, FLOAT

### Ground Truth Categories:
* **Level 0 (MOVE THROUGH THE AIR) [Type: SYNONYM_OR_NEAR]:** FLOAT, FLY, GLIDE, SOAR
* **Level 1 (HIDDEN LISTENING DEVICES) [Type: SYNONYM_OR_NEAR]:** BUG, MIKE, TAP, WIRE
* **Level 2 (SELECT, AS A BOX ON A FORM) [Type: SYNONYM_OR_NEAR]:** CHECK, MARK, TICK, X
* **Level 3 (RAPPERS MINUS FIRST LETTER) [Type: WORDPLAY_TRANSFORM]:** 40, COLE, PAIN, TIP

### Top Candidate Partitions:
1. **Partition Score: 0.4786**
   - Group 1: **0.6406** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 38.2%)]
   - Group 2: **0.6073** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.5549** | CHECK, TICK, MARK, X                                              | CORRECT GROUP (SELECT, AS A BOX ON A FORM, Level 2)
   - Group 4: **0.3762** | TIP, TAP, WIRE, BUG                                               | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)
2. **Partition Score: 0.4343**
   - Group 1: **0.6406** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 38.2%)]
   - Group 2: **0.6073** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.5607** | CHECK, TAP, TICK, MARK                                            | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (50.0%, no-rel 25.4%)]
   - Group 4: **0.2847** | TIP, WIRE, X, BUG                                                 | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
3. **Partition Score: 0.4336**
   - Group 1: **0.6406** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 38.2%)]
   - Group 2: **0.6073** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.4691** | CHECK, WIRE, TICK, MARK                                           | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (46.4%, no-rel 27.3%)]
   - Group 4: **0.3290** | TIP, TAP, X, BUG                                                  | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
4. **Partition Score: 0.4255**
   - Group 1: **0.6406** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 38.2%)]
   - Group 2: **0.6073** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.4313** | TAP, WIRE, TICK, BUG                                              | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)
   - Group 4: **0.3316** | CHECK, TIP, MARK, X                                               | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (47.4%, no-rel 25.9%)]
5. **Partition Score: 0.4185**
   - Group 1: **0.6406** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 38.2%)]
   - Group 2: **0.6073** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.4919** | CHECK, TIP, TICK, MARK                                            | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (54.0%, no-rel 25.9%)]
   - Group 4: **0.2874** | TAP, WIRE, X, BUG                                                 | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)

### Top Candidate Groups:
   - Group 1: **0.6406** | GLIDE, SOAR, FLY, FLOAT                                           | CORRECT GROUP (MOVE THROUGH THE AIR, Level 0) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 38.2%)]
   - Group 2: **0.6073** | MIKE, PAIN, COLE, 40                                              | INCORRECT (Max overlap: 3/4 with RAPPERS MINUS FIRST LETTER)
   - Group 3: **0.5549** | CHECK, TICK, MARK, X                                              | CORRECT GROUP (SELECT, AS A BOX ON A FORM, Level 2)
   - Group 4: **0.3762** | TIP, TAP, WIRE, BUG                                               | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)
   - Group 5: **0.5607** | CHECK, TAP, TICK, MARK                                            | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (50.0%, no-rel 25.4%)]
   - Group 6: **0.2847** | TIP, WIRE, X, BUG                                                 | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 7: **0.4691** | CHECK, WIRE, TICK, MARK                                           | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (46.4%, no-rel 27.3%)]
   - Group 8: **0.3290** | TIP, TAP, X, BUG                                                  | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 9: **0.4313** | TAP, WIRE, TICK, BUG                                              | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)
   - Group 10: **0.3316** | CHECK, TIP, MARK, X                                               | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (47.4%, no-rel 25.9%)]
   - Group 11: **0.4919** | CHECK, TIP, TICK, MARK                                            | INCORRECT (Max overlap: 3/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (54.0%, no-rel 25.9%)]
   - Group 12: **0.2874** | TAP, WIRE, X, BUG                                                 | INCORRECT (Max overlap: 3/4 with HIDDEN LISTENING DEVICES)
   - Group 13: **0.4955** | TIP, TAP, TICK, MARK                                              | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 14: **0.2819** | CHECK, WIRE, X, BUG                                               | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 15: **0.4401** | CHECK, TAP, TICK, BUG                                             | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 16: **0.3029** | TIP, WIRE, MARK, X                                                | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM)
   - Group 17: **0.3703** | CHECK, TIP, TAP, MARK                                             | INCORRECT (Max overlap: 2/4 with SELECT, AS A BOX ON A FORM) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 29.9%)]
   - Group 18: **0.3276** | WIRE, TICK, X, BUG                                                | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES) | [Pred Type: SEMANTIC_SET (46.6%, no-rel 22.8%)]
   - Group 19: **0.5243** | MIKE, COLE, WIRE, 40                                              | INCORRECT (Max overlap: 2/4 with HIDDEN LISTENING DEVICES)
   - Group 20: **0.2764** | TIP, PAIN, TAP, BUG                                               | INCORRECT (Max overlap: 2/4 with RAPPERS MINUS FIRST LETTER)

---

## Puzzle 6 (ID: 708)
**Words on Board:** BLUBBER, BENEFIT, BALL, UTILITY, TOW, FLIPPER, RAILROAD, BAWL, GALA, AVENUE, CHANCE, FLUKE, MELON, SOUL, HEAL, FUNCTION

### Ground Truth Categories:
* **Level 0 (FUNDRAISING EVENT) [Type: SYNONYM_OR_NEAR]:** BALL, BENEFIT, GALA, FUNCTION
* **Level 1 (SPACES ON A MONOPOLY BOARD) [Type: NAMED_ENTITY_SET]:** AVENUE, CHANCE, RAILROAD, UTILITY
* **Level 2 (FEATURES OF A TOOTHED WHALE) [Type: SEMANTIC_SET]:** BLUBBER, FLIPPER, FLUKE, MELON
* **Level 3 (HOMOPHONES OF PARTS OF THE FOOT) [Type: SOUND_OR_SPELLING]:** BAWL, HEAL, SOUL, TOW

### Top Candidate Partitions:
1. **Partition Score: 0.4395**
   - Group 1: **0.5467** | BENEFIT, UTILITY, HEAL, FUNCTION                                  | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 2: **0.4859** | FLIPPER, GALA, AVENUE, MELON                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE)
   - Group 3: **0.4843** | BLUBBER, BAWL, CHANCE, FLUKE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 37.1%)]
   - Group 4: **0.3940** | BALL, TOW, RAILROAD, SOUL                                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT)
2. **Partition Score: 0.4328**
   - Group 1: **0.5467** | BENEFIT, UTILITY, HEAL, FUNCTION                                  | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 2: **0.4843** | BLUBBER, BAWL, CHANCE, FLUKE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 37.1%)]
   - Group 3: **0.4444** | RAILROAD, GALA, AVENUE, MELON                                     | INCORRECT (Max overlap: 2/4 with SPACES ON A MONOPOLY BOARD)
   - Group 4: **0.4012** | BALL, TOW, FLIPPER, SOUL                                          | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT)
3. **Partition Score: 0.4266**
   - Group 1: **0.5467** | BENEFIT, UTILITY, HEAL, FUNCTION                                  | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 2: **0.4843** | BLUBBER, BAWL, CHANCE, FLUKE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 37.1%)]
   - Group 3: **0.4089** | BALL, TOW, FLIPPER, RAILROAD                                      | INCORRECT (Max overlap: 1/4 with FUNDRAISING EVENT)
   - Group 4: **0.4067** | GALA, AVENUE, MELON, SOUL                                         | INCORRECT (Max overlap: 1/4 with FUNDRAISING EVENT) | [Pred Type: FILL_IN_THE_BLANK (52.2%, no-rel 10.5%)]
4. **Partition Score: 0.4258**
   - Group 1: **0.6308** | BENEFIT, UTILITY, CHANCE, FUNCTION                                | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 2: **0.4859** | FLIPPER, GALA, AVENUE, MELON                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE)
   - Group 3: **0.4293** | BLUBBER, BAWL, FLUKE, HEAL                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE)
   - Group 4: **0.3940** | BALL, TOW, RAILROAD, SOUL                                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT)
5. **Partition Score: 0.4240**
   - Group 1: **0.5467** | BENEFIT, UTILITY, HEAL, FUNCTION                                  | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 2: **0.4843** | BLUBBER, BAWL, CHANCE, FLUKE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 37.1%)]
   - Group 3: **0.4156** | BALL, FLIPPER, MELON, SOUL                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE)
   - Group 4: **0.3981** | TOW, RAILROAD, GALA, AVENUE                                       | INCORRECT (Max overlap: 2/4 with SPACES ON A MONOPOLY BOARD)

### Top Candidate Groups:
   - Group 1: **0.5467** | BENEFIT, UTILITY, HEAL, FUNCTION                                  | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 2: **0.4859** | FLIPPER, GALA, AVENUE, MELON                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE)
   - Group 3: **0.4843** | BLUBBER, BAWL, CHANCE, FLUKE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 37.1%)]
   - Group 4: **0.3940** | BALL, TOW, RAILROAD, SOUL                                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT)
   - Group 5: **0.4444** | RAILROAD, GALA, AVENUE, MELON                                     | INCORRECT (Max overlap: 2/4 with SPACES ON A MONOPOLY BOARD)
   - Group 6: **0.4012** | BALL, TOW, FLIPPER, SOUL                                          | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT)
   - Group 7: **0.4089** | BALL, TOW, FLIPPER, RAILROAD                                      | INCORRECT (Max overlap: 1/4 with FUNDRAISING EVENT)
   - Group 8: **0.4067** | GALA, AVENUE, MELON, SOUL                                         | INCORRECT (Max overlap: 1/4 with FUNDRAISING EVENT) | [Pred Type: FILL_IN_THE_BLANK (52.2%, no-rel 10.5%)]
   - Group 9: **0.6308** | BENEFIT, UTILITY, CHANCE, FUNCTION                                | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 10: **0.4293** | BLUBBER, BAWL, FLUKE, HEAL                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE)
   - Group 11: **0.4156** | BALL, FLIPPER, MELON, SOUL                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF A TOOTHED WHALE)
   - Group 12: **0.3981** | TOW, RAILROAD, GALA, AVENUE                                       | INCORRECT (Max overlap: 2/4 with SPACES ON A MONOPOLY BOARD)
   - Group 13: **0.5491** | BENEFIT, UTILITY, FLUKE, FUNCTION                                 | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 14: **0.4148** | BLUBBER, BAWL, CHANCE, HEAL                                       | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT)
   - Group 15: **0.5972** | UTILITY, CHANCE, FLUKE, FUNCTION                                  | INCORRECT (Max overlap: 2/4 with SPACES ON A MONOPOLY BOARD) | [Pred Type: SYNONYM_OR_NEAR (49.1%, no-rel 38.6%)]
   - Group 16: **0.4129** | BLUBBER, BENEFIT, BAWL, HEAL                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT)
   - Group 17: **0.4794** | BLUBBER, BENEFIT, UTILITY, FUNCTION                               | INCORRECT (Max overlap: 2/4 with FUNDRAISING EVENT)
   - Group 18: **0.4127** | BAWL, CHANCE, FLUKE, HEAL                                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 35.0%)]
   - Group 19: **0.4239** | FLIPPER, RAILROAD, GALA, AVENUE                                   | INCORRECT (Max overlap: 2/4 with SPACES ON A MONOPOLY BOARD)
   - Group 20: **0.3837** | BALL, TOW, MELON, SOUL                                            | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF PARTS OF THE FOOT)

---

## Puzzle 7 (ID: 1043)
**Words on Board:** MOTHER, DEVOTE, SKIRT, WHAMMY, PULP, NEIGHBOR, EDUCATED, HISTORICAL, TOTORO, FLANK, ASIAGO, MY, TOUCH, SCIENCE, LITERARY, VERY

### Ground Truth Categories:
* **Level 0 (BORDER) [Type: SYNONYM_OR_NEAR]:** FLANK, NEIGHBOR, SKIRT, TOUCH
* **Level 1 (KINDS OF FICTION) [Type: SEMANTIC_SET]:** HISTORICAL, LITERARY, PULP, SCIENCE
* **Level 2 (WORDS IN A PLANETARY MNEMONIC) [Type: COMMON_PHRASE]:** EDUCATED, MOTHER, MY, VERY
* **Level 3 (STARTING WITH FOUR-LETTER '80S BANDS) [Type: WORDPLAY_TRANSFORM]:** ASIAGO, DEVOTE, TOTORO, WHAMMY

### Top Candidate Partitions:
1. **Partition Score: 0.3923**
   - Group 1: **0.4177** | MOTHER, WHAMMY, MY, SCIENCE                                       | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 2: **0.4119** | PULP, NEIGHBOR, TOTORO, ASIAGO                                    | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS) | [Pred Type: NAMED_ENTITY_SET (47.7%, no-rel 20.9%)]
   - Group 3: **0.4020** | SKIRT, HISTORICAL, FLANK, TOUCH                                   | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 4: **0.3775** | DEVOTE, EDUCATED, LITERARY, VERY                                  | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
2. **Partition Score: 0.3909**
   - Group 1: **0.4574** | WHAMMY, PULP, TOTORO, ASIAGO                                      | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 2: **0.4065** | MOTHER, NEIGHBOR, MY, SCIENCE                                     | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 3: **0.4020** | SKIRT, HISTORICAL, FLANK, TOUCH                                   | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 4: **0.3775** | DEVOTE, EDUCATED, LITERARY, VERY                                  | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
3. **Partition Score: 0.3879**
   - Group 1: **0.4872** | WHAMMY, NEIGHBOR, TOTORO, ASIAGO                                  | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 2: **0.4020** | SKIRT, HISTORICAL, FLANK, TOUCH                                   | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 3: **0.3945** | MOTHER, PULP, MY, SCIENCE                                         | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 4: **0.3775** | DEVOTE, EDUCATED, LITERARY, VERY                                  | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
4. **Partition Score: 0.3874**
   - Group 1: **0.5916** | WHAMMY, TOTORO, ASIAGO, MY                                        | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 2: **0.4020** | SKIRT, HISTORICAL, FLANK, TOUCH                                   | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 3: **0.3924** | MOTHER, PULP, NEIGHBOR, SCIENCE                                   | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 4: **0.3775** | DEVOTE, EDUCATED, LITERARY, VERY                                  | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
5. **Partition Score: 0.3855**
   - Group 1: **0.4471** | PULP, TOTORO, ASIAGO, MY                                          | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 2: **0.4020** | SKIRT, HISTORICAL, FLANK, TOUCH                                   | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 3: **0.3848** | MOTHER, WHAMMY, NEIGHBOR, SCIENCE                                 | INCORRECT (Max overlap: 1/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 4: **0.3775** | DEVOTE, EDUCATED, LITERARY, VERY                                  | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)

### Top Candidate Groups:
   - Group 1: **0.4177** | MOTHER, WHAMMY, MY, SCIENCE                                       | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 2: **0.4119** | PULP, NEIGHBOR, TOTORO, ASIAGO                                    | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS) | [Pred Type: NAMED_ENTITY_SET (47.7%, no-rel 20.9%)]
   - Group 3: **0.4020** | SKIRT, HISTORICAL, FLANK, TOUCH                                   | INCORRECT (Max overlap: 3/4 with BORDER)
   - Group 4: **0.3775** | DEVOTE, EDUCATED, LITERARY, VERY                                  | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 5: **0.4574** | WHAMMY, PULP, TOTORO, ASIAGO                                      | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 6: **0.4065** | MOTHER, NEIGHBOR, MY, SCIENCE                                     | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 7: **0.4872** | WHAMMY, NEIGHBOR, TOTORO, ASIAGO                                  | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 8: **0.3945** | MOTHER, PULP, MY, SCIENCE                                         | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 9: **0.5916** | WHAMMY, TOTORO, ASIAGO, MY                                        | INCORRECT (Max overlap: 3/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 10: **0.3924** | MOTHER, PULP, NEIGHBOR, SCIENCE                                   | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 11: **0.4471** | PULP, TOTORO, ASIAGO, MY                                          | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 12: **0.3848** | MOTHER, WHAMMY, NEIGHBOR, SCIENCE                                 | INCORRECT (Max overlap: 1/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 13: **0.4892** | NEIGHBOR, TOTORO, ASIAGO, MY                                      | INCORRECT (Max overlap: 2/4 with STARTING WITH FOUR-LETTER '80S BANDS)
   - Group 14: **0.3838** | MOTHER, WHAMMY, PULP, SCIENCE                                     | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 15: **0.4288** | WHAMMY, MY, SCIENCE, VERY                                         | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 16: **0.3594** | MOTHER, DEVOTE, EDUCATED, LITERARY                                | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 17: **0.4036** | WHAMMY, PULP, TOUCH, SCIENCE                                      | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)
   - Group 18: **0.3804** | SKIRT, EDUCATED, HISTORICAL, FLANK                                | INCORRECT (Max overlap: 2/4 with BORDER)
   - Group 19: **0.3720** | MOTHER, DEVOTE, LITERARY, VERY                                    | INCORRECT (Max overlap: 2/4 with WORDS IN A PLANETARY MNEMONIC)
   - Group 20: **0.3954** | PULP, NEIGHBOR, TOUCH, SCIENCE                                    | INCORRECT (Max overlap: 2/4 with KINDS OF FICTION)

---

## Puzzle 8 (ID: 986)
**Words on Board:** POSTURE, CHRISTMAS TREE, BOLT, MASQUERADE, WEDDING, BLARNEY STONE, PARTY HAT, BLUFF, VOLCANO, FRONT, MISTLETOE, INHALE, CONE, GORGE, NEW YEAR'S EVE, SCARF

### Ground Truth Categories:
* **Level 0 (EAT VORACIOUSLY) [Type: SYNONYM_OR_NEAR]:** BOLT, GORGE, INHALE, SCARF
* **Level 1 (CONICAL THINGS) [Type: SEMANTIC_SET]:** CHRISTMAS TREE, CONE, PARTY HAT, VOLCANO
* **Level 2 (POSE) [Type: SYNONYM_OR_NEAR]:** BLUFF, FRONT, MASQUERADE, POSTURE
* **Level 3 (SETTINGS FOR A KISS) [Type: NAMED_ENTITY_SET]:** BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE, WEDDING

### Top Candidate Partitions:
1. **Partition Score: 0.3892**
   - Group 1: **0.4419** | BLARNEY STONE, MISTLETOE, INHALE, NEW YEAR'S EVE                  | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 2: **0.4177** | POSTURE, BOLT, BLUFF, FRONT                                       | INCORRECT (Max overlap: 3/4 with POSE)
   - Group 3: **0.4009** | CHRISTMAS TREE, PARTY HAT, VOLCANO, CONE                          | CORRECT GROUP (CONICAL THINGS, Level 1) | [Pred Type: SEMANTIC_SET (68.9%, no-rel 19.7%)]
   - Group 4: **0.3690** | MASQUERADE, WEDDING, GORGE, SCARF                                 | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 25.1%)]
2. **Partition Score: 0.3874**
   - Group 1: **0.4266** | BLARNEY STONE, VOLCANO, MISTLETOE, NEW YEAR'S EVE                 | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 2: **0.4107** | POSTURE, MASQUERADE, WEDDING, BLUFF                               | INCORRECT (Max overlap: 3/4 with POSE)
   - Group 3: **0.4065** | CHRISTMAS TREE, PARTY HAT, CONE, SCARF                            | INCORRECT (Max overlap: 3/4 with CONICAL THINGS) | [Pred Type: SEMANTIC_SET (70.0%, no-rel 16.1%)]
   - Group 4: **0.3662** | BOLT, FRONT, INHALE, GORGE                                        | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
3. **Partition Score: 0.3858**
   - Group 1: **0.4095** | BOLT, BLUFF, GORGE, SCARF                                         | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (46.5%, no-rel 30.9%)]
   - Group 2: **0.4069** | POSTURE, MASQUERADE, FRONT, INHALE                                | INCORRECT (Max overlap: 3/4 with POSE)
   - Group 3: **0.3875** | CHRISTMAS TREE, WEDDING, MISTLETOE, NEW YEAR'S EVE                | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 8.9%)]
   - Group 4: **0.3743** | BLARNEY STONE, PARTY HAT, VOLCANO, CONE                           | INCORRECT (Max overlap: 3/4 with CONICAL THINGS) | [Pred Type: SEMANTIC_SET (62.9%, no-rel 20.6%)]
4. **Partition Score: 0.3855**
   - Group 1: **0.4432** | BOLT, BLUFF, INHALE, GORGE                                        | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 2: **0.4266** | BLARNEY STONE, VOLCANO, MISTLETOE, NEW YEAR'S EVE                 | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 3: **0.4065** | CHRISTMAS TREE, PARTY HAT, CONE, SCARF                            | INCORRECT (Max overlap: 3/4 with CONICAL THINGS) | [Pred Type: SEMANTIC_SET (70.0%, no-rel 16.1%)]
   - Group 4: **0.3545** | POSTURE, MASQUERADE, WEDDING, FRONT                               | INCORRECT (Max overlap: 3/4 with POSE) | [Pred Type: SYNONYM_OR_NEAR (45.6%, no-rel 28.4%)]
5. **Partition Score: 0.3850**
   - Group 1: **0.6199** | CHRISTMAS TREE, BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE          | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 2: **0.4432** | BOLT, BLUFF, INHALE, GORGE                                        | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 3: **0.3880** | PARTY HAT, VOLCANO, CONE, SCARF                                   | INCORRECT (Max overlap: 3/4 with CONICAL THINGS) | [Pred Type: SEMANTIC_SET (72.1%, no-rel 18.3%)]
   - Group 4: **0.3545** | POSTURE, MASQUERADE, WEDDING, FRONT                               | INCORRECT (Max overlap: 3/4 with POSE) | [Pred Type: SYNONYM_OR_NEAR (45.6%, no-rel 28.4%)]

### Top Candidate Groups:
   - Group 1: **0.4419** | BLARNEY STONE, MISTLETOE, INHALE, NEW YEAR'S EVE                  | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 2: **0.4177** | POSTURE, BOLT, BLUFF, FRONT                                       | INCORRECT (Max overlap: 3/4 with POSE)
   - Group 3: **0.4009** | CHRISTMAS TREE, PARTY HAT, VOLCANO, CONE                          | CORRECT GROUP (CONICAL THINGS, Level 1) | [Pred Type: SEMANTIC_SET (68.9%, no-rel 19.7%)]
   - Group 4: **0.3690** | MASQUERADE, WEDDING, GORGE, SCARF                                 | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 25.1%)]
   - Group 5: **0.4266** | BLARNEY STONE, VOLCANO, MISTLETOE, NEW YEAR'S EVE                 | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 6: **0.4107** | POSTURE, MASQUERADE, WEDDING, BLUFF                               | INCORRECT (Max overlap: 3/4 with POSE)
   - Group 7: **0.4065** | CHRISTMAS TREE, PARTY HAT, CONE, SCARF                            | INCORRECT (Max overlap: 3/4 with CONICAL THINGS) | [Pred Type: SEMANTIC_SET (70.0%, no-rel 16.1%)]
   - Group 8: **0.3662** | BOLT, FRONT, INHALE, GORGE                                        | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 9: **0.4095** | BOLT, BLUFF, GORGE, SCARF                                         | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (46.5%, no-rel 30.9%)]
   - Group 10: **0.4069** | POSTURE, MASQUERADE, FRONT, INHALE                                | INCORRECT (Max overlap: 3/4 with POSE)
   - Group 11: **0.3875** | CHRISTMAS TREE, WEDDING, MISTLETOE, NEW YEAR'S EVE                | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 8.9%)]
   - Group 12: **0.3743** | BLARNEY STONE, PARTY HAT, VOLCANO, CONE                           | INCORRECT (Max overlap: 3/4 with CONICAL THINGS) | [Pred Type: SEMANTIC_SET (62.9%, no-rel 20.6%)]
   - Group 13: **0.4432** | BOLT, BLUFF, INHALE, GORGE                                        | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 14: **0.3545** | POSTURE, MASQUERADE, WEDDING, FRONT                               | INCORRECT (Max overlap: 3/4 with POSE) | [Pred Type: SYNONYM_OR_NEAR (45.6%, no-rel 28.4%)]
   - Group 15: **0.6199** | CHRISTMAS TREE, BLARNEY STONE, MISTLETOE, NEW YEAR'S EVE          | INCORRECT (Max overlap: 3/4 with SETTINGS FOR A KISS)
   - Group 16: **0.3880** | PARTY HAT, VOLCANO, CONE, SCARF                                   | INCORRECT (Max overlap: 3/4 with CONICAL THINGS) | [Pred Type: SEMANTIC_SET (72.1%, no-rel 18.3%)]
   - Group 17: **0.4061** | CHRISTMAS TREE, BLARNEY STONE, VOLCANO, NEW YEAR'S EVE            | INCORRECT (Max overlap: 2/4 with CONICAL THINGS)
   - Group 18: **0.3942** | PARTY HAT, MISTLETOE, CONE, SCARF                                 | INCORRECT (Max overlap: 2/4 with CONICAL THINGS) | [Pred Type: SEMANTIC_SET (59.9%, no-rel 16.6%)]
   - Group 19: **0.4420** | POSTURE, BOLT, INHALE, GORGE                                      | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY)
   - Group 20: **0.3493** | MASQUERADE, WEDDING, BLUFF, FRONT                                 | INCORRECT (Max overlap: 3/4 with POSE)

---

## Puzzle 9 (ID: 926)
**Words on Board:** SOLE, CHEW, MUNCH, BREAD, TANG, PAPER, BITE, CHAR, BACON, SINGE, CHAMP, POLLOCK, HUMP, CHEESE, WHISTLER, RAPT

### Ground Truth Categories:
* **Level 0 (SLANG FOR MONEY) [Type: SYNONYM_OR_NEAR]:** BACON, BREAD, CHEESE, PAPER
* **Level 1 (MASTICATE) [Type: SYNONYM_OR_NEAR]:** BITE, CHAMP, CHEW, MUNCH
* **Level 2 (FISH) [Type: SEMANTIC_SET]:** CHAR, POLLOCK, SOLE, TANG
* **Level 3 (WAYS TO VOCALIZE MUSICALLY PLUS A LETTER) [Type: WORDPLAY_TRANSFORM]:** HUMP, RAPT, SINGE, WHISTLER

### Top Candidate Partitions:
1. **Partition Score: 0.4923**
   - Group 1: **0.7251** | BREAD, PAPER, BACON, CHEESE                                       | CORRECT GROUP (SLANG FOR MONEY, Level 0)
   - Group 2: **0.6476** | CHEW, MUNCH, BITE, CHAMP                                          | CORRECT GROUP (MASTICATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 34.5%)]
   - Group 3: **0.5093** | POLLOCK, HUMP, WHISTLER, RAPT                                     | INCORRECT (Max overlap: 3/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 4: **0.4062** | SOLE, TANG, CHAR, SINGE                                           | INCORRECT (Max overlap: 3/4 with FISH)
2. **Partition Score: 0.4771**
   - Group 1: **0.7251** | BREAD, PAPER, BACON, CHEESE                                       | CORRECT GROUP (SLANG FOR MONEY, Level 0)
   - Group 2: **0.6476** | CHEW, MUNCH, BITE, CHAMP                                          | CORRECT GROUP (MASTICATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 34.5%)]
   - Group 3: **0.4372** | SOLE, TANG, SINGE, RAPT                                           | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 4: **0.4118** | CHAR, POLLOCK, HUMP, WHISTLER                                     | INCORRECT (Max overlap: 2/4 with FISH)
3. **Partition Score: 0.4587**
   - Group 1: **0.6476** | CHEW, MUNCH, BITE, CHAMP                                          | CORRECT GROUP (MASTICATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 34.5%)]
   - Group 2: **0.5789** | BREAD, PAPER, POLLOCK, CHEESE                                     | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 3: **0.4437** | BACON, HUMP, WHISTLER, RAPT                                       | INCORRECT (Max overlap: 3/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 4: **0.4062** | SOLE, TANG, CHAR, SINGE                                           | INCORRECT (Max overlap: 3/4 with FISH)
4. **Partition Score: 0.4510**
   - Group 1: **0.6476** | CHEW, MUNCH, BITE, CHAMP                                          | CORRECT GROUP (MASTICATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 34.5%)]
   - Group 2: **0.5579** | BREAD, BACON, POLLOCK, CHEESE                                     | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 3: **0.4336** | PAPER, HUMP, WHISTLER, RAPT                                       | INCORRECT (Max overlap: 3/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 4: **0.4062** | SOLE, TANG, CHAR, SINGE                                           | INCORRECT (Max overlap: 3/4 with FISH)
5. **Partition Score: 0.4497**
   - Group 1: **0.6476** | CHEW, MUNCH, BITE, CHAMP                                          | CORRECT GROUP (MASTICATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 34.5%)]
   - Group 2: **0.4755** | BREAD, CHAR, BACON, CHEESE                                        | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 3: **0.4490** | PAPER, POLLOCK, HUMP, WHISTLER                                    | INCORRECT (Max overlap: 2/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 4: **0.4372** | SOLE, TANG, SINGE, RAPT                                           | INCORRECT (Max overlap: 2/4 with FISH)

### Top Candidate Groups:
   - Group 1: **0.7251** | BREAD, PAPER, BACON, CHEESE                                       | CORRECT GROUP (SLANG FOR MONEY, Level 0)
   - Group 2: **0.6476** | CHEW, MUNCH, BITE, CHAMP                                          | CORRECT GROUP (MASTICATE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 34.5%)]
   - Group 3: **0.5093** | POLLOCK, HUMP, WHISTLER, RAPT                                     | INCORRECT (Max overlap: 3/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 4: **0.4062** | SOLE, TANG, CHAR, SINGE                                           | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 5: **0.4372** | SOLE, TANG, SINGE, RAPT                                           | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 6: **0.4118** | CHAR, POLLOCK, HUMP, WHISTLER                                     | INCORRECT (Max overlap: 2/4 with FISH)
   - Group 7: **0.5789** | BREAD, PAPER, POLLOCK, CHEESE                                     | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 8: **0.4437** | BACON, HUMP, WHISTLER, RAPT                                       | INCORRECT (Max overlap: 3/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 9: **0.5579** | BREAD, BACON, POLLOCK, CHEESE                                     | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 10: **0.4336** | PAPER, HUMP, WHISTLER, RAPT                                       | INCORRECT (Max overlap: 3/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 11: **0.4755** | BREAD, CHAR, BACON, CHEESE                                        | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 12: **0.4490** | PAPER, POLLOCK, HUMP, WHISTLER                                    | INCORRECT (Max overlap: 2/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 13: **0.4609** | BACON, POLLOCK, HUMP, WHISTLER                                    | INCORRECT (Max overlap: 2/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 14: **0.4507** | BREAD, PAPER, CHAR, CHEESE                                        | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 15: **0.5361** | BREAD, PAPER, BACON, POLLOCK                                      | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 16: **0.4296** | HUMP, CHEESE, WHISTLER, RAPT                                      | INCORRECT (Max overlap: 3/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 17: **0.4112** | SOLE, TANG, CHAR, RAPT                                            | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 18: **0.3589** | SINGE, POLLOCK, HUMP, WHISTLER                                    | INCORRECT (Max overlap: 3/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)
   - Group 19: **0.4974** | BREAD, PAPER, HUMP, CHEESE                                        | INCORRECT (Max overlap: 3/4 with SLANG FOR MONEY)
   - Group 20: **0.4602** | BACON, POLLOCK, WHISTLER, RAPT                                    | INCORRECT (Max overlap: 2/4 with WAYS TO VOCALIZE MUSICALLY PLUS A LETTER)

---

## Puzzle 10 (ID: 1021)
**Words on Board:** PLANK, CALF RAISE, CRUNCH, CHICK FLICK, KIT KAT, ABSENCE, DEFICIT, WIRELESS, SPORTS, FRY COOK, JOLLY ROGER, PLUNGE, CANNON, PINCH, PUSH-UP, CROW'S NEST

### Ground Truth Categories:
* **Level 0 (SHORTAGE) [Type: SYNONYM_OR_NEAR]:** ABSENCE, CRUNCH, DEFICIT, PINCH
* **Level 1 (PARTS OF A PIRATE SHIP) [Type: SEMANTIC_SET]:** CANNON, CROW'S NEST, JOLLY ROGER, PLANK
* **Level 2 (KINDS OF BRAS) [Type: SEMANTIC_SET]:** PLUNGE, PUSH-UP, SPORTS, WIRELESS
* **Level 3 (STARTING WITH BABY ANIMALS) [Type: WORDPLAY_TRANSFORM]:** CALF RAISE, CHICK FLICK, FRY COOK, KIT KAT

### Top Candidate Partitions:
1. **Partition Score: 0.4379**
   - Group 1: **0.5606** | CALF RAISE, CHICK FLICK, JOLLY ROGER, CROW'S NEST                 | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 2: **0.4485** | KIT KAT, WIRELESS, FRY COOK, CANNON                               | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 3: **0.4378** | PLANK, SPORTS, PLUNGE, PUSH-UP                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BRAS) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 22.2%)]
   - Group 4: **0.4327** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
2. **Partition Score: 0.4368**
   - Group 1: **0.4446** | KIT KAT, WIRELESS, JOLLY ROGER, CROW'S NEST                       | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)
   - Group 2: **0.4440** | CALF RAISE, CHICK FLICK, FRY COOK, CANNON                         | INCORRECT (Max overlap: 3/4 with STARTING WITH BABY ANIMALS)
   - Group 3: **0.4378** | PLANK, SPORTS, PLUNGE, PUSH-UP                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BRAS) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 22.2%)]
   - Group 4: **0.4327** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
3. **Partition Score: 0.4344**
   - Group 1: **0.4429** | KIT KAT, WIRELESS, FRY COOK, CROW'S NEST                          | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 2: **0.4378** | PLANK, SPORTS, PLUNGE, PUSH-UP                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BRAS) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 22.2%)]
   - Group 3: **0.4347** | CALF RAISE, CHICK FLICK, JOLLY ROGER, CANNON                      | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 4: **0.4327** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
4. **Partition Score: 0.4332**
   - Group 1: **0.4788** | KIT KAT, WIRELESS, FRY COOK, JOLLY ROGER                          | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 2: **0.4378** | PLANK, SPORTS, PLUNGE, PUSH-UP                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BRAS) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 22.2%)]
   - Group 3: **0.4327** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
   - Group 4: **0.4312** | CALF RAISE, CHICK FLICK, CANNON, CROW'S NEST                      | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
5. **Partition Score: 0.4331**
   - Group 1: **0.5888** | CALF RAISE, CHICK FLICK, KIT KAT, CROW'S NEST                     | INCORRECT (Max overlap: 3/4 with STARTING WITH BABY ANIMALS)
   - Group 2: **0.4378** | PLANK, SPORTS, PLUNGE, PUSH-UP                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BRAS) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 22.2%)]
   - Group 3: **0.4327** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
   - Group 4: **0.4310** | WIRELESS, FRY COOK, JOLLY ROGER, CANNON                           | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)

### Top Candidate Groups:
   - Group 1: **0.5606** | CALF RAISE, CHICK FLICK, JOLLY ROGER, CROW'S NEST                 | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 2: **0.4485** | KIT KAT, WIRELESS, FRY COOK, CANNON                               | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 3: **0.4378** | PLANK, SPORTS, PLUNGE, PUSH-UP                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BRAS) | [Pred Type: SEMANTIC_SET (49.1%, no-rel 22.2%)]
   - Group 4: **0.4327** | CRUNCH, ABSENCE, DEFICIT, PINCH                                   | CORRECT GROUP (SHORTAGE, Level 0)
   - Group 5: **0.4446** | KIT KAT, WIRELESS, JOLLY ROGER, CROW'S NEST                       | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)
   - Group 6: **0.4440** | CALF RAISE, CHICK FLICK, FRY COOK, CANNON                         | INCORRECT (Max overlap: 3/4 with STARTING WITH BABY ANIMALS)
   - Group 7: **0.4429** | KIT KAT, WIRELESS, FRY COOK, CROW'S NEST                          | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 8: **0.4347** | CALF RAISE, CHICK FLICK, JOLLY ROGER, CANNON                      | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 9: **0.4788** | KIT KAT, WIRELESS, FRY COOK, JOLLY ROGER                          | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 10: **0.4312** | CALF RAISE, CHICK FLICK, CANNON, CROW'S NEST                      | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 11: **0.5888** | CALF RAISE, CHICK FLICK, KIT KAT, CROW'S NEST                     | INCORRECT (Max overlap: 3/4 with STARTING WITH BABY ANIMALS)
   - Group 12: **0.4310** | WIRELESS, FRY COOK, JOLLY ROGER, CANNON                           | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)
   - Group 13: **0.5710** | CALF RAISE, CHICK FLICK, KIT KAT, JOLLY ROGER                     | INCORRECT (Max overlap: 3/4 with STARTING WITH BABY ANIMALS)
   - Group 14: **0.4268** | WIRELESS, FRY COOK, CANNON, CROW'S NEST                           | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)
   - Group 15: **0.5512** | CALF RAISE, CHICK FLICK, FRY COOK, CROW'S NEST                    | INCORRECT (Max overlap: 3/4 with STARTING WITH BABY ANIMALS)
   - Group 16: **0.4246** | KIT KAT, WIRELESS, JOLLY ROGER, CANNON                            | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)
   - Group 17: **0.4532** | CALF RAISE, CHICK FLICK, KIT KAT, CANNON                          | INCORRECT (Max overlap: 3/4 with STARTING WITH BABY ANIMALS)
   - Group 18: **0.4240** | WIRELESS, FRY COOK, JOLLY ROGER, CROW'S NEST                      | INCORRECT (Max overlap: 2/4 with PARTS OF A PIRATE SHIP)
   - Group 19: **0.5885** | CHICK FLICK, KIT KAT, JOLLY ROGER, CROW'S NEST                    | INCORRECT (Max overlap: 2/4 with STARTING WITH BABY ANIMALS)
   - Group 20: **0.4599** | WIRELESS, SPORTS, FRY COOK, CANNON                                | INCORRECT (Max overlap: 2/4 with KINDS OF BRAS)

---

## Puzzle 11 (ID: 434)
**Words on Board:** NERD, GRUMP, RUNT, WHAT IF, SLEEP, SAY, DO, SNOOZE, ALARM, PERHAPS, DOPE, SUPPOSE, TIME SET, KISS, HOUR, WHOPPER

### Ground Truth Categories:
* **Level 0 (ALARM CLOCK BUTTONS) [Type: SEMANTIC_SET]:** ALARM, HOUR, SNOOZE, TIME SET
* **Level 1 (“HERE’S A THOUGHT ...”) [Type: SYNONYM_OR_NEAR]:** PERHAPS, SAY, SUPPOSE, WHAT IF
* **Level 2 (CANDY PIECES) [Type: NAMED_ENTITY_SET]:** KISS, NERD, RUNT, WHOPPER
* **Level 3 (SEVEN DWARFS MINUS LAST LETTER) [Type: WORDPLAY_TRANSFORM]:** DO, DOPE, GRUMP, SLEEP

### Top Candidate Partitions:
1. **Partition Score: 0.4194**
   - Group 1: **0.4480** | SLEEP, SNOOZE, ALARM, KISS                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 2: **0.4455** | WHAT IF, SAY, PERHAPS, SUPPOSE                                    | CORRECT GROUP (“HERE’S A THOUGHT ...”, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 31.1%)]
   - Group 3: **0.4379** | GRUMP, TIME SET, HOUR, WHOPPER                                    | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 4: **0.3971** | NERD, RUNT, DO, DOPE                                              | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
2. **Partition Score: 0.4118**
   - Group 1: **0.4480** | SLEEP, SNOOZE, ALARM, KISS                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 2: **0.4455** | WHAT IF, SAY, PERHAPS, SUPPOSE                                    | CORRECT GROUP (“HERE’S A THOUGHT ...”, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 31.1%)]
   - Group 3: **0.4025** | DOPE, TIME SET, HOUR, WHOPPER                                     | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 4: **0.3996** | NERD, GRUMP, RUNT, DO                                             | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
3. **Partition Score: 0.4043**
   - Group 1: **0.4480** | SLEEP, SNOOZE, ALARM, KISS                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 2: **0.4455** | WHAT IF, SAY, PERHAPS, SUPPOSE                                    | CORRECT GROUP (“HERE’S A THOUGHT ...”, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 31.1%)]
   - Group 3: **0.4176** | NERD, GRUMP, RUNT, TIME SET                                       | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 4: **0.3769** | DO, DOPE, HOUR, WHOPPER                                           | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
4. **Partition Score: 0.4018**
   - Group 1: **0.4568** | NERD, GRUMP, RUNT, WHOPPER                                        | INCORRECT (Max overlap: 3/4 with CANDY PIECES)
   - Group 2: **0.4480** | SLEEP, SNOOZE, ALARM, KISS                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 3: **0.4455** | WHAT IF, SAY, PERHAPS, SUPPOSE                                    | CORRECT GROUP (“HERE’S A THOUGHT ...”, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 31.1%)]
   - Group 4: **0.3568** | DO, DOPE, TIME SET, HOUR                                          | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
5. **Partition Score: 0.4005**
   - Group 1: **0.4526** | RUNT, SLEEP, SNOOZE, ALARM                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 2: **0.4455** | WHAT IF, SAY, PERHAPS, SUPPOSE                                    | CORRECT GROUP (“HERE’S A THOUGHT ...”, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 31.1%)]
   - Group 3: **0.4379** | GRUMP, TIME SET, HOUR, WHOPPER                                    | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 4: **0.3594** | NERD, DO, DOPE, KISS                                              | INCORRECT (Max overlap: 2/4 with CANDY PIECES)

### Top Candidate Groups:
   - Group 1: **0.4480** | SLEEP, SNOOZE, ALARM, KISS                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 2: **0.4455** | WHAT IF, SAY, PERHAPS, SUPPOSE                                    | CORRECT GROUP (“HERE’S A THOUGHT ...”, Level 1) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 31.1%)]
   - Group 3: **0.4379** | GRUMP, TIME SET, HOUR, WHOPPER                                    | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 4: **0.3971** | NERD, RUNT, DO, DOPE                                              | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 5: **0.4025** | DOPE, TIME SET, HOUR, WHOPPER                                     | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 6: **0.3996** | NERD, GRUMP, RUNT, DO                                             | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 7: **0.4176** | NERD, GRUMP, RUNT, TIME SET                                       | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 8: **0.3769** | DO, DOPE, HOUR, WHOPPER                                           | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 9: **0.4568** | NERD, GRUMP, RUNT, WHOPPER                                        | INCORRECT (Max overlap: 3/4 with CANDY PIECES)
   - Group 10: **0.3568** | DO, DOPE, TIME SET, HOUR                                          | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 11: **0.4526** | RUNT, SLEEP, SNOOZE, ALARM                                        | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 12: **0.3594** | NERD, DO, DOPE, KISS                                              | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 13: **0.4259** | NERD, DO, DOPE, WHOPPER                                           | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 14: **0.3580** | GRUMP, RUNT, TIME SET, HOUR                                       | INCORRECT (Max overlap: 2/4 with ALARM CLOCK BUTTONS)
   - Group 15: **0.4128** | GRUMP, RUNT, TIME SET, WHOPPER                                    | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 16: **0.3644** | NERD, DO, DOPE, HOUR                                              | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 17: **0.5347** | SLEEP, SNOOZE, ALARM, HOUR                                        | INCORRECT (Max overlap: 3/4 with ALARM CLOCK BUTTONS)
   - Group 18: **0.3618** | DO, DOPE, KISS, WHOPPER                                           | INCORRECT (Max overlap: 2/4 with SEVEN DWARFS MINUS LAST LETTER)
   - Group 19: **0.3837** | NERD, TIME SET, HOUR, WHOPPER                                     | INCORRECT (Max overlap: 2/4 with CANDY PIECES)
   - Group 20: **0.3772** | GRUMP, RUNT, DO, DOPE                                             | INCORRECT (Max overlap: 3/4 with SEVEN DWARFS MINUS LAST LETTER)

---

## Puzzle 12 (ID: 622)
**Words on Board:** GLITTER, GOOSE, PAPER, CELTIC, PACKER, CURL, YANKEE, ROD, FEATHER, PARACHUTE, CRIMP, MACARONI, TEASE, DOODLE, CANADIEN, GLUE

### Ground Truth Categories:
* **Level 0 (MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS) [Type: NAMED_ENTITY_SET]:** CANADIEN, CELTIC, PACKER, YANKEE
* **Level 1 (CREATE SOME VOLUME/TEXTURE IN HAIR) [Type: SYNONYM_OR_NEAR]:** CRIMP, CURL, FEATHER, TEASE
* **Level 2 (SUPPLIES FOR MACARONI ART) [Type: SEMANTIC_SET]:** GLITTER, GLUE, MACARONI, PAPER
* **Level 3 (WORDS AFTER “GOLDEN”) [Type: FILL_IN_THE_BLANK]:** DOODLE, GOOSE, PARACHUTE, ROD

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.5647** | CELTIC, PACKER, YANKEE, CANADIEN                                  | CORRECT GROUP (MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS, Level 0)
   - Group 2: **0.5380** | CELTIC, PACKER, YANKEE, MACARONI                                  | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 3: **0.5356** | GOOSE, CELTIC, PACKER, YANKEE                                     | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 4: **0.5317** | CELTIC, YANKEE, MACARONI, CANADIEN                                | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 5: **0.5277** | CELTIC, PACKER, MACARONI, CANADIEN                                | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 6: **0.5181** | PACKER, YANKEE, MACARONI, CANADIEN                                | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 7: **0.5033** | GOOSE, CELTIC, YANKEE, CANADIEN                                   | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 8: **0.5011** | GOOSE, CELTIC, PACKER, CANADIEN                                   | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 9: **0.4974** | CELTIC, PARACHUTE, MACARONI, CANADIEN                             | INCORRECT (Max overlap: 2/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 10: **0.4925** | GOOSE, PACKER, YANKEE, ROD                                        | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 11: **0.4890** | CELTIC, PACKER, PARACHUTE, CANADIEN                               | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 12: **0.4868** | CELTIC, PACKER, YANKEE, PARACHUTE                                 | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 13: **0.4838** | GLITTER, CELTIC, PARACHUTE, MACARONI                              | INCORRECT (Max overlap: 2/4 with SUPPLIES FOR MACARONI ART)
   - Group 14: **0.4821** | GOOSE, CELTIC, PARACHUTE, CANADIEN                                | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 15: **0.4796** | CELTIC, YANKEE, PARACHUTE, CANADIEN                               | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 16: **0.4783** | GOOSE, CELTIC, YANKEE, MACARONI                                   | INCORRECT (Max overlap: 2/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 17: **0.4770** | GLITTER, CELTIC, YANKEE, MACARONI                                 | INCORRECT (Max overlap: 2/4 with SUPPLIES FOR MACARONI ART)
   - Group 18: **0.4765** | GOOSE, CELTIC, YANKEE, PARACHUTE                                  | INCORRECT (Max overlap: 2/4 with WORDS AFTER “GOLDEN”)
   - Group 19: **0.4754** | GOOSE, PACKER, YANKEE, CANADIEN                                   | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)
   - Group 20: **0.4751** | CELTIC, PACKER, YANKEE, ROD                                       | INCORRECT (Max overlap: 3/4 with MEMBER OF A TEAM WITH THE MOST CHAMPIONSHIPS IN THEIR RESPECTIVE SPORTS)

---

## Puzzle 13 (ID: 541)
**Words on Board:** OSCAR, CUZ, CECE, JUNIOR, EDIE, EMMY, TONY, COUNT, GRAMMY, COOKIE, KATIE, MEADOW, MUMMY, POP, CARMELA, SNUFFY

### Ground Truth Categories:
* **Level 0 (SOPRANOS) [Type: NAMED_ENTITY_SET]:** CARMELA, JUNIOR, MEADOW, TONY
* **Level 1 (FAMILIAL NICKNAMES) [Type: SYNONYM_OR_NEAR]:** CUZ, GRAMMY, MUMMY, POP
* **Level 2 (“SESAME STREET” CHARACTERS) [Type: NAMED_ENTITY_SET]:** COOKIE, COUNT, OSCAR, SNUFFY
* **Level 3 (NAMES THAT SOUND LIKE TWO LETTERS) [Type: SOUND_OR_SPELLING]:** CECE, EDIE, EMMY, KATIE

### Top Candidate Partitions:
1. **Partition Score: 0.4759**
   - Group 1: **0.5396** | TONY, KATIE, MEADOW, CARMELA                                      | INCORRECT (Max overlap: 3/4 with SOPRANOS)
   - Group 2: **0.5073** | OSCAR, EDIE, EMMY, GRAMMY                                         | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 3: **0.4847** | JUNIOR, COUNT, COOKIE, MUMMY                                      | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS) | [Pred Type: FILL_IN_THE_BLANK (50.6%, no-rel 11.9%)]
   - Group 4: **0.4559** | CUZ, CECE, POP, SNUFFY                                            | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
2. **Partition Score: 0.4736**
   - Group 1: **0.5384** | EDIE, TONY, KATIE, MEADOW                                         | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 2: **0.4979** | OSCAR, EMMY, GRAMMY, CARMELA                                      | INCORRECT (Max overlap: 1/4 with “SESAME STREET” CHARACTERS)
   - Group 3: **0.4847** | JUNIOR, COUNT, COOKIE, MUMMY                                      | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS) | [Pred Type: FILL_IN_THE_BLANK (50.6%, no-rel 11.9%)]
   - Group 4: **0.4559** | CUZ, CECE, POP, SNUFFY                                            | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
3. **Partition Score: 0.4720**
   - Group 1: **0.5396** | TONY, KATIE, MEADOW, CARMELA                                      | INCORRECT (Max overlap: 3/4 with SOPRANOS)
   - Group 2: **0.5073** | OSCAR, EDIE, EMMY, GRAMMY                                         | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 3: **0.5058** | CUZ, CECE, COUNT, SNUFFY                                          | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 4: **0.4375** | JUNIOR, COOKIE, MUMMY, POP                                        | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
4. **Partition Score: 0.4697**
   - Group 1: **0.5384** | EDIE, TONY, KATIE, MEADOW                                         | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 2: **0.5058** | CUZ, CECE, COUNT, SNUFFY                                          | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 3: **0.4979** | OSCAR, EMMY, GRAMMY, CARMELA                                      | INCORRECT (Max overlap: 1/4 with “SESAME STREET” CHARACTERS)
   - Group 4: **0.4375** | JUNIOR, COOKIE, MUMMY, POP                                        | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
5. **Partition Score: 0.4634**
   - Group 1: **0.5601** | EDIE, KATIE, MEADOW, CARMELA                                      | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 2: **0.4847** | JUNIOR, COUNT, COOKIE, MUMMY                                      | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS) | [Pred Type: FILL_IN_THE_BLANK (50.6%, no-rel 11.9%)]
   - Group 3: **0.4572** | OSCAR, EMMY, TONY, GRAMMY                                         | INCORRECT (Max overlap: 1/4 with “SESAME STREET” CHARACTERS)
   - Group 4: **0.4559** | CUZ, CECE, POP, SNUFFY                                            | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)

### Top Candidate Groups:
   - Group 1: **0.5396** | TONY, KATIE, MEADOW, CARMELA                                      | INCORRECT (Max overlap: 3/4 with SOPRANOS)
   - Group 2: **0.5073** | OSCAR, EDIE, EMMY, GRAMMY                                         | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 3: **0.4847** | JUNIOR, COUNT, COOKIE, MUMMY                                      | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS) | [Pred Type: FILL_IN_THE_BLANK (50.6%, no-rel 11.9%)]
   - Group 4: **0.4559** | CUZ, CECE, POP, SNUFFY                                            | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 5: **0.5384** | EDIE, TONY, KATIE, MEADOW                                         | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 6: **0.4979** | OSCAR, EMMY, GRAMMY, CARMELA                                      | INCORRECT (Max overlap: 1/4 with “SESAME STREET” CHARACTERS)
   - Group 7: **0.5058** | CUZ, CECE, COUNT, SNUFFY                                          | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 8: **0.4375** | JUNIOR, COOKIE, MUMMY, POP                                        | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 9: **0.5601** | EDIE, KATIE, MEADOW, CARMELA                                      | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 10: **0.4572** | OSCAR, EMMY, TONY, GRAMMY                                         | INCORRECT (Max overlap: 1/4 with “SESAME STREET” CHARACTERS)
   - Group 11: **0.4782** | COUNT, COOKIE, MUMMY, SNUFFY                                      | INCORRECT (Max overlap: 3/4 with “SESAME STREET” CHARACTERS)
   - Group 12: **0.4246** | CUZ, CECE, JUNIOR, POP                                            | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 13: **0.4490** | CUZ, CECE, JUNIOR, COUNT                                          | INCORRECT (Max overlap: 1/4 with FAMILIAL NICKNAMES)
   - Group 14: **0.4380** | COOKIE, MUMMY, POP, SNUFFY                                        | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 15: **0.4659** | JUNIOR, COUNT, COOKIE, POP                                        | INCORRECT (Max overlap: 2/4 with “SESAME STREET” CHARACTERS)
   - Group 16: **0.4270** | CUZ, CECE, MUMMY, SNUFFY                                          | INCORRECT (Max overlap: 2/4 with FAMILIAL NICKNAMES)
   - Group 17: **0.4768** | COUNT, COOKIE, POP, SNUFFY                                        | INCORRECT (Max overlap: 3/4 with “SESAME STREET” CHARACTERS)
   - Group 18: **0.4530** | CUZ, CECE, EDIE, TONY                                             | INCORRECT (Max overlap: 2/4 with NAMES THAT SOUND LIKE TWO LETTERS)
   - Group 19: **0.4484** | JUNIOR, KATIE, MEADOW, MUMMY                                      | INCORRECT (Max overlap: 2/4 with SOPRANOS)
   - Group 20: **0.5284** | EDIE, TONY, MEADOW, CARMELA                                       | INCORRECT (Max overlap: 3/4 with SOPRANOS)

---

## Puzzle 14 (ID: 1005)
**Words on Board:** SPORK, FROG, CORNER, SPROCKET, SMOG, BOGART, MONOPOLIZE, HOG, GEAR, COG, MOTEL, DOZE, BLOG, PINION, DOG, HORN

### Ground Truth Categories:
* **Level 0 (GREEDILY CONTROL) [Type: SYNONYM_OR_NEAR]:** BOGART, CORNER, HOG, MONOPOLIZE
* **Level 1 (TOOTHED WHEELS) [Type: SEMANTIC_SET]:** COG, GEAR, PINION, SPROCKET
* **Level 2 (PORTMANTEAUX) [Type: WORDPLAY_TRANSFORM]:** BLOG, MOTEL, SMOG, SPORK
* **Level 3 (BULL___) [Type: FILL_IN_THE_BLANK]:** DOG, DOZE, FROG, HORN

### Top Candidate Partitions:
1. **Partition Score: 0.5464**
   - Group 1: **0.6923** | SPROCKET, GEAR, COG, PINION                                       | CORRECT GROUP (TOOTHED WHEELS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 30.7%)]
   - Group 2: **0.5598** | CORNER, MONOPOLIZE, HOG, DOG                                      | INCORRECT (Max overlap: 3/4 with GREEDILY CONTROL)
   - Group 3: **0.5455** | BOGART, DOZE, BLOG, HORN                                          | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 4: **0.5403** | SPORK, FROG, SMOG, MOTEL                                          | INCORRECT (Max overlap: 3/4 with PORTMANTEAUX)
2. **Partition Score: 0.5437**
   - Group 1: **0.6923** | SPROCKET, GEAR, COG, PINION                                       | CORRECT GROUP (TOOTHED WHEELS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 30.7%)]
   - Group 2: **0.5775** | BOGART, HOG, DOZE, BLOG                                           | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
   - Group 3: **0.5403** | SPORK, FROG, SMOG, MOTEL                                          | INCORRECT (Max overlap: 3/4 with PORTMANTEAUX)
   - Group 4: **0.5286** | CORNER, MONOPOLIZE, DOG, HORN                                     | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
3. **Partition Score: 0.5417**
   - Group 1: **0.6923** | SPROCKET, GEAR, COG, PINION                                       | CORRECT GROUP (TOOTHED WHEELS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 30.7%)]
   - Group 2: **0.5569** | FROG, BOGART, HOG, BLOG                                           | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
   - Group 3: **0.5529** | SPORK, SMOG, MOTEL, DOZE                                          | INCORRECT (Max overlap: 3/4 with PORTMANTEAUX)
   - Group 4: **0.5286** | CORNER, MONOPOLIZE, DOG, HORN                                     | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
4. **Partition Score: 0.5381**
   - Group 1: **0.6923** | SPROCKET, GEAR, COG, PINION                                       | CORRECT GROUP (TOOTHED WHEELS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 30.7%)]
   - Group 2: **0.5403** | SPORK, FROG, SMOG, MOTEL                                          | INCORRECT (Max overlap: 3/4 with PORTMANTEAUX)
   - Group 3: **0.5389** | CORNER, MONOPOLIZE, HOG, HORN                                     | INCORRECT (Max overlap: 3/4 with GREEDILY CONTROL)
   - Group 4: **0.5367** | BOGART, DOZE, BLOG, DOG                                           | INCORRECT (Max overlap: 2/4 with BULL___)
5. **Partition Score: 0.5364**
   - Group 1: **0.6923** | SPROCKET, GEAR, COG, PINION                                       | CORRECT GROUP (TOOTHED WHEELS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 30.7%)]
   - Group 2: **0.5529** | SPORK, SMOG, MOTEL, DOZE                                          | INCORRECT (Max overlap: 3/4 with PORTMANTEAUX)
   - Group 3: **0.5389** | CORNER, MONOPOLIZE, HOG, HORN                                     | INCORRECT (Max overlap: 3/4 with GREEDILY CONTROL)
   - Group 4: **0.5269** | FROG, BOGART, BLOG, DOG                                           | INCORRECT (Max overlap: 2/4 with BULL___)

### Top Candidate Groups:
   - Group 1: **0.6923** | SPROCKET, GEAR, COG, PINION                                       | CORRECT GROUP (TOOTHED WHEELS, Level 1) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 30.7%)]
   - Group 2: **0.5598** | CORNER, MONOPOLIZE, HOG, DOG                                      | INCORRECT (Max overlap: 3/4 with GREEDILY CONTROL)
   - Group 3: **0.5455** | BOGART, DOZE, BLOG, HORN                                          | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 4: **0.5403** | SPORK, FROG, SMOG, MOTEL                                          | INCORRECT (Max overlap: 3/4 with PORTMANTEAUX)
   - Group 5: **0.5775** | BOGART, HOG, DOZE, BLOG                                           | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
   - Group 6: **0.5286** | CORNER, MONOPOLIZE, DOG, HORN                                     | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
   - Group 7: **0.5569** | FROG, BOGART, HOG, BLOG                                           | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
   - Group 8: **0.5529** | SPORK, SMOG, MOTEL, DOZE                                          | INCORRECT (Max overlap: 3/4 with PORTMANTEAUX)
   - Group 9: **0.5389** | CORNER, MONOPOLIZE, HOG, HORN                                     | INCORRECT (Max overlap: 3/4 with GREEDILY CONTROL)
   - Group 10: **0.5367** | BOGART, DOZE, BLOG, DOG                                           | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 11: **0.5269** | FROG, BOGART, BLOG, DOG                                           | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 12: **0.5389** | SPROCKET, MONOPOLIZE, GEAR, COG                                   | INCORRECT (Max overlap: 3/4 with TOOTHED WHEELS) | [Pred Type: SYNONYM_OR_NEAR (52.5%, no-rel 32.4%)]
   - Group 13: **0.5154** | CORNER, PINION, DOG, HORN                                         | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 14: **0.6068** | CORNER, SPROCKET, GEAR, PINION                                    | INCORRECT (Max overlap: 3/4 with TOOTHED WHEELS)
   - Group 15: **0.5150** | MONOPOLIZE, HOG, COG, DOG                                         | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)
   - Group 16: **0.5816** | CORNER, COG, DOG, HORN                                            | INCORRECT (Max overlap: 2/4 with BULL___)
   - Group 17: **0.4979** | SPROCKET, MONOPOLIZE, GEAR, PINION                                | INCORRECT (Max overlap: 3/4 with TOOTHED WHEELS)
   - Group 18: **0.5254** | SPROCKET, GEAR, PINION, HORN                                      | INCORRECT (Max overlap: 3/4 with TOOTHED WHEELS)
   - Group 19: **0.5211** | CORNER, MONOPOLIZE, HOG, COG                                      | INCORRECT (Max overlap: 3/4 with GREEDILY CONTROL)
   - Group 20: **0.5119** | CORNER, MONOPOLIZE, COG, DOG                                      | INCORRECT (Max overlap: 2/4 with GREEDILY CONTROL)

---

## Puzzle 15 (ID: 170)
**Words on Board:** ISLAND, CRAM, KEY, BAG, BEDROOM, ATOLL, KITCHEN, PACK, STUDY, DEN, SPROUT, BAR, JAM, COUNTER, DIP, STUFF

### Ground Truth Categories:
* **Level 0 (ROOMS IN A HOUSE) [Type: SEMANTIC_SET]:** BEDROOM, DEN, KITCHEN, STUDY
* **Level 1 (LAND SURROUNDED BY WATER) [Type: SEMANTIC_SET]:** ATOLL, BAR, ISLAND, KEY
* **Level 2 (FILL TO EXCESS) [Type: SYNONYM_OR_NEAR]:** CRAM, JAM, PACK, STUFF
* **Level 3 (BEAN ___) [Type: FILL_IN_THE_BLANK]:** BAG, COUNTER, DIP, SPROUT

### Top Candidate Partitions:
1. **Partition Score: 0.3517**
   - Group 1: **0.5426** | CRAM, PACK, JAM, STUFF                                            | CORRECT GROUP (FILL TO EXCESS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 36.2%)]
   - Group 2: **0.4477** | BEDROOM, STUDY, DEN, BAR                                          | INCORRECT (Max overlap: 3/4 with ROOMS IN A HOUSE)
   - Group 3: **0.3783** | ISLAND, ATOLL, KITCHEN, SPROUT                                    | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 4: **0.2903** | KEY, BAG, COUNTER, DIP                                            | INCORRECT (Max overlap: 3/4 with BEAN ___)
2. **Partition Score: 0.3506**
   - Group 1: **0.5426** | CRAM, PACK, JAM, STUFF                                            | CORRECT GROUP (FILL TO EXCESS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 36.2%)]
   - Group 2: **0.4031** | ISLAND, BEDROOM, ATOLL, KITCHEN                                   | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER) | [Pred Type: SEMANTIC_SET (55.1%, no-rel 25.8%)]
   - Group 3: **0.3335** | KEY, BAG, SPROUT, DIP                                             | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 4: **0.3328** | STUDY, DEN, BAR, COUNTER                                          | INCORRECT (Max overlap: 2/4 with ROOMS IN A HOUSE) | [Pred Type: SYNONYM_OR_NEAR (48.9%, no-rel 22.3%)]
3. **Partition Score: 0.3490**
   - Group 1: **0.5426** | CRAM, PACK, JAM, STUFF                                            | CORRECT GROUP (FILL TO EXCESS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 36.2%)]
   - Group 2: **0.4477** | BEDROOM, STUDY, DEN, BAR                                          | INCORRECT (Max overlap: 3/4 with ROOMS IN A HOUSE)
   - Group 3: **0.3594** | ISLAND, KEY, ATOLL, KITCHEN                                       | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER) | [Pred Type: SEMANTIC_SET (49.7%, no-rel 24.2%)]
   - Group 4: **0.2946** | BAG, SPROUT, COUNTER, DIP                                         | CORRECT GROUP (BEAN ___, Level 3)
4. **Partition Score: 0.3466**
   - Group 1: **0.5426** | CRAM, PACK, JAM, STUFF                                            | CORRECT GROUP (FILL TO EXCESS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 36.2%)]
   - Group 2: **0.4031** | ISLAND, BEDROOM, ATOLL, KITCHEN                                   | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER) | [Pred Type: SEMANTIC_SET (55.1%, no-rel 25.8%)]
   - Group 3: **0.3377** | BAG, DEN, SPROUT, DIP                                             | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 4: **0.3227** | KEY, STUDY, BAR, COUNTER                                          | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
5. **Partition Score: 0.3461**
   - Group 1: **0.5426** | CRAM, PACK, JAM, STUFF                                            | CORRECT GROUP (FILL TO EXCESS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 36.2%)]
   - Group 2: **0.4327** | BEDROOM, KITCHEN, STUDY, DEN                                      | CORRECT GROUP (ROOMS IN A HOUSE, Level 0) | [Pred Type: SEMANTIC_SET (51.1%, no-rel 19.1%)]
   - Group 3: **0.3624** | ISLAND, KEY, ATOLL, BAR                                           | CORRECT GROUP (LAND SURROUNDED BY WATER, Level 1) | [Pred Type: SEMANTIC_SET (53.6%, no-rel 19.2%)]
   - Group 4: **0.2946** | BAG, SPROUT, COUNTER, DIP                                         | CORRECT GROUP (BEAN ___, Level 3)

### Top Candidate Groups:
   - Group 1: **0.5426** | CRAM, PACK, JAM, STUFF                                            | CORRECT GROUP (FILL TO EXCESS, Level 2) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 36.2%)]
   - Group 2: **0.4477** | BEDROOM, STUDY, DEN, BAR                                          | INCORRECT (Max overlap: 3/4 with ROOMS IN A HOUSE)
   - Group 3: **0.3783** | ISLAND, ATOLL, KITCHEN, SPROUT                                    | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 4: **0.2903** | KEY, BAG, COUNTER, DIP                                            | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 5: **0.4031** | ISLAND, BEDROOM, ATOLL, KITCHEN                                   | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER) | [Pred Type: SEMANTIC_SET (55.1%, no-rel 25.8%)]
   - Group 6: **0.3335** | KEY, BAG, SPROUT, DIP                                             | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 7: **0.3328** | STUDY, DEN, BAR, COUNTER                                          | INCORRECT (Max overlap: 2/4 with ROOMS IN A HOUSE) | [Pred Type: SYNONYM_OR_NEAR (48.9%, no-rel 22.3%)]
   - Group 8: **0.3594** | ISLAND, KEY, ATOLL, KITCHEN                                       | INCORRECT (Max overlap: 3/4 with LAND SURROUNDED BY WATER) | [Pred Type: SEMANTIC_SET (49.7%, no-rel 24.2%)]
   - Group 9: **0.2946** | BAG, SPROUT, COUNTER, DIP                                         | CORRECT GROUP (BEAN ___, Level 3)
   - Group 10: **0.3377** | BAG, DEN, SPROUT, DIP                                             | INCORRECT (Max overlap: 3/4 with BEAN ___)
   - Group 11: **0.3227** | KEY, STUDY, BAR, COUNTER                                          | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 12: **0.4327** | BEDROOM, KITCHEN, STUDY, DEN                                      | CORRECT GROUP (ROOMS IN A HOUSE, Level 0) | [Pred Type: SEMANTIC_SET (51.1%, no-rel 19.1%)]
   - Group 13: **0.3624** | ISLAND, KEY, ATOLL, BAR                                           | CORRECT GROUP (LAND SURROUNDED BY WATER, Level 1) | [Pred Type: SEMANTIC_SET (53.6%, no-rel 19.2%)]
   - Group 14: **0.4709** | BEDROOM, KITCHEN, STUDY, BAR                                      | INCORRECT (Max overlap: 3/4 with ROOMS IN A HOUSE) | [Pred Type: SEMANTIC_SET (55.0%, no-rel 21.5%)]
   - Group 15: **0.3112** | ISLAND, ATOLL, DEN, SPROUT                                        | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 16: **0.3277** | BEDROOM, STUDY, BAR, COUNTER                                      | INCORRECT (Max overlap: 2/4 with ROOMS IN A HOUSE)
   - Group 17: **0.3908** | KITCHEN, STUDY, BAR, COUNTER                                      | INCORRECT (Max overlap: 2/4 with ROOMS IN A HOUSE)
   - Group 18: **0.3124** | ISLAND, BEDROOM, ATOLL, DEN                                       | INCORRECT (Max overlap: 2/4 with LAND SURROUNDED BY WATER)
   - Group 19: **0.5381** | BAG, PACK, JAM, STUFF                                             | INCORRECT (Max overlap: 3/4 with FILL TO EXCESS)
   - Group 20: **0.4684** | ISLAND, BEDROOM, KITCHEN, DEN                                     | INCORRECT (Max overlap: 3/4 with ROOMS IN A HOUSE) | [Pred Type: SEMANTIC_SET (54.1%, no-rel 23.7%)]

---

## Puzzle 16 (ID: 563)
**Words on Board:** JENNY, RUDOLPH, ROBIN HOOD, FEY, STRONG, CUPID, VIXEN, SAGITTARIUS, STAR, SHANNON, HAWKEYE, MOON, PLANET, COMET, QUEEN, NANNY

### Ground Truth Categories:
* **Level 0 (CELESTIAL OBJECTS) [Type: SEMANTIC_SET]:** COMET, MOON, PLANET, STAR
* **Level 1 (ARCHERS) [Type: NAMED_ENTITY_SET]:** CUPID, HAWKEYE, ROBIN HOOD, SAGITTARIUS
* **Level 2 (FEMALE ANIMALS) [Type: SEMANTIC_SET]:** JENNY, NANNY, QUEEN, VIXEN
* **Level 3 (“S.N.L.” CAST MEMBERS) [Type: NAMED_ENTITY_SET]:** FEY, RUDOLPH, SHANNON, STRONG

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.5697** | STAR, MOON, PLANET, COMET                                         | CORRECT GROUP (CELESTIAL OBJECTS, Level 0) | [Pred Type: SEMANTIC_SET (45.5%, no-rel 22.8%)]
   - Group 2: **0.5550** | JENNY, SHANNON, QUEEN, NANNY                                      | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS)
   - Group 3: **0.5440** | JENNY, FEY, SHANNON, NANNY                                        | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS)
   - Group 4: **0.5416** | FEY, STRONG, SHANNON, QUEEN                                       | INCORRECT (Max overlap: 3/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (62.2%, no-rel 13.0%)]
   - Group 5: **0.5408** | ROBIN HOOD, CUPID, SHANNON, QUEEN                                 | INCORRECT (Max overlap: 2/4 with ARCHERS) | [Pred Type: NAMED_ENTITY_SET (51.7%, no-rel 17.0%)]
   - Group 6: **0.5401** | SAGITTARIUS, STAR, MOON, PLANET                                   | INCORRECT (Max overlap: 3/4 with CELESTIAL OBJECTS) | [Pred Type: SEMANTIC_SET (50.6%, no-rel 22.5%)]
   - Group 7: **0.5331** | FEY, SHANNON, QUEEN, NANNY                                        | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (47.2%, no-rel 19.2%)]
   - Group 8: **0.5322** | FEY, CUPID, VIXEN, QUEEN                                          | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (62.4%, no-rel 10.5%)]
   - Group 9: **0.5304** | FEY, CUPID, SHANNON, QUEEN                                        | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (56.2%, no-rel 15.0%)]
   - Group 10: **0.5295** | JENNY, FEY, CUPID, VIXEN                                          | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (51.6%, no-rel 11.9%)]
   - Group 11: **0.5286** | FEY, STRONG, VIXEN, QUEEN                                         | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (64.0%, no-rel 10.1%)]
   - Group 12: **0.5280** | JENNY, CUPID, SHANNON, QUEEN                                      | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (47.9%, no-rel 16.7%)]
   - Group 13: **0.5257** | JENNY, CUPID, VIXEN, QUEEN                                        | INCORRECT (Max overlap: 3/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (52.0%, no-rel 13.6%)]
   - Group 14: **0.5250** | ROBIN HOOD, CUPID, SHANNON, HAWKEYE                               | INCORRECT (Max overlap: 3/4 with ARCHERS)
   - Group 15: **0.5242** | CUPID, SHANNON, QUEEN, NANNY                                      | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (48.6%, no-rel 17.1%)]
   - Group 16: **0.5207** | ROBIN HOOD, FEY, CUPID, SHANNON                                   | INCORRECT (Max overlap: 2/4 with ARCHERS) | [Pred Type: NAMED_ENTITY_SET (45.3%, no-rel 19.4%)]
   - Group 17: **0.5200** | FEY, CUPID, SHANNON, HAWKEYE                                      | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (48.8%, no-rel 18.0%)]
   - Group 18: **0.5193** | JENNY, FEY, SHANNON, QUEEN                                        | INCORRECT (Max overlap: 2/4 with FEMALE ANIMALS) | [Pred Type: NAMED_ENTITY_SET (45.6%, no-rel 18.3%)]
   - Group 19: **0.5184** | FEY, STRONG, VIXEN, SHANNON                                       | INCORRECT (Max overlap: 3/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (61.8%, no-rel 11.1%)]
   - Group 20: **0.5183** | FEY, CUPID, VIXEN, SHANNON                                        | INCORRECT (Max overlap: 2/4 with “S.N.L.” CAST MEMBERS) | [Pred Type: NAMED_ENTITY_SET (57.2%, no-rel 11.5%)]

---

## Puzzle 17 (ID: 487)
**Words on Board:** DOE, HER, EYE, ELF, TEA, RAD, ILL, LEG, BIG, SEW, BAD, HIP, ARM, FAR, FLY, SAW

### Ground Truth Categories:
* **Level 0 (BODY PARTS) [Type: SEMANTIC_SET]:** ARM, EYE, HIP, LEG
* **Level 1 (COOL, IN ’80S SLANG) [Type: SYNONYM_OR_NEAR]:** BAD, FLY, ILL, RAD
* **Level 2 (MOVIES) [Type: NAMED_ENTITY_SET]:** BIG, ELF, HER, SAW
* **Level 3 (WORDS IN “DO-RE-MI”) [Type: SOUND_OR_SPELLING]:** DOE, FAR, SEW, TEA

### Top Candidate Partitions:
1. **Partition Score: 0.4925**
   - Group 1: **0.6046** | HER, EYE, ELF, TEA                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 2: **0.5890** | DOE, RAD, SEW, SAW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (70.8%, no-rel 7.3%)]
   - Group 3: **0.5199** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 4: **0.4305** | LEG, HIP, ARM, FLY                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS) | [Pred Type: SEMANTIC_SET (75.6%, no-rel 17.6%)]
2. **Partition Score: 0.4889**
   - Group 1: **0.5773** | DOE, EYE, RAD, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (67.6%, no-rel 5.6%)]
   - Group 2: **0.5746** | HER, ELF, TEA, SAW                                                | INCORRECT (Max overlap: 3/4 with MOVIES)
   - Group 3: **0.5199** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 4: **0.4305** | LEG, HIP, ARM, FLY                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS) | [Pred Type: SEMANTIC_SET (75.6%, no-rel 17.6%)]
3. **Partition Score: 0.4888**
   - Group 1: **0.5787** | DOE, HER, ELF, TEA                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 2: **0.5743** | EYE, RAD, SEW, SAW                                                | INCORRECT (Max overlap: 1/4 with BODY PARTS) | [Pred Type: SOUND_OR_SPELLING (50.3%, no-rel 13.3%)]
   - Group 3: **0.5199** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 4: **0.4305** | LEG, HIP, ARM, FLY                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS) | [Pred Type: SEMANTIC_SET (75.6%, no-rel 17.6%)]
4. **Partition Score: 0.4868**
   - Group 1: **0.5924** | DOE, HER, TEA, SEW                                                | INCORRECT (Max overlap: 3/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (70.0%, no-rel 6.1%)]
   - Group 2: **0.5663** | EYE, ELF, RAD, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 3: **0.5199** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 4: **0.4305** | LEG, HIP, ARM, FLY                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS) | [Pred Type: SEMANTIC_SET (75.6%, no-rel 17.6%)]
5. **Partition Score: 0.4864**
   - Group 1: **0.6150** | DOE, HER, RAD, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (71.3%, no-rel 3.5%)]
   - Group 2: **0.5644** | EYE, ELF, TEA, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 3: **0.5199** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 4: **0.4305** | LEG, HIP, ARM, FLY                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS) | [Pred Type: SEMANTIC_SET (75.6%, no-rel 17.6%)]

### Top Candidate Groups:
   - Group 1: **0.6046** | HER, EYE, ELF, TEA                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 2: **0.5890** | DOE, RAD, SEW, SAW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (70.8%, no-rel 7.3%)]
   - Group 3: **0.5199** | ILL, BIG, BAD, FAR                                                | INCORRECT (Max overlap: 2/4 with COOL, IN ’80S SLANG)
   - Group 4: **0.4305** | LEG, HIP, ARM, FLY                                                | INCORRECT (Max overlap: 3/4 with BODY PARTS) | [Pred Type: SEMANTIC_SET (75.6%, no-rel 17.6%)]
   - Group 5: **0.5773** | DOE, EYE, RAD, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (67.6%, no-rel 5.6%)]
   - Group 6: **0.5746** | HER, ELF, TEA, SAW                                                | INCORRECT (Max overlap: 3/4 with MOVIES)
   - Group 7: **0.5787** | DOE, HER, ELF, TEA                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”)
   - Group 8: **0.5743** | EYE, RAD, SEW, SAW                                                | INCORRECT (Max overlap: 1/4 with BODY PARTS) | [Pred Type: SOUND_OR_SPELLING (50.3%, no-rel 13.3%)]
   - Group 9: **0.5924** | DOE, HER, TEA, SEW                                                | INCORRECT (Max overlap: 3/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (70.0%, no-rel 6.1%)]
   - Group 10: **0.5663** | EYE, ELF, RAD, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 11: **0.6150** | DOE, HER, RAD, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (71.3%, no-rel 3.5%)]
   - Group 12: **0.5644** | EYE, ELF, TEA, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 13: **0.6166** | DOE, ELF, RAD, SEW                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (65.9%, no-rel 5.6%)]
   - Group 14: **0.5619** | HER, EYE, TEA, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 15: **0.5720** | DOE, ELF, TEA, SEW                                                | INCORRECT (Max overlap: 3/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (63.2%, no-rel 10.0%)]
   - Group 16: **0.5585** | HER, EYE, RAD, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 17: **0.5694** | DOE, EYE, ELF, RAD                                                | INCORRECT (Max overlap: 1/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (45.1%, no-rel 6.6%)]
   - Group 18: **0.5560** | HER, TEA, SEW, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 19: **0.5580** | ELF, RAD, SEW, SAW                                                | INCORRECT (Max overlap: 2/4 with MOVIES)
   - Group 20: **0.5554** | DOE, HER, EYE, TEA                                                | INCORRECT (Max overlap: 2/4 with WORDS IN “DO-RE-MI”) | [Pred Type: SOUND_OR_SPELLING (49.1%, no-rel 8.2%)]

---

## Puzzle 18 (ID: 677)
**Words on Board:** HAUNTING, NOSE, EXORCIST, BOY, APPLE, BIRDS, WOW, EFFECT, BELONGING, BANJO, SHINING, POSSESSION, GOOD, GOODNESS, CARD, MAN

### Ground Truth Categories:
* **Level 0 (INTERJECTIONS) [Type: SEMANTIC_SET]:** BOY, GOODNESS, MAN, WOW
* **Level 1 (HORROR MOVIES, WITH “THE”) [Type: FILL_IN_THE_BLANK]:** BIRDS, EXORCIST, HAUNTING, SHINING
* **Level 2 (THINGS YOU CAN PICK) [Type: SEMANTIC_SET]:** APPLE, BANJO, CARD, NOSE
* **Level 3 (PERSONAL PROPERTY MINUS “S”) [Type: WORDPLAY_TRANSFORM]:** BELONGING, EFFECT, GOOD, POSSESSION

### Top Candidate Partitions:
1. **Partition Score: 0.3455**
   - Group 1: **0.4263** | EFFECT, POSSESSION, GOOD, GOODNESS                                | INCORRECT (Max overlap: 3/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (60.5%, no-rel 31.2%)]
   - Group 2: **0.4006** | NOSE, APPLE, BIRDS, BANJO                                         | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN PICK)
   - Group 3: **0.3460** | HAUNTING, EXORCIST, BELONGING, SHINING                            | INCORRECT (Max overlap: 3/4 with HORROR MOVIES, WITH “THE”)
   - Group 4: **0.3177** | BOY, WOW, CARD, MAN                                               | INCORRECT (Max overlap: 3/4 with INTERJECTIONS)
2. **Partition Score: 0.3431**
   - Group 1: **0.5431** | HAUNTING, BELONGING, SHINING, POSSESSION                          | INCORRECT (Max overlap: 2/4 with HORROR MOVIES, WITH “THE”) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 35.7%)]
   - Group 2: **0.4006** | NOSE, APPLE, BIRDS, BANJO                                         | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN PICK)
   - Group 3: **0.3263** | EXORCIST, BOY, WOW, CARD                                          | INCORRECT (Max overlap: 2/4 with INTERJECTIONS)
   - Group 4: **0.3227** | EFFECT, GOOD, GOODNESS, MAN                                       | INCORRECT (Max overlap: 2/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (61.8%, no-rel 25.9%)]
3. **Partition Score: 0.3412**
   - Group 1: **0.4006** | NOSE, APPLE, BIRDS, BANJO                                         | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN PICK)
   - Group 2: **0.3789** | BELONGING, POSSESSION, GOOD, GOODNESS                             | INCORRECT (Max overlap: 3/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (59.4%, no-rel 31.8%)]
   - Group 3: **0.3506** | HAUNTING, EXORCIST, EFFECT, SHINING                               | INCORRECT (Max overlap: 3/4 with HORROR MOVIES, WITH “THE”)
   - Group 4: **0.3177** | BOY, WOW, CARD, MAN                                               | INCORRECT (Max overlap: 3/4 with INTERJECTIONS)
4. **Partition Score: 0.3386**
   - Group 1: **0.4263** | EFFECT, POSSESSION, GOOD, GOODNESS                                | INCORRECT (Max overlap: 3/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (60.5%, no-rel 31.2%)]
   - Group 2: **0.4006** | NOSE, APPLE, BIRDS, BANJO                                         | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN PICK)
   - Group 3: **0.3263** | EXORCIST, BOY, WOW, CARD                                          | INCORRECT (Max overlap: 2/4 with INTERJECTIONS)
   - Group 4: **0.3137** | HAUNTING, BELONGING, SHINING, MAN                                 | INCORRECT (Max overlap: 2/4 with HORROR MOVIES, WITH “THE”)
5. **Partition Score: 0.3361**
   - Group 1: **0.5431** | HAUNTING, BELONGING, SHINING, POSSESSION                          | INCORRECT (Max overlap: 2/4 with HORROR MOVIES, WITH “THE”) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 35.7%)]
   - Group 2: **0.4474** | NOSE, APPLE, BANJO, CARD                                          | CORRECT GROUP (THINGS YOU CAN PICK, Level 2)
   - Group 3: **0.3227** | EFFECT, GOOD, GOODNESS, MAN                                       | INCORRECT (Max overlap: 2/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (61.8%, no-rel 25.9%)]
   - Group 4: **0.2872** | EXORCIST, BOY, BIRDS, WOW                                         | INCORRECT (Max overlap: 2/4 with HORROR MOVIES, WITH “THE”)

### Top Candidate Groups:
   - Group 1: **0.4263** | EFFECT, POSSESSION, GOOD, GOODNESS                                | INCORRECT (Max overlap: 3/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (60.5%, no-rel 31.2%)]
   - Group 2: **0.4006** | NOSE, APPLE, BIRDS, BANJO                                         | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN PICK)
   - Group 3: **0.3460** | HAUNTING, EXORCIST, BELONGING, SHINING                            | INCORRECT (Max overlap: 3/4 with HORROR MOVIES, WITH “THE”)
   - Group 4: **0.3177** | BOY, WOW, CARD, MAN                                               | INCORRECT (Max overlap: 3/4 with INTERJECTIONS)
   - Group 5: **0.5431** | HAUNTING, BELONGING, SHINING, POSSESSION                          | INCORRECT (Max overlap: 2/4 with HORROR MOVIES, WITH “THE”) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 35.7%)]
   - Group 6: **0.3263** | EXORCIST, BOY, WOW, CARD                                          | INCORRECT (Max overlap: 2/4 with INTERJECTIONS)
   - Group 7: **0.3227** | EFFECT, GOOD, GOODNESS, MAN                                       | INCORRECT (Max overlap: 2/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (61.8%, no-rel 25.9%)]
   - Group 8: **0.3789** | BELONGING, POSSESSION, GOOD, GOODNESS                             | INCORRECT (Max overlap: 3/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (59.4%, no-rel 31.8%)]
   - Group 9: **0.3506** | HAUNTING, EXORCIST, EFFECT, SHINING                               | INCORRECT (Max overlap: 3/4 with HORROR MOVIES, WITH “THE”)
   - Group 10: **0.3137** | HAUNTING, BELONGING, SHINING, MAN                                 | INCORRECT (Max overlap: 2/4 with HORROR MOVIES, WITH “THE”)
   - Group 11: **0.4474** | NOSE, APPLE, BANJO, CARD                                          | CORRECT GROUP (THINGS YOU CAN PICK, Level 2)
   - Group 12: **0.2872** | EXORCIST, BOY, BIRDS, WOW                                         | INCORRECT (Max overlap: 2/4 with HORROR MOVIES, WITH “THE”)
   - Group 13: **0.3806** | NOSE, EXORCIST, APPLE, BANJO                                      | INCORRECT (Max overlap: 3/4 with THINGS YOU CAN PICK)
   - Group 14: **0.3272** | BIRDS, EFFECT, GOOD, GOODNESS                                     | INCORRECT (Max overlap: 2/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (67.6%, no-rel 16.7%)]
   - Group 15: **0.3193** | BOY, BIRDS, WOW, CARD                                             | INCORRECT (Max overlap: 2/4 with INTERJECTIONS)
   - Group 16: **0.3952** | WOW, EFFECT, GOOD, GOODNESS                                       | INCORRECT (Max overlap: 2/4 with INTERJECTIONS) | [Pred Type: SYNONYM_OR_NEAR (63.3%, no-rel 25.6%)]
   - Group 17: **0.3683** | HAUNTING, NOSE, EXORCIST, CARD                                    | INCORRECT (Max overlap: 2/4 with HORROR MOVIES, WITH “THE”)
   - Group 18: **0.3334** | BOY, APPLE, BIRDS, BANJO                                          | INCORRECT (Max overlap: 2/4 with THINGS YOU CAN PICK)
   - Group 19: **0.3190** | BELONGING, SHINING, POSSESSION, MAN                               | INCORRECT (Max overlap: 2/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (49.9%, no-rel 33.5%)]
   - Group 20: **0.3798** | EFFECT, BELONGING, GOOD, GOODNESS                                 | INCORRECT (Max overlap: 3/4 with PERSONAL PROPERTY MINUS “S”) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 32.0%)]

---

## Puzzle 19 (ID: 132)
**Words on Board:** HOOK, TRIPE, BUNK, SPAM, WIRE, SAUCER, CUP, STRAP, DISH, BALONEY, LASER, SCUBA, BOWL, CROCK, PLATE, RADAR

### Ground Truth Categories:
* **Level 0 (TABLEWARE) [Type: SEMANTIC_SET]:** BOWL, DISH, PLATE, SAUCER
* **Level 1 (NONSENSE) [Type: SYNONYM_OR_NEAR]:** BALONEY, BUNK, CROCK, TRIPE
* **Level 2 (BRA PARTS) [Type: SEMANTIC_SET]:** CUP, HOOK, STRAP, WIRE
* **Level 3 (ACRONYMS) [Type: WORDPLAY_TRANSFORM]:** LASER, RADAR, SCUBA, SPAM

### Top Candidate Partitions:
1. **Partition Score: 0.4804**
   - Group 1: **0.6524** | SAUCER, DISH, BOWL, PLATE                                         | CORRECT GROUP (TABLEWARE, Level 0)
   - Group 2: **0.6309** | TRIPE, BUNK, BALONEY, CROCK                                       | CORRECT GROUP (NONSENSE, Level 1)
   - Group 3: **0.4874** | HOOK, WIRE, CUP, STRAP                                            | CORRECT GROUP (BRA PARTS, Level 2) | [Pred Type: SEMANTIC_SET (53.9%, no-rel 27.4%)]
   - Group 4: **0.4017** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
2. **Partition Score: 0.4618**
   - Group 1: **0.7472** | SAUCER, CUP, DISH, PLATE                                          | INCORRECT (Max overlap: 3/4 with TABLEWARE) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 30.4%)]
   - Group 2: **0.6309** | TRIPE, BUNK, BALONEY, CROCK                                       | CORRECT GROUP (NONSENSE, Level 1)
   - Group 3: **0.4130** | HOOK, WIRE, STRAP, BOWL                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)
   - Group 4: **0.4017** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
3. **Partition Score: 0.4485**
   - Group 1: **0.7670** | CUP, DISH, BOWL, PLATE                                            | INCORRECT (Max overlap: 3/4 with TABLEWARE)
   - Group 2: **0.6309** | TRIPE, BUNK, BALONEY, CROCK                                       | CORRECT GROUP (NONSENSE, Level 1)
   - Group 3: **0.4017** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
   - Group 4: **0.3807** | HOOK, WIRE, SAUCER, STRAP                                         | INCORRECT (Max overlap: 3/4 with BRA PARTS) | [Pred Type: SEMANTIC_SET (46.5%, no-rel 24.6%)]
4. **Partition Score: 0.4300**
   - Group 1: **0.5546** | TRIPE, BUNK, SPAM, BALONEY                                        | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 2: **0.5230** | STRAP, LASER, SCUBA, RADAR                                        | INCORRECT (Max overlap: 3/4 with ACRONYMS)
   - Group 3: **0.4552** | SAUCER, DISH, CROCK, PLATE                                        | INCORRECT (Max overlap: 3/4 with TABLEWARE) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 27.0%)]
   - Group 4: **0.3709** | HOOK, WIRE, CUP, BOWL                                             | INCORRECT (Max overlap: 3/4 with BRA PARTS) | [Pred Type: SEMANTIC_SET (50.3%, no-rel 29.5%)]
5. **Partition Score: 0.4294**
   - Group 1: **0.6309** | TRIPE, BUNK, BALONEY, CROCK                                       | CORRECT GROUP (NONSENSE, Level 1)
   - Group 2: **0.5670** | SAUCER, CUP, BOWL, PLATE                                          | INCORRECT (Max overlap: 3/4 with TABLEWARE) | [Pred Type: SEMANTIC_SET (54.8%, no-rel 36.7%)]
   - Group 3: **0.4017** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
   - Group 4: **0.3745** | HOOK, WIRE, STRAP, DISH                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)

### Top Candidate Groups:
   - Group 1: **0.6524** | SAUCER, DISH, BOWL, PLATE                                         | CORRECT GROUP (TABLEWARE, Level 0)
   - Group 2: **0.6309** | TRIPE, BUNK, BALONEY, CROCK                                       | CORRECT GROUP (NONSENSE, Level 1)
   - Group 3: **0.4874** | HOOK, WIRE, CUP, STRAP                                            | CORRECT GROUP (BRA PARTS, Level 2) | [Pred Type: SEMANTIC_SET (53.9%, no-rel 27.4%)]
   - Group 4: **0.4017** | SPAM, LASER, SCUBA, RADAR                                         | CORRECT GROUP (ACRONYMS, Level 3)
   - Group 5: **0.7472** | SAUCER, CUP, DISH, PLATE                                          | INCORRECT (Max overlap: 3/4 with TABLEWARE) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 30.4%)]
   - Group 6: **0.4130** | HOOK, WIRE, STRAP, BOWL                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)
   - Group 7: **0.7670** | CUP, DISH, BOWL, PLATE                                            | INCORRECT (Max overlap: 3/4 with TABLEWARE)
   - Group 8: **0.3807** | HOOK, WIRE, SAUCER, STRAP                                         | INCORRECT (Max overlap: 3/4 with BRA PARTS) | [Pred Type: SEMANTIC_SET (46.5%, no-rel 24.6%)]
   - Group 9: **0.5546** | TRIPE, BUNK, SPAM, BALONEY                                        | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 10: **0.5230** | STRAP, LASER, SCUBA, RADAR                                        | INCORRECT (Max overlap: 3/4 with ACRONYMS)
   - Group 11: **0.4552** | SAUCER, DISH, CROCK, PLATE                                        | INCORRECT (Max overlap: 3/4 with TABLEWARE) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 27.0%)]
   - Group 12: **0.3709** | HOOK, WIRE, CUP, BOWL                                             | INCORRECT (Max overlap: 3/4 with BRA PARTS) | [Pred Type: SEMANTIC_SET (50.3%, no-rel 29.5%)]
   - Group 13: **0.5670** | SAUCER, CUP, BOWL, PLATE                                          | INCORRECT (Max overlap: 3/4 with TABLEWARE) | [Pred Type: SEMANTIC_SET (54.8%, no-rel 36.7%)]
   - Group 14: **0.3745** | HOOK, WIRE, STRAP, DISH                                           | INCORRECT (Max overlap: 3/4 with BRA PARTS)
   - Group 15: **0.4774** | TRIPE, SPAM, BALONEY, CROCK                                       | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 16: **0.3493** | HOOK, BUNK, WIRE, CUP                                             | INCORRECT (Max overlap: 3/4 with BRA PARTS)
   - Group 17: **0.5214** | BUNK, SPAM, BALONEY, CROCK                                        | INCORRECT (Max overlap: 3/4 with NONSENSE)
   - Group 18: **0.4343** | TRIPE, SAUCER, DISH, PLATE                                        | INCORRECT (Max overlap: 3/4 with TABLEWARE) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 29.5%)]
   - Group 19: **0.6019** | SAUCER, CUP, DISH, BOWL                                           | INCORRECT (Max overlap: 3/4 with TABLEWARE) | [Pred Type: SYNONYM_OR_NEAR (45.9%, no-rel 21.9%)]
   - Group 20: **0.3462** | HOOK, WIRE, STRAP, PLATE                                          | INCORRECT (Max overlap: 3/4 with BRA PARTS)

---

## Puzzle 20 (ID: 129)
**Words on Board:** PANT, TONG, SNOOZE, BOXER, PUFF, BREEZE, KICK, DRAG, GOGGLE, DRAFT, YAWN, TANG, GUST, ZIP, BORE, BITE

### Ground Truth Categories:
* **Level 0 (SOMETHING TIRESOME) [Type: SYNONYM_OR_NEAR]:** BORE, DRAG, SNOOZE, YAWN
* **Level 1 (BIT OF WIND) [Type: SYNONYM_OR_NEAR]:** BREEZE, DRAFT, GUST, PUFF
* **Level 2 (PIQUANCY) [Type: SYNONYM_OR_NEAR]:** BITE, KICK, TANG, ZIP
* **Level 3 (SINGULAR OF THINGS SEEN IN PAIRS) [Type: WORDPLAY_TRANSFORM]:** BOXER, GOGGLE, PANT, TONG

### Top Candidate Partitions:
1. **Partition Score: 0.3511**
   - Group 1: **0.4528** | PANT, PUFF, DRAG, BORE                                            | INCORRECT (Max overlap: 2/4 with SOMETHING TIRESOME) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 28.2%)]
   - Group 2: **0.4128** | BREEZE, DRAFT, GUST, ZIP                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 3: **0.3997** | TONG, SNOOZE, BOXER, GOGGLE                                       | INCORRECT (Max overlap: 3/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 4: **0.2959** | KICK, YAWN, TANG, BITE                                            | INCORRECT (Max overlap: 3/4 with PIQUANCY)
2. **Partition Score: 0.3489**
   - Group 1: **0.4403** | PUFF, BREEZE, DRAFT, GUST                                         | CORRECT GROUP (BIT OF WIND, Level 1)
   - Group 2: **0.4274** | KICK, DRAG, ZIP, BORE                                             | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 3: **0.3293** | PANT, SNOOZE, GOGGLE, YAWN                                        | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 4: **0.3195** | TONG, BOXER, TANG, BITE                                           | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
3. **Partition Score: 0.3477**
   - Group 1: **0.4128** | BREEZE, DRAFT, GUST, ZIP                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 2: **0.3997** | TONG, SNOOZE, BOXER, GOGGLE                                       | INCORRECT (Max overlap: 3/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 3: **0.3328** | KICK, YAWN, BORE, BITE                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 4: **0.3291** | PANT, PUFF, DRAG, TANG                                            | INCORRECT (Max overlap: 1/4 with SINGULAR OF THINGS SEEN IN PAIRS) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 27.3%)]
4. **Partition Score: 0.3447**
   - Group 1: **0.4403** | PUFF, BREEZE, DRAFT, GUST                                         | CORRECT GROUP (BIT OF WIND, Level 1)
   - Group 2: **0.4137** | PANT, KICK, DRAG, ZIP                                             | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 3: **0.3259** | SNOOZE, GOGGLE, YAWN, BORE                                        | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 4: **0.3195** | TONG, BOXER, TANG, BITE                                           | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
5. **Partition Score: 0.3445**
   - Group 1: **0.5031** | PANT, PUFF, KICK, DRAG                                            | INCORRECT (Max overlap: 1/4 with SINGULAR OF THINGS SEEN IN PAIRS) | [Pred Type: SYNONYM_OR_NEAR (53.0%, no-rel 31.9%)]
   - Group 2: **0.4128** | BREEZE, DRAFT, GUST, ZIP                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 3: **0.3259** | SNOOZE, GOGGLE, YAWN, BORE                                        | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 4: **0.3195** | TONG, BOXER, TANG, BITE                                           | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)

### Top Candidate Groups:
   - Group 1: **0.4528** | PANT, PUFF, DRAG, BORE                                            | INCORRECT (Max overlap: 2/4 with SOMETHING TIRESOME) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 28.2%)]
   - Group 2: **0.4128** | BREEZE, DRAFT, GUST, ZIP                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND)
   - Group 3: **0.3997** | TONG, SNOOZE, BOXER, GOGGLE                                       | INCORRECT (Max overlap: 3/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 4: **0.2959** | KICK, YAWN, TANG, BITE                                            | INCORRECT (Max overlap: 3/4 with PIQUANCY)
   - Group 5: **0.4403** | PUFF, BREEZE, DRAFT, GUST                                         | CORRECT GROUP (BIT OF WIND, Level 1)
   - Group 6: **0.4274** | KICK, DRAG, ZIP, BORE                                             | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 7: **0.3293** | PANT, SNOOZE, GOGGLE, YAWN                                        | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 8: **0.3195** | TONG, BOXER, TANG, BITE                                           | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 9: **0.3328** | KICK, YAWN, BORE, BITE                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 10: **0.3291** | PANT, PUFF, DRAG, TANG                                            | INCORRECT (Max overlap: 1/4 with SINGULAR OF THINGS SEEN IN PAIRS) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 27.3%)]
   - Group 11: **0.4137** | PANT, KICK, DRAG, ZIP                                             | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 12: **0.3259** | SNOOZE, GOGGLE, YAWN, BORE                                        | INCORRECT (Max overlap: 3/4 with SOMETHING TIRESOME)
   - Group 13: **0.5031** | PANT, PUFF, KICK, DRAG                                            | INCORRECT (Max overlap: 1/4 with SINGULAR OF THINGS SEEN IN PAIRS) | [Pred Type: SYNONYM_OR_NEAR (53.0%, no-rel 31.9%)]
   - Group 14: **0.4071** | KICK, DRAG, DRAFT, ZIP                                            | INCORRECT (Max overlap: 2/4 with PIQUANCY)
   - Group 15: **0.4060** | PANT, PUFF, BREEZE, GUST                                          | INCORRECT (Max overlap: 3/4 with BIT OF WIND) | [Pred Type: SYNONYM_OR_NEAR (55.0%, no-rel 25.9%)]
   - Group 16: **0.3853** | PUFF, KICK, DRAG, BORE                                            | INCORRECT (Max overlap: 2/4 with SOMETHING TIRESOME) | [Pred Type: SYNONYM_OR_NEAR (51.4%, no-rel 35.0%)]
   - Group 17: **0.3545** | PANT, DRAG, ZIP, BORE                                             | INCORRECT (Max overlap: 2/4 with SOMETHING TIRESOME)
   - Group 18: **0.3822** | TONG, SNOOZE, BOXER, TANG                                         | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS)
   - Group 19: **0.3152** | PANT, PUFF, DRAG, GOGGLE                                          | INCORRECT (Max overlap: 2/4 with SINGULAR OF THINGS SEEN IN PAIRS) | [Pred Type: SYNONYM_OR_NEAR (61.0%, no-rel 18.6%)]
   - Group 20: **0.3095** | TONG, BOXER, GOGGLE, TANG                                         | INCORRECT (Max overlap: 3/4 with SINGULAR OF THINGS SEEN IN PAIRS)

---

## Puzzle 21 (ID: 786)
**Words on Board:** HEALTH, MINCE, GRATE, SLICE, DRESS, SECRET, COAL, CARROT, SUBWAY, TUBE, UNDERGROUND, PIPE, CUBE, ZIP, METRO, SCARF

### Ground Truth Categories:
* **Level 0 (SUBTERRANEAN TRANSIT) [Type: SYNONYM_OR_NEAR]:** METRO, SUBWAY, TUBE, UNDERGROUND
* **Level 1 (MAKE INTO SMALLER PIECES WHILE COOKING) [Type: SYNONYM_OR_NEAR]:** CUBE, GRATE, MINCE, SLICE
* **Level 2 (USED TO DECORATE A SNOWMAN) [Type: SEMANTIC_SET]:** CARROT, COAL, PIPE, SCARF
* **Level 3 (___ CODE) [Type: FILL_IN_THE_BLANK]:** DRESS, HEALTH, SECRET, ZIP

### Top Candidate Partitions:
1. **Partition Score: 0.4777**
   - Group 1: **0.5539** | SECRET, SUBWAY, UNDERGROUND, METRO                                | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 18.8%)]
   - Group 2: **0.5065** | MINCE, SLICE, CUBE, ZIP                                           | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 3: **0.4882** | GRATE, COAL, TUBE, PIPE                                           | INCORRECT (Max overlap: 2/4 with USED TO DECORATE A SNOWMAN) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 33.7%)]
   - Group 4: **0.4580** | HEALTH, DRESS, CARROT, SCARF                                      | INCORRECT (Max overlap: 2/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (56.5%, no-rel 19.3%)]
2. **Partition Score: 0.4573**
   - Group 1: **0.5076** | SUBWAY, TUBE, PIPE, METRO                                         | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (60.7%, no-rel 19.0%)]
   - Group 2: **0.5065** | MINCE, SLICE, CUBE, ZIP                                           | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 3: **0.4580** | HEALTH, DRESS, CARROT, SCARF                                      | INCORRECT (Max overlap: 2/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (56.5%, no-rel 19.3%)]
   - Group 4: **0.4322** | GRATE, SECRET, COAL, UNDERGROUND                                  | INCORRECT (Max overlap: 1/4 with MAKE INTO SMALLER PIECES WHILE COOKING) | [Pred Type: SYNONYM_OR_NEAR (48.5%, no-rel 36.5%)]
3. **Partition Score: 0.4467**
   - Group 1: **0.4882** | GRATE, COAL, TUBE, PIPE                                           | INCORRECT (Max overlap: 2/4 with USED TO DECORATE A SNOWMAN) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 33.7%)]
   - Group 2: **0.4580** | HEALTH, DRESS, CARROT, SCARF                                      | INCORRECT (Max overlap: 2/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (56.5%, no-rel 19.3%)]
   - Group 3: **0.4577** | SUBWAY, UNDERGROUND, CUBE, METRO                                  | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 16.5%)]
   - Group 4: **0.4356** | MINCE, SLICE, SECRET, ZIP                                         | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
4. **Partition Score: 0.4465**
   - Group 1: **0.5539** | SECRET, SUBWAY, UNDERGROUND, METRO                                | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 18.8%)]
   - Group 2: **0.4580** | HEALTH, DRESS, CARROT, SCARF                                      | INCORRECT (Max overlap: 2/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (56.5%, no-rel 19.3%)]
   - Group 3: **0.4578** | MINCE, SLICE, PIPE, ZIP                                           | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 4: **0.4350** | GRATE, COAL, TUBE, CUBE                                           | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
5. **Partition Score: 0.4427**
   - Group 1: **0.4580** | HEALTH, DRESS, CARROT, SCARF                                      | INCORRECT (Max overlap: 2/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (56.5%, no-rel 19.3%)]
   - Group 2: **0.4578** | MINCE, SLICE, PIPE, ZIP                                           | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 3: **0.4485** | SUBWAY, TUBE, CUBE, METRO                                         | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 21.1%)]
   - Group 4: **0.4322** | GRATE, SECRET, COAL, UNDERGROUND                                  | INCORRECT (Max overlap: 1/4 with MAKE INTO SMALLER PIECES WHILE COOKING) | [Pred Type: SYNONYM_OR_NEAR (48.5%, no-rel 36.5%)]

### Top Candidate Groups:
   - Group 1: **0.5539** | SECRET, SUBWAY, UNDERGROUND, METRO                                | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 18.8%)]
   - Group 2: **0.5065** | MINCE, SLICE, CUBE, ZIP                                           | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 3: **0.4882** | GRATE, COAL, TUBE, PIPE                                           | INCORRECT (Max overlap: 2/4 with USED TO DECORATE A SNOWMAN) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 33.7%)]
   - Group 4: **0.4580** | HEALTH, DRESS, CARROT, SCARF                                      | INCORRECT (Max overlap: 2/4 with ___ CODE) | [Pred Type: FILL_IN_THE_BLANK (56.5%, no-rel 19.3%)]
   - Group 5: **0.5076** | SUBWAY, TUBE, PIPE, METRO                                         | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (60.7%, no-rel 19.0%)]
   - Group 6: **0.4322** | GRATE, SECRET, COAL, UNDERGROUND                                  | INCORRECT (Max overlap: 1/4 with MAKE INTO SMALLER PIECES WHILE COOKING) | [Pred Type: SYNONYM_OR_NEAR (48.5%, no-rel 36.5%)]
   - Group 7: **0.4577** | SUBWAY, UNDERGROUND, CUBE, METRO                                  | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 16.5%)]
   - Group 8: **0.4356** | MINCE, SLICE, SECRET, ZIP                                         | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 9: **0.4578** | MINCE, SLICE, PIPE, ZIP                                           | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 10: **0.4350** | GRATE, COAL, TUBE, CUBE                                           | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 11: **0.4485** | SUBWAY, TUBE, CUBE, METRO                                         | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 21.1%)]
   - Group 12: **0.4562** | SUBWAY, UNDERGROUND, ZIP, METRO                                   | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (60.0%, no-rel 21.5%)]
   - Group 13: **0.4244** | MINCE, SLICE, SECRET, CUBE                                        | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 14: **0.4765** | SLICE, SUBWAY, UNDERGROUND, METRO                                 | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 19.9%)]
   - Group 15: **0.4132** | MINCE, SECRET, CUBE, ZIP                                          | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 16: **0.4732** | COAL, SUBWAY, UNDERGROUND, METRO                                  | INCORRECT (Max overlap: 3/4 with SUBTERRANEAN TRANSIT) | [Pred Type: SYNONYM_OR_NEAR (57.4%, no-rel 21.4%)]
   - Group 17: **0.4303** | GRATE, TUBE, PIPE, CUBE                                           | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING) | [Pred Type: SYNONYM_OR_NEAR (50.6%, no-rel 36.4%)]
   - Group 18: **0.4361** | GRATE, SLICE, COAL, TUBE                                          | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 19: **0.4294** | MINCE, PIPE, CUBE, ZIP                                            | INCORRECT (Max overlap: 2/4 with MAKE INTO SMALLER PIECES WHILE COOKING)
   - Group 20: **0.4493** | MINCE, SLICE, PIPE, CUBE                                          | INCORRECT (Max overlap: 3/4 with MAKE INTO SMALLER PIECES WHILE COOKING)

---

## Puzzle 22 (ID: 546)
**Words on Board:** WEDGE, SLUG, PUMA, SEOUL, CATERPILLAR, DOVE, BLOW, GREYHOUND, SOCK, INDY, SHOEHORN, WRAP, METTLE, SQUEEZE, SANDWICH, BELT

### Ground Truth Categories:
* **Level 0 (PUNCH) [Type: SYNONYM_OR_NEAR]:** BELT, BLOW, SOCK, SLUG
* **Level 1 (CRAM) [Type: SYNONYM_OR_NEAR]:** SANDWICH, SHOEHORN, SQUEEZE, WEDGE
* **Level 2 (COMPANIES NAMED AFTER ANIMALS) [Type: NAMED_ENTITY_SET]:** CATERPILLAR, DOVE, GREYHOUND, PUMA
* **Level 3 (HOMOPHONES OF MUSIC GENRES) [Type: SOUND_OR_SPELLING]:** INDY, METTLE, SEOUL, WRAP

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.8357** | WEDGE, BLOW, WRAP, SQUEEZE                                        | INCORRECT (Max overlap: 2/4 with CRAM) | [Pred Type: SYNONYM_OR_NEAR (52.1%, no-rel 40.1%)]
   - Group 2: **0.7895** | SLUG, BLOW, SOCK, BELT                                            | CORRECT GROUP (PUNCH, Level 0)
   - Group 3: **0.7349** | WEDGE, BLOW, SQUEEZE, BELT                                        | INCORRECT (Max overlap: 2/4 with CRAM) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 36.8%)]
   - Group 4: **0.7141** | WEDGE, BLOW, SOCK, BELT                                           | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 5: **0.7081** | PUMA, SEOUL, GREYHOUND, INDY                                      | INCORRECT (Max overlap: 2/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 6: **0.7007** | BLOW, SOCK, WRAP, SQUEEZE                                         | INCORRECT (Max overlap: 2/4 with PUNCH)
   - Group 7: **0.6977** | BLOW, SOCK, SQUEEZE, BELT                                         | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 8: **0.6920** | WEDGE, BLOW, SOCK, SQUEEZE                                        | INCORRECT (Max overlap: 2/4 with CRAM)
   - Group 9: **0.6883** | WEDGE, BLOW, WRAP, BELT                                           | INCORRECT (Max overlap: 2/4 with PUNCH)
   - Group 10: **0.6788** | WEDGE, BLOW, SOCK, WRAP                                           | INCORRECT (Max overlap: 2/4 with PUNCH)
   - Group 11: **0.6702** | WEDGE, BLOW, SHOEHORN, SQUEEZE                                    | INCORRECT (Max overlap: 3/4 with CRAM) | [Pred Type: SYNONYM_OR_NEAR (58.9%, no-rel 33.2%)]
   - Group 12: **0.6693** | WEDGE, SHOEHORN, WRAP, SQUEEZE                                    | INCORRECT (Max overlap: 3/4 with CRAM) | [Pred Type: SYNONYM_OR_NEAR (55.3%, no-rel 35.3%)]
   - Group 13: **0.6676** | PUMA, SEOUL, DOVE, INDY                                           | INCORRECT (Max overlap: 2/4 with COMPANIES NAMED AFTER ANIMALS)
   - Group 14: **0.6662** | SLUG, BLOW, SOCK, SQUEEZE                                         | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 15: **0.6622** | BLOW, WRAP, SQUEEZE, BELT                                         | INCORRECT (Max overlap: 2/4 with PUNCH)
   - Group 16: **0.6560** | BLOW, SOCK, WRAP, BELT                                            | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 17: **0.6534** | WEDGE, SLUG, BLOW, BELT                                           | INCORRECT (Max overlap: 3/4 with PUNCH)
   - Group 18: **0.6517** | WEDGE, SOCK, WRAP, SQUEEZE                                        | INCORRECT (Max overlap: 2/4 with CRAM)
   - Group 19: **0.6481** | WEDGE, WRAP, SQUEEZE, SANDWICH                                    | INCORRECT (Max overlap: 3/4 with CRAM) | [Pred Type: SYNONYM_OR_NEAR (55.2%, no-rel 26.9%)]
   - Group 20: **0.6464** | WEDGE, WRAP, SQUEEZE, BELT                                        | INCORRECT (Max overlap: 2/4 with CRAM) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 37.4%)]

---

## Puzzle 23 (ID: 1046)
**Words on Board:** DICK, CLIFF, PITCH, POLYHEDRON, SPOT, CATCH, REGISTER, FINE PRINT, STRINGS, MOTHER, RANGE, CAVEAT, TONE, BUILDING, JANE, CLOCK

### Ground Truth Categories:
* **Level 0 (STIPULATION) [Type: SYNONYM_OR_NEAR]:** CATCH, CAVEAT, FINE PRINT, STRINGS
* **Level 1 (VOCAL CHARACTERISTICS) [Type: SEMANTIC_SET]:** PITCH, RANGE, REGISTER, TONE
* **Level 2 (CHARACTERS IN "DICK AND JANE") [Type: NAMED_ENTITY_SET]:** DICK, JANE, MOTHER, SPOT
* **Level 3 (THINGS WITH FACES) [Type: SEMANTIC_SET]:** BUILDING, CLIFF, CLOCK, POLYHEDRON

### Top Candidate Partitions:
1. **Partition Score: 0.4385**
   - Group 1: **0.5237** | PITCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 2: **0.4753** | DICK, CLIFF, POLYHEDRON, JANE                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.4354** | CATCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 3/4 with STIPULATION)
   - Group 4: **0.4216** | SPOT, MOTHER, BUILDING, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE") | [Pred Type: FILL_IN_THE_BLANK (54.2%, no-rel 16.7%)]
2. **Partition Score: 0.4362**
   - Group 1: **0.4799** | PITCH, REGISTER, STRINGS, RANGE                                   | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 2: **0.4753** | DICK, CLIFF, POLYHEDRON, JANE                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.4264** | CATCH, FINE PRINT, CAVEAT, TONE                                   | INCORRECT (Max overlap: 3/4 with STIPULATION)
   - Group 4: **0.4216** | SPOT, MOTHER, BUILDING, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE") | [Pred Type: FILL_IN_THE_BLANK (54.2%, no-rel 16.7%)]
3. **Partition Score: 0.4304**
   - Group 1: **0.5248** | PITCH, REGISTER, RANGE, TONE                                      | CORRECT GROUP (VOCAL CHARACTERISTICS, Level 1)
   - Group 2: **0.4753** | DICK, CLIFF, POLYHEDRON, JANE                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.4216** | SPOT, MOTHER, BUILDING, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE") | [Pred Type: FILL_IN_THE_BLANK (54.2%, no-rel 16.7%)]
   - Group 4: **0.4123** | CATCH, FINE PRINT, STRINGS, CAVEAT                                | CORRECT GROUP (STIPULATION, Level 0)
4. **Partition Score: 0.4301**
   - Group 1: **0.4880** | PITCH, CATCH, STRINGS, RANGE                                      | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
   - Group 2: **0.4753** | DICK, CLIFF, POLYHEDRON, JANE                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.4216** | SPOT, MOTHER, BUILDING, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE") | [Pred Type: FILL_IN_THE_BLANK (54.2%, no-rel 16.7%)]
   - Group 4: **0.4116** | REGISTER, FINE PRINT, CAVEAT, TONE                                | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
5. **Partition Score: 0.4284**
   - Group 1: **0.4999** | PITCH, CATCH, STRINGS, TONE                                       | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
   - Group 2: **0.4753** | DICK, CLIFF, POLYHEDRON, JANE                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.4216** | SPOT, MOTHER, BUILDING, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE") | [Pred Type: FILL_IN_THE_BLANK (54.2%, no-rel 16.7%)]
   - Group 4: **0.4084** | REGISTER, FINE PRINT, RANGE, CAVEAT                               | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)

### Top Candidate Groups:
   - Group 1: **0.5237** | PITCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 2: **0.4753** | DICK, CLIFF, POLYHEDRON, JANE                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE")
   - Group 3: **0.4354** | CATCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 3/4 with STIPULATION)
   - Group 4: **0.4216** | SPOT, MOTHER, BUILDING, CLOCK                                     | INCORRECT (Max overlap: 2/4 with CHARACTERS IN "DICK AND JANE") | [Pred Type: FILL_IN_THE_BLANK (54.2%, no-rel 16.7%)]
   - Group 5: **0.4799** | PITCH, REGISTER, STRINGS, RANGE                                   | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 6: **0.4264** | CATCH, FINE PRINT, CAVEAT, TONE                                   | INCORRECT (Max overlap: 3/4 with STIPULATION)
   - Group 7: **0.5248** | PITCH, REGISTER, RANGE, TONE                                      | CORRECT GROUP (VOCAL CHARACTERISTICS, Level 1)
   - Group 8: **0.4123** | CATCH, FINE PRINT, STRINGS, CAVEAT                                | CORRECT GROUP (STIPULATION, Level 0)
   - Group 9: **0.4880** | PITCH, CATCH, STRINGS, RANGE                                      | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
   - Group 10: **0.4116** | REGISTER, FINE PRINT, CAVEAT, TONE                                | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
   - Group 11: **0.4999** | PITCH, CATCH, STRINGS, TONE                                       | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
   - Group 12: **0.4084** | REGISTER, FINE PRINT, RANGE, CAVEAT                               | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
   - Group 13: **0.5000** | REGISTER, STRINGS, RANGE, TONE                                    | INCORRECT (Max overlap: 3/4 with VOCAL CHARACTERISTICS)
   - Group 14: **0.4068** | PITCH, CATCH, FINE PRINT, CAVEAT                                  | INCORRECT (Max overlap: 3/4 with STIPULATION)
   - Group 15: **0.4682** | PITCH, CATCH, CAVEAT, TONE                                        | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
   - Group 16: **0.4074** | REGISTER, FINE PRINT, STRINGS, RANGE                              | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)
   - Group 17: **0.4649** | CLIFF, POLYHEDRON, JANE, CLOCK                                    | INCORRECT (Max overlap: 3/4 with THINGS WITH FACES)
   - Group 18: **0.3936** | DICK, SPOT, MOTHER, BUILDING                                      | INCORRECT (Max overlap: 3/4 with CHARACTERS IN "DICK AND JANE") | [Pred Type: FILL_IN_THE_BLANK (46.3%, no-rel 18.3%)]
   - Group 19: **0.5320** | CATCH, STRINGS, RANGE, TONE                                       | INCORRECT (Max overlap: 2/4 with STIPULATION)
   - Group 20: **0.3914** | PITCH, REGISTER, FINE PRINT, CAVEAT                               | INCORRECT (Max overlap: 2/4 with VOCAL CHARACTERISTICS)

---

## Puzzle 24 (ID: 71)
**Words on Board:** MUG, SOPRANO, MONTANA, SPRITE, SQUIRT, COLORADO, YES, STARK, UTAH, NEVADA, CRUSH, ARIZONA, HAWK, KANSAS, GENESIS, RUSH

### Ground Truth Categories:
* **Level 0 (U.S. MOUNTAIN STATES) [Type: NAMED_ENTITY_SET]:** ARIZONA, COLORADO, NEVADA, UTAH
* **Level 1 (SODA BRANDS) [Type: NAMED_ENTITY_SET]:** CRUSH, MUG, SPRITE, SQUIRT
* **Level 2 (CLASSIC ROCK BANDS) [Type: NAMED_ENTITY_SET]:** GENESIS, KANSAS, RUSH, YES
* **Level 3 (TONY ___) [Type: FILL_IN_THE_BLANK]:** HAWK, MONTANA, SOPRANO, STARK

### Top Candidate Partitions:
1. **Partition Score: 0.4711**
   - Group 1: **0.5212** | NEVADA, ARIZONA, KANSAS, GENESIS                                  | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (50.6%, no-rel 17.8%)]
   - Group 2: **0.5050** | SOPRANO, MONTANA, COLORADO, UTAH                                  | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (63.1%, no-rel 15.8%)]
   - Group 3: **0.4615** | SPRITE, YES, STARK, HAWK                                          | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 4: **0.4589** | MUG, SQUIRT, CRUSH, RUSH                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
2. **Partition Score: 0.4705**
   - Group 1: **0.5212** | NEVADA, ARIZONA, KANSAS, GENESIS                                  | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (50.6%, no-rel 17.8%)]
   - Group 2: **0.5122** | SOPRANO, SPRITE, YES, STARK                                       | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 3: **0.4589** | MUG, SQUIRT, CRUSH, RUSH                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 4: **0.4554** | MONTANA, COLORADO, UTAH, HAWK                                     | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (65.2%, no-rel 13.6%)]
3. **Partition Score: 0.4694**
   - Group 1: **0.5212** | NEVADA, ARIZONA, KANSAS, GENESIS                                  | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (50.6%, no-rel 17.8%)]
   - Group 2: **0.5029** | MONTANA, COLORADO, STARK, UTAH                                    | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (63.1%, no-rel 16.4%)]
   - Group 3: **0.4589** | MUG, SQUIRT, CRUSH, RUSH                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 4: **0.4579** | SOPRANO, SPRITE, YES, HAWK                                        | INCORRECT (Max overlap: 2/4 with TONY ___)
4. **Partition Score: 0.4690**
   - Group 1: **0.5113** | SOPRANO, MONTANA, COLORADO, NEVADA                                | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (53.8%, no-rel 21.3%)]
   - Group 2: **0.4964** | UTAH, ARIZONA, KANSAS, GENESIS                                    | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (53.8%, no-rel 15.3%)]
   - Group 3: **0.4615** | SPRITE, YES, STARK, HAWK                                          | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 4: **0.4589** | MUG, SQUIRT, CRUSH, RUSH                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
5. **Partition Score: 0.4683**
   - Group 1: **0.4993** | UTAH, NEVADA, KANSAS, GENESIS                                     | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (54.0%, no-rel 15.3%)]
   - Group 2: **0.4937** | SOPRANO, MONTANA, COLORADO, ARIZONA                               | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (53.0%, no-rel 23.1%)]
   - Group 3: **0.4615** | SPRITE, YES, STARK, HAWK                                          | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 4: **0.4589** | MUG, SQUIRT, CRUSH, RUSH                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)

### Top Candidate Groups:
   - Group 1: **0.5212** | NEVADA, ARIZONA, KANSAS, GENESIS                                  | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (50.6%, no-rel 17.8%)]
   - Group 2: **0.5050** | SOPRANO, MONTANA, COLORADO, UTAH                                  | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (63.1%, no-rel 15.8%)]
   - Group 3: **0.4615** | SPRITE, YES, STARK, HAWK                                          | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 4: **0.4589** | MUG, SQUIRT, CRUSH, RUSH                                          | INCORRECT (Max overlap: 3/4 with SODA BRANDS)
   - Group 5: **0.5122** | SOPRANO, SPRITE, YES, STARK                                       | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 6: **0.4554** | MONTANA, COLORADO, UTAH, HAWK                                     | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (65.2%, no-rel 13.6%)]
   - Group 7: **0.5029** | MONTANA, COLORADO, STARK, UTAH                                    | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (63.1%, no-rel 16.4%)]
   - Group 8: **0.4579** | SOPRANO, SPRITE, YES, HAWK                                        | INCORRECT (Max overlap: 2/4 with TONY ___)
   - Group 9: **0.5113** | SOPRANO, MONTANA, COLORADO, NEVADA                                | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (53.8%, no-rel 21.3%)]
   - Group 10: **0.4964** | UTAH, ARIZONA, KANSAS, GENESIS                                    | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (53.8%, no-rel 15.3%)]
   - Group 11: **0.4993** | UTAH, NEVADA, KANSAS, GENESIS                                     | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (54.0%, no-rel 15.3%)]
   - Group 12: **0.4937** | SOPRANO, MONTANA, COLORADO, ARIZONA                               | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (53.0%, no-rel 23.1%)]
   - Group 13: **0.4992** | SOPRANO, MONTANA, COLORADO, KANSAS                                | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (56.6%, no-rel 18.4%)]
   - Group 14: **0.4921** | UTAH, NEVADA, ARIZONA, GENESIS                                    | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (56.1%, no-rel 14.3%)]
   - Group 15: **0.4982** | COLORADO, UTAH, KANSAS, GENESIS                                   | INCORRECT (Max overlap: 2/4 with U.S. MOUNTAIN STATES) | [Pred Type: NAMED_ENTITY_SET (56.2%, no-rel 15.4%)]
   - Group 16: **0.4918** | SOPRANO, MONTANA, NEVADA, ARIZONA                                 | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (52.3%, no-rel 20.5%)]
   - Group 17: **0.4942** | SOPRANO, MONTANA, UTAH, KANSAS                                    | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (57.4%, no-rel 17.0%)]
   - Group 18: **0.4906** | COLORADO, NEVADA, ARIZONA, GENESIS                                | INCORRECT (Max overlap: 3/4 with U.S. MOUNTAIN STATES)
   - Group 19: **0.4952** | MONTANA, COLORADO, STARK, NEVADA                                  | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (54.1%, no-rel 21.1%)]
   - Group 20: **0.4612** | MONTANA, UTAH, HAWK, KANSAS                                       | INCORRECT (Max overlap: 2/4 with TONY ___) | [Pred Type: NAMED_ENTITY_SET (62.3%, no-rel 14.9%)]

---

## Puzzle 25 (ID: 837)
**Words on Board:** THEATER, GREEK/ROMAN GOD, SHAKE, BLUE, CUP, MARTIAN, SPACECRAFT, PROGRESSIVE, LIBERAL, RAINMAKER, CONE, GOOD SHEPHERD, FICTIONAL BOXER, LEFT, SPLIT, DEPARTED

### Ground Truth Categories:
* **Level 0 (LEFT-LEANING, POLITICALLY) [Type: SYNONYM_OR_NEAR]:** BLUE, LEFT, LIBERAL, PROGRESSIVE
* **Level 1 (ICE CREAM PARLOR ORDERS) [Type: SEMANTIC_SET]:** CONE, CUP, SHAKE, SPLIT
* **Level 2 (MATT DAMON MOVIES, WITH "THE") [Type: NAMED_ENTITY_SET]:** DEPARTED, GOOD SHEPHERD, MARTIAN, RAINMAKER
* **Level 3 (NAMED "APOLLO") [Type: NAMED_ENTITY_SET]:** FICTIONAL BOXER, GREEK/ROMAN GOD, SPACECRAFT, THEATER

### Top Candidate Partitions:
1. **Partition Score: 0.4363**
   - Group 1: **0.5542** | GREEK/ROMAN GOD, MARTIAN, RAINMAKER, FICTIONAL BOXER              | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 2: **0.4928** | SHAKE, LEFT, SPLIT, DEPARTED                                      | INCORRECT (Max overlap: 2/4 with ICE CREAM PARLOR ORDERS) | [Pred Type: SYNONYM_OR_NEAR (51.9%, no-rel 29.3%)]
   - Group 3: **0.4862** | THEATER, CUP, SPACECRAFT, CONE                                    | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 4: **0.3832** | BLUE, PROGRESSIVE, LIBERAL, GOOD SHEPHERD                         | INCORRECT (Max overlap: 3/4 with LEFT-LEANING, POLITICALLY) | [Pred Type: SYNONYM_OR_NEAR (62.9%, no-rel 27.3%)]
2. **Partition Score: 0.4325**
   - Group 1: **0.5841** | BLUE, PROGRESSIVE, LIBERAL, LEFT                                  | CORRECT GROUP (LEFT-LEANING, POLITICALLY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 27.4%)]
   - Group 2: **0.5542** | GREEK/ROMAN GOD, MARTIAN, RAINMAKER, FICTIONAL BOXER              | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 3: **0.4302** | SHAKE, CUP, CONE, SPLIT                                           | CORRECT GROUP (ICE CREAM PARLOR ORDERS, Level 1)
   - Group 4: **0.3728** | THEATER, SPACECRAFT, GOOD SHEPHERD, DEPARTED                      | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
3. **Partition Score: 0.4240**
   - Group 1: **0.5841** | BLUE, PROGRESSIVE, LIBERAL, LEFT                                  | CORRECT GROUP (LEFT-LEANING, POLITICALLY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 27.4%)]
   - Group 2: **0.4551** | GREEK/ROMAN GOD, MARTIAN, GOOD SHEPHERD, FICTIONAL BOXER          | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 3: **0.4302** | SHAKE, CUP, CONE, SPLIT                                           | CORRECT GROUP (ICE CREAM PARLOR ORDERS, Level 1)
   - Group 4: **0.4053** | THEATER, SPACECRAFT, RAINMAKER, DEPARTED                          | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
4. **Partition Score: 0.4191**
   - Group 1: **0.4928** | SHAKE, LEFT, SPLIT, DEPARTED                                      | INCORRECT (Max overlap: 2/4 with ICE CREAM PARLOR ORDERS) | [Pred Type: SYNONYM_OR_NEAR (51.9%, no-rel 29.3%)]
   - Group 2: **0.4677** | GREEK/ROMAN GOD, MARTIAN, SPACECRAFT, FICTIONAL BOXER             | INCORRECT (Max overlap: 3/4 with NAMED "APOLLO")
   - Group 3: **0.4423** | THEATER, CUP, RAINMAKER, CONE                                     | INCORRECT (Max overlap: 2/4 with ICE CREAM PARLOR ORDERS)
   - Group 4: **0.3832** | BLUE, PROGRESSIVE, LIBERAL, GOOD SHEPHERD                         | INCORRECT (Max overlap: 3/4 with LEFT-LEANING, POLITICALLY) | [Pred Type: SYNONYM_OR_NEAR (62.9%, no-rel 27.3%)]
5. **Partition Score: 0.4179**
   - Group 1: **0.5841** | BLUE, PROGRESSIVE, LIBERAL, LEFT                                  | CORRECT GROUP (LEFT-LEANING, POLITICALLY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 27.4%)]
   - Group 2: **0.5542** | GREEK/ROMAN GOD, MARTIAN, RAINMAKER, FICTIONAL BOXER              | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 3: **0.4074** | SHAKE, CUP, SPACECRAFT, CONE                                      | INCORRECT (Max overlap: 3/4 with ICE CREAM PARLOR ORDERS)
   - Group 4: **0.3551** | THEATER, GOOD SHEPHERD, SPLIT, DEPARTED                           | INCORRECT (Max overlap: 2/4 with MATT DAMON MOVIES, WITH "THE")

### Top Candidate Groups:
   - Group 1: **0.5542** | GREEK/ROMAN GOD, MARTIAN, RAINMAKER, FICTIONAL BOXER              | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 2: **0.4928** | SHAKE, LEFT, SPLIT, DEPARTED                                      | INCORRECT (Max overlap: 2/4 with ICE CREAM PARLOR ORDERS) | [Pred Type: SYNONYM_OR_NEAR (51.9%, no-rel 29.3%)]
   - Group 3: **0.4862** | THEATER, CUP, SPACECRAFT, CONE                                    | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 4: **0.3832** | BLUE, PROGRESSIVE, LIBERAL, GOOD SHEPHERD                         | INCORRECT (Max overlap: 3/4 with LEFT-LEANING, POLITICALLY) | [Pred Type: SYNONYM_OR_NEAR (62.9%, no-rel 27.3%)]
   - Group 5: **0.5841** | BLUE, PROGRESSIVE, LIBERAL, LEFT                                  | CORRECT GROUP (LEFT-LEANING, POLITICALLY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 27.4%)]
   - Group 6: **0.4302** | SHAKE, CUP, CONE, SPLIT                                           | CORRECT GROUP (ICE CREAM PARLOR ORDERS, Level 1)
   - Group 7: **0.3728** | THEATER, SPACECRAFT, GOOD SHEPHERD, DEPARTED                      | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 8: **0.4551** | GREEK/ROMAN GOD, MARTIAN, GOOD SHEPHERD, FICTIONAL BOXER          | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 9: **0.4053** | THEATER, SPACECRAFT, RAINMAKER, DEPARTED                          | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 10: **0.4677** | GREEK/ROMAN GOD, MARTIAN, SPACECRAFT, FICTIONAL BOXER             | INCORRECT (Max overlap: 3/4 with NAMED "APOLLO")
   - Group 11: **0.4423** | THEATER, CUP, RAINMAKER, CONE                                     | INCORRECT (Max overlap: 2/4 with ICE CREAM PARLOR ORDERS)
   - Group 12: **0.4074** | SHAKE, CUP, SPACECRAFT, CONE                                      | INCORRECT (Max overlap: 3/4 with ICE CREAM PARLOR ORDERS)
   - Group 13: **0.3551** | THEATER, GOOD SHEPHERD, SPLIT, DEPARTED                           | INCORRECT (Max overlap: 2/4 with MATT DAMON MOVIES, WITH "THE")
   - Group 14: **0.4538** | GREEK/ROMAN GOD, RAINMAKER, GOOD SHEPHERD, FICTIONAL BOXER        | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 15: **0.3919** | THEATER, MARTIAN, SPACECRAFT, DEPARTED                            | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 16: **0.4626** | PROGRESSIVE, LIBERAL, LEFT, DEPARTED                              | INCORRECT (Max overlap: 3/4 with LEFT-LEANING, POLITICALLY) | [Pred Type: SYNONYM_OR_NEAR (68.3%, no-rel 24.4%)]
   - Group 17: **0.4479** | THEATER, SPACECRAFT, RAINMAKER, CONE                              | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")
   - Group 18: **0.3783** | SHAKE, BLUE, CUP, SPLIT                                           | INCORRECT (Max overlap: 3/4 with ICE CREAM PARLOR ORDERS)
   - Group 19: **0.3744** | SHAKE, CUP, SPLIT, DEPARTED                                       | INCORRECT (Max overlap: 3/4 with ICE CREAM PARLOR ORDERS)
   - Group 20: **0.3573** | THEATER, SPACECRAFT, CONE, GOOD SHEPHERD                          | INCORRECT (Max overlap: 2/4 with NAMED "APOLLO")

---

## Puzzle 26 (ID: 498)
**Words on Board:** MUNG, PULL, DEAD, NAVY, DRIVE, NEUTRAL, DRAW, KIDNEY, LIVER, GRAB, REVERSE, PINTO, CAR, LOW, HOOK, WHIRL

### Ground Truth Categories:
* **Level 0 (KINDS OF BEANS) [Type: SEMANTIC_SET]:** KIDNEY, MUNG, NAVY, PINTO
* **Level 1 (ATTRACT) [Type: SYNONYM_OR_NEAR]:** DRAW, GRAB, HOOK, PULL
* **Level 2 (AUTOMATIC GEAR SHIFTER POSITIONS) [Type: SEMANTIC_SET]:** DRIVE, LOW, NEUTRAL, REVERSE
* **Level 3 (___POOL) [Type: FILL_IN_THE_BLANK]:** CAR, DEAD, LIVER, WHIRL

### Top Candidate Partitions:
1. **Partition Score: 0.3796**
   - Group 1: **0.5599** | NAVY, KIDNEY, LIVER, PINTO                                        | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.4992** | PULL, DRIVE, GRAB, HOOK                                           | INCORRECT (Max overlap: 3/4 with ATTRACT)
   - Group 3: **0.3535** | MUNG, NEUTRAL, REVERSE, CAR                                       | INCORRECT (Max overlap: 2/4 with AUTOMATIC GEAR SHIFTER POSITIONS) | [Pred Type: SEMANTIC_SET (50.2%, no-rel 19.7%)]
   - Group 4: **0.3329** | DEAD, DRAW, LOW, WHIRL                                            | INCORRECT (Max overlap: 2/4 with ___POOL)
2. **Partition Score: 0.3774**
   - Group 1: **0.5599** | NAVY, KIDNEY, LIVER, PINTO                                        | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.4369** | PULL, DRIVE, DRAW, CAR                                            | INCORRECT (Max overlap: 2/4 with ATTRACT)
   - Group 3: **0.3893** | MUNG, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 4: **0.3416** | DEAD, GRAB, HOOK, WHIRL                                           | INCORRECT (Max overlap: 2/4 with ___POOL)
3. **Partition Score: 0.3771**
   - Group 1: **0.5599** | NAVY, KIDNEY, LIVER, PINTO                                        | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.3964** | PULL, DRIVE, CAR, HOOK                                            | INCORRECT (Max overlap: 2/4 with ATTRACT)
   - Group 3: **0.3893** | MUNG, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 4: **0.3613** | DEAD, DRAW, GRAB, WHIRL                                           | INCORRECT (Max overlap: 2/4 with ___POOL)
4. **Partition Score: 0.3759**
   - Group 1: **0.6420** | PULL, DRIVE, DRAW, HOOK                                           | INCORRECT (Max overlap: 3/4 with ATTRACT) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 33.7%)]
   - Group 2: **0.5599** | NAVY, KIDNEY, LIVER, PINTO                                        | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 3: **0.3535** | MUNG, NEUTRAL, REVERSE, CAR                                       | INCORRECT (Max overlap: 2/4 with AUTOMATIC GEAR SHIFTER POSITIONS) | [Pred Type: SEMANTIC_SET (50.2%, no-rel 19.7%)]
   - Group 4: **0.2950** | DEAD, GRAB, LOW, WHIRL                                            | INCORRECT (Max overlap: 2/4 with ___POOL)
5. **Partition Score: 0.3734**
   - Group 1: **0.5599** | NAVY, KIDNEY, LIVER, PINTO                                        | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.4693** | PULL, GRAB, HOOK, WHIRL                                           | INCORRECT (Max overlap: 3/4 with ATTRACT)
   - Group 3: **0.3893** | MUNG, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 4: **0.3176** | DEAD, DRIVE, DRAW, CAR                                            | INCORRECT (Max overlap: 2/4 with ___POOL)

### Top Candidate Groups:
   - Group 1: **0.5599** | NAVY, KIDNEY, LIVER, PINTO                                        | INCORRECT (Max overlap: 3/4 with KINDS OF BEANS)
   - Group 2: **0.4992** | PULL, DRIVE, GRAB, HOOK                                           | INCORRECT (Max overlap: 3/4 with ATTRACT)
   - Group 3: **0.3535** | MUNG, NEUTRAL, REVERSE, CAR                                       | INCORRECT (Max overlap: 2/4 with AUTOMATIC GEAR SHIFTER POSITIONS) | [Pred Type: SEMANTIC_SET (50.2%, no-rel 19.7%)]
   - Group 4: **0.3329** | DEAD, DRAW, LOW, WHIRL                                            | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 5: **0.4369** | PULL, DRIVE, DRAW, CAR                                            | INCORRECT (Max overlap: 2/4 with ATTRACT)
   - Group 6: **0.3893** | MUNG, NEUTRAL, REVERSE, LOW                                       | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 7: **0.3416** | DEAD, GRAB, HOOK, WHIRL                                           | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 8: **0.3964** | PULL, DRIVE, CAR, HOOK                                            | INCORRECT (Max overlap: 2/4 with ATTRACT)
   - Group 9: **0.3613** | DEAD, DRAW, GRAB, WHIRL                                           | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 10: **0.6420** | PULL, DRIVE, DRAW, HOOK                                           | INCORRECT (Max overlap: 3/4 with ATTRACT) | [Pred Type: SYNONYM_OR_NEAR (52.6%, no-rel 33.7%)]
   - Group 11: **0.2950** | DEAD, GRAB, LOW, WHIRL                                            | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 12: **0.4693** | PULL, GRAB, HOOK, WHIRL                                           | INCORRECT (Max overlap: 3/4 with ATTRACT)
   - Group 13: **0.3176** | DEAD, DRIVE, DRAW, CAR                                            | INCORRECT (Max overlap: 2/4 with ___POOL)
   - Group 14: **0.4179** | PULL, DEAD, DRIVE, DRAW                                           | INCORRECT (Max overlap: 2/4 with ATTRACT) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 30.4%)]
   - Group 15: **0.3523** | GRAB, LOW, HOOK, WHIRL                                            | INCORRECT (Max overlap: 2/4 with ATTRACT)
   - Group 16: **0.4121** | PULL, DRIVE, GRAB, WHIRL                                          | INCORRECT (Max overlap: 2/4 with ATTRACT)
   - Group 17: **0.3539** | DEAD, DRAW, LOW, HOOK                                             | INCORRECT (Max overlap: 2/4 with ATTRACT) | [Pred Type: SYNONYM_OR_NEAR (57.7%, no-rel 28.7%)]
   - Group 18: **0.3243** | DEAD, DRIVE, DRAW, LOW                                            | INCORRECT (Max overlap: 2/4 with AUTOMATIC GEAR SHIFTER POSITIONS)
   - Group 19: **0.5297** | MUNG, NAVY, KIDNEY, PINTO                                         | CORRECT GROUP (KINDS OF BEANS, Level 0)
   - Group 20: **0.3483** | NEUTRAL, LIVER, REVERSE, LOW                                      | INCORRECT (Max overlap: 3/4 with AUTOMATIC GEAR SHIFTER POSITIONS)

---

## Puzzle 27 (ID: 751)
**Words on Board:** SHARP, SMART, BRUSH, PINCH, TIDY, SHOWER, KEY, PALM, NICK, TOUCH, BIRTH, MILE, NEAT, SHAVE, DRESS, POCKET

### Ground Truth Categories:
* **Level 0 (STEAL) [Type: SYNONYM_OR_NEAR]:** NICK, PALM, PINCH, POCKET
* **Level 1 (DO SOME GROOMING) [Type: SEMANTIC_SET]:** BRUSH, DRESS, SHAVE, SHOWER
* **Level 2 (DAPPER) [Type: SYNONYM_OR_NEAR]:** NEAT, SHARP, SMART, TIDY
* **Level 3 (___STONE) [Type: FILL_IN_THE_BLANK]:** BIRTH, KEY, MILE, TOUCH

### Top Candidate Partitions:
1. **Partition Score: 0.3700**
   - Group 1: **0.4553** | SHARP, SMART, TIDY, NEAT                                          | CORRECT GROUP (DAPPER, Level 2) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 34.7%)]
   - Group 2: **0.3867** | BRUSH, SHOWER, SHAVE, DRESS                                       | CORRECT GROUP (DO SOME GROOMING, Level 1)
   - Group 3: **0.3765** | PALM, NICK, BIRTH, MILE                                           | INCORRECT (Max overlap: 2/4 with STEAL)
   - Group 4: **0.3584** | PINCH, KEY, TOUCH, POCKET                                         | INCORRECT (Max overlap: 2/4 with STEAL) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 29.3%)]
2. **Partition Score: 0.3649**
   - Group 1: **0.3867** | BRUSH, SHOWER, SHAVE, DRESS                                       | CORRECT GROUP (DO SOME GROOMING, Level 1)
   - Group 2: **0.3765** | PALM, NICK, BIRTH, MILE                                           | INCORRECT (Max overlap: 2/4 with STEAL)
   - Group 3: **0.3701** | SHARP, PINCH, KEY, POCKET                                         | INCORRECT (Max overlap: 2/4 with STEAL)
   - Group 4: **0.3565** | SMART, TIDY, TOUCH, NEAT                                          | INCORRECT (Max overlap: 3/4 with DAPPER) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 33.7%)]
3. **Partition Score: 0.3586**
   - Group 1: **0.4575** | PINCH, PALM, TOUCH, POCKET                                        | INCORRECT (Max overlap: 3/4 with STEAL) | [Pred Type: SYNONYM_OR_NEAR (48.4%, no-rel 25.3%)]
   - Group 2: **0.4553** | SHARP, SMART, TIDY, NEAT                                          | CORRECT GROUP (DAPPER, Level 2) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 34.7%)]
   - Group 3: **0.3867** | BRUSH, SHOWER, SHAVE, DRESS                                       | CORRECT GROUP (DO SOME GROOMING, Level 1)
   - Group 4: **0.2962** | KEY, NICK, BIRTH, MILE                                            | INCORRECT (Max overlap: 3/4 with ___STONE)
4. **Partition Score: 0.3461**
   - Group 1: **0.3765** | PALM, NICK, BIRTH, MILE                                           | INCORRECT (Max overlap: 2/4 with STEAL)
   - Group 2: **0.3701** | SHARP, PINCH, KEY, POCKET                                         | INCORRECT (Max overlap: 2/4 with STEAL)
   - Group 3: **0.3485** | SMART, SHOWER, SHAVE, DRESS                                       | INCORRECT (Max overlap: 3/4 with DO SOME GROOMING)
   - Group 4: **0.3329** | BRUSH, TIDY, TOUCH, NEAT                                          | INCORRECT (Max overlap: 2/4 with DAPPER) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 26.2%)]
5. **Partition Score: 0.3449**
   - Group 1: **0.4156** | SHARP, SMART, KEY, POCKET                                         | INCORRECT (Max overlap: 2/4 with DAPPER)
   - Group 2: **0.3867** | BRUSH, SHOWER, SHAVE, DRESS                                       | CORRECT GROUP (DO SOME GROOMING, Level 1)
   - Group 3: **0.3765** | PALM, NICK, BIRTH, MILE                                           | INCORRECT (Max overlap: 2/4 with STEAL)
   - Group 4: **0.3082** | PINCH, TIDY, TOUCH, NEAT                                          | INCORRECT (Max overlap: 2/4 with DAPPER) | [Pred Type: SYNONYM_OR_NEAR (64.8%, no-rel 24.9%)]

### Top Candidate Groups:
   - Group 1: **0.4553** | SHARP, SMART, TIDY, NEAT                                          | CORRECT GROUP (DAPPER, Level 2) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 34.7%)]
   - Group 2: **0.3867** | BRUSH, SHOWER, SHAVE, DRESS                                       | CORRECT GROUP (DO SOME GROOMING, Level 1)
   - Group 3: **0.3765** | PALM, NICK, BIRTH, MILE                                           | INCORRECT (Max overlap: 2/4 with STEAL)
   - Group 4: **0.3584** | PINCH, KEY, TOUCH, POCKET                                         | INCORRECT (Max overlap: 2/4 with STEAL) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 29.3%)]
   - Group 5: **0.3701** | SHARP, PINCH, KEY, POCKET                                         | INCORRECT (Max overlap: 2/4 with STEAL)
   - Group 6: **0.3565** | SMART, TIDY, TOUCH, NEAT                                          | INCORRECT (Max overlap: 3/4 with DAPPER) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 33.7%)]
   - Group 7: **0.4575** | PINCH, PALM, TOUCH, POCKET                                        | INCORRECT (Max overlap: 3/4 with STEAL) | [Pred Type: SYNONYM_OR_NEAR (48.4%, no-rel 25.3%)]
   - Group 8: **0.2962** | KEY, NICK, BIRTH, MILE                                            | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 9: **0.3485** | SMART, SHOWER, SHAVE, DRESS                                       | INCORRECT (Max overlap: 3/4 with DO SOME GROOMING)
   - Group 10: **0.3329** | BRUSH, TIDY, TOUCH, NEAT                                          | INCORRECT (Max overlap: 2/4 with DAPPER) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 26.2%)]
   - Group 11: **0.4156** | SHARP, SMART, KEY, POCKET                                         | INCORRECT (Max overlap: 2/4 with DAPPER)
   - Group 12: **0.3082** | PINCH, TIDY, TOUCH, NEAT                                          | INCORRECT (Max overlap: 2/4 with DAPPER) | [Pred Type: SYNONYM_OR_NEAR (64.8%, no-rel 24.9%)]
   - Group 13: **0.3952** | BRUSH, PINCH, TOUCH, POCKET                                       | INCORRECT (Max overlap: 2/4 with STEAL) | [Pred Type: SYNONYM_OR_NEAR (55.7%, no-rel 28.0%)]
   - Group 14: **0.3001** | SHOWER, KEY, SHAVE, DRESS                                         | INCORRECT (Max overlap: 3/4 with DO SOME GROOMING)
   - Group 15: **0.3900** | PINCH, NICK, TOUCH, POCKET                                        | INCORRECT (Max overlap: 3/4 with STEAL) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 23.1%)]
   - Group 16: **0.2960** | KEY, PALM, BIRTH, MILE                                            | INCORRECT (Max overlap: 3/4 with ___STONE)
   - Group 17: **0.3798** | SHOWER, NICK, SHAVE, DRESS                                        | INCORRECT (Max overlap: 3/4 with DO SOME GROOMING)
   - Group 18: **0.3233** | SHOWER, BIRTH, SHAVE, DRESS                                       | INCORRECT (Max overlap: 3/4 with DO SOME GROOMING)
   - Group 19: **0.3087** | KEY, PALM, NICK, MILE                                             | INCORRECT (Max overlap: 2/4 with ___STONE)
   - Group 20: **0.3662** | SHARP, SHOWER, SHAVE, DRESS                                       | INCORRECT (Max overlap: 3/4 with DO SOME GROOMING)

---

## Puzzle 28 (ID: 88)
**Words on Board:** ROGER, ROAD, MET, FRAMED, PICTURE, MAX, WHO, MAD, WHEN, HARRY, HORROR, SALLY, ROCKY, RABBIT, SHOW, FURY

### Ground Truth Categories:
* **Level 0 (ROCKY HORROR PICTURE SHOW) [Type: NAMED_ENTITY_SET]:** HORROR, PICTURE, ROCKY, SHOW
* **Level 1 (WHO FRAMED ROGER RABBIT) [Type: NAMED_ENTITY_SET]:** FRAMED, RABBIT, ROGER, WHO
* **Level 2 (WHEN HARRY MET SALLY) [Type: NAMED_ENTITY_SET]:** HARRY, MET, SALLY, WHEN
* **Level 3 (MAD MAX FURY ROAD) [Type: NAMED_ENTITY_SET]:** FURY, MAD, MAX, ROAD

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.5696** | ROGER, HARRY, ROCKY, FURY                                         | INCORRECT (Max overlap: 1/4 with WHO FRAMED ROGER RABBIT) | [Pred Type: NAMED_ENTITY_SET (55.1%, no-rel 19.9%)]
   - Group 2: **0.5361** | ROGER, HARRY, SALLY, ROCKY                                        | INCORRECT (Max overlap: 2/4 with WHEN HARRY MET SALLY)
   - Group 3: **0.5335** | HARRY, HORROR, ROCKY, FURY                                        | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 4: **0.5117** | ROGER, HARRY, SALLY, FURY                                         | INCORRECT (Max overlap: 2/4 with WHEN HARRY MET SALLY) | [Pred Type: NAMED_ENTITY_SET (54.5%, no-rel 17.9%)]
   - Group 5: **0.5103** | ROGER, MAX, HARRY, SALLY                                          | INCORRECT (Max overlap: 2/4 with WHEN HARRY MET SALLY) | [Pred Type: NAMED_ENTITY_SET (45.8%, no-rel 22.8%)]
   - Group 6: **0.5067** | MAX, HARRY, ROCKY, FURY                                           | INCORRECT (Max overlap: 2/4 with MAD MAX FURY ROAD) | [Pred Type: NAMED_ENTITY_SET (51.1%, no-rel 19.3%)]
   - Group 7: **0.4993** | ROGER, WHO, HARRY, FURY                                           | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT) | [Pred Type: NAMED_ENTITY_SET (56.5%, no-rel 18.5%)]
   - Group 8: **0.4923** | WHO, HARRY, ROCKY, FURY                                           | INCORRECT (Max overlap: 1/4 with WHO FRAMED ROGER RABBIT) | [Pred Type: NAMED_ENTITY_SET (46.5%, no-rel 22.1%)]
   - Group 9: **0.4911** | ROGER, MAX, HARRY, FURY                                           | INCORRECT (Max overlap: 2/4 with MAD MAX FURY ROAD) | [Pred Type: NAMED_ENTITY_SET (59.3%, no-rel 16.7%)]
   - Group 10: **0.4909** | ROGER, MAX, HARRY, ROCKY                                          | INCORRECT (Max overlap: 1/4 with WHO FRAMED ROGER RABBIT) | [Pred Type: NAMED_ENTITY_SET (50.2%, no-rel 21.7%)]
   - Group 11: **0.4900** | ROAD, FRAMED, PICTURE, SHOW                                       | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW) | [Pred Type: SYNONYM_OR_NEAR (61.3%, no-rel 28.6%)]
   - Group 12: **0.4898** | ROGER, HARRY, SALLY, RABBIT                                       | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT)
   - Group 13: **0.4886** | ROGER, MAX, MAD, FURY                                             | INCORRECT (Max overlap: 3/4 with MAD MAX FURY ROAD) | [Pred Type: NAMED_ENTITY_SET (61.1%, no-rel 16.0%)]
   - Group 14: **0.4875** | ROGER, WHO, WHEN, FURY                                            | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT) | [Pred Type: NAMED_ENTITY_SET (52.8%, no-rel 19.6%)]
   - Group 15: **0.4867** | HARRY, SALLY, ROCKY, RABBIT                                       | INCORRECT (Max overlap: 2/4 with WHEN HARRY MET SALLY)
   - Group 16: **0.4850** | HARRY, HORROR, ROCKY, RABBIT                                      | INCORRECT (Max overlap: 2/4 with ROCKY HORROR PICTURE SHOW)
   - Group 17: **0.4848** | ROGER, MAX, ROCKY, FURY                                           | INCORRECT (Max overlap: 2/4 with MAD MAX FURY ROAD) | [Pred Type: NAMED_ENTITY_SET (58.2%, no-rel 19.1%)]
   - Group 18: **0.4845** | MAX, WHO, HARRY, FURY                                             | INCORRECT (Max overlap: 2/4 with MAD MAX FURY ROAD) | [Pred Type: NAMED_ENTITY_SET (50.8%, no-rel 18.7%)]
   - Group 19: **0.4830** | ROGER, MAX, WHO, FURY                                             | INCORRECT (Max overlap: 2/4 with WHO FRAMED ROGER RABBIT) | [Pred Type: NAMED_ENTITY_SET (57.9%, no-rel 17.9%)]
   - Group 20: **0.4810** | ROGER, SALLY, ROCKY, FURY                                         | INCORRECT (Max overlap: 1/4 with WHO FRAMED ROGER RABBIT) | [Pred Type: NAMED_ENTITY_SET (54.4%, no-rel 18.9%)]

---

## Puzzle 29 (ID: 81)
**Words on Board:** SCRATCH, NICK, NACHO, DING, BINGO, LUMBER, WING, APPLE, POPPER, FRY, YES, RIGHT, CRACKER, CHIP, CORRECT, FLAP

### Ground Truth Categories:
* **Level 0 (APPETIZER UNIT) [Type: SEMANTIC_SET]:** FRY, NACHO, POPPER, WING
* **Level 1 (RESPONSE TO A CORRECT ANSWER) [Type: SYNONYM_OR_NEAR]:** BINGO, CORRECT, RIGHT, YES
* **Level 2 (MAR) [Type: SYNONYM_OR_NEAR]:** CHIP, DING, NICK, SCRATCH
* **Level 3 (___JACK) [Type: FILL_IN_THE_BLANK]:** APPLE, CRACKER, FLAP, LUMBER

### Top Candidate Partitions:
1. **Partition Score: 0.4416**
   - Group 1: **0.5288** | NICK, NACHO, DING, CHIP                                           | INCORRECT (Max overlap: 3/4 with MAR) | [Pred Type: SYNONYM_OR_NEAR (48.4%, no-rel 17.6%)]
   - Group 2: **0.5133** | WING, YES, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 3/4 with RESPONSE TO A CORRECT ANSWER) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 36.8%)]
   - Group 3: **0.4287** | LUMBER, APPLE, POPPER, FRY                                        | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 4: **0.4121** | SCRATCH, BINGO, CRACKER, FLAP                                     | INCORRECT (Max overlap: 2/4 with ___JACK)
2. **Partition Score: 0.4416**
   - Group 1: **0.5359** | NICK, DING, FRY, CHIP                                             | INCORRECT (Max overlap: 3/4 with MAR) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 20.5%)]
   - Group 2: **0.5133** | WING, YES, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 3/4 with RESPONSE TO A CORRECT ANSWER) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 36.8%)]
   - Group 3: **0.4286** | NACHO, LUMBER, APPLE, POPPER                                      | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT)
   - Group 4: **0.4121** | SCRATCH, BINGO, CRACKER, FLAP                                     | INCORRECT (Max overlap: 2/4 with ___JACK)
3. **Partition Score: 0.4340**
   - Group 1: **0.5133** | WING, YES, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 3/4 with RESPONSE TO A CORRECT ANSWER) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 36.8%)]
   - Group 2: **0.4587** | SCRATCH, DING, BINGO, FLAP                                        | INCORRECT (Max overlap: 2/4 with MAR)
   - Group 3: **0.4287** | LUMBER, APPLE, POPPER, FRY                                        | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 4: **0.4243** | NICK, NACHO, CRACKER, CHIP                                        | INCORRECT (Max overlap: 2/4 with MAR) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 20.1%)]
4. **Partition Score: 0.4294**
   - Group 1: **0.4896** | NICK, YES, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 3/4 with RESPONSE TO A CORRECT ANSWER) | [Pred Type: SYNONYM_OR_NEAR (56.0%, no-rel 32.2%)]
   - Group 2: **0.4639** | SCRATCH, BINGO, WING, FLAP                                        | INCORRECT (Max overlap: 1/4 with MAR)
   - Group 3: **0.4287** | LUMBER, APPLE, POPPER, FRY                                        | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 4: **0.4124** | NACHO, DING, CRACKER, CHIP                                        | INCORRECT (Max overlap: 2/4 with MAR) | [Pred Type: SEMANTIC_SET (55.0%, no-rel 16.7%)]
5. **Partition Score: 0.4243**
   - Group 1: **0.5133** | WING, YES, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 3/4 with RESPONSE TO A CORRECT ANSWER) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 36.8%)]
   - Group 2: **0.4587** | SCRATCH, DING, BINGO, FLAP                                        | INCORRECT (Max overlap: 2/4 with MAR)
   - Group 3: **0.4214** | NICK, LUMBER, APPLE, POPPER                                       | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 4: **0.4084** | NACHO, FRY, CRACKER, CHIP                                         | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT) | [Pred Type: SEMANTIC_SET (54.1%, no-rel 18.4%)]

### Top Candidate Groups:
   - Group 1: **0.5288** | NICK, NACHO, DING, CHIP                                           | INCORRECT (Max overlap: 3/4 with MAR) | [Pred Type: SYNONYM_OR_NEAR (48.4%, no-rel 17.6%)]
   - Group 2: **0.5133** | WING, YES, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 3/4 with RESPONSE TO A CORRECT ANSWER) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 36.8%)]
   - Group 3: **0.4287** | LUMBER, APPLE, POPPER, FRY                                        | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 4: **0.4121** | SCRATCH, BINGO, CRACKER, FLAP                                     | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 5: **0.5359** | NICK, DING, FRY, CHIP                                             | INCORRECT (Max overlap: 3/4 with MAR) | [Pred Type: SYNONYM_OR_NEAR (59.1%, no-rel 20.5%)]
   - Group 6: **0.4286** | NACHO, LUMBER, APPLE, POPPER                                      | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT)
   - Group 7: **0.4587** | SCRATCH, DING, BINGO, FLAP                                        | INCORRECT (Max overlap: 2/4 with MAR)
   - Group 8: **0.4243** | NICK, NACHO, CRACKER, CHIP                                        | INCORRECT (Max overlap: 2/4 with MAR) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 20.1%)]
   - Group 9: **0.4896** | NICK, YES, RIGHT, CORRECT                                         | INCORRECT (Max overlap: 3/4 with RESPONSE TO A CORRECT ANSWER) | [Pred Type: SYNONYM_OR_NEAR (56.0%, no-rel 32.2%)]
   - Group 10: **0.4639** | SCRATCH, BINGO, WING, FLAP                                        | INCORRECT (Max overlap: 1/4 with MAR)
   - Group 11: **0.4124** | NACHO, DING, CRACKER, CHIP                                        | INCORRECT (Max overlap: 2/4 with MAR) | [Pred Type: SEMANTIC_SET (55.0%, no-rel 16.7%)]
   - Group 12: **0.4214** | NICK, LUMBER, APPLE, POPPER                                       | INCORRECT (Max overlap: 2/4 with ___JACK)
   - Group 13: **0.4084** | NACHO, FRY, CRACKER, CHIP                                         | INCORRECT (Max overlap: 2/4 with APPETIZER UNIT) | [Pred Type: SEMANTIC_SET (54.1%, no-rel 18.4%)]
   - Group 14: **0.4726** | SCRATCH, NICK, RIGHT, CORRECT                                     | INCORRECT (Max overlap: 2/4 with MAR) | [Pred Type: SYNONYM_OR_NEAR (62.3%, no-rel 28.5%)]
   - Group 15: **0.4432** | BINGO, WING, YES, FLAP                                            | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 16: **0.5225** | BINGO, YES, RIGHT, CORRECT                                        | CORRECT GROUP (RESPONSE TO A CORRECT ANSWER, Level 1) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 38.7%)]
   - Group 17: **0.4202** | SCRATCH, DING, WING, FLAP                                         | INCORRECT (Max overlap: 2/4 with MAR)
   - Group 18: **0.4526** | NICK, WING, RIGHT, CORRECT                                        | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 26.4%)]
   - Group 19: **0.4355** | SCRATCH, BINGO, YES, FLAP                                         | INCORRECT (Max overlap: 2/4 with RESPONSE TO A CORRECT ANSWER)
   - Group 20: **0.3991** | NICK, FRY, CRACKER, CHIP                                          | INCORRECT (Max overlap: 2/4 with MAR) | [Pred Type: SYNONYM_OR_NEAR (61.1%, no-rel 23.1%)]

---

## Puzzle 30 (ID: 1018)
**Words on Board:** PITCHER, ENTER, BOARD, MOMENTUM, ACCELERATION, POWER, FIGURE, ILLUSTRATION, FORCE, MOUNT, EMBARK, PLATE, MASS, ROBERT, PICTURE, FACE

### Ground Truth Categories:
* **Level 0 (STEP ONTO, AS A VEHICLE) [Type: SYNONYM_OR_NEAR]:** BOARD, EMBARK, ENTER, MOUNT
* **Level 1 (QUANTITIES IN MECHANICS) [Type: SEMANTIC_SET]:** ACCELERATION, FORCE, MASS, MOMENTUM
* **Level 2 (TEXTBOOK IMAGES) [Type: SYNONYM_OR_NEAR]:** FIGURE, ILLUSTRATION, PICTURE, PLATE
* **Level 3 (___ PLANT) [Type: FILL_IN_THE_BLANK]:** FACE, PITCHER, POWER, ROBERT

### Top Candidate Partitions:
1. **Partition Score: 0.3964**
   - Group 1: **0.5488** | ENTER, BOARD, FIGURE, EMBARK                                      | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (60.1%, no-rel 31.7%)]
   - Group 2: **0.4938** | ILLUSTRATION, PLATE, PICTURE, FACE                                | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 3: **0.4322** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 23.7%)]
   - Group 4: **0.3297** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)
2. **Partition Score: 0.3860**
   - Group 1: **0.6478** | FIGURE, ILLUSTRATION, PLATE, PICTURE                              | CORRECT GROUP (TEXTBOOK IMAGES, Level 2) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 37.2%)]
   - Group 2: **0.4526** | ENTER, BOARD, EMBARK, FACE                                        | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 35.3%)]
   - Group 3: **0.4322** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 23.7%)]
   - Group 4: **0.3297** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)
3. **Partition Score: 0.3847**
   - Group 1: **0.5402** | BOARD, ILLUSTRATION, PLATE, PICTURE                               | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 2: **0.4471** | ENTER, FIGURE, EMBARK, FACE                                       | INCORRECT (Max overlap: 2/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (59.4%, no-rel 33.0%)]
   - Group 3: **0.4322** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 23.7%)]
   - Group 4: **0.3297** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)
4. **Partition Score: 0.3821**
   - Group 1: **0.4557** | BOARD, ILLUSTRATION, PLATE, FACE                                  | INCORRECT (Max overlap: 2/4 with TEXTBOOK IMAGES)
   - Group 2: **0.4367** | ENTER, FIGURE, EMBARK, PICTURE                                    | INCORRECT (Max overlap: 2/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 33.5%)]
   - Group 3: **0.4322** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 23.7%)]
   - Group 4: **0.3297** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)
5. **Partition Score: 0.3762**
   - Group 1: **0.5108** | BOARD, PLATE, PICTURE, FACE                                       | INCORRECT (Max overlap: 2/4 with TEXTBOOK IMAGES)
   - Group 2: **0.4322** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 23.7%)]
   - Group 3: **0.4133** | ENTER, FIGURE, ILLUSTRATION, EMBARK                               | INCORRECT (Max overlap: 2/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 27.3%)]
   - Group 4: **0.3297** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)

### Top Candidate Groups:
   - Group 1: **0.5488** | ENTER, BOARD, FIGURE, EMBARK                                      | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (60.1%, no-rel 31.7%)]
   - Group 2: **0.4938** | ILLUSTRATION, PLATE, PICTURE, FACE                                | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 3: **0.4322** | MOMENTUM, POWER, FORCE, MASS                                      | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 23.7%)]
   - Group 4: **0.3297** | PITCHER, ACCELERATION, MOUNT, ROBERT                              | INCORRECT (Max overlap: 2/4 with ___ PLANT)
   - Group 5: **0.6478** | FIGURE, ILLUSTRATION, PLATE, PICTURE                              | CORRECT GROUP (TEXTBOOK IMAGES, Level 2) | [Pred Type: SYNONYM_OR_NEAR (48.6%, no-rel 37.2%)]
   - Group 6: **0.4526** | ENTER, BOARD, EMBARK, FACE                                        | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 35.3%)]
   - Group 7: **0.5402** | BOARD, ILLUSTRATION, PLATE, PICTURE                               | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 8: **0.4471** | ENTER, FIGURE, EMBARK, FACE                                       | INCORRECT (Max overlap: 2/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (59.4%, no-rel 33.0%)]
   - Group 9: **0.4557** | BOARD, ILLUSTRATION, PLATE, FACE                                  | INCORRECT (Max overlap: 2/4 with TEXTBOOK IMAGES)
   - Group 10: **0.4367** | ENTER, FIGURE, EMBARK, PICTURE                                    | INCORRECT (Max overlap: 2/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 33.5%)]
   - Group 11: **0.5108** | BOARD, PLATE, PICTURE, FACE                                       | INCORRECT (Max overlap: 2/4 with TEXTBOOK IMAGES)
   - Group 12: **0.4133** | ENTER, FIGURE, ILLUSTRATION, EMBARK                               | INCORRECT (Max overlap: 2/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 27.3%)]
   - Group 13: **0.4286** | ENTER, BOARD, MOUNT, EMBARK                                       | CORRECT GROUP (STEP ONTO, AS A VEHICLE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (55.9%, no-rel 32.6%)]
   - Group 14: **0.4081** | PITCHER, ILLUSTRATION, PLATE, PICTURE                             | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 15: **0.3628** | MOMENTUM, ACCELERATION, MASS, ROBERT                              | INCORRECT (Max overlap: 3/4 with QUANTITIES IN MECHANICS)
   - Group 16: **0.3596** | POWER, FIGURE, FORCE, FACE                                        | INCORRECT (Max overlap: 2/4 with ___ PLANT) | [Pred Type: SYNONYM_OR_NEAR (56.5%, no-rel 33.7%)]
   - Group 17: **0.5202** | FIGURE, PLATE, PICTURE, FACE                                      | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES)
   - Group 18: **0.3929** | ENTER, BOARD, ILLUSTRATION, EMBARK                                | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 27.5%)]
   - Group 19: **0.6461** | FIGURE, ILLUSTRATION, PICTURE, FACE                               | INCORRECT (Max overlap: 3/4 with TEXTBOOK IMAGES) | [Pred Type: SYNONYM_OR_NEAR (55.5%, no-rel 34.2%)]
   - Group 20: **0.3892** | ENTER, BOARD, EMBARK, PLATE                                       | INCORRECT (Max overlap: 3/4 with STEP ONTO, AS A VEHICLE) | [Pred Type: SYNONYM_OR_NEAR (56.4%, no-rel 32.3%)]

---

## Puzzle 31 (ID: 916)
**Words on Board:** FAWN, PORKY, PRAISE, EMPEROR, GUSH, PRINCESS, PIGLET, DUCKLING, COLONEL, CHALK, WOULD, NAPOLEON, FLATTER, CALF, BABE, MERMAID

### Ground Truth Categories:
* **Level 0 (LAY IT ON THICK) [Type: SYNONYM_OR_NEAR]:** FAWN, FLATTER, GUSH, PRAISE
* **Level 1 (HANS CHRISTIAN ANDERSON FIGURES) [Type: NAMED_ENTITY_SET]:** DUCKLING, EMPEROR, MERMAID, PRINCESS
* **Level 2 (SILENT "L") [Type: SOUND_OR_SPELLING]:** CALF, CHALK, COLONEL, WOULD
* **Level 3 (FICTIONAL PIGS) [Type: NAMED_ENTITY_SET]:** BABE, NAPOLEON, PIGLET, PORKY

### Top Candidate Partitions:
1. **Partition Score: 0.4514**
   - Group 1: **0.5453** | FAWN, PRAISE, GUSH, FLATTER                                       | CORRECT GROUP (LAY IT ON THICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 29.2%)]
   - Group 2: **0.4947** | PRINCESS, CHALK, NAPOLEON, MERMAID                                | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 3: **0.4448** | EMPEROR, PIGLET, DUCKLING, CALF                                   | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 4: **0.4331** | PORKY, COLONEL, WOULD, BABE                                       | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
2. **Partition Score: 0.4461**
   - Group 1: **0.5453** | FAWN, PRAISE, GUSH, FLATTER                                       | CORRECT GROUP (LAY IT ON THICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 29.2%)]
   - Group 2: **0.4814** | EMPEROR, PRINCESS, CHALK, NAPOLEON                                | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 3: **0.4369** | PIGLET, DUCKLING, CALF, MERMAID                                   | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 4: **0.4331** | PORKY, COLONEL, WOULD, BABE                                       | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
3. **Partition Score: 0.4413**
   - Group 1: **0.5453** | FAWN, PRAISE, GUSH, FLATTER                                       | CORRECT GROUP (LAY IT ON THICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 29.2%)]
   - Group 2: **0.5103** | DUCKLING, CHALK, NAPOLEON, MERMAID                                | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 3: **0.4331** | PORKY, COLONEL, WOULD, BABE                                       | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
   - Group 4: **0.4110** | EMPEROR, PRINCESS, PIGLET, CALF                                   | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
4. **Partition Score: 0.4402**
   - Group 1: **0.5453** | FAWN, PRAISE, GUSH, FLATTER                                       | CORRECT GROUP (LAY IT ON THICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 29.2%)]
   - Group 2: **0.4814** | EMPEROR, PRINCESS, CHALK, NAPOLEON                                | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 3: **0.4593** | PORKY, PIGLET, DUCKLING, CALF                                     | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
   - Group 4: **0.4101** | COLONEL, WOULD, BABE, MERMAID                                     | INCORRECT (Max overlap: 2/4 with SILENT "L")
5. **Partition Score: 0.4393**
   - Group 1: **0.5453** | FAWN, PRAISE, GUSH, FLATTER                                       | CORRECT GROUP (LAY IT ON THICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 29.2%)]
   - Group 2: **0.4652** | PRINCESS, COLONEL, CHALK, MERMAID                                 | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES) | [Pred Type: NAMED_ENTITY_SET (45.6%, no-rel 25.2%)]
   - Group 3: **0.4448** | EMPEROR, PIGLET, DUCKLING, CALF                                   | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 4: **0.4236** | PORKY, WOULD, NAPOLEON, BABE                                      | INCORRECT (Max overlap: 3/4 with FICTIONAL PIGS)

### Top Candidate Groups:
   - Group 1: **0.5453** | FAWN, PRAISE, GUSH, FLATTER                                       | CORRECT GROUP (LAY IT ON THICK, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 29.2%)]
   - Group 2: **0.4947** | PRINCESS, CHALK, NAPOLEON, MERMAID                                | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 3: **0.4448** | EMPEROR, PIGLET, DUCKLING, CALF                                   | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 4: **0.4331** | PORKY, COLONEL, WOULD, BABE                                       | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
   - Group 5: **0.4814** | EMPEROR, PRINCESS, CHALK, NAPOLEON                                | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 6: **0.4369** | PIGLET, DUCKLING, CALF, MERMAID                                   | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 7: **0.5103** | DUCKLING, CHALK, NAPOLEON, MERMAID                                | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 8: **0.4110** | EMPEROR, PRINCESS, PIGLET, CALF                                   | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 9: **0.4593** | PORKY, PIGLET, DUCKLING, CALF                                     | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
   - Group 10: **0.4101** | COLONEL, WOULD, BABE, MERMAID                                     | INCORRECT (Max overlap: 2/4 with SILENT "L")
   - Group 11: **0.4652** | PRINCESS, COLONEL, CHALK, MERMAID                                 | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES) | [Pred Type: NAMED_ENTITY_SET (45.6%, no-rel 25.2%)]
   - Group 12: **0.4236** | PORKY, WOULD, NAPOLEON, BABE                                      | INCORRECT (Max overlap: 3/4 with FICTIONAL PIGS)
   - Group 13: **0.4591** | PIGLET, DUCKLING, CALF, BABE                                      | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
   - Group 14: **0.4521** | EMPEROR, PRINCESS, CHALK, MERMAID                                 | INCORRECT (Max overlap: 3/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 15: **0.4208** | PORKY, COLONEL, WOULD, NAPOLEON                                   | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
   - Group 16: **0.4562** | PRINCESS, CHALK, BABE, MERMAID                                    | INCORRECT (Max overlap: 2/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 17: **0.4251** | PIGLET, DUCKLING, NAPOLEON, CALF                                  | INCORRECT (Max overlap: 2/4 with FICTIONAL PIGS)
   - Group 18: **0.4347** | PIGLET, DUCKLING, COLONEL, CALF                                   | INCORRECT (Max overlap: 2/4 with SILENT "L")
   - Group 19: **0.4740** | PRINCESS, DUCKLING, CHALK, MERMAID                                | INCORRECT (Max overlap: 3/4 with HANS CHRISTIAN ANDERSON FIGURES)
   - Group 20: **0.4179** | EMPEROR, PIGLET, COLONEL, CALF                                    | INCORRECT (Max overlap: 2/4 with SILENT "L")

---

## Puzzle 32 (ID: 247)
**Words on Board:** SNACK, DAIRY, MOZZARELLA, JAWBREAKER, GOAD, PRODUCE, URGE, SPUR, BANANAS, FROZEN, FIGURE, ORANGE, STEADY, EGG, MEATBALL, FISH

### Ground Truth Categories:
* **Level 0 (ENCOURAGE, WITH "ON") [Type: COMMON_PHRASE]:** EGG, GOAD, SPUR, URGE
* **Level 1 (SPHERICAL FOODS) [Type: SEMANTIC_SET]:** JAWBREAKER, MEATBALL, MOZZARELLA, ORANGE
* **Level 2 (GROCERY STORE AISLES) [Type: SEMANTIC_SET]:** DAIRY, FROZEN, PRODUCE, SNACK
* **Level 3 (GO ___) [Type: FILL_IN_THE_BLANK]:** BANANAS, FIGURE, FISH, STEADY

### Top Candidate Partitions:
1. **Partition Score: 0.4583**
   - Group 1: **0.4964** | DAIRY, MOZZARELLA, BANANAS, MEATBALL                              | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 34.0%)]
   - Group 2: **0.4952** | JAWBREAKER, FROZEN, FIGURE, STEADY                                | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 3: **0.4770** | SNACK, GOAD, URGE, SPUR                                           | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON") | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 32.2%)]
   - Group 4: **0.4304** | PRODUCE, ORANGE, EGG, FISH                                        | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
2. **Partition Score: 0.4570**
   - Group 1: **0.4952** | JAWBREAKER, FROZEN, FIGURE, STEADY                                | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 2: **0.4858** | DAIRY, PRODUCE, EGG, FISH                                         | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 3: **0.4770** | SNACK, GOAD, URGE, SPUR                                           | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON") | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 32.2%)]
   - Group 4: **0.4325** | MOZZARELLA, BANANAS, ORANGE, MEATBALL                             | INCORRECT (Max overlap: 3/4 with SPHERICAL FOODS)
3. **Partition Score: 0.4534**
   - Group 1: **0.4952** | JAWBREAKER, FROZEN, FIGURE, STEADY                                | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 2: **0.4770** | SNACK, GOAD, URGE, SPUR                                           | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON") | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 32.2%)]
   - Group 3: **0.4633** | PRODUCE, BANANAS, EGG, FISH                                       | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 4: **0.4367** | DAIRY, MOZZARELLA, ORANGE, MEATBALL                               | INCORRECT (Max overlap: 3/4 with SPHERICAL FOODS)
4. **Partition Score: 0.4521**
   - Group 1: **0.4808** | DAIRY, ORANGE, EGG, FISH                                          | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
   - Group 2: **0.4770** | SNACK, GOAD, URGE, SPUR                                           | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON") | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 32.2%)]
   - Group 3: **0.4549** | PRODUCE, FROZEN, FIGURE, STEADY                                   | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 4: **0.4382** | MOZZARELLA, JAWBREAKER, BANANAS, MEATBALL                         | INCORRECT (Max overlap: 3/4 with SPHERICAL FOODS)
5. **Partition Score: 0.4506**
   - Group 1: **0.4726** | GOAD, URGE, SPUR, STEADY                                          | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON") | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 28.9%)]
   - Group 2: **0.4635** | SNACK, DAIRY, ORANGE, EGG                                         | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES) | [Pred Type: FILL_IN_THE_BLANK (47.5%, no-rel 17.8%)]
   - Group 3: **0.4624** | PRODUCE, FROZEN, FIGURE, FISH                                     | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 4: **0.4382** | MOZZARELLA, JAWBREAKER, BANANAS, MEATBALL                         | INCORRECT (Max overlap: 3/4 with SPHERICAL FOODS)

### Top Candidate Groups:
   - Group 1: **0.4964** | DAIRY, MOZZARELLA, BANANAS, MEATBALL                              | INCORRECT (Max overlap: 2/4 with SPHERICAL FOODS) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 34.0%)]
   - Group 2: **0.4952** | JAWBREAKER, FROZEN, FIGURE, STEADY                                | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 3: **0.4770** | SNACK, GOAD, URGE, SPUR                                           | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON") | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 32.2%)]
   - Group 4: **0.4304** | PRODUCE, ORANGE, EGG, FISH                                        | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
   - Group 5: **0.4858** | DAIRY, PRODUCE, EGG, FISH                                         | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 6: **0.4325** | MOZZARELLA, BANANAS, ORANGE, MEATBALL                             | INCORRECT (Max overlap: 3/4 with SPHERICAL FOODS)
   - Group 7: **0.4633** | PRODUCE, BANANAS, EGG, FISH                                       | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 8: **0.4367** | DAIRY, MOZZARELLA, ORANGE, MEATBALL                               | INCORRECT (Max overlap: 3/4 with SPHERICAL FOODS)
   - Group 9: **0.4808** | DAIRY, ORANGE, EGG, FISH                                          | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)
   - Group 10: **0.4549** | PRODUCE, FROZEN, FIGURE, STEADY                                   | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 11: **0.4382** | MOZZARELLA, JAWBREAKER, BANANAS, MEATBALL                         | INCORRECT (Max overlap: 3/4 with SPHERICAL FOODS)
   - Group 12: **0.4726** | GOAD, URGE, SPUR, STEADY                                          | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON") | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 28.9%)]
   - Group 13: **0.4635** | SNACK, DAIRY, ORANGE, EGG                                         | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES) | [Pred Type: FILL_IN_THE_BLANK (47.5%, no-rel 17.8%)]
   - Group 14: **0.4624** | PRODUCE, FROZEN, FIGURE, FISH                                     | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 15: **0.5057** | PRODUCE, FIGURE, EGG, FISH                                        | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 16: **0.4592** | DAIRY, JAWBREAKER, FROZEN, STEADY                                 | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 17: **0.4832** | SNACK, JAWBREAKER, FROZEN, STEADY                                 | INCORRECT (Max overlap: 2/4 with GROCERY STORE AISLES)
   - Group 18: **0.4506** | GOAD, URGE, SPUR, FIGURE                                          | INCORRECT (Max overlap: 3/4 with ENCOURAGE, WITH "ON") | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 29.8%)]
   - Group 19: **0.4618** | SNACK, JAWBREAKER, FIGURE, STEADY                                 | INCORRECT (Max overlap: 2/4 with GO ___)
   - Group 20: **0.4562** | FROZEN, ORANGE, EGG, FISH                                         | INCORRECT (Max overlap: 1/4 with GROCERY STORE AISLES)

---

## Puzzle 33 (ID: 60)
**Words on Board:** ANKLET, CHARM, PLEASE, TICKLE, RING, FIELD, PURGE, DIAMOND, BANGLE, RINK, SCREAM, BROOCH, SAW, PENDANT, COURT, DELIGHT

### Ground Truth Categories:
* **Level 0 (HORROR FRANCHISES) [Type: NAMED_ENTITY_SET]:** PURGE, RING, SAW, SCREAM
* **Level 1 (SPORTS VENUES) [Type: SEMANTIC_SET]:** COURT, DIAMOND, FIELD, RINK
* **Level 2 (MAKE HAPPY) [Type: SYNONYM_OR_NEAR]:** CHARM, DELIGHT, PLEASE, TICKLE
* **Level 3 (JEWELRY) [Type: SEMANTIC_SET]:** ANKLET, BANGLE, BROOCH, PENDANT

### Top Candidate Partitions:
1. **Partition Score: 0.3879**
   - Group 1: **0.5228** | TICKLE, PURGE, SCREAM, SAW                                        | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 2: **0.4446** | RING, FIELD, DIAMOND, COURT                                       | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 3: **0.4228** | CHARM, PLEASE, PENDANT, DELIGHT                                   | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 24.2%)]
   - Group 4: **0.3421** | ANKLET, BANGLE, RINK, BROOCH                                      | INCORRECT (Max overlap: 3/4 with JEWELRY)
2. **Partition Score: 0.3860**
   - Group 1: **0.4605** | PLEASE, TICKLE, PURGE, DELIGHT                                    | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 2: **0.4595** | ANKLET, CHARM, BANGLE, PENDANT                                    | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 3: **0.3723** | RING, FIELD, DIAMOND, BROOCH                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 4: **0.3561** | RINK, SCREAM, SAW, COURT                                          | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
3. **Partition Score: 0.3798**
   - Group 1: **0.4493** | ANKLET, TICKLE, BROOCH, PENDANT                                   | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 2: **0.4299** | CHARM, PLEASE, PURGE, DELIGHT                                     | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 33.3%)]
   - Group 3: **0.3771** | RING, FIELD, DIAMOND, BANGLE                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 4: **0.3561** | RINK, SCREAM, SAW, COURT                                          | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
4. **Partition Score: 0.3797**
   - Group 1: **0.4446** | RING, FIELD, DIAMOND, COURT                                       | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 2: **0.4342** | CHARM, TICKLE, PENDANT, DELIGHT                                   | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 3: **0.4002** | PLEASE, PURGE, SCREAM, SAW                                        | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 4: **0.3421** | ANKLET, BANGLE, RINK, BROOCH                                      | INCORRECT (Max overlap: 3/4 with JEWELRY)
5. **Partition Score: 0.3796**
   - Group 1: **0.5228** | TICKLE, PURGE, SCREAM, SAW                                        | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 2: **0.4228** | CHARM, PLEASE, PENDANT, DELIGHT                                   | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 24.2%)]
   - Group 3: **0.3742** | RING, BANGLE, RINK, BROOCH                                        | INCORRECT (Max overlap: 2/4 with JEWELRY)
   - Group 4: **0.3607** | ANKLET, FIELD, DIAMOND, COURT                                     | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)

### Top Candidate Groups:
   - Group 1: **0.5228** | TICKLE, PURGE, SCREAM, SAW                                        | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 2: **0.4446** | RING, FIELD, DIAMOND, COURT                                       | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 3: **0.4228** | CHARM, PLEASE, PENDANT, DELIGHT                                   | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (65.0%, no-rel 24.2%)]
   - Group 4: **0.3421** | ANKLET, BANGLE, RINK, BROOCH                                      | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 5: **0.4605** | PLEASE, TICKLE, PURGE, DELIGHT                                    | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 6: **0.4595** | ANKLET, CHARM, BANGLE, PENDANT                                    | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 7: **0.3723** | RING, FIELD, DIAMOND, BROOCH                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 8: **0.3561** | RINK, SCREAM, SAW, COURT                                          | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 9: **0.4493** | ANKLET, TICKLE, BROOCH, PENDANT                                   | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 10: **0.4299** | CHARM, PLEASE, PURGE, DELIGHT                                     | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 33.3%)]
   - Group 11: **0.3771** | RING, FIELD, DIAMOND, BANGLE                                      | INCORRECT (Max overlap: 2/4 with SPORTS VENUES)
   - Group 12: **0.4342** | CHARM, TICKLE, PENDANT, DELIGHT                                   | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 13: **0.4002** | PLEASE, PURGE, SCREAM, SAW                                        | INCORRECT (Max overlap: 3/4 with HORROR FRANCHISES)
   - Group 14: **0.3742** | RING, BANGLE, RINK, BROOCH                                        | INCORRECT (Max overlap: 2/4 with JEWELRY)
   - Group 15: **0.3607** | ANKLET, FIELD, DIAMOND, COURT                                     | INCORRECT (Max overlap: 3/4 with SPORTS VENUES)
   - Group 16: **0.4243** | CHARM, TICKLE, BANGLE, DELIGHT                                    | INCORRECT (Max overlap: 3/4 with MAKE HAPPY)
   - Group 17: **0.3462** | ANKLET, RINK, BROOCH, PENDANT                                     | INCORRECT (Max overlap: 3/4 with JEWELRY) | [Pred Type: SEMANTIC_SET (45.0%, no-rel 23.5%)]
   - Group 18: **0.3783** | CHARM, PLEASE, BANGLE, DELIGHT                                    | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (60.5%, no-rel 28.2%)]
   - Group 19: **0.4253** | ANKLET, CHARM, BROOCH, PENDANT                                    | INCORRECT (Max overlap: 3/4 with JEWELRY)
   - Group 20: **0.4952** | ANKLET, TICKLE, BANGLE, PENDANT                                   | INCORRECT (Max overlap: 3/4 with JEWELRY)

---

## Puzzle 34 (ID: 246)
**Words on Board:** LAG, PARROT, APOLLO, CANDLES, DROP, MIME, MONKEY, FANTASTIC, FREEZE, SAILOR, SAMURAI, PRISONER, PRINCESS, REFEREE, GENIE, ECHO

### Ground Truth Categories:
* **Level 0 (BAD THINGS FOR A VIDEO CALL TO DO) [Type: SEMANTIC_SET]:** DROP, ECHO, FREEZE, LAG
* **Level 1 (COSTUMES WITH STRIPED SHIRTS) [Type: SEMANTIC_SET]:** MIME, PRISONER, REFEREE, SAILOR
* **Level 2 (SEEN IN “ALADDIN”) [Type: SEMANTIC_SET]:** GENIE, MONKEY, PARROT, PRINCESS
* **Level 3 (MOVIES MINUS NUMBERS) [Type: WORDPLAY_TRANSFORM]:** APOLLO, CANDLES, FANTASTIC, SAMURAI

### Top Candidate Partitions:
1. **Partition Score: 0.4682**
   - Group 1: **0.5069** | PARROT, MONKEY, SAILOR, ECHO                                      | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 2: **0.4952** | APOLLO, CANDLES, PRINCESS, GENIE                                  | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS) | [Pred Type: NAMED_ENTITY_SET (45.3%, no-rel 24.7%)]
   - Group 3: **0.4949** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 4: **0.4413** | MIME, FANTASTIC, SAMURAI, PRISONER                                | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
2. **Partition Score: 0.4624**
   - Group 1: **0.4952** | APOLLO, CANDLES, PRINCESS, GENIE                                  | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS) | [Pred Type: NAMED_ENTITY_SET (45.3%, no-rel 24.7%)]
   - Group 2: **0.4949** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 3: **0.4816** | MIME, MONKEY, FANTASTIC, ECHO                                     | INCORRECT (Max overlap: 1/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 4: **0.4365** | PARROT, SAILOR, SAMURAI, PRISONER                                 | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
3. **Partition Score: 0.4592**
   - Group 1: **0.4984** | APOLLO, CANDLES, GENIE, ECHO                                      | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS) | [Pred Type: NAMED_ENTITY_SET (51.0%, no-rel 15.2%)]
   - Group 2: **0.4949** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 3: **0.4591** | PARROT, MONKEY, SAILOR, PRINCESS                                  | INCORRECT (Max overlap: 3/4 with SEEN IN “ALADDIN”)
   - Group 4: **0.4413** | MIME, FANTASTIC, SAMURAI, PRISONER                                | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
4. **Partition Score: 0.4554**
   - Group 1: **0.4949** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 2: **0.4870** | PARROT, CANDLES, MONKEY, ECHO                                     | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 3: **0.4519** | APOLLO, SAILOR, PRINCESS, GENIE                                   | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”) | [Pred Type: NAMED_ENTITY_SET (57.9%, no-rel 9.5%)]
   - Group 4: **0.4413** | MIME, FANTASTIC, SAMURAI, PRISONER                                | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
5. **Partition Score: 0.4544**
   - Group 1: **0.4952** | APOLLO, CANDLES, PRINCESS, GENIE                                  | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS) | [Pred Type: NAMED_ENTITY_SET (45.3%, no-rel 24.7%)]
   - Group 2: **0.4949** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 3: **0.4603** | MIME, FANTASTIC, SAMURAI, ECHO                                    | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 4: **0.4312** | PARROT, MONKEY, SAILOR, PRISONER                                  | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)

### Top Candidate Groups:
   - Group 1: **0.5069** | PARROT, MONKEY, SAILOR, ECHO                                      | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 2: **0.4952** | APOLLO, CANDLES, PRINCESS, GENIE                                  | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS) | [Pred Type: NAMED_ENTITY_SET (45.3%, no-rel 24.7%)]
   - Group 3: **0.4949** | LAG, DROP, FREEZE, REFEREE                                        | INCORRECT (Max overlap: 3/4 with BAD THINGS FOR A VIDEO CALL TO DO)
   - Group 4: **0.4413** | MIME, FANTASTIC, SAMURAI, PRISONER                                | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 5: **0.4816** | MIME, MONKEY, FANTASTIC, ECHO                                     | INCORRECT (Max overlap: 1/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 6: **0.4365** | PARROT, SAILOR, SAMURAI, PRISONER                                 | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 7: **0.4984** | APOLLO, CANDLES, GENIE, ECHO                                      | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS) | [Pred Type: NAMED_ENTITY_SET (51.0%, no-rel 15.2%)]
   - Group 8: **0.4591** | PARROT, MONKEY, SAILOR, PRINCESS                                  | INCORRECT (Max overlap: 3/4 with SEEN IN “ALADDIN”)
   - Group 9: **0.4870** | PARROT, CANDLES, MONKEY, ECHO                                     | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 10: **0.4519** | APOLLO, SAILOR, PRINCESS, GENIE                                   | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”) | [Pred Type: NAMED_ENTITY_SET (57.9%, no-rel 9.5%)]
   - Group 11: **0.4603** | MIME, FANTASTIC, SAMURAI, ECHO                                    | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS)
   - Group 12: **0.4312** | PARROT, MONKEY, SAILOR, PRISONER                                  | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”)
   - Group 13: **0.4679** | PARROT, SAILOR, PRINCESS, GENIE                                   | INCORRECT (Max overlap: 3/4 with SEEN IN “ALADDIN”) | [Pred Type: NAMED_ENTITY_SET (54.0%, no-rel 9.8%)]
   - Group 14: **0.4647** | APOLLO, CANDLES, MONKEY, ECHO                                     | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS) | [Pred Type: NAMED_ENTITY_SET (46.0%, no-rel 11.9%)]
   - Group 15: **0.4756** | APOLLO, CANDLES, SAILOR, PRINCESS                                 | INCORRECT (Max overlap: 2/4 with MOVIES MINUS NUMBERS) | [Pred Type: NAMED_ENTITY_SET (51.2%, no-rel 10.3%)]
   - Group 16: **0.4533** | PARROT, MONKEY, GENIE, ECHO                                       | INCORRECT (Max overlap: 3/4 with SEEN IN “ALADDIN”) | [Pred Type: NAMED_ENTITY_SET (55.9%, no-rel 11.6%)]
   - Group 17: **0.4667** | PARROT, APOLLO, MONKEY, ECHO                                      | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”) | [Pred Type: NAMED_ENTITY_SET (51.9%, no-rel 14.9%)]
   - Group 18: **0.4617** | CANDLES, SAILOR, PRINCESS, GENIE                                  | INCORRECT (Max overlap: 2/4 with SEEN IN “ALADDIN”) | [Pred Type: NAMED_ENTITY_SET (47.2%, no-rel 10.6%)]
   - Group 19: **0.4534** | MONKEY, SAILOR, SAMURAI, PRISONER                                 | INCORRECT (Max overlap: 2/4 with COSTUMES WITH STRIPED SHIRTS)
   - Group 20: **0.4292** | PARROT, MIME, FANTASTIC, ECHO                                     | INCORRECT (Max overlap: 1/4 with SEEN IN “ALADDIN”)

---

## Puzzle 35 (ID: 315)
**Words on Board:** CYMBAL, SYMBOL, CAR, WIG, MODEL, SIMMER, TRACK, IDEAL, WAX, SCIMITAR, DRUM, EXAMPLE, CONDUCTOR, STATION, SYMPHONY, MARK

### Ground Truth Categories:
* **Level 0 (EMBODIMENT) [Type: SYNONYM_OR_NEAR]:** EXAMPLE, IDEAL, MODEL, SYMBOL
* **Level 1 (RELATED TO TRAINS) [Type: SEMANTIC_SET]:** CAR, CONDUCTOR, STATION, TRACK
* **Level 2 (STARTING WITH THE SAME SOUND) [Type: SOUND_OR_SPELLING]:** CYMBAL, SCIMITAR, SIMMER, SYMPHONY
* **Level 3 (EAR___) [Type: FILL_IN_THE_BLANK]:** DRUM, MARK, WAX, WIG

### Top Candidate Partitions:
1. **Partition Score: 0.4417**
   - Group 1: **0.6825** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 40.8%)]
   - Group 2: **0.4766** | SYMBOL, SIMMER, SCIMITAR, SYMPHONY                                | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 3: **0.4568** | CYMBAL, WIG, DRUM, CONDUCTOR                                      | INCORRECT (Max overlap: 2/4 with EAR___) | [Pred Type: SEMANTIC_SET (57.0%, no-rel 22.5%)]
   - Group 4: **0.4167** | CAR, TRACK, WAX, STATION                                          | INCORRECT (Max overlap: 3/4 with RELATED TO TRAINS) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 31.1%)]
2. **Partition Score: 0.4237**
   - Group 1: **0.6825** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 40.8%)]
   - Group 2: **0.5543** | CYMBAL, DRUM, CONDUCTOR, SYMPHONY                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 26.3%)]
   - Group 3: **0.4107** | SYMBOL, SIMMER, SCIMITAR, STATION                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 4: **0.3649** | CAR, WIG, TRACK, WAX                                              | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
3. **Partition Score: 0.4217**
   - Group 1: **0.4326** | CAR, MODEL, IDEAL, EXAMPLE                                        | INCORRECT (Max overlap: 3/4 with EMBODIMENT) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 31.0%)]
   - Group 2: **0.4264** | CYMBAL, WIG, SCIMITAR, SYMPHONY                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 3: **0.4256** | SYMBOL, SIMMER, WAX, MARK                                         | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 4: **0.4173** | TRACK, DRUM, CONDUCTOR, STATION                                   | INCORRECT (Max overlap: 3/4 with RELATED TO TRAINS) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 32.2%)]
4. **Partition Score: 0.4206**
   - Group 1: **0.6825** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 40.8%)]
   - Group 2: **0.5543** | CYMBAL, DRUM, CONDUCTOR, SYMPHONY                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 26.3%)]
   - Group 3: **0.4167** | CAR, TRACK, WAX, STATION                                          | INCORRECT (Max overlap: 3/4 with RELATED TO TRAINS) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 31.1%)]
   - Group 4: **0.3556** | SYMBOL, WIG, SIMMER, SCIMITAR                                     | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
5. **Partition Score: 0.4159**
   - Group 1: **0.5177** | CYMBAL, SCIMITAR, STATION, SYMPHONY                               | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 2: **0.4326** | CAR, MODEL, IDEAL, EXAMPLE                                        | INCORRECT (Max overlap: 3/4 with EMBODIMENT) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 31.0%)]
   - Group 3: **0.4256** | SYMBOL, SIMMER, WAX, MARK                                         | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 4: **0.4027** | WIG, TRACK, DRUM, CONDUCTOR                                       | INCORRECT (Max overlap: 2/4 with EAR___) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 28.7%)]

### Top Candidate Groups:
   - Group 1: **0.6825** | MODEL, IDEAL, EXAMPLE, MARK                                       | INCORRECT (Max overlap: 3/4 with EMBODIMENT) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 40.8%)]
   - Group 2: **0.4766** | SYMBOL, SIMMER, SCIMITAR, SYMPHONY                                | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 3: **0.4568** | CYMBAL, WIG, DRUM, CONDUCTOR                                      | INCORRECT (Max overlap: 2/4 with EAR___) | [Pred Type: SEMANTIC_SET (57.0%, no-rel 22.5%)]
   - Group 4: **0.4167** | CAR, TRACK, WAX, STATION                                          | INCORRECT (Max overlap: 3/4 with RELATED TO TRAINS) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 31.1%)]
   - Group 5: **0.5543** | CYMBAL, DRUM, CONDUCTOR, SYMPHONY                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 26.3%)]
   - Group 6: **0.4107** | SYMBOL, SIMMER, SCIMITAR, STATION                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 7: **0.3649** | CAR, WIG, TRACK, WAX                                              | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
   - Group 8: **0.4326** | CAR, MODEL, IDEAL, EXAMPLE                                        | INCORRECT (Max overlap: 3/4 with EMBODIMENT) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 31.0%)]
   - Group 9: **0.4264** | CYMBAL, WIG, SCIMITAR, SYMPHONY                                   | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 10: **0.4256** | SYMBOL, SIMMER, WAX, MARK                                         | INCORRECT (Max overlap: 2/4 with EAR___)
   - Group 11: **0.4173** | TRACK, DRUM, CONDUCTOR, STATION                                   | INCORRECT (Max overlap: 3/4 with RELATED TO TRAINS) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 32.2%)]
   - Group 12: **0.3556** | SYMBOL, WIG, SIMMER, SCIMITAR                                     | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 13: **0.5177** | CYMBAL, SCIMITAR, STATION, SYMPHONY                               | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND)
   - Group 14: **0.4027** | WIG, TRACK, DRUM, CONDUCTOR                                       | INCORRECT (Max overlap: 2/4 with EAR___) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 28.7%)]
   - Group 15: **0.5907** | MODEL, SIMMER, IDEAL, EXAMPLE                                     | INCORRECT (Max overlap: 3/4 with EMBODIMENT) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 34.9%)]
   - Group 16: **0.5178** | SYMBOL, SCIMITAR, STATION, SYMPHONY                               | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND)
   - Group 17: **0.3438** | CAR, TRACK, WAX, MARK                                             | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
   - Group 18: **0.3970** | TRACK, SCIMITAR, STATION, SYMPHONY                                | INCORRECT (Max overlap: 2/4 with RELATED TO TRAINS)
   - Group 19: **0.4095** | SYMBOL, WIG, SCIMITAR, STATION                                    | INCORRECT (Max overlap: 1/4 with EMBODIMENT)
   - Group 20: **0.4851** | CYMBAL, SCIMITAR, DRUM, CONDUCTOR                                 | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND) | [Pred Type: SEMANTIC_SET (45.4%, no-rel 26.7%)]

---

## Puzzle 36 (ID: 828)
**Words on Board:** DONUT, SQUID, FOLLOW, ROSE, ROGER, WHITE, TRIX, PEN, JUROR, VELVETEEN, PRINTER, WATCH, MONITOR, TATTOO MACHINE, TRACK, MONTH

### Ground Truth Categories:
* **Level 0 (KEEP TABS ON) [Type: SYNONYM_OR_NEAR]:** FOLLOW, MONITOR, TRACK, WATCH
* **Level 1 (ONE IN A DOZEN) [Type: SEMANTIC_SET]:** DONUT, JUROR, MONTH, ROSE
* **Level 2 (THINGS WITH INK) [Type: SEMANTIC_SET]:** PEN, PRINTER, SQUID, TATTOO MACHINE
* **Level 3 (___ RABBIT) [Type: FILL_IN_THE_BLANK]:** ROGER, TRIX, VELVETEEN, WHITE

### Top Candidate Partitions:
1. **Partition Score: 0.4809**
   - Group 1: **0.8156** | FOLLOW, WATCH, MONITOR, TRACK                                     | CORRECT GROUP (KEEP TABS ON, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 41.2%)]
   - Group 2: **0.5276** | SQUID, VELVETEEN, PRINTER, TATTOO MACHINE                         | INCORRECT (Max overlap: 3/4 with THINGS WITH INK)
   - Group 3: **0.4708** | ROGER, TRIX, JUROR, MONTH                                         | INCORRECT (Max overlap: 2/4 with ___ RABBIT)
   - Group 4: **0.4626** | DONUT, ROSE, WHITE, PEN                                           | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN) | [Pred Type: FILL_IN_THE_BLANK (65.2%, no-rel 7.5%)]
2. **Partition Score: 0.4778**
   - Group 1: **0.8156** | FOLLOW, WATCH, MONITOR, TRACK                                     | CORRECT GROUP (KEEP TABS ON, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 41.2%)]
   - Group 2: **0.5443** | SQUID, PEN, PRINTER, TATTOO MACHINE                               | CORRECT GROUP (THINGS WITH INK, Level 2) | [Pred Type: SEMANTIC_SET (48.5%, no-rel 20.4%)]
   - Group 3: **0.4874** | ROGER, TRIX, JUROR, VELVETEEN                                     | INCORRECT (Max overlap: 3/4 with ___ RABBIT)
   - Group 4: **0.4397** | DONUT, ROSE, WHITE, MONTH                                         | INCORRECT (Max overlap: 3/4 with ONE IN A DOZEN)
3. **Partition Score: 0.4746**
   - Group 1: **0.8156** | FOLLOW, WATCH, MONITOR, TRACK                                     | CORRECT GROUP (KEEP TABS ON, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 41.2%)]
   - Group 2: **0.5443** | SQUID, PEN, PRINTER, TATTOO MACHINE                               | CORRECT GROUP (THINGS WITH INK, Level 2) | [Pred Type: SEMANTIC_SET (48.5%, no-rel 20.4%)]
   - Group 3: **0.5420** | DONUT, ROGER, TRIX, VELVETEEN                                     | INCORRECT (Max overlap: 3/4 with ___ RABBIT)
   - Group 4: **0.4061** | ROSE, WHITE, JUROR, MONTH                                         | INCORRECT (Max overlap: 3/4 with ONE IN A DOZEN) | [Pred Type: FILL_IN_THE_BLANK (50.1%, no-rel 7.8%)]
4. **Partition Score: 0.4694**
   - Group 1: **0.8156** | FOLLOW, WATCH, MONITOR, TRACK                                     | CORRECT GROUP (KEEP TABS ON, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 41.2%)]
   - Group 2: **0.5276** | SQUID, VELVETEEN, PRINTER, TATTOO MACHINE                         | INCORRECT (Max overlap: 3/4 with THINGS WITH INK)
   - Group 3: **0.5148** | DONUT, ROGER, TRIX, JUROR                                         | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN)
   - Group 4: **0.4176** | ROSE, WHITE, PEN, MONTH                                           | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN) | [Pred Type: FILL_IN_THE_BLANK (76.2%, no-rel 6.8%)]
5. **Partition Score: 0.4662**
   - Group 1: **0.8156** | FOLLOW, WATCH, MONITOR, TRACK                                     | CORRECT GROUP (KEEP TABS ON, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 41.2%)]
   - Group 2: **0.5567** | DONUT, SQUID, PEN, PRINTER                                        | INCORRECT (Max overlap: 3/4 with THINGS WITH INK)
   - Group 3: **0.4960** | ROGER, TRIX, VELVETEEN, TATTOO MACHINE                            | INCORRECT (Max overlap: 3/4 with ___ RABBIT)
   - Group 4: **0.4061** | ROSE, WHITE, JUROR, MONTH                                         | INCORRECT (Max overlap: 3/4 with ONE IN A DOZEN) | [Pred Type: FILL_IN_THE_BLANK (50.1%, no-rel 7.8%)]

### Top Candidate Groups:
   - Group 1: **0.8156** | FOLLOW, WATCH, MONITOR, TRACK                                     | CORRECT GROUP (KEEP TABS ON, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 41.2%)]
   - Group 2: **0.5276** | SQUID, VELVETEEN, PRINTER, TATTOO MACHINE                         | INCORRECT (Max overlap: 3/4 with THINGS WITH INK)
   - Group 3: **0.4708** | ROGER, TRIX, JUROR, MONTH                                         | INCORRECT (Max overlap: 2/4 with ___ RABBIT)
   - Group 4: **0.4626** | DONUT, ROSE, WHITE, PEN                                           | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN) | [Pred Type: FILL_IN_THE_BLANK (65.2%, no-rel 7.5%)]
   - Group 5: **0.5443** | SQUID, PEN, PRINTER, TATTOO MACHINE                               | CORRECT GROUP (THINGS WITH INK, Level 2) | [Pred Type: SEMANTIC_SET (48.5%, no-rel 20.4%)]
   - Group 6: **0.4874** | ROGER, TRIX, JUROR, VELVETEEN                                     | INCORRECT (Max overlap: 3/4 with ___ RABBIT)
   - Group 7: **0.4397** | DONUT, ROSE, WHITE, MONTH                                         | INCORRECT (Max overlap: 3/4 with ONE IN A DOZEN)
   - Group 8: **0.5420** | DONUT, ROGER, TRIX, VELVETEEN                                     | INCORRECT (Max overlap: 3/4 with ___ RABBIT)
   - Group 9: **0.4061** | ROSE, WHITE, JUROR, MONTH                                         | INCORRECT (Max overlap: 3/4 with ONE IN A DOZEN) | [Pred Type: FILL_IN_THE_BLANK (50.1%, no-rel 7.8%)]
   - Group 10: **0.5148** | DONUT, ROGER, TRIX, JUROR                                         | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN)
   - Group 11: **0.4176** | ROSE, WHITE, PEN, MONTH                                           | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN) | [Pred Type: FILL_IN_THE_BLANK (76.2%, no-rel 6.8%)]
   - Group 12: **0.5567** | DONUT, SQUID, PEN, PRINTER                                        | INCORRECT (Max overlap: 3/4 with THINGS WITH INK)
   - Group 13: **0.4960** | ROGER, TRIX, VELVETEEN, TATTOO MACHINE                            | INCORRECT (Max overlap: 3/4 with ___ RABBIT)
   - Group 14: **0.5305** | DONUT, ROGER, JUROR, VELVETEEN                                    | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN)
   - Group 15: **0.4968** | SQUID, TRIX, PRINTER, TATTOO MACHINE                              | INCORRECT (Max overlap: 3/4 with THINGS WITH INK)
   - Group 16: **0.5327** | DONUT, SQUID, PRINTER, TATTOO MACHINE                             | INCORRECT (Max overlap: 3/4 with THINGS WITH INK)
   - Group 17: **0.4935** | DONUT, ROGER, TRIX, MONTH                                         | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN)
   - Group 18: **0.4129** | ROSE, WHITE, PEN, JUROR                                           | INCORRECT (Max overlap: 2/4 with ONE IN A DOZEN) | [Pred Type: FILL_IN_THE_BLANK (71.7%, no-rel 6.8%)]
   - Group 19: **0.4409** | ROGER, JUROR, VELVETEEN, MONTH                                    | INCORRECT (Max overlap: 2/4 with ___ RABBIT)
   - Group 20: **0.5161** | SQUID, TRIX, VELVETEEN, TATTOO MACHINE                            | INCORRECT (Max overlap: 2/4 with THINGS WITH INK)

---

## Puzzle 37 (ID: 853)
**Words on Board:** TOM, ALLEY, WEAR, SPORT, TACKLE, GEAR, COURT, STUFF, KIT, LANE, PUT ON, WAY, PAT, BOB, DON, BILL

### Ground Truth Categories:
* **Level 0 (EQUIPMENT) [Type: SYNONYM_OR_NEAR]:** GEAR, KIT, STUFF, TACKLE
* **Level 1 (DRESS IN) [Type: SYNONYM_OR_NEAR]:** DON, PUT ON, SPORT, WEAR
* **Level 2 (STREET SUFFIXES) [Type: FILL_IN_THE_BLANK]:** ALLEY, COURT, LANE, WAY
* **Level 3 (NICKNAMES THAT HAVE OTHER MEANINGS) [Type: NAMED_ENTITY_SET]:** BILL, BOB, PAT, TOM

### Top Candidate Partitions:
1. **Partition Score: 0.4658**
   - Group 1: **0.5622** | TACKLE, GEAR, KIT, PUT ON                                         | INCORRECT (Max overlap: 3/4 with EQUIPMENT) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 36.5%)]
   - Group 2: **0.5385** | WEAR, SPORT, COURT, STUFF                                         | INCORRECT (Max overlap: 2/4 with DRESS IN)
   - Group 3: **0.5214** | TOM, PAT, BOB, BILL                                               | CORRECT GROUP (NICKNAMES THAT HAVE OTHER MEANINGS, Level 3)
   - Group 4: **0.4016** | ALLEY, LANE, WAY, DON                                             | INCORRECT (Max overlap: 3/4 with STREET SUFFIXES) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 23.6%)]
2. **Partition Score: 0.4638**
   - Group 1: **0.5622** | TACKLE, GEAR, KIT, PUT ON                                         | INCORRECT (Max overlap: 3/4 with EQUIPMENT) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 36.5%)]
   - Group 2: **0.5506** | WEAR, SPORT, COURT, DON                                           | INCORRECT (Max overlap: 3/4 with DRESS IN) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 34.7%)]
   - Group 3: **0.5214** | TOM, PAT, BOB, BILL                                               | CORRECT GROUP (NICKNAMES THAT HAVE OTHER MEANINGS, Level 3)
   - Group 4: **0.3915** | ALLEY, STUFF, LANE, WAY                                           | INCORRECT (Max overlap: 3/4 with STREET SUFFIXES)
3. **Partition Score: 0.4621**
   - Group 1: **0.6247** | SPORT, TACKLE, GEAR, KIT                                          | INCORRECT (Max overlap: 3/4 with EQUIPMENT) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 37.5%)]
   - Group 2: **0.5438** | WEAR, COURT, PUT ON, DON                                          | INCORRECT (Max overlap: 3/4 with DRESS IN) | [Pred Type: SYNONYM_OR_NEAR (60.8%, no-rel 31.3%)]
   - Group 3: **0.5214** | TOM, PAT, BOB, BILL                                               | CORRECT GROUP (NICKNAMES THAT HAVE OTHER MEANINGS, Level 3)
   - Group 4: **0.3915** | ALLEY, STUFF, LANE, WAY                                           | INCORRECT (Max overlap: 3/4 with STREET SUFFIXES)
4. **Partition Score: 0.4544**
   - Group 1: **0.5214** | TOM, PAT, BOB, BILL                                               | CORRECT GROUP (NICKNAMES THAT HAVE OTHER MEANINGS, Level 3)
   - Group 2: **0.5193** | SPORT, GEAR, COURT, STUFF                                         | INCORRECT (Max overlap: 2/4 with EQUIPMENT)
   - Group 3: **0.4948** | WEAR, TACKLE, KIT, PUT ON                                         | INCORRECT (Max overlap: 2/4 with DRESS IN)
   - Group 4: **0.4016** | ALLEY, LANE, WAY, DON                                             | INCORRECT (Max overlap: 3/4 with STREET SUFFIXES) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 23.6%)]
5. **Partition Score: 0.4532**
   - Group 1: **0.6329** | TACKLE, GEAR, STUFF, KIT                                          | CORRECT GROUP (EQUIPMENT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.4%, no-rel 35.3%)]
   - Group 2: **0.5214** | TOM, PAT, BOB, BILL                                               | CORRECT GROUP (NICKNAMES THAT HAVE OTHER MEANINGS, Level 3)
   - Group 3: **0.4880** | WEAR, SPORT, COURT, PUT ON                                        | INCORRECT (Max overlap: 3/4 with DRESS IN)
   - Group 4: **0.4016** | ALLEY, LANE, WAY, DON                                             | INCORRECT (Max overlap: 3/4 with STREET SUFFIXES) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 23.6%)]

### Top Candidate Groups:
   - Group 1: **0.5622** | TACKLE, GEAR, KIT, PUT ON                                         | INCORRECT (Max overlap: 3/4 with EQUIPMENT) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 36.5%)]
   - Group 2: **0.5385** | WEAR, SPORT, COURT, STUFF                                         | INCORRECT (Max overlap: 2/4 with DRESS IN)
   - Group 3: **0.5214** | TOM, PAT, BOB, BILL                                               | CORRECT GROUP (NICKNAMES THAT HAVE OTHER MEANINGS, Level 3)
   - Group 4: **0.4016** | ALLEY, LANE, WAY, DON                                             | INCORRECT (Max overlap: 3/4 with STREET SUFFIXES) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 23.6%)]
   - Group 5: **0.5506** | WEAR, SPORT, COURT, DON                                           | INCORRECT (Max overlap: 3/4 with DRESS IN) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 34.7%)]
   - Group 6: **0.3915** | ALLEY, STUFF, LANE, WAY                                           | INCORRECT (Max overlap: 3/4 with STREET SUFFIXES)
   - Group 7: **0.6247** | SPORT, TACKLE, GEAR, KIT                                          | INCORRECT (Max overlap: 3/4 with EQUIPMENT) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 37.5%)]
   - Group 8: **0.5438** | WEAR, COURT, PUT ON, DON                                          | INCORRECT (Max overlap: 3/4 with DRESS IN) | [Pred Type: SYNONYM_OR_NEAR (60.8%, no-rel 31.3%)]
   - Group 9: **0.5193** | SPORT, GEAR, COURT, STUFF                                         | INCORRECT (Max overlap: 2/4 with EQUIPMENT)
   - Group 10: **0.4948** | WEAR, TACKLE, KIT, PUT ON                                         | INCORRECT (Max overlap: 2/4 with DRESS IN)
   - Group 11: **0.6329** | TACKLE, GEAR, STUFF, KIT                                          | CORRECT GROUP (EQUIPMENT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.4%, no-rel 35.3%)]
   - Group 12: **0.4880** | WEAR, SPORT, COURT, PUT ON                                        | INCORRECT (Max overlap: 3/4 with DRESS IN)
   - Group 13: **0.5172** | GEAR, STUFF, KIT, PUT ON                                          | INCORRECT (Max overlap: 3/4 with EQUIPMENT)
   - Group 14: **0.4896** | WEAR, SPORT, TACKLE, COURT                                        | INCORRECT (Max overlap: 2/4 with DRESS IN)
   - Group 15: **0.5523** | WEAR, SPORT, STUFF, PUT ON                                        | INCORRECT (Max overlap: 3/4 with DRESS IN)
   - Group 16: **0.4848** | TACKLE, GEAR, COURT, KIT                                          | INCORRECT (Max overlap: 3/4 with EQUIPMENT) | [Pred Type: SYNONYM_OR_NEAR (52.5%, no-rel 33.0%)]
   - Group 17: **0.5234** | WEAR, SPORT, GEAR, COURT                                          | INCORRECT (Max overlap: 2/4 with DRESS IN)
   - Group 18: **0.4773** | TACKLE, STUFF, KIT, PUT ON                                        | INCORRECT (Max overlap: 3/4 with EQUIPMENT)
   - Group 19: **0.4955** | TACKLE, KIT, PUT ON, DON                                          | INCORRECT (Max overlap: 2/4 with EQUIPMENT)
   - Group 20: **0.5276** | WEAR, GEAR, KIT, PUT ON                                           | INCORRECT (Max overlap: 2/4 with DRESS IN)

---

## Puzzle 38 (ID: 901)
**Words on Board:** CORE, BENCH, BUST, TRUNK, SPLIT, TREE, COVER, STAND, SUBSTITUTE, RELIEF, TORSO, PIGEON, MIDSECTION, BACKUP, STATUE, HIT

### Ground Truth Categories:
* **Level 0 (ABDOMINAL AREA) [Type: SYNONYM_OR_NEAR]:** CORE, MIDSECTION, TORSO, TRUNK
* **Level 1 (REPLACEMENT) [Type: SYNONYM_OR_NEAR]:** BACKUP, COVER, RELIEF, SUBSTITUTE
* **Level 2 (PARK STAPLES) [Type: SEMANTIC_SET]:** BENCH, PIGEON, STATUE, TREE
* **Level 3 (BLACKJACK TERMS) [Type: SEMANTIC_SET]:** BUST, HIT, SPLIT, STAND

### Top Candidate Partitions:
1. **Partition Score: 0.3882**
   - Group 1: **0.6409** | STAND, SUBSTITUTE, RELIEF, BACKUP                                 | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 30.4%)]
   - Group 2: **0.4703** | BUST, SPLIT, COVER, HIT                                           | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 3: **0.4023** | TRUNK, TORSO, MIDSECTION, STATUE                                  | INCORRECT (Max overlap: 3/4 with ABDOMINAL AREA) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 27.8%)]
   - Group 4: **0.3402** | CORE, BENCH, TREE, PIGEON                                         | INCORRECT (Max overlap: 3/4 with PARK STAPLES)
2. **Partition Score: 0.3728**
   - Group 1: **0.4316** | BUST, SPLIT, SUBSTITUTE, HIT                                      | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 2: **0.4084** | COVER, STAND, RELIEF, BACKUP                                      | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (49.2%, no-rel 34.7%)]
   - Group 3: **0.4023** | TRUNK, TORSO, MIDSECTION, STATUE                                  | INCORRECT (Max overlap: 3/4 with ABDOMINAL AREA) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 27.8%)]
   - Group 4: **0.3402** | CORE, BENCH, TREE, PIGEON                                         | INCORRECT (Max overlap: 3/4 with PARK STAPLES)
3. **Partition Score: 0.3700**
   - Group 1: **0.4085** | SUBSTITUTE, RELIEF, BACKUP, HIT                                   | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 33.0%)]
   - Group 2: **0.4023** | TRUNK, TORSO, MIDSECTION, STATUE                                  | INCORRECT (Max overlap: 3/4 with ABDOMINAL AREA) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 27.8%)]
   - Group 3: **0.3973** | BUST, SPLIT, COVER, STAND                                         | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 4: **0.3402** | CORE, BENCH, TREE, PIGEON                                         | INCORRECT (Max overlap: 3/4 with PARK STAPLES)
4. **Partition Score: 0.3670**
   - Group 1: **0.4765** | BUST, SUBSTITUTE, RELIEF, BACKUP                                  | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 35.6%)]
   - Group 2: **0.4023** | TRUNK, TORSO, MIDSECTION, STATUE                                  | INCORRECT (Max overlap: 3/4 with ABDOMINAL AREA) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 27.8%)]
   - Group 3: **0.3852** | SPLIT, COVER, STAND, HIT                                          | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 4: **0.3402** | CORE, BENCH, TREE, PIGEON                                         | INCORRECT (Max overlap: 3/4 with PARK STAPLES)
5. **Partition Score: 0.3669**
   - Group 1: **0.4292** | SPLIT, COVER, SUBSTITUTE, HIT                                     | INCORRECT (Max overlap: 2/4 with BLACKJACK TERMS)
   - Group 2: **0.4023** | TRUNK, TORSO, MIDSECTION, STATUE                                  | INCORRECT (Max overlap: 3/4 with ABDOMINAL AREA) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 27.8%)]
   - Group 3: **0.3847** | BUST, STAND, RELIEF, BACKUP                                       | INCORRECT (Max overlap: 2/4 with BLACKJACK TERMS) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 28.8%)]
   - Group 4: **0.3402** | CORE, BENCH, TREE, PIGEON                                         | INCORRECT (Max overlap: 3/4 with PARK STAPLES)

### Top Candidate Groups:
   - Group 1: **0.6409** | STAND, SUBSTITUTE, RELIEF, BACKUP                                 | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 30.4%)]
   - Group 2: **0.4703** | BUST, SPLIT, COVER, HIT                                           | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 3: **0.4023** | TRUNK, TORSO, MIDSECTION, STATUE                                  | INCORRECT (Max overlap: 3/4 with ABDOMINAL AREA) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 27.8%)]
   - Group 4: **0.3402** | CORE, BENCH, TREE, PIGEON                                         | INCORRECT (Max overlap: 3/4 with PARK STAPLES)
   - Group 5: **0.4316** | BUST, SPLIT, SUBSTITUTE, HIT                                      | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 6: **0.4084** | COVER, STAND, RELIEF, BACKUP                                      | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (49.2%, no-rel 34.7%)]
   - Group 7: **0.4085** | SUBSTITUTE, RELIEF, BACKUP, HIT                                   | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 33.0%)]
   - Group 8: **0.3973** | BUST, SPLIT, COVER, STAND                                         | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 9: **0.4765** | BUST, SUBSTITUTE, RELIEF, BACKUP                                  | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 35.6%)]
   - Group 10: **0.3852** | SPLIT, COVER, STAND, HIT                                          | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 11: **0.4292** | SPLIT, COVER, SUBSTITUTE, HIT                                     | INCORRECT (Max overlap: 2/4 with BLACKJACK TERMS)
   - Group 12: **0.3847** | BUST, STAND, RELIEF, BACKUP                                       | INCORRECT (Max overlap: 2/4 with BLACKJACK TERMS) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 28.8%)]
   - Group 13: **0.3935** | BUST, TRUNK, TORSO, MIDSECTION                                    | INCORRECT (Max overlap: 3/4 with ABDOMINAL AREA) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 28.9%)]
   - Group 14: **0.3903** | STAND, RELIEF, BACKUP, STATUE                                     | INCORRECT (Max overlap: 2/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (55.9%, no-rel 29.0%)]
   - Group 15: **0.4816** | COVER, STAND, SUBSTITUTE, BACKUP                                  | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 36.7%)]
   - Group 16: **0.3811** | BUST, SPLIT, RELIEF, HIT                                          | INCORRECT (Max overlap: 3/4 with BLACKJACK TERMS)
   - Group 17: **0.4838** | COVER, SUBSTITUTE, RELIEF, BACKUP                                 | CORRECT GROUP (REPLACEMENT, Level 1)
   - Group 18: **0.3805** | BUST, SPLIT, STAND, HIT                                           | CORRECT GROUP (BLACKJACK TERMS, Level 3)
   - Group 19: **0.4584** | SUBSTITUTE, RELIEF, BACKUP, STATUE                                | INCORRECT (Max overlap: 3/4 with REPLACEMENT) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 32.4%)]
   - Group 20: **0.4168** | COVER, STAND, SUBSTITUTE, HIT                                     | INCORRECT (Max overlap: 2/4 with REPLACEMENT)

---

## Puzzle 39 (ID: 372)
**Words on Board:** SEND, MAIL, BALM, FIX, LINER, STAIN, ANGLE, HOLE, CORNER, POST, TEMPERATURE, GLOSS, EDUCATION, CRIME, SPOT, SHIP

### Ground Truth Categories:
* **Level 0 (DELIVER, AS A PACKAGE) [Type: SYNONYM_OR_NEAR]:** MAIL, POST, SEND, SHIP
* **Level 1 (KINDS OF LIP MAKEUP) [Type: SEMANTIC_SET]:** BALM, GLOSS, LINER, STAIN
* **Level 2 (PREDICAMENT) [Type: SYNONYM_OR_NEAR]:** CORNER, FIX, HOLE, SPOT
* **Level 3 (MEASURED IN DEGREES) [Type: SEMANTIC_SET]:** ANGLE, CRIME, EDUCATION, TEMPERATURE

### Top Candidate Partitions:
1. **Partition Score: 0.4648**
   - Group 1: **0.7340** | SEND, MAIL, POST, SHIP                                            | CORRECT GROUP (DELIVER, AS A PACKAGE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 32.7%)]
   - Group 2: **0.6604** | BALM, TEMPERATURE, EDUCATION, CRIME                               | INCORRECT (Max overlap: 3/4 with MEASURED IN DEGREES)
   - Group 3: **0.4332** | FIX, ANGLE, HOLE, CORNER                                          | INCORRECT (Max overlap: 3/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (57.1%, no-rel 31.9%)]
   - Group 4: **0.3828** | LINER, STAIN, GLOSS, SPOT                                         | INCORRECT (Max overlap: 3/4 with KINDS OF LIP MAKEUP)
2. **Partition Score: 0.4324**
   - Group 1: **0.7340** | SEND, MAIL, POST, SHIP                                            | CORRECT GROUP (DELIVER, AS A PACKAGE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 32.7%)]
   - Group 2: **0.6604** | BALM, TEMPERATURE, EDUCATION, CRIME                               | INCORRECT (Max overlap: 3/4 with MEASURED IN DEGREES)
   - Group 3: **0.4226** | ANGLE, HOLE, CORNER, SPOT                                         | INCORRECT (Max overlap: 3/4 with PREDICAMENT)
   - Group 4: **0.3232** | FIX, LINER, STAIN, GLOSS                                          | INCORRECT (Max overlap: 3/4 with KINDS OF LIP MAKEUP)
3. **Partition Score: 0.4301**
   - Group 1: **0.6604** | BALM, TEMPERATURE, EDUCATION, CRIME                               | INCORRECT (Max overlap: 3/4 with MEASURED IN DEGREES)
   - Group 2: **0.6167** | SEND, MAIL, POST, SPOT                                            | INCORRECT (Max overlap: 3/4 with DELIVER, AS A PACKAGE) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 34.0%)]
   - Group 3: **0.4332** | FIX, ANGLE, HOLE, CORNER                                          | INCORRECT (Max overlap: 3/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (57.1%, no-rel 31.9%)]
   - Group 4: **0.3351** | LINER, STAIN, GLOSS, SHIP                                         | INCORRECT (Max overlap: 3/4 with KINDS OF LIP MAKEUP) | [Pred Type: SEMANTIC_SET (50.5%, no-rel 23.0%)]
4. **Partition Score: 0.4239**
   - Group 1: **0.6604** | BALM, TEMPERATURE, EDUCATION, CRIME                               | INCORRECT (Max overlap: 3/4 with MEASURED IN DEGREES)
   - Group 2: **0.4332** | FIX, ANGLE, HOLE, CORNER                                          | INCORRECT (Max overlap: 3/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (57.1%, no-rel 31.9%)]
   - Group 3: **0.4307** | STAIN, POST, GLOSS, SPOT                                          | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 4: **0.4158** | SEND, MAIL, LINER, SHIP                                           | INCORRECT (Max overlap: 3/4 with DELIVER, AS A PACKAGE)
5. **Partition Score: 0.4238**
   - Group 1: **0.6604** | BALM, TEMPERATURE, EDUCATION, CRIME                               | INCORRECT (Max overlap: 3/4 with MEASURED IN DEGREES)
   - Group 2: **0.4779** | ANGLE, CORNER, POST, SPOT                                         | INCORRECT (Max overlap: 2/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 38.0%)]
   - Group 3: **0.4158** | SEND, MAIL, LINER, SHIP                                           | INCORRECT (Max overlap: 3/4 with DELIVER, AS A PACKAGE)
   - Group 4: **0.4008** | FIX, STAIN, HOLE, GLOSS                                           | INCORRECT (Max overlap: 2/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (58.2%, no-rel 29.2%)]

### Top Candidate Groups:
   - Group 1: **0.7340** | SEND, MAIL, POST, SHIP                                            | CORRECT GROUP (DELIVER, AS A PACKAGE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 32.7%)]
   - Group 2: **0.6604** | BALM, TEMPERATURE, EDUCATION, CRIME                               | INCORRECT (Max overlap: 3/4 with MEASURED IN DEGREES)
   - Group 3: **0.4332** | FIX, ANGLE, HOLE, CORNER                                          | INCORRECT (Max overlap: 3/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (57.1%, no-rel 31.9%)]
   - Group 4: **0.3828** | LINER, STAIN, GLOSS, SPOT                                         | INCORRECT (Max overlap: 3/4 with KINDS OF LIP MAKEUP)
   - Group 5: **0.4226** | ANGLE, HOLE, CORNER, SPOT                                         | INCORRECT (Max overlap: 3/4 with PREDICAMENT)
   - Group 6: **0.3232** | FIX, LINER, STAIN, GLOSS                                          | INCORRECT (Max overlap: 3/4 with KINDS OF LIP MAKEUP)
   - Group 7: **0.6167** | SEND, MAIL, POST, SPOT                                            | INCORRECT (Max overlap: 3/4 with DELIVER, AS A PACKAGE) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 34.0%)]
   - Group 8: **0.3351** | LINER, STAIN, GLOSS, SHIP                                         | INCORRECT (Max overlap: 3/4 with KINDS OF LIP MAKEUP) | [Pred Type: SEMANTIC_SET (50.5%, no-rel 23.0%)]
   - Group 9: **0.4307** | STAIN, POST, GLOSS, SPOT                                          | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)
   - Group 10: **0.4158** | SEND, MAIL, LINER, SHIP                                           | INCORRECT (Max overlap: 3/4 with DELIVER, AS A PACKAGE)
   - Group 11: **0.4779** | ANGLE, CORNER, POST, SPOT                                         | INCORRECT (Max overlap: 2/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 38.0%)]
   - Group 12: **0.4008** | FIX, STAIN, HOLE, GLOSS                                           | INCORRECT (Max overlap: 2/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (58.2%, no-rel 29.2%)]
   - Group 13: **0.4853** | FIX, STAIN, GLOSS, SPOT                                           | INCORRECT (Max overlap: 2/4 with PREDICAMENT)
   - Group 14: **0.3821** | ANGLE, HOLE, CORNER, POST                                         | INCORRECT (Max overlap: 2/4 with PREDICAMENT)
   - Group 15: **0.5157** | SEND, MAIL, CORNER, POST                                          | INCORRECT (Max overlap: 3/4 with DELIVER, AS A PACKAGE) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 32.2%)]
   - Group 16: **0.3748** | FIX, ANGLE, HOLE, SHIP                                            | INCORRECT (Max overlap: 2/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 31.9%)]
   - Group 17: **0.3208** | LINER, ANGLE, HOLE, SHIP                                          | INCORRECT (Max overlap: 1/4 with KINDS OF LIP MAKEUP)
   - Group 18: **0.4700** | SEND, MAIL, ANGLE, POST                                           | INCORRECT (Max overlap: 3/4 with DELIVER, AS A PACKAGE) | [Pred Type: SYNONYM_OR_NEAR (55.9%, no-rel 32.9%)]
   - Group 19: **0.3984** | FIX, LINER, HOLE, SHIP                                            | INCORRECT (Max overlap: 2/4 with PREDICAMENT) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 23.5%)]
   - Group 20: **0.3769** | STAIN, CORNER, GLOSS, SPOT                                        | INCORRECT (Max overlap: 2/4 with KINDS OF LIP MAKEUP)

---

## Puzzle 40 (ID: 954)
**Words on Board:** CAN, SUIT, NEWSPAPER, CAVE, MOBILE, SHEET, THROW, SIGNAL, BLANKET, COPY, CARDBOARD BOX, LIFT, PIRATE, BOTTLE, CRIB, SHAM

### Ground Truth Categories:
* **Level 0 (ITEMS TO RECYCLE) [Type: SEMANTIC_SET]:** BOTTLE, CAN, CARDBOARD BOX, NEWSPAPER
* **Level 1 (BEDDING) [Type: SEMANTIC_SET]:** BLANKET, SHAM, SHEET, THROW
* **Level 2 (PLAGIARIZE) [Type: SYNONYM_OR_NEAR]:** COPY, CRIB, LIFT, PIRATE
* **Level 3 (BATMAN'S "BAT" THINGS) [Type: FILL_IN_THE_BLANK]:** CAVE, MOBILE, SIGNAL, SUIT

### Top Candidate Partitions:
1. **Partition Score: 0.3788**
   - Group 1: **0.4920** | NEWSPAPER, SHEET, BLANKET, CARDBOARD BOX                          | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (64.4%, no-rel 14.6%)]
   - Group 2: **0.4876** | SIGNAL, COPY, PIRATE, SHAM                                        | INCORRECT (Max overlap: 2/4 with PLAGIARIZE) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 34.9%)]
   - Group 3: **0.3459** | SUIT, CAVE, MOBILE, CRIB                                          | INCORRECT (Max overlap: 3/4 with BATMAN'S "BAT" THINGS)
   - Group 4: **0.3409** | CAN, THROW, LIFT, BOTTLE                                          | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE)
2. **Partition Score: 0.3756**
   - Group 1: **0.4920** | NEWSPAPER, SHEET, BLANKET, CARDBOARD BOX                          | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (64.4%, no-rel 14.6%)]
   - Group 2: **0.4876** | SIGNAL, COPY, PIRATE, SHAM                                        | INCORRECT (Max overlap: 2/4 with PLAGIARIZE) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 34.9%)]
   - Group 3: **0.3458** | CAN, SUIT, THROW, BOTTLE                                          | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 24.9%)]
   - Group 4: **0.3345** | CAVE, MOBILE, LIFT, CRIB                                          | INCORRECT (Max overlap: 2/4 with BATMAN'S "BAT" THINGS)
3. **Partition Score: 0.3682**
   - Group 1: **0.4876** | SIGNAL, COPY, PIRATE, SHAM                                        | INCORRECT (Max overlap: 2/4 with PLAGIARIZE) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 34.9%)]
   - Group 2: **0.4587** | NEWSPAPER, SHEET, BLANKET, CRIB                                   | INCORRECT (Max overlap: 2/4 with BEDDING) | [Pred Type: SEMANTIC_SET (51.8%, no-rel 22.7%)]
   - Group 3: **0.3409** | CAN, THROW, LIFT, BOTTLE                                          | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE)
   - Group 4: **0.3366** | SUIT, CAVE, MOBILE, CARDBOARD BOX                                 | INCORRECT (Max overlap: 3/4 with BATMAN'S "BAT" THINGS)
4. **Partition Score: 0.3665**
   - Group 1: **0.4184** | NEWSPAPER, SHEET, CARDBOARD BOX, CRIB                             | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (68.8%, no-rel 21.0%)]
   - Group 2: **0.4157** | SIGNAL, COPY, LIFT, PIRATE                                        | INCORRECT (Max overlap: 3/4 with PLAGIARIZE)
   - Group 3: **0.3602** | CAN, THROW, BLANKET, BOTTLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (48.1%, no-rel 24.3%)]
   - Group 4: **0.3451** | SUIT, CAVE, MOBILE, SHAM                                          | INCORRECT (Max overlap: 3/4 with BATMAN'S "BAT" THINGS)
5. **Partition Score: 0.3657**
   - Group 1: **0.4284** | SUIT, THROW, LIFT, PIRATE                                         | INCORRECT (Max overlap: 2/4 with PLAGIARIZE)
   - Group 2: **0.4228** | NEWSPAPER, SHEET, BLANKET, BOTTLE                                 | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (53.7%, no-rel 20.0%)]
   - Group 3: **0.3488** | CAN, SIGNAL, COPY, SHAM                                           | INCORRECT (Max overlap: 1/4 with ITEMS TO RECYCLE) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 27.0%)]
   - Group 4: **0.3456** | CAVE, MOBILE, CARDBOARD BOX, CRIB                                 | INCORRECT (Max overlap: 2/4 with BATMAN'S "BAT" THINGS)

### Top Candidate Groups:
   - Group 1: **0.4920** | NEWSPAPER, SHEET, BLANKET, CARDBOARD BOX                          | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (64.4%, no-rel 14.6%)]
   - Group 2: **0.4876** | SIGNAL, COPY, PIRATE, SHAM                                        | INCORRECT (Max overlap: 2/4 with PLAGIARIZE) | [Pred Type: SYNONYM_OR_NEAR (51.5%, no-rel 34.9%)]
   - Group 3: **0.3459** | SUIT, CAVE, MOBILE, CRIB                                          | INCORRECT (Max overlap: 3/4 with BATMAN'S "BAT" THINGS)
   - Group 4: **0.3409** | CAN, THROW, LIFT, BOTTLE                                          | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE)
   - Group 5: **0.3458** | CAN, SUIT, THROW, BOTTLE                                          | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 24.9%)]
   - Group 6: **0.3345** | CAVE, MOBILE, LIFT, CRIB                                          | INCORRECT (Max overlap: 2/4 with BATMAN'S "BAT" THINGS)
   - Group 7: **0.4587** | NEWSPAPER, SHEET, BLANKET, CRIB                                   | INCORRECT (Max overlap: 2/4 with BEDDING) | [Pred Type: SEMANTIC_SET (51.8%, no-rel 22.7%)]
   - Group 8: **0.3366** | SUIT, CAVE, MOBILE, CARDBOARD BOX                                 | INCORRECT (Max overlap: 3/4 with BATMAN'S "BAT" THINGS)
   - Group 9: **0.4184** | NEWSPAPER, SHEET, CARDBOARD BOX, CRIB                             | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (68.8%, no-rel 21.0%)]
   - Group 10: **0.4157** | SIGNAL, COPY, LIFT, PIRATE                                        | INCORRECT (Max overlap: 3/4 with PLAGIARIZE)
   - Group 11: **0.3602** | CAN, THROW, BLANKET, BOTTLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (48.1%, no-rel 24.3%)]
   - Group 12: **0.3451** | SUIT, CAVE, MOBILE, SHAM                                          | INCORRECT (Max overlap: 3/4 with BATMAN'S "BAT" THINGS)
   - Group 13: **0.4284** | SUIT, THROW, LIFT, PIRATE                                         | INCORRECT (Max overlap: 2/4 with PLAGIARIZE)
   - Group 14: **0.4228** | NEWSPAPER, SHEET, BLANKET, BOTTLE                                 | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE) | [Pred Type: SEMANTIC_SET (53.7%, no-rel 20.0%)]
   - Group 15: **0.3488** | CAN, SIGNAL, COPY, SHAM                                           | INCORRECT (Max overlap: 1/4 with ITEMS TO RECYCLE) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 27.0%)]
   - Group 16: **0.3456** | CAVE, MOBILE, CARDBOARD BOX, CRIB                                 | INCORRECT (Max overlap: 2/4 with BATMAN'S "BAT" THINGS)
   - Group 17: **0.4088** | COPY, LIFT, PIRATE, SHAM                                          | INCORRECT (Max overlap: 3/4 with PLAGIARIZE) | [Pred Type: SYNONYM_OR_NEAR (50.7%, no-rel 36.1%)]
   - Group 18: **0.3552** | CAN, THROW, SIGNAL, BOTTLE                                        | INCORRECT (Max overlap: 2/4 with ITEMS TO RECYCLE)
   - Group 19: **0.3380** | SUIT, CAVE, MOBILE, LIFT                                          | INCORRECT (Max overlap: 3/4 with BATMAN'S "BAT" THINGS)
   - Group 20: **0.3375** | CAVE, MOBILE, BOTTLE, CRIB                                        | INCORRECT (Max overlap: 2/4 with BATMAN'S "BAT" THINGS)

---

## Puzzle 41 (ID: 20)
**Words on Board:** BROWN, RICE, BONG, LEE, PRINCE, KING, SPELT, BARLEY, RYE, DUKE, EARL, OAT, FORD, HOWARD, STONE, BARON

### Ground Truth Categories:
* **Level 0 (GRAINS) [Type: SEMANTIC_SET]:** BARLEY, OAT, RYE, SPELT
* **Level 1 (ROYAL TITLES) [Type: SEMANTIC_SET]:** BARON, EARL, KING, PRINCE
* **Level 2 (UNIVERSITIES) [Type: NAMED_ENTITY_SET]:** BROWN, DUKE, HOWARD, RICE
* **Level 3 (BEST DIRECTOR OSCAR WINNERS) [Type: NAMED_ENTITY_SET]:** BONG, FORD, LEE, STONE

### Top Candidate Partitions:
1. **Partition Score: 0.4676**
   - Group 1: **0.7924** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS) | [Pred Type: SEMANTIC_SET (60.4%, no-rel 19.3%)]
   - Group 2: **0.5864** | PRINCE, KING, DUKE, BARON                                         | INCORRECT (Max overlap: 3/4 with ROYAL TITLES) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 12.3%)]
   - Group 3: **0.4781** | BROWN, BONG, SPELT, STONE                                         | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 4: **0.4029** | LEE, EARL, FORD, HOWARD                                           | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS) | [Pred Type: NAMED_ENTITY_SET (47.2%, no-rel 17.0%)]
2. **Partition Score: 0.4591**
   - Group 1: **0.7924** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS) | [Pred Type: SEMANTIC_SET (60.4%, no-rel 19.3%)]
   - Group 2: **0.5421** | PRINCE, DUKE, EARL, BARON                                         | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 3: **0.4610** | BONG, LEE, FORD, HOWARD                                           | INCORRECT (Max overlap: 3/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 4: **0.4168** | BROWN, KING, SPELT, STONE                                         | INCORRECT (Max overlap: 1/4 with UNIVERSITIES)
3. **Partition Score: 0.4378**
   - Group 1: **0.7924** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS) | [Pred Type: SEMANTIC_SET (60.4%, no-rel 19.3%)]
   - Group 2: **0.5421** | PRINCE, DUKE, EARL, BARON                                         | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 3: **0.4264** | BROWN, BONG, KING, STONE                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 4: **0.3914** | LEE, SPELT, FORD, HOWARD                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
4. **Partition Score: 0.4363**
   - Group 1: **0.7924** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS) | [Pred Type: SEMANTIC_SET (60.4%, no-rel 19.3%)]
   - Group 2: **0.5541** | KING, DUKE, EARL, BARON                                           | INCORRECT (Max overlap: 3/4 with ROYAL TITLES) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 9.8%)]
   - Group 3: **0.4781** | BROWN, BONG, SPELT, STONE                                         | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 4: **0.3566** | LEE, PRINCE, FORD, HOWARD                                         | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
5. **Partition Score: 0.4256**
   - Group 1: **0.7924** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS) | [Pred Type: SEMANTIC_SET (60.4%, no-rel 19.3%)]
   - Group 2: **0.5864** | PRINCE, KING, DUKE, BARON                                         | INCORRECT (Max overlap: 3/4 with ROYAL TITLES) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 12.3%)]
   - Group 3: **0.3720** | BROWN, LEE, SPELT, STONE                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 4: **0.3720** | BONG, EARL, FORD, HOWARD                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)

### Top Candidate Groups:
   - Group 1: **0.7924** | RICE, BARLEY, RYE, OAT                                            | INCORRECT (Max overlap: 3/4 with GRAINS) | [Pred Type: SEMANTIC_SET (60.4%, no-rel 19.3%)]
   - Group 2: **0.5864** | PRINCE, KING, DUKE, BARON                                         | INCORRECT (Max overlap: 3/4 with ROYAL TITLES) | [Pred Type: SYNONYM_OR_NEAR (53.4%, no-rel 12.3%)]
   - Group 3: **0.4781** | BROWN, BONG, SPELT, STONE                                         | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 4: **0.4029** | LEE, EARL, FORD, HOWARD                                           | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS) | [Pred Type: NAMED_ENTITY_SET (47.2%, no-rel 17.0%)]
   - Group 5: **0.5421** | PRINCE, DUKE, EARL, BARON                                         | INCORRECT (Max overlap: 3/4 with ROYAL TITLES)
   - Group 6: **0.4610** | BONG, LEE, FORD, HOWARD                                           | INCORRECT (Max overlap: 3/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 7: **0.4168** | BROWN, KING, SPELT, STONE                                         | INCORRECT (Max overlap: 1/4 with UNIVERSITIES)
   - Group 8: **0.4264** | BROWN, BONG, KING, STONE                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 9: **0.3914** | LEE, SPELT, FORD, HOWARD                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 10: **0.5541** | KING, DUKE, EARL, BARON                                           | INCORRECT (Max overlap: 3/4 with ROYAL TITLES) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 9.8%)]
   - Group 11: **0.3566** | LEE, PRINCE, FORD, HOWARD                                         | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 12: **0.3720** | BROWN, LEE, SPELT, STONE                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 13: **0.3720** | BONG, EARL, FORD, HOWARD                                          | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS)
   - Group 14: **0.4163** | BROWN, BONG, KING, SPELT                                          | INCORRECT (Max overlap: 1/4 with UNIVERSITIES)
   - Group 15: **0.3641** | LEE, FORD, HOWARD, STONE                                          | INCORRECT (Max overlap: 3/4 with BEST DIRECTOR OSCAR WINNERS) | [Pred Type: NAMED_ENTITY_SET (51.1%, no-rel 9.6%)]
   - Group 16: **0.3641** | BROWN, BONG, SPELT, EARL                                          | INCORRECT (Max overlap: 1/4 with UNIVERSITIES)
   - Group 17: **0.4941** | PRINCE, KING, EARL, BARON                                         | CORRECT GROUP (ROYAL TITLES, Level 1) | [Pred Type: SYNONYM_OR_NEAR (51.4%, no-rel 10.4%)]
   - Group 18: **0.3471** | LEE, DUKE, FORD, HOWARD                                           | INCORRECT (Max overlap: 2/4 with BEST DIRECTOR OSCAR WINNERS) | [Pred Type: NAMED_ENTITY_SET (56.5%, no-rel 8.9%)]
   - Group 19: **0.3746** | BROWN, BONG, PRINCE, SPELT                                        | INCORRECT (Max overlap: 1/4 with UNIVERSITIES)
   - Group 20: **0.4119** | BROWN, RICE, SPELT, STONE                                         | INCORRECT (Max overlap: 2/4 with UNIVERSITIES)

---

## Puzzle 42 (ID: 501)
**Words on Board:** BILL, ADIEU, GAMES, AUDIO, SCHEDULE, NEWS, PROGRAM, TEMPS, AIRPLANE, FORTUNE TELLER, BELLE, PAIN, SLATE, COOKING, FAN, CRANE

### Ground Truth Categories:
* **Level 0 (LINEUP) [Type: SYNONYM_OR_NEAR]:** BILL, PROGRAM, SCHEDULE, SLATE
* **Level 1 (NYT OFFERINGS) [Type: NAMED_ENTITY_SET]:** AUDIO, COOKING, GAMES, NEWS
* **Level 2 (THINGS MADE BY FOLDING PAPER) [Type: SEMANTIC_SET]:** AIRPLANE, CRANE, FAN, FORTUNE TELLER
* **Level 3 (FRENCH WORDS) [Type: SEMANTIC_SET]:** ADIEU, BELLE, PAIN, TEMPS

### Top Candidate Partitions:
1. **Partition Score: 0.4739**
   - Group 1: **0.6457** | BILL, SCHEDULE, PROGRAM, SLATE                                    | CORRECT GROUP (LINEUP, Level 0)
   - Group 2: **0.5809** | AIRPLANE, FORTUNE TELLER, BELLE, CRANE                            | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 3: **0.5253** | ADIEU, GAMES, PAIN, COOKING                                       | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 4: **0.3947** | AUDIO, NEWS, TEMPS, FAN                                           | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
2. **Partition Score: 0.4631**
   - Group 1: **0.6457** | BILL, SCHEDULE, PROGRAM, SLATE                                    | CORRECT GROUP (LINEUP, Level 0)
   - Group 2: **0.5809** | AIRPLANE, FORTUNE TELLER, BELLE, CRANE                            | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 3: **0.5059** | GAMES, PAIN, COOKING, FAN                                         | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
   - Group 4: **0.3827** | ADIEU, AUDIO, NEWS, TEMPS                                         | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
3. **Partition Score: 0.4625**
   - Group 1: **0.6457** | BILL, SCHEDULE, PROGRAM, SLATE                                    | CORRECT GROUP (LINEUP, Level 0)
   - Group 2: **0.5809** | AIRPLANE, FORTUNE TELLER, BELLE, CRANE                            | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 3: **0.4393** | ADIEU, PAIN, COOKING, FAN                                         | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 4: **0.4149** | GAMES, AUDIO, NEWS, TEMPS                                         | INCORRECT (Max overlap: 3/4 with NYT OFFERINGS)
4. **Partition Score: 0.4495**
   - Group 1: **0.6457** | BILL, SCHEDULE, PROGRAM, SLATE                                    | CORRECT GROUP (LINEUP, Level 0)
   - Group 2: **0.5809** | AIRPLANE, FORTUNE TELLER, BELLE, CRANE                            | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 3: **0.4564** | TEMPS, PAIN, COOKING, FAN                                         | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 4: **0.3803** | ADIEU, GAMES, AUDIO, NEWS                                         | INCORRECT (Max overlap: 3/4 with NYT OFFERINGS)
5. **Partition Score: 0.4465**
   - Group 1: **0.6457** | BILL, SCHEDULE, PROGRAM, SLATE                                    | CORRECT GROUP (LINEUP, Level 0)
   - Group 2: **0.4982** | ADIEU, AIRPLANE, PAIN, COOKING                                    | INCORRECT (Max overlap: 2/4 with FRENCH WORDS) | [Pred Type: FILL_IN_THE_BLANK (49.7%, no-rel 25.3%)]
   - Group 3: **0.4581** | FORTUNE TELLER, BELLE, FAN, CRANE                                 | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 4: **0.4149** | GAMES, AUDIO, NEWS, TEMPS                                         | INCORRECT (Max overlap: 3/4 with NYT OFFERINGS)

### Top Candidate Groups:
   - Group 1: **0.6457** | BILL, SCHEDULE, PROGRAM, SLATE                                    | CORRECT GROUP (LINEUP, Level 0)
   - Group 2: **0.5809** | AIRPLANE, FORTUNE TELLER, BELLE, CRANE                            | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 3: **0.5253** | ADIEU, GAMES, PAIN, COOKING                                       | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 4: **0.3947** | AUDIO, NEWS, TEMPS, FAN                                           | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
   - Group 5: **0.5059** | GAMES, PAIN, COOKING, FAN                                         | INCORRECT (Max overlap: 2/4 with NYT OFFERINGS)
   - Group 6: **0.3827** | ADIEU, AUDIO, NEWS, TEMPS                                         | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 7: **0.4393** | ADIEU, PAIN, COOKING, FAN                                         | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 8: **0.4149** | GAMES, AUDIO, NEWS, TEMPS                                         | INCORRECT (Max overlap: 3/4 with NYT OFFERINGS)
   - Group 9: **0.4564** | TEMPS, PAIN, COOKING, FAN                                         | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 10: **0.3803** | ADIEU, GAMES, AUDIO, NEWS                                         | INCORRECT (Max overlap: 3/4 with NYT OFFERINGS)
   - Group 11: **0.4982** | ADIEU, AIRPLANE, PAIN, COOKING                                    | INCORRECT (Max overlap: 2/4 with FRENCH WORDS) | [Pred Type: FILL_IN_THE_BLANK (49.7%, no-rel 25.3%)]
   - Group 12: **0.4581** | FORTUNE TELLER, BELLE, FAN, CRANE                                 | INCORRECT (Max overlap: 3/4 with THINGS MADE BY FOLDING PAPER)
   - Group 13: **0.4827** | PAIN, COOKING, FAN, CRANE                                         | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 14: **0.4735** | ADIEU, AIRPLANE, FORTUNE TELLER, BELLE                            | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 15: **0.5264** | AIRPLANE, FORTUNE TELLER, FAN, CRANE                              | CORRECT GROUP (THINGS MADE BY FOLDING PAPER, Level 2)
   - Group 16: **0.4204** | ADIEU, BELLE, PAIN, COOKING                                       | INCORRECT (Max overlap: 3/4 with FRENCH WORDS)
   - Group 17: **0.5487** | AIRPLANE, FORTUNE TELLER, BELLE, COOKING                          | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)
   - Group 18: **0.4059** | ADIEU, PAIN, FAN, CRANE                                           | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 19: **0.4980** | ADIEU, GAMES, AIRPLANE, PAIN                                      | INCORRECT (Max overlap: 2/4 with FRENCH WORDS)
   - Group 20: **0.4873** | FORTUNE TELLER, BELLE, COOKING, CRANE                             | INCORRECT (Max overlap: 2/4 with THINGS MADE BY FOLDING PAPER)

---

## Puzzle 43 (ID: 332)
**Words on Board:** RUBY, SPONGE, BUBBLE, SPLASH, DROP, CHERRY, BRICK, ROSE, PICK, TOP, SPOT, CREAM, BIRD, MUD, BEST, SPRINKLE

### Ground Truth Categories:
* **Level 0 (SHADES OF RED) [Type: SEMANTIC_SET]:** BRICK, CHERRY, ROSE, RUBY
* **Level 1 (LITTLE BIT OF A BEVERAGE) [Type: SYNONYM_OR_NEAR]:** DROP, SPLASH, SPOT, SPRINKLE
* **Level 2 (CHOICEST) [Type: SYNONYM_OR_NEAR]:** BEST, CREAM, PICK, TOP
* **Level 3 (___ BATH) [Type: FILL_IN_THE_BLANK]:** BIRD, BUBBLE, MUD, SPONGE

### Top Candidate Partitions:
1. **Partition Score: 0.4333**
   - Group 1: **0.6032** | SPLASH, DROP, SPOT, SPRINKLE                                      | CORRECT GROUP (LITTLE BIT OF A BEVERAGE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (54.7%, no-rel 36.1%)]
   - Group 2: **0.5218** | PICK, TOP, CREAM, BEST                                            | CORRECT GROUP (CHOICEST, Level 2) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 26.9%)]
   - Group 3: **0.4098** | SPONGE, BUBBLE, BRICK, MUD                                        | INCORRECT (Max overlap: 3/4 with ___ BATH)
   - Group 4: **0.4008** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
2. **Partition Score: 0.4260**
   - Group 1: **0.5327** | SPLASH, DROP, SPOT, MUD                                           | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 2: **0.5218** | PICK, TOP, CREAM, BEST                                            | CORRECT GROUP (CHOICEST, Level 2) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 26.9%)]
   - Group 3: **0.4008** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 4: **0.3907** | SPONGE, BUBBLE, BRICK, SPRINKLE                                   | INCORRECT (Max overlap: 2/4 with ___ BATH)
3. **Partition Score: 0.4252**
   - Group 1: **0.4851** | DROP, TOP, CREAM, BEST                                            | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 2: **0.4843** | BUBBLE, SPLASH, SPOT, MUD                                         | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 3: **0.4147** | SPONGE, BRICK, PICK, SPRINKLE                                     | INCORRECT (Max overlap: 1/4 with ___ BATH)
   - Group 4: **0.4008** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
4. **Partition Score: 0.4228**
   - Group 1: **0.5580** | BUBBLE, SPLASH, DROP, SPRINKLE                                    | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE) | [Pred Type: SYNONYM_OR_NEAR (52.1%, no-rel 35.7%)]
   - Group 2: **0.5218** | PICK, TOP, CREAM, BEST                                            | CORRECT GROUP (CHOICEST, Level 2) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 26.9%)]
   - Group 3: **0.4008** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 4: **0.3844** | SPONGE, BRICK, SPOT, MUD                                          | INCORRECT (Max overlap: 2/4 with ___ BATH)
5. **Partition Score: 0.4224**
   - Group 1: **0.4851** | DROP, TOP, CREAM, BEST                                            | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 2: **0.4784** | SPLASH, PICK, SPOT, SPRINKLE                                      | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 31.5%)]
   - Group 3: **0.4098** | SPONGE, BUBBLE, BRICK, MUD                                        | INCORRECT (Max overlap: 3/4 with ___ BATH)
   - Group 4: **0.4008** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)

### Top Candidate Groups:
   - Group 1: **0.6032** | SPLASH, DROP, SPOT, SPRINKLE                                      | CORRECT GROUP (LITTLE BIT OF A BEVERAGE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (54.7%, no-rel 36.1%)]
   - Group 2: **0.5218** | PICK, TOP, CREAM, BEST                                            | CORRECT GROUP (CHOICEST, Level 2) | [Pred Type: SYNONYM_OR_NEAR (62.7%, no-rel 26.9%)]
   - Group 3: **0.4098** | SPONGE, BUBBLE, BRICK, MUD                                        | INCORRECT (Max overlap: 3/4 with ___ BATH)
   - Group 4: **0.4008** | RUBY, CHERRY, ROSE, BIRD                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 5: **0.5327** | SPLASH, DROP, SPOT, MUD                                           | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 6: **0.3907** | SPONGE, BUBBLE, BRICK, SPRINKLE                                   | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 7: **0.4851** | DROP, TOP, CREAM, BEST                                            | INCORRECT (Max overlap: 3/4 with CHOICEST)
   - Group 8: **0.4843** | BUBBLE, SPLASH, SPOT, MUD                                         | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 9: **0.4147** | SPONGE, BRICK, PICK, SPRINKLE                                     | INCORRECT (Max overlap: 1/4 with ___ BATH)
   - Group 10: **0.5580** | BUBBLE, SPLASH, DROP, SPRINKLE                                    | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE) | [Pred Type: SYNONYM_OR_NEAR (52.1%, no-rel 35.7%)]
   - Group 11: **0.3844** | SPONGE, BRICK, SPOT, MUD                                          | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 12: **0.4784** | SPLASH, PICK, SPOT, SPRINKLE                                      | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 31.5%)]
   - Group 13: **0.4546** | SPONGE, PICK, CREAM, BEST                                         | INCORRECT (Max overlap: 3/4 with CHOICEST) | [Pred Type: SYNONYM_OR_NEAR (56.4%, no-rel 27.9%)]
   - Group 14: **0.4446** | DROP, TOP, SPOT, SPRINKLE                                         | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 15: **0.4286** | BUBBLE, SPLASH, BRICK, MUD                                        | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 16: **0.4386** | SPLASH, BRICK, SPOT, MUD                                          | INCORRECT (Max overlap: 2/4 with LITTLE BIT OF A BEVERAGE)
   - Group 17: **0.4342** | BUBBLE, DROP, TOP, SPRINKLE                                       | INCORRECT (Max overlap: 2/4 with LITTLE BIT OF A BEVERAGE)
   - Group 18: **0.5502** | BUBBLE, SPLASH, DROP, SPOT                                        | INCORRECT (Max overlap: 3/4 with LITTLE BIT OF A BEVERAGE)
   - Group 19: **0.3708** | SPONGE, BRICK, MUD, SPRINKLE                                      | INCORRECT (Max overlap: 2/4 with ___ BATH)
   - Group 20: **0.4652** | BUBBLE, DROP, TOP, SPOT                                           | INCORRECT (Max overlap: 2/4 with LITTLE BIT OF A BEVERAGE)

---

## Puzzle 44 (ID: 614)
**Words on Board:** SURPRISE, SHED, INDULGE, HISS, SLITHER, RATTLE, BABY, STRAIGHT, BAE, CREAK, HUMOR, SEE, GUESS WHO, GOTCHA, PAMPER, BOO

### Ground Truth Categories:
* **Level 0 (MOLLYCODDLE) [Type: SYNONYM_OR_NEAR]:** BABY, HUMOR, INDULGE, PAMPER
* **Level 1 (THINGS A RATTLESNAKE DOES) [Type: SEMANTIC_SET]:** HISS, RATTLE, SHED, SLITHER
* **Level 2 (WORDS SAID TO AN UNSUSPECTING PERSON) [Type: SEMANTIC_SET]:** BOO, GOTCHA, GUESS WHO, SURPRISE
* **Level 3 (HOMOPHONES OF BODIES OF WATER) [Type: SOUND_OR_SPELLING]:** BAE, CREAK, SEE, STRAIGHT

### Top Candidate Partitions:
1. **Partition Score: 0.3378**
   - Group 1: **0.5055** | HISS, SLITHER, RATTLE, CREAK                                      | INCORRECT (Max overlap: 3/4 with THINGS A RATTLESNAKE DOES) | [Pred Type: SEMANTIC_SET (53.0%, no-rel 29.5%)]
   - Group 2: **0.3683** | INDULGE, BABY, PAMPER, BOO                                        | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (66.7%, no-rel 24.0%)]
   - Group 3: **0.3482** | SURPRISE, HUMOR, SEE, GOTCHA                                      | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 4: **0.3173** | SHED, STRAIGHT, BAE, GUESS WHO                                    | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
2. **Partition Score: 0.3370**
   - Group 1: **0.3906** | HISS, RATTLE, CREAK, BOO                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 2: **0.3652** | INDULGE, SLITHER, BABY, PAMPER                                    | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (65.8%, no-rel 22.0%)]
   - Group 3: **0.3482** | SURPRISE, HUMOR, SEE, GOTCHA                                      | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 4: **0.3173** | SHED, STRAIGHT, BAE, GUESS WHO                                    | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
3. **Partition Score: 0.3369**
   - Group 1: **0.3906** | HISS, RATTLE, CREAK, BOO                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 2: **0.3836** | INDULGE, BABY, GOTCHA, PAMPER                                     | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 30.1%)]
   - Group 3: **0.3667** | SHED, BAE, HUMOR, SEE                                             | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 4: **0.2987** | SURPRISE, SLITHER, STRAIGHT, GUESS WHO                            | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
4. **Partition Score: 0.3359**
   - Group 1: **0.3906** | HISS, RATTLE, CREAK, BOO                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 2: **0.3836** | INDULGE, BABY, GOTCHA, PAMPER                                     | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 30.1%)]
   - Group 3: **0.3536** | SHED, BAE, HUMOR, GUESS WHO                                       | INCORRECT (Max overlap: 1/4 with THINGS A RATTLESNAKE DOES)
   - Group 4: **0.3033** | SURPRISE, SLITHER, STRAIGHT, SEE                                  | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
5. **Partition Score: 0.3311**
   - Group 1: **0.3906** | HISS, RATTLE, CREAK, BOO                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 2: **0.3836** | INDULGE, BABY, GOTCHA, PAMPER                                     | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 30.1%)]
   - Group 3: **0.3590** | BAE, HUMOR, SEE, GUESS WHO                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 4: **0.2909** | SURPRISE, SHED, SLITHER, STRAIGHT                                 | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)

### Top Candidate Groups:
   - Group 1: **0.5055** | HISS, SLITHER, RATTLE, CREAK                                      | INCORRECT (Max overlap: 3/4 with THINGS A RATTLESNAKE DOES) | [Pred Type: SEMANTIC_SET (53.0%, no-rel 29.5%)]
   - Group 2: **0.3683** | INDULGE, BABY, PAMPER, BOO                                        | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (66.7%, no-rel 24.0%)]
   - Group 3: **0.3482** | SURPRISE, HUMOR, SEE, GOTCHA                                      | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 4: **0.3173** | SHED, STRAIGHT, BAE, GUESS WHO                                    | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 5: **0.3906** | HISS, RATTLE, CREAK, BOO                                          | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 6: **0.3652** | INDULGE, SLITHER, BABY, PAMPER                                    | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (65.8%, no-rel 22.0%)]
   - Group 7: **0.3836** | INDULGE, BABY, GOTCHA, PAMPER                                     | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 30.1%)]
   - Group 8: **0.3667** | SHED, BAE, HUMOR, SEE                                             | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 9: **0.2987** | SURPRISE, SLITHER, STRAIGHT, GUESS WHO                            | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 10: **0.3536** | SHED, BAE, HUMOR, GUESS WHO                                       | INCORRECT (Max overlap: 1/4 with THINGS A RATTLESNAKE DOES)
   - Group 11: **0.3033** | SURPRISE, SLITHER, STRAIGHT, SEE                                  | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 12: **0.3590** | BAE, HUMOR, SEE, GUESS WHO                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 13: **0.2909** | SURPRISE, SHED, SLITHER, STRAIGHT                                 | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 14: **0.3442** | INDULGE, BABY, BAE, PAMPER                                        | INCORRECT (Max overlap: 3/4 with MOLLYCODDLE) | [Pred Type: SYNONYM_OR_NEAR (65.2%, no-rel 19.8%)]
   - Group 15: **0.3150** | SHED, SLITHER, STRAIGHT, GUESS WHO                                | INCORRECT (Max overlap: 2/4 with THINGS A RATTLESNAKE DOES)
   - Group 16: **0.3299** | STRAIGHT, BAE, SEE, GUESS WHO                                     | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF BODIES OF WATER)
   - Group 17: **0.3104** | SURPRISE, SHED, HUMOR, GOTCHA                                     | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 18: **0.3085** | SURPRISE, SLITHER, HUMOR, SEE                                     | INCORRECT (Max overlap: 1/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 19: **0.3053** | SURPRISE, HUMOR, SEE, BOO                                         | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)
   - Group 20: **0.3127** | SURPRISE, SLITHER, SEE, GUESS WHO                                 | INCORRECT (Max overlap: 2/4 with WORDS SAID TO AN UNSUSPECTING PERSON)

---

## Puzzle 45 (ID: 1)
**Words on Board:** SLEET, SHIFT, HAIL, MOM, JAZZ, HEAT, SNOW, OPTION, NETS, TAB, RACECAR, RAIN, KAYAK, LEVEL, RETURN, BUCKS

### Ground Truth Categories:
* **Level 0 (WET WEATHER) [Type: SEMANTIC_SET]:** HAIL, RAIN, SLEET, SNOW
* **Level 1 (NBA TEAMS) [Type: NAMED_ENTITY_SET]:** BUCKS, HEAT, JAZZ, NETS
* **Level 2 (KEYBOARD KEYS) [Type: NAMED_ENTITY_SET]:** OPTION, RETURN, SHIFT, TAB
* **Level 3 (PALINDROMES) [Type: WORD_FORM]:** KAYAK, LEVEL, MOM, RACECAR

### Top Candidate Partitions:
1. **Partition Score: 0.4378**
   - Group 1: **0.8223** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 2: **0.5289** | MOM, RACECAR, KAYAK, BUCKS                                        | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.4188** | JAZZ, NETS, TAB, RETURN                                           | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
   - Group 4: **0.4017** | SHIFT, HEAT, OPTION, LEVEL                                        | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
2. **Partition Score: 0.4364**
   - Group 1: **0.8223** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 2: **0.5289** | MOM, RACECAR, KAYAK, BUCKS                                        | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.4193** | SHIFT, OPTION, LEVEL, RETURN                                      | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 4: **0.3986** | JAZZ, HEAT, NETS, TAB                                             | INCORRECT (Max overlap: 3/4 with NBA TEAMS)
3. **Partition Score: 0.4245**
   - Group 1: **0.8223** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 2: **0.5086** | MOM, JAZZ, RACECAR, KAYAK                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.4426** | OPTION, NETS, TAB, RETURN                                         | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 4: **0.3734** | SHIFT, HEAT, LEVEL, BUCKS                                         | INCORRECT (Max overlap: 2/4 with NBA TEAMS) | [Pred Type: SYNONYM_OR_NEAR (47.4%, no-rel 21.9%)]
4. **Partition Score: 0.4192**
   - Group 1: **0.8223** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 2: **0.5289** | MOM, RACECAR, KAYAK, BUCKS                                        | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.3838** | SHIFT, HEAT, LEVEL, RETURN                                        | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 4: **0.3820** | JAZZ, OPTION, NETS, TAB                                           | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
5. **Partition Score: 0.4158**
   - Group 1: **0.8223** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 2: **0.5289** | MOM, RACECAR, KAYAK, BUCKS                                        | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.4361** | SHIFT, TAB, LEVEL, RETURN                                         | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 4: **0.3490** | JAZZ, HEAT, OPTION, NETS                                          | INCORRECT (Max overlap: 3/4 with NBA TEAMS)

### Top Candidate Groups:
   - Group 1: **0.8223** | SLEET, HAIL, SNOW, RAIN                                           | CORRECT GROUP (WET WEATHER, Level 0)
   - Group 2: **0.5289** | MOM, RACECAR, KAYAK, BUCKS                                        | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.4188** | JAZZ, NETS, TAB, RETURN                                           | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
   - Group 4: **0.4017** | SHIFT, HEAT, OPTION, LEVEL                                        | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 5: **0.4193** | SHIFT, OPTION, LEVEL, RETURN                                      | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 6: **0.3986** | JAZZ, HEAT, NETS, TAB                                             | INCORRECT (Max overlap: 3/4 with NBA TEAMS)
   - Group 7: **0.5086** | MOM, JAZZ, RACECAR, KAYAK                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 8: **0.4426** | OPTION, NETS, TAB, RETURN                                         | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 9: **0.3734** | SHIFT, HEAT, LEVEL, BUCKS                                         | INCORRECT (Max overlap: 2/4 with NBA TEAMS) | [Pred Type: SYNONYM_OR_NEAR (47.4%, no-rel 21.9%)]
   - Group 10: **0.3838** | SHIFT, HEAT, LEVEL, RETURN                                        | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 11: **0.3820** | JAZZ, OPTION, NETS, TAB                                           | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
   - Group 12: **0.4361** | SHIFT, TAB, LEVEL, RETURN                                         | INCORRECT (Max overlap: 3/4 with KEYBOARD KEYS)
   - Group 13: **0.3490** | JAZZ, HEAT, OPTION, NETS                                          | INCORRECT (Max overlap: 3/4 with NBA TEAMS)
   - Group 14: **0.3871** | HEAT, NETS, TAB, RETURN                                           | INCORRECT (Max overlap: 2/4 with NBA TEAMS)
   - Group 15: **0.3729** | SHIFT, OPTION, LEVEL, BUCKS                                       | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS) | [Pred Type: SYNONYM_OR_NEAR (47.2%, no-rel 23.3%)]
   - Group 16: **0.4685** | MOM, JAZZ, RACECAR, BUCKS                                         | INCORRECT (Max overlap: 2/4 with PALINDROMES)
   - Group 17: **0.3836** | NETS, TAB, KAYAK, RETURN                                          | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS) | [Pred Type: SEMANTIC_SET (54.8%, no-rel 16.6%)]
   - Group 18: **0.4138** | HAIL, HEAT, SNOW, RAIN                                            | INCORRECT (Max overlap: 3/4 with WET WEATHER)
   - Group 19: **0.4004** | SLEET, SHIFT, OPTION, LEVEL                                       | INCORRECT (Max overlap: 2/4 with KEYBOARD KEYS)
   - Group 20: **0.4098** | SHIFT, HEAT, SNOW, LEVEL                                          | INCORRECT (Max overlap: 1/4 with KEYBOARD KEYS)

---

## Puzzle 46 (ID: 544)
**Words on Board:** STUMP, REX, CORE, JINX, SLINKY, SPELL, VEX, POX, PERPLEX, MANIA, GATE, PILLED, HAMM, HEX, PUZZLE, BUZZ

### Ground Truth Categories:
* **Level 0 (BAFFLE) [Type: SYNONYM_OR_NEAR]:** PERPLEX, PUZZLE, STUMP, VEX
* **Level 1 (CURSE) [Type: SYNONYM_OR_NEAR]:** HEX, JINX, POX, SPELL
* **Level 2 (“TOY STORY” CHARACTERS, FAMILIARLY) [Type: NAMED_ENTITY_SET]:** BUZZ, HAMM, REX, SLINKY
* **Level 3 (COLLOQUIAL SUFFIXES) [Type: WORD_FORM]:** CORE, GATE, MANIA, PILLED

### Top Candidate Partitions:
1. **Partition Score: 0.4382**
   - Group 1: **0.5600** | REX, CORE, POX, HAMM                                              | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 2: **0.5287** | JINX, SPELL, VEX, HEX                                             | INCORRECT (Max overlap: 3/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 29.5%)]
   - Group 3: **0.4915** | STUMP, PERPLEX, GATE, PUZZLE                                      | INCORRECT (Max overlap: 3/4 with BAFFLE) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 26.2%)]
   - Group 4: **0.3663** | SLINKY, MANIA, PILLED, BUZZ                                       | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY) | [Pred Type: WORDPLAY_TRANSFORM (46.3%, no-rel 9.4%)]
2. **Partition Score: 0.4378**
   - Group 1: **0.6300** | STUMP, VEX, PERPLEX, PUZZLE                                       | CORRECT GROUP (BAFFLE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.5%, no-rel 23.0%)]
   - Group 2: **0.5600** | REX, CORE, POX, HAMM                                              | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 3: **0.4587** | JINX, SPELL, GATE, HEX                                            | INCORRECT (Max overlap: 3/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 34.1%)]
   - Group 4: **0.3663** | SLINKY, MANIA, PILLED, BUZZ                                       | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY) | [Pred Type: WORDPLAY_TRANSFORM (46.3%, no-rel 9.4%)]
3. **Partition Score: 0.4370**
   - Group 1: **0.6300** | STUMP, VEX, PERPLEX, PUZZLE                                       | CORRECT GROUP (BAFFLE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.5%, no-rel 23.0%)]
   - Group 2: **0.5758** | JINX, SPELL, HEX, BUZZ                                            | INCORRECT (Max overlap: 3/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 31.6%)]
   - Group 3: **0.5600** | REX, CORE, POX, HAMM                                              | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 4: **0.3062** | SLINKY, MANIA, GATE, PILLED                                       | INCORRECT (Max overlap: 3/4 with COLLOQUIAL SUFFIXES)
4. **Partition Score: 0.4353**
   - Group 1: **0.5287** | JINX, SPELL, VEX, HEX                                             | INCORRECT (Max overlap: 3/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 29.5%)]
   - Group 2: **0.4915** | STUMP, PERPLEX, GATE, PUZZLE                                      | INCORRECT (Max overlap: 3/4 with BAFFLE) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 26.2%)]
   - Group 3: **0.4859** | REX, CORE, SLINKY, HAMM                                           | INCORRECT (Max overlap: 3/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 4: **0.3819** | POX, MANIA, PILLED, BUZZ                                          | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES) | [Pred Type: WORDPLAY_TRANSFORM (50.6%, no-rel 8.2%)]
5. **Partition Score: 0.4330**
   - Group 1: **0.6414** | REX, SLINKY, PILLED, HAMM                                         | INCORRECT (Max overlap: 3/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 2: **0.6300** | STUMP, VEX, PERPLEX, PUZZLE                                       | CORRECT GROUP (BAFFLE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.5%, no-rel 23.0%)]
   - Group 3: **0.4587** | JINX, SPELL, GATE, HEX                                            | INCORRECT (Max overlap: 3/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 34.1%)]
   - Group 4: **0.3215** | CORE, POX, MANIA, BUZZ                                            | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES)

### Top Candidate Groups:
   - Group 1: **0.5600** | REX, CORE, POX, HAMM                                              | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 2: **0.5287** | JINX, SPELL, VEX, HEX                                             | INCORRECT (Max overlap: 3/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (58.5%, no-rel 29.5%)]
   - Group 3: **0.4915** | STUMP, PERPLEX, GATE, PUZZLE                                      | INCORRECT (Max overlap: 3/4 with BAFFLE) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 26.2%)]
   - Group 4: **0.3663** | SLINKY, MANIA, PILLED, BUZZ                                       | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY) | [Pred Type: WORDPLAY_TRANSFORM (46.3%, no-rel 9.4%)]
   - Group 5: **0.6300** | STUMP, VEX, PERPLEX, PUZZLE                                       | CORRECT GROUP (BAFFLE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (64.5%, no-rel 23.0%)]
   - Group 6: **0.4587** | JINX, SPELL, GATE, HEX                                            | INCORRECT (Max overlap: 3/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 34.1%)]
   - Group 7: **0.5758** | JINX, SPELL, HEX, BUZZ                                            | INCORRECT (Max overlap: 3/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 31.6%)]
   - Group 8: **0.3062** | SLINKY, MANIA, GATE, PILLED                                       | INCORRECT (Max overlap: 3/4 with COLLOQUIAL SUFFIXES)
   - Group 9: **0.4859** | REX, CORE, SLINKY, HAMM                                           | INCORRECT (Max overlap: 3/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 10: **0.3819** | POX, MANIA, PILLED, BUZZ                                          | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES) | [Pred Type: WORDPLAY_TRANSFORM (50.6%, no-rel 8.2%)]
   - Group 11: **0.6414** | REX, SLINKY, PILLED, HAMM                                         | INCORRECT (Max overlap: 3/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 12: **0.3215** | CORE, POX, MANIA, BUZZ                                            | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES)
   - Group 13: **0.5584** | REX, CORE, MANIA, HAMM                                            | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 14: **0.2957** | SLINKY, POX, GATE, PILLED                                         | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES)
   - Group 15: **0.5492** | JINX, VEX, PERPLEX, HEX                                           | INCORRECT (Max overlap: 2/4 with CURSE) | [Pred Type: SYNONYM_OR_NEAR (59.8%, no-rel 29.1%)]
   - Group 16: **0.4421** | STUMP, SPELL, GATE, PUZZLE                                        | INCORRECT (Max overlap: 2/4 with BAFFLE)
   - Group 17: **0.3489** | SLINKY, POX, PILLED, BUZZ                                         | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY) | [Pred Type: WORDPLAY_TRANSFORM (47.3%, no-rel 9.7%)]
   - Group 18: **0.6976** | REX, POX, PILLED, HAMM                                            | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)
   - Group 19: **0.3144** | CORE, SLINKY, MANIA, BUZZ                                         | INCORRECT (Max overlap: 2/4 with COLLOQUIAL SUFFIXES)
   - Group 20: **0.5090** | REX, CORE, PILLED, HAMM                                           | INCORRECT (Max overlap: 2/4 with “TOY STORY” CHARACTERS, FAMILIARLY)

---

## Puzzle 47 (ID: 799)
**Words on Board:** BREAK, SIGNAL, BREAKFAST, PARKING, CHANCE, WI-FI, NOD, STOP, DIGITAL, PROMPT, CUE, SHOT, WRIST, POOL, POCKET, OPENING

### Ground Truth Categories:
* **Level 0 (INDICATION) [Type: SYNONYM_OR_NEAR]:** CUE, NOD, PROMPT, SIGNAL
* **Level 1 (OPPORTUNITY) [Type: SYNONYM_OR_NEAR]:** BREAK, CHANCE, OPENING, SHOT
* **Level 2 (HOTEL AMENITIES) [Type: SEMANTIC_SET]:** BREAKFAST, PARKING, POOL, WI-FI
* **Level 3 (WORDS BEFORE "WATCH") [Type: FILL_IN_THE_BLANK]:** DIGITAL, POCKET, STOP, WRIST

### Top Candidate Partitions:
1. **Partition Score: 0.4544**
   - Group 1: **0.5494** | BREAK, CHANCE, STOP, SHOT                                         | INCORRECT (Max overlap: 3/4 with OPPORTUNITY) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 33.3%)]
   - Group 2: **0.4988** | PARKING, WI-FI, DIGITAL, WRIST                                    | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 3: **0.4703** | SIGNAL, NOD, PROMPT, CUE                                          | CORRECT GROUP (INDICATION, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 33.2%)]
   - Group 4: **0.4243** | BREAKFAST, POOL, POCKET, OPENING                                  | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
2. **Partition Score: 0.4345**
   - Group 1: **0.4988** | PARKING, WI-FI, DIGITAL, WRIST                                    | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 2: **0.4907** | BREAK, CHANCE, NOD, SHOT                                          | INCORRECT (Max overlap: 3/4 with OPPORTUNITY)
   - Group 3: **0.4243** | BREAKFAST, POOL, POCKET, OPENING                                  | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 4: **0.4114** | SIGNAL, STOP, PROMPT, CUE                                         | INCORRECT (Max overlap: 3/4 with INDICATION) | [Pred Type: SYNONYM_OR_NEAR (58.1%, no-rel 31.7%)]
3. **Partition Score: 0.4322**
   - Group 1: **0.4988** | PARKING, WI-FI, DIGITAL, WRIST                                    | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 2: **0.4916** | BREAK, BREAKFAST, CHANCE, SHOT                                    | INCORRECT (Max overlap: 3/4 with OPPORTUNITY)
   - Group 3: **0.4703** | SIGNAL, NOD, PROMPT, CUE                                          | CORRECT GROUP (INDICATION, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 33.2%)]
   - Group 4: **0.3835** | STOP, POOL, POCKET, OPENING                                       | INCORRECT (Max overlap: 2/4 with WORDS BEFORE "WATCH") | [Pred Type: SYNONYM_OR_NEAR (48.2%, no-rel 25.4%)]
4. **Partition Score: 0.4183**
   - Group 1: **0.5494** | BREAK, CHANCE, STOP, SHOT                                         | INCORRECT (Max overlap: 3/4 with OPPORTUNITY) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 33.3%)]
   - Group 2: **0.4703** | SIGNAL, NOD, PROMPT, CUE                                          | CORRECT GROUP (INDICATION, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 33.2%)]
   - Group 3: **0.4034** | BREAKFAST, PARKING, WI-FI, DIGITAL                                | INCORRECT (Max overlap: 3/4 with HOTEL AMENITIES)
   - Group 4: **0.3997** | WRIST, POOL, POCKET, OPENING                                      | INCORRECT (Max overlap: 2/4 with WORDS BEFORE "WATCH")
5. **Partition Score: 0.4154**
   - Group 1: **0.4988** | PARKING, WI-FI, DIGITAL, WRIST                                    | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 2: **0.4916** | BREAK, BREAKFAST, CHANCE, SHOT                                    | INCORRECT (Max overlap: 3/4 with OPPORTUNITY)
   - Group 3: **0.3921** | CUE, POOL, POCKET, OPENING                                        | INCORRECT (Max overlap: 1/4 with INDICATION) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 24.3%)]
   - Group 4: **0.3889** | SIGNAL, NOD, STOP, PROMPT                                         | INCORRECT (Max overlap: 3/4 with INDICATION)

### Top Candidate Groups:
   - Group 1: **0.5494** | BREAK, CHANCE, STOP, SHOT                                         | INCORRECT (Max overlap: 3/4 with OPPORTUNITY) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 33.3%)]
   - Group 2: **0.4988** | PARKING, WI-FI, DIGITAL, WRIST                                    | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 3: **0.4703** | SIGNAL, NOD, PROMPT, CUE                                          | CORRECT GROUP (INDICATION, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 33.2%)]
   - Group 4: **0.4243** | BREAKFAST, POOL, POCKET, OPENING                                  | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 5: **0.4907** | BREAK, CHANCE, NOD, SHOT                                          | INCORRECT (Max overlap: 3/4 with OPPORTUNITY)
   - Group 6: **0.4114** | SIGNAL, STOP, PROMPT, CUE                                         | INCORRECT (Max overlap: 3/4 with INDICATION) | [Pred Type: SYNONYM_OR_NEAR (58.1%, no-rel 31.7%)]
   - Group 7: **0.4916** | BREAK, BREAKFAST, CHANCE, SHOT                                    | INCORRECT (Max overlap: 3/4 with OPPORTUNITY)
   - Group 8: **0.3835** | STOP, POOL, POCKET, OPENING                                       | INCORRECT (Max overlap: 2/4 with WORDS BEFORE "WATCH") | [Pred Type: SYNONYM_OR_NEAR (48.2%, no-rel 25.4%)]
   - Group 9: **0.4034** | BREAKFAST, PARKING, WI-FI, DIGITAL                                | INCORRECT (Max overlap: 3/4 with HOTEL AMENITIES)
   - Group 10: **0.3997** | WRIST, POOL, POCKET, OPENING                                      | INCORRECT (Max overlap: 2/4 with WORDS BEFORE "WATCH")
   - Group 11: **0.3921** | CUE, POOL, POCKET, OPENING                                        | INCORRECT (Max overlap: 1/4 with INDICATION) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 24.3%)]
   - Group 12: **0.3889** | SIGNAL, NOD, STOP, PROMPT                                         | INCORRECT (Max overlap: 3/4 with INDICATION)
   - Group 13: **0.4715** | BREAK, NOD, STOP, SHOT                                            | INCORRECT (Max overlap: 2/4 with OPPORTUNITY)
   - Group 14: **0.3755** | SIGNAL, CHANCE, PROMPT, CUE                                       | INCORRECT (Max overlap: 3/4 with INDICATION) | [Pred Type: SYNONYM_OR_NEAR (59.6%, no-rel 30.6%)]
   - Group 15: **0.4676** | BREAK, CHANCE, SHOT, WRIST                                        | INCORRECT (Max overlap: 3/4 with OPPORTUNITY)
   - Group 16: **0.4261** | BREAK, CHANCE, STOP, OPENING                                      | INCORRECT (Max overlap: 3/4 with OPPORTUNITY) | [Pred Type: SYNONYM_OR_NEAR (55.7%, no-rel 28.8%)]
   - Group 17: **0.4002** | SHOT, WRIST, POOL, POCKET                                         | INCORRECT (Max overlap: 2/4 with WORDS BEFORE "WATCH")
   - Group 18: **0.4484** | BREAKFAST, WI-FI, DIGITAL, WRIST                                  | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 19: **0.3545** | PARKING, POOL, POCKET, OPENING                                    | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)
   - Group 20: **0.3589** | BREAKFAST, SHOT, POOL, POCKET                                     | INCORRECT (Max overlap: 2/4 with HOTEL AMENITIES)

---

## Puzzle 48 (ID: 1031)
**Words on Board:** BEAM, SNOWFLAKE, COLUMN, JUMPER CABLES, BRACE, SPARE TIRE, PATRON, SPONSOR, ANGEL, STRUT, SCREWDRIVER, BOMBAY, CHAMPION, CHELSEA, ICE SCRAPER, JACK

### Ground Truth Categories:
* **Level 0 (FOUND IN THE TRUNK OF A CAR) [Type: SEMANTIC_SET]:** ICE SCRAPER, JACK, JUMPER CABLES, SPARE TIRE
* **Level 1 (BENEFACTOR) [Type: SYNONYM_OR_NEAR]:** ANGEL, CHAMPION, PATRON, SPONSOR
* **Level 2 (STRUCTURAL SUPPORTS) [Type: SYNONYM_OR_NEAR]:** BEAM, BRACE, COLUMN, STRUT
* **Level 3 (ENDING IN BODIES OF WATER) [Type: WORD_FORM]:** BOMBAY, CHELSEA, SCREWDRIVER, SNOWFLAKE

### Top Candidate Partitions:
1. **Partition Score: 0.4823**
   - Group 1: **0.6574** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (72.1%, no-rel 21.4%)]
   - Group 2: **0.6309** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 3: **0.5686** | SNOWFLAKE, SPARE TIRE, SCREWDRIVER, ICE SCRAPER                   | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER) | [Pred Type: SEMANTIC_SET (45.8%, no-rel 33.1%)]
   - Group 4: **0.3648** | JUMPER CABLES, BOMBAY, CHELSEA, JACK                              | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
2. **Partition Score: 0.4590**
   - Group 1: **0.6574** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (72.1%, no-rel 21.4%)]
   - Group 2: **0.6309** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 3: **0.4676** | SPARE TIRE, SCREWDRIVER, ICE SCRAPER, JACK                        | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR) | [Pred Type: SEMANTIC_SET (52.6%, no-rel 30.6%)]
   - Group 4: **0.3686** | SNOWFLAKE, JUMPER CABLES, BOMBAY, CHELSEA                         | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
3. **Partition Score: 0.4563**
   - Group 1: **0.6574** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (72.1%, no-rel 21.4%)]
   - Group 2: **0.6309** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 3: **0.4518** | SNOWFLAKE, SCREWDRIVER, ICE SCRAPER, JACK                         | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER) | [Pred Type: SEMANTIC_SET (52.6%, no-rel 31.2%)]
   - Group 4: **0.3712** | JUMPER CABLES, SPARE TIRE, BOMBAY, CHELSEA                        | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
4. **Partition Score: 0.4516**
   - Group 1: **0.6574** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (72.1%, no-rel 21.4%)]
   - Group 2: **0.6309** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 3: **0.4787** | JUMPER CABLES, SCREWDRIVER, ICE SCRAPER, JACK                     | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR) | [Pred Type: SEMANTIC_SET (55.1%, no-rel 27.3%)]
   - Group 4: **0.3484** | SNOWFLAKE, SPARE TIRE, BOMBAY, CHELSEA                            | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
5. **Partition Score: 0.4447**
   - Group 1: **0.6574** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (72.1%, no-rel 21.4%)]
   - Group 2: **0.6309** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 3: **0.4007** | SNOWFLAKE, JUMPER CABLES, CHELSEA, JACK                           | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)
   - Group 4: **0.3736** | SPARE TIRE, SCREWDRIVER, BOMBAY, ICE SCRAPER                      | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)

### Top Candidate Groups:
   - Group 1: **0.6574** | PATRON, SPONSOR, ANGEL, CHAMPION                                  | CORRECT GROUP (BENEFACTOR, Level 1) | [Pred Type: SYNONYM_OR_NEAR (72.1%, no-rel 21.4%)]
   - Group 2: **0.6309** | BEAM, COLUMN, BRACE, STRUT                                        | CORRECT GROUP (STRUCTURAL SUPPORTS, Level 2)
   - Group 3: **0.5686** | SNOWFLAKE, SPARE TIRE, SCREWDRIVER, ICE SCRAPER                   | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER) | [Pred Type: SEMANTIC_SET (45.8%, no-rel 33.1%)]
   - Group 4: **0.3648** | JUMPER CABLES, BOMBAY, CHELSEA, JACK                              | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 5: **0.4676** | SPARE TIRE, SCREWDRIVER, ICE SCRAPER, JACK                        | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR) | [Pred Type: SEMANTIC_SET (52.6%, no-rel 30.6%)]
   - Group 6: **0.3686** | SNOWFLAKE, JUMPER CABLES, BOMBAY, CHELSEA                         | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
   - Group 7: **0.4518** | SNOWFLAKE, SCREWDRIVER, ICE SCRAPER, JACK                         | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER) | [Pred Type: SEMANTIC_SET (52.6%, no-rel 31.2%)]
   - Group 8: **0.3712** | JUMPER CABLES, SPARE TIRE, BOMBAY, CHELSEA                        | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 9: **0.4787** | JUMPER CABLES, SCREWDRIVER, ICE SCRAPER, JACK                     | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR) | [Pred Type: SEMANTIC_SET (55.1%, no-rel 27.3%)]
   - Group 10: **0.3484** | SNOWFLAKE, SPARE TIRE, BOMBAY, CHELSEA                            | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
   - Group 11: **0.4007** | SNOWFLAKE, JUMPER CABLES, CHELSEA, JACK                           | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)
   - Group 12: **0.3736** | SPARE TIRE, SCREWDRIVER, BOMBAY, ICE SCRAPER                      | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 13: **0.3955** | SNOWFLAKE, SPARE TIRE, CHELSEA, ICE SCRAPER                       | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)
   - Group 14: **0.3750** | JUMPER CABLES, SCREWDRIVER, BOMBAY, JACK                          | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 15: **0.4278** | SNOWFLAKE, SPARE TIRE, ICE SCRAPER, JACK                          | INCORRECT (Max overlap: 3/4 with FOUND IN THE TRUNK OF A CAR) | [Pred Type: SEMANTIC_SET (48.8%, no-rel 32.6%)]
   - Group 16: **0.3537** | JUMPER CABLES, SCREWDRIVER, BOMBAY, CHELSEA                       | INCORRECT (Max overlap: 3/4 with ENDING IN BODIES OF WATER)
   - Group 17: **0.3846** | JUMPER CABLES, SCREWDRIVER, CHELSEA, JACK                         | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 18: **0.3749** | SNOWFLAKE, SPARE TIRE, BOMBAY, ICE SCRAPER                        | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)
   - Group 19: **0.3858** | SPARE TIRE, SCREWDRIVER, CHELSEA, ICE SCRAPER                     | INCORRECT (Max overlap: 2/4 with FOUND IN THE TRUNK OF A CAR)
   - Group 20: **0.3742** | SNOWFLAKE, JUMPER CABLES, BOMBAY, JACK                            | INCORRECT (Max overlap: 2/4 with ENDING IN BODIES OF WATER)

---

## Puzzle 49 (ID: 166)
**Words on Board:** PAN, FIAT, SLAM, RAM, ROAST, ALONE, LILY, SURVIVOR, MAXI, MOUSE, KNOCK, BACHELOR, CHOPPED, JAGUAR, MINI, CATFISH

### Ground Truth Categories:
* **Level 0 (CRITICIZE) [Type: SYNONYM_OR_NEAR]:** KNOCK, PAN, ROAST, SLAM
* **Level 1 (REALITY SHOWS) [Type: NAMED_ENTITY_SET]:** ALONE, CATFISH, CHOPPED, SURVIVOR
* **Level 2 (CAR BRANDS) [Type: NAMED_ENTITY_SET]:** FIAT, JAGUAR, MINI, RAM
* **Level 3 (___ PAD) [Type: FILL_IN_THE_BLANK]:** BACHELOR, LILY, MAXI, MOUSE

### Top Candidate Partitions:
1. **Partition Score: 0.3965**
   - Group 1: **0.6312** | PAN, ROAST, KNOCK, CHOPPED                                        | INCORRECT (Max overlap: 3/4 with CRITICIZE) | [Pred Type: SYNONYM_OR_NEAR (66.9%, no-rel 24.3%)]
   - Group 2: **0.4797** | RAM, SURVIVOR, MOUSE, JAGUAR                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.9%, no-rel 18.0%)]
   - Group 3: **0.4670** | FIAT, LILY, BACHELOR, CATFISH                                     | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 4: **0.3196** | SLAM, ALONE, MAXI, MINI                                           | INCORRECT (Max overlap: 1/4 with CRITICIZE)
2. **Partition Score: 0.3960**
   - Group 1: **0.6312** | PAN, ROAST, KNOCK, CHOPPED                                        | INCORRECT (Max overlap: 3/4 with CRITICIZE) | [Pred Type: SYNONYM_OR_NEAR (66.9%, no-rel 24.3%)]
   - Group 2: **0.4181** | RAM, SURVIVOR, MOUSE, CATFISH                                     | INCORRECT (Max overlap: 2/4 with REALITY SHOWS) | [Pred Type: NAMED_ENTITY_SET (50.2%, no-rel 16.4%)]
   - Group 3: **0.4127** | SLAM, ALONE, LILY, BACHELOR                                       | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 4: **0.3766** | FIAT, MAXI, JAGUAR, MINI                                          | INCORRECT (Max overlap: 3/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (48.5%, no-rel 9.9%)]
3. **Partition Score: 0.3945**
   - Group 1: **0.4797** | RAM, SURVIVOR, MOUSE, JAGUAR                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.9%, no-rel 18.0%)]
   - Group 2: **0.4670** | FIAT, LILY, BACHELOR, CATFISH                                     | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 3: **0.3924** | SLAM, ALONE, MAXI, CHOPPED                                        | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 4: **0.3594** | PAN, ROAST, KNOCK, MINI                                           | INCORRECT (Max overlap: 3/4 with CRITICIZE) | [Pred Type: SYNONYM_OR_NEAR (69.7%, no-rel 21.8%)]
4. **Partition Score: 0.3925**
   - Group 1: **0.4797** | RAM, SURVIVOR, MOUSE, JAGUAR                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.9%, no-rel 18.0%)]
   - Group 2: **0.4670** | FIAT, LILY, BACHELOR, CATFISH                                     | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 3: **0.3733** | ALONE, MAXI, CHOPPED, MINI                                        | INCORRECT (Max overlap: 2/4 with REALITY SHOWS) | [Pred Type: SYNONYM_OR_NEAR (51.2%, no-rel 29.3%)]
   - Group 4: **0.3648** | PAN, SLAM, ROAST, KNOCK                                           | CORRECT GROUP (CRITICIZE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (69.1%, no-rel 21.6%)]
5. **Partition Score: 0.3921**
   - Group 1: **0.4797** | RAM, SURVIVOR, MOUSE, JAGUAR                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.9%, no-rel 18.0%)]
   - Group 2: **0.4670** | FIAT, LILY, BACHELOR, CATFISH                                     | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 3: **0.4190** | PAN, ROAST, MAXI, KNOCK                                           | INCORRECT (Max overlap: 3/4 with CRITICIZE) | [Pred Type: SYNONYM_OR_NEAR (74.0%, no-rel 18.0%)]
   - Group 4: **0.3412** | SLAM, ALONE, CHOPPED, MINI                                        | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)

### Top Candidate Groups:
   - Group 1: **0.6312** | PAN, ROAST, KNOCK, CHOPPED                                        | INCORRECT (Max overlap: 3/4 with CRITICIZE) | [Pred Type: SYNONYM_OR_NEAR (66.9%, no-rel 24.3%)]
   - Group 2: **0.4797** | RAM, SURVIVOR, MOUSE, JAGUAR                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.9%, no-rel 18.0%)]
   - Group 3: **0.4670** | FIAT, LILY, BACHELOR, CATFISH                                     | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 4: **0.3196** | SLAM, ALONE, MAXI, MINI                                           | INCORRECT (Max overlap: 1/4 with CRITICIZE)
   - Group 5: **0.4181** | RAM, SURVIVOR, MOUSE, CATFISH                                     | INCORRECT (Max overlap: 2/4 with REALITY SHOWS) | [Pred Type: NAMED_ENTITY_SET (50.2%, no-rel 16.4%)]
   - Group 6: **0.4127** | SLAM, ALONE, LILY, BACHELOR                                       | INCORRECT (Max overlap: 2/4 with ___ PAD)
   - Group 7: **0.3766** | FIAT, MAXI, JAGUAR, MINI                                          | INCORRECT (Max overlap: 3/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (48.5%, no-rel 9.9%)]
   - Group 8: **0.3924** | SLAM, ALONE, MAXI, CHOPPED                                        | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 9: **0.3594** | PAN, ROAST, KNOCK, MINI                                           | INCORRECT (Max overlap: 3/4 with CRITICIZE) | [Pred Type: SYNONYM_OR_NEAR (69.7%, no-rel 21.8%)]
   - Group 10: **0.3733** | ALONE, MAXI, CHOPPED, MINI                                        | INCORRECT (Max overlap: 2/4 with REALITY SHOWS) | [Pred Type: SYNONYM_OR_NEAR (51.2%, no-rel 29.3%)]
   - Group 11: **0.3648** | PAN, SLAM, ROAST, KNOCK                                           | CORRECT GROUP (CRITICIZE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (69.1%, no-rel 21.6%)]
   - Group 12: **0.4190** | PAN, ROAST, MAXI, KNOCK                                           | INCORRECT (Max overlap: 3/4 with CRITICIZE) | [Pred Type: SYNONYM_OR_NEAR (74.0%, no-rel 18.0%)]
   - Group 13: **0.3412** | SLAM, ALONE, CHOPPED, MINI                                        | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 14: **0.4339** | FIAT, RAM, SURVIVOR, CATFISH                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (57.1%, no-rel 19.0%)]
   - Group 15: **0.4217** | SLAM, ALONE, BACHELOR, CHOPPED                                    | INCORRECT (Max overlap: 2/4 with REALITY SHOWS)
   - Group 16: **0.3624** | LILY, MOUSE, JAGUAR, MINI                                         | INCORRECT (Max overlap: 2/4 with ___ PAD) | [Pred Type: NAMED_ENTITY_SET (50.8%, no-rel 10.1%)]
   - Group 17: **0.4110** | SLAM, ALONE, KNOCK, CHOPPED                                       | INCORRECT (Max overlap: 2/4 with CRITICIZE)
   - Group 18: **0.3384** | PAN, ROAST, MAXI, MINI                                            | INCORRECT (Max overlap: 2/4 with CRITICIZE) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 22.3%)]
   - Group 19: **0.3587** | FIAT, LILY, JAGUAR, MINI                                          | INCORRECT (Max overlap: 3/4 with CAR BRANDS) | [Pred Type: NAMED_ENTITY_SET (57.1%, no-rel 9.4%)]
   - Group 20: **0.4359** | FIAT, LILY, BACHELOR, JAGUAR                                      | INCORRECT (Max overlap: 2/4 with CAR BRANDS)

---

## Puzzle 50 (ID: 943)
**Words on Board:** MOLE, DESKTOP, MOBILE, HOSE, TUBE, PIPE, JET, APP, DIP, VOLT, BAR, GRAM, STRAW, SPLIT, BOOK, WEB

### Ground Truth Categories:
* **Level 0 (HOLLOW CYLINDERS) [Type: SEMANTIC_SET]:** HOSE, PIPE, STRAW, TUBE
* **Level 1 (SOFTWARE PLATFORMS) [Type: SEMANTIC_SET]:** APP, DESKTOP, MOBILE, WEB
* **Level 2 (TAKE OFF) [Type: SYNONYM_OR_NEAR]:** BOOK, DIP, JET, SPLIT
* **Level 3 (UNITS OF MEASURE) [Type: SEMANTIC_SET]:** BAR, GRAM, MOLE, VOLT

### Top Candidate Partitions:
1. **Partition Score: 0.4026**
   - Group 1: **0.7298** | HOSE, TUBE, PIPE, STRAW                                           | CORRECT GROUP (HOLLOW CYLINDERS, Level 0)
   - Group 2: **0.5289** | DESKTOP, MOBILE, APP, WEB                                         | CORRECT GROUP (SOFTWARE PLATFORMS, Level 1)
   - Group 3: **0.3836** | MOLE, DIP, VOLT, GRAM                                             | INCORRECT (Max overlap: 3/4 with UNITS OF MEASURE)
   - Group 4: **0.3489** | JET, BAR, SPLIT, BOOK                                             | INCORRECT (Max overlap: 3/4 with TAKE OFF)
2. **Partition Score: 0.3930**
   - Group 1: **0.7298** | HOSE, TUBE, PIPE, STRAW                                           | CORRECT GROUP (HOLLOW CYLINDERS, Level 0)
   - Group 2: **0.5906** | MOBILE, APP, BOOK, WEB                                            | INCORRECT (Max overlap: 3/4 with SOFTWARE PLATFORMS) | [Pred Type: FILL_IN_THE_BLANK (49.9%, no-rel 22.2%)]
   - Group 3: **0.3297** | DESKTOP, VOLT, GRAM, SPLIT                                        | INCORRECT (Max overlap: 2/4 with UNITS OF MEASURE)
   - Group 4: **0.3258** | MOLE, JET, DIP, BAR                                               | INCORRECT (Max overlap: 2/4 with UNITS OF MEASURE)
3. **Partition Score: 0.3925**
   - Group 1: **0.7298** | HOSE, TUBE, PIPE, STRAW                                           | CORRECT GROUP (HOLLOW CYLINDERS, Level 0)
   - Group 2: **0.4075** | MOBILE, BAR, BOOK, WEB                                            | INCORRECT (Max overlap: 2/4 with SOFTWARE PLATFORMS) | [Pred Type: FILL_IN_THE_BLANK (55.1%, no-rel 13.4%)]
   - Group 3: **0.3942** | DESKTOP, APP, VOLT, GRAM                                          | INCORRECT (Max overlap: 2/4 with SOFTWARE PLATFORMS)
   - Group 4: **0.3840** | MOLE, JET, DIP, SPLIT                                             | INCORRECT (Max overlap: 3/4 with TAKE OFF)
4. **Partition Score: 0.3860**
   - Group 1: **0.7298** | HOSE, TUBE, PIPE, STRAW                                           | CORRECT GROUP (HOLLOW CYLINDERS, Level 0)
   - Group 2: **0.4656** | DESKTOP, APP, BOOK, WEB                                           | INCORRECT (Max overlap: 3/4 with SOFTWARE PLATFORMS)
   - Group 3: **0.3666** | JET, DIP, BAR, SPLIT                                              | INCORRECT (Max overlap: 3/4 with TAKE OFF)
   - Group 4: **0.3560** | MOLE, MOBILE, VOLT, GRAM                                          | INCORRECT (Max overlap: 3/4 with UNITS OF MEASURE)
5. **Partition Score: 0.3857**
   - Group 1: **0.7298** | HOSE, TUBE, PIPE, STRAW                                           | CORRECT GROUP (HOLLOW CYLINDERS, Level 0)
   - Group 2: **0.5289** | DESKTOP, MOBILE, APP, WEB                                         | CORRECT GROUP (SOFTWARE PLATFORMS, Level 1)
   - Group 3: **0.3519** | MOLE, DIP, GRAM, SPLIT                                            | INCORRECT (Max overlap: 2/4 with UNITS OF MEASURE)
   - Group 4: **0.3309** | JET, VOLT, BAR, BOOK                                              | INCORRECT (Max overlap: 2/4 with TAKE OFF)

### Top Candidate Groups:
   - Group 1: **0.7298** | HOSE, TUBE, PIPE, STRAW                                           | CORRECT GROUP (HOLLOW CYLINDERS, Level 0)
   - Group 2: **0.5289** | DESKTOP, MOBILE, APP, WEB                                         | CORRECT GROUP (SOFTWARE PLATFORMS, Level 1)
   - Group 3: **0.3836** | MOLE, DIP, VOLT, GRAM                                             | INCORRECT (Max overlap: 3/4 with UNITS OF MEASURE)
   - Group 4: **0.3489** | JET, BAR, SPLIT, BOOK                                             | INCORRECT (Max overlap: 3/4 with TAKE OFF)
   - Group 5: **0.5906** | MOBILE, APP, BOOK, WEB                                            | INCORRECT (Max overlap: 3/4 with SOFTWARE PLATFORMS) | [Pred Type: FILL_IN_THE_BLANK (49.9%, no-rel 22.2%)]
   - Group 6: **0.3297** | DESKTOP, VOLT, GRAM, SPLIT                                        | INCORRECT (Max overlap: 2/4 with UNITS OF MEASURE)
   - Group 7: **0.3258** | MOLE, JET, DIP, BAR                                               | INCORRECT (Max overlap: 2/4 with UNITS OF MEASURE)
   - Group 8: **0.4075** | MOBILE, BAR, BOOK, WEB                                            | INCORRECT (Max overlap: 2/4 with SOFTWARE PLATFORMS) | [Pred Type: FILL_IN_THE_BLANK (55.1%, no-rel 13.4%)]
   - Group 9: **0.3942** | DESKTOP, APP, VOLT, GRAM                                          | INCORRECT (Max overlap: 2/4 with SOFTWARE PLATFORMS)
   - Group 10: **0.3840** | MOLE, JET, DIP, SPLIT                                             | INCORRECT (Max overlap: 3/4 with TAKE OFF)
   - Group 11: **0.4656** | DESKTOP, APP, BOOK, WEB                                           | INCORRECT (Max overlap: 3/4 with SOFTWARE PLATFORMS)
   - Group 12: **0.3666** | JET, DIP, BAR, SPLIT                                              | INCORRECT (Max overlap: 3/4 with TAKE OFF)
   - Group 13: **0.3560** | MOLE, MOBILE, VOLT, GRAM                                          | INCORRECT (Max overlap: 3/4 with UNITS OF MEASURE)
   - Group 14: **0.3519** | MOLE, DIP, GRAM, SPLIT                                            | INCORRECT (Max overlap: 2/4 with UNITS OF MEASURE)
   - Group 15: **0.3309** | JET, VOLT, BAR, BOOK                                              | INCORRECT (Max overlap: 2/4 with TAKE OFF)
   - Group 16: **0.5314** | DESKTOP, MOBILE, APP, VOLT                                        | INCORRECT (Max overlap: 3/4 with SOFTWARE PLATFORMS)
   - Group 17: **0.3273** | JET, BAR, BOOK, WEB                                               | INCORRECT (Max overlap: 2/4 with TAKE OFF) | [Pred Type: FILL_IN_THE_BLANK (47.5%, no-rel 17.3%)]
   - Group 18: **0.3425** | MOBILE, JET, BAR, SPLIT                                           | INCORRECT (Max overlap: 2/4 with TAKE OFF)
   - Group 19: **0.3190** | MOLE, VOLT, GRAM, BOOK                                            | INCORRECT (Max overlap: 3/4 with UNITS OF MEASURE)
   - Group 20: **0.4614** | DESKTOP, MOBILE, BOOK, WEB                                        | INCORRECT (Max overlap: 3/4 with SOFTWARE PLATFORMS)

---

## Puzzle 51 (ID: 383)
**Words on Board:** CUE, PROMPT, SHORT, DRAWER, WORD, CLUTCH, LICENSE, BRIEF, FREEDOM, LATITUDE, SIGNAL, MESSENGER, SLACK, TOTE, SATCHEL, BOXER

### Ground Truth Categories:
* **Level 0 (TYPES OF BAGS) [Type: SEMANTIC_SET]:** CLUTCH, MESSENGER, SATCHEL, TOTE
* **Level 1 (WIGGLE ROOM) [Type: SYNONYM_OR_NEAR]:** FREEDOM, LATITUDE, LICENSE, SLACK
* **Level 2 (INDICATION TO PROCEED) [Type: SYNONYM_OR_NEAR]:** CUE, PROMPT, SIGNAL, WORD
* **Level 3 (UNDERWEAR IN THE SINGULAR) [Type: WORDPLAY_TRANSFORM]:** BOXER, BRIEF, DRAWER, SHORT

### Top Candidate Partitions:
1. **Partition Score: 0.3926**
   - Group 1: **0.5586** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.4522** | CUE, PROMPT, SHORT, BRIEF                                         | INCORRECT (Max overlap: 2/4 with INDICATION TO PROCEED) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 31.9%)]
   - Group 3: **0.4121** | CLUTCH, LICENSE, FREEDOM, LATITUDE                                | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 30.4%)]
   - Group 4: **0.3532** | WORD, SIGNAL, MESSENGER, SLACK                                    | INCORRECT (Max overlap: 2/4 with INDICATION TO PROCEED)
2. **Partition Score: 0.3857**
   - Group 1: **0.5586** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.4812** | CUE, PROMPT, CLUTCH, SIGNAL                                       | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 34.7%)]
   - Group 3: **0.3733** | WORD, LATITUDE, MESSENGER, SLACK                                  | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 4: **0.3441** | SHORT, LICENSE, BRIEF, FREEDOM                                    | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 29.4%)]
3. **Partition Score: 0.3845**
   - Group 1: **0.5586** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.4824** | CUE, PROMPT, SHORT, SIGNAL                                        | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 30.5%)]
   - Group 3: **0.3733** | WORD, LATITUDE, MESSENGER, SLACK                                  | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 4: **0.3412** | CLUTCH, LICENSE, BRIEF, FREEDOM                                   | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
4. **Partition Score: 0.3833**
   - Group 1: **0.5586** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.4824** | CUE, PROMPT, SHORT, SIGNAL                                        | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 30.5%)]
   - Group 3: **0.4334** | LICENSE, BRIEF, FREEDOM, LATITUDE                                 | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 26.3%)]
   - Group 4: **0.3087** | WORD, CLUTCH, MESSENGER, SLACK                                    | INCORRECT (Max overlap: 2/4 with TYPES OF BAGS)
5. **Partition Score: 0.3808**
   - Group 1: **0.5101** | DRAWER, MESSENGER, SATCHEL, BOXER                                 | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.4824** | CUE, PROMPT, SHORT, SIGNAL                                        | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 30.5%)]
   - Group 3: **0.4334** | LICENSE, BRIEF, FREEDOM, LATITUDE                                 | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 26.3%)]
   - Group 4: **0.3037** | WORD, CLUTCH, SLACK, TOTE                                         | INCORRECT (Max overlap: 2/4 with TYPES OF BAGS)

### Top Candidate Groups:
   - Group 1: **0.5586** | DRAWER, TOTE, SATCHEL, BOXER                                      | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 2: **0.4522** | CUE, PROMPT, SHORT, BRIEF                                         | INCORRECT (Max overlap: 2/4 with INDICATION TO PROCEED) | [Pred Type: SYNONYM_OR_NEAR (56.6%, no-rel 31.9%)]
   - Group 3: **0.4121** | CLUTCH, LICENSE, FREEDOM, LATITUDE                                | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM) | [Pred Type: SYNONYM_OR_NEAR (48.8%, no-rel 30.4%)]
   - Group 4: **0.3532** | WORD, SIGNAL, MESSENGER, SLACK                                    | INCORRECT (Max overlap: 2/4 with INDICATION TO PROCEED)
   - Group 5: **0.4812** | CUE, PROMPT, CLUTCH, SIGNAL                                       | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED) | [Pred Type: SYNONYM_OR_NEAR (54.4%, no-rel 34.7%)]
   - Group 6: **0.3733** | WORD, LATITUDE, MESSENGER, SLACK                                  | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 7: **0.3441** | SHORT, LICENSE, BRIEF, FREEDOM                                    | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 29.4%)]
   - Group 8: **0.4824** | CUE, PROMPT, SHORT, SIGNAL                                        | INCORRECT (Max overlap: 3/4 with INDICATION TO PROCEED) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 30.5%)]
   - Group 9: **0.3412** | CLUTCH, LICENSE, BRIEF, FREEDOM                                   | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 10: **0.4334** | LICENSE, BRIEF, FREEDOM, LATITUDE                                 | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 26.3%)]
   - Group 11: **0.3087** | WORD, CLUTCH, MESSENGER, SLACK                                    | INCORRECT (Max overlap: 2/4 with TYPES OF BAGS)
   - Group 12: **0.5101** | DRAWER, MESSENGER, SATCHEL, BOXER                                 | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 13: **0.3037** | WORD, CLUTCH, SLACK, TOTE                                         | INCORRECT (Max overlap: 2/4 with TYPES OF BAGS)
   - Group 14: **0.3678** | LICENSE, FREEDOM, LATITUDE, MESSENGER                             | INCORRECT (Max overlap: 3/4 with WIGGLE ROOM) | [Pred Type: SYNONYM_OR_NEAR (52.4%, no-rel 20.9%)]
   - Group 15: **0.3464** | WORD, CLUTCH, SIGNAL, SLACK                                       | INCORRECT (Max overlap: 2/4 with INDICATION TO PROCEED)
   - Group 16: **0.3366** | WORD, LATITUDE, SLACK, TOTE                                       | INCORRECT (Max overlap: 2/4 with WIGGLE ROOM)
   - Group 17: **0.4347** | MESSENGER, TOTE, SATCHEL, BOXER                                   | INCORRECT (Max overlap: 3/4 with TYPES OF BAGS)
   - Group 18: **0.3141** | DRAWER, WORD, CLUTCH, SLACK                                       | INCORRECT (Max overlap: 1/4 with UNDERWEAR IN THE SINGULAR)
   - Group 19: **0.4750** | DRAWER, MESSENGER, TOTE, BOXER                                    | INCORRECT (Max overlap: 2/4 with UNDERWEAR IN THE SINGULAR)
   - Group 20: **0.2919** | WORD, CLUTCH, SLACK, SATCHEL                                      | INCORRECT (Max overlap: 2/4 with TYPES OF BAGS)

---

## Puzzle 52 (ID: 982)
**Words on Board:** EGGS, STU, POLYESTER SUIT, SEER, JOHN TRAVOLTA, SHOVEL, BASKET, DISCO, PLATFORM SHOES, BOYLE, BELLOWS, TONGS, DYE, POKER, BRAYS, PEEPS

### Ground Truth Categories:
* **Level 0 (EASTER SUPPLIES) [Type: SEMANTIC_SET]:** BASKET, DYE, EGGS, PEEPS
* **Level 1 (FIREPLACE ACCESSORIES) [Type: SEMANTIC_SET]:** BELLOWS, POKER, SHOVEL, TONGS
* **Level 2 (ELEMENTS OF "SATURDAY NIGHT FEVER") [Type: NAMED_ENTITY_SET]:** DISCO, JOHN TRAVOLTA, PLATFORM SHOES, POLYESTER SUIT
* **Level 3 (HOMOPHONES OF WAYS TO COOK SOMETHING) [Type: SOUND_OR_SPELLING]:** BOYLE, BRAYS, SEER, STU

### Top Candidate Partitions:
1. **Partition Score: 0.4087**
   - Group 1: **0.5093** | STU, POLYESTER SUIT, JOHN TRAVOLTA, PLATFORM SHOES                | INCORRECT (Max overlap: 3/4 with ELEMENTS OF "SATURDAY NIGHT FEVER")
   - Group 2: **0.4830** | BOYLE, BELLOWS, BRAYS, PEEPS                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING) | [Pred Type: SYNONYM_OR_NEAR (46.0%, no-rel 16.6%)]
   - Group 3: **0.4203** | SHOVEL, BASKET, TONGS, POKER                                      | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES) | [Pred Type: SEMANTIC_SET (61.4%, no-rel 20.8%)]
   - Group 4: **0.3657** | EGGS, SEER, DISCO, DYE                                            | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
2. **Partition Score: 0.4076**
   - Group 1: **0.5093** | STU, POLYESTER SUIT, JOHN TRAVOLTA, PLATFORM SHOES                | INCORRECT (Max overlap: 3/4 with ELEMENTS OF "SATURDAY NIGHT FEVER")
   - Group 2: **0.4203** | SHOVEL, BASKET, TONGS, POKER                                      | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES) | [Pred Type: SEMANTIC_SET (61.4%, no-rel 20.8%)]
   - Group 3: **0.4118** | EGGS, DISCO, BELLOWS, DYE                                         | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES) | [Pred Type: SEMANTIC_SET (53.6%, no-rel 19.3%)]
   - Group 4: **0.3991** | SEER, BOYLE, BRAYS, PEEPS                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
3. **Partition Score: 0.4074**
   - Group 1: **0.5093** | STU, POLYESTER SUIT, JOHN TRAVOLTA, PLATFORM SHOES                | INCORRECT (Max overlap: 3/4 with ELEMENTS OF "SATURDAY NIGHT FEVER")
   - Group 2: **0.4203** | SHOVEL, BASKET, TONGS, POKER                                      | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES) | [Pred Type: SEMANTIC_SET (61.4%, no-rel 20.8%)]
   - Group 3: **0.4097** | SEER, BOYLE, BELLOWS, PEEPS                                       | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 4: **0.3997** | EGGS, DISCO, DYE, BRAYS                                           | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES) | [Pred Type: SEMANTIC_SET (54.5%, no-rel 18.3%)]
4. **Partition Score: 0.4056**
   - Group 1: **0.5393** | DISCO, BELLOWS, BRAYS, PEEPS                                      | INCORRECT (Max overlap: 1/4 with ELEMENTS OF "SATURDAY NIGHT FEVER") | [Pred Type: SYNONYM_OR_NEAR (46.8%, no-rel 26.6%)]
   - Group 2: **0.5093** | STU, POLYESTER SUIT, JOHN TRAVOLTA, PLATFORM SHOES                | INCORRECT (Max overlap: 3/4 with ELEMENTS OF "SATURDAY NIGHT FEVER")
   - Group 3: **0.4203** | SHOVEL, BASKET, TONGS, POKER                                      | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES) | [Pred Type: SEMANTIC_SET (61.4%, no-rel 20.8%)]
   - Group 4: **0.3464** | EGGS, SEER, BOYLE, DYE                                            | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
5. **Partition Score: 0.3966**
   - Group 1: **0.5093** | STU, POLYESTER SUIT, JOHN TRAVOLTA, PLATFORM SHOES                | INCORRECT (Max overlap: 3/4 with ELEMENTS OF "SATURDAY NIGHT FEVER")
   - Group 2: **0.4203** | SHOVEL, BASKET, TONGS, POKER                                      | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES) | [Pred Type: SEMANTIC_SET (61.4%, no-rel 20.8%)]
   - Group 3: **0.4104** | SEER, DISCO, BRAYS, PEEPS                                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 24.5%)]
   - Group 4: **0.3778** | EGGS, BOYLE, BELLOWS, DYE                                         | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)

### Top Candidate Groups:
   - Group 1: **0.5093** | STU, POLYESTER SUIT, JOHN TRAVOLTA, PLATFORM SHOES                | INCORRECT (Max overlap: 3/4 with ELEMENTS OF "SATURDAY NIGHT FEVER")
   - Group 2: **0.4830** | BOYLE, BELLOWS, BRAYS, PEEPS                                      | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING) | [Pred Type: SYNONYM_OR_NEAR (46.0%, no-rel 16.6%)]
   - Group 3: **0.4203** | SHOVEL, BASKET, TONGS, POKER                                      | INCORRECT (Max overlap: 3/4 with FIREPLACE ACCESSORIES) | [Pred Type: SEMANTIC_SET (61.4%, no-rel 20.8%)]
   - Group 4: **0.3657** | EGGS, SEER, DISCO, DYE                                            | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 5: **0.4118** | EGGS, DISCO, BELLOWS, DYE                                         | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES) | [Pred Type: SEMANTIC_SET (53.6%, no-rel 19.3%)]
   - Group 6: **0.3991** | SEER, BOYLE, BRAYS, PEEPS                                         | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 7: **0.4097** | SEER, BOYLE, BELLOWS, PEEPS                                       | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 8: **0.3997** | EGGS, DISCO, DYE, BRAYS                                           | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES) | [Pred Type: SEMANTIC_SET (54.5%, no-rel 18.3%)]
   - Group 9: **0.5393** | DISCO, BELLOWS, BRAYS, PEEPS                                      | INCORRECT (Max overlap: 1/4 with ELEMENTS OF "SATURDAY NIGHT FEVER") | [Pred Type: SYNONYM_OR_NEAR (46.8%, no-rel 26.6%)]
   - Group 10: **0.3464** | EGGS, SEER, BOYLE, DYE                                            | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 11: **0.4104** | SEER, DISCO, BRAYS, PEEPS                                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING) | [Pred Type: SYNONYM_OR_NEAR (50.2%, no-rel 24.5%)]
   - Group 12: **0.3778** | EGGS, BOYLE, BELLOWS, DYE                                         | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 13: **0.4544** | EGGS, BELLOWS, BRAYS, PEEPS                                       | INCORRECT (Max overlap: 2/4 with EASTER SUPPLIES)
   - Group 14: **0.3903** | POLYESTER SUIT, JOHN TRAVOLTA, DISCO, PLATFORM SHOES              | CORRECT GROUP (ELEMENTS OF "SATURDAY NIGHT FEVER", Level 2) | [Pred Type: SEMANTIC_SET (45.2%, no-rel 13.9%)]
   - Group 15: **0.3856** | STU, SEER, BOYLE, DYE                                             | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 16: **0.5344** | BELLOWS, TONGS, BRAYS, PEEPS                                      | INCORRECT (Max overlap: 2/4 with FIREPLACE ACCESSORIES)
   - Group 17: **0.3750** | SHOVEL, BASKET, DISCO, POKER                                      | INCORRECT (Max overlap: 2/4 with FIREPLACE ACCESSORIES) | [Pred Type: SEMANTIC_SET (53.8%, no-rel 23.7%)]
   - Group 18: **0.5075** | STU, POLYESTER SUIT, JOHN TRAVOLTA, BOYLE                         | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO COOK SOMETHING)
   - Group 19: **0.4091** | PLATFORM SHOES, BELLOWS, BRAYS, PEEPS                             | INCORRECT (Max overlap: 1/4 with ELEMENTS OF "SATURDAY NIGHT FEVER")
   - Group 20: **0.4090** | SEER, DISCO, BELLOWS, PEEPS                                       | INCORRECT (Max overlap: 1/4 with HOMOPHONES OF WAYS TO COOK SOMETHING) | [Pred Type: SYNONYM_OR_NEAR (48.3%, no-rel 25.1%)]

---

## Puzzle 53 (ID: 204)
**Words on Board:** WHOA, PYRAMID, WHEEL, WHY, CAESAR, FEUD, PLANT, GREEK, WEDGE, GREEN, WATER, WEED, MILLIONAIRE, SEED, WEE, WAY

### Ground Truth Categories:
* **Level 0 (GARDENING NOUNS/VERBS) [Type: SEMANTIC_SET]:** PLANT, SEED, WATER, WEED
* **Level 1 (KINDS OF SALADS) [Type: NAMED_ENTITY_SET]:** CAESAR, GREEK, GREEN, WEDGE
* **Level 2 (CLASSIC GAME SHOWS, FAMILIARLY) [Type: NAMED_ENTITY_SET]:** FEUD, MILLIONAIRE, PYRAMID, WHEEL
* **Level 3 (W + VOWEL SOUND) [Type: SOUND_OR_SPELLING]:** WAY, WEE, WHY, WHOA

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6816** | WHOA, CAESAR, FEUD, GREEK                                         | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS) | [Pred Type: SOUND_OR_SPELLING (47.3%, no-rel 5.8%)]
   - Group 2: **0.6643** | WHOA, WHY, CAESAR, FEUD                                           | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (57.5%, no-rel 7.7%)]
   - Group 3: **0.6365** | WHOA, WHY, FEUD, GREEK                                            | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (53.2%, no-rel 7.0%)]
   - Group 4: **0.6268** | WHY, CAESAR, FEUD, GREEK                                          | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS) | [Pred Type: SOUND_OR_SPELLING (48.0%, no-rel 5.2%)]
   - Group 5: **0.6235** | WHOA, WHY, FEUD, WAY                                              | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (55.4%, no-rel 10.7%)]
   - Group 6: **0.6179** | WHOA, CAESAR, FEUD, MILLIONAIRE                                   | INCORRECT (Max overlap: 2/4 with CLASSIC GAME SHOWS, FAMILIARLY)
   - Group 7: **0.6116** | WHOA, WHY, CAESAR, GREEK                                          | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (62.0%, no-rel 3.9%)]
   - Group 8: **0.6039** | WHOA, WHY, WEE, WAY                                               | CORRECT GROUP (W + VOWEL SOUND, Level 3) | [Pred Type: SOUND_OR_SPELLING (64.3%, no-rel 7.9%)]
   - Group 9: **0.5935** | WHOA, FEUD, GREEK, WAY                                            | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (46.6%, no-rel 9.5%)]
   - Group 10: **0.5878** | WHOA, WHY, FEUD, WEE                                              | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (61.6%, no-rel 9.1%)]
   - Group 11: **0.5820** | WHOA, GREEK, WEE, WAY                                             | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (50.8%, no-rel 8.6%)]
   - Group 12: **0.5794** | WHOA, WHY, GREEK, WAY                                             | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (56.5%, no-rel 6.8%)]
   - Group 13: **0.5722** | WHOA, WHY, GREEK, WEE                                             | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (61.3%, no-rel 5.4%)]
   - Group 14: **0.5721** | WHOA, FEUD, GREEK, WEE                                            | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (55.3%, no-rel 6.4%)]
   - Group 15: **0.5720** | WHY, GREEK, WEE, WAY                                              | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (45.3%, no-rel 11.5%)]
   - Group 16: **0.5690** | WHY, FEUD, WEE, WAY                                               | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (52.8%, no-rel 11.6%)]
   - Group 17: **0.5679** | CAESAR, FEUD, GREEK, MILLIONAIRE                                  | INCORRECT (Max overlap: 2/4 with KINDS OF SALADS) | [Pred Type: WORDPLAY_TRANSFORM (45.3%, no-rel 7.5%)]
   - Group 18: **0.5661** | WHY, FEUD, GREEK, WAY                                             | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND)
   - Group 19: **0.5656** | WHY, FEUD, GREEK, WEE                                             | INCORRECT (Max overlap: 2/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (53.0%, no-rel 6.9%)]
   - Group 20: **0.5598** | WHOA, FEUD, WEE, WAY                                              | INCORRECT (Max overlap: 3/4 with W + VOWEL SOUND) | [Pred Type: SOUND_OR_SPELLING (56.7%, no-rel 9.8%)]

---

## Puzzle 54 (ID: 624)
**Words on Board:** SWALLOW, SHINE, GULP, CHINA, GIVE, ANCHOR, SCARF, BUCKLE, MERMAID, COMPASS, BOW, BUTTE, WOLF, GOBBLE, HEARTH, CAVE

### Ground Truth Categories:
* **Level 0 (EAT VORACIOUSLY) [Type: SYNONYM_OR_NEAR]:** GOBBLE, GULP, SCARF, WOLF
* **Level 1 (BEND UNDER PRESSURE) [Type: SYNONYM_OR_NEAR]:** BOW, BUCKLE, CAVE, GIVE
* **Level 2 (CLASSIC NAUTICAL TATTOOS) [Type: NAMED_ENTITY_SET]:** ANCHOR, COMPASS, MERMAID, SWALLOW
* **Level 3 (BODY PARTS PLUS LETTER) [Type: WORDPLAY_TRANSFORM]:** BUTTE, CHINA, HEARTH, SHINE

### Top Candidate Partitions:
1. **Partition Score: 0.4558**
   - Group 1: **0.6113** | CHINA, MERMAID, HEARTH, CAVE                                      | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 2: **0.5671** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 32.9%)]
   - Group 3: **0.4295** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.4133** | ANCHOR, COMPASS, BOW, BUTTE                                       | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS) | [Pred Type: SEMANTIC_SET (45.5%, no-rel 19.7%)]
2. **Partition Score: 0.4543**
   - Group 1: **0.5671** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 32.9%)]
   - Group 2: **0.4797** | CHINA, MERMAID, BUTTE, HEARTH                                     | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 3: **0.4786** | ANCHOR, COMPASS, BOW, CAVE                                        | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 4: **0.4295** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
3. **Partition Score: 0.4521**
   - Group 1: **0.5671** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 32.9%)]
   - Group 2: **0.5453** | MERMAID, BUTTE, HEARTH, CAVE                                      | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 3: **0.4295** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.4167** | CHINA, ANCHOR, COMPASS, BOW                                       | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
4. **Partition Score: 0.4488**
   - Group 1: **0.5671** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 32.9%)]
   - Group 2: **0.5471** | CHINA, BUTTE, HEARTH, CAVE                                        | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 3: **0.4295** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.4094** | ANCHOR, MERMAID, COMPASS, BOW                                     | INCORRECT (Max overlap: 3/4 with CLASSIC NAUTICAL TATTOOS)
5. **Partition Score: 0.4433**
   - Group 1: **0.5671** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 32.9%)]
   - Group 2: **0.4889** | CHINA, MERMAID, BUTTE, CAVE                                       | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 3: **0.4295** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.4273** | ANCHOR, COMPASS, BOW, HEARTH                                      | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)

### Top Candidate Groups:
   - Group 1: **0.6113** | CHINA, MERMAID, HEARTH, CAVE                                      | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 2: **0.5671** | SWALLOW, GULP, WOLF, GOBBLE                                       | INCORRECT (Max overlap: 3/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.8%, no-rel 32.9%)]
   - Group 3: **0.4295** | SHINE, GIVE, SCARF, BUCKLE                                        | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 4: **0.4133** | ANCHOR, COMPASS, BOW, BUTTE                                       | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS) | [Pred Type: SEMANTIC_SET (45.5%, no-rel 19.7%)]
   - Group 5: **0.4797** | CHINA, MERMAID, BUTTE, HEARTH                                     | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 6: **0.4786** | ANCHOR, COMPASS, BOW, CAVE                                        | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 7: **0.5453** | MERMAID, BUTTE, HEARTH, CAVE                                      | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 8: **0.4167** | CHINA, ANCHOR, COMPASS, BOW                                       | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 9: **0.5471** | CHINA, BUTTE, HEARTH, CAVE                                        | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 10: **0.4094** | ANCHOR, MERMAID, COMPASS, BOW                                     | INCORRECT (Max overlap: 3/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 11: **0.4889** | CHINA, MERMAID, BUTTE, CAVE                                       | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 12: **0.4273** | ANCHOR, COMPASS, BOW, HEARTH                                      | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 13: **0.5682** | CHINA, MERMAID, COMPASS, HEARTH                                   | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)
   - Group 14: **0.3609** | ANCHOR, BOW, BUTTE, CAVE                                          | INCORRECT (Max overlap: 2/4 with BEND UNDER PRESSURE)
   - Group 15: **0.4230** | SHINE, SCARF, BUCKLE, GOBBLE                                      | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY)
   - Group 16: **0.4064** | SWALLOW, GULP, GIVE, WOLF                                         | INCORRECT (Max overlap: 2/4 with EAT VORACIOUSLY) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 32.8%)]
   - Group 17: **0.4743** | CHINA, BOW, BUTTE, HEARTH                                         | INCORRECT (Max overlap: 3/4 with BODY PARTS PLUS LETTER)
   - Group 18: **0.3971** | ANCHOR, MERMAID, COMPASS, CAVE                                    | INCORRECT (Max overlap: 3/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 19: **0.5673** | CHINA, MERMAID, COMPASS, CAVE                                     | INCORRECT (Max overlap: 2/4 with CLASSIC NAUTICAL TATTOOS)
   - Group 20: **0.3347** | ANCHOR, BOW, BUTTE, HEARTH                                        | INCORRECT (Max overlap: 2/4 with BODY PARTS PLUS LETTER)

---

## Puzzle 55 (ID: 941)
**Words on Board:** TINGLE, GOOSEBUMP, SPEED, JAYWALK, SHIVER, DOVETAIL, CROWBAR, CHILL, LITTER, AEROPLANE, SCISSORS, MARSALA, LOITER, HEATHERS, CLOTHESPIN, SEESAW

### Ground Truth Categories:
* **Level 0 (BIT OF A RESPONSE TO STRONG EMOTIONS) [Type: SYNONYM_OR_NEAR]:** CHILL, GOOSEBUMP, SHIVER, TINGLE
* **Level 1 (BREAK THE RULES) [Type: SYNONYM_OR_NEAR]:** JAYWALK, LITTER, LOITER, SPEED
* **Level 2 (FIRST-CLASS LEVERS) [Type: SEMANTIC_SET]:** CLOTHESPIN, CROWBAR, SCISSORS, SEESAW
* **Level 3 (STARTING WITH CANDY BARS) [Type: WORD_FORM]:** AEROPLANE, DOVETAIL, HEATHERS, MARSALA

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.7641** | TINGLE, GOOSEBUMP, SHIVER, CHILL                                  | CORRECT GROUP (BIT OF A RESPONSE TO STRONG EMOTIONS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 38.9%)]
   - Group 2: **0.6469** | CROWBAR, SCISSORS, CLOTHESPIN, SEESAW                             | CORRECT GROUP (FIRST-CLASS LEVERS, Level 2) | [Pred Type: SEMANTIC_SET (56.6%, no-rel 25.0%)]
   - Group 3: **0.6345** | JAYWALK, DOVETAIL, MARSALA, HEATHERS                              | INCORRECT (Max overlap: 3/4 with STARTING WITH CANDY BARS)
   - Group 4: **0.6272** | JAYWALK, AEROPLANE, MARSALA, HEATHERS                             | INCORRECT (Max overlap: 3/4 with STARTING WITH CANDY BARS)
   - Group 5: **0.6180** | CROWBAR, AEROPLANE, SCISSORS, SEESAW                              | INCORRECT (Max overlap: 3/4 with FIRST-CLASS LEVERS) | [Pred Type: SEMANTIC_SET (47.6%, no-rel 26.4%)]
   - Group 6: **0.6151** | JAYWALK, DOVETAIL, HEATHERS, SEESAW                               | INCORRECT (Max overlap: 2/4 with STARTING WITH CANDY BARS)
   - Group 7: **0.6083** | JAYWALK, DOVETAIL, AEROPLANE, HEATHERS                            | INCORRECT (Max overlap: 3/4 with STARTING WITH CANDY BARS)
   - Group 8: **0.6083** | TINGLE, SHIVER, CHILL, LOITER                                     | INCORRECT (Max overlap: 3/4 with BIT OF A RESPONSE TO STRONG EMOTIONS)
   - Group 9: **0.6060** | JAYWALK, DOVETAIL, AEROPLANE, MARSALA                             | INCORRECT (Max overlap: 3/4 with STARTING WITH CANDY BARS)
   - Group 10: **0.6022** | CROWBAR, AEROPLANE, SCISSORS, CLOTHESPIN                          | INCORRECT (Max overlap: 3/4 with FIRST-CLASS LEVERS) | [Pred Type: SEMANTIC_SET (52.7%, no-rel 29.4%)]
   - Group 11: **0.6008** | DOVETAIL, AEROPLANE, MARSALA, HEATHERS                            | CORRECT GROUP (STARTING WITH CANDY BARS, Level 3)
   - Group 12: **0.5938** | JAYWALK, DOVETAIL, AEROPLANE, SEESAW                              | INCORRECT (Max overlap: 2/4 with STARTING WITH CANDY BARS)
   - Group 13: **0.5883** | CROWBAR, AEROPLANE, CLOTHESPIN, SEESAW                            | INCORRECT (Max overlap: 3/4 with FIRST-CLASS LEVERS) | [Pred Type: SEMANTIC_SET (46.0%, no-rel 29.6%)]
   - Group 14: **0.5869** | JAYWALK, AEROPLANE, HEATHERS, SEESAW                              | INCORRECT (Max overlap: 2/4 with STARTING WITH CANDY BARS)
   - Group 15: **0.5853** | JAYWALK, MARSALA, HEATHERS, SEESAW                                | INCORRECT (Max overlap: 2/4 with STARTING WITH CANDY BARS)
   - Group 16: **0.5827** | DOVETAIL, AEROPLANE, HEATHERS, SEESAW                             | INCORRECT (Max overlap: 3/4 with STARTING WITH CANDY BARS)
   - Group 17: **0.5805** | JAYWALK, DOVETAIL, MARSALA, SEESAW                                | INCORRECT (Max overlap: 2/4 with STARTING WITH CANDY BARS)
   - Group 18: **0.5782** | AEROPLANE, SCISSORS, CLOTHESPIN, SEESAW                           | INCORRECT (Max overlap: 3/4 with FIRST-CLASS LEVERS) | [Pred Type: SEMANTIC_SET (48.7%, no-rel 26.5%)]
   - Group 19: **0.5736** | TINGLE, SHIVER, CHILL, LITTER                                     | INCORRECT (Max overlap: 3/4 with BIT OF A RESPONSE TO STRONG EMOTIONS)
   - Group 20: **0.5715** | JAYWALK, AEROPLANE, MARSALA, SEESAW                               | INCORRECT (Max overlap: 2/4 with STARTING WITH CANDY BARS)

---

## Puzzle 56 (ID: 655)
**Words on Board:** PAPER, SWAY, PHONE, CHANGE, DING, WAVE, GREEN, CORRECT, SCRATCH, RIGHT, SCOPE, CHIP, MOVE, BINGO, TOUCH, REACH

### Ground Truth Categories:
* **Level 0 (AFFECT) [Type: SYNONYM_OR_NEAR]:** MOVE, REACH, SWAY, TOUCH
* **Level 1 (YOU GOT IT!) [Type: SYNONYM_OR_NEAR]:** BINGO, CORRECT, DING, RIGHT
* **Level 2 (SLANG FOR MONEY) [Type: SEMANTIC_SET]:** CHANGE, GREEN, PAPER, SCRATCH
* **Level 3 (OBJECTS WITH THE PREFIX “MICRO-”) [Type: FILL_IN_THE_BLANK]:** CHIP, PHONE, SCOPE, WAVE

### Top Candidate Partitions:
1. **Partition Score: 0.4113**
   - Group 1: **0.5354** | CHANGE, CORRECT, RIGHT, MOVE                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (58.1%, no-rel 31.7%)]
   - Group 2: **0.4831** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.4302** | SWAY, SCOPE, TOUCH, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 39.8%)]
   - Group 4: **0.3660** | PAPER, PHONE, WAVE, CHIP                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)
2. **Partition Score: 0.4111**
   - Group 1: **0.5484** | SWAY, CHANGE, MOVE, TOUCH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 2: **0.4831** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.4291** | CORRECT, RIGHT, SCOPE, REACH                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 34.3%)]
   - Group 4: **0.3660** | PAPER, PHONE, WAVE, CHIP                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)
3. **Partition Score: 0.4099**
   - Group 1: **0.5733** | CHANGE, CORRECT, RIGHT, TOUCH                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 31.5%)]
   - Group 2: **0.4831** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.4243** | SWAY, SCOPE, MOVE, REACH                                          | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 4: **0.3660** | PAPER, PHONE, WAVE, CHIP                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)
4. **Partition Score: 0.4098**
   - Group 1: **0.5416** | SCOPE, MOVE, TOUCH, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (54.1%, no-rel 35.8%)]
   - Group 2: **0.4831** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.4239** | SWAY, CHANGE, CORRECT, RIGHT                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 35.0%)]
   - Group 4: **0.3660** | PAPER, PHONE, WAVE, CHIP                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)
5. **Partition Score: 0.4082**
   - Group 1: **0.4831** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 2: **0.4779** | SWAY, CHANGE, RIGHT, MOVE                                         | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 3: **0.4231** | CORRECT, SCOPE, TOUCH, REACH                                      | INCORRECT (Max overlap: 2/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (52.0%, no-rel 36.8%)]
   - Group 4: **0.3660** | PAPER, PHONE, WAVE, CHIP                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)

### Top Candidate Groups:
   - Group 1: **0.5354** | CHANGE, CORRECT, RIGHT, MOVE                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (58.1%, no-rel 31.7%)]
   - Group 2: **0.4831** | DING, GREEN, SCRATCH, BINGO                                       | INCORRECT (Max overlap: 2/4 with YOU GOT IT!)
   - Group 3: **0.4302** | SWAY, SCOPE, TOUCH, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (50.4%, no-rel 39.8%)]
   - Group 4: **0.3660** | PAPER, PHONE, WAVE, CHIP                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH THE PREFIX “MICRO-”)
   - Group 5: **0.5484** | SWAY, CHANGE, MOVE, TOUCH                                         | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 6: **0.4291** | CORRECT, RIGHT, SCOPE, REACH                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 34.3%)]
   - Group 7: **0.5733** | CHANGE, CORRECT, RIGHT, TOUCH                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 31.5%)]
   - Group 8: **0.4243** | SWAY, SCOPE, MOVE, REACH                                          | INCORRECT (Max overlap: 3/4 with AFFECT)
   - Group 9: **0.5416** | SCOPE, MOVE, TOUCH, REACH                                         | INCORRECT (Max overlap: 3/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (54.1%, no-rel 35.8%)]
   - Group 10: **0.4239** | SWAY, CHANGE, CORRECT, RIGHT                                      | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (55.1%, no-rel 35.0%)]
   - Group 11: **0.4779** | SWAY, CHANGE, RIGHT, MOVE                                         | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 12: **0.4231** | CORRECT, SCOPE, TOUCH, REACH                                      | INCORRECT (Max overlap: 2/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (52.0%, no-rel 36.8%)]
   - Group 13: **0.4721** | RIGHT, SCOPE, TOUCH, REACH                                        | INCORRECT (Max overlap: 2/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 35.9%)]
   - Group 14: **0.4181** | SWAY, CHANGE, CORRECT, MOVE                                       | INCORRECT (Max overlap: 2/4 with AFFECT)
   - Group 15: **0.4786** | CHANGE, SCOPE, TOUCH, REACH                                       | INCORRECT (Max overlap: 2/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (54.8%, no-rel 33.9%)]
   - Group 16: **0.4102** | SWAY, CORRECT, RIGHT, MOVE                                        | INCORRECT (Max overlap: 2/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 39.4%)]
   - Group 17: **0.4836** | CHANGE, SCOPE, MOVE, REACH                                        | INCORRECT (Max overlap: 2/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (57.7%, no-rel 32.1%)]
   - Group 18: **0.3980** | SWAY, CORRECT, RIGHT, TOUCH                                       | INCORRECT (Max overlap: 2/4 with AFFECT) | [Pred Type: SYNONYM_OR_NEAR (50.9%, no-rel 38.2%)]
   - Group 19: **0.5643** | SWAY, MOVE, TOUCH, REACH                                          | CORRECT GROUP (AFFECT, Level 0)
   - Group 20: **0.3801** | CHANGE, CORRECT, RIGHT, SCOPE                                     | INCORRECT (Max overlap: 2/4 with YOU GOT IT!) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 32.7%)]

---

## Puzzle 57 (ID: 863)
**Words on Board:** KINGS, DOES, TACKLES, ACES, DRONES, GARAGE DOORS, TELEVISIONS, QUEENS, JACKS, ADDRESSES, BULLS, HORNETS, HANDLES, SPURS, WIIS, BUCKS

### Ground Truth Categories:
* **Level 0 (PLAYING CARDS) [Type: NAMED_ENTITY_SET]:** ACES, JACKS, KINGS, QUEENS
* **Level 1 (TAKES ON) [Type: SYNONYM_OR_NEAR]:** ADDRESSES, DOES, HANDLES, TACKLES
* **Level 2 (N.B.A. TEAMS) [Type: NAMED_ENTITY_SET]:** BUCKS, BULLS, HORNETS, SPURS
* **Level 3 (THINGS YOU CAN CONTROL WITH REMOTES) [Type: SEMANTIC_SET]:** DRONES, GARAGE DOORS, TELEVISIONS, WIIS

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6581** | KINGS, ACES, QUEENS, JACKS                                        | CORRECT GROUP (PLAYING CARDS, Level 0)
   - Group 2: **0.6330** | KINGS, BULLS, HORNETS, SPURS                                      | INCORRECT (Max overlap: 3/4 with N.B.A. TEAMS) | [Pred Type: NAMED_ENTITY_SET (55.8%, no-rel 12.5%)]
   - Group 3: **0.5947** | KINGS, ACES, BULLS, HORNETS                                       | INCORRECT (Max overlap: 2/4 with PLAYING CARDS) | [Pred Type: NAMED_ENTITY_SET (54.9%, no-rel 13.0%)]
   - Group 4: **0.5880** | KINGS, QUEENS, JACKS, HORNETS                                     | INCORRECT (Max overlap: 3/4 with PLAYING CARDS) | [Pred Type: NAMED_ENTITY_SET (46.0%, no-rel 22.7%)]
   - Group 5: **0.5862** | ACES, DRONES, BULLS, HORNETS                                      | INCORRECT (Max overlap: 2/4 with N.B.A. TEAMS) | [Pred Type: NAMED_ENTITY_SET (47.3%, no-rel 14.8%)]
   - Group 6: **0.5786** | DRONES, BULLS, HORNETS, SPURS                                     | INCORRECT (Max overlap: 3/4 with N.B.A. TEAMS) | [Pred Type: NAMED_ENTITY_SET (45.2%, no-rel 16.7%)]
   - Group 7: **0.5770** | KINGS, ACES, HORNETS, SPURS                                       | INCORRECT (Max overlap: 2/4 with PLAYING CARDS) | [Pred Type: NAMED_ENTITY_SET (50.5%, no-rel 21.7%)]
   - Group 8: **0.5767** | KINGS, ACES, BULLS, SPURS                                         | INCORRECT (Max overlap: 2/4 with PLAYING CARDS) | [Pred Type: NAMED_ENTITY_SET (46.2%, no-rel 18.5%)]
   - Group 9: **0.5752** | KINGS, QUEENS, JACKS, BUCKS                                       | INCORRECT (Max overlap: 3/4 with PLAYING CARDS)
   - Group 10: **0.5718** | KINGS, BULLS, SPURS, BUCKS                                        | INCORRECT (Max overlap: 3/4 with N.B.A. TEAMS)
   - Group 11: **0.5716** | KINGS, QUEENS, JACKS, SPURS                                       | INCORRECT (Max overlap: 3/4 with PLAYING CARDS)
   - Group 12: **0.5692** | KINGS, HORNETS, SPURS, BUCKS                                      | INCORRECT (Max overlap: 3/4 with N.B.A. TEAMS) | [Pred Type: NAMED_ENTITY_SET (55.7%, no-rel 14.1%)]
   - Group 13: **0.5634** | KINGS, QUEENS, JACKS, BULLS                                       | INCORRECT (Max overlap: 3/4 with PLAYING CARDS)
   - Group 14: **0.5627** | ACES, BULLS, HORNETS, SPURS                                       | INCORRECT (Max overlap: 3/4 with N.B.A. TEAMS)
   - Group 15: **0.5604** | KINGS, DRONES, BULLS, HORNETS                                     | INCORRECT (Max overlap: 2/4 with N.B.A. TEAMS) | [Pred Type: NAMED_ENTITY_SET (56.1%, no-rel 12.0%)]
   - Group 16: **0.5550** | KINGS, ACES, QUEENS, HORNETS                                      | INCORRECT (Max overlap: 3/4 with PLAYING CARDS) | [Pred Type: NAMED_ENTITY_SET (47.3%, no-rel 24.6%)]
   - Group 17: **0.5545** | BULLS, HORNETS, SPURS, BUCKS                                      | CORRECT GROUP (N.B.A. TEAMS, Level 2)
   - Group 18: **0.5534** | KINGS, DRONES, QUEENS, JACKS                                      | INCORRECT (Max overlap: 3/4 with PLAYING CARDS)
   - Group 19: **0.5526** | KINGS, DRONES, HORNETS, SPURS                                     | INCORRECT (Max overlap: 2/4 with N.B.A. TEAMS) | [Pred Type: NAMED_ENTITY_SET (51.3%, no-rel 21.0%)]
   - Group 20: **0.5524** | KINGS, ACES, DRONES, HORNETS                                      | INCORRECT (Max overlap: 2/4 with PLAYING CARDS) | [Pred Type: NAMED_ENTITY_SET (51.8%, no-rel 19.8%)]

---

## Puzzle 58 (ID: 306)
**Words on Board:** NEAT, ULTRA, TIDY, CLEAN, SNOWBALL, STICK, SUPER, UBER, SWELL, MUSHROOM, HYPER, TRIM, DOMINO, BALLOON, MARBLE, JACK

### Ground Truth Categories:
* **Level 0 (ORDERLY) [Type: SYNONYM_OR_NEAR]:** CLEAN, NEAT, TIDY, TRIM
* **Level 1 (AUGMENTATIVE PREFIXES) [Type: SYNONYM_OR_NEAR]:** HYPER, SUPER, UBER, ULTRA
* **Level 2 (BECOME LARGER) [Type: SYNONYM_OR_NEAR]:** BALLOON, MUSHROOM, SNOWBALL, SWELL
* **Level 3 (ITEMS IN CLASSIC KIDS’ GAMES) [Type: SEMANTIC_SET]:** DOMINO, JACK, MARBLE, STICK

### Top Candidate Partitions:
1. **Partition Score: 0.4902**
   - Group 1: **0.8391** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 33.1%)]
   - Group 2: **0.6691** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 3: **0.4396** | STICK, SWELL, MUSHROOM, BALLOON                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 4: **0.4260** | SNOWBALL, DOMINO, MARBLE, JACK                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES) | [Pred Type: SEMANTIC_SET (58.1%, no-rel 23.9%)]
2. **Partition Score: 0.4874**
   - Group 1: **0.8391** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 33.1%)]
   - Group 2: **0.6691** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 3: **0.4333** | DOMINO, BALLOON, MARBLE, JACK                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES) | [Pred Type: SEMANTIC_SET (58.0%, no-rel 23.2%)]
   - Group 4: **0.4236** | SNOWBALL, STICK, SWELL, MUSHROOM                                  | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
3. **Partition Score: 0.4758**
   - Group 1: **0.8391** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 33.1%)]
   - Group 2: **0.6691** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 3: **0.5009** | SNOWBALL, STICK, SWELL, BALLOON                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 4: **0.3667** | MUSHROOM, DOMINO, MARBLE, JACK                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES) | [Pred Type: SEMANTIC_SET (52.0%, no-rel 23.1%)]
4. **Partition Score: 0.4681**
   - Group 1: **0.6691** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 2: **0.5720** | TIDY, CLEAN, STICK, TRIM                                          | INCORRECT (Max overlap: 3/4 with ORDERLY)
   - Group 3: **0.4339** | NEAT, SNOWBALL, SWELL, MUSHROOM                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 24.3%)]
   - Group 4: **0.4333** | DOMINO, BALLOON, MARBLE, JACK                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES) | [Pred Type: SEMANTIC_SET (58.0%, no-rel 23.2%)]
5. **Partition Score: 0.4605**
   - Group 1: **0.6691** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 2: **0.5720** | TIDY, CLEAN, STICK, TRIM                                          | INCORRECT (Max overlap: 3/4 with ORDERLY)
   - Group 3: **0.4260** | SNOWBALL, DOMINO, MARBLE, JACK                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES) | [Pred Type: SEMANTIC_SET (58.1%, no-rel 23.9%)]
   - Group 4: **0.4220** | NEAT, SWELL, MUSHROOM, BALLOON                                    | INCORRECT (Max overlap: 3/4 with BECOME LARGER) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 26.1%)]

### Top Candidate Groups:
   - Group 1: **0.8391** | NEAT, TIDY, CLEAN, TRIM                                           | CORRECT GROUP (ORDERLY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (61.7%, no-rel 33.1%)]
   - Group 2: **0.6691** | ULTRA, SUPER, UBER, HYPER                                         | CORRECT GROUP (AUGMENTATIVE PREFIXES, Level 1)
   - Group 3: **0.4396** | STICK, SWELL, MUSHROOM, BALLOON                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 4: **0.4260** | SNOWBALL, DOMINO, MARBLE, JACK                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES) | [Pred Type: SEMANTIC_SET (58.1%, no-rel 23.9%)]
   - Group 5: **0.4333** | DOMINO, BALLOON, MARBLE, JACK                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES) | [Pred Type: SEMANTIC_SET (58.0%, no-rel 23.2%)]
   - Group 6: **0.4236** | SNOWBALL, STICK, SWELL, MUSHROOM                                  | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 7: **0.5009** | SNOWBALL, STICK, SWELL, BALLOON                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER)
   - Group 8: **0.3667** | MUSHROOM, DOMINO, MARBLE, JACK                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN CLASSIC KIDS’ GAMES) | [Pred Type: SEMANTIC_SET (52.0%, no-rel 23.1%)]
   - Group 9: **0.5720** | TIDY, CLEAN, STICK, TRIM                                          | INCORRECT (Max overlap: 3/4 with ORDERLY)
   - Group 10: **0.4339** | NEAT, SNOWBALL, SWELL, MUSHROOM                                   | INCORRECT (Max overlap: 3/4 with BECOME LARGER) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 24.3%)]
   - Group 11: **0.4220** | NEAT, SWELL, MUSHROOM, BALLOON                                    | INCORRECT (Max overlap: 3/4 with BECOME LARGER) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 26.1%)]
   - Group 12: **0.4718** | SNOWBALL, DOMINO, BALLOON, MARBLE                                 | INCORRECT (Max overlap: 2/4 with BECOME LARGER) | [Pred Type: SEMANTIC_SET (58.9%, no-rel 18.9%)]
   - Group 13: **0.4383** | NEAT, SUPER, SWELL, MUSHROOM                                      | INCORRECT (Max overlap: 2/4 with BECOME LARGER) | [Pred Type: SYNONYM_OR_NEAR (62.8%, no-rel 17.1%)]
   - Group 14: **0.4353** | ULTRA, UBER, HYPER, JACK                                          | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 15: **0.4630** | NEAT, ULTRA, SUPER, SWELL                                         | INCORRECT (Max overlap: 2/4 with AUGMENTATIVE PREFIXES) | [Pred Type: SYNONYM_OR_NEAR (64.3%, no-rel 16.3%)]
   - Group 16: **0.4604** | SNOWBALL, MUSHROOM, DOMINO, BALLOON                               | INCORRECT (Max overlap: 3/4 with BECOME LARGER) | [Pred Type: SEMANTIC_SET (49.9%, no-rel 24.1%)]
   - Group 17: **0.4195** | UBER, HYPER, MARBLE, JACK                                         | INCORRECT (Max overlap: 2/4 with AUGMENTATIVE PREFIXES)
   - Group 18: **0.4790** | SUPER, UBER, HYPER, JACK                                          | INCORRECT (Max overlap: 3/4 with AUGMENTATIVE PREFIXES)
   - Group 19: **0.4053** | NEAT, ULTRA, SWELL, MUSHROOM                                      | INCORRECT (Max overlap: 2/4 with BECOME LARGER) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 15.6%)]
   - Group 20: **0.4876** | NEAT, ULTRA, TIDY, CLEAN                                          | INCORRECT (Max overlap: 3/4 with ORDERLY) | [Pred Type: SYNONYM_OR_NEAR (70.7%, no-rel 20.8%)]

---

## Puzzle 59 (ID: 641)
**Words on Board:** WILT, WHISTLE, SLANT, FLAG, RIVER, ART, SPIN, THOU, TURN, FLOP, HAIL, WAVE, BIAS, HOLE, ANGLE, ANON

### Ground Truth Categories:
* **Level 0 (PARTIALITY) [Type: SYNONYM_OR_NEAR]:** ANGLE, BIAS, SLANT, SPIN
* **Level 1 (SIGNAL DOWN, AS A TAXI) [Type: SYNONYM_OR_NEAR]:** FLAG, HAIL, WAVE, WHISTLE
* **Level 2 (CARDS IN TEXAS HOLD ’EM) [Type: NAMED_ENTITY_SET]:** FLOP, HOLE, RIVER, TURN
* **Level 3 (SHAKESPEAREAN WORDS) [Type: SEMANTIC_SET]:** ANON, ART, THOU, WILT

### Top Candidate Partitions:
1. **Partition Score: 0.4574**
   - Group 1: **0.5903** | WILT, ART, THOU, ANON                                             | CORRECT GROUP (SHAKESPEAREAN WORDS, Level 3)
   - Group 2: **0.5318** | WHISTLE, RIVER, HAIL, HOLE                                        | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 3: **0.5233** | SLANT, TURN, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 31.7%)]
   - Group 4: **0.3872** | FLAG, SPIN, FLOP, WAVE                                            | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
2. **Partition Score: 0.4572**
   - Group 1: **0.5903** | WILT, ART, THOU, ANON                                             | CORRECT GROUP (SHAKESPEAREAN WORDS, Level 3)
   - Group 2: **0.5318** | WHISTLE, RIVER, HAIL, HOLE                                        | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 3: **0.4744** | SLANT, FLOP, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 4: **0.4114** | FLAG, SPIN, TURN, WAVE                                            | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
3. **Partition Score: 0.4529**
   - Group 1: **0.6416** | WILT, THOU, HAIL, ANON                                            | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 2: **0.5233** | SLANT, TURN, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 31.7%)]
   - Group 3: **0.5139** | WHISTLE, RIVER, ART, HOLE                                         | INCORRECT (Max overlap: 2/4 with CARDS IN TEXAS HOLD ’EM)
   - Group 4: **0.3872** | FLAG, SPIN, FLOP, WAVE                                            | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
4. **Partition Score: 0.4528**
   - Group 1: **0.6416** | WILT, THOU, HAIL, ANON                                            | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 2: **0.5139** | WHISTLE, RIVER, ART, HOLE                                         | INCORRECT (Max overlap: 2/4 with CARDS IN TEXAS HOLD ’EM)
   - Group 3: **0.4744** | SLANT, FLOP, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 4: **0.4114** | FLAG, SPIN, TURN, WAVE                                            | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
5. **Partition Score: 0.4525**
   - Group 1: **0.5903** | WILT, ART, THOU, ANON                                             | CORRECT GROUP (SHAKESPEAREAN WORDS, Level 3)
   - Group 2: **0.5318** | WHISTLE, RIVER, HAIL, HOLE                                        | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 3: **0.5175** | SLANT, TURN, WAVE, ANGLE                                          | INCORRECT (Max overlap: 2/4 with PARTIALITY) | [Pred Type: SYNONYM_OR_NEAR (54.5%, no-rel 28.2%)]
   - Group 4: **0.3804** | FLAG, SPIN, FLOP, BIAS                                            | INCORRECT (Max overlap: 2/4 with PARTIALITY)

### Top Candidate Groups:
   - Group 1: **0.5903** | WILT, ART, THOU, ANON                                             | CORRECT GROUP (SHAKESPEAREAN WORDS, Level 3)
   - Group 2: **0.5318** | WHISTLE, RIVER, HAIL, HOLE                                        | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 3: **0.5233** | SLANT, TURN, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 31.7%)]
   - Group 4: **0.3872** | FLAG, SPIN, FLOP, WAVE                                            | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 5: **0.4744** | SLANT, FLOP, BIAS, ANGLE                                          | INCORRECT (Max overlap: 3/4 with PARTIALITY)
   - Group 6: **0.4114** | FLAG, SPIN, TURN, WAVE                                            | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 7: **0.6416** | WILT, THOU, HAIL, ANON                                            | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 8: **0.5139** | WHISTLE, RIVER, ART, HOLE                                         | INCORRECT (Max overlap: 2/4 with CARDS IN TEXAS HOLD ’EM)
   - Group 9: **0.5175** | SLANT, TURN, WAVE, ANGLE                                          | INCORRECT (Max overlap: 2/4 with PARTIALITY) | [Pred Type: SYNONYM_OR_NEAR (54.5%, no-rel 28.2%)]
   - Group 10: **0.3804** | FLAG, SPIN, FLOP, BIAS                                            | INCORRECT (Max overlap: 2/4 with PARTIALITY)
   - Group 11: **0.4581** | WHISTLE, RIVER, HAIL, WAVE                                        | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI) | [Pred Type: FILL_IN_THE_BLANK (52.4%, no-rel 17.8%)]
   - Group 12: **0.4079** | FLAG, SPIN, FLOP, HOLE                                            | INCORRECT (Max overlap: 2/4 with CARDS IN TEXAS HOLD ’EM)
   - Group 13: **0.5938** | WILT, RIVER, THOU, ANON                                           | INCORRECT (Max overlap: 3/4 with SHAKESPEAREAN WORDS)
   - Group 14: **0.4978** | WHISTLE, ART, HAIL, HOLE                                          | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 15: **0.4751** | SLANT, SPIN, BIAS, ANGLE                                          | CORRECT GROUP (PARTIALITY, Level 0) | [Pred Type: SYNONYM_OR_NEAR (55.0%, no-rel 30.7%)]
   - Group 16: **0.3929** | FLAG, TURN, FLOP, WAVE                                            | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 17: **0.4481** | WHISTLE, RIVER, ART, WAVE                                         | INCORRECT (Max overlap: 2/4 with SIGNAL DOWN, AS A TAXI)
   - Group 18: **0.4407** | WHISTLE, ART, HAIL, WAVE                                          | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
   - Group 19: **0.4828** | WHISTLE, FLAG, TURN, WAVE                                         | INCORRECT (Max overlap: 3/4 with SIGNAL DOWN, AS A TAXI)
   - Group 20: **0.4407** | THOU, FLOP, HAIL, ANON                                            | INCORRECT (Max overlap: 2/4 with SHAKESPEAREAN WORDS)

---

## Puzzle 60 (ID: 893)
**Words on Board:** COSMOPOLITAN, BOLT CUTTER, SCREWDRIVER, AWARENESS RIBBON, WOLF EEL, SCARF RING, GRUMPY OLD MAN, LAPEL PIN, TALKING DOLL, BOUTONNIÈRE, CHOW MEIN, SEA BREEZE, GREYHOUND, RACECAR, LAVALIER, CLOWNFISH

### Ground Truth Categories:
* **Level 0 (THINGS WORN ON LAPELS) [Type: SEMANTIC_SET]:** AWARENESS RIBBON, BOUTONNIÈRE, LAPEL PIN, LAVALIER
* **Level 1 (COCKTAILS) [Type: NAMED_ENTITY_SET]:** COSMOPOLITAN, GREYHOUND, SCREWDRIVER, SEA BREEZE
* **Level 2 (PIXAR PROTAGONISTS) [Type: SEMANTIC_SET]:** CLOWNFISH, GRUMPY OLD MAN, RACECAR, TALKING DOLL
* **Level 3 (STARTING WITH SYNONYMS FOR "EAT") [Type: WORDPLAY_TRANSFORM]:** BOLT CUTTER, CHOW MEIN, SCARF RING, WOLF EEL

### Top Candidate Partitions:
1. **Partition Score: 0.4801**
   - Group 1: **0.4973** | BOLT CUTTER, SCREWDRIVER, SCARF RING, TALKING DOLL                | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT") | [Pred Type: SEMANTIC_SET (59.4%, no-rel 14.4%)]
   - Group 2: **0.4880** | WOLF EEL, CHOW MEIN, SEA BREEZE, CLOWNFISH                        | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 3: **0.4800** | COSMOPOLITAN, AWARENESS RIBBON, LAPEL PIN, BOUTONNIÈRE            | INCORRECT (Max overlap: 3/4 with THINGS WORN ON LAPELS)
   - Group 4: **0.4762** | GRUMPY OLD MAN, GREYHOUND, RACECAR, LAVALIER                      | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)
2. **Partition Score: 0.4769**
   - Group 1: **0.5401** | SCREWDRIVER, AWARENESS RIBBON, SCARF RING, LAPEL PIN              | INCORRECT (Max overlap: 2/4 with THINGS WORN ON LAPELS) | [Pred Type: SEMANTIC_SET (61.0%, no-rel 14.5%)]
   - Group 2: **0.4958** | BOLT CUTTER, GREYHOUND, RACECAR, LAVALIER                         | INCORRECT (Max overlap: 1/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 3: **0.4880** | WOLF EEL, CHOW MEIN, SEA BREEZE, CLOWNFISH                        | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 4: **0.4619** | COSMOPOLITAN, GRUMPY OLD MAN, TALKING DOLL, BOUTONNIÈRE           | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)
3. **Partition Score: 0.4745**
   - Group 1: **0.4958** | BOLT CUTTER, GREYHOUND, RACECAR, LAVALIER                         | INCORRECT (Max overlap: 1/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 2: **0.4880** | WOLF EEL, CHOW MEIN, SEA BREEZE, CLOWNFISH                        | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 3: **0.4800** | COSMOPOLITAN, AWARENESS RIBBON, LAPEL PIN, BOUTONNIÈRE            | INCORRECT (Max overlap: 3/4 with THINGS WORN ON LAPELS)
   - Group 4: **0.4650** | SCREWDRIVER, SCARF RING, GRUMPY OLD MAN, TALKING DOLL             | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS) | [Pred Type: SEMANTIC_SET (50.3%, no-rel 12.7%)]
4. **Partition Score: 0.4729**
   - Group 1: **0.4880** | WOLF EEL, CHOW MEIN, SEA BREEZE, CLOWNFISH                        | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 2: **0.4762** | GRUMPY OLD MAN, GREYHOUND, RACECAR, LAVALIER                      | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)
   - Group 3: **0.4745** | BOLT CUTTER, SCREWDRIVER, TALKING DOLL, BOUTONNIÈRE               | INCORRECT (Max overlap: 1/4 with STARTING WITH SYNONYMS FOR "EAT") | [Pred Type: SEMANTIC_SET (60.9%, no-rel 14.5%)]
   - Group 4: **0.4705** | COSMOPOLITAN, AWARENESS RIBBON, SCARF RING, LAPEL PIN             | INCORRECT (Max overlap: 2/4 with THINGS WORN ON LAPELS)
5. **Partition Score: 0.4729**
   - Group 1: **0.4973** | BOLT CUTTER, SCREWDRIVER, SCARF RING, TALKING DOLL                | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT") | [Pred Type: SEMANTIC_SET (59.4%, no-rel 14.4%)]
   - Group 2: **0.4860** | CHOW MEIN, SEA BREEZE, LAVALIER, CLOWNFISH                        | INCORRECT (Max overlap: 1/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 3: **0.4800** | COSMOPOLITAN, AWARENESS RIBBON, LAPEL PIN, BOUTONNIÈRE            | INCORRECT (Max overlap: 3/4 with THINGS WORN ON LAPELS)
   - Group 4: **0.4628** | WOLF EEL, GRUMPY OLD MAN, GREYHOUND, RACECAR                      | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)

### Top Candidate Groups:
   - Group 1: **0.4973** | BOLT CUTTER, SCREWDRIVER, SCARF RING, TALKING DOLL                | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT") | [Pred Type: SEMANTIC_SET (59.4%, no-rel 14.4%)]
   - Group 2: **0.4880** | WOLF EEL, CHOW MEIN, SEA BREEZE, CLOWNFISH                        | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 3: **0.4800** | COSMOPOLITAN, AWARENESS RIBBON, LAPEL PIN, BOUTONNIÈRE            | INCORRECT (Max overlap: 3/4 with THINGS WORN ON LAPELS)
   - Group 4: **0.4762** | GRUMPY OLD MAN, GREYHOUND, RACECAR, LAVALIER                      | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)
   - Group 5: **0.5401** | SCREWDRIVER, AWARENESS RIBBON, SCARF RING, LAPEL PIN              | INCORRECT (Max overlap: 2/4 with THINGS WORN ON LAPELS) | [Pred Type: SEMANTIC_SET (61.0%, no-rel 14.5%)]
   - Group 6: **0.4958** | BOLT CUTTER, GREYHOUND, RACECAR, LAVALIER                         | INCORRECT (Max overlap: 1/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 7: **0.4619** | COSMOPOLITAN, GRUMPY OLD MAN, TALKING DOLL, BOUTONNIÈRE           | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)
   - Group 8: **0.4650** | SCREWDRIVER, SCARF RING, GRUMPY OLD MAN, TALKING DOLL             | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS) | [Pred Type: SEMANTIC_SET (50.3%, no-rel 12.7%)]
   - Group 9: **0.4745** | BOLT CUTTER, SCREWDRIVER, TALKING DOLL, BOUTONNIÈRE               | INCORRECT (Max overlap: 1/4 with STARTING WITH SYNONYMS FOR "EAT") | [Pred Type: SEMANTIC_SET (60.9%, no-rel 14.5%)]
   - Group 10: **0.4705** | COSMOPOLITAN, AWARENESS RIBBON, SCARF RING, LAPEL PIN             | INCORRECT (Max overlap: 2/4 with THINGS WORN ON LAPELS)
   - Group 11: **0.4860** | CHOW MEIN, SEA BREEZE, LAVALIER, CLOWNFISH                        | INCORRECT (Max overlap: 1/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 12: **0.4628** | WOLF EEL, GRUMPY OLD MAN, GREYHOUND, RACECAR                      | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)
   - Group 13: **0.4750** | WOLF EEL, GREYHOUND, RACECAR, CLOWNFISH                           | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)
   - Group 14: **0.4672** | GRUMPY OLD MAN, CHOW MEIN, SEA BREEZE, LAVALIER                   | INCORRECT (Max overlap: 1/4 with PIXAR PROTAGONISTS)
   - Group 15: **0.5033** | GRUMPY OLD MAN, TALKING DOLL, CHOW MEIN, CLOWNFISH                | INCORRECT (Max overlap: 3/4 with PIXAR PROTAGONISTS)
   - Group 16: **0.4754** | BOLT CUTTER, WOLF EEL, GREYHOUND, RACECAR                         | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 17: **0.4553** | COSMOPOLITAN, BOUTONNIÈRE, SEA BREEZE, LAVALIER                   | INCORRECT (Max overlap: 2/4 with COCKTAILS)
   - Group 18: **0.4817** | GREYHOUND, RACECAR, LAVALIER, CLOWNFISH                           | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS)
   - Group 19: **0.4635** | WOLF EEL, GRUMPY OLD MAN, CHOW MEIN, SEA BREEZE                   | INCORRECT (Max overlap: 2/4 with STARTING WITH SYNONYMS FOR "EAT")
   - Group 20: **0.4597** | SCREWDRIVER, GRUMPY OLD MAN, TALKING DOLL, BOUTONNIÈRE            | INCORRECT (Max overlap: 2/4 with PIXAR PROTAGONISTS) | [Pred Type: SEMANTIC_SET (50.7%, no-rel 12.2%)]

---

## Puzzle 61 (ID: 109)
**Words on Board:** HUNT, CRUNK, GRIME, DRILL, FORAGE, FISH, GLITTER, BEER, RAIL, GLEAM, FLASH, YEAR, BULB, TRAP, SPARKLE, BOUNCE

### Ground Truth Categories:
* **Level 0 (REFLECT LIGHT) [Type: SYNONYM_OR_NEAR]:** FLASH, GLEAM, GLITTER, SPARKLE
* **Level 1 (WAYS TO GATHER FOOD) [Type: SEMANTIC_SET]:** FISH, FORAGE, HUNT, TRAP
* **Level 2 (RAP SUBGENRES) [Type: NAMED_ENTITY_SET]:** BOUNCE, CRUNK, DRILL, GRIME
* **Level 3 (LIGHT ___) [Type: FILL_IN_THE_BLANK]:** BEER, BULB, RAIL, YEAR

### Top Candidate Partitions:
1. **Partition Score: 0.4264**
   - Group 1: **0.5032** | GLITTER, GLEAM, BULB, SPARKLE                                     | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 30.0%)]
   - Group 2: **0.4738** | FISH, BEER, RAIL, YEAR                                            | INCORRECT (Max overlap: 3/4 with LIGHT ___)
   - Group 3: **0.4603** | CRUNK, GRIME, DRILL, BOUNCE                                       | CORRECT GROUP (RAP SUBGENRES, Level 2)
   - Group 4: **0.3857** | HUNT, FORAGE, FLASH, TRAP                                         | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
2. **Partition Score: 0.4199**
   - Group 1: **0.5989** | GLEAM, FLASH, BULB, SPARKLE                                       | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 30.1%)]
   - Group 2: **0.5831** | CRUNK, GRIME, BEER, YEAR                                          | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 3: **0.3691** | DRILL, FISH, RAIL, BOUNCE                                         | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 4: **0.3637** | HUNT, FORAGE, GLITTER, TRAP                                       | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
3. **Partition Score: 0.4154**
   - Group 1: **0.5989** | GLEAM, FLASH, BULB, SPARKLE                                       | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 30.1%)]
   - Group 2: **0.4738** | FISH, BEER, RAIL, YEAR                                            | INCORRECT (Max overlap: 3/4 with LIGHT ___)
   - Group 3: **0.4603** | CRUNK, GRIME, DRILL, BOUNCE                                       | CORRECT GROUP (RAP SUBGENRES, Level 2)
   - Group 4: **0.3637** | HUNT, FORAGE, GLITTER, TRAP                                       | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
4. **Partition Score: 0.4150**
   - Group 1: **0.5989** | GLEAM, FLASH, BULB, SPARKLE                                       | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 30.1%)]
   - Group 2: **0.5638** | CRUNK, FISH, BEER, YEAR                                           | INCORRECT (Max overlap: 2/4 with LIGHT ___)
   - Group 3: **0.3689** | GRIME, DRILL, RAIL, BOUNCE                                        | INCORRECT (Max overlap: 3/4 with RAP SUBGENRES)
   - Group 4: **0.3637** | HUNT, FORAGE, GLITTER, TRAP                                       | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
5. **Partition Score: 0.4122**
   - Group 1: **0.5596** | GLITTER, FLASH, BULB, SPARKLE                                     | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 29.5%)]
   - Group 2: **0.4738** | FISH, BEER, RAIL, YEAR                                            | INCORRECT (Max overlap: 3/4 with LIGHT ___)
   - Group 3: **0.4603** | CRUNK, GRIME, DRILL, BOUNCE                                       | CORRECT GROUP (RAP SUBGENRES, Level 2)
   - Group 4: **0.3573** | HUNT, FORAGE, GLEAM, TRAP                                         | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)

### Top Candidate Groups:
   - Group 1: **0.5032** | GLITTER, GLEAM, BULB, SPARKLE                                     | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (59.0%, no-rel 30.0%)]
   - Group 2: **0.4738** | FISH, BEER, RAIL, YEAR                                            | INCORRECT (Max overlap: 3/4 with LIGHT ___)
   - Group 3: **0.4603** | CRUNK, GRIME, DRILL, BOUNCE                                       | CORRECT GROUP (RAP SUBGENRES, Level 2)
   - Group 4: **0.3857** | HUNT, FORAGE, FLASH, TRAP                                         | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 5: **0.5989** | GLEAM, FLASH, BULB, SPARKLE                                       | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 30.1%)]
   - Group 6: **0.5831** | CRUNK, GRIME, BEER, YEAR                                          | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 7: **0.3691** | DRILL, FISH, RAIL, BOUNCE                                         | INCORRECT (Max overlap: 2/4 with RAP SUBGENRES)
   - Group 8: **0.3637** | HUNT, FORAGE, GLITTER, TRAP                                       | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 9: **0.5638** | CRUNK, FISH, BEER, YEAR                                           | INCORRECT (Max overlap: 2/4 with LIGHT ___)
   - Group 10: **0.3689** | GRIME, DRILL, RAIL, BOUNCE                                        | INCORRECT (Max overlap: 3/4 with RAP SUBGENRES)
   - Group 11: **0.5596** | GLITTER, FLASH, BULB, SPARKLE                                     | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 29.5%)]
   - Group 12: **0.3573** | HUNT, FORAGE, GLEAM, TRAP                                         | INCORRECT (Max overlap: 3/4 with WAYS TO GATHER FOOD)
   - Group 13: **0.4831** | FORAGE, GLITTER, GLEAM, SPARKLE                                   | INCORRECT (Max overlap: 3/4 with REFLECT LIGHT) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 33.6%)]
   - Group 14: **0.3557** | HUNT, FLASH, BULB, TRAP                                           | INCORRECT (Max overlap: 2/4 with WAYS TO GATHER FOOD) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 28.2%)]
   - Group 15: **0.4355** | GRIME, DRILL, BEER, BOUNCE                                        | INCORRECT (Max overlap: 3/4 with RAP SUBGENRES)
   - Group 16: **0.4175** | CRUNK, FISH, RAIL, YEAR                                           | INCORRECT (Max overlap: 2/4 with LIGHT ___)
   - Group 17: **0.4283** | CRUNK, BEER, RAIL, YEAR                                           | INCORRECT (Max overlap: 3/4 with LIGHT ___)
   - Group 18: **0.4141** | GRIME, FORAGE, GLITTER, TRAP                                      | INCORRECT (Max overlap: 2/4 with WAYS TO GATHER FOOD)
   - Group 19: **0.3895** | HUNT, DRILL, FISH, BOUNCE                                         | INCORRECT (Max overlap: 2/4 with WAYS TO GATHER FOOD)
   - Group 20: **0.4494** | CRUNK, GRIME, DRILL, YEAR                                         | INCORRECT (Max overlap: 3/4 with RAP SUBGENRES)

---

## Puzzle 62 (ID: 936)
**Words on Board:** WORK, BAR, UMBRELLA, DIAMONDS, WILLY, JOGGER, BLANKET, SLACK, GENERAL, PRIVATE, SOS, CAPTAIN, MAJOR, OVERALL, NURSE, JEAN

### Ground Truth Categories:
* **Level 0 (ARMY RANKS) [Type: SEMANTIC_SET]:** CAPTAIN, GENERAL, MAJOR, PRIVATE
* **Level 1 (LEGWEAR IN THE SINGULAR) [Type: WORD_FORM]:** JEAN, JOGGER, OVERALL, SLACK
* **Level 2 (RIHANNA #1 HITS) [Type: NAMED_ENTITY_SET]:** DIAMONDS, SOS, UMBRELLA, WORK
* **Level 3 (WET ___) [Type: FILL_IN_THE_BLANK]:** BAR, BLANKET, NURSE, WILLY

### Top Candidate Partitions:
1. **Partition Score: 0.4152**
   - Group 1: **0.4962** | WORK, SLACK, OVERALL, NURSE                                       | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (49.3%, no-rel 31.0%)]
   - Group 2: **0.4570** | UMBRELLA, DIAMONDS, BLANKET, JEAN                                 | INCORRECT (Max overlap: 2/4 with RIHANNA #1 HITS)
   - Group 3: **0.4124** | GENERAL, PRIVATE, CAPTAIN, MAJOR                                  | CORRECT GROUP (ARMY RANKS, Level 0)
   - Group 4: **0.3957** | BAR, WILLY, JOGGER, SOS                                           | INCORRECT (Max overlap: 2/4 with WET ___)
2. **Partition Score: 0.4146**
   - Group 1: **0.4810** | GENERAL, CAPTAIN, MAJOR, OVERALL                                  | INCORRECT (Max overlap: 3/4 with ARMY RANKS) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 25.3%)]
   - Group 2: **0.4570** | UMBRELLA, DIAMONDS, BLANKET, JEAN                                 | INCORRECT (Max overlap: 2/4 with RIHANNA #1 HITS)
   - Group 3: **0.4102** | WORK, SLACK, PRIVATE, NURSE                                       | INCORRECT (Max overlap: 1/4 with RIHANNA #1 HITS) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 23.4%)]
   - Group 4: **0.3957** | BAR, WILLY, JOGGER, SOS                                           | INCORRECT (Max overlap: 2/4 with WET ___)
3. **Partition Score: 0.4144**
   - Group 1: **0.5076** | GENERAL, CAPTAIN, MAJOR, NURSE                                    | INCORRECT (Max overlap: 3/4 with ARMY RANKS)
   - Group 2: **0.4570** | UMBRELLA, DIAMONDS, BLANKET, JEAN                                 | INCORRECT (Max overlap: 2/4 with RIHANNA #1 HITS)
   - Group 3: **0.4093** | WORK, SLACK, PRIVATE, OVERALL                                     | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 23.1%)]
   - Group 4: **0.3957** | BAR, WILLY, JOGGER, SOS                                           | INCORRECT (Max overlap: 2/4 with WET ___)
4. **Partition Score: 0.4112**
   - Group 1: **0.4570** | UMBRELLA, DIAMONDS, BLANKET, JEAN                                 | INCORRECT (Max overlap: 2/4 with RIHANNA #1 HITS)
   - Group 2: **0.4274** | SLACK, PRIVATE, MAJOR, OVERALL                                    | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (45.5%, no-rel 27.1%)]
   - Group 3: **0.4262** | WORK, GENERAL, CAPTAIN, NURSE                                     | INCORRECT (Max overlap: 2/4 with ARMY RANKS)
   - Group 4: **0.3957** | BAR, WILLY, JOGGER, SOS                                           | INCORRECT (Max overlap: 2/4 with WET ___)
5. **Partition Score: 0.4075**
   - Group 1: **0.5140** | DIAMONDS, WILLY, JOGGER, JEAN                                     | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR)
   - Group 2: **0.4180** | WORK, MAJOR, OVERALL, NURSE                                       | INCORRECT (Max overlap: 1/4 with RIHANNA #1 HITS) | [Pred Type: SYNONYM_OR_NEAR (48.2%, no-rel 30.4%)]
   - Group 3: **0.4049** | UMBRELLA, BLANKET, GENERAL, CAPTAIN                               | INCORRECT (Max overlap: 2/4 with ARMY RANKS) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 14.9%)]
   - Group 4: **0.4036** | BAR, SLACK, PRIVATE, SOS                                          | INCORRECT (Max overlap: 1/4 with WET ___)

### Top Candidate Groups:
   - Group 1: **0.4962** | WORK, SLACK, OVERALL, NURSE                                       | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (49.3%, no-rel 31.0%)]
   - Group 2: **0.4570** | UMBRELLA, DIAMONDS, BLANKET, JEAN                                 | INCORRECT (Max overlap: 2/4 with RIHANNA #1 HITS)
   - Group 3: **0.4124** | GENERAL, PRIVATE, CAPTAIN, MAJOR                                  | CORRECT GROUP (ARMY RANKS, Level 0)
   - Group 4: **0.3957** | BAR, WILLY, JOGGER, SOS                                           | INCORRECT (Max overlap: 2/4 with WET ___)
   - Group 5: **0.4810** | GENERAL, CAPTAIN, MAJOR, OVERALL                                  | INCORRECT (Max overlap: 3/4 with ARMY RANKS) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 25.3%)]
   - Group 6: **0.4102** | WORK, SLACK, PRIVATE, NURSE                                       | INCORRECT (Max overlap: 1/4 with RIHANNA #1 HITS) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 23.4%)]
   - Group 7: **0.5076** | GENERAL, CAPTAIN, MAJOR, NURSE                                    | INCORRECT (Max overlap: 3/4 with ARMY RANKS)
   - Group 8: **0.4093** | WORK, SLACK, PRIVATE, OVERALL                                     | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (50.8%, no-rel 23.1%)]
   - Group 9: **0.4274** | SLACK, PRIVATE, MAJOR, OVERALL                                    | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (45.5%, no-rel 27.1%)]
   - Group 10: **0.4262** | WORK, GENERAL, CAPTAIN, NURSE                                     | INCORRECT (Max overlap: 2/4 with ARMY RANKS)
   - Group 11: **0.5140** | DIAMONDS, WILLY, JOGGER, JEAN                                     | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR)
   - Group 12: **0.4180** | WORK, MAJOR, OVERALL, NURSE                                       | INCORRECT (Max overlap: 1/4 with RIHANNA #1 HITS) | [Pred Type: SYNONYM_OR_NEAR (48.2%, no-rel 30.4%)]
   - Group 13: **0.4049** | UMBRELLA, BLANKET, GENERAL, CAPTAIN                               | INCORRECT (Max overlap: 2/4 with ARMY RANKS) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 14.9%)]
   - Group 14: **0.4036** | BAR, SLACK, PRIVATE, SOS                                          | INCORRECT (Max overlap: 1/4 with WET ___)
   - Group 15: **0.4201** | UMBRELLA, DIAMONDS, WILLY, BLANKET                                | INCORRECT (Max overlap: 2/4 with RIHANNA #1 HITS)
   - Group 16: **0.3870** | BAR, JOGGER, SOS, JEAN                                            | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR)
   - Group 17: **0.4483** | UMBRELLA, WILLY, BLANKET, JEAN                                    | INCORRECT (Max overlap: 2/4 with WET ___)
   - Group 18: **0.3791** | BAR, DIAMONDS, JOGGER, SOS                                        | INCORRECT (Max overlap: 2/4 with RIHANNA #1 HITS)
   - Group 19: **0.5224** | WILLY, JOGGER, SOS, JEAN                                          | INCORRECT (Max overlap: 2/4 with LEGWEAR IN THE SINGULAR)
   - Group 20: **0.3494** | BAR, UMBRELLA, DIAMONDS, BLANKET                                  | INCORRECT (Max overlap: 2/4 with WET ___)

---

## Puzzle 63 (ID: 520)
**Words on Board:** SPEED, FLORET, SCALES, CLOVE, GRUMBLE, RESOLUTION, CARP, RAM, STORAGE, STALK, CRAB, BLINDFOLD, SPEAR, ROBE, SWORD, BELLYACHE

### Ground Truth Categories:
* **Level 0 (COMPLAIN) [Type: SYNONYM_OR_NEAR]:** BELLYACHE, CARP, CRAB, GRUMBLE
* **Level 1 (VEGETABLE UNITS) [Type: SEMANTIC_SET]:** CLOVE, FLORET, SPEAR, STALK
* **Level 2 (LAPTOP SPECS) [Type: SEMANTIC_SET]:** RAM, RESOLUTION, SPEED, STORAGE
* **Level 3 (FEATURES OF JUSTICE PERSONIFIED) [Type: SEMANTIC_SET]:** BLINDFOLD, ROBE, SCALES, SWORD

### Top Candidate Partitions:
1. **Partition Score: 0.4375**
   - Group 1: **0.4746** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 18.3%)]
   - Group 2: **0.4624** | CLOVE, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS) | [Pred Type: SEMANTIC_SET (55.6%, no-rel 28.0%)]
   - Group 3: **0.4303** | FLORET, CARP, RAM, STORAGE                                        | INCORRECT (Max overlap: 2/4 with LAPTOP SPECS)
   - Group 4: **0.4286** | SPEED, SCALES, RESOLUTION, STALK                                  | INCORRECT (Max overlap: 2/4 with LAPTOP SPECS)
2. **Partition Score: 0.4300**
   - Group 1: **0.4746** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 18.3%)]
   - Group 2: **0.4624** | CLOVE, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS) | [Pred Type: SEMANTIC_SET (55.6%, no-rel 28.0%)]
   - Group 3: **0.4591** | FLORET, SCALES, RESOLUTION, CARP                                  | INCORRECT (Max overlap: 1/4 with VEGETABLE UNITS)
   - Group 4: **0.3992** | SPEED, RAM, STORAGE, STALK                                        | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS) | [Pred Type: FILL_IN_THE_BLANK (50.7%, no-rel 17.4%)]
3. **Partition Score: 0.4283**
   - Group 1: **0.5038** | FLORET, CLOVE, CARP, STALK                                        | INCORRECT (Max overlap: 3/4 with VEGETABLE UNITS)
   - Group 2: **0.4746** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 18.3%)]
   - Group 3: **0.4186** | SCALES, RESOLUTION, RAM, STORAGE                                  | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS)
   - Group 4: **0.4101** | SPEED, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with FEATURES OF JUSTICE PERSONIFIED) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 23.2%)]
4. **Partition Score: 0.4278**
   - Group 1: **0.4746** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 18.3%)]
   - Group 2: **0.4624** | CLOVE, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS) | [Pred Type: SEMANTIC_SET (55.6%, no-rel 28.0%)]
   - Group 3: **0.4237** | FLORET, SCALES, CARP, RAM                                         | INCORRECT (Max overlap: 1/4 with VEGETABLE UNITS)
   - Group 4: **0.4125** | SPEED, RESOLUTION, STORAGE, STALK                                 | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS) | [Pred Type: FILL_IN_THE_BLANK (56.5%, no-rel 13.1%)]
5. **Partition Score: 0.4260**
   - Group 1: **0.4746** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 18.3%)]
   - Group 2: **0.4624** | CLOVE, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS) | [Pred Type: SEMANTIC_SET (55.6%, no-rel 28.0%)]
   - Group 3: **0.4507** | FLORET, CARP, STORAGE, STALK                                      | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 4: **0.3955** | SPEED, SCALES, RESOLUTION, RAM                                    | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS)

### Top Candidate Groups:
   - Group 1: **0.4746** | GRUMBLE, CRAB, BLINDFOLD, BELLYACHE                               | INCORRECT (Max overlap: 3/4 with COMPLAIN) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 18.3%)]
   - Group 2: **0.4624** | CLOVE, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS) | [Pred Type: SEMANTIC_SET (55.6%, no-rel 28.0%)]
   - Group 3: **0.4303** | FLORET, CARP, RAM, STORAGE                                        | INCORRECT (Max overlap: 2/4 with LAPTOP SPECS)
   - Group 4: **0.4286** | SPEED, SCALES, RESOLUTION, STALK                                  | INCORRECT (Max overlap: 2/4 with LAPTOP SPECS)
   - Group 5: **0.4591** | FLORET, SCALES, RESOLUTION, CARP                                  | INCORRECT (Max overlap: 1/4 with VEGETABLE UNITS)
   - Group 6: **0.3992** | SPEED, RAM, STORAGE, STALK                                        | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS) | [Pred Type: FILL_IN_THE_BLANK (50.7%, no-rel 17.4%)]
   - Group 7: **0.5038** | FLORET, CLOVE, CARP, STALK                                        | INCORRECT (Max overlap: 3/4 with VEGETABLE UNITS)
   - Group 8: **0.4186** | SCALES, RESOLUTION, RAM, STORAGE                                  | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS)
   - Group 9: **0.4101** | SPEED, SPEAR, ROBE, SWORD                                         | INCORRECT (Max overlap: 2/4 with FEATURES OF JUSTICE PERSONIFIED) | [Pred Type: SEMANTIC_SET (51.3%, no-rel 23.2%)]
   - Group 10: **0.4237** | FLORET, SCALES, CARP, RAM                                         | INCORRECT (Max overlap: 1/4 with VEGETABLE UNITS)
   - Group 11: **0.4125** | SPEED, RESOLUTION, STORAGE, STALK                                 | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS) | [Pred Type: FILL_IN_THE_BLANK (56.5%, no-rel 13.1%)]
   - Group 12: **0.4507** | FLORET, CARP, STORAGE, STALK                                      | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 13: **0.3955** | SPEED, SCALES, RESOLUTION, RAM                                    | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS)
   - Group 14: **0.4585** | SCALES, SPEAR, ROBE, SWORD                                        | INCORRECT (Max overlap: 3/4 with FEATURES OF JUSTICE PERSONIFIED) | [Pred Type: SEMANTIC_SET (50.5%, no-rel 22.2%)]
   - Group 15: **0.4181** | FLORET, CLOVE, CARP, RAM                                          | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 16: **0.4256** | SPEED, SCALES, RAM, STORAGE                                       | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS)
   - Group 17: **0.4054** | FLORET, RESOLUTION, CARP, STALK                                   | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)
   - Group 18: **0.4472** | SCALES, RESOLUTION, STORAGE, STALK                                | INCORRECT (Max overlap: 2/4 with LAPTOP SPECS)
   - Group 19: **0.4279** | SPEED, SCALES, RESOLUTION, STORAGE                                | INCORRECT (Max overlap: 3/4 with LAPTOP SPECS)
   - Group 20: **0.3944** | FLORET, CARP, RAM, STALK                                          | INCORRECT (Max overlap: 2/4 with VEGETABLE UNITS)

---

## Puzzle 64 (ID: 183)
**Words on Board:** SILK, LACE, LAND, SOLE, SETTLE, BLOW, BABY, EYELET, PACKAGE, SPEECH, PERCH, ROOST, CHIFFON, TONGUE, SATIN, VELVET

### Ground Truth Categories:
* **Level 0 (LUXURIOUS FABRICS) [Type: SEMANTIC_SET]:** CHIFFON, SATIN, SILK, VELVET
* **Level 1 (COME DOWN TO REST) [Type: SYNONYM_OR_NEAR]:** PERCH, ROOST, SETTLE, LAND
* **Level 2 (SHOE PARTS) [Type: SEMANTIC_SET]:** EYELET, LACE, SOLE, TONGUE
* **Level 3 (THINGS THAT ARE DELIVERED) [Type: FILL_IN_THE_BLANK]:** BABY, BLOW, PACKAGE, SPEECH

### Top Candidate Partitions:
1. **Partition Score: 0.4132**
   - Group 1: **0.8544** | SILK, CHIFFON, SATIN, VELVET                                      | CORRECT GROUP (LUXURIOUS FABRICS, Level 0) | [Pred Type: SEMANTIC_SET (56.2%, no-rel 33.9%)]
   - Group 2: **0.4621** | BLOW, BABY, SPEECH, TONGUE                                        | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE DELIVERED) | [Pred Type: FILL_IN_THE_BLANK (50.7%, no-rel 29.3%)]
   - Group 3: **0.4121** | LAND, SETTLE, PERCH, ROOST                                        | CORRECT GROUP (COME DOWN TO REST, Level 1) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 26.9%)]
   - Group 4: **0.3893** | LACE, SOLE, EYELET, PACKAGE                                       | INCORRECT (Max overlap: 3/4 with SHOE PARTS)
2. **Partition Score: 0.4065**
   - Group 1: **0.5088** | SILK, EYELET, CHIFFON, SATIN                                      | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 34.9%)]
   - Group 2: **0.4224** | SOLE, SETTLE, PERCH, ROOST                                        | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 32.0%)]
   - Group 3: **0.4125** | BLOW, BABY, PACKAGE, SPEECH                                       | CORRECT GROUP (THINGS THAT ARE DELIVERED, Level 3)
   - Group 4: **0.3956** | LACE, LAND, TONGUE, VELVET                                        | INCORRECT (Max overlap: 2/4 with SHOE PARTS) | [Pred Type: SEMANTIC_SET (53.4%, no-rel 24.3%)]
3. **Partition Score: 0.4057**
   - Group 1: **0.4248** | SILK, LACE, LAND, SATIN                                           | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS) | [Pred Type: SEMANTIC_SET (58.5%, no-rel 24.5%)]
   - Group 2: **0.4224** | SOLE, SETTLE, PERCH, ROOST                                        | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 32.0%)]
   - Group 3: **0.4125** | BLOW, BABY, PACKAGE, SPEECH                                       | CORRECT GROUP (THINGS THAT ARE DELIVERED, Level 3)
   - Group 4: **0.3940** | EYELET, CHIFFON, TONGUE, VELVET                                   | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
4. **Partition Score: 0.4025**
   - Group 1: **0.4125** | BLOW, BABY, PACKAGE, SPEECH                                       | CORRECT GROUP (THINGS THAT ARE DELIVERED, Level 3)
   - Group 2: **0.4121** | LAND, SETTLE, PERCH, ROOST                                        | CORRECT GROUP (COME DOWN TO REST, Level 1) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 26.9%)]
   - Group 3: **0.4102** | SILK, LACE, SOLE, SATIN                                           | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS) | [Pred Type: SEMANTIC_SET (53.8%, no-rel 26.7%)]
   - Group 4: **0.3940** | EYELET, CHIFFON, TONGUE, VELVET                                   | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
5. **Partition Score: 0.4022**
   - Group 1: **0.8544** | SILK, CHIFFON, SATIN, VELVET                                      | CORRECT GROUP (LUXURIOUS FABRICS, Level 0) | [Pred Type: SEMANTIC_SET (56.2%, no-rel 33.9%)]
   - Group 2: **0.4441** | SETTLE, PACKAGE, PERCH, ROOST                                     | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 34.7%)]
   - Group 3: **0.4079** | BABY, EYELET, SPEECH, TONGUE                                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
   - Group 4: **0.3785** | LACE, LAND, SOLE, BLOW                                            | INCORRECT (Max overlap: 2/4 with SHOE PARTS)

### Top Candidate Groups:
   - Group 1: **0.8544** | SILK, CHIFFON, SATIN, VELVET                                      | CORRECT GROUP (LUXURIOUS FABRICS, Level 0) | [Pred Type: SEMANTIC_SET (56.2%, no-rel 33.9%)]
   - Group 2: **0.4621** | BLOW, BABY, SPEECH, TONGUE                                        | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE DELIVERED) | [Pred Type: FILL_IN_THE_BLANK (50.7%, no-rel 29.3%)]
   - Group 3: **0.4121** | LAND, SETTLE, PERCH, ROOST                                        | CORRECT GROUP (COME DOWN TO REST, Level 1) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 26.9%)]
   - Group 4: **0.3893** | LACE, SOLE, EYELET, PACKAGE                                       | INCORRECT (Max overlap: 3/4 with SHOE PARTS)
   - Group 5: **0.5088** | SILK, EYELET, CHIFFON, SATIN                                      | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 34.9%)]
   - Group 6: **0.4224** | SOLE, SETTLE, PERCH, ROOST                                        | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST) | [Pred Type: SYNONYM_OR_NEAR (51.7%, no-rel 32.0%)]
   - Group 7: **0.4125** | BLOW, BABY, PACKAGE, SPEECH                                       | CORRECT GROUP (THINGS THAT ARE DELIVERED, Level 3)
   - Group 8: **0.3956** | LACE, LAND, TONGUE, VELVET                                        | INCORRECT (Max overlap: 2/4 with SHOE PARTS) | [Pred Type: SEMANTIC_SET (53.4%, no-rel 24.3%)]
   - Group 9: **0.4248** | SILK, LACE, LAND, SATIN                                           | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS) | [Pred Type: SEMANTIC_SET (58.5%, no-rel 24.5%)]
   - Group 10: **0.3940** | EYELET, CHIFFON, TONGUE, VELVET                                   | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 11: **0.4102** | SILK, LACE, SOLE, SATIN                                           | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS) | [Pred Type: SEMANTIC_SET (53.8%, no-rel 26.7%)]
   - Group 12: **0.4441** | SETTLE, PACKAGE, PERCH, ROOST                                     | INCORRECT (Max overlap: 3/4 with COME DOWN TO REST) | [Pred Type: SYNONYM_OR_NEAR (49.7%, no-rel 34.7%)]
   - Group 13: **0.4079** | BABY, EYELET, SPEECH, TONGUE                                      | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE DELIVERED)
   - Group 14: **0.3785** | LACE, LAND, SOLE, BLOW                                            | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 15: **0.3808** | SOLE, BLOW, BABY, SPEECH                                          | INCORRECT (Max overlap: 3/4 with THINGS THAT ARE DELIVERED)
   - Group 16: **0.4012** | SILK, LACE, LAND, CHIFFON                                         | INCORRECT (Max overlap: 2/4 with LUXURIOUS FABRICS) | [Pred Type: SEMANTIC_SET (61.3%, no-rel 19.8%)]
   - Group 17: **0.3935** | EYELET, TONGUE, SATIN, VELVET                                     | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 18: **0.4156** | BABY, CHIFFON, SATIN, VELVET                                      | INCORRECT (Max overlap: 3/4 with LUXURIOUS FABRICS)
   - Group 19: **0.4101** | SOLE, BLOW, SPEECH, TONGUE                                        | INCORRECT (Max overlap: 2/4 with SHOE PARTS)
   - Group 20: **0.3886** | SILK, LACE, EYELET, PACKAGE                                       | INCORRECT (Max overlap: 2/4 with SHOE PARTS) | [Pred Type: SEMANTIC_SET (50.2%, no-rel 28.5%)]

---

## Puzzle 65 (ID: 782)
**Words on Board:** GABLE, GARLAND, BENT, FACULTY, ROOF, WRAP, FLAIR, HAY, ROAD, TEMPLE, WREATH, JACKPOT, DEAN, SWORD, PLAYWRIGHT, GIFT

### Ground Truth Categories:
* **Level 0 (APTITUDE) [Type: SYNONYM_OR_NEAR]:** BENT, FACULTY, FLAIR, GIFT
* **Level 1 (SILENT “W”) [Type: SOUND_OR_SPELLING]:** PLAYWRIGHT, SWORD, WRAP, WREATH
* **Level 2 (LEGENDS OF CLASSIC HOLLYWOOD) [Type: NAMED_ENTITY_SET]:** DEAN, GABLE, GARLAND, TEMPLE
* **Level 3 (HIT THE ___) [Type: FILL_IN_THE_BLANK]:** HAY, JACKPOT, ROAD, ROOF

### Top Candidate Partitions:
1. **Partition Score: 0.4106**
   - Group 1: **0.5918** | GARLAND, FACULTY, WREATH, DEAN                                    | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 29.7%)]
   - Group 2: **0.5214** | BENT, WRAP, FLAIR, GIFT                                           | INCORRECT (Max overlap: 3/4 with APTITUDE) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 33.5%)]
   - Group 3: **0.4182** | HAY, TEMPLE, JACKPOT, PLAYWRIGHT                                  | INCORRECT (Max overlap: 2/4 with HIT THE ___)
   - Group 4: **0.3513** | GABLE, ROOF, ROAD, SWORD                                          | INCORRECT (Max overlap: 2/4 with HIT THE ___) | [Pred Type: SEMANTIC_SET (55.9%, no-rel 24.0%)]
2. **Partition Score: 0.4102**
   - Group 1: **0.5918** | GARLAND, FACULTY, WREATH, DEAN                                    | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 29.7%)]
   - Group 2: **0.5214** | BENT, WRAP, FLAIR, GIFT                                           | INCORRECT (Max overlap: 3/4 with APTITUDE) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 33.5%)]
   - Group 3: **0.4434** | HAY, ROAD, JACKPOT, PLAYWRIGHT                                    | INCORRECT (Max overlap: 3/4 with HIT THE ___)
   - Group 4: **0.3379** | GABLE, ROOF, TEMPLE, SWORD                                        | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD) | [Pred Type: SEMANTIC_SET (62.5%, no-rel 20.6%)]
3. **Partition Score: 0.4050**
   - Group 1: **0.5484** | GARLAND, WRAP, WREATH, GIFT                                       | INCORRECT (Max overlap: 2/4 with SILENT “W”) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 27.5%)]
   - Group 2: **0.4992** | BENT, FACULTY, FLAIR, DEAN                                        | INCORRECT (Max overlap: 3/4 with APTITUDE)
   - Group 3: **0.4182** | HAY, TEMPLE, JACKPOT, PLAYWRIGHT                                  | INCORRECT (Max overlap: 2/4 with HIT THE ___)
   - Group 4: **0.3513** | GABLE, ROOF, ROAD, SWORD                                          | INCORRECT (Max overlap: 2/4 with HIT THE ___) | [Pred Type: SEMANTIC_SET (55.9%, no-rel 24.0%)]
4. **Partition Score: 0.4046**
   - Group 1: **0.5484** | GARLAND, WRAP, WREATH, GIFT                                       | INCORRECT (Max overlap: 2/4 with SILENT “W”) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 27.5%)]
   - Group 2: **0.4992** | BENT, FACULTY, FLAIR, DEAN                                        | INCORRECT (Max overlap: 3/4 with APTITUDE)
   - Group 3: **0.4434** | HAY, ROAD, JACKPOT, PLAYWRIGHT                                    | INCORRECT (Max overlap: 3/4 with HIT THE ___)
   - Group 4: **0.3379** | GABLE, ROOF, TEMPLE, SWORD                                        | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD) | [Pred Type: SEMANTIC_SET (62.5%, no-rel 20.6%)]
5. **Partition Score: 0.4040**
   - Group 1: **0.5313** | BENT, FACULTY, FLAIR, GIFT                                        | CORRECT GROUP (APTITUDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 37.5%)]
   - Group 2: **0.4951** | GARLAND, WRAP, WREATH, DEAN                                       | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 28.1%)]
   - Group 3: **0.4182** | HAY, TEMPLE, JACKPOT, PLAYWRIGHT                                  | INCORRECT (Max overlap: 2/4 with HIT THE ___)
   - Group 4: **0.3513** | GABLE, ROOF, ROAD, SWORD                                          | INCORRECT (Max overlap: 2/4 with HIT THE ___) | [Pred Type: SEMANTIC_SET (55.9%, no-rel 24.0%)]

### Top Candidate Groups:
   - Group 1: **0.5918** | GARLAND, FACULTY, WREATH, DEAN                                    | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD) | [Pred Type: SYNONYM_OR_NEAR (56.9%, no-rel 29.7%)]
   - Group 2: **0.5214** | BENT, WRAP, FLAIR, GIFT                                           | INCORRECT (Max overlap: 3/4 with APTITUDE) | [Pred Type: SYNONYM_OR_NEAR (51.3%, no-rel 33.5%)]
   - Group 3: **0.4182** | HAY, TEMPLE, JACKPOT, PLAYWRIGHT                                  | INCORRECT (Max overlap: 2/4 with HIT THE ___)
   - Group 4: **0.3513** | GABLE, ROOF, ROAD, SWORD                                          | INCORRECT (Max overlap: 2/4 with HIT THE ___) | [Pred Type: SEMANTIC_SET (55.9%, no-rel 24.0%)]
   - Group 5: **0.4434** | HAY, ROAD, JACKPOT, PLAYWRIGHT                                    | INCORRECT (Max overlap: 3/4 with HIT THE ___)
   - Group 6: **0.3379** | GABLE, ROOF, TEMPLE, SWORD                                        | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD) | [Pred Type: SEMANTIC_SET (62.5%, no-rel 20.6%)]
   - Group 7: **0.5484** | GARLAND, WRAP, WREATH, GIFT                                       | INCORRECT (Max overlap: 2/4 with SILENT “W”) | [Pred Type: SYNONYM_OR_NEAR (56.7%, no-rel 27.5%)]
   - Group 8: **0.4992** | BENT, FACULTY, FLAIR, DEAN                                        | INCORRECT (Max overlap: 3/4 with APTITUDE)
   - Group 9: **0.5313** | BENT, FACULTY, FLAIR, GIFT                                        | CORRECT GROUP (APTITUDE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 37.5%)]
   - Group 10: **0.4951** | GARLAND, WRAP, WREATH, DEAN                                       | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 28.1%)]
   - Group 11: **0.4826** | BENT, FLAIR, WREATH, DEAN                                         | INCORRECT (Max overlap: 2/4 with APTITUDE)
   - Group 12: **0.4810** | GARLAND, FACULTY, WRAP, GIFT                                      | INCORRECT (Max overlap: 2/4 with APTITUDE)
   - Group 13: **0.4771** | GARLAND, BENT, FLAIR, WREATH                                      | INCORRECT (Max overlap: 2/4 with APTITUDE) | [Pred Type: SYNONYM_OR_NEAR (57.7%, no-rel 31.3%)]
   - Group 14: **0.4754** | FACULTY, WRAP, DEAN, GIFT                                         | INCORRECT (Max overlap: 2/4 with APTITUDE)
   - Group 15: **0.5858** | GARLAND, FACULTY, FLAIR, DEAN                                     | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD)
   - Group 16: **0.4648** | BENT, WRAP, WREATH, GIFT                                          | INCORRECT (Max overlap: 2/4 with APTITUDE)
   - Group 17: **0.4863** | GARLAND, BENT, FLAIR, DEAN                                        | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD)
   - Group 18: **0.4608** | FACULTY, WRAP, WREATH, GIFT                                       | INCORRECT (Max overlap: 2/4 with APTITUDE)
   - Group 19: **0.4641** | BENT, FACULTY, WREATH, GIFT                                       | INCORRECT (Max overlap: 3/4 with APTITUDE)
   - Group 20: **0.4605** | GARLAND, WRAP, FLAIR, DEAN                                        | INCORRECT (Max overlap: 2/4 with LEGENDS OF CLASSIC HOLLYWOOD)

---

## Puzzle 66 (ID: 513)
**Words on Board:** TURTLE, DONKEY, CARPET, PRINCESS, FLEECE, MUSHROOM, MARKER, EGG, CLAM, NUT, OGRE, KINGDOM, DRAGON, PEACH, PIPE CLEANER, CATERPILLAR

### Ground Truth Categories:
* **Level 0 (THINGS THAT ARE FUZZY) [Type: SEMANTIC_SET]:** CATERPILLAR, FLEECE, PEACH, PIPE CLEANER
* **Level 1 (THINGS WITH SHELLS) [Type: SEMANTIC_SET]:** CLAM, EGG, NUT, TURTLE
* **Level 2 (FIGURES IN “SHREK”) [Type: NAMED_ENTITY_SET]:** DONKEY, DRAGON, OGRE, PRINCESS
* **Level 3 (MAGIC ___) [Type: FILL_IN_THE_BLANK]:** CARPET, KINGDOM, MARKER, MUSHROOM

### Top Candidate Partitions:
1. **Partition Score: 0.4809**
   - Group 1: **0.5762** | DONKEY, PRINCESS, OGRE, KINGDOM                                   | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”)
   - Group 2: **0.5578** | EGG, CLAM, NUT, PEACH                                             | INCORRECT (Max overlap: 3/4 with THINGS WITH SHELLS)
   - Group 3: **0.4662** | TURTLE, DRAGON, PIPE CLEANER, CATERPILLAR                         | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE FUZZY) | [Pred Type: SEMANTIC_SET (55.3%, no-rel 26.9%)]
   - Group 4: **0.4498** | CARPET, FLEECE, MUSHROOM, MARKER                                  | INCORRECT (Max overlap: 3/4 with MAGIC ___) | [Pred Type: SEMANTIC_SET (51.0%, no-rel 31.3%)]
2. **Partition Score: 0.4798**
   - Group 1: **0.5810** | PRINCESS, OGRE, KINGDOM, DRAGON                                   | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”) | [Pred Type: NAMED_ENTITY_SET (46.9%, no-rel 17.1%)]
   - Group 2: **0.5578** | EGG, CLAM, NUT, PEACH                                             | INCORRECT (Max overlap: 3/4 with THINGS WITH SHELLS)
   - Group 3: **0.4616** | TURTLE, DONKEY, PIPE CLEANER, CATERPILLAR                         | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE FUZZY)
   - Group 4: **0.4498** | CARPET, FLEECE, MUSHROOM, MARKER                                  | INCORRECT (Max overlap: 3/4 with MAGIC ___) | [Pred Type: SEMANTIC_SET (51.0%, no-rel 31.3%)]
3. **Partition Score: 0.4749**
   - Group 1: **0.5838** | DONKEY, PRINCESS, KINGDOM, DRAGON                                 | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”) | [Pred Type: NAMED_ENTITY_SET (46.0%, no-rel 19.8%)]
   - Group 2: **0.5578** | EGG, CLAM, NUT, PEACH                                             | INCORRECT (Max overlap: 3/4 with THINGS WITH SHELLS)
   - Group 3: **0.4498** | CARPET, FLEECE, MUSHROOM, MARKER                                  | INCORRECT (Max overlap: 3/4 with MAGIC ___) | [Pred Type: SEMANTIC_SET (51.0%, no-rel 31.3%)]
   - Group 4: **0.4460** | TURTLE, OGRE, PIPE CLEANER, CATERPILLAR                           | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE FUZZY)
4. **Partition Score: 0.4727**
   - Group 1: **0.5578** | EGG, CLAM, NUT, PEACH                                             | INCORRECT (Max overlap: 3/4 with THINGS WITH SHELLS)
   - Group 2: **0.4973** | DONKEY, OGRE, KINGDOM, PIPE CLEANER                               | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 3: **0.4939** | TURTLE, PRINCESS, DRAGON, CATERPILLAR                             | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”) | [Pred Type: SEMANTIC_SET (51.7%, no-rel 19.7%)]
   - Group 4: **0.4498** | CARPET, FLEECE, MUSHROOM, MARKER                                  | INCORRECT (Max overlap: 3/4 with MAGIC ___) | [Pred Type: SEMANTIC_SET (51.0%, no-rel 31.3%)]
5. **Partition Score: 0.4707**
   - Group 1: **0.5578** | EGG, CLAM, NUT, PEACH                                             | INCORRECT (Max overlap: 3/4 with THINGS WITH SHELLS)
   - Group 2: **0.5136** | TURTLE, OGRE, DRAGON, CATERPILLAR                                 | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 3: **0.4697** | DONKEY, PRINCESS, KINGDOM, PIPE CLEANER                           | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 4: **0.4498** | CARPET, FLEECE, MUSHROOM, MARKER                                  | INCORRECT (Max overlap: 3/4 with MAGIC ___) | [Pred Type: SEMANTIC_SET (51.0%, no-rel 31.3%)]

### Top Candidate Groups:
   - Group 1: **0.5762** | DONKEY, PRINCESS, OGRE, KINGDOM                                   | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”)
   - Group 2: **0.5578** | EGG, CLAM, NUT, PEACH                                             | INCORRECT (Max overlap: 3/4 with THINGS WITH SHELLS)
   - Group 3: **0.4662** | TURTLE, DRAGON, PIPE CLEANER, CATERPILLAR                         | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE FUZZY) | [Pred Type: SEMANTIC_SET (55.3%, no-rel 26.9%)]
   - Group 4: **0.4498** | CARPET, FLEECE, MUSHROOM, MARKER                                  | INCORRECT (Max overlap: 3/4 with MAGIC ___) | [Pred Type: SEMANTIC_SET (51.0%, no-rel 31.3%)]
   - Group 5: **0.5810** | PRINCESS, OGRE, KINGDOM, DRAGON                                   | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”) | [Pred Type: NAMED_ENTITY_SET (46.9%, no-rel 17.1%)]
   - Group 6: **0.4616** | TURTLE, DONKEY, PIPE CLEANER, CATERPILLAR                         | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE FUZZY)
   - Group 7: **0.5838** | DONKEY, PRINCESS, KINGDOM, DRAGON                                 | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”) | [Pred Type: NAMED_ENTITY_SET (46.0%, no-rel 19.8%)]
   - Group 8: **0.4460** | TURTLE, OGRE, PIPE CLEANER, CATERPILLAR                           | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE FUZZY)
   - Group 9: **0.4973** | DONKEY, OGRE, KINGDOM, PIPE CLEANER                               | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 10: **0.4939** | TURTLE, PRINCESS, DRAGON, CATERPILLAR                             | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”) | [Pred Type: SEMANTIC_SET (51.7%, no-rel 19.7%)]
   - Group 11: **0.5136** | TURTLE, OGRE, DRAGON, CATERPILLAR                                 | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 12: **0.4697** | DONKEY, PRINCESS, KINGDOM, PIPE CLEANER                           | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 13: **0.5225** | TURTLE, DONKEY, DRAGON, CATERPILLAR                               | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 14: **0.4577** | PRINCESS, OGRE, KINGDOM, PIPE CLEANER                             | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 15: **0.5632** | TURTLE, DONKEY, KINGDOM, DRAGON                                   | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 16: **0.4316** | PRINCESS, OGRE, PIPE CLEANER, CATERPILLAR                         | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 17: **0.4970** | DONKEY, KINGDOM, DRAGON, PIPE CLEANER                             | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 18: **0.4716** | TURTLE, PRINCESS, OGRE, CATERPILLAR                               | INCORRECT (Max overlap: 2/4 with FIGURES IN “SHREK”)
   - Group 19: **0.5433** | TURTLE, DONKEY, PRINCESS, DRAGON                                  | INCORRECT (Max overlap: 3/4 with FIGURES IN “SHREK”)
   - Group 20: **0.4362** | OGRE, KINGDOM, PIPE CLEANER, CATERPILLAR                          | INCORRECT (Max overlap: 2/4 with THINGS THAT ARE FUZZY)

---

## Puzzle 67 (ID: 999)
**Words on Board:** WEARABLE, WHEREFORE, FISHBOWL, WAREHOUSE, FOZZIE, HOT SEAT, MICROSCOPE, VIDEO GAME, GONZO, SPOTLIGHT, ANIMAL, COMPANY, BEAKER, E STREET BAND, MAFIA, WEREWOLF

### Ground Truth Categories:
* **Level 0 (STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY) [Type: SOUND_OR_SPELLING]:** WAREHOUSE, WEARABLE, WEREWOLF, WHEREFORE
* **Level 1 (METAPHORS FOR PUBLIC SCRUTINY) [Type: COMMON_PHRASE]:** FISHBOWL, HOT SEAT, MICROSCOPE, SPOTLIGHT
* **Level 2 (MUPPETS) [Type: NAMED_ENTITY_SET]:** ANIMAL, BEAKER, FOZZIE, GONZO
* **Level 3 (THEY FEATURE A BOSS) [Type: SEMANTIC_SET]:** COMPANY, E STREET BAND, MAFIA, VIDEO GAME

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.5661** | FISHBOWL, WAREHOUSE, MICROSCOPE, BEAKER                           | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY) | [Pred Type: SEMANTIC_SET (46.9%, no-rel 25.8%)]
   - Group 2: **0.5609** | FISHBOWL, WAREHOUSE, MICROSCOPE, SPOTLIGHT                        | INCORRECT (Max overlap: 3/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 3: **0.5602** | FISHBOWL, WAREHOUSE, COMPANY, MAFIA                               | INCORRECT (Max overlap: 2/4 with THEY FEATURE A BOSS)
   - Group 4: **0.5597** | WEARABLE, WHEREFORE, WAREHOUSE, WEREWOLF                          | CORRECT GROUP (STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY, Level 0)
   - Group 5: **0.5587** | WEARABLE, WHEREFORE, WAREHOUSE, SPOTLIGHT                         | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 6: **0.5491** | WEARABLE, FISHBOWL, WAREHOUSE, SPOTLIGHT                          | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 7: **0.5471** | FISHBOWL, WAREHOUSE, VIDEO GAME, COMPANY                          | INCORRECT (Max overlap: 2/4 with THEY FEATURE A BOSS)
   - Group 8: **0.5410** | WEARABLE, FISHBOWL, WAREHOUSE, COMPANY                            | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 9: **0.5403** | FISHBOWL, WAREHOUSE, MICROSCOPE, COMPANY                          | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 10: **0.5401** | WEARABLE, WAREHOUSE, MICROSCOPE, SPOTLIGHT                        | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 11: **0.5389** | FISHBOWL, VIDEO GAME, COMPANY, MAFIA                              | INCORRECT (Max overlap: 3/4 with THEY FEATURE A BOSS)
   - Group 12: **0.5385** | WEARABLE, FISHBOWL, WAREHOUSE, MICROSCOPE                         | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 13: **0.5371** | WEARABLE, FISHBOWL, WAREHOUSE, VIDEO GAME                         | INCORRECT (Max overlap: 2/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 14: **0.5357** | FISHBOWL, WAREHOUSE, HOT SEAT, SPOTLIGHT                          | INCORRECT (Max overlap: 3/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 15: **0.5338** | WEARABLE, WAREHOUSE, ANIMAL, WEREWOLF                             | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 16: **0.5329** | FISHBOWL, WAREHOUSE, VIDEO GAME, MAFIA                            | INCORRECT (Max overlap: 2/4 with THEY FEATURE A BOSS)
   - Group 17: **0.5327** | WEARABLE, FISHBOWL, MICROSCOPE, SPOTLIGHT                         | INCORRECT (Max overlap: 3/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 18: **0.5325** | FISHBOWL, WAREHOUSE, SPOTLIGHT, E STREET BAND                     | INCORRECT (Max overlap: 2/4 with METAPHORS FOR PUBLIC SCRUTINY)
   - Group 19: **0.5324** | WEARABLE, WHEREFORE, FISHBOWL, WAREHOUSE                          | INCORRECT (Max overlap: 3/4 with STARTING WITH THE SAME SOUND, SPELLED DIFFERENTLY)
   - Group 20: **0.5320** | WAREHOUSE, VIDEO GAME, COMPANY, MAFIA                             | INCORRECT (Max overlap: 3/4 with THEY FEATURE A BOSS)

---

## Puzzle 68 (ID: 738)
**Words on Board:** RIGHT, COFFEE, PEA, COLD, ASTRONAUT, SMACK, WINDY, RANKLE, SHIP, LEAR, BARM, WET, WHALE, DEAD, GRAY, EXACTLY

### Ground Truth Categories:
* **Level 0 (QUALITIES OF A RAINY DAY) [Type: SEMANTIC_SET]:** COLD, GRAY, WET, WINDY
* **Level 1 (SQUARELY) [Type: SYNONYM_OR_NEAR]:** DEAD, EXACTLY, RIGHT, SMACK
* **Level 2 (CONTENTS OF A POD) [Type: FILL_IN_THE_BLANK]:** ASTRONAUT, COFFEE, PEA, WHALE
* **Level 3 (BODY PART PLUS A STARTING LETTER) [Type: WORDPLAY_TRANSFORM]:** BARM, LEAR, RANKLE, SHIP

### Top Candidate Partitions:
1. **Partition Score: 0.4880**
   - Group 1: **0.6013** | COLD, WINDY, WET, DEAD                                            | INCORRECT (Max overlap: 3/4 with QUALITIES OF A RAINY DAY)
   - Group 2: **0.5573** | ASTRONAUT, LEAR, BARM, WHALE                                      | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD)
   - Group 3: **0.4765** | COFFEE, PEA, SHIP, GRAY                                           | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD) | [Pred Type: FILL_IN_THE_BLANK (49.1%, no-rel 24.3%)]
   - Group 4: **0.4592** | RIGHT, SMACK, RANKLE, EXACTLY                                     | INCORRECT (Max overlap: 3/4 with SQUARELY) | [Pred Type: SYNONYM_OR_NEAR (47.6%, no-rel 35.7%)]
2. **Partition Score: 0.4777**
   - Group 1: **0.5618** | RIGHT, SMACK, WINDY, EXACTLY                                      | INCORRECT (Max overlap: 3/4 with SQUARELY)
   - Group 2: **0.5573** | ASTRONAUT, LEAR, BARM, WHALE                                      | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD)
   - Group 3: **0.4765** | COFFEE, PEA, SHIP, GRAY                                           | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD) | [Pred Type: FILL_IN_THE_BLANK (49.1%, no-rel 24.3%)]
   - Group 4: **0.4385** | COLD, RANKLE, WET, DEAD                                           | INCORRECT (Max overlap: 2/4 with QUALITIES OF A RAINY DAY)
3. **Partition Score: 0.4773**
   - Group 1: **0.4922** | ASTRONAUT, LEAR, BARM, GRAY                                       | INCORRECT (Max overlap: 2/4 with BODY PART PLUS A STARTING LETTER)
   - Group 2: **0.4904** | RIGHT, COLD, WINDY, WET                                           | INCORRECT (Max overlap: 3/4 with QUALITIES OF A RAINY DAY)
   - Group 3: **0.4849** | COFFEE, PEA, SHIP, WHALE                                          | INCORRECT (Max overlap: 3/4 with CONTENTS OF A POD) | [Pred Type: FILL_IN_THE_BLANK (46.5%, no-rel 23.7%)]
   - Group 4: **0.4669** | SMACK, RANKLE, DEAD, EXACTLY                                      | INCORRECT (Max overlap: 3/4 with SQUARELY)
4. **Partition Score: 0.4752**
   - Group 1: **0.5573** | ASTRONAUT, LEAR, BARM, WHALE                                      | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD)
   - Group 2: **0.4904** | RIGHT, COLD, WINDY, WET                                           | INCORRECT (Max overlap: 3/4 with QUALITIES OF A RAINY DAY)
   - Group 3: **0.4765** | COFFEE, PEA, SHIP, GRAY                                           | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD) | [Pred Type: FILL_IN_THE_BLANK (49.1%, no-rel 24.3%)]
   - Group 4: **0.4669** | SMACK, RANKLE, DEAD, EXACTLY                                      | INCORRECT (Max overlap: 3/4 with SQUARELY)
5. **Partition Score: 0.4739**
   - Group 1: **0.6013** | COLD, WINDY, WET, DEAD                                            | INCORRECT (Max overlap: 3/4 with QUALITIES OF A RAINY DAY)
   - Group 2: **0.4922** | ASTRONAUT, LEAR, BARM, GRAY                                       | INCORRECT (Max overlap: 2/4 with BODY PART PLUS A STARTING LETTER)
   - Group 3: **0.4849** | COFFEE, PEA, SHIP, WHALE                                          | INCORRECT (Max overlap: 3/4 with CONTENTS OF A POD) | [Pred Type: FILL_IN_THE_BLANK (46.5%, no-rel 23.7%)]
   - Group 4: **0.4592** | RIGHT, SMACK, RANKLE, EXACTLY                                     | INCORRECT (Max overlap: 3/4 with SQUARELY) | [Pred Type: SYNONYM_OR_NEAR (47.6%, no-rel 35.7%)]

### Top Candidate Groups:
   - Group 1: **0.6013** | COLD, WINDY, WET, DEAD                                            | INCORRECT (Max overlap: 3/4 with QUALITIES OF A RAINY DAY)
   - Group 2: **0.5573** | ASTRONAUT, LEAR, BARM, WHALE                                      | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD)
   - Group 3: **0.4765** | COFFEE, PEA, SHIP, GRAY                                           | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD) | [Pred Type: FILL_IN_THE_BLANK (49.1%, no-rel 24.3%)]
   - Group 4: **0.4592** | RIGHT, SMACK, RANKLE, EXACTLY                                     | INCORRECT (Max overlap: 3/4 with SQUARELY) | [Pred Type: SYNONYM_OR_NEAR (47.6%, no-rel 35.7%)]
   - Group 5: **0.5618** | RIGHT, SMACK, WINDY, EXACTLY                                      | INCORRECT (Max overlap: 3/4 with SQUARELY)
   - Group 6: **0.4385** | COLD, RANKLE, WET, DEAD                                           | INCORRECT (Max overlap: 2/4 with QUALITIES OF A RAINY DAY)
   - Group 7: **0.4922** | ASTRONAUT, LEAR, BARM, GRAY                                       | INCORRECT (Max overlap: 2/4 with BODY PART PLUS A STARTING LETTER)
   - Group 8: **0.4904** | RIGHT, COLD, WINDY, WET                                           | INCORRECT (Max overlap: 3/4 with QUALITIES OF A RAINY DAY)
   - Group 9: **0.4849** | COFFEE, PEA, SHIP, WHALE                                          | INCORRECT (Max overlap: 3/4 with CONTENTS OF A POD) | [Pred Type: FILL_IN_THE_BLANK (46.5%, no-rel 23.7%)]
   - Group 10: **0.4669** | SMACK, RANKLE, DEAD, EXACTLY                                      | INCORRECT (Max overlap: 3/4 with SQUARELY)
   - Group 11: **0.4998** | COFFEE, PEA, ASTRONAUT, SHIP                                      | INCORRECT (Max overlap: 3/4 with CONTENTS OF A POD)
   - Group 12: **0.4638** | LEAR, BARM, WHALE, GRAY                                           | INCORRECT (Max overlap: 2/4 with BODY PART PLUS A STARTING LETTER)
   - Group 13: **0.5222** | ASTRONAUT, RANKLE, LEAR, BARM                                     | INCORRECT (Max overlap: 3/4 with BODY PART PLUS A STARTING LETTER)
   - Group 14: **0.4286** | COLD, WET, DEAD, GRAY                                             | INCORRECT (Max overlap: 3/4 with QUALITIES OF A RAINY DAY) | [Pred Type: SYNONYM_OR_NEAR (46.8%, no-rel 24.7%)]
   - Group 15: **0.5056** | RANKLE, LEAR, BARM, WHALE                                         | INCORRECT (Max overlap: 3/4 with BODY PART PLUS A STARTING LETTER)
   - Group 16: **0.6034** | RIGHT, SMACK, DEAD, EXACTLY                                       | CORRECT GROUP (SQUARELY, Level 1)
   - Group 17: **0.4138** | COLD, WINDY, RANKLE, WET                                          | INCORRECT (Max overlap: 3/4 with QUALITIES OF A RAINY DAY)
   - Group 18: **0.4793** | COFFEE, ASTRONAUT, SHIP, BARM                                     | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD)
   - Group 19: **0.4576** | PEA, LEAR, WHALE, GRAY                                            | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD)
   - Group 20: **0.4742** | COFFEE, ASTRONAUT, LEAR, BARM                                     | INCORRECT (Max overlap: 2/4 with CONTENTS OF A POD)

---

## Puzzle 69 (ID: 898)
**Words on Board:** FLOW, IRA, TAB, APR, KAT, CFO, DEB, MAR, SEC, MIGHT, SUE, CAN, JAN, COULD, MAY, GOD

### Ground Truth Categories:
* **Level 0 (VERBS EXPRESSING POSSIBILITY) [Type: SYNONYM_OR_NEAR]:** CAN, COULD, MAY, MIGHT
* **Level 1 (WOMEN’S NICKNAMES) [Type: NAMED_ENTITY_SET]:** DEB, JAN, KAT, SUE
* **Level 2 (FINANCIAL ABBREVIATIONS) [Type: NAMED_ENTITY_SET]:** APR, CFO, IRA, SEC
* **Level 3 (BACKWARDS ANIMALS) [Type: WORDPLAY_TRANSFORM]:** FLOW, GOD, MAR, TAB

### Top Candidate Partitions:
1. **Partition Score: 0.4542**
   - Group 1: **0.5978** | MIGHT, CAN, COULD, MAY                                            | CORRECT GROUP (VERBS EXPRESSING POSSIBILITY, Level 0)
   - Group 2: **0.5929** | APR, CFO, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 3: **0.4154** | FLOW, IRA, SEC, SUE                                               | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 4: **0.4043** | TAB, KAT, DEB, GOD                                                | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
2. **Partition Score: 0.4503**
   - Group 1: **0.6050** | APR, KAT, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with WOMEN’S NICKNAMES)
   - Group 2: **0.5978** | MIGHT, CAN, COULD, MAY                                            | CORRECT GROUP (VERBS EXPRESSING POSSIBILITY, Level 0)
   - Group 3: **0.4066** | FLOW, CFO, SUE, GOD                                               | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 4: **0.3983** | IRA, TAB, DEB, SEC                                                | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
3. **Partition Score: 0.4475**
   - Group 1: **0.6050** | APR, KAT, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with WOMEN’S NICKNAMES)
   - Group 2: **0.5978** | MIGHT, CAN, COULD, MAY                                            | CORRECT GROUP (VERBS EXPRESSING POSSIBILITY, Level 0)
   - Group 3: **0.4297** | IRA, CFO, SUE, GOD                                                | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 4: **0.3813** | FLOW, TAB, DEB, SEC                                               | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
4. **Partition Score: 0.4333**
   - Group 1: **0.5978** | MIGHT, CAN, COULD, MAY                                            | CORRECT GROUP (VERBS EXPRESSING POSSIBILITY, Level 0)
   - Group 2: **0.5563** | APR, DEB, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with WOMEN’S NICKNAMES)
   - Group 3: **0.4154** | FLOW, IRA, SEC, SUE                                               | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 4: **0.3807** | TAB, KAT, CFO, GOD                                                | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
5. **Partition Score: 0.4315**
   - Group 1: **0.6050** | APR, KAT, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with WOMEN’S NICKNAMES)
   - Group 2: **0.5978** | MIGHT, CAN, COULD, MAY                                            | CORRECT GROUP (VERBS EXPRESSING POSSIBILITY, Level 0)
   - Group 3: **0.3813** | TAB, DEB, SEC, GOD                                                | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 4: **0.3734** | FLOW, IRA, CFO, SUE                                               | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)

### Top Candidate Groups:
   - Group 1: **0.5978** | MIGHT, CAN, COULD, MAY                                            | CORRECT GROUP (VERBS EXPRESSING POSSIBILITY, Level 0)
   - Group 2: **0.5929** | APR, CFO, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 3: **0.4154** | FLOW, IRA, SEC, SUE                                               | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 4: **0.4043** | TAB, KAT, DEB, GOD                                                | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 5: **0.6050** | APR, KAT, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with WOMEN’S NICKNAMES)
   - Group 6: **0.4066** | FLOW, CFO, SUE, GOD                                               | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 7: **0.3983** | IRA, TAB, DEB, SEC                                                | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 8: **0.4297** | IRA, CFO, SUE, GOD                                                | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 9: **0.3813** | FLOW, TAB, DEB, SEC                                               | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 10: **0.5563** | APR, DEB, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with WOMEN’S NICKNAMES)
   - Group 11: **0.3807** | TAB, KAT, CFO, GOD                                                | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 12: **0.3813** | TAB, DEB, SEC, GOD                                                | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 13: **0.3734** | FLOW, IRA, CFO, SUE                                               | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 14: **0.3898** | FLOW, CFO, SEC, SUE                                               | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)
   - Group 15: **0.3686** | IRA, TAB, DEB, GOD                                                | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 16: **0.4032** | FLOW, SEC, SUE, GOD                                               | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 17: **0.3641** | IRA, TAB, KAT, DEB                                                | INCORRECT (Max overlap: 2/4 with WOMEN’S NICKNAMES)
   - Group 18: **0.5127** | IRA, APR, CFO, JAN                                                | INCORRECT (Max overlap: 3/4 with FINANCIAL ABBREVIATIONS)
   - Group 19: **0.4046** | TAB, KAT, DEB, MAR                                                | INCORRECT (Max overlap: 2/4 with BACKWARDS ANIMALS)
   - Group 20: **0.5382** | IRA, APR, MAR, JAN                                                | INCORRECT (Max overlap: 2/4 with FINANCIAL ABBREVIATIONS)

---

## Puzzle 70 (ID: 741)
**Words on Board:** THICK, MALT, CONCERN, STOUT, BUTTER, GERM, CIDER, SQUAT, FIRM, PORT, HOUSE, SOLID, SAUCE, BRANDY, LUXE, OUTFIT

### Ground Truth Categories:
* **Level 0 (STOCKY) [Type: SYNONYM_OR_NEAR]:** SOLID, SQUAT, STOUT, THICK
* **Level 1 (COMPANY) [Type: SYNONYM_OR_NEAR]:** CONCERN, FIRM, HOUSE, OUTFIT
* **Level 2 (APPLE PRODUCTS) [Type: SEMANTIC_SET]:** BRANDY, BUTTER, CIDER, SAUCE
* **Level 3 (STARTS OF EUROPEAN COUNTRIES) [Type: WORDPLAY_TRANSFORM]:** GERM, LUXE, MALT, PORT

### Top Candidate Partitions:
1. **Partition Score: 0.4604**
   - Group 1: **0.5823** | BUTTER, CIDER, SAUCE, BRANDY                                      | CORRECT GROUP (APPLE PRODUCTS, Level 2) | [Pred Type: SEMANTIC_SET (55.3%, no-rel 23.3%)]
   - Group 2: **0.5033** | THICK, CONCERN, SQUAT, SOLID                                      | INCORRECT (Max overlap: 3/4 with STOCKY)
   - Group 3: **0.4960** | MALT, STOUT, GERM, LUXE                                           | INCORRECT (Max overlap: 3/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 4: **0.4212** | FIRM, PORT, HOUSE, OUTFIT                                         | INCORRECT (Max overlap: 3/4 with COMPANY) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 28.9%)]
2. **Partition Score: 0.4590**
   - Group 1: **0.5539** | MALT, BUTTER, CIDER, SAUCE                                        | INCORRECT (Max overlap: 3/4 with APPLE PRODUCTS) | [Pred Type: SEMANTIC_SET (50.4%, no-rel 22.9%)]
   - Group 2: **0.5033** | THICK, CONCERN, SQUAT, SOLID                                      | INCORRECT (Max overlap: 3/4 with STOCKY)
   - Group 3: **0.4902** | STOUT, GERM, BRANDY, LUXE                                         | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 4: **0.4212** | FIRM, PORT, HOUSE, OUTFIT                                         | INCORRECT (Max overlap: 3/4 with COMPANY) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 28.9%)]
3. **Partition Score: 0.4569**
   - Group 1: **0.5473** | CONCERN, FIRM, HOUSE, OUTFIT                                      | CORRECT GROUP (COMPANY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 27.2%)]
   - Group 2: **0.5319** | GERM, CIDER, BRANDY, LUXE                                         | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 3: **0.4954** | THICK, STOUT, SQUAT, SOLID                                        | CORRECT GROUP (STOCKY, Level 0)
   - Group 4: **0.4002** | MALT, BUTTER, PORT, SAUCE                                         | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES) | [Pred Type: SEMANTIC_SET (49.7%, no-rel 27.1%)]
4. **Partition Score: 0.4539**
   - Group 1: **0.5473** | CONCERN, FIRM, HOUSE, OUTFIT                                      | CORRECT GROUP (COMPANY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 27.2%)]
   - Group 2: **0.5084** | MALT, GERM, BRANDY, LUXE                                          | INCORRECT (Max overlap: 3/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 3: **0.4954** | THICK, STOUT, SQUAT, SOLID                                        | CORRECT GROUP (STOCKY, Level 0)
   - Group 4: **0.4060** | BUTTER, CIDER, PORT, SAUCE                                        | INCORRECT (Max overlap: 3/4 with APPLE PRODUCTS) | [Pred Type: SEMANTIC_SET (51.9%, no-rel 25.8%)]
5. **Partition Score: 0.4509**
   - Group 1: **0.5099** | MALT, BUTTER, SAUCE, BRANDY                                       | INCORRECT (Max overlap: 3/4 with APPLE PRODUCTS) | [Pred Type: SEMANTIC_SET (54.9%, no-rel 20.4%)]
   - Group 2: **0.5033** | THICK, CONCERN, SQUAT, SOLID                                      | INCORRECT (Max overlap: 3/4 with STOCKY)
   - Group 3: **0.4580** | STOUT, GERM, CIDER, LUXE                                          | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 4: **0.4212** | FIRM, PORT, HOUSE, OUTFIT                                         | INCORRECT (Max overlap: 3/4 with COMPANY) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 28.9%)]

### Top Candidate Groups:
   - Group 1: **0.5823** | BUTTER, CIDER, SAUCE, BRANDY                                      | CORRECT GROUP (APPLE PRODUCTS, Level 2) | [Pred Type: SEMANTIC_SET (55.3%, no-rel 23.3%)]
   - Group 2: **0.5033** | THICK, CONCERN, SQUAT, SOLID                                      | INCORRECT (Max overlap: 3/4 with STOCKY)
   - Group 3: **0.4960** | MALT, STOUT, GERM, LUXE                                           | INCORRECT (Max overlap: 3/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 4: **0.4212** | FIRM, PORT, HOUSE, OUTFIT                                         | INCORRECT (Max overlap: 3/4 with COMPANY) | [Pred Type: SYNONYM_OR_NEAR (54.3%, no-rel 28.9%)]
   - Group 5: **0.5539** | MALT, BUTTER, CIDER, SAUCE                                        | INCORRECT (Max overlap: 3/4 with APPLE PRODUCTS) | [Pred Type: SEMANTIC_SET (50.4%, no-rel 22.9%)]
   - Group 6: **0.4902** | STOUT, GERM, BRANDY, LUXE                                         | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 7: **0.5473** | CONCERN, FIRM, HOUSE, OUTFIT                                      | CORRECT GROUP (COMPANY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (62.0%, no-rel 27.2%)]
   - Group 8: **0.5319** | GERM, CIDER, BRANDY, LUXE                                         | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 9: **0.4954** | THICK, STOUT, SQUAT, SOLID                                        | CORRECT GROUP (STOCKY, Level 0)
   - Group 10: **0.4002** | MALT, BUTTER, PORT, SAUCE                                         | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES) | [Pred Type: SEMANTIC_SET (49.7%, no-rel 27.1%)]
   - Group 11: **0.5084** | MALT, GERM, BRANDY, LUXE                                          | INCORRECT (Max overlap: 3/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 12: **0.4060** | BUTTER, CIDER, PORT, SAUCE                                        | INCORRECT (Max overlap: 3/4 with APPLE PRODUCTS) | [Pred Type: SEMANTIC_SET (51.9%, no-rel 25.8%)]
   - Group 13: **0.5099** | MALT, BUTTER, SAUCE, BRANDY                                       | INCORRECT (Max overlap: 3/4 with APPLE PRODUCTS) | [Pred Type: SEMANTIC_SET (54.9%, no-rel 20.4%)]
   - Group 14: **0.4580** | STOUT, GERM, CIDER, LUXE                                          | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 15: **0.5472** | THICK, SQUAT, FIRM, SOLID                                         | INCORRECT (Max overlap: 3/4 with STOCKY) | [Pred Type: SYNONYM_OR_NEAR (52.9%, no-rel 38.9%)]
   - Group 16: **0.3777** | CONCERN, PORT, HOUSE, OUTFIT                                      | INCORRECT (Max overlap: 3/4 with COMPANY)
   - Group 17: **0.5098** | BUTTER, GERM, BRANDY, LUXE                                        | INCORRECT (Max overlap: 2/4 with APPLE PRODUCTS)
   - Group 18: **0.3930** | MALT, CIDER, PORT, SAUCE                                          | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 19: **0.5025** | MALT, STOUT, BRANDY, LUXE                                         | INCORRECT (Max overlap: 2/4 with STARTS OF EUROPEAN COUNTRIES)
   - Group 20: **0.4460** | BUTTER, GERM, CIDER, SAUCE                                        | INCORRECT (Max overlap: 3/4 with APPLE PRODUCTS) | [Pred Type: SEMANTIC_SET (56.5%, no-rel 21.3%)]

---

## Puzzle 71 (ID: 4)
**Words on Board:** SWEEP, CAROUSEL, BAT, MOP, SPIDER, REEBOK, ADIDAS, DUST, IRON, PUMA, SUPER, CATS, VACUUM, NIKE, CABARET, CHICAGO

### Ground Truth Categories:
* **Level 0 (SNEAKER BRANDS) [Type: NAMED_ENTITY_SET]:** ADIDAS, NIKE, PUMA, REEBOK
* **Level 1 (MUSICALS BEGINNING WITH “C”) [Type: WORD_FORM]:** CABARET, CAROUSEL, CATS, CHICAGO
* **Level 2 (CLEANING VERBS) [Type: SYNONYM_OR_NEAR]:** DUST, MOP, SWEEP, VACUUM
* **Level 3 (___ MAN SUPERHEROES) [Type: FILL_IN_THE_BLANK]:** BAT, IRON, SPIDER, SUPER

### Top Candidate Partitions:
1. **Partition Score: 0.4011**
   - Group 1: **0.5898** | ADIDAS, PUMA, SUPER, NIKE                                         | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS)
   - Group 2: **0.5176** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 3: **0.3803** | CAROUSEL, REEBOK, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
   - Group 4: **0.3533** | BAT, MOP, SPIDER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
2. **Partition Score: 0.3979**
   - Group 1: **0.5613** | REEBOK, PUMA, SUPER, NIKE                                         | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.0%, no-rel 23.0%)]
   - Group 2: **0.5176** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 3: **0.3675** | CAROUSEL, ADIDAS, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
   - Group 4: **0.3533** | BAT, MOP, SPIDER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
3. **Partition Score: 0.3968**
   - Group 1: **0.5176** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 2: **0.4708** | ADIDAS, SUPER, NIKE, CHICAGO                                      | INCORRECT (Max overlap: 2/4 with SNEAKER BRANDS)
   - Group 3: **0.4099** | CAROUSEL, REEBOK, PUMA, CABARET                                   | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (46.5%, no-rel 17.7%)]
   - Group 4: **0.3533** | BAT, MOP, SPIDER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
4. **Partition Score: 0.3945**
   - Group 1: **0.5394** | REEBOK, ADIDAS, PUMA, SUPER                                       | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS)
   - Group 2: **0.5176** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 3: **0.3540** | CAROUSEL, NIKE, CABARET, CHICAGO                                  | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (46.0%, no-rel 18.0%)]
   - Group 4: **0.3533** | BAT, MOP, SPIDER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
5. **Partition Score: 0.3919**
   - Group 1: **0.5176** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 2: **0.4705** | CAROUSEL, REEBOK, ADIDAS, NIKE                                    | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (55.5%, no-rel 15.4%)]
   - Group 3: **0.3907** | PUMA, SUPER, CABARET, CHICAGO                                     | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”)
   - Group 4: **0.3533** | BAT, MOP, SPIDER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)

### Top Candidate Groups:
   - Group 1: **0.5898** | ADIDAS, PUMA, SUPER, NIKE                                         | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS)
   - Group 2: **0.5176** | SWEEP, DUST, IRON, VACUUM                                         | INCORRECT (Max overlap: 3/4 with CLEANING VERBS)
   - Group 3: **0.3803** | CAROUSEL, REEBOK, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
   - Group 4: **0.3533** | BAT, MOP, SPIDER, CATS                                            | INCORRECT (Max overlap: 2/4 with ___ MAN SUPERHEROES)
   - Group 5: **0.5613** | REEBOK, PUMA, SUPER, NIKE                                         | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (47.0%, no-rel 23.0%)]
   - Group 6: **0.3675** | CAROUSEL, ADIDAS, CABARET, CHICAGO                                | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”)
   - Group 7: **0.4708** | ADIDAS, SUPER, NIKE, CHICAGO                                      | INCORRECT (Max overlap: 2/4 with SNEAKER BRANDS)
   - Group 8: **0.4099** | CAROUSEL, REEBOK, PUMA, CABARET                                   | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (46.5%, no-rel 17.7%)]
   - Group 9: **0.5394** | REEBOK, ADIDAS, PUMA, SUPER                                       | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS)
   - Group 10: **0.3540** | CAROUSEL, NIKE, CABARET, CHICAGO                                  | INCORRECT (Max overlap: 3/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (46.0%, no-rel 18.0%)]
   - Group 11: **0.4705** | CAROUSEL, REEBOK, ADIDAS, NIKE                                    | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (55.5%, no-rel 15.4%)]
   - Group 12: **0.3907** | PUMA, SUPER, CABARET, CHICAGO                                     | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”)
   - Group 13: **0.4409** | CAROUSEL, REEBOK, PUMA, NIKE                                      | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (56.5%, no-rel 14.0%)]
   - Group 14: **0.4200** | ADIDAS, SUPER, CABARET, CHICAGO                                   | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”)
   - Group 15: **0.4515** | PUMA, SUPER, NIKE, CHICAGO                                        | INCORRECT (Max overlap: 2/4 with SNEAKER BRANDS)
   - Group 16: **0.3984** | CAROUSEL, REEBOK, ADIDAS, CABARET                                 | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (45.3%, no-rel 20.0%)]
   - Group 17: **0.4589** | ADIDAS, PUMA, SUPER, CHICAGO                                      | INCORRECT (Max overlap: 2/4 with SNEAKER BRANDS)
   - Group 18: **0.3901** | CAROUSEL, REEBOK, NIKE, CABARET                                   | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”) | [Pred Type: NAMED_ENTITY_SET (48.8%, no-rel 16.4%)]
   - Group 19: **0.4346** | CAROUSEL, ADIDAS, PUMA, NIKE                                      | INCORRECT (Max overlap: 3/4 with SNEAKER BRANDS) | [Pred Type: NAMED_ENTITY_SET (55.5%, no-rel 15.4%)]
   - Group 20: **0.4142** | REEBOK, SUPER, CABARET, CHICAGO                                   | INCORRECT (Max overlap: 2/4 with MUSICALS BEGINNING WITH “C”)

---

## Puzzle 72 (ID: 465)
**Words on Board:** DISH, DOPE, SNOOP, PORCH, SCOOP, SIZZLE, DEMO, DROOP, BLOOPER, LAD, STOOP, GOOF, HIGHLIGHT, DECK, YARD, INFO

### Ground Truth Categories:
* **Level 0 (GATHERING SPOT OUTSIDE A RESIDENCE) [Type: SEMANTIC_SET]:** DECK, PORCH, STOOP, YARD
* **Level 1 (LOWDOWN) [Type: SYNONYM_OR_NEAR]:** DISH, DOPE, INFO, SCOOP
* **Level 2 (KINDS OF REELS) [Type: SEMANTIC_SET]:** BLOOPER, DEMO, HIGHLIGHT, SIZZLE
* **Level 3 (CARTOON DOGS MINUS “Y”) [Type: WORDPLAY_TRANSFORM]:** DROOP, GOOF, LAD, SNOOP

### Top Candidate Partitions:
1. **Partition Score: 0.4697**
   - Group 1: **0.5052** | DISH, PORCH, DECK, YARD                                           | INCORRECT (Max overlap: 3/4 with GATHERING SPOT OUTSIDE A RESIDENCE)
   - Group 2: **0.5021** | DOPE, DEMO, BLOOPER, GOOF                                         | INCORRECT (Max overlap: 2/4 with KINDS OF REELS) | [Pred Type: SYNONYM_OR_NEAR (48.3%, no-rel 34.6%)]
   - Group 3: **0.4974** | SNOOP, LAD, HIGHLIGHT, INFO                                       | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)
   - Group 4: **0.4397** | SCOOP, SIZZLE, DROOP, STOOP                                       | INCORRECT (Max overlap: 1/4 with LOWDOWN) | [Pred Type: SEMANTIC_SET (55.9%, no-rel 19.5%)]
2. **Partition Score: 0.4606**
   - Group 1: **0.5076** | DEMO, LAD, HIGHLIGHT, INFO                                        | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 2: **0.5052** | DISH, PORCH, DECK, YARD                                           | INCORRECT (Max overlap: 3/4 with GATHERING SPOT OUTSIDE A RESIDENCE)
   - Group 3: **0.4579** | DOPE, SNOOP, BLOOPER, GOOF                                        | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 27.2%)]
   - Group 4: **0.4397** | SCOOP, SIZZLE, DROOP, STOOP                                       | INCORRECT (Max overlap: 1/4 with LOWDOWN) | [Pred Type: SEMANTIC_SET (55.9%, no-rel 19.5%)]
3. **Partition Score: 0.4502**
   - Group 1: **0.5052** | DISH, PORCH, DECK, YARD                                           | INCORRECT (Max overlap: 3/4 with GATHERING SPOT OUTSIDE A RESIDENCE)
   - Group 2: **0.4634** | DOPE, BLOOPER, LAD, GOOF                                          | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)
   - Group 3: **0.4577** | SNOOP, DEMO, HIGHLIGHT, INFO                                      | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 4: **0.4397** | SCOOP, SIZZLE, DROOP, STOOP                                       | INCORRECT (Max overlap: 1/4 with LOWDOWN) | [Pred Type: SEMANTIC_SET (55.9%, no-rel 19.5%)]
4. **Partition Score: 0.4500**
   - Group 1: **0.5021** | DOPE, DEMO, BLOOPER, GOOF                                         | INCORRECT (Max overlap: 2/4 with KINDS OF REELS) | [Pred Type: SYNONYM_OR_NEAR (48.3%, no-rel 34.6%)]
   - Group 2: **0.4974** | SNOOP, LAD, HIGHLIGHT, INFO                                       | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)
   - Group 3: **0.4836** | DISH, PORCH, SCOOP, YARD                                          | INCORRECT (Max overlap: 2/4 with LOWDOWN) | [Pred Type: SEMANTIC_SET (46.3%, no-rel 34.4%)]
   - Group 4: **0.4096** | SIZZLE, DROOP, STOOP, DECK                                        | INCORRECT (Max overlap: 2/4 with GATHERING SPOT OUTSIDE A RESIDENCE) | [Pred Type: SEMANTIC_SET (61.1%, no-rel 19.3%)]
5. **Partition Score: 0.4486**
   - Group 1: **0.5464** | PORCH, STOOP, DECK, YARD                                          | CORRECT GROUP (GATHERING SPOT OUTSIDE A RESIDENCE, Level 0) | [Pred Type: SEMANTIC_SET (61.8%, no-rel 24.4%)]
   - Group 2: **0.5076** | DEMO, LAD, HIGHLIGHT, INFO                                        | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 3: **0.4328** | DISH, SNOOP, SCOOP, SIZZLE                                        | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 4: **0.4271** | DOPE, DROOP, BLOOPER, GOOF                                        | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”) | [Pred Type: SYNONYM_OR_NEAR (46.3%, no-rel 27.3%)]

### Top Candidate Groups:
   - Group 1: **0.5052** | DISH, PORCH, DECK, YARD                                           | INCORRECT (Max overlap: 3/4 with GATHERING SPOT OUTSIDE A RESIDENCE)
   - Group 2: **0.5021** | DOPE, DEMO, BLOOPER, GOOF                                         | INCORRECT (Max overlap: 2/4 with KINDS OF REELS) | [Pred Type: SYNONYM_OR_NEAR (48.3%, no-rel 34.6%)]
   - Group 3: **0.4974** | SNOOP, LAD, HIGHLIGHT, INFO                                       | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)
   - Group 4: **0.4397** | SCOOP, SIZZLE, DROOP, STOOP                                       | INCORRECT (Max overlap: 1/4 with LOWDOWN) | [Pred Type: SEMANTIC_SET (55.9%, no-rel 19.5%)]
   - Group 5: **0.5076** | DEMO, LAD, HIGHLIGHT, INFO                                        | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 6: **0.4579** | DOPE, SNOOP, BLOOPER, GOOF                                        | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 27.2%)]
   - Group 7: **0.4634** | DOPE, BLOOPER, LAD, GOOF                                          | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)
   - Group 8: **0.4577** | SNOOP, DEMO, HIGHLIGHT, INFO                                      | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 9: **0.4836** | DISH, PORCH, SCOOP, YARD                                          | INCORRECT (Max overlap: 2/4 with LOWDOWN) | [Pred Type: SEMANTIC_SET (46.3%, no-rel 34.4%)]
   - Group 10: **0.4096** | SIZZLE, DROOP, STOOP, DECK                                        | INCORRECT (Max overlap: 2/4 with GATHERING SPOT OUTSIDE A RESIDENCE) | [Pred Type: SEMANTIC_SET (61.1%, no-rel 19.3%)]
   - Group 11: **0.5464** | PORCH, STOOP, DECK, YARD                                          | CORRECT GROUP (GATHERING SPOT OUTSIDE A RESIDENCE, Level 0) | [Pred Type: SEMANTIC_SET (61.8%, no-rel 24.4%)]
   - Group 12: **0.4328** | DISH, SNOOP, SCOOP, SIZZLE                                        | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 13: **0.4271** | DOPE, DROOP, BLOOPER, GOOF                                        | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”) | [Pred Type: SYNONYM_OR_NEAR (46.3%, no-rel 27.3%)]
   - Group 14: **0.4220** | SNOOP, SCOOP, SIZZLE, STOOP                                       | INCORRECT (Max overlap: 1/4 with CARTOON DOGS MINUS “Y”)
   - Group 15: **0.4693** | SNOOP, SCOOP, DROOP, STOOP                                        | INCORRECT (Max overlap: 2/4 with CARTOON DOGS MINUS “Y”)
   - Group 16: **0.3992** | SIZZLE, LAD, HIGHLIGHT, INFO                                      | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 17: **0.4946** | DOPE, SNOOP, HIGHLIGHT, INFO                                      | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 18: **0.4137** | DEMO, BLOOPER, LAD, GOOF                                          | INCORRECT (Max overlap: 2/4 with KINDS OF REELS)
   - Group 19: **0.5297** | DOPE, LAD, HIGHLIGHT, INFO                                        | INCORRECT (Max overlap: 2/4 with LOWDOWN)
   - Group 20: **0.3986** | DEMO, DROOP, BLOOPER, GOOF                                        | INCORRECT (Max overlap: 2/4 with KINDS OF REELS) | [Pred Type: SYNONYM_OR_NEAR (47.6%, no-rel 24.6%)]

---

## Puzzle 73 (ID: 1057)
**Words on Board:** THE PENTAGON, FILM NERD, MAKING OUT, LEFT FIELD, THE BLUE, NECKING, FIRST BASE, HOME PLATE, MEMENTO, NOWHERE, THIN AIR, TONSIL HOCKEY, BURGER KING WHOPPER, PITCHER'S MOUND, SCHOOL CROSSING SIGN, JEANS BACK POCKET

### Ground Truth Categories:
* **Level 0 (CANOODLING) [Type: SYNONYM_OR_NEAR]:** FIRST BASE, MAKING OUT, NECKING, TONSIL HOCKEY
* **Level 1 (FIVE-SIDED THINGS) [Type: SEMANTIC_SET]:** HOME PLATE, JEANS BACK POCKET, SCHOOL CROSSING SIGN, THE PENTAGON
* **Level 2 (UNEXPECTED PLACES TO BE "OUT OF") [Type: FILL_IN_THE_BLANK]:** LEFT FIELD, NOWHERE, THE BLUE, THIN AIR
* **Level 3 (ENDING IN CANDY BRANDS MINUS "S") [Type: WORDPLAY_TRANSFORM]:** BURGER KING WHOPPER, FILM NERD, MEMENTO, PITCHER'S MOUND

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.6327** | LEFT FIELD, FIRST BASE, HOME PLATE, PITCHER'S MOUND               | INCORRECT (Max overlap: 1/4 with UNEXPECTED PLACES TO BE "OUT OF") | [Pred Type: SEMANTIC_SET (57.1%, no-rel 22.0%)]
   - Group 2: **0.6274** | FILM NERD, MEMENTO, NOWHERE, THIN AIR                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 3: **0.6168** | THE PENTAGON, FILM NERD, MEMENTO, NOWHERE                         | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 4: **0.6107** | THE PENTAGON, FILM NERD, NOWHERE, THIN AIR                        | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 5: **0.5990** | THE PENTAGON, MEMENTO, NOWHERE, THIN AIR                          | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 6: **0.5840** | THE PENTAGON, FILM NERD, MEMENTO, THIN AIR                        | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 7: **0.5788** | THE PENTAGON, FILM NERD, THE BLUE, NOWHERE                        | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 8: **0.5758** | THE PENTAGON, THE BLUE, NOWHERE, THIN AIR                         | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 9: **0.5697** | FILM NERD, THE BLUE, NOWHERE, THIN AIR                            | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 10: **0.5616** | FILM NERD, THE BLUE, MEMENTO, NOWHERE                             | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 11: **0.5610** | THE PENTAGON, THE BLUE, MEMENTO, NOWHERE                          | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 12: **0.5536** | THE BLUE, MEMENTO, NOWHERE, THIN AIR                              | INCORRECT (Max overlap: 3/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 13: **0.5480** | THE PENTAGON, FILM NERD, THE BLUE, THIN AIR                       | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 14: **0.5339** | THE PENTAGON, THE BLUE, MEMENTO, THIN AIR                         | INCORRECT (Max overlap: 2/4 with UNEXPECTED PLACES TO BE "OUT OF")
   - Group 15: **0.5331** | THE PENTAGON, FILM NERD, THE BLUE, MEMENTO                        | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 16: **0.5300** | THE PENTAGON, PITCHER'S MOUND, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 3/4 with FIVE-SIDED THINGS)
   - Group 17: **0.5299** | THE PENTAGON, BURGER KING WHOPPER, SCHOOL CROSSING SIGN, JEANS BACK POCKET | INCORRECT (Max overlap: 3/4 with FIVE-SIDED THINGS)
   - Group 18: **0.5297** | THE PENTAGON, BURGER KING WHOPPER, PITCHER'S MOUND, SCHOOL CROSSING SIGN | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)
   - Group 19: **0.5277** | FILM NERD, THE BLUE, MEMENTO, THIN AIR                            | INCORRECT (Max overlap: 2/4 with ENDING IN CANDY BRANDS MINUS "S")
   - Group 20: **0.5267** | THE PENTAGON, BURGER KING WHOPPER, PITCHER'S MOUND, JEANS BACK POCKET | INCORRECT (Max overlap: 2/4 with FIVE-SIDED THINGS)

---

## Puzzle 74 (ID: 446)
**Words on Board:** ROW, DIAMOND, DIVE, GLITTER, BOX, TEMPLE, FENCE, CUBE, GOLD, SEQUIN, LIGHTHOUSE, MACHINE, PYRAMID, GARDENS, CREAM, STORM

### Ground Truth Categories:
* **Level 0 (SPARKLING THINGS) [Type: SEMANTIC_SET]:** DIAMOND, GLITTER, GOLD, SEQUIN
* **Level 1 (PARTICIPATE IN SUMMER OLYMPIC EVENTS) [Type: SEMANTIC_SET]:** BOX, DIVE, FENCE, ROW
* **Level 2 (WONDERS OF THE WORLD) [Type: NAMED_ENTITY_SET]:** GARDENS, LIGHTHOUSE, PYRAMID, TEMPLE
* **Level 3 (ICE ___) [Type: FILL_IN_THE_BLANK]:** CREAM, CUBE, MACHINE, STORM

### Top Candidate Partitions:
1. **Partition Score: 0.4472**
   - Group 1: **0.4556** | ROW, BOX, FENCE, MACHINE                                          | INCORRECT (Max overlap: 3/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 2: **0.4555** | DIAMOND, CUBE, SEQUIN, PYRAMID                                    | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 3: **0.4535** | TEMPLE, GOLD, LIGHTHOUSE, GARDENS                                 | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 4: **0.4399** | DIVE, GLITTER, CREAM, STORM                                       | INCORRECT (Max overlap: 2/4 with ICE ___)
2. **Partition Score: 0.4449**
   - Group 1: **0.4672** | ROW, MACHINE, CREAM, STORM                                        | INCORRECT (Max overlap: 3/4 with ICE ___)
   - Group 2: **0.4565** | DIAMOND, DIVE, GLITTER, SEQUIN                                    | INCORRECT (Max overlap: 3/4 with SPARKLING THINGS)
   - Group 3: **0.4535** | TEMPLE, GOLD, LIGHTHOUSE, GARDENS                                 | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 4: **0.4347** | BOX, FENCE, CUBE, PYRAMID                                         | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
3. **Partition Score: 0.4338**
   - Group 1: **0.4535** | TEMPLE, GOLD, LIGHTHOUSE, GARDENS                                 | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 2: **0.4347** | BOX, FENCE, CUBE, PYRAMID                                         | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 3: **0.4340** | ROW, SEQUIN, MACHINE, CREAM                                       | INCORRECT (Max overlap: 2/4 with ICE ___)
   - Group 4: **0.4332** | DIAMOND, DIVE, GLITTER, STORM                                     | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
4. **Partition Score: 0.4293**
   - Group 1: **0.4672** | ROW, MACHINE, CREAM, STORM                                        | INCORRECT (Max overlap: 3/4 with ICE ___)
   - Group 2: **0.4574** | TEMPLE, SEQUIN, LIGHTHOUSE, GARDENS                               | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 3: **0.4347** | BOX, FENCE, CUBE, PYRAMID                                         | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 4: **0.4125** | DIAMOND, DIVE, GLITTER, GOLD                                      | INCORRECT (Max overlap: 3/4 with SPARKLING THINGS)
5. **Partition Score: 0.4266**
   - Group 1: **0.4535** | TEMPLE, GOLD, LIGHTHOUSE, GARDENS                                 | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 2: **0.4347** | BOX, FENCE, CUBE, PYRAMID                                         | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 3: **0.4300** | ROW, SEQUIN, MACHINE, STORM                                       | INCORRECT (Max overlap: 2/4 with ICE ___)
   - Group 4: **0.4209** | DIAMOND, DIVE, GLITTER, CREAM                                     | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)

### Top Candidate Groups:
   - Group 1: **0.4556** | ROW, BOX, FENCE, MACHINE                                          | INCORRECT (Max overlap: 3/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 2: **0.4555** | DIAMOND, CUBE, SEQUIN, PYRAMID                                    | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 3: **0.4535** | TEMPLE, GOLD, LIGHTHOUSE, GARDENS                                 | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 4: **0.4399** | DIVE, GLITTER, CREAM, STORM                                       | INCORRECT (Max overlap: 2/4 with ICE ___)
   - Group 5: **0.4672** | ROW, MACHINE, CREAM, STORM                                        | INCORRECT (Max overlap: 3/4 with ICE ___)
   - Group 6: **0.4565** | DIAMOND, DIVE, GLITTER, SEQUIN                                    | INCORRECT (Max overlap: 3/4 with SPARKLING THINGS)
   - Group 7: **0.4347** | BOX, FENCE, CUBE, PYRAMID                                         | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 8: **0.4340** | ROW, SEQUIN, MACHINE, CREAM                                       | INCORRECT (Max overlap: 2/4 with ICE ___)
   - Group 9: **0.4332** | DIAMOND, DIVE, GLITTER, STORM                                     | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 10: **0.4574** | TEMPLE, SEQUIN, LIGHTHOUSE, GARDENS                               | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)
   - Group 11: **0.4125** | DIAMOND, DIVE, GLITTER, GOLD                                      | INCORRECT (Max overlap: 3/4 with SPARKLING THINGS)
   - Group 12: **0.4300** | ROW, SEQUIN, MACHINE, STORM                                       | INCORRECT (Max overlap: 2/4 with ICE ___)
   - Group 13: **0.4209** | DIAMOND, DIVE, GLITTER, CREAM                                     | INCORRECT (Max overlap: 2/4 with SPARKLING THINGS)
   - Group 14: **0.4263** | BOX, FENCE, MACHINE, CREAM                                        | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 15: **0.4125** | ROW, DIVE, GLITTER, STORM                                         | INCORRECT (Max overlap: 2/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 16: **0.4775** | TEMPLE, LIGHTHOUSE, PYRAMID, GARDENS                              | CORRECT GROUP (WONDERS OF THE WORLD, Level 2)
   - Group 17: **0.4664** | DIAMOND, GLITTER, GOLD, SEQUIN                                    | CORRECT GROUP (SPARKLING THINGS, Level 0)
   - Group 18: **0.4147** | BOX, CUBE, MACHINE, CREAM                                         | INCORRECT (Max overlap: 3/4 with ICE ___)
   - Group 19: **0.4116** | ROW, DIVE, FENCE, STORM                                           | INCORRECT (Max overlap: 3/4 with PARTICIPATE IN SUMMER OLYMPIC EVENTS)
   - Group 20: **0.4000** | DIVE, TEMPLE, LIGHTHOUSE, GARDENS                                 | INCORRECT (Max overlap: 3/4 with WONDERS OF THE WORLD)

---

## Puzzle 75 (ID: 301)
**Words on Board:** PEANUTS, PIGPEN, SOLID, DUMP, SOUND, PRIZE, DARK, MESS, FIRM, STY, CRAZY, CARAMEL, STABLE, GIFT, POPCORN, CHARLEY

### Ground Truth Categories:
* **Level 0 (DISORDERLY PLACE) [Type: SYNONYM_OR_NEAR]:** DUMP, MESS, PIGPEN, STY
* **Level 1 (STURDY) [Type: SYNONYM_OR_NEAR]:** FIRM, SOLID, SOUND, STABLE
* **Level 2 (FOUND IN CRACKER JACKS) [Type: NAMED_ENTITY_SET]:** CARAMEL, PEANUTS, POPCORN, PRIZE
* **Level 3 (___ HORSE) [Type: FILL_IN_THE_BLANK]:** CHARLEY, CRAZY, DARK, GIFT

### Top Candidate Partitions:
1. **Partition Score: 0.3551**
   - Group 1: **0.5216** | PEANUTS, CARAMEL, POPCORN, CHARLEY                                | INCORRECT (Max overlap: 3/4 with FOUND IN CRACKER JACKS)
   - Group 2: **0.4941** | SOLID, SOUND, FIRM, STABLE                                        | CORRECT GROUP (STURDY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (56.4%, no-rel 34.1%)]
   - Group 3: **0.3142** | PRIZE, DARK, CRAZY, GIFT                                          | INCORRECT (Max overlap: 3/4 with ___ HORSE) | [Pred Type: SYNONYM_OR_NEAR (46.3%, no-rel 20.6%)]
   - Group 4: **0.3061** | PIGPEN, DUMP, MESS, STY                                           | CORRECT GROUP (DISORDERLY PLACE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (65.7%, no-rel 22.9%)]
2. **Partition Score: 0.3425**
   - Group 1: **0.4180** | SOLID, DUMP, SOUND, STABLE                                        | INCORRECT (Max overlap: 3/4 with STURDY)
   - Group 2: **0.4145** | PRIZE, DARK, CRAZY, CARAMEL                                       | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)
   - Group 3: **0.3690** | PEANUTS, PIGPEN, POPCORN, CHARLEY                                 | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS) | [Pred Type: SEMANTIC_SET (54.7%, no-rel 18.8%)]
   - Group 4: **0.2932** | MESS, FIRM, STY, GIFT                                             | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
3. **Partition Score: 0.3410**
   - Group 1: **0.4145** | PRIZE, DARK, CRAZY, CARAMEL                                       | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)
   - Group 2: **0.3841** | DUMP, MESS, FIRM, GIFT                                            | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
   - Group 3: **0.3690** | PEANUTS, PIGPEN, POPCORN, CHARLEY                                 | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS) | [Pred Type: SEMANTIC_SET (54.7%, no-rel 18.8%)]
   - Group 4: **0.3054** | SOLID, SOUND, STY, STABLE                                         | INCORRECT (Max overlap: 3/4 with STURDY)
4. **Partition Score: 0.3381**
   - Group 1: **0.4237** | SOLID, DUMP, SOUND, FIRM                                          | INCORRECT (Max overlap: 3/4 with STURDY) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 36.9%)]
   - Group 2: **0.4145** | PRIZE, DARK, CRAZY, CARAMEL                                       | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)
   - Group 3: **0.3690** | PEANUTS, PIGPEN, POPCORN, CHARLEY                                 | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS) | [Pred Type: SEMANTIC_SET (54.7%, no-rel 18.8%)]
   - Group 4: **0.2845** | MESS, STY, STABLE, GIFT                                           | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
5. **Partition Score: 0.3342**
   - Group 1: **0.4145** | PRIZE, DARK, CRAZY, CARAMEL                                       | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)
   - Group 2: **0.3702** | SOLID, DUMP, SOUND, MESS                                          | INCORRECT (Max overlap: 2/4 with STURDY)
   - Group 3: **0.3690** | PEANUTS, PIGPEN, POPCORN, CHARLEY                                 | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS) | [Pred Type: SEMANTIC_SET (54.7%, no-rel 18.8%)]
   - Group 4: **0.2987** | FIRM, STY, STABLE, GIFT                                           | INCORRECT (Max overlap: 2/4 with STURDY)

### Top Candidate Groups:
   - Group 1: **0.5216** | PEANUTS, CARAMEL, POPCORN, CHARLEY                                | INCORRECT (Max overlap: 3/4 with FOUND IN CRACKER JACKS)
   - Group 2: **0.4941** | SOLID, SOUND, FIRM, STABLE                                        | CORRECT GROUP (STURDY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (56.4%, no-rel 34.1%)]
   - Group 3: **0.3142** | PRIZE, DARK, CRAZY, GIFT                                          | INCORRECT (Max overlap: 3/4 with ___ HORSE) | [Pred Type: SYNONYM_OR_NEAR (46.3%, no-rel 20.6%)]
   - Group 4: **0.3061** | PIGPEN, DUMP, MESS, STY                                           | CORRECT GROUP (DISORDERLY PLACE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (65.7%, no-rel 22.9%)]
   - Group 5: **0.4180** | SOLID, DUMP, SOUND, STABLE                                        | INCORRECT (Max overlap: 3/4 with STURDY)
   - Group 6: **0.4145** | PRIZE, DARK, CRAZY, CARAMEL                                       | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS)
   - Group 7: **0.3690** | PEANUTS, PIGPEN, POPCORN, CHARLEY                                 | INCORRECT (Max overlap: 2/4 with FOUND IN CRACKER JACKS) | [Pred Type: SEMANTIC_SET (54.7%, no-rel 18.8%)]
   - Group 8: **0.2932** | MESS, FIRM, STY, GIFT                                             | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
   - Group 9: **0.3841** | DUMP, MESS, FIRM, GIFT                                            | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
   - Group 10: **0.3054** | SOLID, SOUND, STY, STABLE                                         | INCORRECT (Max overlap: 3/4 with STURDY)
   - Group 11: **0.4237** | SOLID, DUMP, SOUND, FIRM                                          | INCORRECT (Max overlap: 3/4 with STURDY) | [Pred Type: SYNONYM_OR_NEAR (53.2%, no-rel 36.9%)]
   - Group 12: **0.2845** | MESS, STY, STABLE, GIFT                                           | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
   - Group 13: **0.3702** | SOLID, DUMP, SOUND, MESS                                          | INCORRECT (Max overlap: 2/4 with STURDY)
   - Group 14: **0.2987** | FIRM, STY, STABLE, GIFT                                           | INCORRECT (Max overlap: 2/4 with STURDY)
   - Group 15: **0.3868** | SOLID, DUMP, FIRM, STABLE                                         | INCORRECT (Max overlap: 3/4 with STURDY) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 37.4%)]
   - Group 16: **0.2900** | SOUND, MESS, STY, GIFT                                            | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
   - Group 17: **0.3777** | SOLID, SOUND, PRIZE, GIFT                                         | INCORRECT (Max overlap: 2/4 with STURDY)
   - Group 18: **0.3600** | DARK, MESS, CRAZY, CARAMEL                                        | INCORRECT (Max overlap: 2/4 with ___ HORSE)
   - Group 19: **0.3030** | DUMP, FIRM, STY, STABLE                                           | INCORRECT (Max overlap: 2/4 with DISORDERLY PLACE)
   - Group 20: **0.3705** | SOLID, SOUND, MESS, FIRM                                          | INCORRECT (Max overlap: 3/4 with STURDY) | [Pred Type: SYNONYM_OR_NEAR (57.1%, no-rel 32.6%)]

---

## Puzzle 76 (ID: 1028)
**Words on Board:** MONKEY, FELLOW, CONTACT, UNEVEN, ASSOCIATE, COLLEAGUE, SPECTACLE, GOGGLE, LOOK, STYLE, PEER, DESIGN, PULL-UP, SCHEME, PARALLEL, SHADE

### Ground Truth Categories:
* **Level 0 (COHORT MEMBER) [Type: SYNONYM_OR_NEAR]:** ASSOCIATE, COLLEAGUE, FELLOW, PEER
* **Level 1 (AESTHETIC) [Type: SYNONYM_OR_NEAR]:** DESIGN, LOOK, SCHEME, STYLE
* **Level 2 (KINDS OF BAR APPARATUSES) [Type: NAMED_ENTITY_SET]:** MONKEY, PARALLEL, PULL-UP, UNEVEN
* **Level 3 (EYEWEAR IN THE SINGULAR) [Type: WORDPLAY_TRANSFORM]:** CONTACT, GOGGLE, SHADE, SPECTACLE

### Top Candidate Partitions:
1. **Partition Score: 0.3735**
   - Group 1: **0.4511** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 25.7%)]
   - Group 2: **0.4080** | LOOK, STYLE, PEER, DESIGN                                         | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 3: **0.3633** | MONKEY, CONTACT, SPECTACLE, GOGGLE                                | INCORRECT (Max overlap: 3/4 with EYEWEAR IN THE SINGULAR)
   - Group 4: **0.3612** | UNEVEN, PULL-UP, PARALLEL, SHADE                                  | INCORRECT (Max overlap: 3/4 with KINDS OF BAR APPARATUSES)
2. **Partition Score: 0.3722**
   - Group 1: **0.4536** | FELLOW, CONTACT, ASSOCIATE, COLLEAGUE                             | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (66.4%, no-rel 24.4%)]
   - Group 2: **0.4269** | SPECTACLE, STYLE, DESIGN, SCHEME                                  | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 3: **0.3682** | MONKEY, UNEVEN, PULL-UP, SHADE                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BAR APPARATUSES)
   - Group 4: **0.3468** | GOGGLE, LOOK, PEER, PARALLEL                                      | INCORRECT (Max overlap: 1/4 with EYEWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (47.4%, no-rel 20.9%)]
3. **Partition Score: 0.3716**
   - Group 1: **0.6503** | FELLOW, ASSOCIATE, COLLEAGUE, PEER                                | CORRECT GROUP (COHORT MEMBER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.6%, no-rel 20.4%)]
   - Group 2: **0.4005** | LOOK, STYLE, DESIGN, SCHEME                                       | CORRECT GROUP (AESTHETIC, Level 1)
   - Group 3: **0.3633** | MONKEY, CONTACT, SPECTACLE, GOGGLE                                | INCORRECT (Max overlap: 3/4 with EYEWEAR IN THE SINGULAR)
   - Group 4: **0.3612** | UNEVEN, PULL-UP, PARALLEL, SHADE                                  | INCORRECT (Max overlap: 3/4 with KINDS OF BAR APPARATUSES)
4. **Partition Score: 0.3696**
   - Group 1: **0.4511** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 25.7%)]
   - Group 2: **0.4165** | CONTACT, SPECTACLE, STYLE, DESIGN                                 | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 3: **0.3682** | MONKEY, UNEVEN, PULL-UP, SHADE                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BAR APPARATUSES)
   - Group 4: **0.3468** | GOGGLE, LOOK, PEER, PARALLEL                                      | INCORRECT (Max overlap: 1/4 with EYEWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (47.4%, no-rel 20.9%)]
5. **Partition Score: 0.3689**
   - Group 1: **0.4511** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 25.7%)]
   - Group 2: **0.4242** | CONTACT, UNEVEN, PARALLEL, SHADE                                  | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 3: **0.4080** | LOOK, STYLE, PEER, DESIGN                                         | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 4: **0.3216** | MONKEY, SPECTACLE, GOGGLE, PULL-UP                                | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)

### Top Candidate Groups:
   - Group 1: **0.4511** | FELLOW, ASSOCIATE, COLLEAGUE, SCHEME                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 25.7%)]
   - Group 2: **0.4080** | LOOK, STYLE, PEER, DESIGN                                         | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 3: **0.3633** | MONKEY, CONTACT, SPECTACLE, GOGGLE                                | INCORRECT (Max overlap: 3/4 with EYEWEAR IN THE SINGULAR)
   - Group 4: **0.3612** | UNEVEN, PULL-UP, PARALLEL, SHADE                                  | INCORRECT (Max overlap: 3/4 with KINDS OF BAR APPARATUSES)
   - Group 5: **0.4536** | FELLOW, CONTACT, ASSOCIATE, COLLEAGUE                             | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (66.4%, no-rel 24.4%)]
   - Group 6: **0.4269** | SPECTACLE, STYLE, DESIGN, SCHEME                                  | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 7: **0.3682** | MONKEY, UNEVEN, PULL-UP, SHADE                                    | INCORRECT (Max overlap: 3/4 with KINDS OF BAR APPARATUSES)
   - Group 8: **0.3468** | GOGGLE, LOOK, PEER, PARALLEL                                      | INCORRECT (Max overlap: 1/4 with EYEWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (47.4%, no-rel 20.9%)]
   - Group 9: **0.6503** | FELLOW, ASSOCIATE, COLLEAGUE, PEER                                | CORRECT GROUP (COHORT MEMBER, Level 0) | [Pred Type: SYNONYM_OR_NEAR (68.6%, no-rel 20.4%)]
   - Group 10: **0.4005** | LOOK, STYLE, DESIGN, SCHEME                                       | CORRECT GROUP (AESTHETIC, Level 1)
   - Group 11: **0.4165** | CONTACT, SPECTACLE, STYLE, DESIGN                                 | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 12: **0.4242** | CONTACT, UNEVEN, PARALLEL, SHADE                                  | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)
   - Group 13: **0.3216** | MONKEY, SPECTACLE, GOGGLE, PULL-UP                                | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 14: **0.3938** | MONKEY, FELLOW, ASSOCIATE, COLLEAGUE                              | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (62.1%, no-rel 24.3%)]
   - Group 15: **0.3584** | CONTACT, GOGGLE, LOOK, PEER                                       | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR) | [Pred Type: SYNONYM_OR_NEAR (46.7%, no-rel 23.4%)]
   - Group 16: **0.3844** | FELLOW, ASSOCIATE, COLLEAGUE, PARALLEL                            | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (66.1%, no-rel 22.0%)]
   - Group 17: **0.4065** | FELLOW, ASSOCIATE, COLLEAGUE, SPECTACLE                           | INCORRECT (Max overlap: 3/4 with COHORT MEMBER) | [Pred Type: SYNONYM_OR_NEAR (63.2%, no-rel 23.2%)]
   - Group 18: **0.3958** | CONTACT, STYLE, DESIGN, SCHEME                                    | INCORRECT (Max overlap: 3/4 with AESTHETIC)
   - Group 19: **0.3619** | UNEVEN, SPECTACLE, PULL-UP, SHADE                                 | INCORRECT (Max overlap: 2/4 with KINDS OF BAR APPARATUSES)
   - Group 20: **0.3543** | CONTACT, UNEVEN, PULL-UP, SHADE                                   | INCORRECT (Max overlap: 2/4 with EYEWEAR IN THE SINGULAR)

---

## Puzzle 77 (ID: 349)
**Words on Board:** SIGN, ENDORSE, BILLBOARD, BANNER, INITIAL, PREMIER, POSTER, USE, HERE, CHAMPION, WEE, SUPPORT, FIRST, MAIDEN, BACK, THEME

### Ground Truth Categories:
* **Level 0 (ADVERTISING FORMAT) [Type: SEMANTIC_SET]:** BANNER, BILLBOARD, POSTER, SIGN
* **Level 1 (INAUGURAL) [Type: SYNONYM_OR_NEAR]:** FIRST, INITIAL, MAIDEN, PREMIER
* **Level 2 (ADVOCATE FOR) [Type: SYNONYM_OR_NEAR]:** BACK, CHAMPION, ENDORSE, SUPPORT
* **Level 3 (PRONOUN PLUS “E”) [Type: WORDPLAY_TRANSFORM]:** HERE, THEME, USE, WEE

### Top Candidate Partitions:
1. **Partition Score: 0.4697**
   - Group 1: **0.7570** | SIGN, BILLBOARD, BANNER, POSTER                                   | CORRECT GROUP (ADVERTISING FORMAT, Level 0) | [Pred Type: SEMANTIC_SET (67.4%, no-rel 16.2%)]
   - Group 2: **0.5481** | ENDORSE, CHAMPION, SUPPORT, BACK                                  | CORRECT GROUP (ADVOCATE FOR, Level 2) | [Pred Type: SYNONYM_OR_NEAR (72.5%, no-rel 16.1%)]
   - Group 3: **0.5058** | HERE, WEE, MAIDEN, THEME                                          | INCORRECT (Max overlap: 3/4 with PRONOUN PLUS “E”)
   - Group 4: **0.4123** | INITIAL, PREMIER, USE, FIRST                                      | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 22.7%)]
2. **Partition Score: 0.4595**
   - Group 1: **0.5185** | ENDORSE, USE, SUPPORT, BACK                                       | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (64.9%, no-rel 23.7%)]
   - Group 2: **0.5058** | HERE, WEE, MAIDEN, THEME                                          | INCORRECT (Max overlap: 3/4 with PRONOUN PLUS “E”)
   - Group 3: **0.4693** | BILLBOARD, BANNER, POSTER, CHAMPION                               | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT) | [Pred Type: SEMANTIC_SET (61.3%, no-rel 22.0%)]
   - Group 4: **0.4315** | SIGN, INITIAL, PREMIER, FIRST                                     | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (63.0%, no-rel 20.2%)]
3. **Partition Score: 0.4588**
   - Group 1: **0.5253** | BILLBOARD, BANNER, POSTER, THEME                                  | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT) | [Pred Type: SEMANTIC_SET (56.1%, no-rel 29.4%)]
   - Group 2: **0.5185** | ENDORSE, USE, SUPPORT, BACK                                       | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (64.9%, no-rel 23.7%)]
   - Group 3: **0.4535** | HERE, CHAMPION, WEE, MAIDEN                                       | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 4: **0.4315** | SIGN, INITIAL, PREMIER, FIRST                                     | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (63.0%, no-rel 20.2%)]
4. **Partition Score: 0.4511**
   - Group 1: **0.7570** | SIGN, BILLBOARD, BANNER, POSTER                                   | CORRECT GROUP (ADVERTISING FORMAT, Level 0) | [Pred Type: SEMANTIC_SET (67.4%, no-rel 16.2%)]
   - Group 2: **0.5185** | ENDORSE, USE, SUPPORT, BACK                                       | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (64.9%, no-rel 23.7%)]
   - Group 3: **0.5058** | HERE, WEE, MAIDEN, THEME                                          | INCORRECT (Max overlap: 3/4 with PRONOUN PLUS “E”)
   - Group 4: **0.3900** | INITIAL, PREMIER, CHAMPION, FIRST                                 | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (60.0%, no-rel 20.5%)]
5. **Partition Score: 0.4505**
   - Group 1: **0.5253** | BILLBOARD, BANNER, POSTER, THEME                                  | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT) | [Pred Type: SEMANTIC_SET (56.1%, no-rel 29.4%)]
   - Group 2: **0.5237** | SIGN, ENDORSE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (61.8%, no-rel 25.9%)]
   - Group 3: **0.4535** | HERE, CHAMPION, WEE, MAIDEN                                       | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 4: **0.4123** | INITIAL, PREMIER, USE, FIRST                                      | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 22.7%)]

### Top Candidate Groups:
   - Group 1: **0.7570** | SIGN, BILLBOARD, BANNER, POSTER                                   | CORRECT GROUP (ADVERTISING FORMAT, Level 0) | [Pred Type: SEMANTIC_SET (67.4%, no-rel 16.2%)]
   - Group 2: **0.5481** | ENDORSE, CHAMPION, SUPPORT, BACK                                  | CORRECT GROUP (ADVOCATE FOR, Level 2) | [Pred Type: SYNONYM_OR_NEAR (72.5%, no-rel 16.1%)]
   - Group 3: **0.5058** | HERE, WEE, MAIDEN, THEME                                          | INCORRECT (Max overlap: 3/4 with PRONOUN PLUS “E”)
   - Group 4: **0.4123** | INITIAL, PREMIER, USE, FIRST                                      | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 22.7%)]
   - Group 5: **0.5185** | ENDORSE, USE, SUPPORT, BACK                                       | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (64.9%, no-rel 23.7%)]
   - Group 6: **0.4693** | BILLBOARD, BANNER, POSTER, CHAMPION                               | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT) | [Pred Type: SEMANTIC_SET (61.3%, no-rel 22.0%)]
   - Group 7: **0.4315** | SIGN, INITIAL, PREMIER, FIRST                                     | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (63.0%, no-rel 20.2%)]
   - Group 8: **0.5253** | BILLBOARD, BANNER, POSTER, THEME                                  | INCORRECT (Max overlap: 3/4 with ADVERTISING FORMAT) | [Pred Type: SEMANTIC_SET (56.1%, no-rel 29.4%)]
   - Group 9: **0.4535** | HERE, CHAMPION, WEE, MAIDEN                                       | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 10: **0.3900** | INITIAL, PREMIER, CHAMPION, FIRST                                 | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (60.0%, no-rel 20.5%)]
   - Group 11: **0.5237** | SIGN, ENDORSE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (61.8%, no-rel 25.9%)]
   - Group 12: **0.4871** | HERE, CHAMPION, MAIDEN, THEME                                     | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 13: **0.3587** | INITIAL, PREMIER, WEE, FIRST                                      | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (53.8%, no-rel 21.5%)]
   - Group 14: **0.4295** | INITIAL, PREMIER, FIRST, MAIDEN                                   | CORRECT GROUP (INAUGURAL, Level 1) | [Pred Type: SYNONYM_OR_NEAR (61.5%, no-rel 13.9%)]
   - Group 15: **0.3850** | HERE, CHAMPION, WEE, THEME                                        | INCORRECT (Max overlap: 3/4 with PRONOUN PLUS “E”)
   - Group 16: **0.3951** | ENDORSE, WEE, SUPPORT, BACK                                       | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (65.8%, no-rel 19.9%)]
   - Group 17: **0.4107** | CHAMPION, WEE, MAIDEN, THEME                                      | INCORRECT (Max overlap: 2/4 with PRONOUN PLUS “E”)
   - Group 18: **0.3794** | INITIAL, PREMIER, HERE, FIRST                                     | INCORRECT (Max overlap: 3/4 with INAUGURAL) | [Pred Type: SYNONYM_OR_NEAR (55.7%, no-rel 24.1%)]
   - Group 19: **0.4538** | ENDORSE, HERE, SUPPORT, BACK                                      | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (66.0%, no-rel 22.1%)]
   - Group 20: **0.4581** | ENDORSE, PREMIER, SUPPORT, BACK                                   | INCORRECT (Max overlap: 3/4 with ADVOCATE FOR) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 25.6%)]

---

## Puzzle 78 (ID: 657)
**Words on Board:** CARGO, CRYSTAL, LINEN, MAN, COMMANDO, SILVER, CANAL, CHINA, BOXER, PLAN, WITNESS, CLUE, BIKE, BERMUDA, BRAZIL, PANAMA

### Ground Truth Categories:
* **Level 0 (MATERIALS ASSOCIATED WITH FANCY DINING) [Type: SEMANTIC_SET]:** CHINA, CRYSTAL, LINEN, SILVER
* **Level 1 (KINDS OF SHORTS) [Type: SEMANTIC_SET]:** BERMUDA, BIKE, BOXER, CARGO
* **Level 2 (NOUNS IN A FAMOUS PALINDROME) [Type: WORDPLAY_TRANSFORM]:** CANAL, MAN, PANAMA, PLAN
* **Level 3 (MOVIES FROM 1985) [Type: NAMED_ENTITY_SET]:** BRAZIL, CLUE, COMMANDO, WITNESS

### Top Candidate Partitions:
1. **Partition Score: 0.4040**
   - Group 1: **0.5837** | MAN, PLAN, WITNESS, CLUE                                          | INCORRECT (Max overlap: 2/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 2: **0.4418** | CANAL, CHINA, BRAZIL, PANAMA                                      | INCORRECT (Max overlap: 2/4 with NOUNS IN A FAMOUS PALINDROME) | [Pred Type: SEMANTIC_SET (61.2%, no-rel 12.0%)]
   - Group 3: **0.4042** | CRYSTAL, LINEN, COMMANDO, SILVER                                  | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 4: **0.3850** | CARGO, BOXER, BIKE, BERMUDA                                       | CORRECT GROUP (KINDS OF SHORTS, Level 1)
2. **Partition Score: 0.3990**
   - Group 1: **0.5400** | CHINA, BERMUDA, BRAZIL, PANAMA                                    | INCORRECT (Max overlap: 1/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 2: **0.4630** | MAN, CANAL, PLAN, CLUE                                            | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 3: **0.4128** | CARGO, CRYSTAL, LINEN, SILVER                                     | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING) | [Pred Type: SEMANTIC_SET (50.9%, no-rel 22.2%)]
   - Group 4: **0.3602** | COMMANDO, BOXER, WITNESS, BIKE                                    | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
3. **Partition Score: 0.3990**
   - Group 1: **0.5400** | CHINA, BERMUDA, BRAZIL, PANAMA                                    | INCORRECT (Max overlap: 1/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 2: **0.4630** | MAN, CANAL, PLAN, CLUE                                            | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 3: **0.4042** | CRYSTAL, LINEN, COMMANDO, SILVER                                  | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 4: **0.3644** | CARGO, BOXER, WITNESS, BIKE                                       | INCORRECT (Max overlap: 3/4 with KINDS OF SHORTS)
4. **Partition Score: 0.3989**
   - Group 1: **0.5837** | MAN, PLAN, WITNESS, CLUE                                          | INCORRECT (Max overlap: 2/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 2: **0.4418** | CANAL, CHINA, BRAZIL, PANAMA                                      | INCORRECT (Max overlap: 2/4 with NOUNS IN A FAMOUS PALINDROME) | [Pred Type: SEMANTIC_SET (61.2%, no-rel 12.0%)]
   - Group 3: **0.4128** | CARGO, CRYSTAL, LINEN, SILVER                                     | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING) | [Pred Type: SEMANTIC_SET (50.9%, no-rel 22.2%)]
   - Group 4: **0.3705** | COMMANDO, BOXER, BIKE, BERMUDA                                    | INCORRECT (Max overlap: 3/4 with KINDS OF SHORTS)
5. **Partition Score: 0.3981**
   - Group 1: **0.5400** | CHINA, BERMUDA, BRAZIL, PANAMA                                    | INCORRECT (Max overlap: 1/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 2: **0.4630** | MAN, CANAL, PLAN, CLUE                                            | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 3: **0.3770** | CARGO, COMMANDO, BOXER, WITNESS                                   | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 4: **0.3762** | CRYSTAL, LINEN, SILVER, BIKE                                      | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)

### Top Candidate Groups:
   - Group 1: **0.5837** | MAN, PLAN, WITNESS, CLUE                                          | INCORRECT (Max overlap: 2/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 2: **0.4418** | CANAL, CHINA, BRAZIL, PANAMA                                      | INCORRECT (Max overlap: 2/4 with NOUNS IN A FAMOUS PALINDROME) | [Pred Type: SEMANTIC_SET (61.2%, no-rel 12.0%)]
   - Group 3: **0.4042** | CRYSTAL, LINEN, COMMANDO, SILVER                                  | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 4: **0.3850** | CARGO, BOXER, BIKE, BERMUDA                                       | CORRECT GROUP (KINDS OF SHORTS, Level 1)
   - Group 5: **0.5400** | CHINA, BERMUDA, BRAZIL, PANAMA                                    | INCORRECT (Max overlap: 1/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 6: **0.4630** | MAN, CANAL, PLAN, CLUE                                            | INCORRECT (Max overlap: 3/4 with NOUNS IN A FAMOUS PALINDROME)
   - Group 7: **0.4128** | CARGO, CRYSTAL, LINEN, SILVER                                     | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING) | [Pred Type: SEMANTIC_SET (50.9%, no-rel 22.2%)]
   - Group 8: **0.3602** | COMMANDO, BOXER, WITNESS, BIKE                                    | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 9: **0.3644** | CARGO, BOXER, WITNESS, BIKE                                       | INCORRECT (Max overlap: 3/4 with KINDS OF SHORTS)
   - Group 10: **0.3705** | COMMANDO, BOXER, BIKE, BERMUDA                                    | INCORRECT (Max overlap: 3/4 with KINDS OF SHORTS)
   - Group 11: **0.3770** | CARGO, COMMANDO, BOXER, WITNESS                                   | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS)
   - Group 12: **0.3762** | CRYSTAL, LINEN, SILVER, BIKE                                      | INCORRECT (Max overlap: 3/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 13: **0.3863** | LINEN, COMMANDO, BOXER, WITNESS                                   | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 14: **0.3635** | CARGO, CRYSTAL, SILVER, BIKE                                      | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS) | [Pred Type: SEMANTIC_SET (51.0%, no-rel 22.2%)]
   - Group 15: **0.3953** | LINEN, BOXER, BIKE, BERMUDA                                       | INCORRECT (Max overlap: 3/4 with KINDS OF SHORTS) | [Pred Type: FILL_IN_THE_BLANK (48.2%, no-rel 14.0%)]
   - Group 16: **0.3685** | CARGO, CRYSTAL, COMMANDO, SILVER                                  | INCORRECT (Max overlap: 2/4 with MATERIALS ASSOCIATED WITH FANCY DINING)
   - Group 17: **0.3838** | CARGO, CRYSTAL, LINEN, BIKE                                       | INCORRECT (Max overlap: 2/4 with KINDS OF SHORTS) | [Pred Type: SEMANTIC_SET (47.8%, no-rel 24.0%)]
   - Group 18: **0.3585** | COMMANDO, SILVER, BOXER, WITNESS                                  | INCORRECT (Max overlap: 2/4 with MOVIES FROM 1985)
   - Group 19: **0.4933** | CARGO, CHINA, BRAZIL, PANAMA                                      | INCORRECT (Max overlap: 1/4 with KINDS OF SHORTS)
   - Group 20: **0.3775** | CRYSTAL, LINEN, BIKE, BERMUDA                                     | INCORRECT (Max overlap: 2/4 with MATERIALS ASSOCIATED WITH FANCY DINING) | [Pred Type: FILL_IN_THE_BLANK (46.9%, no-rel 14.9%)]

---

## Puzzle 79 (ID: 789)
**Words on Board:** DEGREE, TIE, GRANT, EVEN, DOZE, MARVEL, PAC-MAN, CONFER, DOODLE, PRESENT, SQUARE, VEST, DRAW, PASS NOTES, SPACE, PAINT

### Ground Truth Categories:
* **Level 0 (MAKE EQUAL, AS A SCORE) [Type: SYNONYM_OR_NEAR]:** DRAW, EVEN, SQUARE, TIE
* **Level 1 (BESTOW) [Type: SYNONYM_OR_NEAR]:** CONFER, GRANT, PRESENT, VEST
* **Level 2 (THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING) [Type: SEMANTIC_SET]:** DOODLE, DOZE, PASS NOTES, SPACE
* **Level 3 (WORDS AFTER THE LETTERS “MS”) [Type: FILL_IN_THE_BLANK]:** DEGREE, MARVEL, PAC-MAN, PAINT

### Top Candidate Partitions:
1. **Partition Score: 0.4234**
   - Group 1: **0.5982** | GRANT, CONFER, PRESENT, VEST                                      | CORRECT GROUP (BESTOW, Level 1)
   - Group 2: **0.4903** | DOZE, MARVEL, PAC-MAN, PASS NOTES                                 | INCORRECT (Max overlap: 2/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING)
   - Group 3: **0.4586** | TIE, DOODLE, DRAW, PAINT                                          | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE)
   - Group 4: **0.3723** | DEGREE, EVEN, SQUARE, SPACE                                       | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE) | [Pred Type: FILL_IN_THE_BLANK (53.4%, no-rel 21.5%)]
2. **Partition Score: 0.4145**
   - Group 1: **0.5982** | GRANT, CONFER, PRESENT, VEST                                      | CORRECT GROUP (BESTOW, Level 1)
   - Group 2: **0.4586** | TIE, DOODLE, DRAW, PAINT                                          | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE)
   - Group 3: **0.4274** | MARVEL, PAC-MAN, PASS NOTES, SPACE                                | INCORRECT (Max overlap: 2/4 with WORDS AFTER THE LETTERS “MS”)
   - Group 4: **0.3861** | DEGREE, EVEN, DOZE, SQUARE                                        | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE) | [Pred Type: FILL_IN_THE_BLANK (47.8%, no-rel 19.7%)]
3. **Partition Score: 0.3961**
   - Group 1: **0.5982** | GRANT, CONFER, PRESENT, VEST                                      | CORRECT GROUP (BESTOW, Level 1)
   - Group 2: **0.4903** | DOZE, MARVEL, PAC-MAN, PASS NOTES                                 | INCORRECT (Max overlap: 2/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING)
   - Group 3: **0.3683** | EVEN, DOODLE, DRAW, PAINT                                         | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE)
   - Group 4: **0.3629** | DEGREE, TIE, SQUARE, SPACE                                        | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE) | [Pred Type: FILL_IN_THE_BLANK (54.4%, no-rel 17.6%)]
4. **Partition Score: 0.3954**
   - Group 1: **0.5233** | DOODLE, PRESENT, DRAW, PAINT                                      | INCORRECT (Max overlap: 1/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING)
   - Group 2: **0.4903** | DOZE, MARVEL, PAC-MAN, PASS NOTES                                 | INCORRECT (Max overlap: 2/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING)
   - Group 3: **0.3723** | DEGREE, EVEN, SQUARE, SPACE                                       | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE) | [Pred Type: FILL_IN_THE_BLANK (53.4%, no-rel 21.5%)]
   - Group 4: **0.3595** | TIE, GRANT, CONFER, VEST                                          | INCORRECT (Max overlap: 3/4 with BESTOW)
5. **Partition Score: 0.3934**
   - Group 1: **0.4903** | DOZE, MARVEL, PAC-MAN, PASS NOTES                                 | INCORRECT (Max overlap: 2/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING)
   - Group 2: **0.4586** | TIE, DOODLE, DRAW, PAINT                                          | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE)
   - Group 3: **0.4247** | DEGREE, PRESENT, SQUARE, SPACE                                    | INCORRECT (Max overlap: 1/4 with WORDS AFTER THE LETTERS “MS”) | [Pred Type: FILL_IN_THE_BLANK (48.2%, no-rel 21.0%)]
   - Group 4: **0.3451** | GRANT, EVEN, CONFER, VEST                                         | INCORRECT (Max overlap: 3/4 with BESTOW) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 35.4%)]

### Top Candidate Groups:
   - Group 1: **0.5982** | GRANT, CONFER, PRESENT, VEST                                      | CORRECT GROUP (BESTOW, Level 1)
   - Group 2: **0.4903** | DOZE, MARVEL, PAC-MAN, PASS NOTES                                 | INCORRECT (Max overlap: 2/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING)
   - Group 3: **0.4586** | TIE, DOODLE, DRAW, PAINT                                          | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE)
   - Group 4: **0.3723** | DEGREE, EVEN, SQUARE, SPACE                                       | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE) | [Pred Type: FILL_IN_THE_BLANK (53.4%, no-rel 21.5%)]
   - Group 5: **0.4274** | MARVEL, PAC-MAN, PASS NOTES, SPACE                                | INCORRECT (Max overlap: 2/4 with WORDS AFTER THE LETTERS “MS”)
   - Group 6: **0.3861** | DEGREE, EVEN, DOZE, SQUARE                                        | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE) | [Pred Type: FILL_IN_THE_BLANK (47.8%, no-rel 19.7%)]
   - Group 7: **0.3683** | EVEN, DOODLE, DRAW, PAINT                                         | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE)
   - Group 8: **0.3629** | DEGREE, TIE, SQUARE, SPACE                                        | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE) | [Pred Type: FILL_IN_THE_BLANK (54.4%, no-rel 17.6%)]
   - Group 9: **0.5233** | DOODLE, PRESENT, DRAW, PAINT                                      | INCORRECT (Max overlap: 1/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING)
   - Group 10: **0.3595** | TIE, GRANT, CONFER, VEST                                          | INCORRECT (Max overlap: 3/4 with BESTOW)
   - Group 11: **0.4247** | DEGREE, PRESENT, SQUARE, SPACE                                    | INCORRECT (Max overlap: 1/4 with WORDS AFTER THE LETTERS “MS”) | [Pred Type: FILL_IN_THE_BLANK (48.2%, no-rel 21.0%)]
   - Group 12: **0.3451** | GRANT, EVEN, CONFER, VEST                                         | INCORRECT (Max overlap: 3/4 with BESTOW) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 35.4%)]
   - Group 13: **0.4948** | DOZE, MARVEL, PAC-MAN, SPACE                                      | INCORRECT (Max overlap: 2/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING)
   - Group 14: **0.3648** | DEGREE, TIE, EVEN, SQUARE                                         | INCORRECT (Max overlap: 3/4 with MAKE EQUAL, AS A SCORE)
   - Group 15: **0.3458** | DOODLE, DRAW, PASS NOTES, PAINT                                   | INCORRECT (Max overlap: 2/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING) | [Pred Type: SEMANTIC_SET (50.5%, no-rel 22.7%)]
   - Group 16: **0.3441** | DOODLE, DRAW, SPACE, PAINT                                        | INCORRECT (Max overlap: 2/4 with THINGS YOU MIGHT DO DURING A BORING CLASS/MEETING) | [Pred Type: SEMANTIC_SET (49.6%, no-rel 20.0%)]
   - Group 17: **0.3381** | GRANT, CONFER, VEST, PASS NOTES                                   | INCORRECT (Max overlap: 3/4 with BESTOW) | [Pred Type: SYNONYM_OR_NEAR (49.0%, no-rel 29.9%)]
   - Group 18: **0.4847** | DOODLE, SQUARE, DRAW, PAINT                                       | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE) | [Pred Type: SEMANTIC_SET (45.6%, no-rel 30.8%)]
   - Group 19: **0.3688** | GRANT, CONFER, PRESENT, PASS NOTES                                | INCORRECT (Max overlap: 3/4 with BESTOW) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 22.4%)]
   - Group 20: **0.3400** | DEGREE, TIE, EVEN, VEST                                           | INCORRECT (Max overlap: 2/4 with MAKE EQUAL, AS A SCORE)

---

## Puzzle 80 (ID: 274)
**Words on Board:** MEOW, PAMPER, EYE, SLIPPERS, MOTHER, CRADLE, ROBE, TOWEL, PAJAMAS, WASHCLOTH, SPOIL, BABY, CAN, BUM, REAR, BOOTY

### Ground Truth Categories:
* **Level 0 (TREAT WITH EXCESSIVE CARE) [Type: SYNONYM_OR_NEAR]:** BABY, MOTHER, PAMPER, SPOIL
* **Level 1 (BACKSIDE) [Type: SYNONYM_OR_NEAR]:** BOOTY, BUM, CAN, REAR
* **Level 2 (THINGS IN A SPA LOCKER ROOM) [Type: SEMANTIC_SET]:** ROBE, SLIPPERS, TOWEL, WASHCLOTH
* **Level 3 (CAT’S ___) [Type: FILL_IN_THE_BLANK]:** CRADLE, EYE, MEOW, PAJAMAS

### Top Candidate Partitions:
1. **Partition Score: 0.4494**
   - Group 1: **0.6845** | SLIPPERS, TOWEL, PAJAMAS, WASHCLOTH                               | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 2: **0.5948** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (67.5%, no-rel 26.1%)]
   - Group 3: **0.4532** | MEOW, CRADLE, BUM, REAR                                           | INCORRECT (Max overlap: 2/4 with CAT’S ___) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 30.9%)]
   - Group 4: **0.3748** | EYE, MOTHER, ROBE, CAN                                            | INCORRECT (Max overlap: 1/4 with CAT’S ___)
2. **Partition Score: 0.4459**
   - Group 1: **0.6845** | SLIPPERS, TOWEL, PAJAMAS, WASHCLOTH                               | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 2: **0.5959** | PAMPER, CRADLE, SPOIL, BABY                                       | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (76.6%, no-rel 16.0%)]
   - Group 3: **0.4380** | MEOW, BUM, REAR, BOOTY                                            | INCORRECT (Max overlap: 3/4 with BACKSIDE) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 34.2%)]
   - Group 4: **0.3748** | EYE, MOTHER, ROBE, CAN                                            | INCORRECT (Max overlap: 1/4 with CAT’S ___)
3. **Partition Score: 0.4249**
   - Group 1: **0.6845** | SLIPPERS, TOWEL, PAJAMAS, WASHCLOTH                               | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 2: **0.5030** | MEOW, PAMPER, SPOIL, BABY                                         | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (73.1%, no-rel 19.1%)]
   - Group 3: **0.4470** | CRADLE, BUM, REAR, BOOTY                                          | INCORRECT (Max overlap: 3/4 with BACKSIDE) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 32.5%)]
   - Group 4: **0.3748** | EYE, MOTHER, ROBE, CAN                                            | INCORRECT (Max overlap: 1/4 with CAT’S ___)
4. **Partition Score: 0.4159**
   - Group 1: **0.7332** | SLIPPERS, ROBE, PAJAMAS, WASHCLOTH                                | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 2: **0.5948** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (67.5%, no-rel 26.1%)]
   - Group 3: **0.3748** | EYE, MOTHER, TOWEL, BUM                                           | INCORRECT (Max overlap: 1/4 with CAT’S ___)
   - Group 4: **0.3471** | MEOW, CRADLE, CAN, REAR                                           | INCORRECT (Max overlap: 2/4 with CAT’S ___) | [Pred Type: SYNONYM_OR_NEAR (53.0%, no-rel 28.8%)]
5. **Partition Score: 0.4157**
   - Group 1: **0.6845** | SLIPPERS, TOWEL, PAJAMAS, WASHCLOTH                               | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 2: **0.5948** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (67.5%, no-rel 26.1%)]
   - Group 3: **0.3623** | MEOW, MOTHER, CRADLE, REAR                                        | INCORRECT (Max overlap: 2/4 with CAT’S ___) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 30.5%)]
   - Group 4: **0.3529** | EYE, ROBE, CAN, BUM                                               | INCORRECT (Max overlap: 2/4 with BACKSIDE)

### Top Candidate Groups:
   - Group 1: **0.6845** | SLIPPERS, TOWEL, PAJAMAS, WASHCLOTH                               | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 2: **0.5948** | PAMPER, SPOIL, BABY, BOOTY                                        | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (67.5%, no-rel 26.1%)]
   - Group 3: **0.4532** | MEOW, CRADLE, BUM, REAR                                           | INCORRECT (Max overlap: 2/4 with CAT’S ___) | [Pred Type: SYNONYM_OR_NEAR (57.5%, no-rel 30.9%)]
   - Group 4: **0.3748** | EYE, MOTHER, ROBE, CAN                                            | INCORRECT (Max overlap: 1/4 with CAT’S ___)
   - Group 5: **0.5959** | PAMPER, CRADLE, SPOIL, BABY                                       | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (76.6%, no-rel 16.0%)]
   - Group 6: **0.4380** | MEOW, BUM, REAR, BOOTY                                            | INCORRECT (Max overlap: 3/4 with BACKSIDE) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 34.2%)]
   - Group 7: **0.5030** | MEOW, PAMPER, SPOIL, BABY                                         | INCORRECT (Max overlap: 3/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (73.1%, no-rel 19.1%)]
   - Group 8: **0.4470** | CRADLE, BUM, REAR, BOOTY                                          | INCORRECT (Max overlap: 3/4 with BACKSIDE) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 32.5%)]
   - Group 9: **0.7332** | SLIPPERS, ROBE, PAJAMAS, WASHCLOTH                                | INCORRECT (Max overlap: 3/4 with THINGS IN A SPA LOCKER ROOM)
   - Group 10: **0.3748** | EYE, MOTHER, TOWEL, BUM                                           | INCORRECT (Max overlap: 1/4 with CAT’S ___)
   - Group 11: **0.3471** | MEOW, CRADLE, CAN, REAR                                           | INCORRECT (Max overlap: 2/4 with CAT’S ___) | [Pred Type: SYNONYM_OR_NEAR (53.0%, no-rel 28.8%)]
   - Group 12: **0.3623** | MEOW, MOTHER, CRADLE, REAR                                        | INCORRECT (Max overlap: 2/4 with CAT’S ___) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 30.5%)]
   - Group 13: **0.3529** | EYE, ROBE, CAN, BUM                                               | INCORRECT (Max overlap: 2/4 with BACKSIDE)
   - Group 14: **0.3681** | EYE, MOTHER, ROBE, BUM                                            | INCORRECT (Max overlap: 1/4 with CAT’S ___)
   - Group 15: **0.3467** | MEOW, MOTHER, REAR, BOOTY                                         | INCORRECT (Max overlap: 2/4 with BACKSIDE)
   - Group 16: **0.4462** | CRADLE, BABY, BUM, REAR                                           | INCORRECT (Max overlap: 2/4 with BACKSIDE) | [Pred Type: SYNONYM_OR_NEAR (60.9%, no-rel 23.9%)]
   - Group 17: **0.4300** | MEOW, PAMPER, SPOIL, BOOTY                                        | INCORRECT (Max overlap: 2/4 with TREAT WITH EXCESSIVE CARE) | [Pred Type: SYNONYM_OR_NEAR (61.9%, no-rel 30.5%)]
   - Group 18: **0.5132** | MEOW, CAN, BUM, REAR                                              | INCORRECT (Max overlap: 3/4 with BACKSIDE) | [Pred Type: SYNONYM_OR_NEAR (54.9%, no-rel 29.3%)]
   - Group 19: **0.3974** | CRADLE, ROBE, PAJAMAS, WASHCLOTH                                  | INCORRECT (Max overlap: 2/4 with CAT’S ___) | [Pred Type: SEMANTIC_SET (47.0%, no-rel 18.6%)]
   - Group 20: **0.3550** | EYE, SLIPPERS, MOTHER, TOWEL                                      | INCORRECT (Max overlap: 2/4 with THINGS IN A SPA LOCKER ROOM)

---

## Puzzle 81 (ID: 770)
**Words on Board:** DRY, GIN, BOUNCE, TWIST, DRAG, PUFF, CROSS, SWAY, SHAKEN, DRAW, BOP, LOAN, PULL, PASS, GROOVE, BUZZ

### Ground Truth Categories:
* **Level 0 (MOVE TO THE MUSIC) [Type: SYNONYM_OR_NEAR]:** BOP, BOUNCE, GROOVE, SWAY
* **Level 1 (INHALATION) [Type: SYNONYM_OR_NEAR]:** DRAG, DRAW, PUFF, PULL
* **Level 2 (MARTINI SPECIFICATIONS) [Type: SEMANTIC_SET]:** DRY, GIN, SHAKEN, TWIST
* **Level 3 (___WORD) [Type: FILL_IN_THE_BLANK]:** BUZZ, CROSS, LOAN, PASS

### Top Candidate Partitions:
1. **Partition Score: 0.4568**
   - Group 1: **0.6008** | DRAG, PUFF, SWAY, PULL                                            | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (62.9%, no-rel 28.1%)]
   - Group 2: **0.4836** | DRY, GIN, SHAKEN, LOAN                                            | INCORRECT (Max overlap: 3/4 with MARTINI SPECIFICATIONS) | [Pred Type: FILL_IN_THE_BLANK (51.9%, no-rel 19.8%)]
   - Group 3: **0.4649** | BOUNCE, CROSS, DRAW, PASS                                         | INCORRECT (Max overlap: 2/4 with ___WORD)
   - Group 4: **0.4393** | TWIST, BOP, GROOVE, BUZZ                                          | INCORRECT (Max overlap: 2/4 with MOVE TO THE MUSIC)
2. **Partition Score: 0.4439**
   - Group 1: **0.6008** | DRAG, PUFF, SWAY, PULL                                            | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (62.9%, no-rel 28.1%)]
   - Group 2: **0.4997** | DRY, BOUNCE, DRAW, PASS                                           | INCORRECT (Max overlap: 1/4 with MARTINI SPECIFICATIONS)
   - Group 3: **0.4582** | TWIST, SHAKEN, BOP, BUZZ                                          | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS)
   - Group 4: **0.4088** | GIN, CROSS, LOAN, GROOVE                                          | INCORRECT (Max overlap: 2/4 with ___WORD)
3. **Partition Score: 0.4397**
   - Group 1: **0.5501** | DRAG, PUFF, PULL, PASS                                            | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (61.3%, no-rel 26.0%)]
   - Group 2: **0.4901** | TWIST, SWAY, SHAKEN, DRAW                                         | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 32.7%)]
   - Group 3: **0.4305** | BOUNCE, BOP, GROOVE, BUZZ                                         | INCORRECT (Max overlap: 3/4 with MOVE TO THE MUSIC)
   - Group 4: **0.4190** | DRY, GIN, CROSS, LOAN                                             | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: FILL_IN_THE_BLANK (64.6%, no-rel 13.9%)]
4. **Partition Score: 0.4394**
   - Group 1: **0.4695** | DRAG, PUFF, PULL, BUZZ                                            | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 30.1%)]
   - Group 2: **0.4649** | BOUNCE, CROSS, DRAW, PASS                                         | INCORRECT (Max overlap: 2/4 with ___WORD)
   - Group 3: **0.4628** | TWIST, SWAY, SHAKEN, BOP                                          | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (50.0%, no-rel 34.5%)]
   - Group 4: **0.4149** | DRY, GIN, LOAN, GROOVE                                            | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: FILL_IN_THE_BLANK (49.2%, no-rel 20.8%)]
5. **Partition Score: 0.4382**
   - Group 1: **0.6008** | DRAG, PUFF, SWAY, PULL                                            | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (62.9%, no-rel 28.1%)]
   - Group 2: **0.4649** | BOUNCE, CROSS, DRAW, PASS                                         | INCORRECT (Max overlap: 2/4 with ___WORD)
   - Group 3: **0.4582** | TWIST, SHAKEN, BOP, BUZZ                                          | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS)
   - Group 4: **0.4149** | DRY, GIN, LOAN, GROOVE                                            | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: FILL_IN_THE_BLANK (49.2%, no-rel 20.8%)]

### Top Candidate Groups:
   - Group 1: **0.6008** | DRAG, PUFF, SWAY, PULL                                            | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (62.9%, no-rel 28.1%)]
   - Group 2: **0.4836** | DRY, GIN, SHAKEN, LOAN                                            | INCORRECT (Max overlap: 3/4 with MARTINI SPECIFICATIONS) | [Pred Type: FILL_IN_THE_BLANK (51.9%, no-rel 19.8%)]
   - Group 3: **0.4649** | BOUNCE, CROSS, DRAW, PASS                                         | INCORRECT (Max overlap: 2/4 with ___WORD)
   - Group 4: **0.4393** | TWIST, BOP, GROOVE, BUZZ                                          | INCORRECT (Max overlap: 2/4 with MOVE TO THE MUSIC)
   - Group 5: **0.4997** | DRY, BOUNCE, DRAW, PASS                                           | INCORRECT (Max overlap: 1/4 with MARTINI SPECIFICATIONS)
   - Group 6: **0.4582** | TWIST, SHAKEN, BOP, BUZZ                                          | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS)
   - Group 7: **0.4088** | GIN, CROSS, LOAN, GROOVE                                          | INCORRECT (Max overlap: 2/4 with ___WORD)
   - Group 8: **0.5501** | DRAG, PUFF, PULL, PASS                                            | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (61.3%, no-rel 26.0%)]
   - Group 9: **0.4901** | TWIST, SWAY, SHAKEN, DRAW                                         | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (49.4%, no-rel 32.7%)]
   - Group 10: **0.4305** | BOUNCE, BOP, GROOVE, BUZZ                                         | INCORRECT (Max overlap: 3/4 with MOVE TO THE MUSIC)
   - Group 11: **0.4190** | DRY, GIN, CROSS, LOAN                                             | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: FILL_IN_THE_BLANK (64.6%, no-rel 13.9%)]
   - Group 12: **0.4695** | DRAG, PUFF, PULL, BUZZ                                            | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 30.1%)]
   - Group 13: **0.4628** | TWIST, SWAY, SHAKEN, BOP                                          | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (50.0%, no-rel 34.5%)]
   - Group 14: **0.4149** | DRY, GIN, LOAN, GROOVE                                            | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS) | [Pred Type: FILL_IN_THE_BLANK (49.2%, no-rel 20.8%)]
   - Group 15: **0.4567** | DRY, CROSS, DRAW, PASS                                            | INCORRECT (Max overlap: 2/4 with ___WORD)
   - Group 16: **0.4533** | BOUNCE, TWIST, BOP, BUZZ                                          | INCORRECT (Max overlap: 2/4 with MOVE TO THE MUSIC)
   - Group 17: **0.4201** | GIN, SHAKEN, LOAN, GROOVE                                         | INCORRECT (Max overlap: 2/4 with MARTINI SPECIFICATIONS)
   - Group 18: **0.6162** | BOUNCE, DRAG, PUFF, PULL                                          | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 31.1%)]
   - Group 19: **0.4420** | TWIST, SWAY, BOP, BUZZ                                            | INCORRECT (Max overlap: 2/4 with MOVE TO THE MUSIC)
   - Group 20: **0.5672** | TWIST, DRAG, PUFF, PULL                                           | INCORRECT (Max overlap: 3/4 with INHALATION) | [Pred Type: SYNONYM_OR_NEAR (62.3%, no-rel 27.3%)]

---

## Puzzle 82 (ID: 550)
**Words on Board:** FUDGE, GEEZ, TEE (SHIRT), BANK, NUTS, DELTA, COMB, SAW, TEE (GOLF), BED, TEA, GEAR, RATS, TI (MUSICAL NOTE), ZIPPER, MOUTH

### Ground Truth Categories:
* **Level 0 (THINGS THAT SOUND LIKE "T") [Type: SOUND_OR_SPELLING]:** TEA, TEE (GOLF), TEE (SHIRT), TI (MUSICAL NOTE)
* **Level 1 (OBJECTS WITH TEETH) [Type: SEMANTIC_SET]:** COMB, GEAR, SAW, ZIPPER
* **Level 2 (MILD OATHS) [Type: SYNONYM_OR_NEAR]:** FUDGE, GEEZ, NUTS, RATS
* **Level 3 (PARTS OF A RIVER) [Type: SEMANTIC_SET]:** BANK, BED, DELTA, MOUTH

### Top Candidate Partitions:
1. **Partition Score: 0.3989**
   - Group 1: **0.4498** | COMB, GEAR, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 2: **0.4152** | BANK, SAW, BED, TEA                                               | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 3: **0.4114** | FUDGE, GEEZ, NUTS, RATS                                           | CORRECT GROUP (MILD OATHS, Level 2)
   - Group 4: **0.3846** | TEE (SHIRT), DELTA, TEE (GOLF), TI (MUSICAL NOTE)                 | INCORRECT (Max overlap: 3/4 with THINGS THAT SOUND LIKE "T")
2. **Partition Score: 0.3956**
   - Group 1: **0.4195** | FUDGE, NUTS, RATS, MOUTH                                          | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 2: **0.4154** | BANK, COMB, GEAR, ZIPPER                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 3: **0.3981** | GEEZ, SAW, BED, TEA                                               | INCORRECT (Max overlap: 1/4 with MILD OATHS)
   - Group 4: **0.3846** | TEE (SHIRT), DELTA, TEE (GOLF), TI (MUSICAL NOTE)                 | INCORRECT (Max overlap: 3/4 with THINGS THAT SOUND LIKE "T")
3. **Partition Score: 0.3943**
   - Group 1: **0.4076** | FUDGE, GEEZ, NUTS, TEA                                            | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 2: **0.4057** | GEAR, RATS, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)
   - Group 3: **0.4026** | BANK, COMB, SAW, BED                                              | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 4: **0.3846** | TEE (SHIRT), DELTA, TEE (GOLF), TI (MUSICAL NOTE)                 | INCORRECT (Max overlap: 3/4 with THINGS THAT SOUND LIKE "T")
4. **Partition Score: 0.3942**
   - Group 1: **0.4498** | COMB, GEAR, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 2: **0.4097** | FUDGE, BANK, NUTS, RATS                                           | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 3: **0.3981** | GEEZ, SAW, BED, TEA                                               | INCORRECT (Max overlap: 1/4 with MILD OATHS)
   - Group 4: **0.3846** | TEE (SHIRT), DELTA, TEE (GOLF), TI (MUSICAL NOTE)                 | INCORRECT (Max overlap: 3/4 with THINGS THAT SOUND LIKE "T")
5. **Partition Score: 0.3918**
   - Group 1: **0.4498** | COMB, GEAR, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 2: **0.4324** | BANK, NUTS, BED, TEA                                              | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 3: **0.3846** | TEE (SHIRT), DELTA, TEE (GOLF), TI (MUSICAL NOTE)                 | INCORRECT (Max overlap: 3/4 with THINGS THAT SOUND LIKE "T")
   - Group 4: **0.3752** | FUDGE, GEEZ, SAW, RATS                                            | INCORRECT (Max overlap: 3/4 with MILD OATHS)

### Top Candidate Groups:
   - Group 1: **0.4498** | COMB, GEAR, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 2: **0.4152** | BANK, SAW, BED, TEA                                               | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 3: **0.4114** | FUDGE, GEEZ, NUTS, RATS                                           | CORRECT GROUP (MILD OATHS, Level 2)
   - Group 4: **0.3846** | TEE (SHIRT), DELTA, TEE (GOLF), TI (MUSICAL NOTE)                 | INCORRECT (Max overlap: 3/4 with THINGS THAT SOUND LIKE "T")
   - Group 5: **0.4195** | FUDGE, NUTS, RATS, MOUTH                                          | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 6: **0.4154** | BANK, COMB, GEAR, ZIPPER                                          | INCORRECT (Max overlap: 3/4 with OBJECTS WITH TEETH)
   - Group 7: **0.3981** | GEEZ, SAW, BED, TEA                                               | INCORRECT (Max overlap: 1/4 with MILD OATHS)
   - Group 8: **0.4076** | FUDGE, GEEZ, NUTS, TEA                                            | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 9: **0.4057** | GEAR, RATS, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)
   - Group 10: **0.4026** | BANK, COMB, SAW, BED                                              | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 11: **0.4097** | FUDGE, BANK, NUTS, RATS                                           | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 12: **0.4324** | BANK, NUTS, BED, TEA                                              | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 13: **0.3752** | FUDGE, GEEZ, SAW, RATS                                            | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 14: **0.3893** | BANK, SAW, BED, RATS                                              | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 15: **0.4203** | BANK, GEAR, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 16: **0.3972** | FUDGE, NUTS, COMB, RATS                                           | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 17: **0.4038** | FUDGE, NUTS, GEAR, RATS                                           | INCORRECT (Max overlap: 3/4 with MILD OATHS)
   - Group 18: **0.3921** | BANK, COMB, ZIPPER, MOUTH                                         | INCORRECT (Max overlap: 2/4 with PARTS OF A RIVER)
   - Group 19: **0.4044** | BANK, NUTS, COMB, RATS                                            | INCORRECT (Max overlap: 2/4 with MILD OATHS)
   - Group 20: **0.3898** | FUDGE, GEAR, ZIPPER, MOUTH                                        | INCORRECT (Max overlap: 2/4 with OBJECTS WITH TEETH)

---

## Puzzle 83 (ID: 908)
**Words on Board:** NEWTON, STANDARD, MONSTER, ADDERALL, CAR, TOADY, INCREDIBLE, MINION, TEMPER, MODERATE, COOL, AVERAGE, PAR, SETTLE, MONITORSHIP, MEAN

### Ground Truth Categories:
* **Level 0 (NORM) [Type: SYNONYM_OR_NEAR]:** AVERAGE, MEAN, PAR, STANDARD
* **Level 1 (MOLLIFY) [Type: SYNONYM_OR_NEAR]:** COOL, MODERATE, SETTLE, TEMPER
* **Level 2 (MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE) [Type: NAMED_ENTITY_SET]:** CAR, INCREDIBLE, MINION, MONSTER
* **Level 3 (STARTING WITH HERPETOFAUNA) [Type: WORD_FORM]:** ADDERALL, MONITORSHIP, NEWTON, TOADY

### Top Candidate Partitions:
1. **Partition Score: 0.4977**
   - Group 1: **0.7843** | STANDARD, AVERAGE, PAR, MEAN                                      | CORRECT GROUP (NORM, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 33.8%)]
   - Group 2: **0.5919** | TEMPER, MODERATE, COOL, SETTLE                                    | CORRECT GROUP (MOLLIFY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 28.3%)]
   - Group 3: **0.5842** | NEWTON, MONSTER, ADDERALL, CAR                                    | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
   - Group 4: **0.4075** | TOADY, INCREDIBLE, MINION, MONITORSHIP                            | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
2. **Partition Score: 0.4583**
   - Group 1: **0.7843** | STANDARD, AVERAGE, PAR, MEAN                                      | CORRECT GROUP (NORM, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 33.8%)]
   - Group 2: **0.5919** | TEMPER, MODERATE, COOL, SETTLE                                    | CORRECT GROUP (MOLLIFY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 28.3%)]
   - Group 3: **0.5753** | MONSTER, ADDERALL, CAR, TOADY                                     | INCORRECT (Max overlap: 2/4 with MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE)
   - Group 4: **0.3330** | NEWTON, INCREDIBLE, MINION, MONITORSHIP                           | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
3. **Partition Score: 0.4562**
   - Group 1: **0.7843** | STANDARD, AVERAGE, PAR, MEAN                                      | CORRECT GROUP (NORM, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 33.8%)]
   - Group 2: **0.5919** | TEMPER, MODERATE, COOL, SETTLE                                    | CORRECT GROUP (MOLLIFY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 28.3%)]
   - Group 3: **0.5330** | NEWTON, MONSTER, CAR, MINION                                      | INCORRECT (Max overlap: 3/4 with MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE)
   - Group 4: **0.3500** | ADDERALL, TOADY, INCREDIBLE, MONITORSHIP                          | INCORRECT (Max overlap: 3/4 with STARTING WITH HERPETOFAUNA) | [Pred Type: WORDPLAY_TRANSFORM (47.7%, no-rel 8.5%)]
4. **Partition Score: 0.4547**
   - Group 1: **0.7843** | STANDARD, AVERAGE, PAR, MEAN                                      | CORRECT GROUP (NORM, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 33.8%)]
   - Group 2: **0.5919** | TEMPER, MODERATE, COOL, SETTLE                                    | CORRECT GROUP (MOLLIFY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 28.3%)]
   - Group 3: **0.5625** | MONSTER, ADDERALL, CAR, MINION                                    | INCORRECT (Max overlap: 3/4 with MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE)
   - Group 4: **0.3322** | NEWTON, TOADY, INCREDIBLE, MONITORSHIP                            | INCORRECT (Max overlap: 3/4 with STARTING WITH HERPETOFAUNA) | [Pred Type: WORDPLAY_TRANSFORM (47.5%, no-rel 12.5%)]
5. **Partition Score: 0.4501**
   - Group 1: **0.7843** | STANDARD, AVERAGE, PAR, MEAN                                      | CORRECT GROUP (NORM, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 33.8%)]
   - Group 2: **0.5919** | TEMPER, MODERATE, COOL, SETTLE                                    | CORRECT GROUP (MOLLIFY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 28.3%)]
   - Group 3: **0.5230** | NEWTON, MONSTER, CAR, TOADY                                       | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
   - Group 4: **0.3428** | ADDERALL, INCREDIBLE, MINION, MONITORSHIP                         | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)

### Top Candidate Groups:
   - Group 1: **0.7843** | STANDARD, AVERAGE, PAR, MEAN                                      | CORRECT GROUP (NORM, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 33.8%)]
   - Group 2: **0.5919** | TEMPER, MODERATE, COOL, SETTLE                                    | CORRECT GROUP (MOLLIFY, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.7%, no-rel 28.3%)]
   - Group 3: **0.5842** | NEWTON, MONSTER, ADDERALL, CAR                                    | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
   - Group 4: **0.4075** | TOADY, INCREDIBLE, MINION, MONITORSHIP                            | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
   - Group 5: **0.5753** | MONSTER, ADDERALL, CAR, TOADY                                     | INCORRECT (Max overlap: 2/4 with MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE)
   - Group 6: **0.3330** | NEWTON, INCREDIBLE, MINION, MONITORSHIP                           | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
   - Group 7: **0.5330** | NEWTON, MONSTER, CAR, MINION                                      | INCORRECT (Max overlap: 3/4 with MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE)
   - Group 8: **0.3500** | ADDERALL, TOADY, INCREDIBLE, MONITORSHIP                          | INCORRECT (Max overlap: 3/4 with STARTING WITH HERPETOFAUNA) | [Pred Type: WORDPLAY_TRANSFORM (47.7%, no-rel 8.5%)]
   - Group 9: **0.5625** | MONSTER, ADDERALL, CAR, MINION                                    | INCORRECT (Max overlap: 3/4 with MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE)
   - Group 10: **0.3322** | NEWTON, TOADY, INCREDIBLE, MONITORSHIP                            | INCORRECT (Max overlap: 3/4 with STARTING WITH HERPETOFAUNA) | [Pred Type: WORDPLAY_TRANSFORM (47.5%, no-rel 12.5%)]
   - Group 11: **0.5230** | NEWTON, MONSTER, CAR, TOADY                                       | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
   - Group 12: **0.3428** | ADDERALL, INCREDIBLE, MINION, MONITORSHIP                         | INCORRECT (Max overlap: 2/4 with STARTING WITH HERPETOFAUNA)
   - Group 13: **0.4880** | MONSTER, ADDERALL, CAR, INCREDIBLE                                | INCORRECT (Max overlap: 3/4 with MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE)
   - Group 14: **0.3414** | NEWTON, TOADY, MINION, MONITORSHIP                                | INCORRECT (Max overlap: 3/4 with STARTING WITH HERPETOFAUNA)
   - Group 15: **0.5062** | STANDARD, AVERAGE, PAR, SETTLE                                    | INCORRECT (Max overlap: 3/4 with NORM)
   - Group 16: **0.4399** | TEMPER, MODERATE, COOL, MEAN                                      | INCORRECT (Max overlap: 3/4 with MOLLIFY) | [Pred Type: SYNONYM_OR_NEAR (54.6%, no-rel 31.1%)]
   - Group 17: **0.4518** | NEWTON, MONSTER, CAR, INCREDIBLE                                  | INCORRECT (Max overlap: 3/4 with MEMBER OF A TITULAR GROUP IN AN ANIMATION FRANCHISE)
   - Group 18: **0.3574** | ADDERALL, TOADY, MINION, MONITORSHIP                              | INCORRECT (Max overlap: 3/4 with STARTING WITH HERPETOFAUNA)
   - Group 19: **0.4891** | AVERAGE, PAR, SETTLE, MEAN                                        | INCORRECT (Max overlap: 3/4 with NORM) | [Pred Type: SYNONYM_OR_NEAR (55.4%, no-rel 34.4%)]
   - Group 20: **0.4523** | STANDARD, TEMPER, MODERATE, COOL                                  | INCORRECT (Max overlap: 3/4 with MOLLIFY) | [Pred Type: SYNONYM_OR_NEAR (61.6%, no-rel 28.3%)]

---

## Puzzle 84 (ID: 700)
**Words on Board:** SUIT, HEALTH, LEVEL, PLEASE, EARTH, SHAKE, DODGE, DELIGHT, SUPERIOR, BOSS, GOOSE, POWER-UP, SKIRT, TICKLE, MAY I, DUCK

### Ground Truth Categories:
* **Level 0 (MAKE HAPPY) [Type: SYNONYM_OR_NEAR]:** DELIGHT, PLEASE, SUIT, TICKLE
* **Level 1 (EVADE) [Type: SYNONYM_OR_NEAR]:** DODGE, DUCK, SHAKE, SKIRT
* **Level 2 (COMMON VIDEO GAME FEATURES) [Type: SEMANTIC_SET]:** BOSS, LEVEL, HEALTH, POWER-UP
* **Level 3 (MOTHER ___) [Type: FILL_IN_THE_BLANK]:** EARTH, GOOSE, MAY I, SUPERIOR

### Top Candidate Partitions:
1. **Partition Score: 0.3789**
   - Group 1: **0.5102** | PLEASE, DELIGHT, TICKLE, MAY I                                    | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 38.3%)]
   - Group 2: **0.4534** | DODGE, GOOSE, SKIRT, DUCK                                         | INCORRECT (Max overlap: 3/4 with EVADE) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 25.6%)]
   - Group 3: **0.4106** | HEALTH, LEVEL, EARTH, SHAKE                                       | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES)
   - Group 4: **0.3258** | SUIT, SUPERIOR, BOSS, POWER-UP                                    | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES) | [Pred Type: SYNONYM_OR_NEAR (49.2%, no-rel 27.5%)]
2. **Partition Score: 0.3704**
   - Group 1: **0.5271** | SHAKE, DODGE, SKIRT, DUCK                                         | CORRECT GROUP (EVADE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (57.9%, no-rel 23.1%)]
   - Group 2: **0.5102** | PLEASE, DELIGHT, TICKLE, MAY I                                    | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 38.3%)]
   - Group 3: **0.3258** | SUIT, SUPERIOR, BOSS, POWER-UP                                    | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES) | [Pred Type: SYNONYM_OR_NEAR (49.2%, no-rel 27.5%)]
   - Group 4: **0.3228** | HEALTH, LEVEL, EARTH, GOOSE                                       | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES)
3. **Partition Score: 0.3691**
   - Group 1: **0.4534** | DODGE, GOOSE, SKIRT, DUCK                                         | INCORRECT (Max overlap: 3/4 with EVADE) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 25.6%)]
   - Group 2: **0.4267** | PLEASE, POWER-UP, TICKLE, MAY I                                   | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 3: **0.4106** | HEALTH, LEVEL, EARTH, SHAKE                                       | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES)
   - Group 4: **0.3196** | SUIT, DELIGHT, SUPERIOR, BOSS                                     | INCORRECT (Max overlap: 2/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (45.5%, no-rel 27.2%)]
4. **Partition Score: 0.3668**
   - Group 1: **0.5102** | PLEASE, DELIGHT, TICKLE, MAY I                                    | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 38.3%)]
   - Group 2: **0.4113** | SUIT, SUPERIOR, BOSS, SKIRT                                       | INCORRECT (Max overlap: 1/4 with MAKE HAPPY)
   - Group 3: **0.3851** | SHAKE, DODGE, GOOSE, DUCK                                         | INCORRECT (Max overlap: 3/4 with EVADE) | [Pred Type: SYNONYM_OR_NEAR (46.6%, no-rel 24.1%)]
   - Group 4: **0.3354** | HEALTH, LEVEL, EARTH, POWER-UP                                    | INCORRECT (Max overlap: 3/4 with COMMON VIDEO GAME FEATURES)
5. **Partition Score: 0.3614**
   - Group 1: **0.4132** | SHAKE, DODGE, TICKLE, DUCK                                        | INCORRECT (Max overlap: 3/4 with EVADE) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 26.7%)]
   - Group 2: **0.4113** | SUIT, SUPERIOR, BOSS, SKIRT                                       | INCORRECT (Max overlap: 1/4 with MAKE HAPPY)
   - Group 3: **0.3887** | PLEASE, DELIGHT, POWER-UP, MAY I                                  | INCORRECT (Max overlap: 2/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (61.5%, no-rel 30.3%)]
   - Group 4: **0.3228** | HEALTH, LEVEL, EARTH, GOOSE                                       | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES)

### Top Candidate Groups:
   - Group 1: **0.5102** | PLEASE, DELIGHT, TICKLE, MAY I                                    | INCORRECT (Max overlap: 3/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (52.2%, no-rel 38.3%)]
   - Group 2: **0.4534** | DODGE, GOOSE, SKIRT, DUCK                                         | INCORRECT (Max overlap: 3/4 with EVADE) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 25.6%)]
   - Group 3: **0.4106** | HEALTH, LEVEL, EARTH, SHAKE                                       | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES)
   - Group 4: **0.3258** | SUIT, SUPERIOR, BOSS, POWER-UP                                    | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES) | [Pred Type: SYNONYM_OR_NEAR (49.2%, no-rel 27.5%)]
   - Group 5: **0.5271** | SHAKE, DODGE, SKIRT, DUCK                                         | CORRECT GROUP (EVADE, Level 1) | [Pred Type: SYNONYM_OR_NEAR (57.9%, no-rel 23.1%)]
   - Group 6: **0.3228** | HEALTH, LEVEL, EARTH, GOOSE                                       | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES)
   - Group 7: **0.4267** | PLEASE, POWER-UP, TICKLE, MAY I                                   | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 8: **0.3196** | SUIT, DELIGHT, SUPERIOR, BOSS                                     | INCORRECT (Max overlap: 2/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (45.5%, no-rel 27.2%)]
   - Group 9: **0.4113** | SUIT, SUPERIOR, BOSS, SKIRT                                       | INCORRECT (Max overlap: 1/4 with MAKE HAPPY)
   - Group 10: **0.3851** | SHAKE, DODGE, GOOSE, DUCK                                         | INCORRECT (Max overlap: 3/4 with EVADE) | [Pred Type: SYNONYM_OR_NEAR (46.6%, no-rel 24.1%)]
   - Group 11: **0.3354** | HEALTH, LEVEL, EARTH, POWER-UP                                    | INCORRECT (Max overlap: 3/4 with COMMON VIDEO GAME FEATURES)
   - Group 12: **0.4132** | SHAKE, DODGE, TICKLE, DUCK                                        | INCORRECT (Max overlap: 3/4 with EVADE) | [Pred Type: SYNONYM_OR_NEAR (53.7%, no-rel 26.7%)]
   - Group 13: **0.3887** | PLEASE, DELIGHT, POWER-UP, MAY I                                  | INCORRECT (Max overlap: 2/4 with MAKE HAPPY) | [Pred Type: SYNONYM_OR_NEAR (61.5%, no-rel 30.3%)]
   - Group 14: **0.3181** | HEALTH, LEVEL, EARTH, DELIGHT                                     | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES) | [Pred Type: FILL_IN_THE_BLANK (54.3%, no-rel 10.4%)]
   - Group 15: **0.3798** | HEALTH, LEVEL, EARTH, BOSS                                        | INCORRECT (Max overlap: 3/4 with COMMON VIDEO GAME FEATURES)
   - Group 16: **0.3242** | SUIT, DELIGHT, SUPERIOR, SKIRT                                    | INCORRECT (Max overlap: 2/4 with MAKE HAPPY)
   - Group 17: **0.3915** | SUIT, LEVEL, SUPERIOR, BOSS                                       | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES) | [Pred Type: SYNONYM_OR_NEAR (45.4%, no-rel 26.9%)]
   - Group 18: **0.3134** | HEALTH, EARTH, SHAKE, TICKLE                                      | INCORRECT (Max overlap: 1/4 with COMMON VIDEO GAME FEATURES)
   - Group 19: **0.3100** | HEALTH, LEVEL, EARTH, TICKLE                                      | INCORRECT (Max overlap: 2/4 with COMMON VIDEO GAME FEATURES)
   - Group 20: **0.3243** | SHAKE, DODGE, DELIGHT, DUCK                                       | INCORRECT (Max overlap: 3/4 with EVADE) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 20.0%)]

---

## Puzzle 85 (ID: 118)
**Words on Board:** HANNAH, SAVANNA, CLIFF, SHARON, AARON, DREW, ROSE, EVE, WILL, DARREN, OTTO, NATAN, MAY, KAREN, DALE, BROOK

### Ground Truth Categories:
* **Level 0 (RHYMES) [Type: SOUND_OR_SPELLING]:** DARREN, KAREN, SHARON, AARON
* **Level 1 (NATURAL FEATURES) [Type: SEMANTIC_SET]:** DALE, BROOK, SAVANNA, CLIFF
* **Level 2 (IRREGULAR VERBS) [Type: SEMANTIC_SET]:** DREW, ROSE, WILL, MAY
* **Level 3 (PALINDROMES) [Type: WORD_FORM]:** EVE, HANNAH, OTTO, NATAN

### Top Candidate Partitions:
1. **Partition Score: 0.4939**
   - Group 1: **0.5452** | DREW, ROSE, WILL, MAY                                             | CORRECT GROUP (IRREGULAR VERBS, Level 2)
   - Group 2: **0.5077** | SHARON, DARREN, OTTO, DALE                                        | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 3: **0.4959** | HANNAH, AARON, EVE, NATAN                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 4: **0.4861** | SAVANNA, CLIFF, KAREN, BROOK                                      | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES)
2. **Partition Score: 0.4930**
   - Group 1: **0.5452** | DREW, ROSE, WILL, MAY                                             | CORRECT GROUP (IRREGULAR VERBS, Level 2)
   - Group 2: **0.5038** | SAVANNA, CLIFF, DARREN, BROOK                                     | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES)
   - Group 3: **0.4968** | AARON, EVE, NATAN, KAREN                                          | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 4: **0.4858** | HANNAH, SHARON, OTTO, DALE                                        | INCORRECT (Max overlap: 2/4 with PALINDROMES) | [Pred Type: NAMED_ENTITY_SET (45.6%, no-rel 14.0%)]
3. **Partition Score: 0.4912**
   - Group 1: **0.5452** | DREW, ROSE, WILL, MAY                                             | CORRECT GROUP (IRREGULAR VERBS, Level 2)
   - Group 2: **0.5063** | HANNAH, AARON, EVE, OTTO                                          | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.4865** | SHARON, DARREN, NATAN, DALE                                       | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 4: **0.4861** | SAVANNA, CLIFF, KAREN, BROOK                                      | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES)
4. **Partition Score: 0.4855**
   - Group 1: **0.5452** | DREW, ROSE, WILL, MAY                                             | CORRECT GROUP (IRREGULAR VERBS, Level 2)
   - Group 2: **0.5089** | AARON, EVE, OTTO, NATAN                                           | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 3: **0.4861** | SAVANNA, CLIFF, KAREN, BROOK                                      | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES)
   - Group 4: **0.4735** | HANNAH, SHARON, DARREN, DALE                                      | INCORRECT (Max overlap: 2/4 with RHYMES)
5. **Partition Score: 0.4849**
   - Group 1: **0.5452** | DREW, ROSE, WILL, MAY                                             | CORRECT GROUP (IRREGULAR VERBS, Level 2)
   - Group 2: **0.4988** | HANNAH, SAVANNA, AARON, EVE                                       | INCORRECT (Max overlap: 2/4 with PALINDROMES) | [Pred Type: NAMED_ENTITY_SET (46.3%, no-rel 16.0%)]
   - Group 3: **0.4865** | SHARON, DARREN, NATAN, DALE                                       | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 4: **0.4772** | CLIFF, OTTO, KAREN, BROOK                                         | INCORRECT (Max overlap: 2/4 with NATURAL FEATURES)

### Top Candidate Groups:
   - Group 1: **0.5452** | DREW, ROSE, WILL, MAY                                             | CORRECT GROUP (IRREGULAR VERBS, Level 2)
   - Group 2: **0.5077** | SHARON, DARREN, OTTO, DALE                                        | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 3: **0.4959** | HANNAH, AARON, EVE, NATAN                                         | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 4: **0.4861** | SAVANNA, CLIFF, KAREN, BROOK                                      | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES)
   - Group 5: **0.5038** | SAVANNA, CLIFF, DARREN, BROOK                                     | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES)
   - Group 6: **0.4968** | AARON, EVE, NATAN, KAREN                                          | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 7: **0.4858** | HANNAH, SHARON, OTTO, DALE                                        | INCORRECT (Max overlap: 2/4 with PALINDROMES) | [Pred Type: NAMED_ENTITY_SET (45.6%, no-rel 14.0%)]
   - Group 8: **0.5063** | HANNAH, AARON, EVE, OTTO                                          | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 9: **0.4865** | SHARON, DARREN, NATAN, DALE                                       | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 10: **0.5089** | AARON, EVE, OTTO, NATAN                                           | INCORRECT (Max overlap: 3/4 with PALINDROMES)
   - Group 11: **0.4735** | HANNAH, SHARON, DARREN, DALE                                      | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 12: **0.4988** | HANNAH, SAVANNA, AARON, EVE                                       | INCORRECT (Max overlap: 2/4 with PALINDROMES) | [Pred Type: NAMED_ENTITY_SET (46.3%, no-rel 16.0%)]
   - Group 13: **0.4772** | CLIFF, OTTO, KAREN, BROOK                                         | INCORRECT (Max overlap: 2/4 with NATURAL FEATURES)
   - Group 14: **0.4824** | CLIFF, SHARON, KAREN, BROOK                                       | INCORRECT (Max overlap: 2/4 with NATURAL FEATURES)
   - Group 15: **0.4743** | DARREN, OTTO, NATAN, DALE                                         | INCORRECT (Max overlap: 2/4 with PALINDROMES)
   - Group 16: **0.4737** | HANNAH, DARREN, OTTO, DALE                                        | INCORRECT (Max overlap: 2/4 with PALINDROMES)
   - Group 17: **0.4728** | SAVANNA, CLIFF, SHARON, BROOK                                     | INCORRECT (Max overlap: 3/4 with NATURAL FEATURES)
   - Group 18: **0.4715** | AARON, EVE, DARREN, NATAN                                         | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 19: **0.4711** | DARREN, OTTO, KAREN, DALE                                         | INCORRECT (Max overlap: 2/4 with RHYMES)
   - Group 20: **0.4830** | HANNAH, AARON, EVE, KAREN                                         | INCORRECT (Max overlap: 2/4 with PALINDROMES)

---

## Puzzle 86 (ID: 740)
**Words on Board:** MUSEUM, BUTTON, TAPE, RECORD, SHOOT, SNAKE, HITMAN, UNDERTAKER, ROCK, SEAL, SCISSORS, THREAD, FILM, POETIC, PAPER, NEEDLE

### Ground Truth Categories:
* **Level 0 (ITEMS IN A SEWING KIT) [Type: SEMANTIC_SET]:** BUTTON, NEEDLE, SCISSORS, THREAD
* **Level 1 (CAPTURE ON VIDEO) [Type: SYNONYM_OR_NEAR]:** FILM, RECORD, SHOOT, TAPE
* **Level 2 (PRO WRESTLING ICONS, WITH “THE”) [Type: NAMED_ENTITY_SET]:** HITMAN, ROCK, SNAKE, UNDERTAKER
* **Level 3 (WAX ___) [Type: FILL_IN_THE_BLANK]:** MUSEUM, PAPER, POETIC, SEAL

### Top Candidate Partitions:
1. **Partition Score: 0.4828**
   - Group 1: **0.7223** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 27.0%)]
   - Group 2: **0.6583** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.4717** | BUTTON, ROCK, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (56.4%, no-rel 30.6%)]
   - Group 4: **0.4006** | SNAKE, SEAL, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (52.9%, no-rel 22.9%)]
2. **Partition Score: 0.4711**
   - Group 1: **0.7223** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 27.0%)]
   - Group 2: **0.6583** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.4496** | BUTTON, SEAL, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (56.7%, no-rel 29.0%)]
   - Group 4: **0.3883** | SNAKE, ROCK, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”) | [Pred Type: SEMANTIC_SET (53.2%, no-rel 24.2%)]
3. **Partition Score: 0.4655**
   - Group 1: **0.7223** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 27.0%)]
   - Group 2: **0.6583** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.4073** | BUTTON, ROCK, SEAL, PAPER                                         | INCORRECT (Max overlap: 2/4 with WAX ___) | [Pred Type: SEMANTIC_SET (48.2%, no-rel 35.0%)]
   - Group 4: **0.3982** | SNAKE, SCISSORS, THREAD, NEEDLE                                   | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (57.9%, no-rel 18.8%)]
4. **Partition Score: 0.4631**
   - Group 1: **0.7223** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 27.0%)]
   - Group 2: **0.6583** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.4245** | ROCK, SEAL, SCISSORS, PAPER                                       | INCORRECT (Max overlap: 2/4 with WAX ___) | [Pred Type: SEMANTIC_SET (52.9%, no-rel 32.7%)]
   - Group 4: **0.3848** | BUTTON, SNAKE, THREAD, NEEDLE                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (55.0%, no-rel 23.8%)]
5. **Partition Score: 0.4616**
   - Group 1: **0.6583** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 2: **0.5120** | BUTTON, SEAL, SCISSORS, NEEDLE                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (57.9%, no-rel 25.3%)]
   - Group 3: **0.4684** | TAPE, RECORD, ROCK, PAPER                                         | INCORRECT (Max overlap: 2/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 27.9%)]
   - Group 4: **0.4329** | SHOOT, SNAKE, THREAD, FILM                                        | INCORRECT (Max overlap: 2/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (60.5%, no-rel 22.2%)]

### Top Candidate Groups:
   - Group 1: **0.7223** | TAPE, RECORD, SHOOT, FILM                                         | CORRECT GROUP (CAPTURE ON VIDEO, Level 1) | [Pred Type: SYNONYM_OR_NEAR (62.4%, no-rel 27.0%)]
   - Group 2: **0.6583** | MUSEUM, HITMAN, UNDERTAKER, POETIC                                | INCORRECT (Max overlap: 2/4 with WAX ___)
   - Group 3: **0.4717** | BUTTON, ROCK, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (56.4%, no-rel 30.6%)]
   - Group 4: **0.4006** | SNAKE, SEAL, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (52.9%, no-rel 22.9%)]
   - Group 5: **0.4496** | BUTTON, SEAL, SCISSORS, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (56.7%, no-rel 29.0%)]
   - Group 6: **0.3883** | SNAKE, ROCK, THREAD, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with PRO WRESTLING ICONS, WITH “THE”) | [Pred Type: SEMANTIC_SET (53.2%, no-rel 24.2%)]
   - Group 7: **0.4073** | BUTTON, ROCK, SEAL, PAPER                                         | INCORRECT (Max overlap: 2/4 with WAX ___) | [Pred Type: SEMANTIC_SET (48.2%, no-rel 35.0%)]
   - Group 8: **0.3982** | SNAKE, SCISSORS, THREAD, NEEDLE                                   | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (57.9%, no-rel 18.8%)]
   - Group 9: **0.4245** | ROCK, SEAL, SCISSORS, PAPER                                       | INCORRECT (Max overlap: 2/4 with WAX ___) | [Pred Type: SEMANTIC_SET (52.9%, no-rel 32.7%)]
   - Group 10: **0.3848** | BUTTON, SNAKE, THREAD, NEEDLE                                     | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (55.0%, no-rel 23.8%)]
   - Group 11: **0.5120** | BUTTON, SEAL, SCISSORS, NEEDLE                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (57.9%, no-rel 25.3%)]
   - Group 12: **0.4684** | TAPE, RECORD, ROCK, PAPER                                         | INCORRECT (Max overlap: 2/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (49.5%, no-rel 27.9%)]
   - Group 13: **0.4329** | SHOOT, SNAKE, THREAD, FILM                                        | INCORRECT (Max overlap: 2/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (60.5%, no-rel 22.2%)]
   - Group 14: **0.4257** | ROCK, THREAD, PAPER, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (49.4%, no-rel 33.3%)]
   - Group 15: **0.3582** | BUTTON, SNAKE, SEAL, SCISSORS                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (57.5%, no-rel 21.0%)]
   - Group 16: **0.5353** | BUTTON, ROCK, SCISSORS, NEEDLE                                    | INCORRECT (Max overlap: 3/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (61.2%, no-rel 23.1%)]
   - Group 17: **0.4142** | TAPE, RECORD, SEAL, PAPER                                         | INCORRECT (Max overlap: 2/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (52.4%, no-rel 25.8%)]
   - Group 18: **0.4775** | TAPE, RECORD, PAPER, NEEDLE                                       | INCORRECT (Max overlap: 2/4 with CAPTURE ON VIDEO) | [Pred Type: SYNONYM_OR_NEAR (52.0%, no-rel 25.2%)]
   - Group 19: **0.4510** | BUTTON, ROCK, SEAL, SCISSORS                                      | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (58.5%, no-rel 26.1%)]
   - Group 20: **0.3951** | ROCK, SCISSORS, THREAD, PAPER                                     | INCORRECT (Max overlap: 2/4 with ITEMS IN A SEWING KIT) | [Pred Type: SEMANTIC_SET (53.4%, no-rel 31.2%)]

---

## Puzzle 87 (ID: 978)
**Words on Board:** INFERIORITY, ENCYCLOPEDIA, VESTIGE, ATLAS, CALLIOPE, OEDIPUS, RINGMASTER, REMINDER, SUPERIORITY, DIALECT, ELECTRA, THESAURUS, TRACE, DICTIONARY, BUZZARD, ECHO

### Ground Truth Categories:
* **Level 0 (REFERENCE BOOKS) [Type: SEMANTIC_SET]:** ATLAS, DICTIONARY, ENCYCLOPEDIA, THESAURUS
* **Level 1 (SOMETHING THAT BRINGS BACK MEMORIES) [Type: SYNONYM_OR_NEAR]:** ECHO, REMINDER, TRACE, VESTIGE
* **Level 2 (KINDS OF COMPLEXES) [Type: FILL_IN_THE_BLANK]:** ELECTRA, INFERIORITY, OEDIPUS, SUPERIORITY
* **Level 3 (STARTING WITH WAYS TO REACH SOMEONE VIA PHONE) [Type: WORDPLAY_TRANSFORM]:** BUZZARD, CALLIOPE, DIALECT, RINGMASTER

### Top Candidate Partitions:
1. **Partition Score: 0.3501**
   - Group 1: **0.5674** | ENCYCLOPEDIA, ATLAS, THESAURUS, DICTIONARY                        | CORRECT GROUP (REFERENCE BOOKS, Level 0)
   - Group 2: **0.4293** | CALLIOPE, OEDIPUS, ELECTRA, BUZZARD                               | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 3: **0.3930** | RINGMASTER, REMINDER, DIALECT, ECHO                               | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 4: **0.2891** | INFERIORITY, VESTIGE, SUPERIORITY, TRACE                          | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 20.2%)]
2. **Partition Score: 0.3468**
   - Group 1: **0.4442** | CALLIOPE, OEDIPUS, RINGMASTER, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 2: **0.3680** | ENCYCLOPEDIA, SUPERIORITY, THESAURUS, DICTIONARY                  | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 3: **0.3553** | ATLAS, DIALECT, ELECTRA, ECHO                                     | INCORRECT (Max overlap: 1/4 with REFERENCE BOOKS) | [Pred Type: SEMANTIC_SET (46.6%, no-rel 27.3%)]
   - Group 4: **0.3319** | INFERIORITY, VESTIGE, REMINDER, TRACE                             | INCORRECT (Max overlap: 3/4 with SOMETHING THAT BRINGS BACK MEMORIES) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 29.7%)]
3. **Partition Score: 0.3458**
   - Group 1: **0.3905** | OEDIPUS, RINGMASTER, ELECTRA, BUZZARD                             | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
   - Group 2: **0.3680** | ENCYCLOPEDIA, SUPERIORITY, THESAURUS, DICTIONARY                  | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 3: **0.3514** | ATLAS, CALLIOPE, DIALECT, ECHO                                    | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 4: **0.3319** | INFERIORITY, VESTIGE, REMINDER, TRACE                             | INCORRECT (Max overlap: 3/4 with SOMETHING THAT BRINGS BACK MEMORIES) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 29.7%)]
4. **Partition Score: 0.3433**
   - Group 1: **0.5674** | ENCYCLOPEDIA, ATLAS, THESAURUS, DICTIONARY                        | CORRECT GROUP (REFERENCE BOOKS, Level 0)
   - Group 2: **0.4513** | CALLIOPE, OEDIPUS, RINGMASTER, ELECTRA                            | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 3: **0.3437** | REMINDER, DIALECT, BUZZARD, ECHO                                  | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 4: **0.2891** | INFERIORITY, VESTIGE, SUPERIORITY, TRACE                          | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 20.2%)]
5. **Partition Score: 0.3408**
   - Group 1: **0.4565** | CALLIOPE, RINGMASTER, ELECTRA, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 2: **0.3680** | ENCYCLOPEDIA, SUPERIORITY, THESAURUS, DICTIONARY                  | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 3: **0.3319** | INFERIORITY, VESTIGE, REMINDER, TRACE                             | INCORRECT (Max overlap: 3/4 with SOMETHING THAT BRINGS BACK MEMORIES) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 29.7%)]
   - Group 4: **0.3316** | ATLAS, OEDIPUS, DIALECT, ECHO                                     | INCORRECT (Max overlap: 1/4 with REFERENCE BOOKS)

### Top Candidate Groups:
   - Group 1: **0.5674** | ENCYCLOPEDIA, ATLAS, THESAURUS, DICTIONARY                        | CORRECT GROUP (REFERENCE BOOKS, Level 0)
   - Group 2: **0.4293** | CALLIOPE, OEDIPUS, ELECTRA, BUZZARD                               | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 3: **0.3930** | RINGMASTER, REMINDER, DIALECT, ECHO                               | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 4: **0.2891** | INFERIORITY, VESTIGE, SUPERIORITY, TRACE                          | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 20.2%)]
   - Group 5: **0.4442** | CALLIOPE, OEDIPUS, RINGMASTER, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 6: **0.3680** | ENCYCLOPEDIA, SUPERIORITY, THESAURUS, DICTIONARY                  | INCORRECT (Max overlap: 3/4 with REFERENCE BOOKS)
   - Group 7: **0.3553** | ATLAS, DIALECT, ELECTRA, ECHO                                     | INCORRECT (Max overlap: 1/4 with REFERENCE BOOKS) | [Pred Type: SEMANTIC_SET (46.6%, no-rel 27.3%)]
   - Group 8: **0.3319** | INFERIORITY, VESTIGE, REMINDER, TRACE                             | INCORRECT (Max overlap: 3/4 with SOMETHING THAT BRINGS BACK MEMORIES) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 29.7%)]
   - Group 9: **0.3905** | OEDIPUS, RINGMASTER, ELECTRA, BUZZARD                             | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
   - Group 10: **0.3514** | ATLAS, CALLIOPE, DIALECT, ECHO                                    | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 11: **0.4513** | CALLIOPE, OEDIPUS, RINGMASTER, ELECTRA                            | INCORRECT (Max overlap: 2/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 12: **0.3437** | REMINDER, DIALECT, BUZZARD, ECHO                                  | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 13: **0.4565** | CALLIOPE, RINGMASTER, ELECTRA, BUZZARD                            | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 14: **0.3316** | ATLAS, OEDIPUS, DIALECT, ECHO                                     | INCORRECT (Max overlap: 1/4 with REFERENCE BOOKS)
   - Group 15: **0.3580** | ATLAS, CALLIOPE, OEDIPUS, ELECTRA                                 | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES)
   - Group 16: **0.3387** | RINGMASTER, DIALECT, BUZZARD, ECHO                                | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 17: **0.3357** | REMINDER, DIALECT, ELECTRA, ECHO                                  | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 18: **0.3197** | OEDIPUS, REMINDER, DIALECT, ECHO                                  | INCORRECT (Max overlap: 2/4 with SOMETHING THAT BRINGS BACK MEMORIES)
   - Group 19: **0.3756** | CALLIOPE, RINGMASTER, BUZZARD, ECHO                               | INCORRECT (Max overlap: 3/4 with STARTING WITH WAYS TO REACH SOMEONE VIA PHONE)
   - Group 20: **0.3219** | ATLAS, OEDIPUS, DIALECT, ELECTRA                                  | INCORRECT (Max overlap: 2/4 with KINDS OF COMPLEXES) | [Pred Type: SEMANTIC_SET (56.1%, no-rel 22.9%)]

---

## Puzzle 88 (ID: 12)
**Words on Board:** PACK, PRIDE, SIN, TORTOISE, COT, SCHOOL, SLOTH, FLOCK, LUST, POD, GREED, SEC, LORIS, SNAIL, ENVY, TAN

### Ground Truth Categories:
* **Level 0 (ANIMAL GROUP NAMES) [Type: SEMANTIC_SET]:** FLOCK, PACK, POD, SCHOOL
* **Level 1 (DEADLY SINS) [Type: SEMANTIC_SET]:** ENVY, GREED, LUST, PRIDE
* **Level 2 (SLOW ANIMALS) [Type: SEMANTIC_SET]:** LORIS, SLOTH, SNAIL, TORTOISE
* **Level 3 (TRIG FUNCTIONS) [Type: SEMANTIC_SET]:** COT, SEC, SIN, TAN

### Top Candidate Partitions:
1. **Partition Score: 0.5137**
   - Group 1: **0.6478** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 2: **0.6270** | PRIDE, SLOTH, LUST, GREED                                         | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 3: **0.4973** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.4652** | SIN, SEC, ENVY, TAN                                               | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
2. **Partition Score: 0.5073**
   - Group 1: **0.6738** | SLOTH, LUST, GREED, ENVY                                          | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 2: **0.6478** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 3: **0.4973** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.4421** | PRIDE, SIN, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 24.1%)]
3. **Partition Score: 0.5051**
   - Group 1: **0.6478** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 2: **0.6249** | PRIDE, SLOTH, GREED, ENVY                                         | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 3: **0.4973** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.4492** | SIN, LUST, SEC, TAN                                               | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS) | [Pred Type: SYNONYM_OR_NEAR (45.9%, no-rel 22.3%)]
4. **Partition Score: 0.4884**
   - Group 1: **0.6738** | SLOTH, LUST, GREED, ENVY                                          | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 2: **0.6353** | PACK, PRIDE, SCHOOL, POD                                          | INCORRECT (Max overlap: 3/4 with ANIMAL GROUP NAMES)
   - Group 3: **0.4973** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.4105** | SIN, FLOCK, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
5. **Partition Score: 0.4879**
   - Group 1: **0.6478** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 2: **0.6163** | PRIDE, SLOTH, LUST, ENVY                                          | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 3: **0.4973** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.4191** | SIN, GREED, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)

### Top Candidate Groups:
   - Group 1: **0.6478** | PACK, SCHOOL, FLOCK, POD                                          | CORRECT GROUP (ANIMAL GROUP NAMES, Level 0)
   - Group 2: **0.6270** | PRIDE, SLOTH, LUST, GREED                                         | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 3: **0.4973** | TORTOISE, COT, LORIS, SNAIL                                       | INCORRECT (Max overlap: 3/4 with SLOW ANIMALS)
   - Group 4: **0.4652** | SIN, SEC, ENVY, TAN                                               | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
   - Group 5: **0.6738** | SLOTH, LUST, GREED, ENVY                                          | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 6: **0.4421** | PRIDE, SIN, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 24.1%)]
   - Group 7: **0.6249** | PRIDE, SLOTH, GREED, ENVY                                         | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 8: **0.4492** | SIN, LUST, SEC, TAN                                               | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS) | [Pred Type: SYNONYM_OR_NEAR (45.9%, no-rel 22.3%)]
   - Group 9: **0.6353** | PACK, PRIDE, SCHOOL, POD                                          | INCORRECT (Max overlap: 3/4 with ANIMAL GROUP NAMES)
   - Group 10: **0.4105** | SIN, FLOCK, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
   - Group 11: **0.6163** | PRIDE, SLOTH, LUST, ENVY                                          | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 12: **0.4191** | SIN, GREED, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
   - Group 13: **0.8502** | PRIDE, LUST, GREED, ENVY                                          | CORRECT GROUP (DEADLY SINS, Level 1)
   - Group 14: **0.3772** | SIN, SLOTH, SEC, TAN                                              | INCORRECT (Max overlap: 3/4 with TRIG FUNCTIONS)
   - Group 15: **0.4586** | SLOTH, FLOCK, LUST, GREED                                         | INCORRECT (Max overlap: 2/4 with DEADLY SINS)
   - Group 16: **0.4638** | SLOTH, FLOCK, GREED, ENVY                                         | INCORRECT (Max overlap: 2/4 with DEADLY SINS)
   - Group 17: **0.5373** | PRIDE, LUST, SEC, ENVY                                            | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 18: **0.4084** | SIN, SLOTH, GREED, TAN                                            | INCORRECT (Max overlap: 2/4 with TRIG FUNCTIONS)
   - Group 19: **0.5151** | PRIDE, LUST, GREED, SEC                                           | INCORRECT (Max overlap: 3/4 with DEADLY SINS)
   - Group 20: **0.4110** | SIN, SLOTH, ENVY, TAN                                             | INCORRECT (Max overlap: 2/4 with TRIG FUNCTIONS)

---

## Puzzle 89 (ID: 984)
**Words on Board:** LATE, MINION, GREAT, INFINITIVE, AUDITS, DODGERS, SOLID, ABSENT, BACKGROUND, PHEW, EXCUSED, PERFECT, HISTORY, LIFE, PRESENT, PAST

### Ground Truth Categories:
* **Level 0 (EXPERIENCE) [Type: SYNONYM_OR_NEAR]:** BACKGROUND, HISTORY, LIFE, PAST
* **Level 1 (ATTENDANCE STATUS) [Type: SEMANTIC_SET]:** ABSENT, EXCUSED, LATE, PRESENT
* **Level 2 (COMMENTARY ABOUT YOUR CONNECTIONS RESULTS) [Type: SEMANTIC_SET]:** GREAT, PERFECT, PHEW, SOLID
* **Level 3 (CAR BRANDS PLUS TWO LETTERS) [Type: WORDPLAY_TRANSFORM]:** AUDITS, DODGERS, INFINITIVE, MINION

### Top Candidate Partitions:
1. **Partition Score: 0.4277**
   - Group 1: **0.4911** | BACKGROUND, HISTORY, LIFE, PAST                                   | CORRECT GROUP (EXPERIENCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 31.4%)]
   - Group 2: **0.4312** | MINION, INFINITIVE, DODGERS, PHEW                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 3: **0.4289** | LATE, AUDITS, ABSENT, PRESENT                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 4: **0.4254** | GREAT, SOLID, EXCUSED, PERFECT                                    | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
2. **Partition Score: 0.4273**
   - Group 1: **0.5101** | LATE, AUDITS, ABSENT, EXCUSED                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 2: **0.4911** | BACKGROUND, HISTORY, LIFE, PAST                                   | CORRECT GROUP (EXPERIENCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 31.4%)]
   - Group 3: **0.4312** | MINION, INFINITIVE, DODGERS, PHEW                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 4: **0.3936** | GREAT, SOLID, PERFECT, PRESENT                                    | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
3. **Partition Score: 0.4266**
   - Group 1: **0.4911** | BACKGROUND, HISTORY, LIFE, PAST                                   | CORRECT GROUP (EXPERIENCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 31.4%)]
   - Group 2: **0.4475** | AUDITS, ABSENT, EXCUSED, PRESENT                                  | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 3: **0.4312** | MINION, INFINITIVE, DODGERS, PHEW                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 4: **0.4139** | LATE, GREAT, SOLID, PERFECT                                       | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
4. **Partition Score: 0.4211**
   - Group 1: **0.4911** | BACKGROUND, HISTORY, LIFE, PAST                                   | CORRECT GROUP (EXPERIENCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 31.4%)]
   - Group 2: **0.4312** | MINION, INFINITIVE, DODGERS, PHEW                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 3: **0.4183** | AUDITS, ABSENT, PERFECT, PRESENT                                  | INCORRECT (Max overlap: 2/4 with ATTENDANCE STATUS)
   - Group 4: **0.4175** | LATE, GREAT, SOLID, EXCUSED                                       | INCORRECT (Max overlap: 2/4 with ATTENDANCE STATUS)
5. **Partition Score: 0.4089**
   - Group 1: **0.4912** | LATE, ABSENT, EXCUSED, PRESENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1)
   - Group 2: **0.4911** | BACKGROUND, HISTORY, LIFE, PAST                                   | CORRECT GROUP (EXPERIENCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 31.4%)]
   - Group 3: **0.4312** | MINION, INFINITIVE, DODGERS, PHEW                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 4: **0.3567** | GREAT, AUDITS, SOLID, PERFECT                                     | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)

### Top Candidate Groups:
   - Group 1: **0.4911** | BACKGROUND, HISTORY, LIFE, PAST                                   | CORRECT GROUP (EXPERIENCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 31.4%)]
   - Group 2: **0.4312** | MINION, INFINITIVE, DODGERS, PHEW                                 | INCORRECT (Max overlap: 3/4 with CAR BRANDS PLUS TWO LETTERS)
   - Group 3: **0.4289** | LATE, AUDITS, ABSENT, PRESENT                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 4: **0.4254** | GREAT, SOLID, EXCUSED, PERFECT                                    | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 5: **0.5101** | LATE, AUDITS, ABSENT, EXCUSED                                     | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 6: **0.3936** | GREAT, SOLID, PERFECT, PRESENT                                    | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 7: **0.4475** | AUDITS, ABSENT, EXCUSED, PRESENT                                  | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 8: **0.4139** | LATE, GREAT, SOLID, PERFECT                                       | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 9: **0.4183** | AUDITS, ABSENT, PERFECT, PRESENT                                  | INCORRECT (Max overlap: 2/4 with ATTENDANCE STATUS)
   - Group 10: **0.4175** | LATE, GREAT, SOLID, EXCUSED                                       | INCORRECT (Max overlap: 2/4 with ATTENDANCE STATUS)
   - Group 11: **0.4912** | LATE, ABSENT, EXCUSED, PRESENT                                    | CORRECT GROUP (ATTENDANCE STATUS, Level 1)
   - Group 12: **0.3567** | GREAT, AUDITS, SOLID, PERFECT                                     | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 13: **0.4647** | LATE, ABSENT, PERFECT, PRESENT                                    | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 14: **0.3683** | GREAT, AUDITS, SOLID, EXCUSED                                     | INCORRECT (Max overlap: 2/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 15: **0.4775** | ABSENT, EXCUSED, PERFECT, PRESENT                                 | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 16: **0.3610** | LATE, GREAT, AUDITS, SOLID                                        | INCORRECT (Max overlap: 2/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 17: **0.4552** | GREAT, ABSENT, PERFECT, PRESENT                                   | INCORRECT (Max overlap: 2/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)
   - Group 18: **0.3720** | LATE, AUDITS, SOLID, EXCUSED                                      | INCORRECT (Max overlap: 2/4 with ATTENDANCE STATUS)
   - Group 19: **0.4351** | LATE, AUDITS, EXCUSED, PRESENT                                    | INCORRECT (Max overlap: 3/4 with ATTENDANCE STATUS)
   - Group 20: **0.3769** | GREAT, SOLID, ABSENT, PERFECT                                     | INCORRECT (Max overlap: 3/4 with COMMENTARY ABOUT YOUR CONNECTIONS RESULTS)

---

## Puzzle 90 (ID: 567)
**Words on Board:** STRAND, MAROON, RUBY, BEACH, BRICK, PAIR, HEAD, LOCATION, FUR, YOU, LOCK, WISP, CHERRY, TIME, DURATION, DATE

### Ground Truth Categories:
* **Level 0 (SHADES OF RED) [Type: SEMANTIC_SET]:** BRICK, CHERRY, MAROON, RUBY
* **Level 1 (APPOINTMENT SPECIFICATIONS) [Type: SEMANTIC_SET]:** DATE, DURATION, LOCATION, TIME
* **Level 2 (DIFFERENT AMOUNTS OF HAIR) [Type: SEMANTIC_SET]:** HEAD, LOCK, STRAND, WISP
* **Level 3 (TREE HOMOPHONES) [Type: SOUND_OR_SPELLING]:** BEACH, FUR, PAIR, YOU

### Top Candidate Partitions:
1. **Partition Score: 0.3626**
   - Group 1: **0.3866** | STRAND, MAROON, BEACH, PAIR                                       | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES) | [Pred Type: SYNONYM_OR_NEAR (61.6%, no-rel 22.5%)]
   - Group 2: **0.3859** | LOCK, TIME, DURATION, DATE                                        | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 3: **0.3821** | BRICK, HEAD, LOCATION, CHERRY                                     | INCORRECT (Max overlap: 2/4 with SHADES OF RED) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 21.8%)]
   - Group 4: **0.3413** | RUBY, FUR, YOU, WISP                                              | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
2. **Partition Score: 0.3625**
   - Group 1: **0.3866** | STRAND, MAROON, BEACH, PAIR                                       | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES) | [Pred Type: SYNONYM_OR_NEAR (61.6%, no-rel 22.5%)]
   - Group 2: **0.3859** | LOCK, TIME, DURATION, DATE                                        | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 3: **0.3745** | RUBY, BRICK, LOCATION, CHERRY                                     | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 4: **0.3448** | HEAD, FUR, YOU, WISP                                              | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
3. **Partition Score: 0.3569**
   - Group 1: **0.3928** | BEACH, TIME, DURATION, DATE                                       | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 2: **0.3821** | BRICK, HEAD, LOCATION, CHERRY                                     | INCORRECT (Max overlap: 2/4 with SHADES OF RED) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 21.8%)]
   - Group 3: **0.3628** | STRAND, MAROON, PAIR, LOCK                                        | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR) | [Pred Type: SYNONYM_OR_NEAR (62.8%, no-rel 24.9%)]
   - Group 4: **0.3413** | RUBY, FUR, YOU, WISP                                              | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
4. **Partition Score: 0.3567**
   - Group 1: **0.3928** | BEACH, TIME, DURATION, DATE                                       | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 2: **0.3745** | RUBY, BRICK, LOCATION, CHERRY                                     | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 3: **0.3628** | STRAND, MAROON, PAIR, LOCK                                        | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR) | [Pred Type: SYNONYM_OR_NEAR (62.8%, no-rel 24.9%)]
   - Group 4: **0.3448** | HEAD, FUR, YOU, WISP                                              | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
5. **Partition Score: 0.3564**
   - Group 1: **0.3866** | STRAND, MAROON, BEACH, PAIR                                       | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES) | [Pred Type: SYNONYM_OR_NEAR (61.6%, no-rel 22.5%)]
   - Group 2: **0.3745** | RUBY, BRICK, LOCATION, CHERRY                                     | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 3: **0.3671** | YOU, TIME, DURATION, DATE                                         | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 4: **0.3420** | HEAD, FUR, LOCK, WISP                                             | INCORRECT (Max overlap: 3/4 with DIFFERENT AMOUNTS OF HAIR)

### Top Candidate Groups:
   - Group 1: **0.3866** | STRAND, MAROON, BEACH, PAIR                                       | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES) | [Pred Type: SYNONYM_OR_NEAR (61.6%, no-rel 22.5%)]
   - Group 2: **0.3859** | LOCK, TIME, DURATION, DATE                                        | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 3: **0.3821** | BRICK, HEAD, LOCATION, CHERRY                                     | INCORRECT (Max overlap: 2/4 with SHADES OF RED) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 21.8%)]
   - Group 4: **0.3413** | RUBY, FUR, YOU, WISP                                              | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 5: **0.3745** | RUBY, BRICK, LOCATION, CHERRY                                     | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 6: **0.3448** | HEAD, FUR, YOU, WISP                                              | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 7: **0.3928** | BEACH, TIME, DURATION, DATE                                       | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 8: **0.3628** | STRAND, MAROON, PAIR, LOCK                                        | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR) | [Pred Type: SYNONYM_OR_NEAR (62.8%, no-rel 24.9%)]
   - Group 9: **0.3671** | YOU, TIME, DURATION, DATE                                         | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS)
   - Group 10: **0.3420** | HEAD, FUR, LOCK, WISP                                             | INCORRECT (Max overlap: 3/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 11: **0.4024** | PAIR, TIME, DURATION, DATE                                        | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (45.0%, no-rel 33.7%)]
   - Group 12: **0.3507** | STRAND, MAROON, BEACH, LOCK                                       | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 23.7%)]
   - Group 13: **0.3638** | MAROON, TIME, DURATION, DATE                                      | INCORRECT (Max overlap: 3/4 with APPOINTMENT SPECIFICATIONS) | [Pred Type: SYNONYM_OR_NEAR (46.2%, no-rel 27.1%)]
   - Group 14: **0.3552** | STRAND, BEACH, PAIR, LOCK                                         | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 15: **0.4011** | RUBY, BRICK, FUR, CHERRY                                          | INCORRECT (Max overlap: 3/4 with SHADES OF RED)
   - Group 16: **0.3677** | STRAND, MAROON, BEACH, WISP                                       | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR) | [Pred Type: SYNONYM_OR_NEAR (64.5%, no-rel 17.6%)]
   - Group 17: **0.3362** | PAIR, HEAD, LOCATION, LOCK                                        | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR)
   - Group 18: **0.3319** | PAIR, HEAD, FUR, LOCK                                             | INCORRECT (Max overlap: 2/4 with TREE HOMOPHONES)
   - Group 19: **0.3692** | STRAND, MAROON, PAIR, WISP                                        | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR) | [Pred Type: SYNONYM_OR_NEAR (71.1%, no-rel 19.6%)]
   - Group 20: **0.3250** | HEAD, FUR, YOU, LOCK                                              | INCORRECT (Max overlap: 2/4 with DIFFERENT AMOUNTS OF HAIR) | [Pred Type: FILL_IN_THE_BLANK (46.1%, no-rel 21.3%)]

---

## Puzzle 91 (ID: 258)
**Words on Board:** WINE, RIND, HEAVY, WINK, WIND, MILL, SEED, FEATHER, FACTORY, STEM, LIGHT, SHOP, WING, CORE, MIDDLE, PLANT

### Ground Truth Categories:
* **Level 0 (MANUFACTURING LOCATIONS) [Type: SYNONYM_OR_NEAR]:** FACTORY, MILL, PLANT, SHOP
* **Level 1 (WIN + LETTER) [Type: WORDPLAY_TRANSFORM]:** WIND, WINE, WING, WINK
* **Level 2 (PARTS OF FRUIT YOU MIGHT NOT EAT) [Type: SEMANTIC_SET]:** CORE, RIND, SEED, STEM
* **Level 3 (WEIGHTS IN BOXING) [Type: NAMED_ENTITY_SET]:** FEATHER, HEAVY, LIGHT, MIDDLE

### Top Candidate Partitions:
1. **Partition Score: 0.3792**
   - Group 1: **0.4050** | HEAVY, STEM, LIGHT, PLANT                                         | INCORRECT (Max overlap: 2/4 with WEIGHTS IN BOXING)
   - Group 2: **0.3973** | WIND, FEATHER, WING, CORE                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 3: **0.3757** | WINE, RIND, WINK, MIDDLE                                          | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 4: **0.3719** | MILL, SEED, FACTORY, SHOP                                         | INCORRECT (Max overlap: 3/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 27.1%)]
2. **Partition Score: 0.3792**
   - Group 1: **0.4390** | WINK, WIND, FEATHER, WING                                         | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 2: **0.4050** | HEAVY, STEM, LIGHT, PLANT                                         | INCORRECT (Max overlap: 2/4 with WEIGHTS IN BOXING)
   - Group 3: **0.3719** | MILL, SEED, FACTORY, SHOP                                         | INCORRECT (Max overlap: 3/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 27.1%)]
   - Group 4: **0.3699** | WINE, RIND, CORE, MIDDLE                                          | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
3. **Partition Score: 0.3791**
   - Group 1: **0.3995** | MILL, FACTORY, LIGHT, SHOP                                        | INCORRECT (Max overlap: 3/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (55.8%, no-rel 30.2%)]
   - Group 2: **0.3973** | WIND, FEATHER, WING, CORE                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 3: **0.3757** | WINE, RIND, WINK, MIDDLE                                          | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 4: **0.3717** | HEAVY, SEED, STEM, PLANT                                          | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
4. **Partition Score: 0.3778**
   - Group 1: **0.4390** | WINK, WIND, FEATHER, WING                                         | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 2: **0.3995** | MILL, FACTORY, LIGHT, SHOP                                        | INCORRECT (Max overlap: 3/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (55.8%, no-rel 30.2%)]
   - Group 3: **0.3717** | HEAVY, SEED, STEM, PLANT                                          | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 4: **0.3699** | WINE, RIND, CORE, MIDDLE                                          | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
5. **Partition Score: 0.3764**
   - Group 1: **0.4275** | SEED, STEM, CORE, PLANT                                           | INCORRECT (Max overlap: 3/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 2: **0.3995** | MILL, FACTORY, LIGHT, SHOP                                        | INCORRECT (Max overlap: 3/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (55.8%, no-rel 30.2%)]
   - Group 3: **0.3757** | WINE, RIND, WINK, MIDDLE                                          | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 4: **0.3653** | HEAVY, WIND, FEATHER, WING                                        | INCORRECT (Max overlap: 2/4 with WEIGHTS IN BOXING)

### Top Candidate Groups:
   - Group 1: **0.4050** | HEAVY, STEM, LIGHT, PLANT                                         | INCORRECT (Max overlap: 2/4 with WEIGHTS IN BOXING)
   - Group 2: **0.3973** | WIND, FEATHER, WING, CORE                                         | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 3: **0.3757** | WINE, RIND, WINK, MIDDLE                                          | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 4: **0.3719** | MILL, SEED, FACTORY, SHOP                                         | INCORRECT (Max overlap: 3/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 27.1%)]
   - Group 5: **0.4390** | WINK, WIND, FEATHER, WING                                         | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 6: **0.3699** | WINE, RIND, CORE, MIDDLE                                          | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 7: **0.3995** | MILL, FACTORY, LIGHT, SHOP                                        | INCORRECT (Max overlap: 3/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (55.8%, no-rel 30.2%)]
   - Group 8: **0.3717** | HEAVY, SEED, STEM, PLANT                                          | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 9: **0.4275** | SEED, STEM, CORE, PLANT                                           | INCORRECT (Max overlap: 3/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 10: **0.3653** | HEAVY, WIND, FEATHER, WING                                        | INCORRECT (Max overlap: 2/4 with WEIGHTS IN BOXING)
   - Group 11: **0.3939** | WINE, WIND, FEATHER, WING                                         | INCORRECT (Max overlap: 3/4 with WIN + LETTER)
   - Group 12: **0.3686** | RIND, WINK, CORE, MIDDLE                                          | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 13: **0.3824** | HEAVY, WIND, FEATHER, LIGHT                                       | INCORRECT (Max overlap: 3/4 with WEIGHTS IN BOXING) | [Pred Type: SEMANTIC_SET (53.2%, no-rel 32.4%)]
   - Group 14: **0.3811** | SEED, STEM, WING, PLANT                                           | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 15: **0.3643** | MILL, FACTORY, SHOP, CORE                                         | INCORRECT (Max overlap: 3/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 30.8%)]
   - Group 16: **0.3846** | SEED, STEM, MIDDLE, PLANT                                         | INCORRECT (Max overlap: 2/4 with PARTS OF FRUIT YOU MIGHT NOT EAT)
   - Group 17: **0.3692** | WINE, RIND, WINK, CORE                                            | INCORRECT (Max overlap: 2/4 with WIN + LETTER)
   - Group 18: **0.3770** | MILL, SEED, FACTORY, STEM                                         | INCORRECT (Max overlap: 2/4 with MANUFACTURING LOCATIONS) | [Pred Type: SYNONYM_OR_NEAR (53.6%, no-rel 25.2%)]
   - Group 19: **0.3645** | HEAVY, LIGHT, SHOP, PLANT                                         | INCORRECT (Max overlap: 2/4 with WEIGHTS IN BOXING)
   - Group 20: **0.4846** | WIND, FEATHER, LIGHT, WING                                        | INCORRECT (Max overlap: 2/4 with WIN + LETTER)

---

## Puzzle 92 (ID: 1062)
**Words on Board:** HOAGIE, FILTERS, DONUT, ARGUMENT, BELLY, CROP, CAUSE, GROUNDS, BEAN, GRINDER, HERO, MARKUP, ADJUST, BASIS, ROLL, SUB

### Ground Truth Categories:
* **Level 0 (LONG SANDWICH) [Type: SYNONYM_OR_NEAR]:** GRINDER, HERO, HOAGIE, SUB
* **Level 1 (PRETEXT) [Type: SYNONYM_OR_NEAR]:** ARGUMENT, BASIS, CAUSE, GROUNDS
* **Level 2 (SMARTPHONE PHOTO EDITING OPTIONS) [Type: SEMANTIC_SET]:** ADJUST, CROP, FILTERS, MARKUP
* **Level 3 (JELLY ___) [Type: FILL_IN_THE_BLANK]:** BEAN, BELLY, DONUT, ROLL

### Top Candidate Partitions:
1. **Partition Score: 0.4350**
   - Group 1: **0.9146** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 18.4%)]
   - Group 2: **0.6524** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 3: **0.3862** | DONUT, BELLY, BEAN, ROLL                                          | CORRECT GROUP (JELLY ___, Level 3) | [Pred Type: FILL_IN_THE_BLANK (45.7%, no-rel 14.7%)]
   - Group 4: **0.3507** | FILTERS, CROP, MARKUP, ADJUST                                     | CORRECT GROUP (SMARTPHONE PHOTO EDITING OPTIONS, Level 2)
2. **Partition Score: 0.4261**
   - Group 1: **0.9146** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 18.4%)]
   - Group 2: **0.6524** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 3: **0.3846** | DONUT, BELLY, BEAN, MARKUP                                        | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 4: **0.3337** | FILTERS, CROP, ADJUST, ROLL                                       | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
3. **Partition Score: 0.4126**
   - Group 1: **0.9146** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 18.4%)]
   - Group 2: **0.6524** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 3: **0.3663** | BELLY, CROP, BEAN, ROLL                                           | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 4: **0.3158** | FILTERS, DONUT, MARKUP, ADJUST                                    | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
4. **Partition Score: 0.3993**
   - Group 1: **0.9146** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 18.4%)]
   - Group 2: **0.5151** | DONUT, BELLY, CROP, BEAN                                          | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 3: **0.3859** | CAUSE, GROUNDS, BASIS, ROLL                                       | INCORRECT (Max overlap: 3/4 with PRETEXT) | [Pred Type: SYNONYM_OR_NEAR (55.8%, no-rel 34.1%)]
   - Group 4: **0.3481** | FILTERS, ARGUMENT, MARKUP, ADJUST                                 | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
5. **Partition Score: 0.3870**
   - Group 1: **0.6524** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 2: **0.4344** | DONUT, BELLY, BEAN, HERO                                          | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 3: **0.4122** | HOAGIE, GRINDER, ROLL, SUB                                        | INCORRECT (Max overlap: 3/4 with LONG SANDWICH) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 18.6%)]
   - Group 4: **0.3507** | FILTERS, CROP, MARKUP, ADJUST                                     | CORRECT GROUP (SMARTPHONE PHOTO EDITING OPTIONS, Level 2)

### Top Candidate Groups:
   - Group 1: **0.9146** | HOAGIE, GRINDER, HERO, SUB                                        | CORRECT GROUP (LONG SANDWICH, Level 0) | [Pred Type: SYNONYM_OR_NEAR (60.2%, no-rel 18.4%)]
   - Group 2: **0.6524** | ARGUMENT, CAUSE, GROUNDS, BASIS                                   | CORRECT GROUP (PRETEXT, Level 1)
   - Group 3: **0.3862** | DONUT, BELLY, BEAN, ROLL                                          | CORRECT GROUP (JELLY ___, Level 3) | [Pred Type: FILL_IN_THE_BLANK (45.7%, no-rel 14.7%)]
   - Group 4: **0.3507** | FILTERS, CROP, MARKUP, ADJUST                                     | CORRECT GROUP (SMARTPHONE PHOTO EDITING OPTIONS, Level 2)
   - Group 5: **0.3846** | DONUT, BELLY, BEAN, MARKUP                                        | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 6: **0.3337** | FILTERS, CROP, ADJUST, ROLL                                       | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 7: **0.3663** | BELLY, CROP, BEAN, ROLL                                           | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 8: **0.3158** | FILTERS, DONUT, MARKUP, ADJUST                                    | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 9: **0.5151** | DONUT, BELLY, CROP, BEAN                                          | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 10: **0.3859** | CAUSE, GROUNDS, BASIS, ROLL                                       | INCORRECT (Max overlap: 3/4 with PRETEXT) | [Pred Type: SYNONYM_OR_NEAR (55.8%, no-rel 34.1%)]
   - Group 11: **0.3481** | FILTERS, ARGUMENT, MARKUP, ADJUST                                 | INCORRECT (Max overlap: 3/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 12: **0.4344** | DONUT, BELLY, BEAN, HERO                                          | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 13: **0.4122** | HOAGIE, GRINDER, ROLL, SUB                                        | INCORRECT (Max overlap: 3/4 with LONG SANDWICH) | [Pred Type: SYNONYM_OR_NEAR (52.7%, no-rel 18.6%)]
   - Group 14: **0.4308** | GRINDER, HERO, ROLL, SUB                                          | INCORRECT (Max overlap: 3/4 with LONG SANDWICH) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 23.7%)]
   - Group 15: **0.4132** | HOAGIE, DONUT, BELLY, BEAN                                        | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 16: **0.4439** | DONUT, BELLY, BEAN, GRINDER                                       | INCORRECT (Max overlap: 3/4 with JELLY ___)
   - Group 17: **0.3948** | HOAGIE, HERO, ROLL, SUB                                           | INCORRECT (Max overlap: 3/4 with LONG SANDWICH) | [Pred Type: SYNONYM_OR_NEAR (55.9%, no-rel 19.4%)]
   - Group 18: **0.4663** | HOAGIE, FILTERS, GRINDER, HERO                                    | INCORRECT (Max overlap: 3/4 with LONG SANDWICH)
   - Group 19: **0.3418** | ARGUMENT, MARKUP, ADJUST, SUB                                     | INCORRECT (Max overlap: 2/4 with SMARTPHONE PHOTO EDITING OPTIONS)
   - Group 20: **0.5128** | HOAGIE, DONUT, GRINDER, HERO                                      | INCORRECT (Max overlap: 3/4 with LONG SANDWICH)

---

## Puzzle 93 (ID: 480)
**Words on Board:** PUNCH, SMITE, STICK, PRUNE, POT, MILK, JUICE, SOCK, SODA, WATER, BOOKEND, FERTILIZE, SKI, PANT, EARBUD, BLOUSE

### Ground Truth Categories:
* **Level 0 (BEVERAGES) [Type: SEMANTIC_SET]:** JUICE, MILK, PUNCH, SODA
* **Level 1 (CARE FOR A PLANT) [Type: SEMANTIC_SET]:** FERTILIZE, POT, PRUNE, WATER
* **Level 2 (ITEM SOLD IN PAIRS) [Type: SEMANTIC_SET]:** BOOKEND, EARBUD, SKI, SOCK
* **Level 3 (BUGS PLUS STARTING LETTER) [Type: WORDPLAY_TRANSFORM]:** BLOUSE, PANT, SMITE, STICK

### Top Candidate Partitions:
1. **Partition Score: 0.4002**
   - Group 1: **0.4507** | PUNCH, SMITE, JUICE, SOCK                                         | INCORRECT (Max overlap: 2/4 with BEVERAGES)
   - Group 2: **0.4485** | BOOKEND, FERTILIZE, EARBUD, BLOUSE                                | INCORRECT (Max overlap: 2/4 with ITEM SOLD IN PAIRS)
   - Group 3: **0.4058** | POT, MILK, SODA, WATER                                            | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)
   - Group 4: **0.3733** | STICK, PRUNE, SKI, PANT                                           | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
2. **Partition Score: 0.3980**
   - Group 1: **0.4507** | PUNCH, SMITE, JUICE, SOCK                                         | INCORRECT (Max overlap: 2/4 with BEVERAGES)
   - Group 2: **0.4058** | POT, MILK, SODA, WATER                                            | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)
   - Group 3: **0.4056** | STICK, PRUNE, FERTILIZE, PANT                                     | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 4: **0.3903** | BOOKEND, SKI, EARBUD, BLOUSE                                      | INCORRECT (Max overlap: 3/4 with ITEM SOLD IN PAIRS)
3. **Partition Score: 0.3969**
   - Group 1: **0.4109** | SMITE, PRUNE, FERTILIZE, PANT                                     | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 2: **0.4058** | POT, MILK, SODA, WATER                                            | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)
   - Group 3: **0.4013** | PUNCH, STICK, JUICE, SOCK                                         | INCORRECT (Max overlap: 2/4 with BEVERAGES)
   - Group 4: **0.3903** | BOOKEND, SKI, EARBUD, BLOUSE                                      | INCORRECT (Max overlap: 3/4 with ITEM SOLD IN PAIRS)
4. **Partition Score: 0.3961**
   - Group 1: **0.4507** | PUNCH, SMITE, JUICE, SOCK                                         | INCORRECT (Max overlap: 2/4 with BEVERAGES)
   - Group 2: **0.4058** | POT, MILK, SODA, WATER                                            | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)
   - Group 3: **0.4041** | FERTILIZE, PANT, EARBUD, BLOUSE                                   | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 4: **0.3872** | STICK, PRUNE, BOOKEND, SKI                                        | INCORRECT (Max overlap: 2/4 with ITEM SOLD IN PAIRS)
5. **Partition Score: 0.3931**
   - Group 1: **0.4394** | MILK, JUICE, SODA, WATER                                          | INCORRECT (Max overlap: 3/4 with BEVERAGES)
   - Group 2: **0.4099** | STICK, POT, SOCK, PANT                                            | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 3: **0.3903** | BOOKEND, SKI, EARBUD, BLOUSE                                      | INCORRECT (Max overlap: 3/4 with ITEM SOLD IN PAIRS)
   - Group 4: **0.3860** | PUNCH, SMITE, PRUNE, FERTILIZE                                    | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)

### Top Candidate Groups:
   - Group 1: **0.4507** | PUNCH, SMITE, JUICE, SOCK                                         | INCORRECT (Max overlap: 2/4 with BEVERAGES)
   - Group 2: **0.4485** | BOOKEND, FERTILIZE, EARBUD, BLOUSE                                | INCORRECT (Max overlap: 2/4 with ITEM SOLD IN PAIRS)
   - Group 3: **0.4058** | POT, MILK, SODA, WATER                                            | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)
   - Group 4: **0.3733** | STICK, PRUNE, SKI, PANT                                           | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 5: **0.4056** | STICK, PRUNE, FERTILIZE, PANT                                     | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 6: **0.3903** | BOOKEND, SKI, EARBUD, BLOUSE                                      | INCORRECT (Max overlap: 3/4 with ITEM SOLD IN PAIRS)
   - Group 7: **0.4109** | SMITE, PRUNE, FERTILIZE, PANT                                     | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 8: **0.4013** | PUNCH, STICK, JUICE, SOCK                                         | INCORRECT (Max overlap: 2/4 with BEVERAGES)
   - Group 9: **0.4041** | FERTILIZE, PANT, EARBUD, BLOUSE                                   | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 10: **0.3872** | STICK, PRUNE, BOOKEND, SKI                                        | INCORRECT (Max overlap: 2/4 with ITEM SOLD IN PAIRS)
   - Group 11: **0.4394** | MILK, JUICE, SODA, WATER                                          | INCORRECT (Max overlap: 3/4 with BEVERAGES)
   - Group 12: **0.4099** | STICK, POT, SOCK, PANT                                            | INCORRECT (Max overlap: 2/4 with BUGS PLUS STARTING LETTER)
   - Group 13: **0.3860** | PUNCH, SMITE, PRUNE, FERTILIZE                                    | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)
   - Group 14: **0.4892** | PUNCH, SMITE, PRUNE, SOCK                                         | INCORRECT (Max overlap: 1/4 with BEVERAGES)
   - Group 15: **0.4135** | POT, MILK, JUICE, WATER                                           | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)
   - Group 16: **0.4061** | STICK, BOOKEND, PANT, BLOUSE                                      | INCORRECT (Max overlap: 3/4 with BUGS PLUS STARTING LETTER)
   - Group 17: **0.3761** | SODA, FERTILIZE, SKI, EARBUD                                      | INCORRECT (Max overlap: 2/4 with ITEM SOLD IN PAIRS)
   - Group 18: **0.4528** | BOOKEND, PANT, EARBUD, BLOUSE                                     | INCORRECT (Max overlap: 2/4 with ITEM SOLD IN PAIRS)
   - Group 19: **0.3576** | STICK, PRUNE, FERTILIZE, SKI                                      | INCORRECT (Max overlap: 2/4 with CARE FOR A PLANT)
   - Group 20: **0.4562** | PUNCH, SMITE, MILK, SOCK                                          | INCORRECT (Max overlap: 2/4 with BEVERAGES)

---

## Puzzle 94 (ID: 976)
**Words on Board:** LESSON, COLORS, KENT, RESEED, SHEER, STARK, FLAG, STANDARD, CAMEL, BANNER, PURE, SYNC, UTTER, WAYNE, SALEM, PARLIAMENT

### Ground Truth Categories:
* **Level 0 (DOWNRIGHT) [Type: SYNONYM_OR_NEAR]:** PURE, SHEER, STARK, UTTER
* **Level 1 (PENNANT) [Type: SYNONYM_OR_NEAR]:** BANNER, COLORS, FLAG, STANDARD
* **Level 2 (CIGARETTE BRANDS) [Type: NAMED_ENTITY_SET]:** CAMEL, KENT, PARLIAMENT, SALEM
* **Level 3 (HOMOPHONES OF WAYS TO GET SMALLER) [Type: SOUND_OR_SPELLING]:** LESSON, RESEED, SYNC, WAYNE

### Top Candidate Partitions:
1. **Partition Score: 0.5337**
   - Group 1: **0.8106** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.2%, no-rel 30.7%)]
   - Group 2: **0.7561** | SHEER, STARK, PURE, UTTER                                         | CORRECT GROUP (DOWNRIGHT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 34.4%)]
   - Group 3: **0.6477** | KENT, WAYNE, SALEM, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 4: **0.3655** | LESSON, RESEED, CAMEL, SYNC                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
2. **Partition Score: 0.4923**
   - Group 1: **0.8106** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.2%, no-rel 30.7%)]
   - Group 2: **0.6477** | KENT, WAYNE, SALEM, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 3: **0.5274** | RESEED, SHEER, PURE, UTTER                                        | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 37.0%)]
   - Group 4: **0.3971** | LESSON, STARK, CAMEL, SYNC                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
3. **Partition Score: 0.4792**
   - Group 1: **0.8106** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.2%, no-rel 30.7%)]
   - Group 2: **0.6728** | KENT, CAMEL, WAYNE, SALEM                                         | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 3: **0.5274** | RESEED, SHEER, PURE, UTTER                                        | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 37.0%)]
   - Group 4: **0.3582** | LESSON, STARK, SYNC, PARLIAMENT                                   | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
4. **Partition Score: 0.4677**
   - Group 1: **0.6477** | KENT, WAYNE, SALEM, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 2: **0.6289** | SHEER, STANDARD, PURE, UTTER                                      | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 36.1%)]
   - Group 3: **0.4477** | COLORS, RESEED, FLAG, BANNER                                      | INCORRECT (Max overlap: 3/4 with PENNANT)
   - Group 4: **0.3971** | LESSON, STARK, CAMEL, SYNC                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
5. **Partition Score: 0.4646**
   - Group 1: **0.8106** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.2%, no-rel 30.7%)]
   - Group 2: **0.6477** | KENT, WAYNE, SALEM, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 3: **0.4785** | RESEED, SHEER, STARK, PURE                                        | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (58.1%, no-rel 32.3%)]
   - Group 4: **0.3661** | LESSON, CAMEL, SYNC, UTTER                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)

### Top Candidate Groups:
   - Group 1: **0.8106** | COLORS, FLAG, STANDARD, BANNER                                    | CORRECT GROUP (PENNANT, Level 1) | [Pred Type: SYNONYM_OR_NEAR (59.2%, no-rel 30.7%)]
   - Group 2: **0.7561** | SHEER, STARK, PURE, UTTER                                         | CORRECT GROUP (DOWNRIGHT, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.2%, no-rel 34.4%)]
   - Group 3: **0.6477** | KENT, WAYNE, SALEM, PARLIAMENT                                    | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 4: **0.3655** | LESSON, RESEED, CAMEL, SYNC                                       | INCORRECT (Max overlap: 3/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 5: **0.5274** | RESEED, SHEER, PURE, UTTER                                        | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 37.0%)]
   - Group 6: **0.3971** | LESSON, STARK, CAMEL, SYNC                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 7: **0.6728** | KENT, CAMEL, WAYNE, SALEM                                         | INCORRECT (Max overlap: 3/4 with CIGARETTE BRANDS)
   - Group 8: **0.3582** | LESSON, STARK, SYNC, PARLIAMENT                                   | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 9: **0.6289** | SHEER, STANDARD, PURE, UTTER                                      | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 36.1%)]
   - Group 10: **0.4477** | COLORS, RESEED, FLAG, BANNER                                      | INCORRECT (Max overlap: 3/4 with PENNANT)
   - Group 11: **0.4785** | RESEED, SHEER, STARK, PURE                                        | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (58.1%, no-rel 32.3%)]
   - Group 12: **0.3661** | LESSON, CAMEL, SYNC, UTTER                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 13: **0.4596** | LESSON, SHEER, PURE, UTTER                                        | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (50.1%, no-rel 35.4%)]
   - Group 14: **0.3699** | RESEED, STARK, CAMEL, SYNC                                        | INCORRECT (Max overlap: 2/4 with HOMOPHONES OF WAYS TO GET SMALLER)
   - Group 15: **0.5669** | COLORS, SHEER, PURE, UTTER                                        | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (53.9%, no-rel 36.4%)]
   - Group 16: **0.4804** | RESEED, FLAG, STANDARD, BANNER                                    | INCORRECT (Max overlap: 3/4 with PENNANT) | [Pred Type: SYNONYM_OR_NEAR (56.0%, no-rel 32.5%)]
   - Group 17: **0.4456** | COLORS, STARK, FLAG, BANNER                                       | INCORRECT (Max overlap: 3/4 with PENNANT) | [Pred Type: SYNONYM_OR_NEAR (45.2%, no-rel 31.5%)]
   - Group 18: **0.4355** | LESSON, COLORS, FLAG, BANNER                                      | INCORRECT (Max overlap: 3/4 with PENNANT)
   - Group 19: **0.5529** | COLORS, STARK, PURE, UTTER                                        | INCORRECT (Max overlap: 3/4 with DOWNRIGHT) | [Pred Type: SYNONYM_OR_NEAR (49.1%, no-rel 36.3%)]
   - Group 20: **0.5172** | SHEER, FLAG, STANDARD, BANNER                                     | INCORRECT (Max overlap: 3/4 with PENNANT) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 29.6%)]

---

## Puzzle 95 (ID: 391)
**Words on Board:** CELL, JUG, BOTTLE, MOBILE, FREEZE, CRIB, ATOM, RATTLE, SAW, PHONE, DOG, PROTEIN, SPOONS, WASHBOARD, MOLECULE, PRICE

### Ground Truth Categories:
* **Level 0 (BIOLOGICAL BUILDING BLOCKS) [Type: SEMANTIC_SET]:** ATOM, CELL, MOLECULE, PROTEIN
* **Level 1 (PURCHASES FOR A BABY) [Type: SEMANTIC_SET]:** BOTTLE, CRIB, MOBILE, RATTLE
* **Level 2 (OBJECTS PLAYED AS INSTRUMENTS) [Type: SEMANTIC_SET]:** JUG, SAW, SPOONS, WASHBOARD
* **Level 3 (___ TAG) [Type: FILL_IN_THE_BLANK]:** DOG, FREEZE, PHONE, PRICE

### Top Candidate Partitions:
1. **Partition Score: 0.3944**
   - Group 1: **0.4205** | FREEZE, CRIB, RATTLE, PHONE                                       | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 2: **0.4007** | SAW, DOG, PROTEIN, PRICE                                          | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 3: **0.3968** | CELL, MOBILE, ATOM, MOLECULE                                      | INCORRECT (Max overlap: 3/4 with BIOLOGICAL BUILDING BLOCKS) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 27.1%)]
   - Group 4: **0.3901** | JUG, BOTTLE, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS) | [Pred Type: SEMANTIC_SET (69.2%, no-rel 17.6%)]
2. **Partition Score: 0.3943**
   - Group 1: **0.4517** | CRIB, SAW, DOG, WASHBOARD                                         | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 2: **0.4008** | FREEZE, PHONE, PROTEIN, PRICE                                     | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 3: **0.3968** | CELL, MOBILE, ATOM, MOLECULE                                      | INCORRECT (Max overlap: 3/4 with BIOLOGICAL BUILDING BLOCKS) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 27.1%)]
   - Group 4: **0.3898** | JUG, BOTTLE, RATTLE, SPOONS                                       | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS) | [Pred Type: SEMANTIC_SET (45.1%, no-rel 32.0%)]
3. **Partition Score: 0.3940**
   - Group 1: **0.4018** | CRIB, SAW, DOG, PROTEIN                                           | INCORRECT (Max overlap: 1/4 with PURCHASES FOR A BABY)
   - Group 2: **0.3989** | FREEZE, RATTLE, PHONE, PRICE                                      | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 3: **0.3968** | CELL, MOBILE, ATOM, MOLECULE                                      | INCORRECT (Max overlap: 3/4 with BIOLOGICAL BUILDING BLOCKS) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 27.1%)]
   - Group 4: **0.3901** | JUG, BOTTLE, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS) | [Pred Type: SEMANTIC_SET (69.2%, no-rel 17.6%)]
4. **Partition Score: 0.3936**
   - Group 1: **0.4129** | FREEZE, SAW, DOG, PRICE                                           | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 2: **0.3982** | CRIB, PHONE, PROTEIN, WASHBOARD                                   | INCORRECT (Max overlap: 1/4 with PURCHASES FOR A BABY)
   - Group 3: **0.3968** | CELL, MOBILE, ATOM, MOLECULE                                      | INCORRECT (Max overlap: 3/4 with BIOLOGICAL BUILDING BLOCKS) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 27.1%)]
   - Group 4: **0.3898** | JUG, BOTTLE, RATTLE, SPOONS                                       | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS) | [Pred Type: SEMANTIC_SET (45.1%, no-rel 32.0%)]
5. **Partition Score: 0.3927**
   - Group 1: **0.4261** | JUG, BOTTLE, CRIB, SPOONS                                         | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS) | [Pred Type: SEMANTIC_SET (45.1%, no-rel 32.7%)]
   - Group 2: **0.3989** | FREEZE, RATTLE, PHONE, PRICE                                      | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 3: **0.3968** | CELL, MOBILE, ATOM, MOLECULE                                      | INCORRECT (Max overlap: 3/4 with BIOLOGICAL BUILDING BLOCKS) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 27.1%)]
   - Group 4: **0.3875** | SAW, DOG, PROTEIN, WASHBOARD                                      | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)

### Top Candidate Groups:
   - Group 1: **0.4205** | FREEZE, CRIB, RATTLE, PHONE                                       | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 2: **0.4007** | SAW, DOG, PROTEIN, PRICE                                          | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 3: **0.3968** | CELL, MOBILE, ATOM, MOLECULE                                      | INCORRECT (Max overlap: 3/4 with BIOLOGICAL BUILDING BLOCKS) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 27.1%)]
   - Group 4: **0.3901** | JUG, BOTTLE, SPOONS, WASHBOARD                                    | INCORRECT (Max overlap: 3/4 with OBJECTS PLAYED AS INSTRUMENTS) | [Pred Type: SEMANTIC_SET (69.2%, no-rel 17.6%)]
   - Group 5: **0.4517** | CRIB, SAW, DOG, WASHBOARD                                         | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 6: **0.4008** | FREEZE, PHONE, PROTEIN, PRICE                                     | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 7: **0.3898** | JUG, BOTTLE, RATTLE, SPOONS                                       | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS) | [Pred Type: SEMANTIC_SET (45.1%, no-rel 32.0%)]
   - Group 8: **0.4018** | CRIB, SAW, DOG, PROTEIN                                           | INCORRECT (Max overlap: 1/4 with PURCHASES FOR A BABY)
   - Group 9: **0.3989** | FREEZE, RATTLE, PHONE, PRICE                                      | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 10: **0.4129** | FREEZE, SAW, DOG, PRICE                                           | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 11: **0.3982** | CRIB, PHONE, PROTEIN, WASHBOARD                                   | INCORRECT (Max overlap: 1/4 with PURCHASES FOR A BABY)
   - Group 12: **0.4261** | JUG, BOTTLE, CRIB, SPOONS                                         | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS) | [Pred Type: SEMANTIC_SET (45.1%, no-rel 32.7%)]
   - Group 13: **0.3875** | SAW, DOG, PROTEIN, WASHBOARD                                      | INCORRECT (Max overlap: 2/4 with OBJECTS PLAYED AS INSTRUMENTS)
   - Group 14: **0.4269** | FREEZE, CRIB, SAW, DOG                                            | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 15: **0.3914** | RATTLE, PHONE, PROTEIN, PRICE                                     | INCORRECT (Max overlap: 2/4 with ___ TAG)
   - Group 16: **0.4123** | SAW, PHONE, DOG, PRICE                                            | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 17: **0.3899** | FREEZE, CRIB, RATTLE, PROTEIN                                     | INCORRECT (Max overlap: 2/4 with PURCHASES FOR A BABY)
   - Group 18: **0.3885** | CRIB, RATTLE, PHONE, PROTEIN                                      | INCORRECT (Max overlap: 2/4 with PURCHASES FOR A BABY)
   - Group 19: **0.4772** | FREEZE, CRIB, PHONE, PRICE                                        | INCORRECT (Max overlap: 3/4 with ___ TAG)
   - Group 20: **0.4456** | FREEZE, CRIB, SAW, PRICE                                          | INCORRECT (Max overlap: 2/4 with ___ TAG)

---

## Puzzle 96 (ID: 395)
**Words on Board:** SASS, BASS, ATTITUDE, PROSPECT, LIP, BRIDGE, LENS, RIM, FORECAST, TEMPLE, FLUKE, PERCH, OUTLOOK, CHANCE, CHEEK, PIKE

### Ground Truth Categories:
* **Level 0 (FUTURE LIKELIHOOD) [Type: SYNONYM_OR_NEAR]:** CHANCE, FORECAST, OUTLOOK, PROSPECT
* **Level 1 (BACK TALK) [Type: SYNONYM_OR_NEAR]:** ATTITUDE, CHEEK, LIP, SASS
* **Level 2 (FISH) [Type: SEMANTIC_SET]:** BASS, FLUKE, PERCH, PIKE
* **Level 3 (COMPONENTS OF EYEGLASSES) [Type: SEMANTIC_SET]:** BRIDGE, LENS, RIM, TEMPLE

### Top Candidate Partitions:
1. **Partition Score: 0.4145**
   - Group 1: **0.5536** | SASS, ATTITUDE, LIP, CHEEK                                        | CORRECT GROUP (BACK TALK, Level 1) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 28.4%)]
   - Group 2: **0.5303** | PROSPECT, FLUKE, OUTLOOK, CHANCE                                  | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (68.3%, no-rel 25.6%)]
   - Group 3: **0.4606** | BRIDGE, LENS, RIM, TEMPLE                                         | CORRECT GROUP (COMPONENTS OF EYEGLASSES, Level 3)
   - Group 4: **0.3336** | BASS, FORECAST, PERCH, PIKE                                       | INCORRECT (Max overlap: 3/4 with FISH)
2. **Partition Score: 0.4103**
   - Group 1: **0.6798** | BASS, BRIDGE, PERCH, PIKE                                         | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 2: **0.5836** | ATTITUDE, PROSPECT, FORECAST, OUTLOOK                             | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (54.5%, no-rel 36.6%)]
   - Group 3: **0.4318** | SASS, LIP, FLUKE, CHANCE                                          | INCORRECT (Max overlap: 2/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 28.0%)]
   - Group 4: **0.3129** | LENS, RIM, TEMPLE, CHEEK                                          | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES) | [Pred Type: SEMANTIC_SET (45.1%, no-rel 23.7%)]
3. **Partition Score: 0.4044**
   - Group 1: **0.5762** | ATTITUDE, PROSPECT, OUTLOOK, CHANCE                               | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (67.2%, no-rel 27.7%)]
   - Group 2: **0.4896** | SASS, LIP, FLUKE, CHEEK                                           | INCORRECT (Max overlap: 3/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (67.0%, no-rel 24.3%)]
   - Group 3: **0.4606** | BRIDGE, LENS, RIM, TEMPLE                                         | CORRECT GROUP (COMPONENTS OF EYEGLASSES, Level 3)
   - Group 4: **0.3336** | BASS, FORECAST, PERCH, PIKE                                       | INCORRECT (Max overlap: 3/4 with FISH)
4. **Partition Score: 0.3980**
   - Group 1: **0.4858** | ATTITUDE, PROSPECT, FLUKE, OUTLOOK                                | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 38.7%)]
   - Group 2: **0.4643** | SASS, LIP, CHANCE, CHEEK                                          | INCORRECT (Max overlap: 3/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (66.4%, no-rel 26.0%)]
   - Group 3: **0.4606** | BRIDGE, LENS, RIM, TEMPLE                                         | CORRECT GROUP (COMPONENTS OF EYEGLASSES, Level 3)
   - Group 4: **0.3336** | BASS, FORECAST, PERCH, PIKE                                       | INCORRECT (Max overlap: 3/4 with FISH)
5. **Partition Score: 0.3920**
   - Group 1: **0.4606** | BRIDGE, LENS, RIM, TEMPLE                                         | CORRECT GROUP (COMPONENTS OF EYEGLASSES, Level 3)
   - Group 2: **0.4595** | ATTITUDE, FLUKE, OUTLOOK, CHANCE                                  | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 36.0%)]
   - Group 3: **0.4411** | SASS, PROSPECT, LIP, CHEEK                                        | INCORRECT (Max overlap: 3/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 26.8%)]
   - Group 4: **0.3336** | BASS, FORECAST, PERCH, PIKE                                       | INCORRECT (Max overlap: 3/4 with FISH)

### Top Candidate Groups:
   - Group 1: **0.5536** | SASS, ATTITUDE, LIP, CHEEK                                        | CORRECT GROUP (BACK TALK, Level 1) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 28.4%)]
   - Group 2: **0.5303** | PROSPECT, FLUKE, OUTLOOK, CHANCE                                  | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (68.3%, no-rel 25.6%)]
   - Group 3: **0.4606** | BRIDGE, LENS, RIM, TEMPLE                                         | CORRECT GROUP (COMPONENTS OF EYEGLASSES, Level 3)
   - Group 4: **0.3336** | BASS, FORECAST, PERCH, PIKE                                       | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 5: **0.6798** | BASS, BRIDGE, PERCH, PIKE                                         | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 6: **0.5836** | ATTITUDE, PROSPECT, FORECAST, OUTLOOK                             | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (54.5%, no-rel 36.6%)]
   - Group 7: **0.4318** | SASS, LIP, FLUKE, CHANCE                                          | INCORRECT (Max overlap: 2/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 28.0%)]
   - Group 8: **0.3129** | LENS, RIM, TEMPLE, CHEEK                                          | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES) | [Pred Type: SEMANTIC_SET (45.1%, no-rel 23.7%)]
   - Group 9: **0.5762** | ATTITUDE, PROSPECT, OUTLOOK, CHANCE                               | INCORRECT (Max overlap: 3/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (67.2%, no-rel 27.7%)]
   - Group 10: **0.4896** | SASS, LIP, FLUKE, CHEEK                                           | INCORRECT (Max overlap: 3/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (67.0%, no-rel 24.3%)]
   - Group 11: **0.4858** | ATTITUDE, PROSPECT, FLUKE, OUTLOOK                                | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (51.0%, no-rel 38.7%)]
   - Group 12: **0.4643** | SASS, LIP, CHANCE, CHEEK                                          | INCORRECT (Max overlap: 3/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (66.4%, no-rel 26.0%)]
   - Group 13: **0.4595** | ATTITUDE, FLUKE, OUTLOOK, CHANCE                                  | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (51.8%, no-rel 36.0%)]
   - Group 14: **0.4411** | SASS, PROSPECT, LIP, CHEEK                                        | INCORRECT (Max overlap: 3/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (64.4%, no-rel 26.8%)]
   - Group 15: **0.4795** | ATTITUDE, PROSPECT, OUTLOOK, CHEEK                                | INCORRECT (Max overlap: 2/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (57.3%, no-rel 33.2%)]
   - Group 16: **0.4338** | BASS, RIM, PERCH, PIKE                                            | INCORRECT (Max overlap: 3/4 with FISH)
   - Group 17: **0.2972** | BRIDGE, LENS, FORECAST, TEMPLE                                    | INCORRECT (Max overlap: 3/4 with COMPONENTS OF EYEGLASSES)
   - Group 18: **0.4850** | SASS, FLUKE, CHANCE, CHEEK                                        | INCORRECT (Max overlap: 2/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (48.7%, no-rel 34.7%)]
   - Group 19: **0.4306** | ATTITUDE, PROSPECT, LIP, OUTLOOK                                  | INCORRECT (Max overlap: 2/4 with BACK TALK) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 35.1%)]
   - Group 20: **0.5329** | ATTITUDE, PROSPECT, FLUKE, CHANCE                                 | INCORRECT (Max overlap: 2/4 with FUTURE LIKELIHOOD) | [Pred Type: SYNONYM_OR_NEAR (58.7%, no-rel 35.1%)]

---

## Puzzle 97 (ID: 1026)
**Words on Board:** HOLES, HOEDOWN, MALLET, WICKET, HOP, MOLE, CONCERN, OLIVES, CAROUSER, RAVE, EVITE, TIMER, SHARE, CLAIM, STAKE, BALL

### Ground Truth Categories:
* **Level 0 (EVENTS WITH DANCING) [Type: SEMANTIC_SET]:** BALL, HOEDOWN, HOP, RAVE
* **Level 1 (INTEREST) [Type: SYNONYM_OR_NEAR]:** CLAIM, CONCERN, SHARE, STAKE
* **Level 2 (COMPONENTS OF WHAC-A-MOLE) [Type: SEMANTIC_SET]:** HOLES, MALLET, MOLE, TIMER
* **Level 3 (MUSICALS WITH LAST LETTER CHANGED) [Type: WORDPLAY_TRANSFORM]:** CAROUSER, EVITE, OLIVES, WICKET

### Top Candidate Partitions:
1. **Partition Score: 0.4524**
   - Group 1: **0.5592** | HOEDOWN, CAROUSER, EVITE, TIMER                                   | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 2: **0.5513** | CONCERN, SHARE, CLAIM, STAKE                                      | CORRECT GROUP (INTEREST, Level 1)
   - Group 3: **0.4400** | HOLES, MALLET, MOLE, OLIVES                                       | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE) | [Pred Type: SEMANTIC_SET (48.3%, no-rel 20.6%)]
   - Group 4: **0.4092** | WICKET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 22.3%)]
2. **Partition Score: 0.4286**
   - Group 1: **0.5592** | HOEDOWN, CAROUSER, EVITE, TIMER                                   | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 2: **0.5513** | CONCERN, SHARE, CLAIM, STAKE                                      | CORRECT GROUP (INTEREST, Level 1)
   - Group 3: **0.4075** | HOLES, WICKET, MOLE, OLIVES                                       | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE) | [Pred Type: SEMANTIC_SET (53.3%, no-rel 21.0%)]
   - Group 4: **0.3779** | MALLET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING)
3. **Partition Score: 0.4213**
   - Group 1: **0.5513** | CONCERN, SHARE, CLAIM, STAKE                                      | CORRECT GROUP (INTEREST, Level 1)
   - Group 2: **0.5015** | MALLET, CAROUSER, EVITE, TIMER                                    | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 3: **0.4092** | WICKET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 22.3%)]
   - Group 4: **0.3872** | HOLES, HOEDOWN, MOLE, OLIVES                                      | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
4. **Partition Score: 0.4208**
   - Group 1: **0.5879** | HOEDOWN, MALLET, CAROUSER, EVITE                                  | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 2: **0.5513** | CONCERN, SHARE, CLAIM, STAKE                                      | CORRECT GROUP (INTEREST, Level 1)
   - Group 3: **0.4092** | WICKET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 22.3%)]
   - Group 4: **0.3613** | HOLES, MOLE, OLIVES, TIMER                                        | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE)
5. **Partition Score: 0.4179**
   - Group 1: **0.5513** | CONCERN, SHARE, CLAIM, STAKE                                      | CORRECT GROUP (INTEREST, Level 1)
   - Group 2: **0.5231** | OLIVES, CAROUSER, EVITE, TIMER                                    | INCORRECT (Max overlap: 3/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 3: **0.4092** | WICKET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 22.3%)]
   - Group 4: **0.3697** | HOLES, HOEDOWN, MALLET, MOLE                                      | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE)

### Top Candidate Groups:
   - Group 1: **0.5592** | HOEDOWN, CAROUSER, EVITE, TIMER                                   | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 2: **0.5513** | CONCERN, SHARE, CLAIM, STAKE                                      | CORRECT GROUP (INTEREST, Level 1)
   - Group 3: **0.4400** | HOLES, MALLET, MOLE, OLIVES                                       | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE) | [Pred Type: SEMANTIC_SET (48.3%, no-rel 20.6%)]
   - Group 4: **0.4092** | WICKET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING) | [Pred Type: SEMANTIC_SET (46.8%, no-rel 22.3%)]
   - Group 5: **0.4075** | HOLES, WICKET, MOLE, OLIVES                                       | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE) | [Pred Type: SEMANTIC_SET (53.3%, no-rel 21.0%)]
   - Group 6: **0.3779** | MALLET, HOP, RAVE, BALL                                           | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING)
   - Group 7: **0.5015** | MALLET, CAROUSER, EVITE, TIMER                                    | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 8: **0.3872** | HOLES, HOEDOWN, MOLE, OLIVES                                      | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 9: **0.5879** | HOEDOWN, MALLET, CAROUSER, EVITE                                  | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 10: **0.3613** | HOLES, MOLE, OLIVES, TIMER                                        | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 11: **0.5231** | OLIVES, CAROUSER, EVITE, TIMER                                    | INCORRECT (Max overlap: 3/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 12: **0.3697** | HOLES, HOEDOWN, MALLET, MOLE                                      | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 13: **0.6178** | HOEDOWN, OLIVES, CAROUSER, EVITE                                  | INCORRECT (Max overlap: 3/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 14: **0.4326** | HOLES, MALLET, WICKET, MOLE                                       | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE) | [Pred Type: SEMANTIC_SET (54.3%, no-rel 21.4%)]
   - Group 15: **0.3353** | HOP, RAVE, TIMER, BALL                                            | INCORRECT (Max overlap: 3/4 with EVENTS WITH DANCING)
   - Group 16: **0.5146** | HOEDOWN, MOLE, CAROUSER, EVITE                                    | INCORRECT (Max overlap: 2/4 with MUSICALS WITH LAST LETTER CHANGED)
   - Group 17: **0.3649** | HOLES, MALLET, OLIVES, TIMER                                      | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE)
   - Group 18: **0.3601** | HOLES, WICKET, MOLE, TIMER                                        | INCORRECT (Max overlap: 3/4 with COMPONENTS OF WHAC-A-MOLE) | [Pred Type: SEMANTIC_SET (45.1%, no-rel 22.6%)]
   - Group 19: **0.3434** | HOLES, MALLET, MOLE, TIMER                                        | CORRECT GROUP (COMPONENTS OF WHAC-A-MOLE, Level 2)
   - Group 20: **0.4461** | HOEDOWN, MALLET, EVITE, TIMER                                     | INCORRECT (Max overlap: 2/4 with COMPONENTS OF WHAC-A-MOLE)

---

## Puzzle 98 (ID: 611)
**Words on Board:** JACK, KNEE, BOLSTER, TUG, NIGHT, BUB, HUB, YANK, MAN, JERK, BLOCK, BUD, MAD, WRENCH, MAT, STRAP

### Ground Truth Categories:
* **Level 0 (WREST) [Type: SYNONYM_OR_NEAR]:** JERK, TUG, WRENCH, YANK
* **Level 1 (BUSTER) [Type: FILL_IN_THE_BLANK]:** BUB, BUD, JACK, MAN
* **Level 2 (YOGA ACCESSORIES) [Type: SEMANTIC_SET]:** BLOCK, BOLSTER, MAT, STRAP
* **Level 3 (___CAP) [Type: FILL_IN_THE_BLANK]:** HUB, KNEE, MAD, NIGHT

### Top Candidate Partitions:
1. **Partition Score: 0.4735**
   - Group 1: **0.5611** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 32.1%)]
   - Group 2: **0.4802** | JACK, NIGHT, HUB, MAN                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.4757** | KNEE, BLOCK, MAT, STRAP                                           | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 30.0%)]
   - Group 4: **0.4691** | BOLSTER, BUB, BUD, MAD                                            | INCORRECT (Max overlap: 2/4 with BUSTER)
2. **Partition Score: 0.4576**
   - Group 1: **0.5680** | BOLSTER, TUG, YANK, JERK                                          | INCORRECT (Max overlap: 3/4 with WREST) | [Pred Type: SYNONYM_OR_NEAR (64.2%, no-rel 28.5%)]
   - Group 2: **0.5520** | BUB, HUB, BUD, MAD                                                | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.4376** | BLOCK, WRENCH, MAT, STRAP                                         | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)
   - Group 4: **0.4203** | JACK, KNEE, NIGHT, MAN                                            | INCORRECT (Max overlap: 2/4 with BUSTER)
3. **Partition Score: 0.4566**
   - Group 1: **0.5611** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 32.1%)]
   - Group 2: **0.4866** | NIGHT, HUB, MAN, MAD                                              | INCORRECT (Max overlap: 3/4 with ___CAP)
   - Group 3: **0.4555** | BOLSTER, BUB, BLOCK, BUD                                          | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 4: **0.4421** | JACK, KNEE, MAT, STRAP                                            | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES) | [Pred Type: SEMANTIC_SET (46.2%, no-rel 28.3%)]
4. **Partition Score: 0.4557**
   - Group 1: **0.5611** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 32.1%)]
   - Group 2: **0.5520** | BUB, HUB, BUD, MAD                                                | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.4301** | BOLSTER, BLOCK, MAT, STRAP                                        | CORRECT GROUP (YOGA ACCESSORIES, Level 2)
   - Group 4: **0.4203** | JACK, KNEE, NIGHT, MAN                                            | INCORRECT (Max overlap: 2/4 with BUSTER)
5. **Partition Score: 0.4480**
   - Group 1: **0.5611** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 32.1%)]
   - Group 2: **0.4802** | JACK, NIGHT, HUB, MAN                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.4479** | KNEE, BOLSTER, BLOCK, STRAP                                       | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)
   - Group 4: **0.4319** | BUB, BUD, MAD, MAT                                                | INCORRECT (Max overlap: 2/4 with BUSTER)

### Top Candidate Groups:
   - Group 1: **0.5611** | TUG, YANK, JERK, WRENCH                                           | CORRECT GROUP (WREST, Level 0) | [Pred Type: SYNONYM_OR_NEAR (57.6%, no-rel 32.1%)]
   - Group 2: **0.4802** | JACK, NIGHT, HUB, MAN                                             | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 3: **0.4757** | KNEE, BLOCK, MAT, STRAP                                           | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES) | [Pred Type: SEMANTIC_SET (48.0%, no-rel 30.0%)]
   - Group 4: **0.4691** | BOLSTER, BUB, BUD, MAD                                            | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 5: **0.5680** | BOLSTER, TUG, YANK, JERK                                          | INCORRECT (Max overlap: 3/4 with WREST) | [Pred Type: SYNONYM_OR_NEAR (64.2%, no-rel 28.5%)]
   - Group 6: **0.5520** | BUB, HUB, BUD, MAD                                                | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 7: **0.4376** | BLOCK, WRENCH, MAT, STRAP                                         | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)
   - Group 8: **0.4203** | JACK, KNEE, NIGHT, MAN                                            | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 9: **0.4866** | NIGHT, HUB, MAN, MAD                                              | INCORRECT (Max overlap: 3/4 with ___CAP)
   - Group 10: **0.4555** | BOLSTER, BUB, BLOCK, BUD                                          | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES)
   - Group 11: **0.4421** | JACK, KNEE, MAT, STRAP                                            | INCORRECT (Max overlap: 2/4 with YOGA ACCESSORIES) | [Pred Type: SEMANTIC_SET (46.2%, no-rel 28.3%)]
   - Group 12: **0.4301** | BOLSTER, BLOCK, MAT, STRAP                                        | CORRECT GROUP (YOGA ACCESSORIES, Level 2)
   - Group 13: **0.4479** | KNEE, BOLSTER, BLOCK, STRAP                                       | INCORRECT (Max overlap: 3/4 with YOGA ACCESSORIES)
   - Group 14: **0.4319** | BUB, BUD, MAD, MAT                                                | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 15: **0.5083** | BUB, MAN, BUD, MAD                                                | INCORRECT (Max overlap: 3/4 with BUSTER)
   - Group 16: **0.4206** | JACK, KNEE, NIGHT, HUB                                            | INCORRECT (Max overlap: 3/4 with ___CAP)
   - Group 17: **0.4253** | KNEE, MAD, MAT, STRAP                                             | INCORRECT (Max overlap: 2/4 with ___CAP)
   - Group 18: **0.5036** | JACK, NIGHT, MAN, MAD                                             | INCORRECT (Max overlap: 2/4 with BUSTER) | [Pred Type: FILL_IN_THE_BLANK (48.4%, no-rel 33.0%)]
   - Group 19: **0.4017** | BOLSTER, BUB, HUB, BUD                                            | INCORRECT (Max overlap: 2/4 with BUSTER)
   - Group 20: **0.4586** | BUB, HUB, MAN, BUD                                                | INCORRECT (Max overlap: 3/4 with BUSTER)

---

## Puzzle 99 (ID: 433)
**Words on Board:** TONGUE, PRAIRIE, SPEECH, COTTAGE, TAPE, BANDAGE, RANCH, FRENCH, KISS, DRESSING, CRAFTSMAN, DIALECT, LANGUAGE, NECK, SCISSORS, MAKE OUT

### Ground Truth Categories:
* **Level 0 (SPOKEN COMMUNICATION) [Type: SEMANTIC_SET]:** DIALECT, LANGUAGE, SPEECH, TONGUE
* **Level 1 (CANOODLE) [Type: SYNONYM_OR_NEAR]:** FRENCH, KISS, MAKE OUT, NECK
* **Level 2 (FIRST AID KIT ITEMS) [Type: SEMANTIC_SET]:** BANDAGE, DRESSING, SCISSORS, TAPE
* **Level 3 (HOUSE STYLES) [Type: SEMANTIC_SET]:** COTTAGE, CRAFTSMAN, PRAIRIE, RANCH

### Top Candidate Partitions:
_No complete four-group partitions were found from the bounded search; showing top individual candidate groups instead._

### Top Candidate Groups:
   - Group 1: **0.8265** | TONGUE, SPEECH, DIALECT, LANGUAGE                                 | CORRECT GROUP (SPOKEN COMMUNICATION, Level 0)
   - Group 2: **0.7682** | TONGUE, FRENCH, DIALECT, LANGUAGE                                 | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 3: **0.7330** | SPEECH, FRENCH, DIALECT, LANGUAGE                                 | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 4: **0.7100** | TONGUE, FRENCH, KISS, NECK                                        | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 5: **0.7066** | TONGUE, SPEECH, FRENCH, LANGUAGE                                  | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 6: **0.6664** | TONGUE, SPEECH, FRENCH, DIALECT                                   | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 7: **0.6654** | TONGUE, FRENCH, DIALECT, NECK                                     | INCORRECT (Max overlap: 2/4 with SPOKEN COMMUNICATION)
   - Group 8: **0.6512** | FRENCH, KISS, NECK, MAKE OUT                                      | CORRECT GROUP (CANOODLE, Level 1)
   - Group 9: **0.6459** | TONGUE, FRENCH, KISS, LANGUAGE                                    | INCORRECT (Max overlap: 2/4 with SPOKEN COMMUNICATION)
   - Group 10: **0.6427** | TONGUE, KISS, NECK, MAKE OUT                                      | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 11: **0.6372** | TONGUE, FRENCH, LANGUAGE, NECK                                    | INCORRECT (Max overlap: 2/4 with SPOKEN COMMUNICATION)
   - Group 12: **0.6169** | TONGUE, DIALECT, LANGUAGE, NECK                                   | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 13: **0.6142** | TONGUE, SPEECH, KISS, LANGUAGE                                    | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION) | [Pred Type: SYNONYM_OR_NEAR (47.9%, no-rel 37.1%)]
   - Group 14: **0.6081** | FRENCH, DIALECT, LANGUAGE, NECK                                   | INCORRECT (Max overlap: 2/4 with CANOODLE)
   - Group 15: **0.6035** | FRENCH, DIALECT, LANGUAGE, MAKE OUT                               | INCORRECT (Max overlap: 2/4 with CANOODLE)
   - Group 16: **0.5935** | FRENCH, DIALECT, NECK, MAKE OUT                                   | INCORRECT (Max overlap: 3/4 with CANOODLE)
   - Group 17: **0.5934** | TONGUE, KISS, DIALECT, LANGUAGE                                   | INCORRECT (Max overlap: 3/4 with SPOKEN COMMUNICATION)
   - Group 18: **0.5899** | TONGUE, FRENCH, KISS, DIALECT                                     | INCORRECT (Max overlap: 2/4 with SPOKEN COMMUNICATION)
   - Group 19: **0.5881** | TONGUE, KISS, DIALECT, NECK                                       | INCORRECT (Max overlap: 2/4 with SPOKEN COMMUNICATION)
   - Group 20: **0.5869** | PRAIRIE, COTTAGE, RANCH, CRAFTSMAN                                | CORRECT GROUP (HOUSE STYLES, Level 3)

---

## Puzzle 100 (ID: 1073)
**Words on Board:** HERB, STRIKE, SHED, MARCH, ITSY, RALLY, STABLE, HISS, DRUM, PEN, MYA, MASK, PICKET, COOP, STAFF, RATTLE

### Ground Truth Categories:
* **Level 0 (FARM FIXTURES) [Type: SEMANTIC_SET]:** COOP, PEN, SHED, STABLE
* **Level 1 (LABOR PROTEST ACTIONS) [Type: SEMANTIC_SET]:** MARCH, PICKET, RALLY, STRIKE
* **Level 2 (OBJECTS USED IN RITUAL PERFORMANCES) [Type: SEMANTIC_SET]:** DRUM, MASK, RATTLE, STAFF
* **Level 3 (POSSESSIVE ADJECTIVES PLUS A LETTER) [Type: WORDPLAY_TRANSFORM]:** HERB, HISS, ITSY, MYA

### Top Candidate Partitions:
1. **Partition Score: 0.3957**
   - Group 1: **0.4562** | STRIKE, MARCH, RALLY, PICKET                                      | CORRECT GROUP (LABOR PROTEST ACTIONS, Level 1)
   - Group 2: **0.4408** | HERB, ITSY, MYA, MASK                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 3: **0.3870** | SHED, HISS, DRUM, RATTLE                                          | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 4: **0.3775** | STABLE, PEN, COOP, STAFF                                          | INCORRECT (Max overlap: 3/4 with FARM FIXTURES)
2. **Partition Score: 0.3912**
   - Group 1: **0.4562** | STRIKE, MARCH, RALLY, PICKET                                      | CORRECT GROUP (LABOR PROTEST ACTIONS, Level 1)
   - Group 2: **0.4312** | HISS, DRUM, MASK, RATTLE                                          | INCORRECT (Max overlap: 3/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 3: **0.3786** | HERB, SHED, ITSY, MYA                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 4: **0.3775** | STABLE, PEN, COOP, STAFF                                          | INCORRECT (Max overlap: 3/4 with FARM FIXTURES)
3. **Partition Score: 0.3890**
   - Group 1: **0.4408** | HERB, ITSY, MYA, MASK                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 2: **0.4156** | RALLY, HISS, DRUM, RATTLE                                         | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 3: **0.3855** | STRIKE, SHED, MARCH, PICKET                                       | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 4: **0.3775** | STABLE, PEN, COOP, STAFF                                          | INCORRECT (Max overlap: 3/4 with FARM FIXTURES)
4. **Partition Score: 0.3800**
   - Group 1: **0.4408** | HERB, ITSY, MYA, MASK                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 2: **0.3856** | MARCH, RALLY, HISS, PICKET                                        | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 3: **0.3794** | STRIKE, SHED, DRUM, RATTLE                                        | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 4: **0.3775** | STABLE, PEN, COOP, STAFF                                          | INCORRECT (Max overlap: 3/4 with FARM FIXTURES)
5. **Partition Score: 0.3792**
   - Group 1: **0.4816** | HERB, ITSY, MYA, STAFF                                            | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 2: **0.4562** | STRIKE, MARCH, RALLY, PICKET                                      | CORRECT GROUP (LABOR PROTEST ACTIONS, Level 1)
   - Group 3: **0.3870** | SHED, HISS, DRUM, RATTLE                                          | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 4: **0.3367** | STABLE, PEN, MASK, COOP                                           | INCORRECT (Max overlap: 3/4 with FARM FIXTURES)

### Top Candidate Groups:
   - Group 1: **0.4562** | STRIKE, MARCH, RALLY, PICKET                                      | CORRECT GROUP (LABOR PROTEST ACTIONS, Level 1)
   - Group 2: **0.4408** | HERB, ITSY, MYA, MASK                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 3: **0.3870** | SHED, HISS, DRUM, RATTLE                                          | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 4: **0.3775** | STABLE, PEN, COOP, STAFF                                          | INCORRECT (Max overlap: 3/4 with FARM FIXTURES)
   - Group 5: **0.4312** | HISS, DRUM, MASK, RATTLE                                          | INCORRECT (Max overlap: 3/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 6: **0.3786** | HERB, SHED, ITSY, MYA                                             | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 7: **0.4156** | RALLY, HISS, DRUM, RATTLE                                         | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 8: **0.3855** | STRIKE, SHED, MARCH, PICKET                                       | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 9: **0.3856** | MARCH, RALLY, HISS, PICKET                                        | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 10: **0.3794** | STRIKE, SHED, DRUM, RATTLE                                        | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 11: **0.4816** | HERB, ITSY, MYA, STAFF                                            | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 12: **0.3367** | STABLE, PEN, MASK, COOP                                           | INCORRECT (Max overlap: 3/4 with FARM FIXTURES)
   - Group 13: **0.3738** | HERB, ITSY, RALLY, MYA                                            | INCORRECT (Max overlap: 3/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)
   - Group 14: **0.3929** | SHED, HISS, DRUM, MASK                                            | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 15: **0.3852** | STRIKE, MARCH, PICKET, RATTLE                                     | INCORRECT (Max overlap: 3/4 with LABOR PROTEST ACTIONS)
   - Group 16: **0.4170** | HERB, ITSY, HISS, MYA                                             | CORRECT GROUP (POSSESSIVE ADJECTIVES PLUS A LETTER, Level 3)
   - Group 17: **0.3737** | SHED, RALLY, DRUM, MASK                                           | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 18: **0.3734** | RALLY, HISS, DRUM, MASK                                           | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES)
   - Group 19: **0.4418** | HERB, PEN, MASK, STAFF                                            | INCORRECT (Max overlap: 2/4 with OBJECTS USED IN RITUAL PERFORMANCES) | [Pred Type: FILL_IN_THE_BLANK (52.5%, no-rel 21.2%)]
   - Group 20: **0.3360** | ITSY, STABLE, MYA, COOP                                           | INCORRECT (Max overlap: 2/4 with POSSESSIVE ADJECTIVES PLUS A LETTER)

---

## Puzzle 101 (ID: 813)
**Words on Board:** PREMIERE, BISHOP, PRESIDENT, LAUNCH, SAINT VALENTINE, M.L.B. PLAYER, INTRODUCTION, N.F.L. PLAYER, LORDE, SAINT PATRICK, CLERGY MEMBER, POPE, BURNS, BIRD, DEBUT, MOTHER

### Ground Truth Categories:
* **Level 0 (FIRST APPEARANCE) [Type: SYNONYM_OR_NEAR]:** DEBUT, INTRODUCTION, LAUNCH, PREMIERE
* **Level 1 (ONES CELEBRATED WITH HOLIDAYS) [Type: NAMED_ENTITY_SET]:** MOTHER, PRESIDENT, SAINT PATRICK, SAINT VALENTINE
* **Level 2 (FAMOUS POETS) [Type: NAMED_ENTITY_SET]:** BISHOP, BURNS, LORDE, POPE
* **Level 3 (WHAT "CARDINAL" MIGHT REFER TO) [Type: WORDPLAY_TRANSFORM]:** BIRD, CLERGY MEMBER, M.L.B. PLAYER, N.F.L. PLAYER

### Top Candidate Partitions:
1. **Partition Score: 0.4787**
   - Group 1: **0.6149** | PREMIERE, LAUNCH, INTRODUCTION, DEBUT                             | CORRECT GROUP (FIRST APPEARANCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (67.3%, no-rel 26.6%)]
   - Group 2: **0.5830** | SAINT VALENTINE, LORDE, SAINT PATRICK, CLERGY MEMBER              | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 3: **0.4872** | PRESIDENT, BURNS, BIRD, MOTHER                                    | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS) | [Pred Type: FILL_IN_THE_BLANK (54.5%, no-rel 19.6%)]
   - Group 4: **0.4223** | BISHOP, M.L.B. PLAYER, N.F.L. PLAYER, POPE                        | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (50.7%, no-rel 17.5%)]
2. **Partition Score: 0.4783**
   - Group 1: **0.6149** | PREMIERE, LAUNCH, INTRODUCTION, DEBUT                             | CORRECT GROUP (FIRST APPEARANCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (67.3%, no-rel 26.6%)]
   - Group 2: **0.6027** | SAINT VALENTINE, M.L.B. PLAYER, N.F.L. PLAYER, SAINT PATRICK      | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 3: **0.4386** | BISHOP, CLERGY MEMBER, POPE, BIRD                                 | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (61.9%, no-rel 20.9%)]
   - Group 4: **0.4359** | PRESIDENT, LORDE, BURNS, MOTHER                                   | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
3. **Partition Score: 0.4772**
   - Group 1: **0.6149** | PREMIERE, LAUNCH, INTRODUCTION, DEBUT                             | CORRECT GROUP (FIRST APPEARANCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (67.3%, no-rel 26.6%)]
   - Group 2: **0.6027** | SAINT VALENTINE, M.L.B. PLAYER, N.F.L. PLAYER, SAINT PATRICK      | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 3: **0.4514** | BISHOP, PRESIDENT, CLERGY MEMBER, POPE                            | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (58.7%, no-rel 18.5%)]
   - Group 4: **0.4274** | LORDE, BURNS, BIRD, MOTHER                                        | INCORRECT (Max overlap: 2/4 with FAMOUS POETS)
4. **Partition Score: 0.4727**
   - Group 1: **0.6149** | PREMIERE, LAUNCH, INTRODUCTION, DEBUT                             | CORRECT GROUP (FIRST APPEARANCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (67.3%, no-rel 26.6%)]
   - Group 2: **0.6027** | SAINT VALENTINE, M.L.B. PLAYER, N.F.L. PLAYER, SAINT PATRICK      | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 3: **0.5063** | PRESIDENT, LORDE, CLERGY MEMBER, MOTHER                           | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 4: **0.3909** | BISHOP, POPE, BURNS, BIRD                                         | INCORRECT (Max overlap: 3/4 with FAMOUS POETS)
5. **Partition Score: 0.4683**
   - Group 1: **0.6149** | PREMIERE, LAUNCH, INTRODUCTION, DEBUT                             | CORRECT GROUP (FIRST APPEARANCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (67.3%, no-rel 26.6%)]
   - Group 2: **0.5471** | SAINT VALENTINE, N.F.L. PLAYER, LORDE, SAINT PATRICK              | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 3: **0.4872** | PRESIDENT, BURNS, BIRD, MOTHER                                    | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS) | [Pred Type: FILL_IN_THE_BLANK (54.5%, no-rel 19.6%)]
   - Group 4: **0.4196** | BISHOP, M.L.B. PLAYER, CLERGY MEMBER, POPE                        | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (56.2%, no-rel 14.6%)]

### Top Candidate Groups:
   - Group 1: **0.6149** | PREMIERE, LAUNCH, INTRODUCTION, DEBUT                             | CORRECT GROUP (FIRST APPEARANCE, Level 0) | [Pred Type: SYNONYM_OR_NEAR (67.3%, no-rel 26.6%)]
   - Group 2: **0.5830** | SAINT VALENTINE, LORDE, SAINT PATRICK, CLERGY MEMBER              | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 3: **0.4872** | PRESIDENT, BURNS, BIRD, MOTHER                                    | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS) | [Pred Type: FILL_IN_THE_BLANK (54.5%, no-rel 19.6%)]
   - Group 4: **0.4223** | BISHOP, M.L.B. PLAYER, N.F.L. PLAYER, POPE                        | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (50.7%, no-rel 17.5%)]
   - Group 5: **0.6027** | SAINT VALENTINE, M.L.B. PLAYER, N.F.L. PLAYER, SAINT PATRICK      | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 6: **0.4386** | BISHOP, CLERGY MEMBER, POPE, BIRD                                 | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (61.9%, no-rel 20.9%)]
   - Group 7: **0.4359** | PRESIDENT, LORDE, BURNS, MOTHER                                   | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 8: **0.4514** | BISHOP, PRESIDENT, CLERGY MEMBER, POPE                            | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (58.7%, no-rel 18.5%)]
   - Group 9: **0.4274** | LORDE, BURNS, BIRD, MOTHER                                        | INCORRECT (Max overlap: 2/4 with FAMOUS POETS)
   - Group 10: **0.5063** | PRESIDENT, LORDE, CLERGY MEMBER, MOTHER                           | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 11: **0.3909** | BISHOP, POPE, BURNS, BIRD                                         | INCORRECT (Max overlap: 3/4 with FAMOUS POETS)
   - Group 12: **0.5471** | SAINT VALENTINE, N.F.L. PLAYER, LORDE, SAINT PATRICK              | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 13: **0.4196** | BISHOP, M.L.B. PLAYER, CLERGY MEMBER, POPE                        | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (56.2%, no-rel 14.6%)]
   - Group 14: **0.5087** | PRESIDENT, SAINT VALENTINE, LORDE, SAINT PATRICK                  | INCORRECT (Max overlap: 3/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 15: **0.4716** | POPE, BURNS, BIRD, MOTHER                                         | INCORRECT (Max overlap: 2/4 with FAMOUS POETS)
   - Group 16: **0.4450** | BISHOP, M.L.B. PLAYER, N.F.L. PLAYER, CLERGY MEMBER               | INCORRECT (Max overlap: 3/4 with WHAT "CARDINAL" MIGHT REFER TO)
   - Group 17: **0.5379** | SAINT VALENTINE, M.L.B. PLAYER, LORDE, SAINT PATRICK              | INCORRECT (Max overlap: 2/4 with ONES CELEBRATED WITH HOLIDAYS)
   - Group 18: **0.4220** | BISHOP, N.F.L. PLAYER, CLERGY MEMBER, POPE                        | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (56.3%, no-rel 15.3%)]
   - Group 19: **0.4254** | PRESIDENT, LORDE, BURNS, BIRD                                     | INCORRECT (Max overlap: 2/4 with FAMOUS POETS)
   - Group 20: **0.4199** | BISHOP, CLERGY MEMBER, POPE, MOTHER                               | INCORRECT (Max overlap: 2/4 with FAMOUS POETS) | [Pred Type: SEMANTIC_SET (50.2%, no-rel 22.1%)]

---

## Puzzle 102 (ID: 1049)
**Words on Board:** STRING, ROOM, PHASE, SHADOW, SOCK, ROLL, ORDERS, ROUND, BOOM, HAND, CLAP, RUMBLE, STAGE, LEVEL, JOKE, OVATION

### Ground Truth Categories:
* **Level 0 (STEP IN A PROCESS) [Type: SYNONYM_OR_NEAR]:** LEVEL, PHASE, ROUND, STAGE
* **Level 1 (SOUND LIKE THUNDER) [Type: SEMANTIC_SET]:** BOOM, CLAP, ROLL, RUMBLE
* **Level 2 (KINDS OF PUPPETS) [Type: SEMANTIC_SET]:** HAND, SHADOW, SOCK, STRING
* **Level 3 (STANDING ___) [Type: FILL_IN_THE_BLANK]:** JOKE, ORDERS, OVATION, ROOM

### Top Candidate Partitions:
1. **Partition Score: 0.4300**
   - Group 1: **0.5022** | STRING, SOCK, HAND, CLAP                                          | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 2: **0.4954** | ROLL, ROUND, BOOM, RUMBLE                                         | INCORRECT (Max overlap: 3/4 with SOUND LIKE THUNDER) | [Pred Type: SYNONYM_OR_NEAR (46.1%, no-rel 36.0%)]
   - Group 3: **0.4379** | ROOM, SHADOW, JOKE, OVATION                                       | INCORRECT (Max overlap: 3/4 with STANDING ___)
   - Group 4: **0.3934** | PHASE, ORDERS, STAGE, LEVEL                                       | INCORRECT (Max overlap: 3/4 with STEP IN A PROCESS) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 19.3%)]
2. **Partition Score: 0.4250**
   - Group 1: **0.5644** | ROLL, BOOM, CLAP, RUMBLE                                          | CORRECT GROUP (SOUND LIKE THUNDER, Level 1)
   - Group 2: **0.4754** | STRING, SOCK, ROUND, HAND                                         | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 3: **0.4379** | ROOM, SHADOW, JOKE, OVATION                                       | INCORRECT (Max overlap: 3/4 with STANDING ___)
   - Group 4: **0.3934** | PHASE, ORDERS, STAGE, LEVEL                                       | INCORRECT (Max overlap: 3/4 with STEP IN A PROCESS) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 19.3%)]
3. **Partition Score: 0.4187**
   - Group 1: **0.4954** | ROLL, ROUND, BOOM, RUMBLE                                         | INCORRECT (Max overlap: 3/4 with SOUND LIKE THUNDER) | [Pred Type: SYNONYM_OR_NEAR (46.1%, no-rel 36.0%)]
   - Group 2: **0.4590** | SOCK, HAND, CLAP, OVATION                                         | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 3: **0.4292** | STRING, ROOM, SHADOW, JOKE                                        | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS) | [Pred Type: FILL_IN_THE_BLANK (61.3%, no-rel 15.6%)]
   - Group 4: **0.3934** | PHASE, ORDERS, STAGE, LEVEL                                       | INCORRECT (Max overlap: 3/4 with STEP IN A PROCESS) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 19.3%)]
4. **Partition Score: 0.4166**
   - Group 1: **0.5644** | ROLL, BOOM, CLAP, RUMBLE                                          | CORRECT GROUP (SOUND LIKE THUNDER, Level 1)
   - Group 2: **0.5029** | STRING, SHADOW, SOCK, HAND                                        | CORRECT GROUP (KINDS OF PUPPETS, Level 2)
   - Group 3: **0.4321** | ROOM, ORDERS, JOKE, OVATION                                       | CORRECT GROUP (STANDING ___, Level 3)
   - Group 4: **0.3657** | PHASE, ROUND, STAGE, LEVEL                                        | CORRECT GROUP (STEP IN A PROCESS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 25.6%)]
5. **Partition Score: 0.4155**
   - Group 1: **0.4954** | ROLL, ROUND, BOOM, RUMBLE                                         | INCORRECT (Max overlap: 3/4 with SOUND LIKE THUNDER) | [Pred Type: SYNONYM_OR_NEAR (46.1%, no-rel 36.0%)]
   - Group 2: **0.4644** | SOCK, HAND, CLAP, JOKE                                            | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 3: **0.4105** | STRING, ROOM, SHADOW, OVATION                                     | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 4: **0.3934** | PHASE, ORDERS, STAGE, LEVEL                                       | INCORRECT (Max overlap: 3/4 with STEP IN A PROCESS) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 19.3%)]

### Top Candidate Groups:
   - Group 1: **0.5022** | STRING, SOCK, HAND, CLAP                                          | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 2: **0.4954** | ROLL, ROUND, BOOM, RUMBLE                                         | INCORRECT (Max overlap: 3/4 with SOUND LIKE THUNDER) | [Pred Type: SYNONYM_OR_NEAR (46.1%, no-rel 36.0%)]
   - Group 3: **0.4379** | ROOM, SHADOW, JOKE, OVATION                                       | INCORRECT (Max overlap: 3/4 with STANDING ___)
   - Group 4: **0.3934** | PHASE, ORDERS, STAGE, LEVEL                                       | INCORRECT (Max overlap: 3/4 with STEP IN A PROCESS) | [Pred Type: SYNONYM_OR_NEAR (71.7%, no-rel 19.3%)]
   - Group 5: **0.5644** | ROLL, BOOM, CLAP, RUMBLE                                          | CORRECT GROUP (SOUND LIKE THUNDER, Level 1)
   - Group 6: **0.4754** | STRING, SOCK, ROUND, HAND                                         | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 7: **0.4590** | SOCK, HAND, CLAP, OVATION                                         | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 8: **0.4292** | STRING, ROOM, SHADOW, JOKE                                        | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS) | [Pred Type: FILL_IN_THE_BLANK (61.3%, no-rel 15.6%)]
   - Group 9: **0.5029** | STRING, SHADOW, SOCK, HAND                                        | CORRECT GROUP (KINDS OF PUPPETS, Level 2)
   - Group 10: **0.4321** | ROOM, ORDERS, JOKE, OVATION                                       | CORRECT GROUP (STANDING ___, Level 3)
   - Group 11: **0.3657** | PHASE, ROUND, STAGE, LEVEL                                        | CORRECT GROUP (STEP IN A PROCESS, Level 0) | [Pred Type: SYNONYM_OR_NEAR (63.9%, no-rel 25.6%)]
   - Group 12: **0.4644** | SOCK, HAND, CLAP, JOKE                                            | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 13: **0.4105** | STRING, ROOM, SHADOW, OVATION                                     | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 14: **0.4458** | ROOM, SHADOW, ORDERS, OVATION                                     | INCORRECT (Max overlap: 3/4 with STANDING ___)
   - Group 15: **0.3567** | PHASE, STAGE, LEVEL, JOKE                                         | INCORRECT (Max overlap: 3/4 with STEP IN A PROCESS) | [Pred Type: SYNONYM_OR_NEAR (64.6%, no-rel 25.2%)]
   - Group 16: **0.4622** | STRING, SOCK, HAND, JOKE                                          | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 17: **0.4489** | ROLL, BOOM, RUMBLE, JOKE                                          | INCORRECT (Max overlap: 3/4 with SOUND LIKE THUNDER)
   - Group 18: **0.4385** | SOCK, ROUND, HAND, CLAP                                           | INCORRECT (Max overlap: 2/4 with KINDS OF PUPPETS)
   - Group 19: **0.4683** | STRING, SOCK, HAND, OVATION                                       | INCORRECT (Max overlap: 3/4 with KINDS OF PUPPETS)
   - Group 20: **0.4350** | ROOM, SHADOW, ORDERS, JOKE                                        | INCORRECT (Max overlap: 3/4 with STANDING ___) | [Pred Type: FILL_IN_THE_BLANK (52.9%, no-rel 16.5%)]

---

## Puzzle 103 (ID: 643)
**Words on Board:** TONIGHT, SUE, PEG, MOVE, STRING, BARB, NEEDLE, SERVE, BRIDGE, BRISTLE, SPINE, MIGHT, NECK, CHARGE, WISH, MAY

### Ground Truth Categories:
* **Level 0 (SHARP PROTRUSION) [Type: SEMANTIC_SET]:** BARB, BRISTLE, NEEDLE, SPINE
* **Level 1 (FEATURES OF STRINGED INSTRUMENTS) [Type: SEMANTIC_SET]:** BRIDGE, NECK, PEG, STRING
* **Level 2 (LITIGATION VERBS) [Type: SEMANTIC_SET]:** CHARGE, MOVE, SERVE, SUE
* **Level 3 (IN “STAR LIGHT, STAR BRIGHT”) [Type: FILL_IN_THE_BLANK]:** MAY, MIGHT, TONIGHT, WISH

### Top Candidate Partitions:
1. **Partition Score: 0.4067**
   - Group 1: **0.4852** | PEG, NEEDLE, SPINE, NECK                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS) | [Pred Type: SEMANTIC_SET (49.0%, no-rel 28.5%)]
   - Group 2: **0.4696** | MIGHT, CHARGE, WISH, MAY                                          | INCORRECT (Max overlap: 3/4 with IN “STAR LIGHT, STAR BRIGHT”) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 25.9%)]
   - Group 3: **0.4299** | STRING, BARB, BRIDGE, BRISTLE                                     | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 4: **0.3636** | TONIGHT, SUE, MOVE, SERVE                                         | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
2. **Partition Score: 0.4055**
   - Group 1: **0.4293** | SUE, MOVE, MIGHT, MAY                                             | INCORRECT (Max overlap: 2/4 with LITIGATION VERBS)
   - Group 2: **0.4151** | STRING, BRISTLE, SPINE, NECK                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS) | [Pred Type: SEMANTIC_SET (46.9%, no-rel 24.6%)]
   - Group 3: **0.4122** | BARB, SERVE, CHARGE, WISH                                         | INCORRECT (Max overlap: 2/4 with LITIGATION VERBS)
   - Group 4: **0.3973** | TONIGHT, PEG, NEEDLE, BRIDGE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
3. **Partition Score: 0.4032**
   - Group 1: **0.4266** | MOVE, MIGHT, WISH, MAY                                            | INCORRECT (Max overlap: 3/4 with IN “STAR LIGHT, STAR BRIGHT”)
   - Group 2: **0.4151** | STRING, BRISTLE, SPINE, NECK                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS) | [Pred Type: SEMANTIC_SET (46.9%, no-rel 24.6%)]
   - Group 3: **0.4031** | SUE, BARB, SERVE, CHARGE                                          | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 4: **0.3973** | TONIGHT, PEG, NEEDLE, BRIDGE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
4. **Partition Score: 0.4032**
   - Group 1: **0.5981** | SUE, MOVE, SERVE, MAY                                             | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 2: **0.4151** | STRING, BRISTLE, SPINE, NECK                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS) | [Pred Type: SEMANTIC_SET (46.9%, no-rel 24.6%)]
   - Group 3: **0.4029** | BARB, MIGHT, CHARGE, WISH                                         | INCORRECT (Max overlap: 2/4 with IN “STAR LIGHT, STAR BRIGHT”)
   - Group 4: **0.3973** | TONIGHT, PEG, NEEDLE, BRIDGE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
5. **Partition Score: 0.4024**
   - Group 1: **0.4789** | SUE, MOVE, SERVE, CHARGE                                          | CORRECT GROUP (LITIGATION VERBS, Level 2)
   - Group 2: **0.4151** | STRING, BRISTLE, SPINE, NECK                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS) | [Pred Type: SEMANTIC_SET (46.9%, no-rel 24.6%)]
   - Group 3: **0.4000** | BARB, MIGHT, WISH, MAY                                            | INCORRECT (Max overlap: 3/4 with IN “STAR LIGHT, STAR BRIGHT”)
   - Group 4: **0.3973** | TONIGHT, PEG, NEEDLE, BRIDGE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)

### Top Candidate Groups:
   - Group 1: **0.4852** | PEG, NEEDLE, SPINE, NECK                                          | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS) | [Pred Type: SEMANTIC_SET (49.0%, no-rel 28.5%)]
   - Group 2: **0.4696** | MIGHT, CHARGE, WISH, MAY                                          | INCORRECT (Max overlap: 3/4 with IN “STAR LIGHT, STAR BRIGHT”) | [Pred Type: SYNONYM_OR_NEAR (48.0%, no-rel 25.9%)]
   - Group 3: **0.4299** | STRING, BARB, BRIDGE, BRISTLE                                     | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 4: **0.3636** | TONIGHT, SUE, MOVE, SERVE                                         | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 5: **0.4293** | SUE, MOVE, MIGHT, MAY                                             | INCORRECT (Max overlap: 2/4 with LITIGATION VERBS)
   - Group 6: **0.4151** | STRING, BRISTLE, SPINE, NECK                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS) | [Pred Type: SEMANTIC_SET (46.9%, no-rel 24.6%)]
   - Group 7: **0.4122** | BARB, SERVE, CHARGE, WISH                                         | INCORRECT (Max overlap: 2/4 with LITIGATION VERBS)
   - Group 8: **0.3973** | TONIGHT, PEG, NEEDLE, BRIDGE                                      | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 9: **0.4266** | MOVE, MIGHT, WISH, MAY                                            | INCORRECT (Max overlap: 3/4 with IN “STAR LIGHT, STAR BRIGHT”)
   - Group 10: **0.4031** | SUE, BARB, SERVE, CHARGE                                          | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 11: **0.5981** | SUE, MOVE, SERVE, MAY                                             | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 12: **0.4029** | BARB, MIGHT, CHARGE, WISH                                         | INCORRECT (Max overlap: 2/4 with IN “STAR LIGHT, STAR BRIGHT”)
   - Group 13: **0.4789** | SUE, MOVE, SERVE, CHARGE                                          | CORRECT GROUP (LITIGATION VERBS, Level 2)
   - Group 14: **0.4000** | BARB, MIGHT, WISH, MAY                                            | INCORRECT (Max overlap: 3/4 with IN “STAR LIGHT, STAR BRIGHT”)
   - Group 15: **0.4601** | PEG, STRING, BARB, BRISTLE                                        | INCORRECT (Max overlap: 2/4 with FEATURES OF STRINGED INSTRUMENTS)
   - Group 16: **0.4169** | NEEDLE, BRIDGE, SPINE, NECK                                       | INCORRECT (Max overlap: 2/4 with SHARP PROTRUSION) | [Pred Type: SEMANTIC_SET (51.6%, no-rel 28.0%)]
   - Group 17: **0.4569** | SUE, MIGHT, WISH, MAY                                             | INCORRECT (Max overlap: 3/4 with IN “STAR LIGHT, STAR BRIGHT”)
   - Group 18: **0.3954** | MOVE, BARB, SERVE, CHARGE                                         | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)
   - Group 19: **0.4401** | BARB, CHARGE, WISH, MAY                                           | INCORRECT (Max overlap: 2/4 with IN “STAR LIGHT, STAR BRIGHT”) | [Pred Type: SYNONYM_OR_NEAR (45.5%, no-rel 33.5%)]
   - Group 20: **0.3937** | SUE, MOVE, SERVE, MIGHT                                           | INCORRECT (Max overlap: 3/4 with LITIGATION VERBS)

---

## Puzzle 104 (ID: 157)
**Words on Board:** HAI, WE, O, W, DA, ICK, US, JA, WEE, SI, OK, OUI, EW, PU, UGH, WII

### Ground Truth Categories:
* **Level 0 (“GROSS!”) [Type: SYNONYM_OR_NEAR]:** EW, ICK, PU, UGH
* **Level 1 (MAGAZINES) [Type: NAMED_ENTITY_SET]:** O, OK, US, W
* **Level 2 (“YES” IN DIFFERENT LANGUAGES) [Type: SYNONYM_OR_NEAR]:** HAI, JA, SI, DA
* **Level 3 (HOMOPHONES) [Type: SOUND_OR_SPELLING]:** OUI, WE, WEE, WII

### Top Candidate Partitions:
1. **Partition Score: 0.4266**
   - Group 1: **0.4644** | WE, WEE, OK, OUI                                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (74.1%, no-rel 7.7%)]
   - Group 2: **0.4441** | HAI, DA, JA, WII                                                  | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES) | [Pred Type: SOUND_OR_SPELLING (45.7%, no-rel 15.2%)]
   - Group 3: **0.4228** | O, W, US, PU                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 4: **0.4198** | ICK, SI, EW, UGH                                                  | INCORRECT (Max overlap: 3/4 with “GROSS!”) | [Pred Type: SYNONYM_OR_NEAR (45.8%, no-rel 26.7%)]
2. **Partition Score: 0.4226**
   - Group 1: **0.4477** | HAI, WE, WEE, WII                                                 | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (75.7%, no-rel 7.6%)]
   - Group 2: **0.4279** | DA, JA, OK, OUI                                                   | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES) | [Pred Type: SOUND_OR_SPELLING (50.8%, no-rel 10.8%)]
   - Group 3: **0.4228** | O, W, US, PU                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 4: **0.4198** | ICK, SI, EW, UGH                                                  | INCORRECT (Max overlap: 3/4 with “GROSS!”) | [Pred Type: SYNONYM_OR_NEAR (45.8%, no-rel 26.7%)]
3. **Partition Score: 0.4217**
   - Group 1: **0.4358** | WE, DA, WEE, WII                                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (74.7%, no-rel 9.4%)]
   - Group 2: **0.4246** | HAI, JA, OK, OUI                                                  | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 3: **0.4228** | O, W, US, PU                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 4: **0.4198** | ICK, SI, EW, UGH                                                  | INCORRECT (Max overlap: 3/4 with “GROSS!”) | [Pred Type: SYNONYM_OR_NEAR (45.8%, no-rel 26.7%)]
4. **Partition Score: 0.4211**
   - Group 1: **0.5757** | WE, WEE, OUI, WII                                                 | CORRECT GROUP (HOMOPHONES, Level 3) | [Pred Type: SOUND_OR_SPELLING (79.7%, no-rel 6.8%)]
   - Group 2: **0.4228** | O, W, US, PU                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 3: **0.4221** | HAI, DA, JA, OK                                                   | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 4: **0.4198** | ICK, SI, EW, UGH                                                  | INCORRECT (Max overlap: 3/4 with “GROSS!”) | [Pred Type: SYNONYM_OR_NEAR (45.8%, no-rel 26.7%)]
5. **Partition Score: 0.4210**
   - Group 1: **0.4442** | WE, JA, OUI, WII                                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (65.7%, no-rel 11.8%)]
   - Group 2: **0.4228** | O, W, US, PU                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 3: **0.4215** | HAI, DA, WEE, OK                                                  | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 4: **0.4198** | ICK, SI, EW, UGH                                                  | INCORRECT (Max overlap: 3/4 with “GROSS!”) | [Pred Type: SYNONYM_OR_NEAR (45.8%, no-rel 26.7%)]

### Top Candidate Groups:
   - Group 1: **0.4644** | WE, WEE, OK, OUI                                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (74.1%, no-rel 7.7%)]
   - Group 2: **0.4441** | HAI, DA, JA, WII                                                  | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES) | [Pred Type: SOUND_OR_SPELLING (45.7%, no-rel 15.2%)]
   - Group 3: **0.4228** | O, W, US, PU                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 4: **0.4198** | ICK, SI, EW, UGH                                                  | INCORRECT (Max overlap: 3/4 with “GROSS!”) | [Pred Type: SYNONYM_OR_NEAR (45.8%, no-rel 26.7%)]
   - Group 5: **0.4477** | HAI, WE, WEE, WII                                                 | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (75.7%, no-rel 7.6%)]
   - Group 6: **0.4279** | DA, JA, OK, OUI                                                   | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES) | [Pred Type: SOUND_OR_SPELLING (50.8%, no-rel 10.8%)]
   - Group 7: **0.4358** | WE, DA, WEE, WII                                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (74.7%, no-rel 9.4%)]
   - Group 8: **0.4246** | HAI, JA, OK, OUI                                                  | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 9: **0.5757** | WE, WEE, OUI, WII                                                 | CORRECT GROUP (HOMOPHONES, Level 3) | [Pred Type: SOUND_OR_SPELLING (79.7%, no-rel 6.8%)]
   - Group 10: **0.4221** | HAI, DA, JA, OK                                                   | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 11: **0.4442** | WE, JA, OUI, WII                                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (65.7%, no-rel 11.8%)]
   - Group 12: **0.4215** | HAI, DA, WEE, OK                                                  | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 13: **0.4281** | WE, JA, WEE, WII                                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (75.3%, no-rel 7.6%)]
   - Group 14: **0.4185** | HAI, DA, OK, OUI                                                  | INCORRECT (Max overlap: 2/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 15: **0.4210** | WEE, OK, OUI, WII                                                 | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (69.7%, no-rel 8.6%)]
   - Group 16: **0.4129** | HAI, WE, DA, JA                                                   | INCORRECT (Max overlap: 3/4 with “YES” IN DIFFERENT LANGUAGES) | [Pred Type: SOUND_OR_SPELLING (50.0%, no-rel 10.7%)]
   - Group 17: **0.4913** | O, W, US, SI                                                      | INCORRECT (Max overlap: 3/4 with MAGAZINES)
   - Group 18: **0.4090** | HAI, ICK, EW, UGH                                                 | INCORRECT (Max overlap: 3/4 with “GROSS!”)
   - Group 19: **0.4030** | DA, WEE, OK, PU                                                   | INCORRECT (Max overlap: 1/4 with “YES” IN DIFFERENT LANGUAGES)
   - Group 20: **0.4273** | WE, DA, OUI, WII                                                  | INCORRECT (Max overlap: 3/4 with HOMOPHONES) | [Pred Type: SOUND_OR_SPELLING (71.0%, no-rel 8.6%)]

---

## Puzzle 105 (ID: 113)
**Words on Board:** SALUTE, DOWN, MAPS, FINGER, FUR, STAND, KNEEL, MAIL, NOTES, HINT, CLOCK, SHELL, ARROW, DOG, SCALES, BOW

### Ground Truth Categories:
* **Level 0 (WAYS TO SHOW RESPECT) [Type: SEMANTIC_SET]:** BOW, KNEEL, SALUTE, STAND
* **Level 1 (IPHONE APPS) [Type: NAMED_ENTITY_SET]:** CLOCK, MAIL, MAPS, NOTES
* **Level 2 (ANIMAL COVERINGS) [Type: SEMANTIC_SET]:** DOWN, FUR, SCALES, SHELL
* **Level 3 (“POINTERS”) [Type: SEMANTIC_SET]:** ARROW, DOG, FINGER, HINT

### Top Candidate Partitions:
1. **Partition Score: 0.3636**
   - Group 1: **0.3853** | SALUTE, FINGER, STAND, NOTES                                      | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 2: **0.3802** | DOWN, KNEEL, ARROW, BOW                                           | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 3: **0.3687** | MAPS, CLOCK, SHELL, SCALES                                        | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 4: **0.3528** | FUR, MAIL, HINT, DOG                                              | INCORRECT (Max overlap: 2/4 with “POINTERS”)
2. **Partition Score: 0.3524**
   - Group 1: **0.4428** | SALUTE, FINGER, STAND, KNEEL                                      | INCORRECT (Max overlap: 3/4 with WAYS TO SHOW RESPECT)
   - Group 2: **0.3761** | MAPS, FUR, MAIL, HINT                                             | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 3: **0.3620** | NOTES, CLOCK, SHELL, SCALES                                       | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 4: **0.3357** | DOWN, ARROW, DOG, BOW                                             | INCORRECT (Max overlap: 2/4 with “POINTERS”)
3. **Partition Score: 0.3437**
   - Group 1: **0.4153** | SALUTE, DOWN, STAND, KNEEL                                        | INCORRECT (Max overlap: 3/4 with WAYS TO SHOW RESPECT)
   - Group 2: **0.4030** | FINGER, MAIL, NOTES, HINT                                         | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 3: **0.3687** | MAPS, CLOCK, SHELL, SCALES                                        | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 4: **0.3015** | FUR, ARROW, DOG, BOW                                              | INCORRECT (Max overlap: 2/4 with “POINTERS”)
4. **Partition Score: 0.3409**
   - Group 1: **0.4428** | SALUTE, FINGER, STAND, KNEEL                                      | INCORRECT (Max overlap: 3/4 with WAYS TO SHOW RESPECT)
   - Group 2: **0.4255** | MAPS, MAIL, NOTES, HINT                                           | INCORRECT (Max overlap: 3/4 with IPHONE APPS)
   - Group 3: **0.3357** | DOWN, ARROW, DOG, BOW                                             | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 4: **0.3012** | FUR, CLOCK, SHELL, SCALES                                         | INCORRECT (Max overlap: 3/4 with ANIMAL COVERINGS)
5. **Partition Score: 0.3406**
   - Group 1: **0.3687** | MAPS, CLOCK, SHELL, SCALES                                        | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 2: **0.3648** | SALUTE, STAND, KNEEL, NOTES                                       | INCORRECT (Max overlap: 3/4 with WAYS TO SHOW RESPECT)
   - Group 3: **0.3528** | FUR, MAIL, HINT, DOG                                              | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 4: **0.3224** | DOWN, FINGER, ARROW, BOW                                          | INCORRECT (Max overlap: 2/4 with “POINTERS”)

### Top Candidate Groups:
   - Group 1: **0.3853** | SALUTE, FINGER, STAND, NOTES                                      | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 2: **0.3802** | DOWN, KNEEL, ARROW, BOW                                           | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 3: **0.3687** | MAPS, CLOCK, SHELL, SCALES                                        | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 4: **0.3528** | FUR, MAIL, HINT, DOG                                              | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 5: **0.4428** | SALUTE, FINGER, STAND, KNEEL                                      | INCORRECT (Max overlap: 3/4 with WAYS TO SHOW RESPECT)
   - Group 6: **0.3761** | MAPS, FUR, MAIL, HINT                                             | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 7: **0.3620** | NOTES, CLOCK, SHELL, SCALES                                       | INCORRECT (Max overlap: 2/4 with IPHONE APPS)
   - Group 8: **0.3357** | DOWN, ARROW, DOG, BOW                                             | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 9: **0.4153** | SALUTE, DOWN, STAND, KNEEL                                        | INCORRECT (Max overlap: 3/4 with WAYS TO SHOW RESPECT)
   - Group 10: **0.4030** | FINGER, MAIL, NOTES, HINT                                         | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 11: **0.3015** | FUR, ARROW, DOG, BOW                                              | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 12: **0.4255** | MAPS, MAIL, NOTES, HINT                                           | INCORRECT (Max overlap: 3/4 with IPHONE APPS)
   - Group 13: **0.3012** | FUR, CLOCK, SHELL, SCALES                                         | INCORRECT (Max overlap: 3/4 with ANIMAL COVERINGS)
   - Group 14: **0.3648** | SALUTE, STAND, KNEEL, NOTES                                       | INCORRECT (Max overlap: 3/4 with WAYS TO SHOW RESPECT)
   - Group 15: **0.3224** | DOWN, FINGER, ARROW, BOW                                          | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 16: **0.3118** | SALUTE, FINGER, STAND, DOG                                        | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 17: **0.4014** | SALUTE, DOWN, FINGER, KNEEL                                       | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 18: **0.3044** | STAND, ARROW, DOG, BOW                                            | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT)
   - Group 19: **0.3183** | FINGER, FUR, MAIL, HINT                                           | INCORRECT (Max overlap: 2/4 with “POINTERS”)
   - Group 20: **0.3644** | SALUTE, FINGER, KNEEL, NOTES                                      | INCORRECT (Max overlap: 2/4 with WAYS TO SHOW RESPECT) | [Pred Type: SYNONYM_OR_NEAR (45.6%, no-rel 34.9%)]

---

## Puzzle 106 (ID: 883)
**Words on Board:** REST, SPEECH BUBBLE, BLUSH, MUSIC NOTES, SCALE, COMPASS, SCOPE, EXTENT, STAND, ENVELOPE, FOUNDATION, BASE, HOLDER, RANGE, HIGHLIGHTER, POWDER

### Ground Truth Categories:
* **Level 0 (MAKEUP) [Type: SEMANTIC_SET]:** BLUSH, FOUNDATION, HIGHLIGHTER, POWDER
* **Level 1 (BREADTH) [Type: SYNONYM_OR_NEAR]:** EXTENT, RANGE, SCALE, SCOPE
* **Level 2 (OBJECT USED FOR SUPPORT) [Type: SYNONYM_OR_NEAR]:** BASE, HOLDER, REST, STAND
* **Level 3 (ICONS ON AN IPHONE) [Type: NAMED_ENTITY_SET]:** COMPASS, ENVELOPE, MUSIC NOTES, SPEECH BUBBLE

### Top Candidate Partitions:
1. **Partition Score: 0.4511**
   - Group 1: **0.7364** | COMPASS, SCOPE, EXTENT, RANGE                                     | INCORRECT (Max overlap: 3/4 with BREADTH) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 34.9%)]
   - Group 2: **0.5942** | REST, SCALE, STAND, BASE                                          | INCORRECT (Max overlap: 3/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (54.1%, no-rel 30.4%)]
   - Group 3: **0.4346** | SPEECH BUBBLE, MUSIC NOTES, ENVELOPE, HIGHLIGHTER                 | INCORRECT (Max overlap: 3/4 with ICONS ON AN IPHONE) | [Pred Type: SEMANTIC_SET (58.2%, no-rel 20.9%)]
   - Group 4: **0.3878** | BLUSH, FOUNDATION, HOLDER, POWDER                                 | INCORRECT (Max overlap: 3/4 with MAKEUP) | [Pred Type: FILL_IN_THE_BLANK (50.8%, no-rel 17.2%)]
2. **Partition Score: 0.4263**
   - Group 1: **0.7364** | COMPASS, SCOPE, EXTENT, RANGE                                     | INCORRECT (Max overlap: 3/4 with BREADTH) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 34.9%)]
   - Group 2: **0.5129** | REST, STAND, FOUNDATION, BASE                                     | INCORRECT (Max overlap: 3/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 31.1%)]
   - Group 3: **0.4148** | SCALE, ENVELOPE, HIGHLIGHTER, POWDER                              | INCORRECT (Max overlap: 2/4 with MAKEUP) | [Pred Type: SEMANTIC_SET (59.8%, no-rel 25.6%)]
   - Group 4: **0.3888** | SPEECH BUBBLE, BLUSH, MUSIC NOTES, HOLDER                         | INCORRECT (Max overlap: 2/4 with ICONS ON AN IPHONE)
3. **Partition Score: 0.4252**
   - Group 1: **0.7364** | COMPASS, SCOPE, EXTENT, RANGE                                     | INCORRECT (Max overlap: 3/4 with BREADTH) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 34.9%)]
   - Group 2: **0.5129** | REST, STAND, FOUNDATION, BASE                                     | INCORRECT (Max overlap: 3/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 31.1%)]
   - Group 3: **0.4346** | SPEECH BUBBLE, MUSIC NOTES, ENVELOPE, HIGHLIGHTER                 | INCORRECT (Max overlap: 3/4 with ICONS ON AN IPHONE) | [Pred Type: SEMANTIC_SET (58.2%, no-rel 20.9%)]
   - Group 4: **0.3768** | BLUSH, SCALE, HOLDER, POWDER                                      | INCORRECT (Max overlap: 2/4 with MAKEUP)
4. **Partition Score: 0.4200**
   - Group 1: **0.7364** | COMPASS, SCOPE, EXTENT, RANGE                                     | INCORRECT (Max overlap: 3/4 with BREADTH) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 34.9%)]
   - Group 2: **0.5129** | REST, STAND, FOUNDATION, BASE                                     | INCORRECT (Max overlap: 3/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 31.1%)]
   - Group 3: **0.4168** | BLUSH, MUSIC NOTES, HOLDER, POWDER                                | INCORRECT (Max overlap: 2/4 with MAKEUP)
   - Group 4: **0.3751** | SPEECH BUBBLE, SCALE, ENVELOPE, HIGHLIGHTER                       | INCORRECT (Max overlap: 2/4 with ICONS ON AN IPHONE) | [Pred Type: SEMANTIC_SET (64.9%, no-rel 21.1%)]
5. **Partition Score: 0.4189**
   - Group 1: **0.7364** | COMPASS, SCOPE, EXTENT, RANGE                                     | INCORRECT (Max overlap: 3/4 with BREADTH) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 34.9%)]
   - Group 2: **0.5129** | REST, STAND, FOUNDATION, BASE                                     | INCORRECT (Max overlap: 3/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 31.1%)]
   - Group 3: **0.4053** | SCALE, ENVELOPE, HOLDER, POWDER                                   | INCORRECT (Max overlap: 1/4 with BREADTH)
   - Group 4: **0.3788** | SPEECH BUBBLE, BLUSH, MUSIC NOTES, HIGHLIGHTER                    | INCORRECT (Max overlap: 2/4 with ICONS ON AN IPHONE)

### Top Candidate Groups:
   - Group 1: **0.7364** | COMPASS, SCOPE, EXTENT, RANGE                                     | INCORRECT (Max overlap: 3/4 with BREADTH) | [Pred Type: SYNONYM_OR_NEAR (56.3%, no-rel 34.9%)]
   - Group 2: **0.5942** | REST, SCALE, STAND, BASE                                          | INCORRECT (Max overlap: 3/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (54.1%, no-rel 30.4%)]
   - Group 3: **0.4346** | SPEECH BUBBLE, MUSIC NOTES, ENVELOPE, HIGHLIGHTER                 | INCORRECT (Max overlap: 3/4 with ICONS ON AN IPHONE) | [Pred Type: SEMANTIC_SET (58.2%, no-rel 20.9%)]
   - Group 4: **0.3878** | BLUSH, FOUNDATION, HOLDER, POWDER                                 | INCORRECT (Max overlap: 3/4 with MAKEUP) | [Pred Type: FILL_IN_THE_BLANK (50.8%, no-rel 17.2%)]
   - Group 5: **0.5129** | REST, STAND, FOUNDATION, BASE                                     | INCORRECT (Max overlap: 3/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 31.1%)]
   - Group 6: **0.4148** | SCALE, ENVELOPE, HIGHLIGHTER, POWDER                              | INCORRECT (Max overlap: 2/4 with MAKEUP) | [Pred Type: SEMANTIC_SET (59.8%, no-rel 25.6%)]
   - Group 7: **0.3888** | SPEECH BUBBLE, BLUSH, MUSIC NOTES, HOLDER                         | INCORRECT (Max overlap: 2/4 with ICONS ON AN IPHONE)
   - Group 8: **0.3768** | BLUSH, SCALE, HOLDER, POWDER                                      | INCORRECT (Max overlap: 2/4 with MAKEUP)
   - Group 9: **0.4168** | BLUSH, MUSIC NOTES, HOLDER, POWDER                                | INCORRECT (Max overlap: 2/4 with MAKEUP)
   - Group 10: **0.3751** | SPEECH BUBBLE, SCALE, ENVELOPE, HIGHLIGHTER                       | INCORRECT (Max overlap: 2/4 with ICONS ON AN IPHONE) | [Pred Type: SEMANTIC_SET (64.9%, no-rel 21.1%)]
   - Group 11: **0.4053** | SCALE, ENVELOPE, HOLDER, POWDER                                   | INCORRECT (Max overlap: 1/4 with BREADTH)
   - Group 12: **0.3788** | SPEECH BUBBLE, BLUSH, MUSIC NOTES, HIGHLIGHTER                    | INCORRECT (Max overlap: 2/4 with ICONS ON AN IPHONE)
   - Group 13: **0.4860** | BLUSH, HOLDER, HIGHLIGHTER, POWDER                                | INCORRECT (Max overlap: 3/4 with MAKEUP)
   - Group 14: **0.3366** | SPEECH BUBBLE, MUSIC NOTES, SCALE, ENVELOPE                       | INCORRECT (Max overlap: 3/4 with ICONS ON AN IPHONE) | [Pred Type: SEMANTIC_SET (60.8%, no-rel 22.4%)]
   - Group 15: **0.4669** | STAND, FOUNDATION, BASE, RANGE                                    | INCORRECT (Max overlap: 2/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 30.1%)]
   - Group 16: **0.4479** | SCALE, COMPASS, SCOPE, EXTENT                                     | INCORRECT (Max overlap: 3/4 with BREADTH) | [Pred Type: SYNONYM_OR_NEAR (49.2%, no-rel 32.0%)]
   - Group 17: **0.3893** | REST, BLUSH, HOLDER, POWDER                                       | INCORRECT (Max overlap: 2/4 with OBJECT USED FOR SUPPORT) | [Pred Type: FILL_IN_THE_BLANK (54.9%, no-rel 17.5%)]
   - Group 18: **0.6326** | REST, STAND, BASE, RANGE                                          | INCORRECT (Max overlap: 3/4 with OBJECT USED FOR SUPPORT) | [Pred Type: SYNONYM_OR_NEAR (54.1%, no-rel 36.4%)]
   - Group 19: **0.4533** | SPEECH BUBBLE, BLUSH, HOLDER, POWDER                              | INCORRECT (Max overlap: 2/4 with MAKEUP)
   - Group 20: **0.3436** | MUSIC NOTES, SCALE, ENVELOPE, HIGHLIGHTER                         | INCORRECT (Max overlap: 2/4 with ICONS ON AN IPHONE) | [Pred Type: SEMANTIC_SET (62.5%, no-rel 22.0%)]

---

## Puzzle 107 (ID: 49)
**Words on Board:** DAFFY, WACKY, NEPHEW, ALARM, GRANDFATHER, SCROOGE, BIOLOGICAL, DEWEY, AUNT, DONALD, DAISY, CUCKOO, COUSIN, QUIRKY, KOOKY, MOTHER

### Ground Truth Categories:
* **Level 0 (RELATIVES) [Type: SEMANTIC_SET]:** AUNT, COUSIN, MOTHER, NEPHEW
* **Level 1 (SYNONYMS FOR OFFBEAT) [Type: SYNONYM_OR_NEAR]:** DAFFY, KOOKY, QUIRKY, WACKY
* **Level 2 (DISNEY DUCKS) [Type: NAMED_ENTITY_SET]:** DAISY, DEWEY, DONALD, SCROOGE
* **Level 3 (___ CLOCK) [Type: FILL_IN_THE_BLANK]:** ALARM, BIOLOGICAL, CUCKOO, GRANDFATHER

### Top Candidate Partitions:
1. **Partition Score: 0.5038**
   - Group 1: **0.6320** | NEPHEW, GRANDFATHER, AUNT, MOTHER                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 2: **0.5970** | WACKY, BIOLOGICAL, QUIRKY, KOOKY                                  | INCORRECT (Max overlap: 3/4 with SYNONYMS FOR OFFBEAT) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 28.8%)]
   - Group 3: **0.5395** | DAFFY, SCROOGE, DEWEY, DONALD                                     | INCORRECT (Max overlap: 3/4 with DISNEY DUCKS)
   - Group 4: **0.4393** | ALARM, DAISY, CUCKOO, COUSIN                                      | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
2. **Partition Score: 0.4975**
   - Group 1: **0.6776** | GRANDFATHER, AUNT, COUSIN, MOTHER                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 2: **0.5970** | WACKY, BIOLOGICAL, QUIRKY, KOOKY                                  | INCORRECT (Max overlap: 3/4 with SYNONYMS FOR OFFBEAT) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 28.8%)]
   - Group 3: **0.5395** | DAFFY, SCROOGE, DEWEY, DONALD                                     | INCORRECT (Max overlap: 3/4 with DISNEY DUCKS)
   - Group 4: **0.4267** | NEPHEW, ALARM, DAISY, CUCKOO                                      | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
3. **Partition Score: 0.4898**
   - Group 1: **0.6320** | NEPHEW, GRANDFATHER, AUNT, MOTHER                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 2: **0.5970** | WACKY, BIOLOGICAL, QUIRKY, KOOKY                                  | INCORRECT (Max overlap: 3/4 with SYNONYMS FOR OFFBEAT) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 28.8%)]
   - Group 3: **0.5559** | DAFFY, DEWEY, DONALD, DAISY                                       | INCORRECT (Max overlap: 3/4 with DISNEY DUCKS)
   - Group 4: **0.4031** | ALARM, SCROOGE, CUCKOO, COUSIN                                    | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
4. **Partition Score: 0.4844**
   - Group 1: **0.6776** | GRANDFATHER, AUNT, COUSIN, MOTHER                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 2: **0.5970** | WACKY, BIOLOGICAL, QUIRKY, KOOKY                                  | INCORRECT (Max overlap: 3/4 with SYNONYMS FOR OFFBEAT) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 28.8%)]
   - Group 3: **0.5559** | DAFFY, DEWEY, DONALD, DAISY                                       | INCORRECT (Max overlap: 3/4 with DISNEY DUCKS)
   - Group 4: **0.3922** | NEPHEW, ALARM, SCROOGE, CUCKOO                                    | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
5. **Partition Score: 0.4773**
   - Group 1: **0.5970** | WACKY, BIOLOGICAL, QUIRKY, KOOKY                                  | INCORRECT (Max overlap: 3/4 with SYNONYMS FOR OFFBEAT) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 28.8%)]
   - Group 2: **0.5395** | DAFFY, SCROOGE, DEWEY, DONALD                                     | INCORRECT (Max overlap: 3/4 with DISNEY DUCKS)
   - Group 3: **0.5300** | ALARM, GRANDFATHER, AUNT, MOTHER                                  | INCORRECT (Max overlap: 2/4 with ___ CLOCK) | [Pred Type: SEMANTIC_SET (52.5%, no-rel 19.1%)]
   - Group 4: **0.4198** | NEPHEW, DAISY, CUCKOO, COUSIN                                     | INCORRECT (Max overlap: 2/4 with RELATIVES)

### Top Candidate Groups:
   - Group 1: **0.6320** | NEPHEW, GRANDFATHER, AUNT, MOTHER                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 2: **0.5970** | WACKY, BIOLOGICAL, QUIRKY, KOOKY                                  | INCORRECT (Max overlap: 3/4 with SYNONYMS FOR OFFBEAT) | [Pred Type: SYNONYM_OR_NEAR (48.1%, no-rel 28.8%)]
   - Group 3: **0.5395** | DAFFY, SCROOGE, DEWEY, DONALD                                     | INCORRECT (Max overlap: 3/4 with DISNEY DUCKS)
   - Group 4: **0.4393** | ALARM, DAISY, CUCKOO, COUSIN                                      | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
   - Group 5: **0.6776** | GRANDFATHER, AUNT, COUSIN, MOTHER                                 | INCORRECT (Max overlap: 3/4 with RELATIVES)
   - Group 6: **0.4267** | NEPHEW, ALARM, DAISY, CUCKOO                                      | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
   - Group 7: **0.5559** | DAFFY, DEWEY, DONALD, DAISY                                       | INCORRECT (Max overlap: 3/4 with DISNEY DUCKS)
   - Group 8: **0.4031** | ALARM, SCROOGE, CUCKOO, COUSIN                                    | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
   - Group 9: **0.3922** | NEPHEW, ALARM, SCROOGE, CUCKOO                                    | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
   - Group 10: **0.5300** | ALARM, GRANDFATHER, AUNT, MOTHER                                  | INCORRECT (Max overlap: 2/4 with ___ CLOCK) | [Pred Type: SEMANTIC_SET (52.5%, no-rel 19.1%)]
   - Group 11: **0.4198** | NEPHEW, DAISY, CUCKOO, COUSIN                                     | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 12: **0.4433** | ALARM, SCROOGE, DAISY, CUCKOO                                     | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
   - Group 13: **0.4316** | DAFFY, DEWEY, DONALD, COUSIN                                      | INCORRECT (Max overlap: 2/4 with DISNEY DUCKS)
   - Group 14: **0.4304** | DAFFY, NEPHEW, DEWEY, DONALD                                      | INCORRECT (Max overlap: 2/4 with DISNEY DUCKS)
   - Group 15: **0.5391** | WACKY, AUNT, QUIRKY, KOOKY                                        | INCORRECT (Max overlap: 3/4 with SYNONYMS FOR OFFBEAT) | [Pred Type: SYNONYM_OR_NEAR (53.5%, no-rel 29.1%)]
   - Group 16: **0.5012** | GRANDFATHER, BIOLOGICAL, COUSIN, MOTHER                           | INCORRECT (Max overlap: 2/4 with ___ CLOCK)
   - Group 17: **0.4019** | NEPHEW, SCROOGE, CUCKOO, COUSIN                                   | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 18: **0.4717** | NEPHEW, GRANDFATHER, BIOLOGICAL, MOTHER                           | INCORRECT (Max overlap: 2/4 with RELATIVES)
   - Group 19: **0.4832** | DAFFY, SCROOGE, DEWEY, CUCKOO                                     | INCORRECT (Max overlap: 2/4 with DISNEY DUCKS)
   - Group 20: **0.3992** | ALARM, DONALD, DAISY, COUSIN                                      | INCORRECT (Max overlap: 2/4 with DISNEY DUCKS)

---

## Puzzle 108 (ID: 775)
**Words on Board:** SECRET, FAIR, IN, OK, BED, MA, PRIVATE, BALL, BEE, OUT, OH, FOUL, QUIET, MUM, MARY, MOTHER

### Ground Truth Categories:
* **Level 0 (HUSH-HUSH) [Type: SYNONYM_OR_NEAR]:** MUM, PRIVATE, QUIET, SECRET
* **Level 1 (STATE ABBREVIATIONS) [Type: NAMED_ENTITY_SET]:** IN, MA, OH, OK
* **Level 2 (BASEBALL CALLS) [Type: SEMANTIC_SET]:** BALL, FAIR, FOUL, OUT
* **Level 3 (QUEEN ___) [Type: FILL_IN_THE_BLANK]:** BED, BEE, MARY, MOTHER

### Top Candidate Partitions:
1. **Partition Score: 0.4315**
   - Group 1: **0.6977** | MA, MUM, MARY, MOTHER                                             | INCORRECT (Max overlap: 2/4 with QUEEN ___)
   - Group 2: **0.5848** | SECRET, PRIVATE, OUT, QUIET                                       | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 35.8%)]
   - Group 3: **0.3862** | FAIR, BALL, BEE, FOUL                                             | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SEMANTIC_SET (52.8%, no-rel 28.2%)]
   - Group 4: **0.3775** | IN, OK, BED, OH                                                   | INCORRECT (Max overlap: 3/4 with STATE ABBREVIATIONS) | [Pred Type: SYNONYM_OR_NEAR (46.5%, no-rel 30.6%)]
2. **Partition Score: 0.4045**
   - Group 1: **0.6977** | MA, MUM, MARY, MOTHER                                             | INCORRECT (Max overlap: 2/4 with QUEEN ___)
   - Group 2: **0.4729** | SECRET, FAIR, PRIVATE, QUIET                                      | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 34.8%)]
   - Group 3: **0.3901** | BALL, BEE, OUT, FOUL                                              | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SEMANTIC_SET (47.6%, no-rel 29.4%)]
   - Group 4: **0.3775** | IN, OK, BED, OH                                                   | INCORRECT (Max overlap: 3/4 with STATE ABBREVIATIONS) | [Pred Type: SYNONYM_OR_NEAR (46.5%, no-rel 30.6%)]
3. **Partition Score: 0.4044**
   - Group 1: **0.6977** | MA, MUM, MARY, MOTHER                                             | INCORRECT (Max overlap: 2/4 with QUEEN ___)
   - Group 2: **0.5102** | FAIR, BALL, OUT, FOUL                                             | CORRECT GROUP (BASEBALL CALLS, Level 2)
   - Group 3: **0.3775** | IN, OK, BED, OH                                                   | INCORRECT (Max overlap: 3/4 with STATE ABBREVIATIONS) | [Pred Type: SYNONYM_OR_NEAR (46.5%, no-rel 30.6%)]
   - Group 4: **0.3650** | SECRET, PRIVATE, BEE, QUIET                                       | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 28.9%)]
4. **Partition Score: 0.4038**
   - Group 1: **0.6977** | MA, MUM, MARY, MOTHER                                             | INCORRECT (Max overlap: 2/4 with QUEEN ___)
   - Group 2: **0.5659** | SECRET, IN, PRIVATE, OUT                                          | INCORRECT (Max overlap: 2/4 with HUSH-HUSH)
   - Group 3: **0.3862** | FAIR, BALL, BEE, FOUL                                             | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SEMANTIC_SET (52.8%, no-rel 28.2%)]
   - Group 4: **0.3315** | OK, BED, OH, QUIET                                                | INCORRECT (Max overlap: 2/4 with STATE ABBREVIATIONS)
5. **Partition Score: 0.4023**
   - Group 1: **0.6977** | MA, MUM, MARY, MOTHER                                             | INCORRECT (Max overlap: 2/4 with QUEEN ___)
   - Group 2: **0.4819** | IN, OK, BED, OUT                                                  | INCORRECT (Max overlap: 2/4 with STATE ABBREVIATIONS)
   - Group 3: **0.3862** | FAIR, BALL, BEE, FOUL                                             | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SEMANTIC_SET (52.8%, no-rel 28.2%)]
   - Group 4: **0.3706** | SECRET, PRIVATE, OH, QUIET                                        | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 33.0%)]

### Top Candidate Groups:
   - Group 1: **0.6977** | MA, MUM, MARY, MOTHER                                             | INCORRECT (Max overlap: 2/4 with QUEEN ___)
   - Group 2: **0.5848** | SECRET, PRIVATE, OUT, QUIET                                       | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (56.1%, no-rel 35.8%)]
   - Group 3: **0.3862** | FAIR, BALL, BEE, FOUL                                             | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SEMANTIC_SET (52.8%, no-rel 28.2%)]
   - Group 4: **0.3775** | IN, OK, BED, OH                                                   | INCORRECT (Max overlap: 3/4 with STATE ABBREVIATIONS) | [Pred Type: SYNONYM_OR_NEAR (46.5%, no-rel 30.6%)]
   - Group 5: **0.4729** | SECRET, FAIR, PRIVATE, QUIET                                      | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 34.8%)]
   - Group 6: **0.3901** | BALL, BEE, OUT, FOUL                                              | INCORRECT (Max overlap: 3/4 with BASEBALL CALLS) | [Pred Type: SEMANTIC_SET (47.6%, no-rel 29.4%)]
   - Group 7: **0.5102** | FAIR, BALL, OUT, FOUL                                             | CORRECT GROUP (BASEBALL CALLS, Level 2)
   - Group 8: **0.3650** | SECRET, PRIVATE, BEE, QUIET                                       | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (63.1%, no-rel 28.9%)]
   - Group 9: **0.5659** | SECRET, IN, PRIVATE, OUT                                          | INCORRECT (Max overlap: 2/4 with HUSH-HUSH)
   - Group 10: **0.3315** | OK, BED, OH, QUIET                                                | INCORRECT (Max overlap: 2/4 with STATE ABBREVIATIONS)
   - Group 11: **0.4819** | IN, OK, BED, OUT                                                  | INCORRECT (Max overlap: 2/4 with STATE ABBREVIATIONS)
   - Group 12: **0.3706** | SECRET, PRIVATE, OH, QUIET                                        | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (58.0%, no-rel 33.0%)]
   - Group 13: **0.4720** | SECRET, BED, PRIVATE, QUIET                                       | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (58.6%, no-rel 33.7%)]
   - Group 14: **0.3724** | FAIR, IN, OK, OH                                                  | INCORRECT (Max overlap: 3/4 with STATE ABBREVIATIONS)
   - Group 15: **0.4276** | SECRET, BED, PRIVATE, OUT                                         | INCORRECT (Max overlap: 2/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (57.8%, no-rel 30.2%)]
   - Group 16: **0.3886** | IN, OK, OH, QUIET                                                 | INCORRECT (Max overlap: 3/4 with STATE ABBREVIATIONS)
   - Group 17: **0.4107** | SECRET, PRIVATE, OUT, FOUL                                        | INCORRECT (Max overlap: 2/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (57.0%, no-rel 31.7%)]
   - Group 18: **0.3845** | FAIR, BED, BALL, BEE                                              | INCORRECT (Max overlap: 2/4 with BASEBALL CALLS)
   - Group 19: **0.3507** | IN, OK, OUT, OH                                                   | INCORRECT (Max overlap: 3/4 with STATE ABBREVIATIONS)
   - Group 20: **0.4029** | SECRET, PRIVATE, FOUL, QUIET                                      | INCORRECT (Max overlap: 3/4 with HUSH-HUSH) | [Pred Type: SYNONYM_OR_NEAR (58.8%, no-rel 33.7%)]

---
