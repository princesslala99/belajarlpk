import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.title("This is a title")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
