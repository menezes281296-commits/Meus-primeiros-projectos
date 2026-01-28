#1 O CASDASTRO
print('Welcome to HostStreaming')
user=input('Create your user').strip().lower()
password=input('Create your password')
balance=float(input('Deposit you initial balance: $'))
age=2026-int(input('Enter your year of birth:'))
# --- 2. LOGIN (WHILE/TRUE) ---
while True:
    login_user=input('Enter your user').strip().lower()
    login_password=input('Enter your password')
    if login_user==user and login_password==password:
        print('Login completed')
        break 
    else:
        print('Try again')
# --- 3. Função Filmes ---
def get_movie(choice):
    movies= {
        'the smurfs': {
            'price': 10.0,
            'rating': 0,
        }, 'deadpool': {
            'price': 25.0,
            'rating': 18,
        }, 'joker': {
            'price': 28.0,
            'rating': 14,
        }, 'spider-man': {
            'price': 20.0,
            'rating': 10,
        }
    }
    return movies.get(choice.lower())
# --- 4. Compra Final ---
movie_client=input('chose wich movie you want (the smurfs/deadpool/joker/spider-man)').strip().lower()
details=get_movie(movie_client)
if details != None:
    preco_item=details['price']
    rating_item=details['rating']
    if age<details['rating']:
        print('To new')
    else:
        print('Age approved!Checking balance!')
        if balance>=details['price']:
            print('Approved purchase')
            new_balance=balance-details['price']
            print('Congratulation on your purchase')
            print(f'New balance: {new_balance}')
            print(f'Movie {movie_client.capitalize()}')
            print(f'Price R$:{details['price']}')
            print(f'Rating: {details['rating']}')
        else:
            print('insufficient balance')
else:
    print('non-existent movie')