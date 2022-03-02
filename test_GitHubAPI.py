import unittest
import GitHubAPI
from unittest import mock


class MyTestCase(unittest.TestCase):

    @mock.patch('GitHubAPI.getProjects')
    def test_mock(self, get_mock):
        get_mock.return_value = []
        response = GitHubAPI.getProjects('')
        assert response == get_mock.return_value


    @mock.patch('GitHubAPI.getProjects')
    def test_mock2(self, get_mock):
        get_mock.return_value = [['csp', 2], ['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2],
                                 ['richkempinski.github.io', 9], ['threads-of-life', 1], ['try_nbdev', 2],
                                 ['try_nbdev2', 5]]
        response = GitHubAPI.getProjects("richkempinski")
        assert response == get_mock.return_value

    @mock.patch('GitHubAPI.getProjects')
    def test_mock3(self, get_mock):
        get_mock.return_value = [['GitHubApi567', 1], ['hw1TriangleTesting', 3], ['SSW-567', 2], ['Triangle567', 12]]
        response = GitHubAPI.getProjects("kobedawes")
        assert response == get_mock.return_value


if __name__ == '__main__':
    unittest.main()

