# hotel reviews analysis

If you do not have conda installed, please follow these steps to install conda https://conda.io/projects/conda/en/latest/user-guide/getting-started.html

## Step 1 - Setup python environment - open anaconda prompt

```cmd
git clone https://github.com/amishpopli/perpetua-coding-challenge.git
cd perpetua-coding-challenge
conda env create -f environment.yml
activate pyamish
ipython kernel install --user --name=pyamish
```
## Step 2 - Run flask application - open anaconda prompt

```cmd
cd <project directory>/scripts
python app.py
```

## Step 3 - View notebooks - open anaconda prompt
-EDA Hotel reviews - Has EDA on the hotel reviews and 2 actionable insights

-Data prep and modelling - Has 2 machine learning models tfidf and bow

```cmd
jupyter notebook
```
