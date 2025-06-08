# 📊 YouTube Data Engineering & Analytics Project

## 📽️ Overview

This project is inspired by the [YouTube tutorial](https://www.youtube.com/watch?v=yZKJFKu49Dk). The goal is to create a scalable, secure, and cloud-native data lake on AWS that analyzes trending YouTube video data from both structured (CSV) and semi-structured (JSON) sources.

---

## 🎯 Project Goals

1. **Data Ingestion**: Automate the collection of trending video data.  
2. **ETL System**: Clean, transform, and format raw data.  
3. **Data Lake Architecture**: Use Amazon S3 as a centralized storage.  
4. **Scalability**: Ensure the system can handle increasing data volume.  
5. **Cloud-Native**: Leverage AWS services for performance and cost-efficiency.  
6. **Reporting**: Visualize insights with Amazon QuickSight dashboards.

---

## 🧰 Tools & Technologies

| Tool / Service          | Purpose                            |
|------------------------|----------------------------------|
| Amazon S3              | Data lake storage                 |
| AWS Glue               | ETL & transformation engine      |
| AWS Glue Data Catalog  | Metadata repository               |
| AWS Lambda             | Event-driven orchestration        |
| Amazon Athena          | Serverless SQL querying           |
| Amazon QuickSight      | Data visualization and BI         |
| AWS CloudWatch         | Logs and performance monitoring   |
| AWS IAM                | Security and permissions          |
| Amazon SNS             | Alerting and notifications        |

---

## 📦 Dataset

**Source:** [Kaggle - Trending YouTube Video Statistics](https://www.kaggle.com/datasets/datasnaek/youtube-new)

**Types:**

- CSV files (e.g., `USvideos.csv`)  
- JSON files (e.g., `US_category_id.json`)  

These files contain information such as:

- Video ID, Title, Channel  
- Category ID  
- Views, Likes, Dislikes, Comments  
- Description, Tags  
- Trending dates per country  

---
