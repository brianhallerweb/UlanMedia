from functions.data_acquisition_functions.create_c_widgets_for_one_p_widget_dataset import create_c_widgets_for_one_p_widget_dataset
import sys

p_widget_id = sys.argv[1]
date_range = sys.argv[2]
# p_widget_id = "5681145"
# date_range = "ninety"


print(create_c_widgets_for_one_p_widget_dataset(p_widget_id, date_range))

