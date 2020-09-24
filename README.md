# File Structure
```
├── Data
│   ├── en_dup.csv
│   └── USC_Melady_Lab_hasDup.csv
│	└── news
│	└── twitter
├── Data Analysis
│   └── data_process.ipynb
├── Data Collecting
│   └── snopes.py
├── LICENSE
└── README.md
```

# Data Collecting  
- `snopes.py` by Tianqi
  - It is used to collect data from website www.snopes.com and qc.wa.news.cn (departed)

# Data Analysis  
`data_process.ipynb` is written on Jupyter Notebook.  


# Data
- `news` 
  - news.csv and subfolder of each news
  - The number of subfolder records: 3936   

- `twitter` 
  - Twitter.csv and subfolder of each twitter
  - The number of subfolder records: 1383  
 
- `en_dup.csv` 
  - The number of records: 7179.   
  - Part of data are collected manually by keywords searching from sources such as twitter.com.  
  - Data from www.snopes.com and qc.wa.news.cn are collected by 'snopes.py'.  

- `USC_Melady_Lab_hasDup.csv` 
  - The number of records: 35134 (with duplicates).  
  - Data come from usc-melady.github.io/COVID-19-Tweet-Analysis/misinfo.html, accessed in May.  
  - Reference: Sharma, Karishma, et al. "Coronavirus on social media: Analyzing misinformation in Twitter conversations."   arXiv preprint arXiv:2003.12309 (2020).
  
  
# Acknowledgement
- We thank Tianqi, Wenshuo, Jianni, Xiaofeng, and Hanlong for rumor data collection and labeling.  

# The MIT License (MIT)

