# 📌 NexGen ERP – Mini ERP System
A fully functional console-based Mini ERP (Enterprise Resource Planning) system written in Python.
This project simulates how a real ERP works by managing:

- Employees
- Assets
- Financial Reports
- Authentication & Data Persistence

It is designed using Object-Oriented Programming (OOP) and follows real enterprise software principles such as modularity, encapsulation, inheritance, and separation of concerns.

---

## 🏗️ System Architecture Overview

**The system is divided into four major layers:**
```
User Interface (Menus)
        ↓
Business Logic (Employee, Asset, Finance modules)
        ↓
Data Models (Employee, Manager, Assets, Hardware, Software)
        ↓
Persistence Layer (Text files)
```

This layered design allows the system to scale later into databases, APIs, or web interfaces.

---

## 🚀 How the System Works

When the system starts, it follows four controlled phases:

### Phase 1 – Boot & Data Load
The system loads all saved data from text files into memory
      
Employees → `employee.txt`

Assets  → `asset.txt`

Login   → `login_cred.txt`


>If files don’t exist, it safely starts with empty data structures.
This logic is implemented in app.py and read.py

---

### Phase 2 – Secure Login System

The user must log in using:

- Role (admin, manager, etc)

- Username

- Password

>The system allows only 3 attempts.
After 3 failures, the ERP locks and shuts down.
This provides basic enterprise-grade authentication app

---

### Phase 3 – Main Control Hub

Once logged in, users access the Main Menu:

1. Manage Employees
2. Manage Assets
3. Company Financial
4. Save & Exit


> Every module returns here, making it the central navigation hub.
This loop is controlled inside main_menu_loop() in Main_menu.py 

---

### Phase 4 – Business Operations

Each menu opens a fully isolated subsystem:

| Module      | What it does                       |
| ----------- | ---------------------------------- |
| Employees   | Hire, update, fire employees       |
| Assets      | Track company hardware & software  |
| Finance     | Company valuation & salary reports |
| Save & Exit | Persist all data to disk           |



---


### 📁 Project Folder Structure
```
NexGen-ERP/
│
├── app.py                  → System boot & login
├── Main_menu.py            → Main navigation & saving
├── read.py                 → File loading system
│
├── Emplyoees.py            → Employee & Manager classes
├── Assets.py               → Asset, Hardware, Software classes
│
├── employee_management.py → Employee CRUD logic
├── asset_menu.py          → Asset operations
├── company_financial.py   → Financial reporting
├── input_validation.py    → Input safety & validation
│
├── employee.txt           → Saved employees
├── asset.txt              → Saved assets
└── login_cred.txt         → Login credentials
```

---

### 👨 ‍💼 Employee Management System

The system supports:

- Staff
- Managers

Managers inherit from Employees using **OOP inheritance**.

Features:

- Auto-generated Employee IDs (ES001, ES002…)

- Add / View / Update / Delete employees

- Managers receive bonus

- Assets can be assigned to employees

Implemented in:
- `Emplyoees.py`
- `employee_management.py`

---


### 🖥️ Asset Management System

Assets are divided into:

| Type     | Extra Field                 |
| -------- | --------------------------- |
| Hardware | Condition (Good, Fair, etc) |
| Software | Expiry Date                 |


All assets inherit from a base Assets class using **inheritance**.

Supports:

* Auto-generated Asset IDs
* Asset assignment to employees
* Depreciation calculation
* View all assets

Implemented in:

* `Assets.py`
* `asset_menu.py`

--- 

### 💰 Financial Reporting System


* The ERP can calculate:
* Monthly salary cost
* Annual salary cost
* Total asset value
* Asset-to-salary ratio
* Average salary
* Complete financial overview

Uses:

* **Polymorphism** (`Manager.total_pay()`)
* **Operator overloading** (`Assets.__add__()`)


Implemented in 
* `company_financial.py`
* `company_financial`

---

### 💾 Data Persistence

Data is saved when user chooses Save & Exit.

**Format example:**
```
ES001|John|manager|50000|5000
ES002|Sara|staff|30000
```

A**ssets:**

A001|Laptop|Hardware|70000|Good

A002|MS Office|Software|10000|2026


**Handled by:**

* `save_employee_data()`
* `save_asset_data()`

in `Main_menu.py`


---

### 🔐 Input Validation

All inputs are protected:

* Names cannot contain digits
* Salaries have minimum limits
* Menu choices must be valid
* This prevents crashes & data corruption

Handled in 
* `input_validation.py`
* `input_validation`

### 📈 How This Can Scale Into a Real ERP

This system is already designed like a real ERP backend. It can be extended into:

### #️⃣ Database Integration

Replace text files with:

- MySQL
- PostgreSQL
- MongoDB

> Only read.py and save_*() need change.

---

### #️⃣ Web / API Interface

Add:

- Flask / Django API
- React frontend
- The business logic can stay unchanged.

---

### 3️⃣ User Roles

Add:

- Manager
- Staff
- Admin
> Each role can be restricted to certain menus.

---

### 4️⃣ Enterprise Features

Future upgrades:

* Audit logs
* Payroll system
* Vendor management
* Cloud deployment

--- 
### 🧠 What You Learned from This Project

* This Mini ERP demonstrates:
* Real-world OOP
* Modular software architecture
* Authentication
* CRUD operations
* Data persistence
* Business logic modeling
* Financial calculations
> This is exactly how backend ERP systems are designed, only at a smaller scale.

---

### 🏁 Conclusion

_**NexGen ERP is not just a practice project —**_

It is a fully structured enterprise-grade backend system that can be scaled into:

* A company HR system
* An asset management platform
* A financial tracking system

> With a database and UI, this could become a real product.