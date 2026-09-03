# CSV Data Analyzer & Visualizer 📊

> Originally developed as a procedural Python project in **2023** and substantially refactored into a modular **Object-Oriented application in 2026**.

A command-line application for analyzing, manipulating, and visualizing CSV datasets.

The project demonstrates the progression from a working monolithic implementation to a more maintainable architecture with separation of concerns, structured error handling, application logging, and reusable components.

## 🚀 Features

- **Interactive CLI:** Navigate through menus for dataframe inspection and manipulation.
- **Data Manipulation:** Select, slice, modify, delete, and rename rows and columns, as well as individual cells.
- **Statistical Operations:** Calculate Sum, Mean, Median, Mode, Minimum, Maximum, and Standard Deviation for selected columns.
- **Visualization:** Generate line graphs, bar charts, scatter plots, histograms, and pie charts using Matplotlib.
- **Metadata Inspection:** View dataframe dimensions, shape, size, and data types.
- **CSV Export:** Save modified datasets to a separate directory with duplicate-file protection.
- **Application Logging:** Record informational, warning, and error events to a log file for debugging.

## 🏗️ Project Evolution

### v1.0 — Procedural Implementation · 2023

The original version was developed as a single Python script containing:

- CLI menus and user input
- Pandas dataframe operations
- Statistical calculations
- Matplotlib visualization
- Error handling

Although functional, the implementation became difficult to maintain because user-interface logic, data manipulation, and visualization were tightly coupled within the same program.

### v2.0 — OOP Refactor · 2026

The project was revisited and re-architected into separate modules to improve maintainability and separation of responsibilities.

```text
main.py
│
├── CLI / User Interaction
│
├── analyzer.py
│   └── Analyzer
│       ├── Data loading
│       ├── Data inspection
│       ├── Data manipulation
│       ├── Statistical operations
│       └── CSV export
│
└── visualizer.py
    └── Visualization functions
        ├── Line graphs
        ├── Bar charts
        ├── Scatter plots
        ├── Histograms
        └── Pie charts
```

### What Changed?

| v1.0 | v2.0 |
|---|---|
| Monolithic script | Modular multi-file architecture |
| Procedural data handling | `Analyzer` class |
| UI mixed with application logic | Dedicated CLI/controller layer |
| Visualization embedded in main program | Isolated visualization module |
| Basic error handling | Layered exception handling and validation |
| Console-only debugging | File-based application logging |
| Direct CSV output | Duplicate-safe export workflow |

## 🧠 Refactoring & Engineering Learnings

The main purpose of v2.0 was not simply to add features, but to improve the structure of an existing working application.

### Separation of Concerns

The original implementation combined user interaction, dataframe operations, and visualization. These responsibilities were separated into dedicated modules so that changes to one part of the application would require fewer changes elsewhere.

### Object-Oriented Design

The `Analyzer` class became the central component responsible for loading and manipulating the active dataframe rather than relying on a collection of unrelated procedural operations.

### Error Handling

The refactored implementation uses specific exception handling for expected dataframe and input errors while using higher-level handling at the CLI boundary to prevent individual failures from terminating the application.

### Logging

Python's `logging` module was introduced to record application events and errors to `app.log`, making it easier to trace failures across multiple modules.

### CLI Navigation

The original nested menu structure could trap users inside submenus. The refactored version introduced explicit return-to-main-menu paths and clearer navigation flow.

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/CALVIN-CSX/CSV-Data-Analyzer-Visualizer-Refactoring-Project.git
cd CSV-Data-Analyzer-Visualizer-Refactoring-Project
```

### 2. Install Dependencies

```bash
pip install pandas matplotlib numpy tabulate
```

### 3. Add a Dataset

Create a `CSV` directory in the project root and place a `.csv` file inside it.

A sample dataset is included for testing.

### 4. Run the Application

```bash
python main.py
```

## 📖 Development Log

The reasoning behind the v1.0 → v2.0 refactor is documented in my learning log:

[008. Learned Refactoring and Implemented OOP in Old Project](https://github.com/CALVIN-CSX/learning-python/blob/main/learn-log/008.Learned_refactoring_and_implemented_OOPS_in_old_project.md)

The log covers the architectural problems identified in v1.0, the decisions made during the refactor, debugging challenges, and the lessons learned from restructuring the application.

## 🤝 Acknowledgments

- **Original v1.0 implementation:** Developed collaboratively with [Gnanav T](https://github.com/gnanavt22).
