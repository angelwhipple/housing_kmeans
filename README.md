## Human vs. Algorithmic Feature Weighting in K-Means Clustering
This Python experiment investigates tensions between stakeholder-informed priorities and data-driven optimization in K-Means clustering, with a focus on human-centered applications. It compares the effects of using human-assigned feature weights versus weights learned programmatically.

### Objectives
- Understand how human and algorithmic definitions of feature importance differ.
- Evaluate clustering performance across three weighting strategies:
  - Uniform (baseline)
  - Human-informed
  - Algorithmically learned
- Explore whether and when these definitions of importance converge.

### Approach
1. Baseline: Standard K-Means
    - All features are equally weighted.
    - Uses Euclidean or squared distance as the distortion metric.
2. Human-Informed Feature Weighting 
   - Weights are derived from user-generated importance rankings. 
   - Captures subjective and relative judgments of feature importance.
3. Algorithmic Feature Weighting
   1. FWSA (Feature Weight Self Adjustment)
      - Adaptively updates feature weights during K-means iterations. 
      - Prioritizes features that improve cluster compactness and separation. 
      - Adjustment margins are inversely related to feature dispersion.
   2. FRFCM (Feature Reduction Fuzzy C-Means)
      - Extends fuzzy clustering by reducing the influence of low-importance features. 
      - Discards features with persistently low weights.

### Evaluation
- Clustering performance is assessed using average within-cluster dispersion and between-cluster separation.
- Analysis focuses on how well each method groups similar data and distinguishes between clusters.
- Investigates when human-defined and algorithm-defined importance align or diverge.

### Dataset
My analysis draws from two self-conducted surveys gauging short-term relocation preferences of over 100 college students and interns:
- 2024 Survey (for human-informed feature weights): Collected importance rankings of relocation-related features from undergraduates, graduate students, and interns. See the dataset [here](https://docs.google.com/spreadsheets/d/1DGOwN7Gwb7nG2BkWNWkKRHiLhEgzNuqkeso_NzWX6Mo/edit?usp=sharing)
- 2025 Survey (for clustering): Collected numerical feature values for the same relocation factors from a similar demographic. See the dataset [here](https://docs.google.com/spreadsheets/d/1a7sTa1XrTWnLoJEi-FCJkWHguHw9MIXtH7jacJG0QZ8/edit?usp=sharing)

Respondents attended universities such as MIT, Northeastern, Texas Southern, University of Cincinnati, Georgia Tech, UT Austin, and more. Interns were included from companies like Apple, NVIDIA, Bloomberg, Google, and Amazon.



### Credits
- Tsai, Chieh-Yuan, and Chuang-Cheng Chiu. "Developing a feature weight self-adjustment mechanism for a K-means clustering algorithm." Computational Statistics & Data Analysis 52, no. 10 (2008): 4658–4672.
- Modha, Dharmendra S., and W. Scott Spangler. "Feature weighting in k-means clustering." Machine Learning 52, no. 3 (2003): 217–237.​