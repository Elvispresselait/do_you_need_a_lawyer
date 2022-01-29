def hello_gdpr():
    x = input('''Are you a lawyer? (y/n)
    ''')
    x = x.lower()
    if x == 'y':
        return 'No you\'re not'
    else:
        return 'Call a lawyer before processing this data (+33 6 63 58 62 82❤️) ⚖️!'

if __name__=='__main__':
    print(hello_gdpr())