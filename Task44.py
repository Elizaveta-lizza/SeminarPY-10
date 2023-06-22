# В ячейке ниже представлен код генерирующий DataFrame, которая состоит 
# всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это 
# сделать без get_dummies?

import pandas as pd
import random

def my_dummies(some_df, column_name, search_val):
    human = list()
    robot = list()
    for val in some_df[column_name]:
        if val == search_val:
            human.append('true')
            robot.append('false')
        else:
            human.append('false')
            robot.append('true')
    return pd.DataFrame({'human':human, 'robot':robot})

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head(20))
# print(pd.get_dummies(data['whoAmI']))
print()
print(my_dummies(data, 'whoAmI', 'human'))