from prophet import Prophet
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from prophet.plot import add_changepoints_to_plot
from prophet.make_holidays import make_holidays_df
import prophet.utilities as utils
from IPython.display import display, Markdown

import gradio as gr
from datetime import date
pd.options.plotting.backend = "plotly"

import datetime

pd.set_option("mode.chained_assignment", None)

df_use_case_upcs = pd.read_csv("../data/input_upcs - synthetic-usecases.csv")

def get_forecast(upc, retailer):
    
    # Stores
    df_stores = pd.read_csv("../data/stores.csv")
    
    df_use_cases_upcs_current = df_use_case_upcs[df_use_case_upcs["UPC"]==int(upc)]
    RETAILER_ID = df_use_cases_upcs_current["RETAILER_ID"].values[0]
    PPG = df_use_cases_upcs_current["PPG"].values[0]
    
    df = pd.read_csv("../data/upc_sales.csv")
    
    # DEMO data
    df["DATE"] = pd.to_datetime(df["DATE"])
    df["WEEK"] = df['DATE'].dt.to_period('W').dt.to_timestamp()
    df = pd.merge(df, df_stores, left_on="STOREID", right_on="STORE_ID", how="inner")
    df.rename(columns={"RETAILER_ID_x":"RETAILER_ID", "CITY":"PPG"},inplace=True)
    df.drop(columns=["RETAILER_ID_y","STORE_NAME","STORE_ID"],inplace=True)

    # Group
    df_grouped_volume = df.groupby(["UPC","RETAILER_ID","PPG","WEEK"]).agg(
        {"qty":"sum","mean_unit_price_rounded":"mean"}).reset_index()

    df_grouped_volume.rename(columns={"mean_unit_price_rounded":"mean_unit_price"},inplace=True)
    df_grouped_volume.set_index("WEEK",inplace=True)
    
    df_upc_grouped = df_grouped_volume[(df_grouped_volume["UPC"]==int(upc))
                               &(df_grouped_volume["RETAILER_ID"]==int(retailer))
                               &(df_grouped_volume["PPG"]==PPG)]

    df_upc = df_upc_grouped[["qty","mean_unit_price"]]
    df_upc = df_upc.asfreq('W',method="ffill") #prophet can deal with missing

    df_upc_prophet = df_upc_grouped[["qty","mean_unit_price"]]
    df_upc_prophet.loc[:,"WEEK"] = df_upc_prophet.index
    df_upc_prophet.rename(columns={"qty":"y","WEEK":"ds"},inplace=True)


    FUTURE_PERIODS = 12
    regressors = {"mean_unit_price":
              {"mode":"multiplicative"}}

    plot, plot_components, forecast = create_and_predict_model(df_upc_prophet, regressors, FUTURE_PERIODS, markdown_output=False, output_graphs=False)
    
    return plot, plot_components, forecast

def export_csv(d):
    d.to_csv("output.csv",float_format='%.2f')
    return gr.File.update(value="output.csv", visible=True)


def create_and_predict_model(input_df,regressors,future_periods,markdown_output=True,
                             output_graphs=False,trend_flexibility=0.05,yearly_seasonality=10):
    
    
    year_list = input_df['ds'].dt.year.unique().tolist()
    year_list.append(year_list[-1] + 1)
    holidays = make_holidays_df(year_list=year_list,
                                country='US')

    # yearly_seasonality i.e. fourier order = 4 to address overfit
    m = Prophet(seasonality_mode="multiplicative", 
                 yearly_seasonality=4, daily_seasonality=False,
                 holidays=holidays,changepoint_prior_scale=trend_flexibility)
    # US holidays
    m.add_country_holidays(country_name="US")
    
    for regressor in regressors.keys():
        m.add_regressor(regressor, mode=regressors[regressor]["mode"])
    
    m.fit(input_df)
    future = m.make_future_dataframe(periods=future_periods, freq="W")
    
    random_input_df = input_df.sample(future_periods)
    
    # DERIVE FUTURE REGRESSOR VALUES
    for regressor in regressors.keys():
        future.loc[:,regressor] = input_df[regressor].to_list() + random_input_df[regressor].to_list()
    
    forecast = m.predict(future)  
    
    main_plot = m.plot(forecast, xlabel="WEEK", ylabel="VOLUME")
    add_changepoints_to_plot(main_plot.gca(), m , forecast)
    components_plot = m.plot_components(forecast)
            
    return main_plot,components_plot, forecast