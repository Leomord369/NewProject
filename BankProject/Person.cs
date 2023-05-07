using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankProject.Models
{
    public class Person
    {
        public Person(int id, string firstname, string lastName, DateTime birthDate, string mobile)
        {
            Id = id;
            Firstname = firstname;
            LastName = lastName;
            BirthDate = birthDate;
            Mobile = mobile;
        }

        public int Id { get; set; }
        public string Firstname { get; set; }
        public string LastName { get; set; }
        public DateTime BirthDate { get; set; }
        public string Mobile { get; set; }
    }
}
