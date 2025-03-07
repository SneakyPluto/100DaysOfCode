namespace BroFirstProgram
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Hello, what is your name? ");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, " + name + "!");

            int age = GetAgeFromUser();
            Console.WriteLine("Your name is " + name + " and your age is " + age + "!");
        }

        static int GetAgeFromUser()
        {
            while (true)
            {
                Console.Write("Hello, what is your age? ");
                string ageInput = Console.ReadLine();

                try
                {
                    return Convert.ToInt32(ageInput);
                }
                catch (FormatException)
                {
                    Console.WriteLine("Invalid age entered. Please enter a valid number.");
                }
            }
        }
    }
}
