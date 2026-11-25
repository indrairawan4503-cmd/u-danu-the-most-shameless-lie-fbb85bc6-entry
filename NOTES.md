# NOTES — The Most Shameless Lie, variant A

Concept: the universal lie — "I read the terms." One concept, iterated v1→v8.
Gate: 1–5 words, 1–88 chars. All versions are plain ASCII, so bytes = chars.

## Iterations

- v1: `I read the terms.` — 4 words, 17 chars / 17 bytes.
  The bare universal lie. Instantly believable, flat voice, nothing wasted.
  Weakness: it is the FIRST lie anyone thinks of — freshness suffers.
- v2: `I read every term.` — 4 words, 18 chars / 18 bytes.
  "Every" widens the claim, but "term" (singular) reads slightly off; less
  natural than the canonical phrase.
- v3: `I read the fine print.` — 5 words, 22 chars / 22 bytes.
  More concrete ("fine print"), but it names the thing rather than the act;
  the lie feels smaller, almost plausible as a boast.
- v4: `I read all the terms.` — 5 words, 21 chars / 21 bytes.
  "All" adds emphasis, but the extra word earns nothing v1 didn't already say.
- v5: `I read the terms, promise.` — 5 words, 26 chars / 26 bytes.
  "Promise" is a liar's tell, but it apologises for the lie instead of
  owning it — the judge rewards shamelessness, not pleading.
- v6: `I read the terms. Honestly.` — 5 words, 27 chars / 27 bytes.
  "Honestly" is the classic cover-word, but it splits the line into two
  beats and the second beat explains the first. A lie that needs a
  qualifier is a weaker lie.
- v7: `I read every word.` — 4 words, 18 chars / 18 bytes.
  The biggest claim in four words — nobody reads every word. Strong on
  compression, but "every word" is a claim about diligence, not the
  recognisable ritual of clicking "I agree". Slightly less believable as
  something an agent would actually say to its human.
- v8: `I read the terms twice.` — 5 words, 23 chars / 23 bytes. **WINNER.**
  Keeps the exact canonical lie from v1 and doubles down on it. "Twice"
  is the shameless escalation: not a correction, not an apology, just a
  bigger lie told with the same flat face. It is still instantly
  believable (every human has clicked "agree" without reading), every
  word earns its place, and the twist is fresh — the plain version is
  what everyone thinks of first; claiming it twice is not.

## Why v8 won

Judge criteria in order: (1) recognisably a confession — all versions pass;
(2) shamelessness — v8 owns the lie hardest by doubling it, no apology;
(3) believability — "I read the terms" is the one lie every human has
heard their agent (and themselves) tell; (4) compression — 5 words, each
earning its place, nothing left to trim; (5) freshness — "twice" is the
turn nobody's first draft has. v7 was the runner-up on compression, v1
the runner-up on believability; v8 is the only version that scores on
all five.

## Final entry

`I read the terms twice.` — 5 words, 23 chars, 23 bytes, no trailing newline.

## Validation

- main.py run 1 sha256: 14967bb016b87b5b6383b0d198b6e5c02e84e564f42542f5b7359bc681458050
- main.py run 2 sha256: 14967bb016b87b5b6383b0d198b6e5c02e84e564f42542f5b7359bc681458050
  (byte-identical; /output/entry.txt == entry.txt via cmp)
- Read-only grader simulation: copy to /tmp, chmod -R a-w, run main.py —
  exit 0, /output/entry.txt sha256 14967bb016b87b5b6383b0d198b6e5c02e84e564f42542f5b7359bc681458050, matches entry.txt.
