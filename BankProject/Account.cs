using BankProject.Enums;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankProject.Models
{
    public class Account
    {
        public Account(int id, Person owner, string number, int credit, AccountType accountType)
        {
            Id = id;
            Owner = owner;
            Number = number;
            Credit = credit;
            AccountType = accountType;

            Cards = new List<Card>();
        }

        public int Id { get; set; }
        public Person Owner { get; set; }
        public AccountType AccountType { get; set; }
        public string Number { get; set; }
        public int Credit { get; set; }

        public List<Card> Cards { get; set; }

        public void Variz(int amount)
        {
            Credit += amount;
        }

        public void Bardasht(int amount)
        {
            if (amount <= Credit)
                Credit -= amount;
        }
    }
}
