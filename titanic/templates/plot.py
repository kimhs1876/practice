from titanic.models.dataset import Dataset
from titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Plot(object):

    dataset : object = Dataset()
    service : object = Service()

    def __init__(self, fname): #??
        self.entity = self.service.new_model(fname)

    def draw_survived_dead(self):
        this = self.entity # 원본 데이터는 건들지 않고 카피데이터를 사용하겠다는 의미
        f, ax = plt.subplots(1, 2, figsize = (18, 8)) # 1행 2열 그래프 플레인 생성
        this['Survived'].value_count().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0],shadow=True) #?
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('') #?
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1]) #?
        plt.show()

    def draw_Pclass(self):
        this = self.entity #?
        f, ax = plt.subplots(1, 2, figsize =(18, 8))
        this['Pclass'].value_count().plot.pie(explode=[0,0,0.1], autopct='%1.1f%%', ax=ax[0],shadow=True)

        ax[0].set_title('1.일등석 vs 2.이등석 vs 3.삼등석')
        ax[0].set_ylabel('')
        ax[1].set_title('1.일등석 vs 2.이등석 vs 3.삼등석')
        sns.countplot('Pclass', data=this, ax=ax[1]) #?
        plt.show()

    def draw_sex(self):
        this = self.entity #?
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)

        ax[0].set_title('남성의 생존비율 [1.사망자 vs 2.생존자]')
        ax[1].set_title('여성의 생존비율 [1.사망자 vs 2.생존자]')
        plt.show()

    def draw_embarked(self): #??
        this = self.entity
        this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['승선항구'] = this['Embarked'].replace("C", '쉘버그').replace("S", '사우스햄톤').replace("Q", '퀸즈타운')
        sns.countplot(data=this, x='승선항구', hue='생존결과') #this는 데이터프레임
        plt.show()






