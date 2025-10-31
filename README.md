-----

#  CSC 3115: Advanced Programming - Individual Practical Test Solutions

This repository contains the Python-based solutions for the **Individual Practical Test** for the Advanced Programming course (CSC 3115), structured to reflect the questions on the exam paper.

The solutions demonstrate a strong grasp of core programming paradigms, including **Object-Oriented Programming (OOP)**, **Functional Programming**, **Concurrency**, and **Asynchronous Programming** using modern Python tools.

-----

##  Repository Structure & Key Concepts

The folders below correspond to the questions asked on the exam paper.

###  `Question__Review_Refactoring`

  * **Focus:** **Object-Oriented Programming (OOP)** Review.
  * **Content:** Implementation of a **`BankAccount`** class with encapsulation (using a **private `_balance`** attribute and control methods like `deposit` and `withdraw`), and refactoring of procedural code into a modular **`Student`** class.

###  `Question__Modular_Programming`

  * **Focus:** **Modularity** and Code Organization.
  * **Content:** Creation and utilization of Python **modules** (`string_tools.py`, `math_tools.py`) and a simple **package structure** to demonstrate effective code reuse and separation of concerns.

###  `Question__Generics_Templates`

  * **Focus:** **Generic Programming** and Higher-Order Functions.
  * **Content:** Application of Python's built-in **generic functions** (`map()`, `filter()`, `reduce()`) for flexible data processing, illustrating how the language handles generic operations without explicit templates.

###  `Question__Functional_Programming`

  * **Focus:** **Functional Paradigms** on Real-World Data.
  * **Content:** Data analysis performed using a **functional pipeline** (chained map/filter/reduce operations) on public datasets (e.g., World Population Data), prioritizing **immutability** and function composition.

###  `Question__Concurrency`

  * **Focus:** **Multithreading** and **Synchronization** (Parallelism simulation).
  * **Content:** Implementation of **multiple threads** to concurrently download and process different datasets (COVID, Global Temperature). Includes use of **`threading.Thread.join()`** for synchronization, ensuring the main process waits for all I/O and computation tasks to finish.
  * *Bonus:* Includes a comparison of **threading vs. multiprocessing** runtime performance.

###  `Question__Emerging_Paradigms`

  * **Focus:** **Asynchronous Programming** and Cloud API Interaction.
  * **Content:** Demonstrates efficient I/O handling using the **`asyncio`** framework and **`aiohttp`** library to perform **concurrent API calls** to services like the GitHub API, maximizing throughput for network-bound tasks.
  * *Bonus:* Implements **Asynchronous Retry Logic** with exponential backoff on failed API requests and non-blocking **asynchronous logging** using `aiofiles` to maintain responsiveness.

-----

###  Technologies Used

| Category | Tools & Libraries |
| :--- | :--- |
| **Language** | Python 3.x |
| **Networking** | `requests`, `aiohttp` |
| **Concurrency** | `threading`, `multiprocessing`, `asyncio` |
| **File I/O** | `csv`, `aiofiles` (for async logging) |

###  To Run the Solutions

All solutions can be executed with a standard Python 3.x environment. You will need to install the following libraries:

```bash
pip install requests aiohttp aiofiles
```

Navigate to any question folder (e.g., `Question_5_Concurrency`) and run the main script. All code is **well-commented** for easy review.
