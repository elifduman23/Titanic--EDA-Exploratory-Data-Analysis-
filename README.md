# 🚢 Titanic Dataset: EDA & Feature Engineering

[![TR](https://img.shields.io/badge/Lang-Türkçe-red)](#türkçe)
[![EN](https://img.shields.io/badge/Lang-English-blue)](#english)

---

## 🇹🇷 Türkçe

### Proje Özeti
Bu proje, meşhur **Titanic veri seti** üzerinde yapılan Keşifçi Veri Analizi (EDA) ve Temel Özellik Mühendisliği (Feature Engineering) pratiklerini içermektedir. Projenin ana amacı Pandas kullanarak veriyi tanımak, eksik (null) değerleri istatistiksel olarak yönetmek ve temel görselleştirme tekniklerini uygulamaktır.

### Neler Yapıldı?
* **Eksik Veri Yönetimi (Imputation):** Veri setindeki eksik `age` (yaş) ve `embarked` (biniş yeri) değerleri, istatistiksel yöntemlerle (Ortalama/Mean, Medyan/Median ve Mod/Mode Imputation) dolduruldu.
* **Veri Keşfi ve İşleme:** `titanicDataset.ipynb` dosyasında **Pandas** kütüphanesi kullanılarak veri filtreleme, sıralama ve gruplama (groupby) işlemleri yapıldı.
* **Veri Görselleştirme (EDA):** Veri seti içindeki yolcuların yaş dağılımı vb. özellikleri `Seaborn` ve `Matplotlib` kütüphaneleri kullanılarak Histogram ve Boxplot grafikleriyle incelendi.
* Çalışmalar Jupyter Notebook (`.ipynb`) formatında hazırlandı.

### Nasıl Çalıştırılır?
1. Repoyu bilgisayarınıza indirin:
   ```bash
   git clone https://github.com/elifduman23/Titanic--EDA-Exploratory-Data-Analysis-.git
   ```
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. Jupyter Notebook uygulamasını başlatın:
   ```bash
   jupyter notebook
   ```

---

## 🇬🇧 English

### Project Overview
This repository contains Exploratory Data Analysis (EDA) and fundamental Feature Engineering practices applied to the famous **Titanic dataset**. The primary focus of the project is to manipulate data using Pandas, handle missing (null) values statistically, and apply basic data visualization techniques.

### What Was Done?
* **Missing Value Imputation:** Handled missing data in the `age` and `embarked` columns using statistical methods, specifically Mean, Median, and Mode Imputation.
* **Data Exploration and Processing:** Data filtering, sorting, and grouping (groupby) operations were performed using the **Pandas** library in the `titanicDataset.ipynb` file.
* **Data Visualization (EDA):** Analyzed the distribution of passengers' ages and other features using Histograms and Boxplots with `Seaborn` and `Matplotlib`.
* The work is provided in Jupyter Notebook (`.ipynb`) format.

### How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/elifduman23/Titanic--EDA-Exploratory-Data-Analysis-.git
   ```
2. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. Start the Jupyter Notebook application:
   ```bash
   jupyter notebook
   ```
