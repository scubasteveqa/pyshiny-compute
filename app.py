---
title: "System Details"
format: html
jupyter: python3
---

```{python}
import multiprocessing
import pandas as pd
import platform
import psutil
import subprocess
import sys

def system_details():
    # Host memory
    host_total = psutil.virtual_memory().total
    host_mem = f"{int(host_total / 1024 / 1024 / 1024)} GiB ({host_total} bytes)"
    
    # CPU limit details
    try:
        cpu_max = subprocess.check_output(["cat", "/sys/fs/cgroup/cpu.max"]).decode().strip()
        parts = cpu_max.split()
        if len(parts) == 2:
            cpu_limit = int(parts[0]) / int(parts[1])
        else:
            cpu_limit = cpu_max
    except Exception:
        cpu_limit = "N/A"
    
    # Memory limit details
    try:
        memory_max = int(subprocess.check_output(["cat", "/sys/fs/cgroup/memory.max"]).decode().strip())
        pod_mem = f"{int(memory_max / 1024 / 1024 / 1024)} GiB ({memory_max} bytes)"
    except Exception:
        pod_mem = "N/A"

    # Creating a DataFrame to hold system information
    details = pd.DataFrame([
        {"Metric": "Python Version", "Value": platform.python_version()},
        {"Metric": "Host CPU Count", "Value": multiprocessing.cpu_count()},
        {"Metric": "Host Memory", "Value": host_mem},
        {"Metric": "CPU Limit", "Value": cpu_limit},
        {"Metric": "Memory Limit", "Value": pod_mem},
    ])
    
    return details

# Display the system details
system_details()
```
