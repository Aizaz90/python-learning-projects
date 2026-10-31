# Python Learning Projects

A collection of hands-on Python projects documenting my progress in programming, problem-solving, networking, and cybersecurity automation.

I am currently pursuing an M.Sc. in Computer Science at TU Dresden, focusing on cybersecurity, network security, and secure systems.

This repository serves as a record of my Python learning journey, from fundamental programming concepts to practical cybersecurity tools.

---

## Projects

### 01 — Student Grade Management System

**Status:** Completed

A Python program that manages student records and performs basic data processing.

**Features:**
- Stores student information using lists and dictionaries
- Displays student names, ages, and marks
- Separates passing and failing students
- Sorts students by marks in descending order
- Calculates total and average marks

**Concepts practiced:**
- Lists and dictionaries
- For loops and conditional statements
- Functions and return values
- Sorting using `sorted()` and `key`
- Formatted output using f-strings
- Basic arithmetic operations

**Run:**

```bash
python3 01-student-grade-management.py
```

---

### 02 — Command-Line Calculator

**Status:** Completed

A Python command-line calculator that performs basic mathematical operations using arguments supplied through the terminal.

**Features:**
- Addition, subtraction, multiplication, and division
- Command-line input using `sys.argv`
- Validation of missing or extra arguments
- Error handling using `try/except`
- Division-by-zero protection
- Detection of invalid operators
- Helpful error messages for invalid input

**Concepts practiced:**
- Importing Python modules
- Working with `sys.argv`
- String-to-integer conversion using `int()`
- Conditional statements (`if`, `elif`, `else`)
- Exception handling (`try`, `except`)
- Program termination using `sys.exit()`
- Command-line execution

**Usage:**

```bash
python3 02-command-line-calculator.py <number1> <operator> <number2>
```

**Examples:**

```bash
# Addition
python3 02-command-line-calculator.py 10 + 5

# Subtraction
python3 02-command-line-calculator.py 10 - 5

# Multiplication
python3 02-command-line-calculator.py 10 "*" 5

# Division
python3 02-command-line-calculator.py 10 / 5
```

**Note:** The calculator currently accepts integer inputs. Put `*` in quotation marks to prevent the shell from interpreting it as a wildcard.

---

### 03 — Security Log Analyzer

**Status:** Completed

A beginner-friendly Python tool that analyzes synthetic authentication logs and flags IP addresses with repeated failed login attempts.

**Features:**
- Reads authentication logs from a text file
- Counts successful and failed logins
- Extracts source IP addresses
- Counts failed login attempts per IP using dictionaries
- Flags IP addresses with 3 or more failed login attempts
- Displays a security summary and total suspicious IP count

**Concepts practiced:** File handling, `with open()`, `.readlines()`, loops, string methods, `.split()`, dictionaries, and conditional statements.

**Run:**

```bash
cd 03-security-log-analyzer
python3 analyzer.py
```

**Note:** Uses synthetic training logs. The threshold is for demonstration, not definitive detection of malicious activity.


### TCP Port Scanner

**Status:** Work in Progress

An educational Python project exploring TCP socket programming, networking, and concurrent execution.

**Topics explored:**
- IPv4 and TCP socket programming
- Hostname-to-IP resolution
- TCP connection attempts
- Socket timeouts
- Exception handling
- Multithreading using Python's `threading` module

**Planned improvements:**
- Implement controlled concurrency
- Improve error handling
- Add configurable port ranges
- Improve output formatting
- Test and document the completed implementation

**Security note:** This project is intended strictly for educational purposes and authorized network testing.

---

## Technologies and Tools

- **Programming:** Python 3
- **Development:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub
- **Operating Systems:** macOS and Linux
- **Networking:** Python Socket API

---

## Learning Goals

My primary goals are to:

1. Strengthen Python programming fundamentals.
2. Develop problem-solving and debugging skills.
3. Understand file handling, exceptions, and modules.
4. Learn socket programming and network communication.
5. Practice Git and GitHub through terminal-based workflows.
6. Build Python tools for cybersecurity automation.
7. Progress toward practical SOC, Blue Team, and threat-intelligence projects.

---

## Upcoming Projects

| Project | Main Learning Focus |
|---|---|
| Security Log Analyzer | File handling, parsing, filtering, and log analysis |
| Hostname-to-IP Resolver | DNS resolution and socket programming |
| Multithreaded Task Runner | Threads, concurrency, and task management |
| Improved TCP Port Scanner | Network scanning, timeouts, and controlled concurrency |

Projects will be added as they are developed, tested, and documented.

---

## Running the Projects

**1. Clone the repository:**

```bash
git clone https://github.com/Aizaz90/python-learning-projects.git
```

**2. Navigate to the