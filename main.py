import logging
from analyzer import Analyzer
import visualizer

l = logging.getLogger("app")
handler1 = logging.FileHandler("app.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler1.setFormatter(formatter)
l.addHandler(handler1)
l.setLevel(logging.INFO)

try:
    analyzer = Analyzer()
except FileNotFoundError:
    l.error("File not found.")
    print("File not found.")
    exit(1)

if __name__ == "__main__":
    l.info("Starting Data Manupulation and Visualization Tool...")
    while True:
        try:
            name = analyzer.file
            name = name.split(".")[0]
            print('1. INTERACT WITH DATAFRAME')
            print(f'2. VISUALIZE {name.upper()} DATA')
            print(f'3. PERFORM OPERATIONS ON {name.upper()} DATA')
            print(f'4. DISPLAY {name.upper()} DETAILS')
            print(f'5. GET METADATA {name.upper()}')
            print('6. CONCLUDE PROGRAM')
            print("9. Save CSV FILE")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                try:
                    while True:
                        print(
                            "1. SELECT COLUMNS\n2. SELECT ROWS\n3. GET INDIVIDUAL VALUE\n4. SLICE DATAFRAME\n5. MODIFY COLUMN\n6. MODIFY ROW\n7. MODIFY SINGLE CELL\n8. DELETE ROW/COLUMN\n9. RENAME ROW/COLUMN\n10. GO BACK TO MAIN MENU")
                        operation = int(input("Enter your operation choice: "))

                        if operation == 10:
                            break

                        if operation == 1:
                            print(analyzer.get_column_names())
                            col_name = input("Enter COLUMN NAME: ")
                            print(analyzer.get_column_data(col_name))
                        elif operation == 2:
                            print(analyzer.get_row_names())
                            start = int(input("Enter START ROW NUMBER: "))
                            end = int(input("Enter END ROW NUMBER: "))
                            print(analyzer.get_rows(start, end))
                        elif operation == 3:
                            print(analyzer.get_column_names())
                            print(analyzer.get_row_names())
                            row_name = input("Enter ROW NAME: ")
                            column_name = input("Enter COLUMN NAME: ")
                            print(analyzer.single_value(row_name, column_name))
                        elif operation == 4:
                            print(analyzer.get_column_names())
                            print(analyzer.get_row_names())
                            row_start = int(input("Enter START ROW NUMBER: "))
                            row_end = int(input("Enter END ROW NUMBER: "))
                            column_start = input("Enter START COLUMN NAME: ")
                            column_end = input("Enter END COLUMN NAME: ")
                            print(analyzer.slice_data(row_start, row_end, column_start, column_end))
                        elif operation == 5:
                            print(analyzer.get_column_names())
                            column_name = input("Enter COLUMN NAME: ")
                            column_value = input("Enter COLUMN VALUE: ")
                            print(analyzer.modify_column(column_name, column_value))
                        elif operation == 6:
                            print(analyzer.get_row_names())
                            row_index = int(input("Enter ROW NUMBER: "))
                            row_value = input("Enter ROW VALUE: ")
                            print(analyzer.modify_row(row_index, row_value))
                        elif operation == 7:
                            print(analyzer.get_column_names())
                            print(analyzer.get_row_names())
                            row_index = int(input("Enter ROW NUMBER: "))
                            column_name = input("Enter COLUMN NAME: ")
                            row_value = input("Enter New VALUE: ")
                            print(analyzer.modify_single_cell(row_index, column_name, row_value))
                        elif operation == 8:
                            print(analyzer.get_column_names())
                            print(analyzer.get_row_names())
                            choice_del = input(
                                "Do you want to delete a ROW or COLUMN? (Enter '1' for row or '2' for column): ").strip().lower()
                            if choice_del == 'row' or choice_del == "1":
                                row_index = int(input("Enter ROW NUMBER to delete: "))
                                analyzer.delete_row_or_column(axis=0, label=row_index)
                                print(f"Row {row_index} deleted successfully.")
                            elif choice_del == 'column' or choice_del == "2":
                                column_name = input("Enter COLUMN NAME to delete: ")
                                analyzer.delete_row_or_column(axis=1, label=column_name)
                                print(f"Column '{column_name}' deleted successfully.")
                            else:
                                l.warning(f"Invalid choice for deletion. User selected '{choice_del}'.")
                                print(f"Invalid choice. Please enter 'row' or 'column'.\nuser selected '{choice_del}'.")
                        elif operation == 9:
                            choice_ren = input(
                                "Do you want to rename a ROW or COLUMN? (Enter '1' for row or '2' for column): ").strip().lower()
                            if choice_ren == 'row' or choice_ren == "1":
                                print(analyzer.get_row_names())
                                row_index = int(input("Enter ROW NUMBER to rename: "))
                                row_value = input("Enter NEW ROW NUMBER: ")
                                print(analyzer.rename_row(row_index, row_value))
                            elif choice_ren == 'column' or choice_ren == "2":
                                print(analyzer.get_column_names())
                                column_name = input("Enter COLUMN NAME to rename: ")
                                column_new_name = input("Enter NEW COLUMN NAME: ")
                                print(analyzer.rename_column(column_name, column_new_name))
                            else:
                                l.warning(f"Invalid choice for renaming. User selected '{choice_ren}'.")
                                print(f"Invalid choice. Please enter 'row' or 'column'.\nuser selected '{choice_ren}'.")
                        else:
                            l.warning(f"Invalid choice for dataframe interaction. User selected '{operation}'.")
                            print(
                                f"Invalid choice. Please enter a number between 1 and 10.\nuser selected '{operation}'.")
                except Exception as e:
                    l.error(f"An error occurred during dataframe interaction: {e}")
                    print(f"An error occurred: {e}")

            elif choice == 2:
                try:
                    while True:
                        print(
                            "1. PLOT A LINE GRAPH\n2. PLOT A BAR GRAPH\n3. PLOT A SCATTER PLOT\n4. PLOT A HISTOGRAM\n5. PLOT A PIE CHART\n6. GO BACK TO MAIN MENU")
                        operation = int(input("Enter your choice: "))

                        if operation == 6:
                            break

                        if operation == 1:
                            sub_choice = input(
                                "Do you want to plot a SINGLE LINE GRAPH or MULTIPLE LINE GRAPH? (Enter '1' for single or '2' for multiple): ").strip().lower()
                            if sub_choice == 'single' or sub_choice == "1":
                                print(analyzer.get_column_names())
                                col_name = input("Enter COLUMN NAME to plot: ")
                                visualizer.single_line_graph(name, analyzer.data, col_name)
                            elif sub_choice == 'multiple' or sub_choice == "2":
                                print(analyzer.get_column_names())
                                col_names = input("Enter COLUMN NAMES to plot (comma-separated): ").strip().split(',')
                                visualizer.multi_line_graph(name, analyzer.data, col_names)
                            else:
                                l.warning(f"Invalid choice for line graph plotting. User selected '{sub_choice}'.")
                                print(
                                    f"Invalid choice. Please enter 'single' or 'multiple'.\nuser selected '{sub_choice}'.")
                        elif operation == 2:
                            sub_choice = input(
                                "Do you want to plot a SINGLE BAR GRAPH or MULTIPLE BAR GRAPH? (Enter '1' for single or '2' for multiple): ").strip().lower()
                            if sub_choice == 'single' or sub_choice == '1':
                                print(analyzer.get_column_names())
                                col_name = input("Enter COLUMN NAME to plot: ")
                                visualizer.single_bar_graph(name, analyzer.data, col_name)
                            elif sub_choice == 'multiple' or sub_choice == '2':
                                print(analyzer.get_column_names())
                                col_names = input("Enter COLUMN NAMES to plot (comma-separated): ").strip().split(',')
                                visualizer.multi_bar_graph(name, analyzer.data, col_names)
                            else:
                                l.warning(f"Invalid choice for bar graph plotting. User selected '{sub_choice}'.")
                                print(
                                    f"Invalid choice. Please enter 'single' or 'multiple'.\nuser selected '{sub_choice}'.")
                        elif operation == 3:
                            sub_choice = input(
                                "Do you want to plot a SINGLE SCATTER PLOT or MULTIPLE SCATTER PLOT? (Enter '1' for single or '2' for multiple): ").strip().lower()
                            if sub_choice == 'single' or sub_choice == '1':
                                print(analyzer.get_column_names())
                                X_name = input("Enter X AXIS COLUMN NAME: ")
                                Y_name = input("Enter Y AXIS COLUMN NAME: ")
                                visualizer.scatter_graph(name, analyzer.data, X_name, Y_name)
                            elif sub_choice == 'multiple' or sub_choice == '2':
                                print(analyzer.get_column_names())
                                X_name = input("Enter X AXIS COLUMN NAME: ")
                                Y_names = input("Enter Y AXIS COLUMN NAMES to plot (comma-separated): ").strip().split(
                                    ',')
                                visualizer.multiple_scatter_graph(name, analyzer.data, X_name, Y_names)
                            else:
                                l.warning(f"Invalid choice for scatter graph plotting. User selected '{sub_choice}'.")
                                print(
                                    f"Invalid choice. Please enter 'single' or 'multiple'.\nuser selected '{sub_choice}'.")
                        elif operation == 4:
                            print(analyzer.get_column_names())
                            col_name = input("Enter COLUMN NAME: ")
                            visualizer.histogram(name, analyzer.data, col_name)
                        elif operation == 5:
                            print(analyzer.get_column_names())
                            col_name = input("Enter COLUMN NAME: ")
                            visualizer.pie_chart(name, analyzer.data, col_name)
                        else:
                            l.warning(f"Invalid choice for visualization. User selected '{operation}'.")
                            print(
                                f"Invalid choice. Please enter a number between 1 and 6.\nuser selected '{operation}'.")
                except Exception as e:
                    l.error(f"An error occurred during data visualization: {e}")
                    print(f"An error occurred: {e}")

            elif choice == 3:
                try:
                    while True:
                        print(
                            "1. GET SUM OF A COLUMN\n2. GET MINIMUM OF A COLUMN\n3. GET MAXIMUM OF A COLUMN\n4. GET MEAN OF A COLUMN\n5. GET MEDIAN OF A COLUMN\n6. GET MODE OF A COLUMN\n7. GET STANDARD DEVIATION OF A COLUMN\n8. GO BACK TO MAIN MENU")
                        operation = int(input("Enter your choice: "))

                        if operation == 8:
                            break

                        if 1 <= operation <= 7:
                            print(analyzer.get_column_names())
                            col_name = input("Enter COLUMN NAME: ")

                            if operation == 1:
                                print(analyzer.data_sum(col_name))
                            elif operation == 2:
                                print(analyzer.data_min(col_name))
                            elif operation == 3:
                                print(analyzer.data_max(col_name))
                            elif operation == 4:
                                print(analyzer.data_mean(col_name))
                            elif operation == 5:
                                print(analyzer.data_median(col_name))
                            elif operation == 6:
                                print(analyzer.data_mode(col_name))
                            elif operation == 7:
                                print(analyzer.data_std(col_name))
                        else:
                            l.warning(f"Invalid choice for mathematical operation. User selected '{operation}'.")
                            print(
                                f"Invalid choice. Please enter a number between 1 and 8.\nuser selected '{operation}'.")
                except Exception as e:
                    l.error(f"An error occurred during data calculation: {e}")
                    print(f"An error occurred: {e}")

            elif choice == 4:
                print(analyzer.get_dataframe())
            elif choice == 5:
                metadata = analyzer.get_dataframe_metadata()
                for key, value in metadata.items():
                    print(f"\n--- {key} ---")
                    print(value)
                print("\n")
            elif choice == 6:
                l.info("Exiting the program.")
                print("Exiting the program.")
                break
            elif choice == 9:
                file_path = input("SAVE IT AS: ")
                print(analyzer.save_copy_to_csv(file_path))
            else:
                l.warning(f"Invalid choice for main menu. User selected '{choice}'.")
                print(f"Invalid choice. Please enter a number accordingly.\nuser selected '{choice}'.")
        except Exception as e:
            l.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")