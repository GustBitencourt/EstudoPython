## verifica se a cidade começa com a palavra santo
print('Do you come from a holy city?')
city = input('Enter the city where you were born! ').strip()

print('Você nasceu em um lugar SANTO? ', city[:5].upper() == 'SANTO')