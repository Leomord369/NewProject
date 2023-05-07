using BankProject.Enums;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankProject.Models
{
    public class Card
    {
        public Card(int id, CardTypes cardType, string number, DateTime expireDate, string password, Account account)
        {
            Id = id;
            CardType = cardType;
            Number = number;
            ExpireDate = expireDate;
            Password = password;
            Account = account;
            Account.Cards.Add(this);
        }

        public int Id { get; set; }
        public CardTypes CardType { get; set; }
        public string Number { get; set; }
        public DateTime ExpireDate { get; set; }
        public string Password { get; set; }

        public Account Account { get; set; }

        public void Bardasht(int amount, string password)
        {
            if (password == Password)
            {
                Account.Bardasht(amount);
            }
        }
    }
}
