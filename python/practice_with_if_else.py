
final_score = 0
count = 0
combine_score = 0
Score_Before_Finalization = 0

def Display_Options(final_score, count, combine_score):
    print()
    
    print('Select the number 1 if you have grades to add: ')
    print('Select the number 2 if you are ready to obtain the total score of the grades: ')
    Selection = (input('Enter Selection: '))
    if Selection == '1':
        grades(final_score, count, combine_score, Score_Before_Finalization)
    elif Selection == '2':
        if count <= 1:
            print('PLEASE ENTER MORE THAN 1 GRADE')
            Display_Options(final_score, count, combine_score)
        print(str(final_score) + '%')
        print()
        print('End of application')
    else:
        print("1 or 2 was not entered")
        Display_Options(final_score, count, combine_score)

def grades(final_score, count, combine_score, Score_Before_Finalization):
    print()    
    more_grades = input('Are there grades to add?: Y/N ')
    if more_grades.upper() == 'Y':
        count += 1
        Score_Before_Finalization = float(input('Input a grade: '))
        combine_score += Score_Before_Finalization
        grades(final_score, count, combine_score, Score_Before_Finalization)
    elif more_grades.upper() == 'N':
        final_score = combine_score / count
        Display_Options(final_score, count, combine_score)
    else:
        print('Need to say y for yes or n for no')
        grades(final_score, count, combine_score, Score_Before_Finalization)

Display_Options(final_score, count, combine_score)



