"""
Workout_ToolKit

This class will be used as a collection of methods used
for interpeting multiple Workout objects and giving back
data, trends, etc about them
"""
import pandas as pd
import pyprind

class Workout_ToolKit:

    @staticmethod
    def read_in_weight_training_data(spread_sheet_name):
        # TODO: Need to test the method
        # TODO: Make method more more versatile
        print('Reading DS18 Data Sheet')
        df = pd.read_excel(spread_sheet_name)
        ds18_products= []

        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            ds18_product = None
            if df['MSRP'][i] != 0:
                ds18_product = Set(str(df['Model'][i]),
                                      str(df['Brand'][i]),
                                      str(df['Name'][i]),
                                      str(df['M/C'][i]),
                                      str(df['MSRP'][i]),
                                      str(df['Dealer'][i]))
            if ds18_product is not None:
                ds18_products.append(ds18_product)
            total += 1
            all_total += 1
            bar.update()
        return ds18_products

    @staticmethod
    def get_workouts(begin_date, end_date):
        """
        Method used to get all of the workouts between
        one date and another in chronical order
        :param: begin_date - beginning date
        :param: end_date - ending date
        :return: array of Workout objects
        """
        pass

    @staticmethod
    def total_weight_lifted_in():
        """
        Method used to return a dictionary of the
        total weight lifted for a particular exercise
        :param: exercise_name - name of the exercise
        :return dictionary, exercise_name:weight_lifted
        """
        pass

    @staticmethod
    def progress_in_exercises():
        """
        Method used to show how the weights lifted have
        changed over all time
        """
        pass
