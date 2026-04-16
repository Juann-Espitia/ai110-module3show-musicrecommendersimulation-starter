# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder 1.0 suggests songs from a small catalog based on a user's preferred genre, mood, and energy level. It is a classroom simulation — not designed for production use or real users. Its purpose is to demonstrate how content-based filtering works by making every scoring decision visible and explainable.

**Non-intended use:** This system should not be used to make real listening decisions for real users. The dataset is too small, the feature set is too narrow, and there is no mechanism for learning from feedback.

---

## 3. How the Model Works

Imagine you walk into a record store and tell the clerk: "I want something pop, happy, and high-energy." The clerk goes through every record, gives it points based on how well it matches, and hands you the top five.

That is exactly what VibeFinder does. For each song in the catalog it asks three questions:

1. Does the genre match what the user said they like? If yes, add 2 points.
2. Does the mood match? If yes, add 1 point.
3. How close is the song's energy to what the user wants? The closer it is, the more points it gets (up to 1 point).

Then it sorts all songs from highest score to lowest and returns the top results with a plain-English explanation of why each song ranked where it did.

Genre is weighted the most (2 points) because it represents the broadest musical identity. Mood is worth 1 point because it shapes the emotional feel. Energy is a continuous score so it rewards any song that is in the right neighborhood, not just an exact match.

---

## 4. Data

- **Catalog size:** 18 songs (10 starter + 8 added)
- **Genres represented:** pop, lofi, rock, ambient, jazz, synthwave, indie pop, country, hip-hop, classical, blues, funk, metal, r&b, reggae
- **Moods represented:** happy, chill, intense, relaxed, moody, focused, peaceful, melancholic, romantic
- **Features per song:** genre, mood, energy (0–1), tempo_bpm, valence, danceability, acousticness
- **Added songs:** 8 new tracks to improve genre and mood diversity — including classical, blues, metal, funk, r&b, reggae, country, and hip-hop entries that were missing from the starter set
- **Limitation:** Most genres have only one representative song, so any user whose favorite genre is not pop, lofi, or rock will get very few genre matches

---

## 5. Strengths

- **Transparent:** Every recommendation comes with a human-readable reason — no black box.
- **Predictable:** For mainstream profiles (pop-happy-high energy, lofi-chill-low energy), the top result is exactly what you would expect and it earns it with a near-perfect score.
- **Fast:** Scoring 18 songs takes milliseconds with no external dependencies beyond the standard library.
- **Diverse catalog:** Adding 8 songs meant profiles like "classical" or "blues" are no longer completely unsatisfied.

---

## 6. Limitations and Bias

The system's most significant weakness is **genre over-dominance**. Genre accounts for 2 out of a maximum ~4 points, meaning a wrong-genre song can never beat a right-genre song even if it is a perfect energy and mood match. This creates a filter bubble where users are almost never surprised by a different-genre recommendation.

A second limitation is **string equality for categorical features**. "indie pop" and "pop" are treated as completely different genres even though they share most musical characteristics. A user who enters "pop" will never match "indie pop" songs.

Third, the dataset skews toward certain genres. Even after expansion, pop and lofi each have multiple songs while metal, classical, and blues each have only one. A metal fan will always see other-genre songs filling spots 2 through 5.

Finally, the system ignores **tempo, valence, and danceability** entirely in scoring, even though these features could meaningfully differentiate between "intense EDM" and "intense rock."

---

## 7. Evaluation

**Profiles tested:**
1. High-Energy Pop Fan (`genre: pop, mood: happy, energy: 0.85`)
2. Chill Lofi Student (`genre: lofi, mood: chill, energy: 0.38`)
3. Deep Intense Rocker (`genre: rock, mood: intense, energy: 0.92`)

**What I looked for:** Whether the top result made intuitive sense, and whether the score gap between #1 and #2 revealed anything about the system's sensitivity.

**What surprised me:** The Rocker profile ranked "Gym Hero" (pop, intense) #2 — above metal and hip-hop songs — purely because its energy (0.93) was almost identical to the user's target (0.92). A real rock fan would find a pop song an odd recommendation. This confirms the genre weight is not strong enough to keep out near-energy-match songs from other genres.

**Experiment — weight shift:** Doubling the energy weight shifted the Chill Lofi #4 and #5 rankings but did not change the top 3. The top spots are locked in when all three features match, regardless of weight adjustments.

---

## 8. Future Work

1. **Add tempo range scoring** — reward songs whose BPM falls within a user's preferred range, not just songs with a matching energy level.
2. **Genre family mapping** — group "indie pop," "synth pop," and "pop" under a shared parent so partial genre matches earn partial points.
3. **Diversity injection** — after scoring, ensure the top-5 list includes at least two different genres so the system does not always return a single-genre echo chamber.
4. **Valence and danceability weights** — incorporate these features to distinguish between "intense but danceable" (EDM) and "intense but dark" (metal), which currently score identically.

---

## 9. Personal Reflection

The biggest learning moment was discovering how much power a single weight number has. Setting genre to 2.0 versus 1.5 completely changes who gets recommended what. Real AI systems have the same problem at a much larger scale — tiny tuning decisions made by engineers end up shaping what millions of people listen to, watch, or buy.

Using AI tools sped up the boilerplate (CSV parsing, sorted() syntax) but I had to verify every piece of scoring logic manually because the AI occasionally suggested approaches that looked correct but would have produced the wrong ranking order. Human judgment was essential for catching those subtle bugs.

What surprised me most is how a four-line scoring function can produce results that *feel* like recommendations. When the pop-happy-high-energy profile returns "Sunrise City" at the top with a score of 3.97, it genuinely feels right — not because the algorithm is smart, but because the features it checks happen to align with the human intuition of "pop + happy + high energy = Sunrise City." That illusion of intelligence is exactly what makes simple recommender systems both powerful and dangerous when scaled up without oversight.

If I extended this project, I would add a feedback loop: after a user skips or likes a recommendation, the weights update automatically. That is the bridge between content-based filtering and the reinforcement-learning approaches that real platforms use.
