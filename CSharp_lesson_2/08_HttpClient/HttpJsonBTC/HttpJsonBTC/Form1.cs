using System.Text.Json;
using System.Text.Json.Serialization;

namespace HttpJsonBTC
{
    public partial class Form1 : Form
    {
        readonly HttpClient client = new HttpClient();
        readonly string url = 
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd";
        public Form1()
        {
            InitializeComponent();
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            try
            {
                txtPrice.Text = "Загрузка...";
                string json = await client.GetStringAsync(url);

                var options = new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true,
                    DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull
                };

                var response = JsonSerializer.Deserialize<CryptoResponse>(json, options);
                txtPrice.Text = $"{response?.Bitcoin?.Usd ?? 0m} USD";
            }
            catch (HttpRequestException ex)
            {
                MessageBox.Show($"Ошибка сети: {ex.Message}", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                txtPrice.Text = "Ошибка сети";
            }
            catch (JsonException ex)
            {
                MessageBox.Show($"Ошибка JSON: {ex.Message}", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                txtPrice.Text = "Ошибка данных";
            }
        }


    }
    // Классы для десериализации JSON
    public class CryptoPrice
    {
        public decimal Usd { get; set; }
    }

    public class CryptoResponse
    {
        public CryptoPrice Bitcoin { get; set; }
    }
}

/*
Разберём строку:
return response?.Bitcoin?.Usd ?? 0m;

response?
Оператор ?. — это null-условный (или безопасный) оператор доступа.
Если response null, то всё выражение завершается и возвращает null.

response?.Bitcoin?
Если response не null, то программа идёт дальше и проверяет response.Bitcoin.
Если Bitcoin == null, то выражение тоже завершается и возвращает null.
r
esponse?.Bitcoin?.Usd
Если response и Bitcoin не null, то возвращается значение Usd (decimal).

?? 0m
Оператор ?? — это оператор "если null".
Если всё выражение слева равно null, то вместо null подставляется 0m (0 типа decimal).
 */