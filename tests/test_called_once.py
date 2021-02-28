import time
from functools import lru_cache
from unittest.mock import MagicMock

class TestDatabase():

    def database_called(self):
        print('Database has been called')

    @lru_cache(maxsize=256)
    def function_example(self, a: int, b: int):
        print('Parameters are', a, b)

        self.database_called()

def test_database_memoization():
    TestDatabase.database_called = MagicMock()

    test = TestDatabase()

    test.function_example(3, 3)
    test.function_example(3, 7)
    test.function_example(3, 3)

    TestDatabase.database_called.assert_called()
    assert TestDatabase.database_called.call_count == 2
