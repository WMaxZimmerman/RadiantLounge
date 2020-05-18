using NTrospection.CLI.Core;

namespace RadiantLounge.Console
{
   class Program
   {
       static void Main(string[] args)
       {
           new Processor().ProcessArguments(args);
       }
   }
}
