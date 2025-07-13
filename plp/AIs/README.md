## AI for Sustainable Cities: Clustering Transport Accessibility

# SDG Focus: Sustainable Cities and Communities (SDG 11)

📌 Project Overview

This project aims to support SDG 11 by using unsupervised machine learning to cluster urban regions based on public transport accessibility. By identifying well-served and underserved areas, we can provide actionable insights for city planners and transport agencies.

🎯 Objective

Cluster regions based on:

Average walking distance to nearest public transport stop

Accessibility score reflecting quality and availability of transit

🧠 Machine Learning Approach

ML Type: Unsupervised Learning

Algorithm: K-Means Clustering

Libraries Used: pandas, scikit-learn, matplotlib, seaborn

🗂 Dataset

Source: OPTIMAP Public Transport Accessibility Data (Germany)

Format: Parquet

Features Used:

MinDistanceWalking: distance to nearest stop (meters)

scores_OVERALL: overall transit accessibility score (lower = better)

🔬 Workflow

Load and sample data (100,000 rows for efficiency)

Group data into regional grids by rounding lat/lng

Compute average accessibility features per grid

Normalize data using StandardScaler

Use elbow method to determine optimal k (found k=4)

Apply K-Means clustering

Visualize clusters and save results

📊 Output

Scatter plot of clusters based on walking distance and accessibility score

CSV file of clustered data: clustered_transport_accessibility.csv

📌 Ethical Considerations

Bias Risk: Accessibility data may not reflect informal settlements or non-registered regions

Fairness: Clustering helps identify underserved areas for more equitable urban planning

Sustainability Impact: Data-driven resource allocation improves long-term transit planning

📁 Files Included
