import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

if platform.system() == "Windows":# Window
    plt.rc("font", family= "Malgun Gothic")
elif platform.system() == 'Darwin': # Mac
    plt.rc("font", family= "Malgun Gothic")
else: #linux
    plt.rc("font", family= "NanumGothic")

# 그래프에 마이너스 표시가 되도록 변경
plt.rcParams['axes.unicode_minus'] = False
