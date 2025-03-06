using System.Text.Json;
using System.Text.Json.Serialization;

namespace HttpJsonBTC
{
    public partial class Form1 : Form
    {
        static HttpClient client = new HttpClient();
        static string url =
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD";
        
        public Form1()
        {
            InitializeComponent();
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            // Выполняем GET-запрос
            var response = await client.GetAsync(url);

            response.EnsureSuccessStatusCode(); // Убедимся, что запрос успешен

            // Читаем ответ как строку
            string responseBody = await response.Content.ReadAsStringAsync();

            // Десериализуем JSON-ответ в объект
            var rateData = JsonSerializer.Deserialize<CryptoCompareResponse>(responseBody);

            // Возвращаем курс биткоина
            txtPrice.Text = rateData.USD.ToString();
        }
    }
    // Класс для десериализации JSON-ответа
    public class CryptoCompareResponse
    {
        public decimal USD { get; set; }
    }
}

