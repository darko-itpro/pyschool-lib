def load_students_list() -> list[str]:
    """
    :return: a list of students names
    """
    return ['Agnan', 'Alceste', 'Clotaire', 'Eudes', 'Geoffroy', 'Joachim', 'Maixent', 'Nicolas', 'Rufus']

def load_grades(course:str) -> list[int]:
    """
    :param course: name of the course, can be either "math" or "english". Any other value raises an exception.
    :return: a list of grades.
    """
    if course == "math":
        return [20, 15, 2, 17, 15, 6, 9, 12, 14]
    elif course == "english":
        return [19, 14, 3, 15, 8, 12, 13, 14, 16]
    else:
        raise ValueError("No course found")