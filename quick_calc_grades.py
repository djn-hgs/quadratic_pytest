
def calc_grades(mark: float, grade_boundaries: dict[str, float]) -> str:
    # Get the grade

    grade_achieved = None

    for grade, boundary in grade_boundaries.items():
        if grade in ('MAX', 'MIN'):
            continue
        if mark >= boundary:
            grade_achieved = grade
            break

    return grade_achieved
