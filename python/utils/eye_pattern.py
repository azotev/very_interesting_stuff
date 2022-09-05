#!/usr/bin/env python3

from typing import Tuple, List

EyePattern = Tuple[str, str, str, str, str]

EYE_PATTERN_1: EyePattern = (
  "/---\\",
  "|   |",
  "|-o-|",
  "|   |",
  "\\---/"
)

EYE_PATTERN_2: EyePattern = (
  "/---\\",
  "| | |",
  "| 0 |",
  "| | |",
  "\\---/"
)

EYE_PATTERN_3: EyePattern = (
  "/---\\",
  "| | |",
  "|-q-|",
  "| | |",
  "\\---/"
)

EYE_PATTERN_4: EyePattern = (
  "/---\\",
  "|\\ /|",
  "| w |",
  "|/ \\|",
  "\\---/"
)

EYE_PATTERNS_SIZE = 5

EYE_PATTERNS: List[Tuple[EyePattern, int]] = [
    (EYE_PATTERN_4, sum([not x.isspace() for row in EYE_PATTERN_4 for x in row])),
    (EYE_PATTERN_3, sum([not x.isspace() for row in EYE_PATTERN_3 for x in row])),
    (EYE_PATTERN_2, sum([not x.isspace() for row in EYE_PATTERN_2 for x in row])),
    (EYE_PATTERN_1, sum([not x.isspace() for row in EYE_PATTERN_1 for x in row]))
]
