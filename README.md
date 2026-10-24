
E-Commerce Payment Fraud Detection

A Machine Learning project designed to detect and prevent fraudulent financial transactions in e-commerce platforms. As global online shopping markets expand rapidly, payment fraud presents a significant financial challenge. This project leverages data analysis and predictive modeling to classify transactions as legitimate or fraudulent in real-time.

📊 Problem Statement & Market Context

According to recent Economic Survey trends, the surge in the e-commerce market correlates directly with an increasing risk of digital payment fraud. Out of hundreds of millions of active e-commerce shoppers globally, a notable percentage fall victim to transaction scams. This project builds a robust verification pipeline to solve this issue by flagging high-risk anomalies before payments are completed.

🚀 Key Features

• Real-Time Fraud Classification: Identifies fraudulent patterns instantly using machine learning models.
• Data Anomaly Detection: Flags suspicious transaction amounts, geographical mismatches, or odd purchasing hours.
• Imbalanced Data Handling: Utilizes techniques like SMOTE or class weighting to address the rarity of fraud instances in datasets.
• Automated Hyperparameter Optimization: Leverages Optuna to maximize model detection rates.

🛠️ Tech Stack & Frameworks

• Language: Python
• Libraries: Pandas, NumPy, Scikit-Learn, XGBoost, Optuna
• Visualization: Matplotlib, Seaborn
• Database/Queries: SQL (for data extraction and exploratory analysis)

📁 Repository Structure

text
├── data/                  # Placeholder for dataset descriptions or sample data
├── notebooks/             # Jupyter notebooks covering EDA and model training
├── src/                   # Python source code for data preprocessing and modeling
├── .gitignore             # Python gitignore file
└── README.md              # Project documentation
Use code with caution.

📈 Machine Learning Models & Optimization

We implemented and evaluated Random Forest and XGBoost algorithms to identify fraudulent financial actions. To maximize predictive accuracy and prevent overfitting, Optuna was integrated to conduct automated hyperparameter tuning via Bayesian optimization across dozens of trial iterations.

Performance Metrics Comparison

Below is the direct classification performance comparison following the hyperparameter tuning phase:

Performance Metric	Random Forest	XGBoost
Accuracy	92.01%	86.56%
Precision	30.31%	20.38%
Recall	41.28%	54.47%
F1-Score	34.95%	29.66%
ROC-AUC Score	79.78%	78.48%


🔍 Key Insights & Trade-offs

• The Imbalanced Data Challenge: The lower precision and recall scores across both models indicate a highly imbalanced dataset, which is standard in transaction fraud contexts where legitimate payments heavily outnumber scams.
• Random Forest (Higher Precision): Achieved a higher overall accuracy (92.01%) and F1-score (34.95%). It is more conservative, resulting in fewer false positives (flagging innocent users).
• XGBoost (Higher Recall): Achieved a significantly higher recall (54.47%). In a real-world financial ecosystem, this means XGBoost is more effective at catching actual fraud cases, even if it leads to a higher rate of initial false alarms.

🔧 Installation & Usage

1. Clone the repository and install requirements via standard package management.
2. Run the training script located in the source directory.

🔮 Future Enhancements

• Implementing deep learning models for unsupervised anomaly detection.
• Building a live API endpoint using FastAPI or Flask for real-time verification.
