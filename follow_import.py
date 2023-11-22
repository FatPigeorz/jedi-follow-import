import os
from jedi import Script, Project

if __name__ == "__main__":
    proj_root = os.path.join(os.path.dirname(os.path.realpath(__file__)), "foo")
    project = Project(proj_root)
    file_path = os.path.join(proj_root, "bar", "bar.py")
    script = Script(path=file_path, project=project)
    print(script.goto(1, 22, follow_imports=True))
    # output is []
    print(script.infer(1, 22))
    # output is []
