namespace BroFirstProgram
{
    internal class Program
    {
        static void Main(string[] args)
        {
            String day_of_week = "Tuesday";

            switch (day_of_week = "Tuesday") 
            {
                case "Monday":
                    console.WriteLine("Fav day of week");
                break;
                case "Tuesday":
                    console.WriteLine("Yawn");
                break;
                case "Wednesday":
                    console.WriteLine("Wednesday my due");
                break;
            }
        }
    }
}
