import unittest
from functions.run_python import run_python_file

# class TestGetinfo(unittest.TestCase):
    
#     def test_cal_dir(self):
#         result = get_files_info("calculator", ".")
#         print(result)
        
#     def test_cal_pkg_dir(self):
#         result = get_files_info("calculator", "pkg")
#         print(result)
        
#     def test_outside_dir1(self):
#         result = get_files_info("calculator", "/bin")
#         self.assertEquals(result,f'Error: Cannot list "/bin" as it is outside the permitted working directory')
        
#     def test_outside_dir2(self):
#         result = get_files_info("calculator", "../")
#         self.assertEquals(result,'Error: Cannot list "../" as it is outside the permitted working directory')

# class TestGetFileContent(unittest.TestCase):
#     def test_get_content_file_exist1(self):
#         result = get_file_content("calculator", "main.py")
#         print(result)
#     def test_get_content_file_exist2(self):
#         result = get_file_content("calculator", "pkg/calculator.py")
#         print(result)
#     def test_get_content_file_not_found1(self):
#         result = get_file_content("calculator", "/bin/cat")
#         print(result)
#     def test_get_content_not_found1(self):
#         result = get_file_content("calculator", "pkg/does_not_exist.py")
#         print(result)

# class TestWriteFileContent(unittest.TestCase):
#     def test_write_content_file_exist1(self):
#         result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#         print(result)
#     def test_write_content_file_exist2(self):
#         result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#         print(result)
#     def test_write_content_file_not_found1(self):
#         result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#         print(result)

class TestRunPythonFile(unittest.TestCase):
    def test_run_python_file1(self):
        result = run_python_file("calculator", "main.py")
        print(result)
        print('-'*50)
        
    def test_run_python_file2(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)
        print('-'*50)
           
    def test_run_python_file3(self):
        result = run_python_file("calculator", "tests.py")
        print(result)
        print('-'*50)
        
    def test_run_python_file4(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
        print('-'*50)
        
    def test_run_python_file5(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        print('-'*50)

if __name__ == "__main__":
    unittest.main()