# Software-Development-text-based-hatchery-simulation
# 🐟 Hatchery Simulation (Text-Based Game)

A text-based simulation program of a fish hatchery business built using Python and object-oriented programming (OOP). The hatchery must manage fish species, technicians, supply purchases, and financials to survive and turn a profit quarter by quarter.

---

## 📘 Background

The hatchery sells fish species by the **pond** (unit). The business requires:

- Employees (aquaculture technicians)
- Species-specific supplies
- Vendor selection for restocking
- Financial decisions each quarter

The goal is to **make a profit** and avoid **bankruptcy**.

---

## 📝 Task Overview

You will build a text-based simulation with the following features:

### 🐠 A. Fish Species and Requirements

| Fish Type           | Fertiliser (ml) | Feed (kg) | Salt (kg) | Maintenance Time (days) |
|---------------------|------------------|-----------|-----------|--------------------------|
| Clef Fins           | 100.0            | 12        | 2         | 2.0                      |
| Timpani Snapper     | 50.0             | 9         | 2         | 1.0                      |
| Andalusian Brim     | 90.0             | 6         | 2         | 0.5                      |
| Plagal Cod          | 100.0            | 10        | 2         | 2.0                      |
| Fugue Flounder      | 200.0            | 12        | 2         | 2.5                      |
| Modal Bass          | 300.0            | 12        | 6         | 3.0                      |

---

### 🏢 B. Warehouses

| Supply     | Main Capacity | Aux Capacity | Depreciation/Quarter | Warehouse Cost |
|------------|----------------|---------------|-----------------------|----------------|
| Fertiliser | 20 litres       | 10 litres      | 0.4                   | £0.10/litre    |
| Feed       | 400 kg          | 200 kg         | 0.1                   | £0.001/g       |
| Salt       | 200 kg          | 100 kg         | 0.0                   | £0.001/g       |

- Depreciation uses **ceiling rounding**
- Fixed hatchery cost per quarter: **£1500**
- Starting cash: **£10,000**

---

### 👷‍♂️ C. Technicians

- Paid **£500 per week**
- Work **9 weeks per quarter**
- Paid for **12 weeks**
- Must have **at least 1 technician**
- Max **5 technicians**
- Each technician has a name

---

### 🛒 D. Vendors

| Supplier Name      | Fertiliser (£/l) | Feed (£/g) | Salt (£/g) |
|--------------------|------------------|------------|------------|
| Slippery Lakes     | 0.30             | 0.10       | 0.05       |
| Scaly Wholesaler   | 0.20             | 0.40       | 0.25       |

---

### 📈 E. Customer Demand and Prices

| Fish Species       | Demand/Quarter | Price (£) |
|--------------------|----------------|-----------|
| Clef Fins          | 25             | 250       |
| Timpani Snapper    | 10             | 350       |
| Andalusian Brim    | 15             | 250       |
| Plagal Cod         | 20             | 400       |
| Fugue Flounder     | 30             | 550       |
| Modal Bass         | 50             | 500       |

---

## 🕹️ Simulation Flow

1. Ask how many quarters to simulate (default: 8).
2. Start with warehouses full and £10,000 cash.
3. Each quarter:
   - Add/remove technicians
   - Sell fish (respecting supply, demand, labour)
   - Calculate income
   - Pay technicians
   - Pay fixed costs
   - Depreciate unused supplies
   - Choose a vendor to restock
   - Replenish supplies (if affordable)
   - If cash < 0 → **bankrupt**

---

## 💡 Example Interaction
$ python3 main.py
>>> Please enter number of quarters [default: 8]: 8

================================
====== SIMULATING Quarter 1 ======
================================

To add enter positive, to remove enter negative, no change enter 0.
>>> Enter number of technicians: 2
>>> Enter technician name: James
Hired James, weekly rate = £500
>>> Enter technician name: Richard
Hired Richard, weekly rate = £500

--- Fish Sales (max by demand) ---
Fish Clef Fins (Demand: 25) - Sell: 25
Fish Timpani Snapper (Demand: 10) - Sell: 10
Fish Andalusian Brim (Demand: 15) - Sell: 15
Fish Plagal Cod (Demand: 20) - Sell: 20
Insufficient labour: Required 8.00 weeks, Available 4.50
Insufficient ingredients:
 - Fertiliser: need 2.0, available 25.65
 - Feed: need 200.0, available 120.0
 - Salt: need 40.0, available 200.0

Fish Plagal Cod - Sell: 0
Fish Fugue Flounder - Sell: 0
Fish Modal Bass - Sell: 0

--- Payments ---
Paid James: £6000
Paid Richard: £6000
Fixed expenses (rent/utilities): £1500

--- Warehouse Costs ---
Main Warehouse:
 - Fertiliser: £1.57
 - Feed: £0.00
 - Salt: £100.00
Auxiliary Warehouse:
 - Fertiliser: £1.00
 - Feed: £120.00
 - Salt: £100.00

--- Vendor Selection ---
Available Vendors:
1. Slippery Lakes
2. Scaly Wholesaler
>>> Select vendor (1 or 2): 1

Warehouse restocked successfully.
Hatchery Name: Eastaboga
Cash: £9618.63

Warehouse Status:
 Main - Fertiliser: 20.0 / 20.0
        Feed: 400.0 / 400.0
        Salt: 200.0 / 200.0
 Aux  - Fertiliser: 10.0 / 10.0
        Feed: 200.0 / 200.0
        Salt: 100.0 / 100.0

Technicians:
 - James (£500/week)
 - Richard (£500/week)

================================
====== SIMULATING Quarter 2 ======
================================

>>> Enter number of technicians: -1
Let go: Richard

Fish Clef Fins (Demand: 25) - Sell: 25
Insufficient labour: Required 10.00 weeks, Available 9.00

Fish Clef Fins - Sell: 0
Fish Timpani Snapper - Sell: 0
Fish Andalusian Brim - Sell: 0
Fish Plagal Cod - Sell: 0
Fish Fugue Flounder - Sell: 0
Fish Modal Bass - Sell: 0

--- Payments ---
Paid James: £6000
Fixed expenses: £1500

--- Warehouse Costs ---
Main Warehouse:
 - Fertiliser: £2.00
 - Feed: £400.00
 - Salt: £200.00
Auxiliary Warehouse:
 - Fertiliser: £1.00
 - Feed: £200.00
 - Salt: £100.00

>>> Select vendor (1 or 2): 1

Hatchery Name: Eastaboga
Cash: £1206.03
Warehouse restocked.

================================
====== SIMULATING Quarter 3 ======
================================

>>> Enter number of technicians: 0

Fish Clef Fins - Sell: 0
Fish Timpani Snapper - Sell: 0
Fish Andalusian Brim - Sell: 0
Fish Plagal Cod - Sell: 0
Fish Fugue Flounder - Sell: 0
Fish Modal Bass - Sell: 0

--- Payments ---
Paid James: £6000
Fixed expenses: £1500

--- Warehouse Costs ---
Main Warehouse:
 - Fertiliser: £2.00
 - Feed: £400.00
 - Salt: £200.00
Auxiliary Warehouse:
 - Fertiliser: £1.00
 - Feed: £200.00
 - Salt: £100.00

>>> Select vendor (1 or 2): 1

Can't restock Fertiliser: Need £2.40, only have £-7196.97  
Went bankrupt restocking main warehouse in Quarter 3

===== FINAL STATE: Quarter 4 =====
Hatchery Name: Eastaboga  
Cash: £-7196.97

Warehouse Status:
 Main - Fertiliser: 12.0
        Feed: 360.0
        Salt: 200.0
 Aux  - Fertiliser: 6.0
        Feed: 180.0
        Salt: 100.0

Technicians:
 - James (£500/week)

Simulation Ended - Bankrupt 





## Software Development

This project is a text-based simulation about managing a hatchery using object-oriented programming. The aim of this simulationis operating hatchery in order to gain more profit and keep profitable to avoid bankrupt. This simulation includes different steps like: technician hairing and firing, fish selling, payment, etc. For construction of this project I used the strategy of tracking back from the example output to consider the main file and add the necessary functions or objects into different class. The process of each round(quarter) was divided into 6 steps.

The total 6 files to run the project includes 4 classes: fishspecies, hatchery, supply and technician, a utils file to store prompt functions and a main file to run the process. Then I will specify each file and their functions:

## Fishspecies file:

It includes a fish class represents species of fish the hatchery raised. And it involve parameters: name(str, The name of the fish species), fertilizer (int, the amount of fertilizer required per fish), feed (int, the amount of feed required per fish), salt (int, the amount of salt required per fish), maintenance_time (float, the time required to maintain a fish), price (float, the selling price of a fish) and demand (int, the market demand for this fish species).

## Technician file:
It includes a technician class represents techinician hired by the hatchery and each technician contain the parameters: name (str, the name of the technician), rate (float, the weekly rate paid to the technician) and specialty (str, the specialty fish species the technician can handleoptional which is optional).

## Supply file:
It includes a supply class represents supplies used in the hatchery and each supply has the parameter: name (str, the name of the supply), main_capacity (int, the maximum capacity of the main warehouse), aux_capacity (int, the maximum capacity of the auxiliary warehouse), depreciation (float, the depreciation rate per quarter) and cost_per_unit (float, the cost per unit of the supply).

A function in the supply class is apply_depreciation which applies depreciation to the supply stocks and decreases the main and auxiliary stocks based on the depreciation rate.

## Hatchery file:
It includes hatchery class which can represents the hatchery and manages its operations with attributes: cash_balance(float, the current cash balance of the hatchery),fixed_cost(float, the fixed costs of rent and utilities per quarter), technicians(list, list of hired technicians), supplies(dict, dictionary of suppliers with their details) and fish_species(dict, dictionary of fish species with their detail).

This class has the essential functions tof hatchery operations about supplies, cash status and number of technicians which involve:

**hire_technician:**

To hire new technician. With parameters: name(str): The name of the technician, rate (float): The weekly rate paid to the technician, specialty (str, optional): The specialty fish species the technician can handle. For special cases, maximum of 5 technicians can be hired and each technician must have a unique name. User assign a same name to a new technician will be asked to change a new name.

**fire_technician:**

To fire an existing technician.

**pay_technicians:**

It pays the weekly wage to all hired technicians.

**pay_fixed_costs:**

It pays the fixed cost of rent and utilities quarterly.

**pay_supply_costs:**

It pays for the supplies used in the main and auxiliary warehouses.

**apply_depreciation:**

It applies depreciation to all supplies.

**purchase_supplies:**

It purchase supplies from a vendor(vendor need to be choose in main). The only parameter is vendor_prices (dict): Dictionary of vendor prices for each supply. It return True if supplies were successfully purchased and False otherwise. For the special case, insufficient funds will prevent the purchase. For the process, it firstly compute the required amount of supplies in 2 warehouses and the cost of supplies in 2 warehouse, then check whether the cash can afford the required supplies.

**sell_fish**

This function is the main function to sell fish to the market. Firstly it compute the maximum value(the smaller value of the fish demand and the amount of fish maintained by technicians) of each kind of fish can be sold, then check the quantity the user want to sell and compute the total price. In addition, if there is a technician specialise in a specific fish, this kind of fish can be sold and maintained in 2/3 of the original time.

**display_status:**

It displays the status of the hatchery which includes state of 2 warehouses and technicians.

## utils file:

This file involves 5 prompting functions to prompt the user to enter the required information:
 
**get_int:**

Prompt the user to enter an integer.

**get_quarters_int:**

Prompt the user to enter a number of quarters. The input value should always be a non-negative integer and the default value is 8 if there is no input.

**get_non_negative_int:**

Prompt the user to enter a non-negative integer.

**get_vendor_choice:**

Prompt the user to enter 1 or 2 for a vendor number.

**get_technician_name:**

Prompt the user to enter a valid technician name.

## main file:

It includes the main functions to run the hatchery simulation.The number of rounds(quarters) the user set will be performed by the simulation. Before the first quarter, the user will be prompted to enter the number of rounds and the default rounds number is 8. We also add the vendor dictionary here. After that, the simulation start. The process of each round was divided in to 6 steps(bankrupt included):

**step 1: change of technician**

At the beginning of each quarter the user need to take some operation on the number of technician. User can add new technician or remove existed technician or do nothing with them. If we add a new technician we have opportunity to assign a specialty(enter 'yes') for him/her or not(enter 'no' or others). The maintaining time of the related kind of fish can reduce 1/3. However, if we assign a specialty wich can not match any sold fish, it will have no effect on the operation.

**step 2: sell fish**

Sell fish, operate the sell_fish function in hatchery class.

**step 3: pay for the cost**

Pay for the quartery rate of technicians, rent/utilities, supplies and depreciation. Operate the sell_fish, pay_technicians, pay_fixed_cost, pay_supply_cost and apply_depreciation functions in hatchery class.

**step 4: choose the vendor**

Choose a number for a vendor to deliver the supplies to the warehouses and pay for the restock.

**step 5: display status**

Display the recent status of the hatchery, includes the hatchery name, cash balance, supplies amount of 2 warehouses and technician state. 

**step 6: check bankrupt**

Check whether the cash balance less than 0. If cash less than 0 the hatchery bankrupt in this quarter. Then the system will still show the final status.

Additionally, each quarter will just run the step 1 to 5 except the bankrupt quarter. If hatchery bankrupt and the number of round of your setting have not reached, the last round run step 6 and the simulation end. If you have not bankrupted until running your last round, the simulation will end automatically and show your final state.
