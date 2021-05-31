from titanic.views.controller import Controller
from titanic.templates.plot import Plot

if __name__ == '__main__':
    while 1:
        menu = input('0-exit\n'
                     '1-data visualization\n'
                     '2-machine learning\n'
                     '3-machine release')
        if menu =='0':
            break
        elif menu == '1':
            plot = Plot('train.csv') #?
            plot.draw_survived_dead()
            plot.draw_Pclass()
            plot.draw_sex()
            plot.draw_embarked()
        elif menu == '2':
            controller = Controller()
            controller.modeling('train.csv', 'test.csv') #?
        elif menu == '3':
            pass
        elif menu == '4':
            pass
        else:
            continue