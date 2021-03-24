# File Structure
```
├── Data
│   ├── en_dup.csv
│	└── news
│	└── twitter
├── Data Analysis
│   └── PowerLaw Analysis.pdf
├── Data Collecting
│   └── snopes.py
├── LICENSE
└── README.md
```

# Data Collecting  
- `snopes.py` by Tianqi
  - It is used to collect data from website www.snopes.com and qc.wa.news.cn (departed)

# Data Analysis  
- PowerLaw Analysis includes the statistical analysis of rumor popularity data.  
- Sentiment analysis https://colab.research.google.com/drive/1CyGtXPSol_Ayt_WR7zsq60M2Q5kDUofd?usp=sharing  
- Stance analysis https://colab.research.google.com/drive/1ItGmEvumyOesXeB2dV7w5cnjRW9fTAKL?usp=sharing  


# Data
- `news` 
  - news.csv (4129) and subfolder of each news
  - The number of subfolder records: 3936   

- `twitter` 
  - Twitter.csv (2705) and subfolder of each twitter
  - The number of subfolder records: 1383  

- `en_dup.csv`
  - Unprocessed data with both news and twitter records.  
  - The number of records: 7179 (with duplication).   
  - Part of data are collected manually by keywords searching from sources such as twitter.com.  
  - Data from www.snopes.com and qc.wa.news.cn are collected by 'snopes.py'.  

  
  
# Acknowledgement
- We thank Tianqi, Wenshuo, Jianni, Xiaofeng, and Hanlong for rumor data collection and labeling.  


