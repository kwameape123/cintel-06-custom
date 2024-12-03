import pathlib as pt
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.foreignexchange import ForeignExchange
from faicons import icon_svg
from shiny import reactive
from shiny.express import input, render, ui
from shiny.ui import output_ui
from shinywidgets import render_plotly
from stocks import stocks
from currencies import currency_codes

# Define API key
API_key = 'WTFEVW7AXQOQ7WQP'

# UI page setup
ui.page_opts(title="Stock Market Explorer", fillable=True)

# Sidebar with stock ticker selection and date range input
with ui.sidebar():
    ui.input_selectize(id="ticker", label="Select Stocks", choices=stocks, selected="AAPL")
    ui.input_selectize(  id="local_currency",label="Select local Currency",choices=currency_codes,
                       selected="United States Dollar")
    ui.input_selectize(  id="foreign_currency",label="Select foreign Currency",choices=currency_codes,
                       selected="Euro")
    ui.input_numeric("foreign_amount", "Amount in foreign Currency to buy", 1, min=1, max=1e6)

# Reactive function to fetch stock data based on selected ticker and date range
@reactive.calc
def get_ts_data():
    # Activate the API client with the key
    ts = TimeSeries(key=API_key, output_format='pandas')
    
    # Get the selected ticker symbol
    ticker = input.ticker()  # Get ticker selected by the user
    
    # Fetch the monthly data from Alpha Vantage API
    data, metadata = ts.get_monthly_adjusted(ticker)  # You can choose 'get_monthly' or 'get_monthly_adjusted'
    
    return data
    
@reactive.calc
def get_fd_data():
    # Activate the API client with the key
    fd =FundamentalData(API_key,output_format='pandas')

    #Get the selected tcker symbol
    ticker =input.ticker()

    # Fetch fundamental data from Alpha Vantage API
    data1=fd.get_company_overview(ticker)
    data2=fd.get_balance_sheet_annual(ticker)
    data3=fd.get_income_statement_annual(ticker)
    data4=fd.get_cashflow_annual(ticker)
    data5=fd.get_earnings_annual(ticker)
    return data1,data2,data3,data4,data5

@reactive.calc
def realtime_forex():
    # Activate the ForeignExchange client with your API key
    fx = ForeignExchange(key=API_key, output_format='pandas')

    # get local and foreign currency
    local_currency =input.local_currency()
    foreign_currency =input.foreign_currency()

        # Get real-time exchange rate for the given currency pair
    data = fx.get_currency_exchange_rate(from_currency=local_currency,
                                              to_currency=foreign_currency)
        
    return data

    

############################
# OUTPUT COMPONENTS
############################
with ui.hold():

    @render.ui
    def cash_icon():
        icon = icon_svg("money-bills")
        return icon

    @render.ui
    def local_currency_icon():
            currency_symbol =input.local_currency()
            icon = icon_svg(f"{currency_symbol}-sign")
            return icon


    @render.ui
    def foreign_currency_icon():
        currency_symbol =input.foreign_currency()
        icon = icon_svg(f"{currency_symbol}-sign")
        return icon


# Tab setup for UI components
with ui.navset_card_tab(id="tab"):
    with ui.nav_panel("Company Overview"):
        with ui.layout_column_wrap(fill=False):
              @render.data_frame
              def company_overview_df():
              # Get the stock data using the reactive get_fd_data() function
                  data1,data2,data3,data4,data5 = get_fd_data()
    
                  return data1  # Return the formatted data as a data frame for rendering
                
    with ui.nav_panel("Monthly Historical data"):
        with ui.layout_column_wrap(fill=False):
            # Render a Data with the stock dat
            @render.data_frame
            def stock_df():
                # Get the stock data using the reactive get_ts_data() function
                data = get_ts_data()
    
                return data  # Return the formatted data as a data frame for rendering
    with ui.nav_panel("Financial Statements"):
        with ui.accordion(id="acc", open="Balance Sheet"):  
            with ui.accordion_panel("Balance Sheet"):  
                @render.data_frame
                def balance_sheet_df():
                  # Get the stock data using the reactive get_fd_data() function
                  data1,data2,data3,data4,data5 = get_fd_data()
    
                  return data2

            with ui.accordion_panel("Income Statement"):  
                @render.data_frame
                def income_statement_df():
                  # Get the stock data using the reactive get_fd_data() function
                  data1,data2,data3,data4,data5 = get_fd_data()
    
                  return data3

            with ui.accordion_panel("Cash Flow Statement"):  
                @render.data_frame
                def cashflow_statement_df():
                  # Get the stock data using the reactive get_fd_data() function
                  data1,data2,data3,data4,data5 = get_fd_data()
    
                  return data4

            with ui.accordion_panel("Earnings Statement"):  
                @render.data_frame
                def earnings_statement_df():
                  # Get the stock data using the reactive get_fd_data() function
                  data1,data2,data3,data4,data5 = get_fd_data()
    
                  return data5
                    
    with ui.nav_panel("Forex"):
         with ui.value_box(showcase=output_ui("cash_icon")):
            "EXCHANGE RATE INFO"
            @render.ui
            def local_currency_info():
                data=realtime_forex()
                return data
                
         with ui.value_box(showcase=output_ui("foreign_currency_icon")):
            "FOREIGN CURRENCY AMOUNT"
            @render.ui
            async def foreign_currency_amount():
                data=await realtime_forex()
                amount =data["Exchange Rate"]*input.Local_amount()
                return amount
                
        
        
    
        
        
            
