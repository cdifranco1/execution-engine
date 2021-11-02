# from enum import Enum, auto
import docker
import os
from typing import ByteString, Dict, Set

class Executor:
  executable_count = 0 

  docker_client = docker.from_env()
  language_configs = {
    "python": {
      "interpreter": "python3",
      "extension": ".py"
    }
  }
  file_path_template = "{cwd}/executables/exec_{count}{extension}"

  def file_path(self, language: str):
    cwd = os.getcwd()
    file_extension = self.language_configs.get(language)["extension"]
    return self.file_path_template.format(cwd = cwd, count = self.executable_count, extension = file_extension)

  def docker_file_path(self, language: str):
    file_name = os.path.basename(self.file_path(language))
    return f"/executables/{file_name}"

  def write_executable(self, language: str, code_input: str) -> None:
    self.executable_count += 1
    with open(self.file_path(language), 'w') as f:
      f.write(code_input)


  def run(self, language: str):
    cwd = os.getcwd()

    container = self.docker_client.containers.run("python:3", command = ["bash"], tty=True, detach=True, volumes={f'{cwd}/executables': {'bind': '/executables', 'mode': 
    'ro'}})
    output = container.exec_run(["python3", self.docker_file_path(language=language)])
    
    print(output[0], output[1])
    os.remove(self.file_path(language=language))

    self.executable_count -= 1

    

code_input = """print("hello world")"""
executor = Executor()
executor.write_executable("python", code_input=code_input)
executor.run("python")


# class Executor:

#   # based on lang config, create images
#   # store images in a dict of lang -> image
#   def __init__(self, lang_config: Dict[str, Dict[str, str]] = None) -> None:
#     self.client = docker.from_env()

#     self.count = 0

#   # when code comes in, write to a file corresponding to input language
#   def write_executable(self, language: str, code_input: str) -> None:
#     with open(f'exec_{self.count}') as f:
#       f.write(code_input)

#   # get image from dict, spin up container, and execute code, return as a string
#   def run_code(self, language: str, filepath: str) -> str:
#     pass



