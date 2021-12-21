import sys

from csvgen.generator import CsvGenerator


def test_generation():
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
    generator = CsvGenerator(";", "\"", True, schema)
    print(generator)
    generator.generate(10)
    print("Generated CSV:")
    generator.write(sys.stdout.buffer)


if __name__ == "__main__":
    test_generation()
