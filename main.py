import pandas_data_handler ,database_handler,lookups
from prehook import execute_prehook
import lookups 
from misc_handler import return_lookup_items_as_dict
from hook import execute_hook
from posthook import execute_posthook

df_src_list,df_src_titles=execute_prehook(sql_command_directory_path = 'SQL_COMMANDS')
execute_hook(df_src_titles,df_src_list)
execute_posthook()
