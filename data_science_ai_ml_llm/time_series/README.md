# TIME SERIES MODELLING

## TL;DR
Just read the entire [blog](https://www.linkedin.com/pulse/time-series-forecasting-demand-use-case-pradeep-macharla/)


## Minimal Context

Advanced data Science & statistical modelling techniques existed and flourished in the past 5-10 years. The maturity and reliability of the models are also very high as long as you know which modelling technique to fit & transform your data into (and all the preprocessing, feature engineering etc. work ). scikit-learn library already provides initial guidance for selecting model this

## Classical methods challenges
- Focus on complete data: missing or corrupt data is generally unsupported
- Focus on linear relationships: assuming a linear relationship excludes more complex joint distributions
- Focus on fixed temporal dependence: the relationship between observations at different times, and in turn the number of lag observations provided as input, must be diagnosed and specified
- Focus on univariate data: many real-world problems have multiple input variables
- Focus on one-step forecasts: many real-world problems require forecasts with a long time horizon

## Prediction of demand 
of a product is a unique and complex case because in addition to all the conventional modelling

- Seasonality, trend, holiday effects etc make this prediction problem a time series modelling problem (temporal dependence between observations)
- Once you get into time series modelling domain - you will learn quickly that it is no longer a simple scale-fit-transform (or some other order) loop OR some form of from-pretrained-tokenize-embed-collate-optimize loop in ML / deep learning techniques
- You have to model processes like AR (autoregression which means an observation is dependent on n previous observations), MA (moving average meaning an observation can be modelled as an average of m observations surrounding it)
- Exogenous variable values like holidays, events like super-bowl , soccer, olympics and many more have to be taken into account (e.g. beer sales are up during super-bowl and soccer events, turkey during thanks-giving etc.)
- Many more...


## HOW

- First read the [blog](https://www.linkedin.com/pulse/time-series-forecasting-demand-use-case-pradeep-macharla/)
- Open notebooks and execute the code to internalize the concepts and put into action
    - ARIMA MODEL: [SAMPLE_ARIMA_OUTPUT.ipynb](./SAMPLE_ARIMA_OUTPUT.ipynb)
    - SARIMAX MODEL: [SAMPLE_SARIMAX_EXOG_OUTPUT.ipynb](SAMPLE_SARIMAX_EXOG_OUTPUT.ipynb)
    - PROPHET MODEL : [PROPHET_weekly.ipynb](./PROPHET_weekly.ipynb)
    - NEURAL PROPHET MODEL: [NEURAL_PROPHET.ipynb](./NEURAL_PROPHET.ipynb)
    - LAUNCH WEB SERVER AND PLAY WITH THE APP: See instructions below
    
### Gradio app

All official documentation for [gradio](https://www.gradio.app/)

- git clone `https://github.com/techsparksguru/data_ai_for_all`
- cd `data_science_ai_ml_llm/data_science_ai_ml_llm`

#### Notebook POC

- Get your python environment ready (conda or pyenv is what I recommed and 3.10.x version)
- once you have activated your python environment `pip3 install -r gradio/requirements.txt`
- Open [POC.ipynb](./gradio/POC.ipynb) in your favorite notebook environment 
- Replace `server_name="192.168.0.111"` with your own internal IP address (or public IP/domain if you wish to expose publically) . Generally on your home network you would either have your ip as 192.168.* or 10.0.* or 172.16.* etc. You can read all the [network stuff](https://www.ibm.com/docs/en/networkmanager/4.2.0?topic=translation-private-address-ranges)
- Generally I do `ifconfig | grep 192` to determine my private address
- You can completely remove `server_name="192.168.0.111"` as parameter to `demo.launch(..)` and that will launch the webserver on localhost and that is fine too. I generally use one machine as my desktop and all my code and server on another machine in the network, hence this workaround of determining IP
- The notebook POC will launch the webserver and you can interact with the app on `http://<ip>:7860` OR `http://localhost:7860`

### Standalone webserver
- If you are more used to launching Flask like webserver , then that is also availabe in app.py
- Start server `cd gradio && python3 app.py`
- You can run `gradio app.py` to hot reload for changes in files, however if other processes (like jupyter which creates checkpoints .ipynb_checkpoints etc.) is already using the same workspace , then gradio might error out "too many files in open state -ish". So I skipped this option. At the POC stage, it is okay to stop-start server many times, as I wanted to get it up and running first