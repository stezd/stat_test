import random
import statistics
import matplotlib.pyplot as plt
import csv
import seaborn as sns
from scipy.stats import norm

filename = "datatugas.csv"

fields = []
rows = []
kolom_nilai = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
        kolom_nilai.append(row[1].replace(',', '.'))

    print("Total Baris (Termasuk Header Kolom): %d" %csvreader.line_num)

#deklarasi mean, variance, stdev dari populasi
kolom_nilai = [float(value) for value in kolom_nilai]
mean_populasi = statistics.mean(kolom_nilai)
variance_populasi = statistics.pvariance(kolom_nilai, mean_populasi)
stdev_populasi = statistics.pstdev(kolom_nilai, mean_populasi)

#histogram dari populasi
sns.histplot(kolom_nilai, kde=True ,bins=30, color='Blue', edgecolor='black')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Histogram dari datatugas.csv')
plt.show()

print("mean_populasi = {:.6f}".format(mean_populasi))
print("variance_populasi = {:.6f}".format(variance_populasi))
print("stdev_populasi = {:.6f}".format(stdev_populasi))
print("\n")

#select 100 random sample
random.seed(4206969)  # seed agar dapat direproduksi
sample_100 = random.sample(kolom_nilai, 100)
print("Random sample of 100 values: ", sample_100)
mean_sample100 = statistics.mean(sample_100)
variance_sample100 = statistics.variance(sample_100, mean_sample100)
stdev_sample100 = statistics.stdev(sample_100, mean_sample100)

print("mean_sample100 = {:.6f}".format(mean_sample100))
print("variance_sample100 = {:.6f}".format(variance_sample100))
print("stdev_sample100 = {:.6f}".format(stdev_sample100))
print("\n")

# Hitung P(X_population >= x_sample)
p_value = 1 - norm.cdf(mean_sample100, loc=mean_populasi, scale=stdev_populasi)
print("P(X_population >= x_sample) = {:.6f}".format(p_value))



