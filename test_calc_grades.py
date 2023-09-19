import pytest

import quick_calc_grades

grade_boundaries = {
    'MAX': 350,
    'A*': 264,
    'A': 229,
    'B': 189,
    'C': 150,
    'D': 111,
    'E': 72,
    'U': 0,
    'MIN': 0
}

silly_grade_boundaries = {
    'MAX': 350,
    'A*': 264,
    'A': 269,
    'B': 189,
    'C': 150,
    'D': 111,
    'E': 72,
    'U': 0,
    'MIN': 0
}

test_data = [
    (350, 'A*'),
    (264, 'A*'),
    (228, 'B'),
    (229, 'A'),
    (0, 'U')
]


@pytest.mark.parametrize("mark, grade", test_data)
def test_correct_grades(mark, grade):
    assert quick_calc_grades.calc_grades(mark, grade_boundaries) == grade


def test_invalid_grade_boundaries():
    with pytest.raises(ValueError):
        quick_calc_grades.calc_grades(0, silly_grade_boundaries)


def test_invalid_values():
    # Too big

    with pytest.raises(ValueError):
        quick_calc_grades.calc_grades(500, grade_boundaries)

    # Too negative

    with pytest.raises(ValueError):
        quick_calc_grades.calc_grades(-1, grade_boundaries)

    # Wrong type

    with pytest.raises(TypeError):
        quick_calc_grades.calc_grades('A', grade_boundaries)  # type:ignore
