# =-=-=-=- {import space} =-=-=-=-  
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import plotly.graph_objects as go

# მონაცემები
temp_off = [
    32.8, 32.4, 31.8, 32.7, 33.0, 32.7, 32.0, 32.8, 33.0, 32.7, 32.2,
    33.0, 33.1, 32.6, 32.7, 33.2, 33.0, 32.5, 31.7, 32.3, 32.4
]
temp_on = [
    20.3, 21.1, 22.5, 23.0, 24.4, 25.8, 27.0, 27.9, 28.6, 29.2, 29.8,
    30.3, 30.8, 31.1, 31.5, 31.8, 32.1, 32.4, 31.5, 31.0, 31.1, 31.5,
    32.1, 31.2, 31.1, 31.6, 32.2, 31.3, 31.2, 31.7, 32.4, 31.9, 31.2,
    32.3, 32.0, 31.8, 31.2, 31.5, 31.2
]
temp = [
    20.3, 21.1, 22.5, 23.0, 24.4, 25.8, 27.0, 27.9, 28.6, 29.2, 29.8, 30.3, 30.8,
    31.1, 31.5, 31.8, 32.1, 32.4, 32.8, 32.4, 31.8, 31.5, 31.0, 31.1, 31.5, 32.1,
    32.7, 33.0, 32.7, 32.0, 31.2, 31.1, 31.6, 32.2, 32.8, 33.0, 32.7, 32.2, 31.3,
    31.2, 31.7, 32.4, 33.0, 33.1, 32.6, 31.9, 31.2, 32.3, 32.0, 32.7, 33.2, 33.0,
    32.5, 31.8, 31.2, 31.5, 31.2, 31.7, 32.3, 32.4
]


line_off = np.arange(len(temp_off))  
line_on = np.arange(len(temp_on))   
line_all = np.arange(len(temp))    

# გრაფიკი
plt.figure(figsize=(14, 7))
plt.plot(line_off, temp_off, label="ტემპერატურა (გათიშული)", color="red", linestyle='--')
plt.plot(line_on, temp_on, label="ტემპერატურა (ჩართული)", color="green", linestyle='-')
plt.plot(line_all, temp, label="მიმდინარეობის ტემპერატურა", color="blue", linestyle='-.')

# სეთთინგი
plt.title("ტემპერატურის ცვალებადობის გრაფიკი", fontsize=16)
plt.xlabel("დრო (∆ წუთი)", fontsize=14)
plt.ylabel("ტემპერატურა (°C)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12)


# Создание интерактивного графика
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=line_off, y=temp_off,
    mode='lines+markers',
    name='Температура (выключено)',
    line=dict(color='red', dash='dash'),
    hovertemplate='Время: %{x}<br>Температура: %{y}°C'
))

fig.add_trace(go.Scatter(
    x=line_on, y=temp_on,
    mode='lines+markers',
    name='Температура (включено)',
    line=dict(color='green', dash='solid'),
    hovertemplate='Время: %{x}<br>Температура: %{y}°C'
))

fig.add_trace(go.Scatter(
    x=line_all, y=temp,
    mode='lines+markers',
    name='Общая температура',
    line=dict(color='blue', dash='dot'),
    hovertemplate='Время: %{x}<br>Температура: %{y}°C'
))

def init():
    line_off.set_data([], [])
    line_on.set_data([], [])
    line_all.set_data([], [])
    return line_off, line_on, line_all

def update(frame):
    line_off.set_data(line_off[:frame], temp_off[:frame])
    line_on.set_data(line_on[:frame], temp_on[:frame])
    line_all.set_data(line_all[:frame], temp[:frame])
    return line_off, line_on, line_all

# Анимация (по желанию)
fig.update_traces(mode="lines+markers", marker=dict(size=8))

plt.show()