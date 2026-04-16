# Reflection

## Profile Comparisons

### High-Energy Pop Fan vs. Chill Lofi Student

These two profiles produce almost perfectly opposite results. The pop fan's top song (Sunrise City, energy 0.82) would feel frenetic to the lofi student, whose top song (Library Rain, energy 0.35) would sound almost silent to the pop fan. Both profiles earned a near-perfect score of 3.97 because both had a song that matched all three criteria — genre, mood, and energy — simultaneously. This tells us the scoring system is working as designed: when everything aligns, the system is confident. When nothing aligns (like a lofi fan getting jazz as their #5), the system is essentially guessing by energy alone.

### Chill Lofi Student vs. Deep Intense Rocker

The structural difference here is stark. The lofi student's recommendations cluster between energy 0.28–0.42, all quiet and slow. The rocker's recommendations cluster between energy 0.88–0.96, all loud and fast. What is interesting is that both profiles got a #2 song from a completely different genre — the lofi student got Spacewalk Thoughts (ambient) and the rocker got Gym Hero (pop). In both cases, the non-genre song earned its spot purely through a mood match plus near-perfect energy closeness. This reveals that genre is powerful but not absolute: a song from any genre can sneak into the top 5 if the other features align well enough.

### High-Energy Pop Fan vs. Deep Intense Rocker

Both profiles share a love of high energy (0.85 vs 0.92), but differ on genre and mood (happy vs. intense). Gym Hero (pop, intense, energy 0.93) appears in both top-5 lists — ranked #2 for the pop fan (genre match) and #2 for the rocker (mood + energy match). This is the clearest example of a song that bridges two profiles. It also highlights a potential bias: Gym Hero is essentially a "pop workout song" and might not feel right to a rock fan, but the numbers say it belongs there. The output is valid mathematically but not always musically intuitive.

## What These Comparisons Tell Us

The scoring system is consistent and transparent, but it lacks contextual nuance. Real music recommendation is partly about *flow* — the song after a loud rock track should transition naturally, not just match a genre label. Our system has no sense of sequencing or contrast. Every recommendation is evaluated in isolation, which is both the system's greatest strength (explainability) and its clearest limitation (no context-awareness).
