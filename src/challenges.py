from __future__ import annotations


def analyze_lanterns(
    expected_lanterns: set[str],
    lantern_log: list[tuple[str, str]],
    correct_sections: dict[str, str],
) -> dict[str, object]:

    seen_lanterns: set[str] = set()
    duplicate_lanterns: set[str] = set()

    count_by_section: dict[str, int] = {}

    wrong_section_lanterns: dict[str, dict[str, str]] = {}

    for lantern_name, actual_section in lantern_log:

        if lantern_name in seen_lanterns:
            duplicate_lanterns.add(lantern_name)

        seen_lanterns.add(lantern_name)

        count_by_section[actual_section] = (
            count_by_section.get(actual_section, 0) + 1
        )

        if lantern_name in correct_sections:

            expected_section = correct_sections[lantern_name]

            if actual_section != expected_section:

                wrong_section_lanterns[lantern_name] = {
                    "expected": expected_section,
                    "actual": actual_section,
                }

    missing_lanterns = (
        expected_lanterns - seen_lanterns
    )

    unexpected_lanterns = (
        seen_lanterns - expected_lanterns
    )

    return {
        "seen_lanterns": seen_lanterns,
        "missing_lanterns": missing_lanterns,
        "unexpected_lanterns": unexpected_lanterns,
        "duplicate_lanterns": duplicate_lanterns,
        "count_by_section": count_by_section,
        "wrong_section_lanterns": wrong_section_lanterns,
    }