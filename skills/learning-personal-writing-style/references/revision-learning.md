# 从改稿中学习规则

Use this when the user provides AI draft vs user-edited draft, or asks the skill to become more like them.

## Compare in layers

1. **Title**: Did the user make it more direct, restrained, suspenseful, official, or concrete?
2. **Opening**: Did the user remove background, add a hook, add context, or state the conclusion earlier?
3. **Structure**: Did the user reorder points, merge sections, split paragraphs, or add hierarchy?
4. **Evidence**: Did the user add examples, data, policy basis, lived detail, or reader scenarios?
5. **Tone**: Did the user soften, sharpen, reduce emotion, add authority, or remove AI smoothness?
6. **Language**: Which words were replaced? Which phrases were deleted?
7. **Ending**: Did the user add a call to action, practical summary, formal closing, or reflective note?

## Convert edits into rules

Use this format:

```markdown
## Revision Rule

- Trigger: When the draft ...
- Preferred change: Do ...
- Avoid: Do not ...
- Example before: ...
- Example after: ...
- Confidence: low / medium / high
```

## High-value edit patterns

- Deleting generic openings such as `在当今时代`.
- Replacing abstract praise with concrete action.
- Adding first-person uncertainty or lived detail.
- Moving the conclusion to the first three sentences.
- Turning long paragraphs into one-point paragraphs.
- Replacing policy-sounding filler with actual mechanisms.
- Reducing exaggerated adjectives.
- Changing a broad title into a promise, question, or concrete contradiction.

## Update policy

- Add a rule after one strong edit if it is highly diagnostic.
- Raise confidence after the same pattern appears in 3+ edits.
- Retire a rule if newer edits contradict it across multiple samples.
- Keep genre-specific rules separate from general voice rules.
