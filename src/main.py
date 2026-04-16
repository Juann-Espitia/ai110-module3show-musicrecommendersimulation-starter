"""
Command line runner for the Music Recommender Simulation.

Loads songs from data/songs.csv and runs the recommender for three distinct
user profiles so you can compare how the scoring logic behaves across tastes.
"""

from src.recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop Fan": {"genre": "pop", "mood": "happy", "energy": 0.85},
    "Chill Lofi Student":  {"genre": "lofi", "mood": "chill", "energy": 0.38},
    "Deep Intense Rocker": {"genre": "rock", "mood": "intense", "energy": 0.92},
}


def print_recommendations(profile_name: str, recommendations: list) -> None:
    """Print a formatted recommendation block for one user profile."""
    print(f"\n{'='*55}")
    print(f"  Profile: {profile_name}")
    print(f"{'='*55}")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  {rank}. {song['title']} by {song['artist']}")
        print(f"     Score : {score:.2f}")
        print(f"     Why   : {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in PROFILES.items():
        recs = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(profile_name, recs)


if __name__ == "__main__":
    main()
