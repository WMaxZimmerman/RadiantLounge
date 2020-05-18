using RadiantLounge.DAL.Repositories;

namespace RadiantLounge.ApplicationCore.Services
{
    public class ExampleService
    {
        public static string HelloWorld()
        {
            return ExampleRepository.HelloWorld();
        }
    }
}
