import json
import sys

from csvgen.generator import CsvGenerator


def main():
    args_num: int = len(sys.argv) - 1
    if args_num < 3:
        print("usage: csv-gen [schema file] [lines number] [(optional) filename]")
        return
    with open(sys.argv[1], "r") as file:
        loaded_config: dict = json.load(file)
    generator = CsvGenerator(
        loaded_config.get("separator", default=";"),
        loaded_config.get("delimiter", default="\""),
        loaded_config.get("headers", default=True),
        loaded_config.get("schema", default=[{"type": "string"}]),
        delimit_all=loaded_config.get("delimit all", default=False),
    )
    print(generator)
    generator.generate(int(sys.argv[2]))
    if args_num > 3:
        with open(sys.argv[3], "wb") as file:
            generator.write(file)
    else:
        generator.write(sys.stdout.buffer)


if __name__ == "__main__":
    main()
