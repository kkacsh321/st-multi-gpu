import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

def load_excel_data(file_path):
    """
    Loads an Excel file and returns a Pandas ExcelFile object along with its sheet names.
    
    Parameters:
        file_path (str): The path to the Excel file.
        
    Returns:
        xl (pd.ExcelFile): The ExcelFile object.
        sheet_names (list): A list of sheet names in the Excel file.
    """
    try:
        xl = pd.ExcelFile(file_path)
        sheet_names = xl.sheet_names
        return xl, sheet_names
    except Exception as err:
        st.error(f"Failed to load Excel file: {err}")
        return None, []

def main():
    load_dotenv('.env')

    excel_file_path = './gpu_test_data/LLM_Multi_4060_Comparison.xlsx'
    xl, sheet_names = load_excel_data(excel_file_path)

    try:
        image = Image.open("images/4060.png")
        st.image(image, width=600, caption="4060TI Pile")
    except FileNotFoundError as err:
        st.error(f"The image file '4060.png' was not found: {err}")
    except Exception as err:
        st.error(f"Failed to load image: {err}")

    if xl is not None:
        st.write("GPU Tests Found:", sheet_names)
        st.write("## Results (Use select metric menu from side to see more options)")
        try:
            data = {config: xl.parse(config) for config in sheet_names}
            st.write(data[sheet_names[0]].head())
        except Exception as e:
            st.error(f"Failed to parse sheet: {e}")

        st.sidebar.header('4060TI 16GB Metrics')
        metric = st.sidebar.selectbox('Select Metric', ['Prompt Eval Time (MS)', 'Eval Time (MS)', 'Total Time (MS)', 'Prompt Token Per Second', 'Eval Token Per Second'])

        fig, ax = plt.subplots()
        for config, df in data.items():
            ax.plot(df[metric], label=config)
        ax.set_ylabel(metric)
        ax.set_title(f'{metric} Comparison')
        ax.legend()
        st.pyplot(fig)

        if st.checkbox('Show Raw Data'):
            config_to_show = st.selectbox('Select Configuration', list(data.keys()))
            st.write(data[config_to_show])

    st.write("### What are the goals?")
    st.write("To plot the data of single vs multiple GPUs in different configurations using LocalAI to \
    host a Large Language Model (LLM), a fixed 100 token prompt (including system prompt) to gather \
    valuation times, and token per second counts in order to compare the results.")
    st.write("### Software used:")
    st.write("* Kubernetes (1.25.13)")
    st.write("* LocalAI (2.9.0) - Deployed by Helm [Github](https://github.com/mudler/LocalAI)")
    st.write("* Streamlit (1.32.2) - [Github](https://github.com/streamlit)")
    st.write("* Langchain (0.1.2) - [Github](https://github.com/langchain-ai)")
    st.write("* Excel (Who cares?)")

    st.write("### GPU Node Specs:")
    st.write("* Asus WS X299 SAGE/10G Workstation Motherboard")
    st.write("* Intel Core i9-7960X X-Series Processor 16 Cores up to 4.2 GHz")
    st.write("* 256GB DDR4 3200 RAM")
    st.write("* 2TB NVMe Drives for Docker/Model storage")

    st.write("### GPUs for Todays Test:")
    st.write("* 6x PNY 4060Ti 16GB VRAM *Fairly Cheap GPUs")
    st.write("* These will cards all run in PCIE 8x")

    st.write("### LLM For Today's Use:")
    st.write("* Llama2-13b (because this will max a single 16GB VRAM GPU)")

    st.write("### How are we going to run these tests?")
    st.write("* Use a static 100 Token based prompt")
    st.write("* Run the tests 10x in each single, dual, triple, quad, and six GPUs")
    st.write("* Record the Prompt Eval Time, Eval Time, Total Time, Prompt TPS,\
    Eval TPS (Token Per Second)")
    st.write("* Compare our end results")

    st.write("## Links")
    st.write("* This Github Repo [Github](https://github.com/kkacsh321/st-multi-gpu)")
    st.write("* Youtube Videos for this discussion:")
    st.write("  * [4060TI 16GB Single vs Multiple](https://youtu.be/Zu29LHKXEjs)")
    st.write("  * Robotf [Robotf](https://robotf.ai)")

if __name__ == "__main__":
    main()