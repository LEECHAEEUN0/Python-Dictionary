Dic1 = {
    'name1' : '이채은',
    'age1': '19',
    'birthday1': '0207',
    'gender1' : '여자',
    'phone number1' : '010-6710-3682'
}
Dic2 = {
    'name2' : '이코코',
    'age2': '13',
    'birthday2': '1125',
    'gender2' : '남자',
    'phone number2' : '010-3710-3682'
}
Dic3 = {
    'name3' : '임창균',
    'age3': '27',
    'birthday3': '0126',
    'gender3' : '남자',
    'phone number3' : '010-1234-5678'
}

Name = [1, 2, 3]
Age = [1, 2, 3]
Birthday= [1, 2, 3]
Gender = [1, 2, 3]
Phonenumber = [1, 2, 3]

Name = [Dic1['name1'], Dic2['name2'], Dic3['name3']]
Age = [Dic1['age1'], Dic2['age2'], Dic3['age3']]
Birthday = [Dic1['birthday1'], Dic2['birthday2'], Dic3['birthday3']]
Gender = [Dic1['gender1'], Dic2['gender2'], Dic3['gender3']]
Phonenumber = [Dic1['phone number1'], Dic2['phone number2'], Dic3['phone number3']]

print("이름 리스트는 " + str(Name))
print("나이 리스트는 " + str(Age))
print("생일 리스트는 " + str(Birthday))
print("성별 리스트는 " + str(Gender))
print("전화번호 리스트는 " + str(Phonenumber))
