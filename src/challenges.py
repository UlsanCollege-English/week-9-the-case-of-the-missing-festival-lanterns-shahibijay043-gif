def analyze_lanterns(expected_lanterns, lantern_log, correct_sections):

    seen_lanterns = set()
    duplicate_lanterns = set()
    count_by_section = {}
    wrong_section_lanterns = {}

    for lantern_name, actual_section in lantern_log:

        # seen lanterns
        if lantern_name in seen_lanterns:
            duplicate_lanterns.add(lantern_name)
        seen_lanterns.add(lantern_name)

        # count sections
        if actual_section not in count_by_section:
            count_by_section[actual_section] = 0
        count_by_section[actual_section] += 1

        # wrong section check
        if lantern_name in expected_lanterns:
            correct = correct_sections[lantern_name]
            if actual_section != correct:
                if lantern_name not in wrong_section_lanterns:
                    wrong_section_lanterns[lantern_name] = {
                        "expected": correct,
                        "actual": actual_section
                    }

    missing_lanterns = expected_lanterns - seen_lanterns
    unexpected_lanterns = seen_lanterns - expected_lanterns

    return {
        "seen_lanterns": seen_lanterns,
        "missing_lanterns": missing_lanterns,
        "unexpected_lanterns": unexpected_lanterns,
        "duplicate_lanterns": duplicate_lanterns,
        "count_by_section": count_by_section,
        "wrong_section_lanterns": wrong_section_lanterns
    }