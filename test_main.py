import pytest

import main

test_data = [
    (350, 'A*'),
    (264, 'A*'),
    (228, 'B'),
    (229, 'A'),
    (0, 'U')
]


@pytest.mark.parametrize("mark, grade", test_data)
def test_correct_grades(mark, grade):
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
    assert main.calc_grades(mark, grade_boundaries) == grade


def test_invalid_grade_boundaries():
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

    with pytest.raises(ValueError):
        main.calc_grades(0, silly_grade_boundaries)


def test_invalid_values():
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

    # Too big

    with pytest.raises(ValueError):
        main.calc_grades(500, grade_boundaries)

    # Too negative

    with pytest.raises(ValueError):
        main.calc_grades(-1, grade_boundaries)

    # Wrong type

    with pytest.raises(TypeError):
        main.calc_grades('A', grade_boundaries)  # type:ignore
