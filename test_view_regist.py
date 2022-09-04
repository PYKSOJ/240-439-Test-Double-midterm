import view_regist
import unittest
from unittest import mock


class RegistTest(unittest.TestCase):
    @mock.patch("pathlib.Path")
    @mock.patch("view_regist.get_subblueprints", return_value=["user/6210112016"])
    def test_view_regist_1(self, get_subblueprints_mock, path_mock):
        dir_name = "user/6210110216"
        path_mock_result = path_mock()
        result = view_regist.get_subblueprints(dir_name)
        self.assertIs(result, path_mock_result)
        
    @mock.patch("pathlib.Path")
    @mock.patch("view_regist.get_subblueprints", return_value=["user/yim"])
    def test_view_regist_2(self, get_subblueprints_mock, path_mock):
        dir_name = "user/yim"
        path_mock_result = path_mock()
        result = view_regist.get_subblueprints(dir_name)
        self.assertIs(result, path_mock_result)

    @mock.patch("pathlib.Path")
    @mock.patch("view_regist.get_subblueprints", return_value=["user/pongsapuk"])
    def test_view_regist(self, get_subblueprints_mock, path_mock):
        dir_name = "user/6210110216"
        path_mock_result = path_mock()
        result = view_regist.get_subblueprints(dir_name)
        self.assertIs(result, path_mock_result)