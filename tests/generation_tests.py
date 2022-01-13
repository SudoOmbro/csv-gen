import sys
import time

from csvgen.generator import CsvGenerator


schema = [
    {
        "type": "email",
        "header": "Email"
    },
    {
        "type": "name",
        "header": "Name"
    },
    {
        "type": "name",
        "header": "Surname"
    },
    {
        "type": "date",
        "header": "DateOfBirth"
    },
    {
        "type": "CustomerID",
        "header": "number"
    }
]


def test_generation():
    start_time = time.time()
    generator = CsvGenerator(";", "\"", True, schema)
    print(generator)
    generator.generate(10)
    print("Generated CSV:")
    generator.write(sys.stdout.buffer)
    print(f"\n\nelapsed time: {time.time() - start_time}")


if __name__ == "__main__":
    test_generation()
