# hw01
# in part 2
# first step, I declare a list to store data, and name it target_data and mean_val
# I use teacher give us command like target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# and then we will get data about about id is C0A880, C0F9A0, C0G640, C0R190, C0X260.
# second step, I declare a list about ans to store output
# third step, the mean of  the ID of the station in the lexicographical order.
# so, I use for loop to calculate the mean value of pressure. use if and else to remove the value is -99.0 or -999.0
# forth step,if ans is equal to zero, I give them name 'none'
# and print ans.

# my result is [['C0A880', 1017.7], ['C0F9A0', 967.76], ['C0G640', 1016.96], ['C0R190', 1011.22], ['C0X260', 1012.21]]

