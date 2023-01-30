import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('data/iris.csv')

iris_setosa = df[df['class'] == 'Iris-setosa']['petal_length']
iris_versicolor = df[df['class']=='Iris-versicolor']['petal_length']
iris_virginica = df[df['class']== 'Iris-virginica']['petal_length']

hist_data=[iris_setosa, iris_versicolor, iris_virginica]
group_labels = ['Petal Legth Iris Setosa','Petal Legth Iris Versicolor',
                'Petal Legth Iris Virginica']

fig = ff.create_distplot(hist_data, group_labels)

pyo.plot(fig,filename='HTML/Displot_Exercise.HTML')