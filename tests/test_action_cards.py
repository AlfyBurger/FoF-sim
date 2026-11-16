"""Checks on data/action_cards.json: structure, and the worked examples in the official books."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "data", "action_cards.json")))["cards"]}


def test_fifty_cards():
    assert sorted(CARDS) == list(range(1, 51))


def test_random_number_rows_are_monotonic_and_in_range():
    for N in range(2, 13):
        col = [CARDS[n]["rn"][str(N)] for n in range(1, 51)]
        assert all(1 <= v <= N for v in col)
        assert col == sorted(col), N
        assert set(col) == set(range(1, N + 1)), N


def test_combat_table_shape():
    # results only get milder as the modifier rises: HIT... PIN... MISS
    rank = {"H": 0, "P": 1, "M": 2}
    for c in CARDS.values():
        seq = [rank[c["combat"][str(m)]] for m in range(-4, 7)]
        assert seq == sorted(seq), c["id"]


def test_fm1_pac_run1_draws():
    # Field Manual 1, Platoon Assault Course Run 1 walkthrough (pp. 9-14)
    ex = [(30, "activated", 3), (25, "initiative", 2), (24, "activated", 4), (27, "initiative", 2),
          (11, "activated", 4), (16, "initiative", 3), (23, "activated", 4), (13, "initiative", 3),
          (3, "activated", 5), (18, "initiative", 2)]
    for n, f, v in ex:
        assert CARDS[n][f] == v, (n, f)


def test_fm1_pac_run2_r3_and_run3_draws():
    assert CARDS[25]["rn"]["3"] == 2      # FM1 Run 3: card #25, column 3 -> 2
    assert CARDS[31]["initiative"] == 2   # FM1: card #31 initiative 2
    assert CARDS[1]["activated"] == 6     # FM1 Run 3: card #1 helmet 6
