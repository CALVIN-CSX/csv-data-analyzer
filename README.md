# CSV Data Analyzer & Visualizer 📊

A modular, Object-Oriented command-line application for analyzing, manipulating, and visualizing CSV datasets. 

This tool was designed with a focus on clean data structures and separation of concerns, decoupling the data processing engine from the visual rendering and the user interface.

## 🚀 Features
* **Interactive CLI Interface:** Navigate through multi-layered menus to perform data operations.
* **Data Manipulation Engine:** Slice dataframes, modify rows/columns, and rename headers on the fly.
* **Mathematical Operations:** Quickly compute Sum, Mean, Median, Mode, Min, Max, and Standard Deviation.
* **Dynamic Visualization:** Generate Single/Multi-Line Graphs, Bar Charts, Scatter Plots, Histograms, and Pie Charts dynamically using Matplotlib.
* **Clean Exports:** Save modified datasets safely with built-in duplicate checking to prevent overwriting files.

## 🛠️ Architecture & Refactoring (Before vs. After)
* **v1.0 (The Procedural Script):** A monolithic script handling inputs, logic, and rendering all in one place.
* **v2.0 (The OOP Refactor):** Re-architected into a scalable application using robust logic building. 
    * `analyzer.py`: A dedicated Pandas engine handling all data structures and hash map/dictionary parsing.
    * `visualizer.py`: An isolated Matplotlib rendering engine.
    * `main.py`: The controller layer strictly handling routing and CLI UI.

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/CALVIN-CSX/csv-data-analyzer.git](https://github.com/CALVIN-CSX/csv-data-analyzer.git)
   ```
2. **Install required dependencies:**
   ```bash
   pip install pandas matplotlib numpy tabulate
   ```
3. **Add your data:**
   Create a folder named `CSV` in the root directory and drop your `.csv` files inside. (A sample file is provided to test the application immediately).
4. **Run the application:**
   ```bash
   python main.py
   ```

📖 **Read the full breakdown of this refactor in my learning log:** 
[008. Learned refactoring and implemented OOPS in old project](https://github.com/CALVIN-CSX/learning-python/blob/main/learn-log/008.Learned_refactoring_and_implemented_OOPS_in_old_project.md)

## 🙌 Acknowledgments
* **Original Script Concept:** Special thanks to Gnanav T for collaborating on the original procedural v1.0 script.
* **Architecture & Refactor:** Designed, modularized, and refactored into OOP (v2.0) by CALVIN-CSX.