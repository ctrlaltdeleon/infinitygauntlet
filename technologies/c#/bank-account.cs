using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnitTest
{
    public class BankAccount
    {

        string _customerName;
        double _balance;

        public BankAccount(string customerName, double balance)
        {
            _customerName = customerName;
            _balance = balance;
        }

        public double Balance { get { return _balance; } }

        public void Debit(double amount)
        {
            if (_balance == 0)
                throw new Exception("balance = 0");
            if (amount <= 0 || amount > _balance)
                throw new ArgumentOutOfRangeException("amount <= 0 or amount > balance");
            _balance -= amount;
        }

        public void Credit(double amount)
        {
            if (amount <= 0)
                throw new ArgumentOutOfRangeException("amount <= 0");
            _balance += amount;
        }
    }
}
