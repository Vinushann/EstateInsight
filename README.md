# Bengaluru House Price Prediction Application

Welcome to the Bengaluru House Price Prediction Application! This project aims to provide accurate predictions of house prices in Bengaluru based on various features such as location, size, and amenities. By leveraging machine learning techniques and explainable AI, the application helps users make informed decisions in the real estate market.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Explainable AI](#explainable-ai)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Introduction

The rapid growth of Bengaluru has led to a complex and fluctuating real estate market. This project addresses the challenges of inconsistent housing prices by developing a predictive model that estimates property prices based on key factors. The application provides users with price predictions and insights into how different features influence the price.

## Features

- Predict house prices based on user inputs:
  - Area type
  - Location
  - Size (e.g., 2 BHK, 3 BHK)
  - Total square footage
  - Number of bathrooms
  - Number of balconies
- Interactive web application built with Streamlit
- Explainable AI integration using SHAP values to interpret model predictions
- Option to download prediction results and explanations as a PDF report
- User-friendly interface with real-time prediction updates

## Dataset

The dataset used for this project is the **Bengaluru House Prices** dataset obtained from [Kaggle](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data). It includes features like area type, location, size, total square footage, number of bathrooms, balconies, and price.

**Note:** Due to file size limitations, the dataset is not included in this repository. Please download it from Kaggle and place it in the `data/raw/` directory as mentioned in the [Project Structure](#project-structure) section.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Vinushann/The-Analytica.git
   cd your-repository
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Dataset**

   - Go to the [Kaggle dataset page](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data) and download `Bengaluru_House_Data.csv`.
   - Place the downloaded file in the `data/raw/` directory.

5. **Run Initial Data Preprocessing**

   ```bash
   python src/data_preprocessing.py
   ```

   This script will preprocess the data and prepare it for model training.

6. **Train the Model**

   ```bash
   python src/model_training.py
   ```

   The trained model will be saved as `models/model.pkl`.

## Usage

1. **Run the Streamlit App**

   ```bash
   streamlit run app/streamlit_app.py
   ```

2. **Access the Application**

   - Open your web browser and go to `http://localhost:8501/`.

3. **Use the Application**

   - Enter the required property details in the input fields.
   - Click on the "Predict Price" button to get the estimated house price.
   - View the SHAP value plot to understand feature contributions.
   - Optionally, download the prediction report as a PDF.

## Project Structure

```plaintext
your-project/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── raw/
│       └── Bengaluru_House_Data.csv
├── models/
│   └── model.pkl
├── notebooks/
│   └── data_exploration.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── explainable_ai.py
├── app/
│   └── streamlit_app.py
└── docs/
    └── project_report.docx
```

- **.gitignore**: Specifies intentionally untracked files to ignore.
- **README.md**: Project documentation and usage instructions.
- **requirements.txt**: List of project dependencies.
- **data/**: Directory for datasets.
  - **raw/**: Contains the original dataset.
- **models/**: Contains the trained machine learning model.
- **notebooks/**: Jupyter notebooks for data exploration and analysis.
- **src/**: Source code for data processing and model training.
  - **data_preprocessing.py**: Script for cleaning and preprocessing data.
  - **model_training.py**: Script for training the machine learning model.
  - **explainable_ai.py**: Script for generating explainable AI visualizations.
- **app/**: Contains the Streamlit application.
  - **streamlit_app.py**: Main script for running the web app.
- **docs/**: Documentation and reports.
  - **project_report.docx**: Detailed project report.

## Technologies Used

- **Programming Language**: Python 3.x
- **Data Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **Machine Learning**: scikit-learn
- **Explainable AI**: SHAP
- **Web Framework**: Streamlit
- **Environment Management**: Virtualenv
- **Version Control**: Git and GitHub
- **IDE**: Visual Studio Code, Jupyter Notebook

## Explainable AI

To enhance transparency and interpretability, we integrated SHAP (SHapley Additive exPlanations) into the application. SHAP values explain the contribution of each feature to the model's predictions, allowing users to understand how different factors influence the estimated house price.

**Features:**

- SHAP value plots displayed alongside predictions
- Interactive visualizations for better insight
- Helps build trust in the model's predictions

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. **Fork the Repository**

   Click on the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/your-forked-repo.git
   cd your-forked-repo
   ```

3. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**

   - Implement your feature or bug fix.
   - Commit your changes with clear and descriptive messages.

5. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**

   - Go to the original repository and click on "New Pull Request".
   - Select your branch and submit the pull request for review.

## Acknowledgments

- **Kaggle** for providing the Bengaluru housing prices dataset.
- **scikit-learn** and **Streamlit** communities for their excellent tools and documentation.
- **Professors and Mentors** who guided us through this project.
- **Team Members** who collaborated and contributed to this project.

---

**Note:** This project is part of a university data mining course and is intended for educational purposes.
