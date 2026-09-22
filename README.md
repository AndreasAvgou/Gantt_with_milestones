# PhD Timeline Gantt Chart Generator

This repository contains a collection of Python scripts designed to generate clean, professional, and publication-ready Gantt charts for a PhD thesis timeline (or any long-term project). The charts are built using `matplotlib` and can be exported to multiple high-quality formats including `.svg`, `.pdf`, and `.png`.

## 📂 Included Files

The project includes three distinct Python scripts, each tailored to a specific visual layout:

1. **`gantt_with_milestones.py`**
   - Features a standard task timeline in the main body.
   - Includes a dedicated "Milestones" (Ορόσημα) section at the bottom using diamond markers to indicate major events (e.g., journal publications, thesis defense).
   
2. **`gantt_without_milestones_v1.py`**
   - A streamlined version containing only the main and supportive tasks.
   - Removes the milestone section entirely to save vertical space.

3. **`gantt_without_milestones_v2.py`**
   - Similar to `v1` (no milestones), but introduces dashed vertical grid lines halfway through each semester.
   - Ideal for breaking down semesters into quarters (3-month intervals) for more granular time tracking.

## ⚙️ Prerequisites

To run these scripts, you will need Python 3 installed on your system along with the `matplotlib` library.

You can install the required dependency using pip:
```bash
pip install matplotlib
```

## 🚀 How to Run

Navigate to the directory containing the scripts and execute the desired file via your terminal or command prompt:

```bash
python gantt_with_milestones.py
```
*(Replace the filename with the specific version you wish to run).*

Upon successful execution, the script will silently generate the output files (e.g., `gantt.svg`, `gantt.pdf`) in the same directory and print a confirmation message.

## 🛠️ Customization Guide

You can easily adapt the chart for your specific project by opening the Python scripts in any text editor and modifying the data lists. 

### 1. Modifying Tasks
Locate the `TASKS` list. Each entry is a tuple containing:
`(Task Name, Start Time, Duration, Task Type)`
* **Start Time & Duration:** Measured in semesters (e.g., `0.5` is halfway through the first semester).
* **Task Type:** Use `"main"` for primary tasks and `"sub"` for supportive tasks.

```python
TASKS = [
    ("Literature Review", 0.0, 1.0, "main"),
    ("Data Collection", 1.0, 2.0, "main"),
    ("Ethics Approval", 0.5, 0.5, "sub"),
]
```

### 2. Modifying Milestones (Only in `gantt_with_milestones.py`)
Locate the `MILESTONES` list. Each entry is a tuple containing:
`(Milestone Name, Position)`
* **Position:** Measured in semesters from the start date.

```python
MILESTONES = [
    ("First Conference Paper", 2.5),
    ("Journal Submission", 4.0),
]
```

### 3. Changing Colors and Fonts
In the `# 2. (APPEARANCE)` section of the code, you can tweak the hex color codes to match your university's branding or your personal preference:
```python
COLOR_MAIN = "#3A5A73" # Color for main tasks
COLOR_SUB  = "#7A98AE" # Color for supportive tasks
```
*Note: The scripts use the `DejaVu Sans` font by default to ensure Greek character support. You can change this to `Arial`, `Calibri`, or any other system font you prefer.*

## 📄 Output Formats
By default, the scripts are configured to generate vector graphics (`.svg`, `.pdf`) which are perfect for embedding into LaTeX documents, Word files, or presentations without losing quality. Raster images (`.png` at 300 DPI) are also supported and included in some of the scripts.
