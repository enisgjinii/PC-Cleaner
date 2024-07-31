# AI-Powered PC Cleaner 2024

## Description

AI-Powered PC Cleaner 2024 is an advanced desktop application that combines traditional PC maintenance tools with artificial intelligence to provide smarter, more personalized computer optimization. Built with Python, CustomTkinter, and integrated machine learning capabilities, this application offers an intelligent approach to system cleaning and analysis.

## Features

1. **AI-Powered Cleaning Recommendations**
   - Analyzes current system state
   - Provides personalized cleaning recommendations

2. **Predictive System Health Analysis**
   - Calculates a system health score
   - Offers insights into potential system issues

3. **Intelligent File Categorization**
   - Automatically categorizes files based on type
   - Helps identify space-consuming file categories

4. **Traditional Cleaning Tools**
   - Quick Clean: Removes temporary files and clears the Recycle Bin
   - Deep Clean: Performs a Quick Clean, plus clears Windows Update cache and browser cache

5. **Real-Time System Information**
   - Display of CPU usage, memory utilization, and disk space usage

6. **Disk Space Analyzer**
   - Visual representation of folder sizes
   - Hierarchical view of file and folder structure

7. **User-Friendly Interface**
   - Dark-themed, modern UI
   - Sidebar navigation for easy access to all features
   - Real-time logging of operations

## Requirements

- Python 3.7 or higher
- Windows operating system

## Installation

1. Clone this repository or download the source code.
2. Install the required packages:


pip install customtkinter pillow psutil scikit-learn joblib numpy


3. If you want to use the Recycle Bin clearing feature, also install:


pip install winshell


## Usage

Run the application by executing the main Python script:


python ai_pc_cleaner.py


Navigate through the application using the sidebar and explore the AI-powered features:
- Use "AI Recommendations" for smart cleaning suggestions
- Check "Predict System Health" for a health score
- Try "Intelligent Categorization" to analyze file types in a folder

## AI Model

The current version uses a simple Random Forest Classifier for demonstration purposes. In a production environment, consider using more sophisticated models or integrating with cloud-based AI services for better predictions and recommendations.

## Safety and Permissions

This application performs operations that modify your system files. It's recommended to:
- Run the application with administrator privileges
- Create a system restore point before using the cleaning features
- Review the logs to understand what actions have been performed

## Contributing

Contributions to improve AI-Powered PC Cleaner 2024 are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

[MIT License](LICENSE)

## Disclaimer

This software is provided "as is", without warranty of any kind. Use at your own risk. Always ensure you have backups before performing system cleaning operations. The AI recommendations are based on a simple model and should not be considered as professional IT advice.

This updated README now reflects the AI capabilities of your enhanced PC Cleaner application. It provides users with information about the new intelligent features and sets appropriate expectations about the AI model's capabilities.