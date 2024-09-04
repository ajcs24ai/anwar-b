import matplotlib.pyplot as plt
data=pd.read_csv(r"E:\Dataset\titanic.csv")
age_survived=data[data['survived']==1]['age']
age_notsurvived=data[data['survived']==0]['age']
plt.hist(age_survived,color='g',alpha=0.9,label='survived')
plt.hist(age_notsurvived,color='k',alpha=0.5,label='notsurvived')
plt.xlabel('age')
plt.ylabel('frequency')
plt.title("age distribution of survived and not survived")
plt.legend()
plt.show()