\# CSV Data Analyzer \& Visualizer 📊



A modular, Object-Oriented command-line application for analyzing, manipulating, and visualizing CSV datasets. 



This tool was designed with a focus on clean data structures and separation of concerns, decoupling the data processing engine from the visual rendering and the user interface.



\## 🚀 Features

\* \*\*Interactive CLI Interface:\*\* Navigate through multi-layered menus to perform data operations.

\* \*\*Data Manipulation Engine:\*\* Slice dataframes, modify rows/columns, and rename headers on the fly.

\* \*\*Mathematical Operations:\*\* Quickly compute Sum, Mean, Median, Mode, Min, Max, and Standard Deviation.

\* \*\*Dynamic Visualization:\*\* Generate Single/Multi-Line Graphs, Bar Charts, Scatter Plots, Histograms, and Pie Charts dynamically using Matplotlib.

\* \*\*Clean Exports:\*\* Save modified datasets safely with built-in duplicate checking to prevent overwriting files.



\## 🛠️ Architecture \& Refactoring (Before vs. After)

\* \*\*v1.0 (The Procedural Script):\*\* A monolithic script handling inputs, logic, and rendering all in one place.

\* \*\*v2.0 (The OOP Refactor):\*\* Re-architected into a scalable application using robust logic building. 

&#x20;   \* `analyzer.py`: A dedicated Pandas engine handling all data structures and hash map/dictionary parsing.

&#x20;   \* `visualizer.py`: An isolated Matplotlib rendering engine.

&#x20;   \* `main.py`: The controller layer strictly handling routing and CLI UI.



\## 💻 Installation \& Setup



1\. \*\*Clone the repository:\*\*

&#x20;  ```bash

&#x20;  git clone \[https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)

&#x20;  ```

2\. \*\*Install required dependencies:\*\*

&#x20;  ```bash

&#x20;  pip install pandas matplotlib numpy tabulate

&#x20;  ```

3\. \*\*Add your data:\*\*

&#x20;  Create a folder named `CSV` in the root directory and drop your `.csv` files inside. (A sample file is provided to test the application immediately).

4\. \*\*Run the application:\*\*

&#x20;  ```bash

&#x20;  python main.py

&#x20;  ```



\## 🛠️ Architecture \& Refactoring (Before vs. After)

\* \*\*v1.0 (The Procedural Script):\*\* A monolithic script handling inputs, logic, and rendering all in one place.

\* \*\*v2.0 (The OOP Refactor):\*\* Re-architected into a scalable application using robust logic building. 

&#x20;   \* `analyzer.py`: A dedicated Pandas engine handling all data structures and dictionary parsing.

&#x20;   \* `visualizer.py`: An isolated Matplotlib rendering engine.

&#x20;   \* `main.py`: The controller layer strictly handling routing and CLI UI.



📖 \*\*Read the full breakdown of this refactor in my learning log:\*\* 

\[008. Learned refactoring and implemented OOPS in old project](link\_to\_your\_learning\_log\_file\_here.md)



\## 🙌 Acknowledgments

\* \*\*Original Script Concept:\*\* Special thanks to Gnanav T for collaborating on the original procedural v1.0 script.

\* \*\*Architecture \& Refactor:\*\* Designed, modularized, and refactored into OOP (v2.0) by CALVIN-CSX.

