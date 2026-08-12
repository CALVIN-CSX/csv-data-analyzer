\# Changelog



All notable changes to this project will be documented in this file.



\## \[2.0.0] - 2026-08-12



\### Added

\- \*\*OOP Architecture:\*\* Decoupled the monolithic script into three dedicated modules (`main.py`, `analyzer.py`, `visualizer.py`).

\- \*\*Data Engine:\*\* Introduced the `Analyzer` class to act as the single source of truth for all Pandas dataframe mutations.

\- \*\*Logging System:\*\* Implemented Python's native `logging` library (`app.log`) to track warnings, errors, and system events silently in the background.

\- \*\*Safe Directory Validations:\*\* Added explicit checks to verify the existence of the `./CSV` directory and `.csv` files before initialization, preventing fatal runtime crashes.



\### Changed

\- \*\*CLI Navigation:\*\* Overhauled the interactive menu system. Users can now cleanly back-trace their steps using a unified `10. GO BACK TO MAIN MENU` exit condition.

\- \*\*Visualization Logic:\*\* Matplotlib rendering is now fully isolated. Bar charts utilize `enumerate` to mathematically calculate dynamic offsets, preventing overlapping data renders.

\- \*\*Chart Labeling:\*\* Implemented dynamic logical fallbacks (`dataFrame.index.name or "Index"`) to safely handle datasets missing named indexes without throwing exceptions.

\- \*\*Clean CSV Exports:\*\* Data exports now use `index=False` to prevent redundant index column generation.



\### Fixed

\- \*\*Infinite Loops:\*\* Squashed the nested `while True` loop traps that previously locked users inside sub-menus.

\- \*\*Out-of-Bounds Exceptions:\*\* Added boundary and length checks during dataframe slicing to catch invalid user inputs before they crash the Pandas engine.

\- \*\*Silent Failures:\*\* Replaced generic error drops with explicit, specialized `try/except` blocks (e.g., `KeyError`, `TypeError`) across all data manipulation methods.



\---



\## \[1.0.0] - Initial Release

\- \*\*Procedural Script:\*\* Initial monolithic implementation of the data analyzer.

\- \*\*Features:\*\* Basic dataframe slicing, standard Matplotlib plotting, and terminal-based math operations.

