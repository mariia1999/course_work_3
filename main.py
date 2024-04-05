from src.utils import get_data, filter_data, sort_operations, print_transactions

load_data = get_data()
filter_ = filter_data(load_data)
sort_ = sort_operations(filter_)
print_transactions(sort_)

