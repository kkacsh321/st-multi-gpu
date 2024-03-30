<!-- markdownlint-disable-file MD013-->
# Multi GPU LLM Testing - Streamlit Excel Data Visualization App

![ai-gpu-test](images/robot_gpu.png)

Interact with this app live at <https://gputests.robotf.ai/>

Description
This Streamlit app provides an interactive way to visualize data from testing Multiple GPU's using LocalAI [localai](https://github.com/mudler/LocalAI).

Single 4060TI 16GB GPU vs Multiple 4060TI's, Along with testing visually in this video [youtube](https://youtu.be/Zu29LHKXEjs)

In general users can select different metrics to compare across various configurations detailed in the Excel sheets. The app allows for the display of sheet names, a preview of the first few rows of data, dynamic generation of plots based on selected metrics, and an option to view raw data tables for detailed analysis.

Features
Load and preview Excel sheet names and their first few rows.
Select and visualize specific metrics from the Excel file.
Interactive sidebar for metric selection.
Option to display raw data tables for in-depth analysis.
Installation
Before you can run the app, you need to have Python installed on your system. This app is built with Python 3.8 or later in mind. You can download Python from python.org.

Once Python is installed, follow these steps to set up the app:

Clone this repository to your local machine.

Run the setup script (if on mac with brew already installed):

```sh
./scripts/setup.sh
```

Otherwise install the required Python packages:

```sh
pip install -r requirements.txt
```

This command installs all the necessary packages, including Streamlit, pandas, matplotlib, and python-dotenv.

Create a .env file in the root directory of the app and add any environment variables required by the app. Use the `.env_example` and copy it to .env. This is only needed if running the tests against an LLM.

Running the App
To run the app, navigate to the app's directory in your terminal and execute the following command:

with task:

```sh
task run
```

with docker:

```sh
task docker-load && task docker-run
```

with just plain streamlit

```sh
streamlit run Multi-GPU.py
```

Usage
After launching the app, follow these steps for usage:

View Sheet Names and Preview Data: Upon loading, the app will display the names of the sheets found in the Excel file and a preview of the first few rows from the first sheet.
Select Metric: Use the sidebar to select the metric you wish to visualize. The app supports metrics like 'Prompt Eval Time', 'Eval Time', 'Total Time', 'Prompt Token Per Second', 'Eval Token Per Second'.
View Visualization: The main area will display a plot based on the selected metric, comparing different configurations detailed in the Excel file.
Show Raw Data: If detailed analysis is required, check the 'Show Raw Data' checkbox and select a configuration to view its raw data table.
Contributing
Contributions to the app are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.

License
Distributed under the MIT License. See LICENSE for more information.

Contact
<keith@robotf.ai>

Project Link: <https://github.com/kkacsh321/st-multi-gpu>

YouTube Video: <https://youtu.be/Zu29LHKXEjs>
