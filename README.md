#  CS432 Track 1 Assignment 2 

Video links 

Module_A - https://drive.google.com/file/d/1dPDESA7kt90Q3XH8O4LIsKymRxUvmlx7/view?usp=sharing


##  Application Development & Database Index Structure Implementation

---

#  Project Overview

This project implements a complete database system pipeline combining:

- **Module A:** B+ Tree-based DBMS engine  
- **Module B:** Secure API system with RBAC, UI, and SQL optimization  

The project demonstrates both:
- Low-level data structure implementation  
- High-level backend system design and optimization  

---

#  Module A — Lightweight DBMS with B+ Tree Index

##  Objective
To implement a B+ Tree from scratch and compare its performance with a brute-force approach.

---

##  B+ Tree Implementation

- Insertion with automatic node splitting  
- Deletion with merging and redistribution  
- Exact search (key lookup)  
- Range queries using linked leaf nodes  
- Key-value storage (records mapped to keys)  

---

##  DBMS Integration

- Custom **Table abstraction**  
- **Database Manager** for:
  - Creating tables  
  - Inserting records  
  - Querying data  

---

##  Performance Analysis

Comparison between:
- **B+ Tree**
- **BruteForceDB**

Metrics evaluated:
- Insertion time  
- Search time  
- Deletion time  
- Range query time  
- Random workload performance  
- Memory usage  

---

##  Benchmarking & Visualization

- Implemented inside a **Jupyter Notebook**
- Uses:
  - Matplotlib (performance graphs)
  - Graphviz (tree visualization)

---

#  Module B — API Development, RBAC & Database Optimization

##  Objective
To build a secure and optimized application layer with APIs, role-based access control, and query optimization.

---

#  System Architecture

```
Frontend UI → REST API → Authentication & RBAC → Database

```

---

##  Backend Structure

Located in:

```
Module_B/app/

```


### Key Components:

- `main.py` → Application entry point  
- `auth.py` → Authentication logic  
- `db.py` → Database connection handling  
- `routes/` → API endpoints  
- `utils/logger.py` → Audit logging  

---

##  REST API Design

###  Authentication APIs
- `POST /login` → Authenticate user and generate session token  
- `GET /isAuth` → Validate user session  

---

###  CRUD APIs
- Create records  
- Read records  
- Update records  
- Delete records  

All APIs:
- Require authentication  
- Validate session tokens  
- Enforce role-based permissions  

---

##  Role-Based Access Control (RBAC)

###  Admin
- Full system access  
- Can manage users and all data  

###  Students
- Restricted access  
- Can view and modify only own data  

###  Authority
- System access 
- Can view all profiles and manage scholarships

---

##  Security Features

- Session-based authentication  
- Authorization checks on every API request  
- Audit logging system  

###  Logs stored in:

```
Module_B/logs/audit.log

```


Logs include:
- API activity  
- Unauthorized access attempts  
- Data modification records  

---

##  Web UI — Member Portfolio

Templates located in:

```
Module_B/sql/indexes.sql

```


Optimized for:
- WHERE clauses  
 

---

## Benchmarking

Notebook:

```
Module_B/performance_benchmarking.ipynb

```


Measures:
- Query execution time  
- API response time  
- Performance before and after indexing  

---

# Team Contributions

| Member Name | Roll No. | Role | Main Responsibility | Detailed Tasks | Technologies / Tools | Deliverables |
|-------------|----------|------|---------------------|----------------|----------------------|--------------|
|       Siri Durugapu      |   24110343       | B+ Tree Engine Developer | Implement the core database indexing structure (Module A) | Design B+ Tree classes; implement insert, delete, search, range query, update; handle node splitting/merging; maintain leaf node links; ensure correctness and efficiency | Python | bplustree.py, table.py, db_manager.py; fully working B+ Tree implementation |
|     Manashree Ashtekar        |    24110192      | Performance & Visualization Engineer | Benchmark and prove efficiency of B+ Tree (Module A) | Implement brute-force DB; run performance tests (insert, search, delete, range query); measure time & memory; generate graphs; visualize tree using Graphviz; document in notebook | Python, Matplotlib, Graphviz, Jupyter Notebook | bruteforce.py; graphs comparing performance; tree visualizations; report.ipynb |
|     Shweta Roshia        |    24110304      | Backend API Developer | Build server-side logic and APIs (Module B) | Create REST APIs (login, CRUD, apply, verify, payments); connect APIs to database; handle request/response logic; implement authentication/session handling | Flask / FastAPI (Python) or Node.js | API code (app/api/, app/auth/); working endpoints returning JSON |
|      Sejal Kadgi       |    24110323      | Frontend / UI Developer | Build user interface for system (Module B) | Design pages for Student, Admin, Authority; implement forms (login, apply, upload docs); connect UI to backend APIs; ensure usability and navigation | HTML, CSS, JavaScript, Bootstrap / React | UI templates (templates/, static/); fully working web interface |
|      Swamini More       |    24110211      | Database Optimization & Security Engineer | Ensure performance, access control, and logging (Module B) | Implement RBAC (role-based permissions); create audit logging system; add SQL indexes; run query optimization (EXPLAIN); measure before/after performance; secure endpoints | SQL (MySQL/PostgreSQL), Python | Indexed database; audit.log; performance comparison results; optimization report |

---

# Repository Structure

CS432_Track1_Submission/

├── Module_A/
│   ├── database/
│   ├── report.ipynb
│   └── requirements.txt
│
├── Module_B/
│   ├── app/
│   ├── templates/
│   ├── sql/
│   ├── logs/
│   │   └── audit.log
│   ├── performance_benchmarking.ipynb
│   ├── report.ipynb
│   └── requirements.txt
│
└── README.md




