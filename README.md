```markdown
# Perhitungan Nilai Z dan Integral Distribusi Normal

## Deskripsi Tugas
Tugas ini bertujuan untuk menghitung nilai **z** dan integral dari distribusi normal menggunakan parameter yang telah diberikan. Semua perhitungan dinyatakan dalam format LaTeX.

---

## 1. Perhitungan Nilai Z
Rumus dasar untuk menghitung nilai **z** adalah:

```latex
z = \frac{x - \mu}{\sigma}


### Parameter yang Diketahui:
- \( x = 75.531300 \)
- \( \mu = 75.230990 \)
- \( \sigma = 4.991295 \)

### Substitusi ke dalam rumus:
```latex
z = \frac{75.531300 - 75.230990}{4.991295}


---

## 2. Integral Distribusi Normal
Rumus integral untuk distribusi normal adalah:

```latex
\int_{a}^{b} \frac{1}{\sqrt{2 \pi \sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \, dx


### Parameter yang Diketahui:
- \( \mu = 75 \)
- \( \sigma^2 = 25 \) (maka \( \sigma = 5 \))
- Batas integral: \( a = 76 \), \( b = 100 \)

### Substitusi ke dalam rumus:
```latex
\int_{76}^{100} \frac{1}{\sqrt{2 \pi \cdot 25}} \exp\left(-\frac{(x - 75)^2}{2 \cdot 25}\right) \, dx
`

---

## Catatan
- Format LaTeX disiapkan agar mudah dimasukkan ke dalam dokumen laporan atau skrip untuk visualisasi lebih lanjut.
- Tidak dilakukan perhitungan nilai numerik dalam tugas ini.
