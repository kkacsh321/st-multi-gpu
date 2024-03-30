import streamlit as st
from PIL import Image

# Streamlit UI setup
st.set_page_config(layout="wide")
st.title("LocalAI Single VS. Multiple GPU Showdown")

try:
    image = Image.open("images/robot_gpu.png")
    st.image(image, width=600, caption="AI GPU Testing")
except FileNotFoundError as e:
    st.error(f"The image file 'robot_gpu.png' was not found: {e}")
except Exception as e:
    st.error(f"Failed to load image: {e}")


# Show information about testing rig and software
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
VIDEO_URL = "https://youtu.be/Zu29LHKXEjs"
with st.container(border=True):
    st.video(VIDEO_URL)
    st.write("  * [4060TI 16GB Single vs Multiple](https://youtu.be/Zu29LHKXEjs)")
st.write("  * Robotf [Robotf](https://robotf.ai)")
