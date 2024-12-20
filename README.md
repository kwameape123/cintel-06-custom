# cintel-06-custom
## Author: Arnold Atchoe
## Date: 12/02/2024

## Project Description

The goal of this project is to create an interactive dashboard app that allows users to 
visualize live data. The App.py is designed to retrieve and display a range of financial market data. This includes capital market data, such as historical stock information, as well as real-time foreign exchange (forex) data on various currency exchange rates.

## Data Description

Historical stock data includes the open and closing prices for the last day of the month, the high and low prices throughout the month, the adjusted closing price on the last day, and the trading volume for the month. Capital market data provides general information about a listed company, along with various financial statements. The terms and column names adhere to widely accepted definitions. As for forex data, it contains information such as currency symbols, currency names, bid and ask prices, exchange rates, the date and time when the data was last updated, and the associated time zone.

## Data Cleaning and transformation

Dataset used for this project was in an acceptable format and state.

## Project Execution

### Prep Development Environment
Determine and prepare the tools require to execute project successfully.

1. Install latest version of python.
2. Install latest version of Git for version control.
3. Install VS Code as a Code editor.
4. Download and enable python and shiny extension for VS Code.
5. Create and activate python project virtual environment(.venv). Virtual enivroment keep
project dependencies exclusive.  
```py -m venv .venv```  
```.venv\Scripts\activate```  
6. Install project dependencies and libraries.  
```py -m pip install -r requirements.txt```  
The requirements.txt file contains a list of all projedct dependencies to allow for easy installation.  

#### Notes(In terminal):
1. Configure git with username and email used in github with the following lines of code;  
```git config --global user.name "Your Name"```  
```git config --global user.email "youremail@example.com"```  
2. Check python version, Git version and confriguration with following lines of code;  
 ```py --version```  
```git --version```  
 ```git config user.name```  
 ```git config user.email```  

### Run App
Launch app in web browser by running ```shiny run --reload --launch-browser penguins/app.py``` in terminal.  
Terminal becomes occupied after running this code hence another terminal must be used for other tasks.  

### Build App to Docs folder and Test locally.
Keep virtual environment active for this step.  

1. Remove any existing static assets using terminal command ```shiny static-assets remove```.  
2. Export the contents of penguins folder to docs folder to build a web app using shinylive export.  
    Docs folder is created if it does not exist. Terminal command used is  
```shinylive export dashboard docs```  
3. Edit index.html file to modify web app browser tab to include custom title and favicon.Favicon used was generate on  
    (https://favicon.io/).(https://favicon.io/) provides instructions on implement favicons. Section of index.html edited  
    is shown below;  
```<title>Arnold Atchoe-Financial Market</title>```  
```<link rel="icon" type="image/x-icon" href="./favicon.ico">```  
4. Test app in browser using the link generated by terminal command  
 ```py -m http.server --directory docs --bind localhost 8008```.  
 
 Note: Push app to GitHub Repo before publishing
### Publish App with GitHub Pages
GitHub pages hosts this web application. An initial confriguration is done to setup pages for repository 
containing the web app. After, any subsequent update pushed to repository will be reflected in the web 
application.  

 1. Go the settings tab of the web app repository.  
 2. Scroll to the bottom of the page and click the pages section.  
 3. Select branch main as the source for the site.  
 4. Change from the root folder to the docs folder as publishing source.  
 5. Click Save and wait for the site to build.  
 6. Edit the "About" section of the repository to include a link to the live app.  

## Resoruces  

Alpha Vantage API documentation:
https://www.alphavantage.co/documentation/#  



