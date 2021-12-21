import subprocess


def test_command_line_tool(params: str):
    command: str = f"\"../csvgen/__main__.py\" {params}"
    print(command)
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    test_command_line_tool("test_schema.json 2")
    test_command_line_tool("test_schema.json 20 test.csv")
