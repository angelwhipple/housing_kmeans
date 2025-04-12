## Human vs. Algorithmic Feature Weighting in K-Means Clustering
This Python experiment investigates tensions between stakeholder-informed priorities and data-driven optimization in K-Means clustering, with a focus on human-centered applications. It compares the effects of using human-assigned feature weights versus weights learned programmatically.

### Approach
1. Baseline: Standard K-Means
2. Human-Informed Feature Weighting
3. Algorithmic Feature Weighting
   1. FWSA (Feature Weight Self Adjustment)
   2. FRFCM (Feature Reduction Fuzzy C-Means)

### Dataset
The analysis draws from two self-conducted surveys gauging short-term relocation preferences of over 100 college students and interns:
- 2024 Survey (for human-informed feature weights): Collected importance rankings of relocation-related features from undergraduates, graduate students, and interns. See the dataset [here](https://docs.google.com/spreadsheets/d/1DGOwN7Gwb7nG2BkWNWkKRHiLhEgzNuqkeso_NzWX6Mo/edit?usp=sharing)
- 2025 Survey (for clustering): Collected numerical feature values for the same relocation factors from a similar demographic. See the dataset [here](https://docs.google.com/spreadsheets/d/1a7sTa1XrTWnLoJEi-FCJkWHguHw9MIXtH7jacJG0QZ8/edit?usp=sharing)

Respondents attended universities such as MIT, Northeastern, Texas Southern, Georgia Tech, UT Austin, and more. Interns were included from companies like Apple, NVIDIA, Bloomberg, Google, and Amazon.



### Credits
- Tsai, Chieh-Yuan, and Chuang-Cheng Chiu. "Developing a feature weight self-adjustment mechanism for a K-means clustering algorithm." Computational Statistics & Data Analysis 52, no. 10 (2008): 4658–4672.
- Modha, Dharmendra S., and W. Scott Spangler. "Feature weighting in k-means clustering." Machine Learning 52, no. 3 (2003): 217–237.​