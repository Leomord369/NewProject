// See https://aka.ms/new-console-template for more information

using BankProject.Enums;
using BankProject.Models;

var person1 = new Person(1, "nohannad", "gerami", DateTime.Now, "0919");

var account1 = new Account(1, person1, "123456-789", 0, AccountType.Jari);

var myCard = new Card(1, CardTypes.Primary, "1234 1234 5678 5678", DateTime.Now.AddDays(100), "1370", account1);
var wifeCard = new Card(2, CardTypes.Primary, "1234 1234 5678 5670", DateTime.Now.AddDays(50), "1371", account1);

account1.Variz(100000);
wifeCard.Bardasht(1000, "1371");
int x = 0;

