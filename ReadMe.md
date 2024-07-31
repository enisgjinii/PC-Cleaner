# AI-Powered PC Cleaner 2024

## Description

AI-Powered PC Cleaner 2024 is a sophisticated desktop application that merges traditional PC maintenance tools with artificial intelligence to deliver smarter, personalized computer optimization. Developed with Python and CustomTkinter, and enhanced with machine learning capabilities, this application offers an intelligent approach to system cleaning and analysis.

## Features

1. **AI-Powered Cleaning Recommendations**
   - Analyzes the current system state
   - Provides personalized cleaning suggestions

2. **Predictive System Health Analysis**
   - Calculates a system health score
   - Offers insights into potential system issues

3. **Intelligent File Categorization**
   - Automatically categorizes files by type
   - Identifies space-consuming file categories

4. **Traditional Cleaning Tools**
   - **Quick Clean**: Removes temporary files and clears the Recycle Bin
   - **Deep Clean**: Performs a Quick Clean and clears Windows Update cache and browser cache

5. **Real-Time System Information**
   - Displays CPU usage, memory utilization, and disk space usage

6. **Disk Space Analyzer**
   - Provides a visual representation of folder sizes
   - Displays a hierarchical view of file and folder structure

7. **User-Friendly Interface**
   - Modern, dark-themed UI
   - Sidebar navigation for easy access to all features
   - Real-time logging of operations

## Requirements

- Python 3.7 or higher
- Windows operating system

## Installation

1. Clone this repository or download the source code.
2. Install the required packages:
   ```sh
   pip install customtkinter pillow psutil scikit-learn joblib numpy
   ```
3. To enable Recycle Bin clearing, also install:
   ```sh
   pip install winshell
   ```

## Usage

Run the application by executing the main Python script:
```sh
python ai_pc_cleaner.py
```
Navigate through the application using the sidebar to explore the AI-powered features:
- Use **AI Recommendations** for smart cleaning suggestions.
- Check **Predict System Health** for a health score.
- Try **Intelligent Categorization** to analyze file types in a folder.

## AI Model

The current version employs a simple Random Forest Classifier for demonstration purposes. For a production environment, consider using more sophisticated models or integrating with cloud-based AI services for enhanced predictions and recommendations.

## Safety and Permissions

This application performs operations that modify your system files. It is recommended to:
- Run the application with administrator privileges.
- Create a system restore point before using the cleaning features.
- Review the logs to understand the actions performed.

## Contributing

Contributions to improve AI-Powered PC Cleaner 2024 are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This software is provided "as is", without warranty of any kind. Use at your own risk. Always ensure you have backups before performing system cleaning operations. The AI recommendations are based on a simple model and should not be considered professional IT advice.