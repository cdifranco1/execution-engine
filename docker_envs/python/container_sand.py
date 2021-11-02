import docker
import os
from typing import ByteString, Dict, Set

client = docker.from_env()

cwd = os.getcwd()

container = client.containers.run("python:3", command = ["bash"], tty=True, detach=True, volumes={f'{cwd}/executables': {'bind': '/executables', 'mode': 
'ro'}})
output = container.exec_run(["python3", "/executables/hello_world.py"])
print(output[0], output[1])



class Executor:

  # based on lang config, create images
  # store images in a dict of lang -> image
  def __init__(self, lang_config: Dict[str, Dict[str, str]]) -> None:
    pass

  # when code comes in, write to a file corresponding to input language
  def write_executable(self, language: str, code_input: str) -> None:
    pass

  # get image from dict, spin up container, and execute code, return as a string
  def run_code(self, language: str, filepath: str) -> str:
    pass



