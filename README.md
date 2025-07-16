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

```text
$ python3 main.py
>>> Please enter number of quarters: 8

====== SIMULATING quarter 1 ======
>>> Enter number of technicians: 2
>>> Enter technician name: James
>>> Enter technician name: Richard

Fish Clef Fins, sell 25: 25
Fish Timpani Snapper, sell 10: 10
...

Insufficient labour: required 8.00 weeks, available 4.50
Insufficient ingredients:
 fertiliser need 2.0 storage 25.65
 feed need 200.0 storage 120.0
...

Paid James, £6000
Paid Richard, £6000
Paid rent/utilities: £1500

>>> Choose vendor:
1. Slippery Lakes
2. Scaly Wholesaler
>>> 1

Hatchery Cash: £9618.63
Warehouse restocked

====== SIMULATING quarter 2 ======
>>> Enter number of technicians: -1
Let go Richard
...
Went bankrupt in quarter 3
Hatchery Cash: -£7196.97
