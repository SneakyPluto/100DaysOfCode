namespace BroFirstProgram
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Convert double to int
            double a = 5.5; 
            int b = Convert.ToInt32(a); // Should print 5, value will be truncated
            Console.WriteLine(b.GetType()); // Get the type of the variable

            // Convert int to double
            int c = 123;
            double d = Convert.ToDouble(c);  // Convert int to double
            Console.WriteLine(d.GetType()); // Should print System.Double

            // Convert int to string
            int e = 321;
            String f = e.ToString(); // Convert int to string
            Console.WriteLine(f.GetType()); // Should print System.String

            // Convert string to char
            String h = "$";
            Char g = Convert.ToChar(h); // Convert string to char
            Console.WriteLine(g.GetType());

            // Convert string to boolean
            String i = "True";
            bool j = Convert.ToBoolean(i); // Convert string to boolean
            Console.WriteLine(j.GetType()); // Should print System.Boolean
        }
    }
}
