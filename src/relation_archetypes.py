RELATION_ARCHETYPES = (
    "NO_RELATION",
    "SEMANTIC_SET",
    "SYNONYM_OR_NEAR",
    "NAMED_ENTITY_SET",
    "WORD_FORM",
    "SOUND_OR_SPELLING",
    "WORDPLAY_TRANSFORM",
    "FILL_IN_THE_BLANK",
    "COMMON_PHRASE",
)

RELATION_ARCHETYPE_SCHEMA_VERSION = 2
NO_RELATION_IDX = 0
DEFAULT_POSITIVE_RELATION_ARCHETYPE = "SEMANTIC_SET"
POSITIVE_RELATION_THRESHOLD = 0.45
RELATION_NO_RELATION_MARGIN = 0.10

RELATION_ARCHETYPE_TO_IDX = {
    archetype: idx for idx, archetype in enumerate(RELATION_ARCHETYPES)
}
NUM_RELATION_ARCHETYPES = len(RELATION_ARCHETYPES)

LEGACY_RELATION_ARCHETYPE_ALIASES = {
    "SYNONYM": "SYNONYM_OR_NEAR",
    "WORDPLAY": "WORDPLAY_TRANSFORM",
    "PHRASE_COMPLETION": "FILL_IN_THE_BLANK",
    "TRIVIA_ENCYCLOPEDIC": "SEMANTIC_SET",
    "MORPHOLOGY": "WORD_FORM",
}


def normalize_relation_archetype(label: str) -> str:
    """Return a current positive relation archetype for current or legacy labels."""
    if label in RELATION_ARCHETYPE_TO_IDX and label != "NO_RELATION":
        return label
    if label in LEGACY_RELATION_ARCHETYPE_ALIASES:
        return LEGACY_RELATION_ARCHETYPE_ALIASES[label]
    return DEFAULT_POSITIVE_RELATION_ARCHETYPE


def relation_prediction_from_probabilities(
    probabilities,
    positive_threshold: float = POSITIVE_RELATION_THRESHOLD,
    no_relation_margin: float = RELATION_NO_RELATION_MARGIN,
):
    """Return a positive relation index only when it clears the no-relation gate."""
    probs = list(probabilities)
    if len(probs) != NUM_RELATION_ARCHETYPES:
        raise ValueError(
            f"Expected {NUM_RELATION_ARCHETYPES} relation probabilities, got {len(probs)}"
        )

    no_relation_prob = float(probs[NO_RELATION_IDX])
    best_positive_idx = max(
        range(1, NUM_RELATION_ARCHETYPES),
        key=lambda idx: float(probs[idx]),
    )
    best_positive_prob = float(probs[best_positive_idx])
    if (
        best_positive_prob >= positive_threshold
        and best_positive_prob - no_relation_prob >= no_relation_margin
    ):
        return best_positive_idx
    return None
