namespace BroFirstProgram
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double a = 5.5; 

            int b = Convert.ToInt32(a); // Should print 5, value will be truncated

            Console.WriteLine(b);
        }
    }
}
