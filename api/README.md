# API

This repository contains Python scripts that demonstrate working with REST APIs, data processing, and various export formats. These scripts showcase how to retrieve data from APIs and convert it to different structured formats.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Key Concepts](#key-concepts)
- [Scripts](#scripts)
- [Resources](#resources)

## Description

This project focuses on working with REST APIs and data export techniques, covering:
- Making HTTP requests to REST APIs
- Processing and manipulating API response data
- Exporting data to CSV format
- Exporting data to JSON format
- Building structured data representations
- Following Python naming conventions and style guidelines

Each script demonstrates specific aspects of API interaction and data processing, providing practical examples for common data retrieval and export tasks.

## Requirements

- Ubuntu 14.04 LTS
- Python 3.4.3
- PEP 8 style (version 1.7.x)
- All files must be executable
- Documentation for modules, classes, and functions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/holbertonschool-back-end.git
```

2. Navigate to the directory:
```bash
cd holbertonschool-back-end/api
```

3. Install dependencies:
```bash
pip3 install requests
```

## Usage

Run any script using Python:

```bash
python3 script_name.py [arguments]
```

For example:
```bash
python3 0-gather_data_from_an_API.py 2
```

## Key Concepts

- **REST APIs**: Understanding and interacting with RESTful web services
- **HTTP Requests**: Making GET requests to retrieve data from APIs
- **Data Processing**: Parsing and manipulating API response data
- **CSV Export**: Converting data to comma-separated values format
- **JSON Export**: Converting data to JavaScript Object Notation format
- **Python Style Guidelines**: Following PEP 8 and naming conventions

## Scripts

| Script | Description |
|--------|-------------|
| 0-gather_data_from_an_API.py | Retrieves TODO list progress for a given employee ID |
| 1-export_to_CSV.py | Exports TODO list data to CSV format |
| 2-export_to_JSON.py | Exports TODO list data to JSON format |
| 3-dictionary_of_list_of_dictionaries.py | Exports TODO list data for all employees to JSON format |

## Resources

- [REST API Design](https://restfulapi.net/)
- [Python Requests Library](https://requests.readthedocs.io/en/master/)
- [Working with CSV in Python](https://docs.python.org/3/library/csv.html)
- [Working with JSON in Python](https://docs.python.org/3/library/json.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

## Author
