import unittest
import GitHubAPI

class MyTestCase(unittest.TestCase):

    def test_getProjects(self):
        """may not account for new repositories being made i believe but does for increasing commits"""
        self.assertEqual(GitHubAPI.getProjects(''), [])
        #self.assertGreaterEqual(GitHubAPI.getProjects('richkempinski'), [['csp', 2], ['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2], ['richkempinski.github.io', 9], ['threads-of-life', 1], ['try_nbdev', 2], ['try_nbdev2', 5]])
        self.assertGreaterEqual(GitHubAPI.getProjects('kobedawes'), [['GitHubApi567', 1], ['hw1TriangleTesting', 3], ['SSW-567', 2], ['Triangle567', 12]])

if __name__ == '__main__':
    unittest.main()
"""def printList(list):
    if list == []:
        return ''
    else:
        return f'Repo: {list[0][0]} Commits {list[0][1]}' + printList(list[1:])"""