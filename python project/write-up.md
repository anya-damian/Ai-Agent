# Design Rationale: Daily Reflection Tree

## Why These Specific Questions?
The goal of this reflection tree is to gently guide the user through three psychological axes without making them feel judged. I designed the questions to move from the concrete (Axis 1) to the relational (Axis 2) and finally to the systemic (Axis 3).

- **Axis 1 (Locus of Control):** Instead of asking "Are you a victim?", the tree asks "When things got difficult, what was your first instinct?" This grounds the concept of agency in a specific, recent behavior rather than a core identity.
- **Axis 2 (Orientation):** Entitlement is often invisible to the person holding it. Asking "Were you giving or expecting?" forces a moment of pause. The options range from pure organizational citizenship ("I helped someone") to entitlement ("I expected others to do their part"). 
- **Axis 3 (Radius of Concern):** Self-transcendence requires realizing the impact of our work on the wider world. The question "who comes to mind?" isolates the user's radius of concern—whether it's just themselves, their immediate team, or the end user.

## Branching Design and Trade-offs
I used a deterministic structure with explicit `decision` nodes that route based on the exact string values of previous answers. 

**Trade-offs made:**
- **No free text:** While free text allows for deeper expression, it introduces ambiguity and requires NLP/LLMs to parse. Sticking to fixed options ensures predictable, auditable paths.
- **Simplified State:** Instead of a complex scoring algorithm, the tree accumulates `signals` (e.g., `axis1:internal`). This ensures the logic remains readable purely as data.

## Psychological Sources
1. **Locus of Control (Julian Rotter, 1954):** Informed Axis 1. Options were structured to distinguish between internal locus ("I adapted on the fly") and external locus ("Wait for someone to step in").
2. **Organizational Citizenship Behavior (Organ, 1988) vs. Psychological Entitlement (Campbell et al., 2004):** Informed Axis 2. 
3. **Self-Transcendence (Maslow, 1969):** Informed Axis 3. Moving from self-preservation to finding meaning in serving others.

## What I'd Improve With More Time
- **Dynamic Option Generation:** While the tree is static, I would use an LLM during the *authoring* phase to generate dozens of highly contextual options based on the user's role (e.g., Engineer vs. Sales).
- **Longitudinal State:** Allow the tree to remember signals from *previous days* to offer week-level insights ("You've leaned heavily on an external locus all week...").
