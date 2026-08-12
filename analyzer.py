import pandas as pd
import os
import logging

logger = logging.getLogger("app")

class Analyzer:

    def __init__(self):
        self.file = None
        self.data = None
        if not os.path.exists("./CSV"):
            logger.error("No CSV directory found.")
            raise FileNotFoundError("The './CSV' directory does not exist.")
        else:
            for files in os.listdir("./CSV"):
                logger.info(f"checking for {files}")
                if files.endswith(".csv"):
                    self.file = files
                    break

        if self.file is not None:
            full_path = os.path.join("./CSV", self.file)
            self.data = pd.read_csv(full_path)
            logger.info(f"Successfully loaded {self.file}")
        else:
            logger.error("No CSV file found in ./CSV folder.")
            raise FileNotFoundError("No CSV file found in the './CSV' directory.")

    def get_column_names(self):
        return self.data.columns.to_list()

    def get_row_names(self):
        return self.data.index.to_list()

    def get_column_data(self, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        return self.data[[column_name]].to_markdown()

    def get_rows(self, start, end):
        maxdt = len(self.data.index)
        if maxdt < start or maxdt < end:
            logger.error("start or end are out of range.")
            raise KeyError(f"Error: {start} and {end} are out of range.")

        if start > end:
            return self.data.loc[end:start, :].to_markdown()
        else:
            return self.data.loc[start:end, :].to_markdown()

    def single_value(self, row_name, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        if row_name not in self.data.index:
            logger.error("row not found in dataframe.")
            raise KeyError(f"Error: {row_name} not found in dataframe.")
        return self.data.loc[row_name, column_name]

    def slice_data(self, row_start, row_end, column_start, column_end):
        try:
            result = self.data.loc[row_start:row_end, column_start:column_end]
            if result.empty:
                logger.warning(
                    f"Slicing returned empty data for bounds: rows {row_start}-{row_end}, cols {column_start}-{column_end}")
            return result.to_markdown()
        except KeyError as e:
            logger.error(f"KeyError during slicing: Invalid column or row label provided. Error: {e}")
            raise KeyError(f"Error: Could not slice. Ensure columns '{column_start}' and '{column_end}' exist.")
        except TypeError as e:
            logger.error(f"TypeError during slicing: {e}")
            raise TypeError("Error: Invalid input type. Rows should be numbers, columns should be text.")

    def modify_column(self, column_name, new_value):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        self.data[column_name] = new_value
        logger.info(f"Column {column_name} updated to {new_value}")
        return f"Success: Column '{column_name}' updated to {new_value}."

    def modify_row(self, row_index, row_value):
        if row_index not in self.data.index:
            logger.error("row not found in dataframe.")
            raise KeyError(f"Error: {row_index} not found in dataframe.")
        self.data.loc[row_index, :] = row_value
        logger.info("The Data has been modified Successfully.")
        return f"Success: Row {row_index} updated to {row_value}."

    def modify_single_cell(self, row_index, column_name, new_value):
        if row_index not in self.data.index:
            logger.error("row not found in dataframe.")
            raise KeyError(f"Error: {row_index} not found in dataframe.")
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        self.data.loc[row_index, column_name] = new_value
        logger.info("The Data has been modified Successfully.")
        return f"Success: Cell at row {row_index}, column '{column_name}' updated to {new_value}."

    def delete_row_or_column(self, axis, label):
        try:
            if axis == 0:
                self.data = self.data.drop(label, axis=0)
                return f"Success: Row {label} deleted."
            if axis == 1:
                self.data = self.data.drop(label, axis=1)
                return f"Success: Column '{label}' deleted."
        except KeyError as e:
            logger.error(f"Error: unable to delete row or column {label} from dataframe. error: {e}")
            raise KeyError(f"Error: Could not delete row or column {label} from dataframe.")

    def rename_column(self, old_label, new_label):
        try:
            self.data = self.data.rename(columns={old_label: new_label})
            return f"Success: Column '{old_label}' renamed to '{new_label}'."
        except KeyError as e:
            logger.error(f"Error: unable to rename column {old_label} from dataframe. error: {e}")
            raise KeyError(f"Error: Could not rename column '{old_label}'.")

    def rename_row(self, old_label, new_label):
        try:
            self.data = self.data.rename(index={old_label: new_label})
            return f"Success: Row {old_label} renamed to {new_label}."
        except KeyError as e:
            logger.error(f"Error: unable to rename row {old_label} from dataframe. error: {e}")
            raise KeyError(f"Error: Could not rename row {old_label}.")

    def get_multiple_columns(self, columname_list):
        for cols in columname_list:
            if cols not in self.data.columns:
                logger.error(f"Column {cols} not found in dataframe.")
                raise KeyError(f"Error: '{cols}' not found in dataframe.")
        return self.data[columname_list].to_markdown()

    def data_sum(self, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        return round(self.data[column_name].sum(), 2)

    def data_mean(self, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        return round(self.data[column_name].mean(), 2)

    def data_median(self, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        return round(self.data[column_name].median(), 2)

    def data_mode(self, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        return self.data[column_name].mode().tolist()

    def data_max(self, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        return round(self.data[column_name].max(), 2)

    def data_min(self, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        return round(self.data[column_name].min(), 2)

    def data_std(self, column_name):
        if column_name not in self.data.columns:
            logger.error(f"Column {column_name} not found in dataframe.")
            raise KeyError(f"Error: {column_name} not found in dataframe.")
        return round(self.data[column_name].std(), 2)

    def get_dataframe(self):
        return self.data.to_markdown()

    def get_transposed_dataframe(self):
        return self.data.T.to_markdown()

    def get_dataframe_metadata(self):
        return {
            "Dimension": self.data.ndim,
            "Shape": self.data.shape,
            "Size": self.data.size,
            "Data Types": self.data.dtypes.to_string()
        }

    def save_copy_to_csv(self, new_filename):
        """Exports the current state of self.data to a new CSV file."""
        try:
            if not new_filename.endswith('.csv'):
                new_filename += '.csv'
            if not os.path.exists("./COPY_CSV"):
                os.mkdir("./COPY_CSV")
            if new_filename in os.listdir("./COPY_CSV"):
                logger.warning(f"File {new_filename} already exists.")
                new_filename = new_filename.replace('.csv', '_copy.csv')
            self.data.to_csv(f"./COPY_CSV/{new_filename}", index=False)
            logger.info(f"Successfully saved modified dataset to {new_filename}")
            return f"Success: File saved as '{new_filename}'"

        except Exception as e:
            logger.error(f"Failed to save CSV copy: {e}")
            raise IOError(f"Error: Could not save the file. System returned: {e}")