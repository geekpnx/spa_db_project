# **STORES PRICING ANALYTICS (SPA) CLI APP**

![spa](assets/SPA_Overview.gif)

## **DESCRIPTION**

The purpose of this CLI application is to collect data from different stores, based on the product, prices and compare them before you decide to purchase things.  

## **USAGE**

### **Step 1.** Virtual Environment (with venv)

- Create venv by running the command

  **`python3 -m venv .venv --prompt spa`**

- Activate venv

  **`source .venv/bin/activate`**

### **Step 2.** Install required modules/libraries

- command below will automatically install dependencies

  **`pip install -r requirements.txt`**

### **Step 3.** Setup Database

- Go to initspa directory
  **`cd initspa/`**

- and run command
  **`python3 -m initspa`**

> #### ***Note:***  

> *What happens when you run the last script above?*

> - *It will create user admin Database with the name  **`spa_admin`**, for this we need to access **PSQL** using the default **postgres** user. Therefor you will need to enter **postgres** default password '`postgres`'(without single quote) if you haven't changed it already. If you did you might need to enter the one you have set.*

> - *The program will ask you to login to **postgres** Database using your the new username '**spa_admin**' we have created, all you needed to do here is to enter the password that has been set by the program and that is '`password`' (without single quote).*

> - *After tables will be created and data sample data will be inserted automatically.*

### **Step 4.** Run the CLI SPA APP

- Just by enter the command: **`spa`**
