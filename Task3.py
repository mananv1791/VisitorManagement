def add_contact(contacts,pk):
    add_decide='Y'
    name=input('Enter Contact Name: ').lower()
    number=[]
    while add_decide!='N':
        number.append(input('Enter Number: '))
        add_decide=input('Add another number, enter "Y", to quit, enter "N": ').upper()
    contacts[pk]={'name':name,'numbers':tuple(number)}
    return 0

def access_contact(kw,contacts):
    listp=[]
    for contacts_pk,pk_val in contacts.items():
        if kw not in contacts[contacts_pk]['name']:
            pass
        else:
            listp.append([contacts_pk,contacts[contacts_pk]['name']])
            for i in range(len(listp)):
                print(f'Name:{listp[i][1]} ,Associated Index: {listp[i][0]}')
            index=int(input("Enter Associated Index of your chosen name: "))
            txt='contact retrived:\n Name:{name}\nNumbers:{number} '.format(name=contacts[index]['name'],number=contacts[index]['numbers'])
            print(txt)
    return 0

def print_contacts(contacts):
    sted = sorted(contacts.items(),key=lambda x:x[1]['name'])
    print(sted)
    return 0


contacts={0:{'name':'krr','numbers':(202020,)},1:{'name':'koorr','numbers':(202020,3030,)}}
pk=2
do_other='Y'
while do_other!='N':
    choice=input('"Add" to add contacts \n"Access" to access contacts\n"Print" to print database in sorted order \n Enter Here: ').lower()
    
    if choice=='add':
        keep_adding = 'Y'
        while keep_adding!='N':
            add_contact(contacts,pk)
            print('Contact is Saved',contacts[pk])
    
            pk=pk+1
            keep_adding=input('Add another contact? "Y" for Yes,"N" for No : ').upper()
    
        do_other=input("Do another operation? 'Y' for Yes and 'N' for No: ").upper()
    elif choice=='access':
    
        kw=input('\nEnter Your Keyword: ').lower()
        access_contact(kw,contacts)
    
        do_other=input("Do another operation? 'Y' for Yes and 'N' for No: ").upper()
    elif choice=="print":
        
        print_contacts(contacts)
        print("===Databases are sorted by names irrespective to Primary Key.====")
        do_other=input("Do another operation? 'Y' for Yes and 'N' for No: ").upper()
    else:
        print('Invalid Input')
    