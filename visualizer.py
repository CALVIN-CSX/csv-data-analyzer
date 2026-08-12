import matplotlib.pyplot as plt
import logging
import numpy as np

plt.style.use('ggplot')
logger = logging.getLogger("app")

def single_line_graph(name, dataFrame, columname):
    try:
        fig, ax = plt.subplots()
        ax.plot(dataFrame.index, dataFrame[columname])
        ax.set_xlabel(dataFrame.index.name or "Index")
        ax.set_ylabel(columname)
        ax.set_title(f"Single Line Graph of {name}")
        plt.show()
    except Exception as e:
        logger.error(e)
        raise KeyError(f"Error: {e}")

def multi_line_graph(name, dataFrame, colums_to_plot):
    try:
        fig, ax = plt.subplots()
        for col in colums_to_plot:
            ax.plot(dataFrame.index, dataFrame[col], label=col)
        ax.set_xlabel(dataFrame.index.name or "Index")
        ax.set_ylabel("Values")
        ax.legend()
        ax.set_title(f"Multiple Line Graph of {name}")
        plt.show()
    except Exception as e:
        logger.error(e)
        raise KeyError(f"Error: {e}")

def single_bar_graph(name, dataFrame, columname):
    try:
        fig, ax = plt.subplots()
        ax.bar(dataFrame.index, dataFrame[columname])
        ax.set_xlabel(dataFrame.index.name or "Index")
        ax.set_ylabel(columname)
        ax.set_title(f"Single Bar Graph of {name}")
        plt.show()
    except Exception as e:
        logger.error(e)
        raise KeyError(f"Error: {e}")

def multi_bar_graph(name, dataFrame, columname):
    try:
        fig, ax = plt.subplots()
        x = np.arange(len(dataFrame))
        width = 0.2
        for i, col in enumerate(columname):
            ax.bar(x + (i * width), dataFrame[col], width=width, label=col)
        ax.set_xlabel(dataFrame.index.name or "Index")
        ax.set_ylabel("Values")
        ax.legend()
        ax.set_title(f"Multiple Bar Graph of {name}")
        plt.show()
    except Exception as e:
        logger.error(e)
        raise KeyError(f"Error: {e}")

def scatter_graph(name, dataFrame, rowname, columnname):
    try:
        fig, ax = plt.subplots()
        ax.scatter(dataFrame[rowname], dataFrame[columnname])
        ax.set_xlabel(rowname)
        ax.set_ylabel(columnname)
        ax.set_title(f"Scatter Graph of {name}")
        plt.show()
    except Exception as e:
        logger.error(e)
        raise KeyError(f"Error: {e}")

def multiple_scatter_graph(name, dataFrame, rowname, columnname):
    try:
        fig, ax = plt.subplots()
        for col in columnname:
            ax.scatter(dataFrame[rowname], dataFrame[col], label=col)
        ax.set_xlabel(rowname)
        ax.set_ylabel("Values")
        ax.legend()
        ax.set_title(f"Multiple Scatter Graph of {name}")
        plt.show()
    except Exception as e:
        logger.error(e)
        raise KeyError(f"Error: {e}")

def histogram(name, dataFrame, columname):
    try:
        fig, ax = plt.subplots()
        ax.hist(dataFrame[columname], bins=int(1+np.log2(len(dataFrame))))
        ax.set_xlabel(columname)
        ax.set_ylabel("Frequency")
        ax.set_title(f"Histogram of {name}")
        plt.show()
    except Exception as e:
        logger.error(e)
        raise KeyError(f"Error: {e}")

def pie_chart(name, dataFrame, columname):
    try:
        fig, ax = plt.subplots()
        labels = dataFrame[columname].index.tolist()
        ax.pie(dataFrame[columname], labels=labels)
        plt.title(f"Pie Chart of {columname} from {name}")
        plt.show()
    except Exception as e:
        logger.error(e)
        raise KeyError(f"Error: {e}")