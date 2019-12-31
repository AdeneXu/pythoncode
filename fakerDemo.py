from faker import Faker

faker = Faker('zh_CN')
print('name:',faker.name())
print('address:',faker.address())
print('text:',faker.text())
print('Date:',faker.date(pattern="%Y-%m-%d",date_end='today'))
