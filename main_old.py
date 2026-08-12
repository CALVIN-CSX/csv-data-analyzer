import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset from the "ADANIPORTS-EQ-01-04-2023.csv" file with specified column names
data = pd.read_csv("data.csv")

while True:
    try:
        # Display menu options
        print('1. INTERACT WITH DATAFRAME')
        print('2. ANALYZE ADANIPORTS SHARE')
        print('3. DISPLAY ADANIPORTS STOCK DETAILS')
        print('4. CONCLUDE PROGRAM')

        # Take user input for the menu choice
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Sub-menu for DataFrame operations
            print("""1. SELECT COLUMNS
2. SELECT ROWS
3. GET INDIVIDUAL VALUE
4. SLICE DATAFRAME
5. ADD/MODIFY COLUMN
6. ADD/MODIFY ROW
7. MODIFY SINGLE CELL
8. DELETE ROW/COLUMN
9. RENAME ROW/COLUMN""")

            # Take user input for the sub-menu choice
            operation = int(input("Enter your operation choice: "))

            if operation == 1:
                # Selecting Columns
                while True:
                    try:
                        print("COLUMNS:", data.columns)
                        col_name = input("Enter COLUMN NAME: ")
                        print(data[col_name])
                        break
                    except KeyError:
                        print("Error: Invalid column name. Please enter a valid column name.")

            elif operation == 2:
                # Selecting Rows
                while True:
                    try:
                        print("ROWS:", data.index)
                        num_rows = int(input('Enter the number of rows you want to access: '))
                        start_row = int(input("Enter STARTING ROW INDEX: "))
                        end_row = int(input("Enter ENDING ROW INDEX: "))
                        print(data.loc[start_row:end_row, :])
                        break  # Break out of the loop if the input is valid
                    except KeyError:
                        print("Error: Invalid row index. Please enter a valid row index.")

            elif operation == 3:
                # Get Individual Value
                while True:
                    try:
                        print('ROW:', data.index)
                        print('COLUMN:', data.columns)
                        row_label = int(input("ENTER ROW LABEL: "))
                        col_label = input("ENTER COLUMN LABEL: ")
                        print(data.loc[row_label, col_label])
                        break  # Break out of the loop if the input is valid
                    except KeyError:
                        print("Error: Invalid row/column label. Please enter a valid label.")

            elif operation == 4:
                # Slice DataFrame
                while True:
                    try:
                        print("ROW:", data.index)
                        print("COLUMN:", data.columns)
                        start_row = int(input("Enter starting row index: "))
                        end_row = int(input('Enter ending row index: '))
                        start_col = input("Enter starting column index: ")
                        end_col = input("Enter ending column index: ")
                        print(data.loc[start_row:end_row, start_col:end_col])
                        break  # Break out of the loop if the input is valid
                    except KeyError:
                        print("Error: Invalid row/column index. Please enter valid indices.")

            elif operation == 5:
                # Add/Modify Column
                while True:
                    try:
                        print("COLUMNS:", data.columns)
                        col_name = input("ENTER THE COLUMN HEADING: ")
                        col_values = input("ENTER THE VALUES: ")
                        data[col_name] = col_values
                        print(data)
                        break  # Break out of the loop if the input is valid
                    except ValueError:
                        print("Error: Invalid values. Please enter valid values.")

            elif operation == 6:
                # Add/Modify Row
                while True:
                    try:
                        print("ROW:", data.index)
                        row_label = int(input("ENTER ROW HEADING: "))
                        row_values = input("ENTER VALUES: ")
                        data.loc[row_label, :] = row_values
                        print(data)
                        break  # Break out of the loop if the input is valid
                    except ValueError:
                        print("Error: Invalid values. Please enter valid values.")

            elif operation == 7:
                # Modify Single Cell
                while True:
                    try:
                        print("ROW LABELS:", data.index)
                        print("COLUMN LABELS:", data.columns)
                        row_label = int(input("ENTER ROW LABEL: "))
                        col_label = input("ENTER COLUMN LABEL: ")
                        new_value = int(input("ENTER NEW VALUE: "))
                        data.loc[row_label, col_label] = new_value
                        print(data)
                        break  # Break out of the loop if the input is valid
                    except KeyError:
                        print("Error: Invalid row/column label. Please enter a valid label.")

            elif operation == 8:
                # Delete Row/Column
                while True:
                    try:
                        print('ROW:', data.index)
                        print('COLUMN:', data.columns)
                        try:
                            axis = int(input("SPECIFY THE AXIS (0 for row, 1 for column): "))
                        except ValueError:
                            print("Invalid input. Please enter 0 for row or 1 for column.")

                        if axis == 0:
                            try:
                                label = int(input("ENTER ROW/COLUMN HEADING: "))
                                data = data.drop(label)
                            except KeyError:
                                print(f"Row with label '{label}' not found.")
                        else:
                            try:
                                label =(input("ENTER ROW/COLUMN HEADING: "))
                                data = data.drop([label], axis=1)
                            except KeyError:
                                print(f"Column with label '{label}' not found.")

                        print(data)
                        break  # exit the loop after successful deletion
                    except KeyError:
                        print("Error: Invalid column or row label. Please enter a valid label.")

            elif operation == 9:
                # Rename Row/Column
                while True:
                    try:
                        print('ROW:', data.index)
                        print('COLUMN:', data.columns)
                        rename_type = int(input("""WANT TO RENAME:
    1. ROW
    2. COLUMN
    Enter your choice: """))
                        old_label = int(input("Enter OLD ROW/COLUMN NAME: "))
                        new_label = input("Enter NEW ROW/COLUMN NAME: ")

                        if rename_type == 1:
                            data.rename(index={old_label: new_label}, inplace=True)
                        elif rename_type == 2:
                            data.rename(columns={old_label: new_label}, inplace=True)
                        print(data)
                        break  # Break out of the loop if the input is valid
                    except KeyError:
                        print("Error: Invalid row/column name. Please enter a valid name.")

        elif choice == 2:
            # Sub-menu for Analyzing ADANIPORTS Share using matplotlib.pyplot
            print("""1. DATA VISUALIZATION REPRESENTATION
2. TOOLS""")

            # Take user input for the sub-menu choice
            analyze_choice = int(input("Enter your analysis choice: "))

            if analyze_choice == 1:
                # Sub-menu for Pictorial Representation
                print("""1. PLOT A LINE GRAPH
2. PLOT A BAR GRAPH
3. PLOT A SCATTER PLOT
4. PLOT A HISTOGRAM
5. PLOT A PIE CHART""")

                # Take user input for the sub-menu choice
                plot_choice = int(input("Enter your plot choice: "))

                if plot_choice == 1:
                    while True:
                        try:
                            # Plot a Line Graph
                            print('1. SINGLE LINE GRAPH')
                            print('2. MULTIPLE LINE GRAPH')
                            line_choice = int(input("Enter graph type: "))

                            if line_choice == 1:
                                while True:
                                    try:
                                        print('COLUMN:', data.columns)
                                        column_name = input('Enter COLUMN HEADING: ')
                                        plt.plot(data.index, data[column_name])
                                        plt.title('ADANI PORTS:Line Graph of ' + column_name)
                                        plt.xlabel('Index')
                                        plt.ylabel(column_name)
                                        plt.show()
                                        break
                                    except KeyError:
                                        print("Error: Invalid column name. Please enter a valid column name.")

                            elif line_choice == 2:
                                while True:
                                    try:
                                        print('COLUMNS:', data.columns)
                                        columns_to_plot = input('Enter COLUMN HEADINGS (comma-separated): ').split(',')
                                        for col in columns_to_plot:
                                            plt.plot(data.index, data[col], label=col)

                                        plt.title('ADANI PORTS:Multiple Line Graph')
                                        plt.xlabel('Index')
                                        plt.ylabel('Values')
                                        plt.legend()
                                        plt.show()
                                        break
                                    except KeyError:
                                        print("Error: Invalid column name. Please enter a valid column name.")

                        except ValueError:
                            print("Error: Invalid input. Please enter a valid choice.")

                elif plot_choice == 2:
                    while True:
                        try:
                            # Plot a Bar Graph
                            print('1. SINGLE BAR GRAPH')
                            print('2. MULTIPLE BAR GRAPH')
                            bar_choice = int(input("Enter graph type: "))

                            if bar_choice == 1:
                                while True:
                                    try:
                                        # Plot a Single Bar Graph
                                        print('COLUMN:', data.columns)
                                        column_name = input('Enter COLUMN HEADING: ')
                                        plt.bar(data.index, data[column_name])
                                        plt.title('ADANI PORTS:Bar Graph of ' + column_name)
                                        plt.xlabel('Index')
                                        plt.ylabel(column_name)
                                        plt.show()
                                        break
                                    except KeyError:
                                        print("Error: Invalid column name. Please enter a valid column name.")

                            elif bar_choice == 2:
                                while True:
                                    try:
                                        # Plot Multiple Bar Graph
                                        print('COLUMNS:', data.columns)
                                        x = np.arange(len(data))
                                        columns_to_plot = input('Enter COLUMN HEADINGS (comma-separated): ').split(',')
                                        for col in columns_to_plot:
                                            plt.bar(x+0.25, data[col], label=col)
                                        plt.title('ADANI PORTS:Multiple bar graph')
                                        plt.xlabel('Index')
                                        plt.ylabel('Values')
                                        plt.legend()
                                        plt.show()
                                        break
                                    except KeyError:
                                        print("Error: Invalid column name. Please enter a valid column name.")
                        except ValueError:
                            print("Error: Invalid input. Please enter a valid choice.")
#print('COLUMNS:', data.columns): This line prints the column headings of the DataFrame data.
#x = np.arange(len(data)): It creates an array x that represents the positions on the x-axis for the bars. It assumes that the DataFrame data has a length, and np.arange(len(data)) generates an array of integers from 0 to len(data)-1.
#columns_to_plot = input('Enter COLUMN HEADINGS (comma-separated): ').split(','): It takes user input for the column headings they want to plot. The input is assumed to be a comma-separated list of column headings, and split(',') is used to split this input into a list.
#for col in columns_to_plot:: This sets up a loop that iterates over each column heading in the columns_to_plot list.
#plt.bar(x + 0.25, data[col], label=col): Inside the loop, this line creates a bar plot using the plt.bar() function from the matplotlib library.
#x + 0.25: It offsets the x-coordinates for each bar to avoid overlap. This is done to make the bars more distinguishable.
#data[col]: It assumes that data is a DataFrame, and data[col] refers to the values in the column specified by the current iteration of the loop. These values are used as the heights of the bars.
#label=col: It assigns a label to the bars, using the current column heading as the label. This label will be used in the legend to identify each set of bars.

                elif plot_choice == 3:
                    while True:
                        try:
                            # Plot a Scatter Plot
                            print('1. SINGLE SCATTER PLOT')
                            print('2. MULTIPLE SCATTER PLOT')
                            scatter_choice = int(input("Enter scatter plot type: "))

                            if scatter_choice == 1:
                                while True:
                                    try:
                                        # Plot a Single Scatter Plot
                                        print('COLUMNS:', data.columns)
                                        x_col = input('Enter X-AXIS COLUMN HEADING: ')
                                        y_col = input('Enter Y-AXIS COLUMN HEADING: ')
                                        plt.scatter(data[x_col], data[y_col])
                                        plt.title(f'ADANI PORTS:Scatter Plot of {x_col} vs {y_col}')
                                        plt.xlabel(x_col)
                                        plt.ylabel(y_col)
                                        plt.show()
                                        break
                                    except KeyError:
                                        print("Error: Invalid column name. Please enter a valid column name.")

                            elif scatter_choice == 2:
                                while True:
                                    try:
                                        # Plot Multiple Scatter Plot
                                        print('COLUMNS:', data.columns)
                                        x_col = input('Enter X-AXIS COLUMN HEADING: ')
                                        columns_to_plot = input(
                                            'Enter Y-AXIS COLUMN HEADINGS (comma-separated): ').split(',')
                                        for col in columns_to_plot:
                                            plt.scatter(data[x_col], data[col], label=col)

                                        plt.title(f'ADANI PORTS:Multiple Scatter Plot')
                                        plt.xlabel(x_col)
                                        plt.ylabel('Values')
                                        plt.legend()
                                        plt.show()
                                        break
                                    except KeyError:
                                        print("Error: Invalid column name. Please enter a valid column name.")

                        except ValueError:
                            print("Error: Invalid input. Please enter a valid choice.")

                elif plot_choice == 4:
                    while True:
                        try:
                            # Plot a Histogram
                            print('COLUMNS:', data.columns)
                            column_name = input('Enter COLUMN HEADING: ')
                            #The Formula Used To Find The Bins Are 1+log2(N) Which Is Sturges' Rule
                            plt.hist(data[column_name], bins=int(1 + np.log2(len(data))))
                            plt.title(f'ADANI PORTS:Histogram of {column_name}')
                            plt.xlabel(column_name)
                            plt.ylabel('Frequency')
                            plt.show()
                            break
                        except KeyError:
                            print("Error: Invalid column name. Please enter a valid column name.")

                elif plot_choice == 5:
                    while True:
                        try:
                            # Plot a Pie Chart
                            print('COLUMNS:', data.columns)
                            column_name = input('Enter COLUMN HEADING for Pie Chart: ')
                            labels = data.index
                            sizes = data[column_name]
                            plt.pie(sizes, labels=labels)
                            plt.title(f'ADANI PORTS:Pie Chart of {column_name}')
                            plt.show()
                            break
                        except KeyError:
                            print("Error: Invalid column name. Please enter a valid column name.")

            elif analyze_choice == 2:
                # Sub-menu for Tools (you can add more tools as needed)
                print("1. SUM")
                print("2. AVERAGE")
                print("3. MAXIMUM")
                print("4. MINIMUM")

                aggregate_choice = int(input("Enter your aggregate function choice: "))
                while True:
                    try:
                        if aggregate_choice in [1, 2, 3, 4]:
                            print("COLUMNS:", data.columns)
                            aggregate_column = input("Enter the COLUMN HEADING for aggregation: ")

                            if aggregate_choice == 1:
                                result = data[aggregate_column].sum()
                            elif aggregate_choice == 2:
                                result = data[aggregate_column].mean()
                            elif aggregate_choice == 3:
                                result = data[aggregate_column].max()
                            elif aggregate_choice == 4:
                                result = data[aggregate_column].min()

                            print(f"The result of {aggregate_column} using the chosen aggregate function is: {result}")
                            break  # Break out of the loop if the input is valid
                        else:
                            print("Invalid aggregate function choice.")
                            break  # Break out of the loop if the input is invalid
                    except KeyError as e:
                        print(f"Error: {e}. Please check your input.")

        elif choice == 3:
            # Sub-menu for displaying details about the DataFrame
            print("1. DISPLAY DATAFRAME")
            print("2. DISPLAY IN TRANSPOSE")
            print("3. DISPLAY DIMENSION")
            print("4. DISPLAY SHAPE")
            print("5. DISPLAY SIZE")
            print("6. DISPLAY DATATYPE")

            # Take user input for the sub-menu choice
            display_choice = int(input("Enter your display choice: "))

            if display_choice == 1:
                print(data)
            elif display_choice == 2:
                print(data.T)
            elif display_choice == 3:
                print("Dimension:", data.ndim)
            elif display_choice == 4:
                print("Shape:", data.shape)
            elif display_choice == 5:
                print("Size:", data.size)
            elif display_choice == 6:
                print("Data Types:")
                print(data.dtypes)

        elif choice == 4:
            # Exit the program
            print("THE PROJECT WAS SUCCESSFULLY COMPLETED BY GNANAV & CALVIN 12C")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THANK YOU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
    except ValueError as e:
        print(f"Error: {e}. Please check your input.")
print()
