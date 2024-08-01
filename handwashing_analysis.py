import pandas as pd
import matplotlib.pyplot as plt

# Read datasets/yearly_deaths_by_clinic.csv into yearly
yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')


# Calculate proportion of deaths per no. births
yearly['proportion_deaths'] = yearly['deaths'] / yearly['births']

# Extract Clinic 1 data into clinic_1 and Clinic 2 data into clinic_2
clinic_1 = yearly[yearly['clinic'] == 'clinic 1']
clinic_2 = yearly[yearly['clinic'] == 'clinic 2']

# Print out clinic_1
print(clinic_1)

# Plot yearly proportion of deaths at the two clinics
ax = clinic_1.plot(x='year', y='proportion_deaths', label='Clinic 1', marker='o')
clinic_2.plot(x='year', y='proportion_deaths', label='Clinic 2', marker='o', ax=ax)

# Set y-axis label
ax.set_ylabel('Proportion deaths')

# Show the plot
plt.show()

# Read datasets/monthly_deaths.csv into monthly
monthly = pd.read_csv('datasets/monthly_deaths.csv', parse_dates=['date'])

# Calculate proportion of deaths per no. births
monthly['proportion_deaths'] = monthly['deaths'] / monthly['births']

# Print out the first rows in monthly
print(monthly.head())

# Plot monthly proportion of deaths
ax = monthly.plot(x='date', y='proportion_deaths', label='Proportion Deaths', marker='o')

# Set the y-axis label
ax.set_ylabel('Proportion deaths')

# Show the plot
plt.show()

# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly[monthly['date'] < handwashing_start]
after_washing = monthly[monthly['date'] >= handwashing_start]

# Plot monthly proportion of deaths before and after handwashing
ax = before_washing.plot(x='date', y='proportion_deaths', label='Before Handwashing', marker='o')
after_washing.plot(x='date', y='proportion_deaths', label='After Handwashing', marker='o', ax=ax)

# Set y-axis label
ax.set_ylabel('Proportion deaths')

# Show the plot
plt.show()

# Difference in mean monthly proportion of deaths due to handwashing
# Select the proportion_deaths column for before and after handwashing
before_proportion = before_washing['proportion_deaths']
after_proportion = after_washing['proportion_deaths']

# Calculate the mean of each proportion
mean_before_proportion = before_proportion.mean()
mean_after_proportion = after_proportion.mean()

# Calculate the difference in mean proportions
mean_diff = mean_after_proportion - mean_before_proportion

# Print the average reduction
print(f'Average reduction in proportion of deaths due to handwashing: {mean_diff:.4f}')

# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append(boot_after.mean() - boot_before.mean())

# Calculating a 95% confidence interval from boot_mean_diff
boot_mean_diff_series = pd.Series(boot_mean_diff)
confidence_interval = boot_mean_diff_series.quantile([0.025, 0.975])
print(confidence_interval)
