import Student_Classroom
from io import StringIO
import mock
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student_default = Student_Classroom.Student()

        self.student_param = Student_Classroom.Student("Jakab", 81)
        self.student_param._grades = [5, 4, 3]

    def test_student_default(self):
        self.assertEqual(self.student_default.name, "Nincs nevem")
        self.assertEqual(self.student_default.age, 12)

    def test_student_param(self):
        self.assertEqual(self.student_param.name, "Jakab")
        self.assertEqual(self.student_param.age, 81)
        self.assertEqual(self.student_param._grades, [5, 4, 3])

    def test_add_grade(self):
        self.student_param._grades = []

        self.student_param.add_grade(5)
        self.assertEqual(self.student_param._grades, [5])

        self.student_param.add_grade(4)
        self.student_param.add_grade(3)
        self.assertEqual(self.student_param._grades, [5, 4, 3])

    def test_avg(self):
        with self.assertRaises(ZeroDivisionError): #ehhez kellett help:"D
            self.student_default.avg()

        self.assertEqual(self.student_param.avg(), 4)

        self.student_param.add_grade(2)
        self.assertEqual(self.student_param.avg(), 3.5)

    def test_max_min(self):
        with self.assertRaises(ValueError):
            self.student_default.max_grade()
        with self.assertRaises(ValueError):
            self.student_default.min_grade()

        self.assertEqual(self.student_param.max_grade(), 5)
        self.assertEqual(self.student_param.min_grade(), 3)

        self.student_param.add_grade(2)
        self.assertEqual(self.student_param.max_grade(), 5)
        self.assertEqual(self.student_param.min_grade(), 2)

    def tset_eq(self):
        student1 = Student_Classroom.Student("Jakab", 81)
        student1._grades = [5, 4, 3]
        self.assertEqual(self.student_param, student1)

        student2 = Student_Classroom.Student("Gizi", 75)
        self.assertNotEqual(self.student_param, student2)

class TestClassroom(unittest.TestCase):
    def setUp(self):
        self.classroom = Student_Classroom.ClassRoom()

        self.student1 = Student_Classroom.Student("Jakab", 81)
        self.student1._grades = [5, 4, 5]
        self.student2 = Student_Classroom.Student("Gizi", 75)
        self.student2._grades = [3, 4, 3]

    def test_new_studen_validt(self):
        self.classroom.new_student(self.student1)
        self.assertEqual(len(self.classroom._students), 1)

        self.classroom.new_student(self.student2)
        self.assertEqual(len(self.classroom._students), 2)

    def test_new_student_invalid(self):
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            self.classroom.new_student("invalid student")
            self.assertEqual(len(self.classroom._students), 0)
            self.assertIn("You can't do that", fake_out.getvalue())

    @mock.patch('Student_Classroom.Student.avg')
    def test_avg_with_mock(self, mock_avg):
        mock_avg.side_effect = [4.5, 3.5]

        self.classroom.new_student(self.student1)
        self.classroom.new_student(self.student2)

        self.assertEqual(self.classroom.avg(), (4.5 + 3.5) / 2)

        self.assertEqual(mock_avg.call_count, 2)