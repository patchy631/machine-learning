import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Illustrating the Central Limit Theorem")

# Add a slider for sample size
sample_size = st.slider("Sample Size", min_value=1, max_value=100, value=5)

perc_heads = st.number_input(
    label="Chance of Coins Landing on Heads", min_value=0.0, max_value=1.0, value=0.5
)

binom_dist = np.random.binomial(1, perc_heads, 1000)

list_of_means = []

for i in range(0, 1000):
    sample = np.random.choice(binom_dist, sample_size, replace=True)
    list_of_means.append(sample.mean())

# Plotting
fig, ax = plt.subplots()
sns.histplot(list_of_means, ax=ax, color="cyan", stat="density")
sns.kdeplot(list_of_means, ax=ax, color="hotpink", lw=2)
st.pyplot(fig)
