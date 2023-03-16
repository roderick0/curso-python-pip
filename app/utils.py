def filter_country(data, country):
  list_filter = list(filter(lambda x: x['Country/Territory'] == country, data))
  data_filter = list_filter[0]
  return data_filter

def select_columns(data_filter):
  end_data = {}
  end_data['2022'] = int(data_filter['2022 Population'])
  end_data['2020'] = int(data_filter['2020 Population'])
  end_data['2015'] = int(data_filter['2015 Population'])
  end_data['2010'] = int(data_filter['2010 Population'])
  end_data['2000'] = int(data_filter['2000 Population'])
  end_data['1990'] = int(data_filter['1990 Population'])
  end_data['1980'] = int(data_filter['1980 Population'])
  end_data['1970'] = int(data_filter['1970 Population'])
  return end_data

def generate_charts(end_data):  
  labels = end_data.keys()
  values = end_data.values()
  return labels, values
  
def select_columns_1(data):
  
  def create_keys(item):
    key = item['Country/Territory']
    return key

  def create_values(item):
    value = item['World Population Percentage']
    return value
    
  keys = list(map(create_keys, data))
  values = list(map(create_values, data))
  return keys, values

  