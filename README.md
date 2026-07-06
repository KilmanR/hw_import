# hw_import

Accounting app — homework on Python modules and packages.

## Structure

```
hw_import/
├── main.py                        # entry point
├── application/                   # main package
│   ├── salary.py                  # calculate_salary()
│   └── db/                        # subpackage
│       └── people.py              # get_employees()
├── requirements.txt               # dependencies
├── .gitignore
└── README.md
```

## Usage

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
