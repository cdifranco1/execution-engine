import docker
import os


LANGUAGE_CONFIGS = {
    "python": {
      "interpreter": "python3",
      "extension": ".py"
    }
  }

class Executor:
  def __init__(self, language: str, code_input: str) -> None:
    self.code_input = code_input
    self.language_config = LANGUAGE_CONFIGS.get(language)
    self.file_extension = self.language_config.get("extension")
    self.interpreter = self.language_config.get("interpreter")
    self.docker_client = docker.from_env()
    self.file_path_template = "{cwd}/python-mount/executable/exec{extension}"

  def file_path(self):
    cwd = os.getcwd()
    return self.file_path_template.format(cwd = cwd, extension = self.file_extension)

  def docker_file_path(self):
    file_name = os.path.basename(self.file_path())
    return f"/execution-environment/executable/{file_name}"
  
  def test_runner_path(self):
    filename = "test_runner.py"
    return f"/execution-environment/{filename}"

  def write_executable(self) -> None:
    with open(self.file_path(), 'w') as f:
      f.write(code_input)
  
  def run(self):
    self.write_executable()
    return self.exec_tests()

  def exec_tests(self):
    cwd = os.getcwd()
    output = self.docker_client.containers.run("python:3", command = ["python3", self.test_runner_path()], tty=True, volumes={f'{cwd}/python-mount': {'bind': '/execution-environment', 'mode': 
    'ro'}})
    print(output)
    os.remove(self.file_path())



code_input = """class Solution:
  def add(self, a, b):
    return a + b"""

# sample run
Executor("python", code_input=code_input).run()


# Todo
# Set timeout on call to container
# Figure out how to start up container before beginning to execute code within the container



