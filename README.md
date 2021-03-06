# OmbroCSV

```pip install ombrocsv```

A **fast random CSV generator** with a powerful yet simple template system that
can be used either as a standalone Command line tool or easily integrated 
into any codebase.

## Schema
The schema is basically the "template" of the CSV you are generating,
it's a list of dictionaries (each dict represents a column).
Here's how it should look:
```
[
    {
            "type": {see types for valid types}
            "header": {header name (optional)}
    },
    {
            "type": {see types for valid types}
            "header": {header name (optional)}
    },
    ...
]
```
the order in which the columns appear in the schema will be the order in 
which they will appear in the generated CSV.

## Types
Here are the supported types with a brief description:

- **"bit"** - random integer value between 1 and 0.
- **"phone_prefix"** random 4-digit integer value.
- **"phone_number"** random 10-digit number.
- **"phone_complete"** random 14-digit number.
- **"string"** - completely random string.
- **"name"** - random string that loosely resembles a name.
- **"email"** - random email
- **"number"** - random integer number
- **"id"** - incremental id that starts from 0
- **"date"** - random date

**Note**: Any non recognized type will be treated as a string

### Custom Types
you can easily **override the default types** by passing a 
different `RandUtils` in the constructor of CsvGenerator, just make
sure that your custom RandUtils inherits from the base one and that
every new type you add inherits from `RandomBase`.

Both `RandUtils` and `RandomBase` can be found in _random_utils.py_

To use your custom types then simply write the name it has been
registered with in your custom RandUtils class in the "type" field
when passing the schema.

#### Example
adding `CustomType` to code:
```
Class CustomType(RandomBase):
    ...


Class CustomRandUtils(RandUtils):

    def __init__():
        super().__init__()
        self.custom_type = CustomType()
```
Using `CustomType` in the Schema:
```
[
    {
            "type": "custom_type"
    },
    ...
]
```

## Usage
This section details how to use the Package in both it's intended use cases.

### As a Command Line Tool
Create a config file and use this package as a 
convenient way to generate CSV files on the fly.

#### Generate file and output to terminal
``` ombrocsv [config file] [number of lines to generate] ```

#### Generate file and output to file
``` ombrocsv [config file] [number of lines to generate] [output file]```

#### Config file
```
{
    "schema": [
        {
            "type": {see types for valid types}
            "header": {header name (optional)}
        },
        ...
    ],
    "separator": {separator character (optional, default = ;)},
    "delimiter": {delimiter character (optional, default = ")},
    "headers": {true/false (optional, default = true)},
    "delimit all": {true/false (optional, default = false)}
}
```

##### Example
```
{
  "schema": [{
      "type": "email",
      "header": "Email"
    }, {
      "type": "name",
      "header": "Name"
    }, {
      "type": "name",
      "header": "Surname"
    }, {
      "type": "date",
      "header": "DateOfBirth"
    }, {
      "type": "CustomerID",
      "header": "string"
    }
  ],
  "separator": "|",
  "delimiter": "'"
}
```

### As a Package
Just import `CsvGenerator`, initialize it with the required 
parameters and generate your CSV files.

#### Example
```
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
        "header": "string"
    }
]
generator = CsvGenerator(";", "\"", True, schema)
generator.generate(10)
generator.write(sys.stdout.buffer)
```
