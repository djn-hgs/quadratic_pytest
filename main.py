
def calc_grades(mark: float, grade_boundaries: dict[str, float]) -> str:
    min_mark = grade_boundaries['MIN']
    max_mark = grade_boundaries['MAX']

    # Test that the data is monotone
    last_value = None

    for grade, boundary in grade_boundaries.items():
        if last_value:
            if boundary > last_value:
                raise ValueError(f'Grade boundaries should be in descending order:\n{grade_boundaries}')
            else:
                last_value = boundary
        else:
            last_value = boundary

    # Check that the mark is a float
    if not isinstance(mark, (int, float)):
        raise TypeError(f'Can only return grades for scores of type {float}')

    # Check that the mark is in range

    if mark < min_mark:
        raise ValueError(f'{mark} is below minimum mark {min_mark}')
    if mark > max_mark:
        raise ValueError(f'{mark} is above maximum mark {max_mark}')

    # Get the grade

    grade_achieved = None

    for grade, boundary in grade_boundaries.items():
        if grade in ('MAX', 'MIN'):
            continue
        if mark >= boundary:
            grade_achieved = grade
            break

    if grade_achieved:
        return grade_achieved
    else:
        raise ValueError(f'{mark} does not have an associated grade.')
