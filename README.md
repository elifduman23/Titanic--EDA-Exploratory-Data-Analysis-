# 🚢 Titanic Dataset: EDA & Feature Engineering

[![TR](https://img.shields.io/badge/Lang-Türkçe-red)](#türkçe)
[![EN](https://img.shields.io/badge/Lang-English-blue)](#english)

---

## 🇹🇷 Türkçe

### Proje Özeti
Bu proje, meşhur **Titanic veri seti** üzerinde yapılan Keşifçi Veri Analizi (EDA) ve Temel Özellik Mühendisliği (Feature Engineering) pratiklerini içermektedir. Projenin ana amacı veri setindeki eksik (null) değerleri yönetmek ve temel görselleştirme tekniklerini uygulamaktır.

### Neler Yapıldı?
* **Eksik Veri Yönetimi (Imputation):** Veri setindeki eksik `age` (yaş) ve `embarked` (biniş yeri) değerleri, istatistiksel yöntemlerle (Ortalama/Mean, Medyan/Median ve Mod/Mode Imputation) dolduruldu.
* **Keşifçi Veri Analizi (EDA):** Veri seti içindeki yolcuların yaş dağılımı vb. özellikleri `Seaborn` ve `Matplotlib` kütüphaneleri kullanılarak Histogram ve Boxplot grafikleriyle incelendi.
* Çalışmalar hem Python scriptleri (`.py`) hem de Jupyter Notebook (`.ipynb`) formatlarında hazırlandı.

### Nasıl Çalıştırılır?
1. Repoyu bilgisayarınıza indirin:
   ```bash
   git clone https://github.com/elifduman23/Titanic--EDA-Exploratory-Data-Analysis-1.git
   ```
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. İster `.py` dosyalarını çalıştırın, ister `jupyter notebook` ile `.ipynb` dosyalarını açın.

---

## 🇬🇧 English

### Project Overview
This repository contains Exploratory Data Analysis (EDA) and fundamental Feature Engineering practices applied to the famous **Titanic dataset**. The primary focus of the project is handling missing (null) values and applying basic data visualization techniques.

### What Was Done?
* **Missing Value Imputation:** Handled missing data in the `age` and `embarked` columns using statistical methods, specifically Mean, Median, and Mode Imputation.
* **Exploratory Data Analysis (EDA):** Analyzed the distribution of passengers' ages and other features using Histograms and Boxplots with `Seaborn` and `Matplotlib`.
* The work is provided in both Python scripts (`.py`) and Jupyter Notebook (`.ipynb`) formats.

### How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/elifduman23/Titanic--EDA-Exploratory-Data-Analysis-1.git
   ```
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. Run the `.py` scripts via terminal or open the `.ipynb` files using `jupyter notebook`.
