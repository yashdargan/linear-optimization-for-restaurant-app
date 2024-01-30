# JobShop Optimization

## Overview

This project focuses on the optimization of a logistics problem in a job shop setting. The primary goal is to improve the efficiency of resource allocation and scheduling within a job shop environment.

## Functions

### Exploratory Data Analysis (EDA)

The EDA function provides insights into the dataset, highlighting specific patterns or observations that can inform the optimization process. One notable observation is the absence of shift partners during the noon shift (12 pm - 3 pm).

#### Hourly and Minutely Analysis

The EDA includes hourly and minutely analysis, revealing trends and patterns in resource utilization and workflow dynamics.

### Timestamp Function

The timestamp function plays a crucial role in structuring the data by categorizing shifts based on the 'created_at' column. This categorization is essential for subsequent optimization steps.

## Usage

To utilize the functionalities provided by this project, follow these steps:

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```
 ### Tasks to Do Next

* Work on Employee Scheduling
- Implement a scheduling mechanism to efficiently allocate employees to different shifts.
- Consider factors such as employee availability, skill sets, and workload distribution.
* Apply the Job Shop Model Based on Priority
- Develop a job shop model that prioritizes tasks based on specific criteria.
- Optimize the job shop model to maximize efficiency and minimize completion times.