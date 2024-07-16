# **STORES PRICING ANALYTICS (SPA) - CLI APP**

![spa](assets/SPA_Overview.gif)

## **DESCRIPTION**

The purpose of this CLI application is to collect data from different stores, based on the product, prices and compare them before you decide to purchase things.  

## **INSTALL**

### **Step 1.** Setup virtual Environment (with venv)

- Create venv by running the command

  **`python3 -m venv .venv --prompt spa`**

- Activate venv

  **`source .venv/bin/activate`**

### **Step 2.** Install required modules/libraries

- Command below will install the dependencies

  **`pip install -r requirements.txt`**

- This one will install the latest version of SPA package (**`v.11`**):

  **`pip install -i https://test.pypi.org/simple/ spa`**

### **Step 3.** Setup Database

> #### ***Note:***  

> *What happens when you run the last script below in Database Setup process?*
*Please, make sure your **`PostgreSQL`** running and you have the user **`postgres`** exist*
> - *It will create user admin Database with the name  **`spa_admin`**, for this we need to access **PSQL** using the default **postgres** user. Therefor you will need to enter **postgres** password '`postgres`'(without single quote) if you haven't changed it already. If you did you might need to enter the password you have set.*

> - *The program will ask you to login to **postgres** Database using the new username '**spa_admin**', all you needed to do now is, to enter the password that has been set by the program and that is '`password`' (without single quote).*

> - *After tables will be created and sample data will be inserted automatically.*

- Next step, go to initspa directory
  
  **`cd initspa/`**

- and run command
  
  **`python3 -m initspa`**

### **USAGE**

Run the CLI SPA APP

- Just by enter the command: **`spa`**
