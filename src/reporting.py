import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
from datetime import datetime
import os

from reporting.data_analyze import *

def generate_pdf(plot_img_path, data, output_path='./outputs/report.pdf'):
    # save FPDF() class into a 
    # variable pdf
    now = datetime.now()
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    
    # create a cell
    pdf.cell(200, 10, txt = "Report of stock", 
            ln = 1, align = 'C')
    
    # add another cell
    pdf.cell(200, 10, txt = f"Date: {now.strftime('%d-%B-%Y_%H-%M')}",
            ln = 2, align = 'C')
    
    pdf.image(name=plot_img_path, w=210)

    pdf.set_font("Arial", size = 10)
    
    # create a cell
    pdf.cell(200, 10, txt = f"Best Stock Day: {data['best_stock_day']}", 
            ln = 1, align = 'L')

    pdf.cell(200, 10, txt = f"Worst Stock Day: {data['worst_stock_day']}", 
            ln = 1, align = 'L')

    pdf.cell(200, 10, txt = f"Amount of data: {data['stored_data_len']}", 
            ln = 1, align = 'L')

    pdf.output(output_path)   


if __name__ == "__main__":
    script_path = os.path.dirname(os.path.realpath(__file__))
    df_apple = get_data_frame(file_path=f'{script_path}/outputs/gathered_data.csv')
    plt = get_plot(df_apple)
    plot_img_path = save_plot(plt, file_path=f'{script_path}/outputs/plot.png')
    data = get_report_data(df_apple)

    generate_pdf(plot_img_path, data, output_path=f"{script_path}/outputs/report.pdf")