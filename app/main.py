import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')
  country = input('Por favor ingrese el pais a graficar: ')
  data_filter = utils.filter_country(data, country)
  end_data = utils.select_columns(data_filter)
  labels, values = utils.generate_charts(end_data)
  charts.generate_bar_chart(country,labels, values)
  print(labels)
  print(values)

def run_1():
  data = read_csv.read_csv('./data.csv')
  labels, values = utils.select_columns_1(data)
  charts.generate_pie_chart(labels, values)
  
if __name__ == '__main__':
  run()
  #run_1()