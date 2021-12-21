# CSV Generator

```pip install csv-gen```

A **fast random CSV generator** with a powerful yet simple template system that
can be used either as a standalone Command line tool or easily integrated 
into any codebase.

## Schema
TODO

## Types
TODO

## Usage
This section details how to use the Package in both it's intended use cases.

### As a Command Line Tool
Create a config file and use this package as a 
convenient way to generate CSV files on the fly.

#### Generate file and output to terminal
``` csvgen [config file] [number of lines to generate] ```

#### Generate file and output to file
``` csvgen [config file] [number of lines to generate] [output file]```

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
        "header": "number"
    }
]
generator = CsvGenerator(";", "\"", True, schema)
generator.generate(10)
generator.write(sys.stdout.buffer)
```
