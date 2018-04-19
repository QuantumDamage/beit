## Środowisko wirtualne

```bash
conda create -y -n beit
conda activate beit
```

## Instalacja TPOT i Jupyter Notebook

```bash
conda install -y numpy scipy scikit-learn pandas
pip install deap update_checker tqdm stopit
pip install tpot
conda install -y notebook
```

## Zbiór danych - pobrać do katalogu beit/input

Opis zbioru danych: [Wine Quality Data Set](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)

* czerwone wino - [https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
* białe wino - [https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv)
* opis - [https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names)

