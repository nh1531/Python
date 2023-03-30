import matplotlib.pyplot as plt
import numpy as np

# 2x2 서브플롯 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
'''
# 2x2 서브플롯 생성
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

# 첫 번째 서브플롯
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine')

# 두 번째 서브플롯
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine')

# 세 번째 서브플롯
axs[1, 0].plot(x, y1 + y2)
axs[1, 0].set_title('Sine + Cosine')

# 네 번째 서브플롯
axs[1, 1].plot(x, y1 - y2)
axs[1, 1].set_title('Sine - Cosine')

plt.show()
'''
#2행2열로 틀을 잡고 1번째 부분에 그래프 그림
plt.subplot(2,2,1)
plt.plot(x,y1)
plt.title('Sine')

plt.subplot(1,2,2)
plt.plot(x,y1)
plt.title('Sine')

plt.subplot(4,4,9)
plt.plot(x,y1)
plt.title('Sine')



plt.show()

