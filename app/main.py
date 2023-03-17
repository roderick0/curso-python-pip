import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  country = input('Por favor ingrese el pais a graficar: ')
  data = read_csv.read_csv('./data.csv')
  data_filter = utils.filter_country(data, country)
  end_data = utils.select_columns(data_filter)
  labels, values = utils.generate_charts(end_data)
  charts.generate_bar_chart(country,labels, values)
  print(labels)
  print(values)'''
  #############Pandas################
  df = pd.read_csv('./data.csv')  
  #print(type(df))
  Continent = input('Por favor ingrese el continente a graficar: ')
  df = df[df['Continent'] == Continent]
  print(df)
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(Continent,countries, percentages)

def run_1():
  data = read_csv.read_csv('./data.csv')
  labels, values = utils.select_columns_1(data)
  charts.generate_pie_chart(labels, values)
  
if __name__ == '__main__':
  run()
  #run_1()