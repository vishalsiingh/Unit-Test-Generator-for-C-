# 🧪 Unit Test Generator - Approach & Test Coverage Summary

## 📌 Objective
Automate the generation of C++ unit tests using an LLM and validate them using Google Test and `gcov`.

## 🛠 Approach
1. A Python orchestrator reads a C++ source file and invokes the LLM using instructions in `generate_tests.yaml`.
2. The LLM returns well-structured unit test code (Google Test framework).
3. We ensure the test file compiles with g++ using `-fprofile-arcs -ftest-coverage` for `gcov` compatibility.
4. Post execution, coverage reports are generated using `gcov`.

## 🧪 Test Quality
- Tests cover 85.71% of `EmployeeManager.cpp`
- One trivial function intentionally excluded (`UnusedFunction`)

## 🧼 Improvements Made
- Removed redundant tests
- Handled build errors (missing headers, linking errors)
- Ensured tests reflect logic in the source

## 📦 Repeatable Setup
- Everything is automated via YAML + `main.py`
- Easy to extend to new files

## 🔚 Conclusion
The system provides a clean, repeatable, LLM-assisted test generation workflow with good coverage and readability.
