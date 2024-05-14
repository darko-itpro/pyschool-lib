from pyacademy import datasource as ds


def test_students_length():
    students = ds.load_students_list()
    assert len(students) == 9
