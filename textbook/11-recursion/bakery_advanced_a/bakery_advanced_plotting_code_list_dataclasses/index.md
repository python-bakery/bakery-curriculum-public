---
waltz:
  title: bakery_advanced_plotting_code_list_dataclasses
  display title: 11A1.2) Plotting Dataclasses
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    hide_files: false
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 90
    created: November 13 2022, 0655 PM
    modified: November 15 2022, 0411 PM
  files:
    path: bakery_advanced_plotting_code_list_dataclasses
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_advanced_plotting_code_list_dataclasses\bakery_salary.py
    - bakery_advanced_plotting_code_list_dataclasses\raw_salaries.csv
---
The `raw_salaries.csv` file contains pipe-separated (`|`) values representing salary data about different industries in the US in 2021 (data from [Bureau of Labor Statistics](https://www.bls.gov/oes/current/oes_nat.htm#00-0000)). That data is loaded into a field named `industries` in the `bakery_salary.py` file as a list of dataclass instances (`list[Industry]`). The dataclass is named `Industry` and has four fields; you can see the dataclass by opening the `bakery_salary.py` file. However, you will only need one field: `mean_salary`, which is an integer representing the average salary of people in the given industry.

Make a histogram of the `mean_salary` for all of the `industries`. Make sure you give meaningful labels to the axes and a title.

You may notice that the x-values are so big, they spill into each other. If you would like, you may divide each salary by 1000 to make the X-axis easier to read.

**HINT:** Do not overthink this problem! You are not creating a function, you are just mapping a list of dataclass instances into a list of integers, and plotting them as a histogram.