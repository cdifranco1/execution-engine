from typing import Any, List, Tuple, Union
# from executable.exec import Solution


class Solution:
  def divide(self, a, b):
    return a / b
  def add(self, a, b):
    return a + b


class DisplayError(Exception):
  def __init__(self, message: str) -> None:
      super().__init__(message)

class TestRunner:
  def __init__(self, solution_name: str, test_cases: List[Tuple[str, Tuple[str, ...]]]) -> None:
    self.solution = Solution()
    self.solution_method = getattr(self.solution, solution_name)
    self.test_cases = test_cases

  def execute_test(self, *args) -> Union[Any, Exception]:
    try:
      return self.solution_method(*args)
    except Exception as e:
      raise e

  def get_results(self) -> str:
    return [(expected, self.execute_test(*args)) for expected, args in self.test_cases]
  
  
  
test_cases = [
  (4, (2, 0)),
  (8, (3, 5)),
  (9, (4, 5))
]

test_runner = TestRunner("divide", test_cases=test_cases)
print(test_runner.get_results())


# Todo -- create method to convert test case tuples to correct type based on the signature of the solution method