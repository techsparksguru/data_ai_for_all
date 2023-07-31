import gradio as gr
from datetime import date
import pandas as pd
from prophet import Prophet
pd.options.plotting.backend = "plotly"

from lib.helpers import *

with gr.Blocks() as demo:
    gr.Markdown(
    """
    **DEMAND FORECASTING 📈 USING AI/ML** : Select UPC & RETAILER values to see demand forecasted graphs. The [ source code for this demo is here](https://github.com/techsparksguru/data_ai_for_all/tree/master).
    """)
    with gr.Row():
        upc = gr.Dropdown(["987654321"], label="UPC", value="987654321")
        retailer = gr.Dropdown(["3"], label="RETAILER", value="3")
    
    plt = gr.Plot()
    plt_components = gr.Plot()
    
    with gr.Row():
        dataframe = gr.DataFrame(overflow_row_behaviour="paginate", max_rows=10, 
                                 label="FORECAST TABLE",show_label=True)
    with gr.Row():    
        button = gr.Button("Export Forecast CSV")
        csv = gr.File(interactive=False, visible=False)


    
    upc.change(get_forecast, [upc, retailer], [plt,plt_components,dataframe], queue=False)
    retailer.change(get_forecast, [upc, retailer], [plt,plt_components,dataframe], queue=False)    
    demo.load(get_forecast, [upc, retailer], [plt,plt_components,dataframe], queue=False)  
    
    button.click(export_csv, dataframe, csv)

    
if __name__ == "__main__":
    demo.launch(share=False,server_name="192.168.0.111",ssl_verify=False,inbrowser=True, debug=True)