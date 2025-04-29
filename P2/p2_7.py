import random

heightTotalCm = random.randint(1,199)
heightMeter = heightTotalCm // 100
heightCm = heightTotalCm % 100
print(f"Height { heightTotalCm }cm is ",end='')
print(f"{ heightMeter }m and {heightCm}cm")
