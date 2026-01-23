from collections import Counter


def checkMagazine(magazine: str, note: str) -> str:
    # Tokenize inputs into words
    maga_words = magazine.split(" ")
    note_words = note.split(" ")

    # Create hash map of words required in note
    note_wordcount = Counter(note_words)
    # Check for overlapping words between magazine and note
    for maga_word in maga_words:
        if maga_word in note_wordcount.keys():
            if note_wordcount[maga_word] == 0:
                pass
            else:
                note_wordcount[maga_word] -= 1

    # Check if all required words are in the magazine
    if sum(note_wordcount.values()) == 0:
        return "Yes"
    return "No"


def test(fn) -> None:
    case_0_magazine = "give me one grand today night"
    case_0_note = "give me one grand today"
    assert fn(case_0_magazine, case_0_note) == "Yes"

    case_1_magazine = (
        "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg"
    )
    case_1_note = "elo lxkvg bg mwz clm w"
    assert fn(case_1_magazine, case_1_note) == "Yes"


if __name__ == "__main__":
    test(checkMagazine)
