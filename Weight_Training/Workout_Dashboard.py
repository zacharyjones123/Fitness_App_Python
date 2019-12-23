from Weight_Training.Exercise import Exercise
from Weight_Training.Set import Set
from Weight_Training.Workout import Workout



sets = [Set(1, 45, 15, 1, 1),
        Set(2, 65, 12, 1, 1),
        Set(3, 95, 10, 1, 3),
        Set(4, 115, 8, 1, 4),
        Set(5, 145, 5, 1, 6),
        Set(6, 145, 5, 1, 6),
        Set(7, 145, 5, 1, 6),
        Set(8, 145, 5, 1, 6),
        Set(9, 145, 5, 1, 6)]

shoulder_press = Exercise("Shoulder Press", sets)

exercises = [shoulder_press]

workout = Workout("12-23-19", exercises)

print(workout)