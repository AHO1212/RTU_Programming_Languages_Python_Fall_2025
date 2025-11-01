import re
from typing import List, Dict, Any


def count_characters(text: str) -> int:
    """Count non-space characters."""
    return sum(1 for ch in (text or "") if not ch.isspace())


def count_words(text: str) -> int:
    """Count number of words."""
    return len((text or "").split())


def extract_numbers(text: str) -> List[int]:
    """Extract all integers (including negatives) from text."""
    if not text:
        return []
    return [int(m.group()) for m in re.finditer(r"-?\d+", text)]


def analyze_text(text: str) -> Dict[str, Any]:
    """Analyze text and return statistics."""
    nums = extract_numbers(text)
    total = sum(nums) if nums else 0
    avg = (total / len(nums)) if nums else None
    return {
        "non_space_characters": count_characters(text),
        "word_count": count_words(text),
        "numbers": nums,
        "sum": total,
        "average": avg,
    }


if __name__ == "__main__":
    t = input("Enter text: ")
    r = analyze_text(t)
    print(f"Non-space characters: {r['non_space_characters']}")
    print(f"Word count: {r['word_count']}")
    print(f"Numbers: {r['numbers']}")
    print(f"Sum of numbers: {r['sum']}")
    print(
        "Average of numbers: "
        + (f"{r['average']:.2f}" if r["average"] is not None else "N/A")
    )
