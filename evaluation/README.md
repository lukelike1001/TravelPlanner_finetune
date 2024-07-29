# **evaluation** folder 📂

tl;dr This folder contains smaller samples of the validation dataset from [TravelPlanner](https://github.com/OSU-NLP-Group/TravelPlanner), to make it easier to run prompt engineering tests with lower time and resource constraints.

## **Table of Contents: 📔**

### **Folders: 🗂️**
- `1day_1person`: Folder containing datasets for 1-day trips with just 1 person
- `2day_1person`: Folder containing datasets for 2-day trips with just 1 person
- `3day_1person`: Folder containing datasets for 3-day trips with just 1 person

- **The CSVs contained inside the folders are structured with the following format:**
  - `budget_[COST]_[NUM_DAYS]d_[NUM_PERSONS]p.csv`
  - Additional words refer to different constraints, while `nc` denotes **n**o **c**onstraints.

### **Python Scripts: 🐍**
- `download_subset_from_hf.py`: Downloads selected validation tests from **HuggingFace**
- `scramble_restaurants.py`: Anonymizes restaurant names for the restaurant dataset (i.e., [`database/restaurants/clean_restaurant_2022.csv`](../database/restaurants/clean_restaurant_2022.csv)) with a random sequence of letters and numbers

### **CSVs: 📝**
- `selected_validation.csv`: Subset of `validation.csv` created by running `download_subset_from_hf.py`
- `test.csv`: Testing data sourced from osunlp **[[source](https://huggingface.co/datasets/osunlp/TravelPlanner/viewer/test/test)]**
- `validation.csv`: Validation data sourced from osunlp **[[source](https://huggingface.co/datasets/osunlp/TravelPlanner/viewer/validation)]**

### **Contact: ☎️**
If you have any questions about any of the files or folders featured here, please reach out to Luke Nam at [lukelike1001@gmail.com](mailto:lukelike1001@gmail.com)
