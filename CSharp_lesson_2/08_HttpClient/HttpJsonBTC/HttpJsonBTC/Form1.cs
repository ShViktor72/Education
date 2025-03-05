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
            // ��������� GET-������
            var response = await client.GetAsync(url);

            response.EnsureSuccessStatusCode(); // ��������, ��� ������ �������

            // ������ ����� ��� ������
            string responseBody = await response.Content.ReadAsStringAsync();

            // ������������� JSON-����� � ������
            var rateData = JsonSerializer.Deserialize<CryptoCompareResponse>(responseBody);

            // ���������� ���� ��������
            txtPrice.Text = rateData.USD.ToString();
        }
    }
    // ����� ��� �������������� JSON-������
    public class CryptoCompareResponse
    {
        public decimal USD { get; set; }
    }
}

