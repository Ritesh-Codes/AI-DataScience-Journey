import numpy as np

# Step 1: Generate random temperature data for 7 days
temperatures_celsius = np.random.randint(20, 41, size=7)
print("🌡️ Weekly Temperatures (°C):", temperatures_celsius)

# Step 2: Basic statistics
print("📊 Average Temperature:", np.mean(temperatures_celsius))
print("🔥 Maximum Temperature:", np.max(temperatures_celsius))
print("❄️ Minimum Temperature:", np.min(temperatures_celsius))
print("📉 Standard Deviation:", np.std(temperatures_celsius))

# Step 3: Days with temperature > 35°C
hot_days = np.sum(temperatures_celsius > 35)
print("☀️ Days above 35°C:", hot_days)

# Step 4 (Bonus): Convert temperatures to Fahrenheit
temperatures_fahrenheit = (temperatures_celsius * 9/5) + 32
print("🌡️ Weekly Temperatures (°F):", temperatures_fahrenheit)