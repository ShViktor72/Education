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
                txtPrice.Text = "��������...";
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
                MessageBox.Show($"������ ����: {ex.Message}", "������", MessageBoxButtons.OK, MessageBoxIcon.Error);
                txtPrice.Text = "������ ����";
            }
            catch (JsonException ex)
            {
                MessageBox.Show($"������ JSON: {ex.Message}", "������", MessageBoxButtons.OK, MessageBoxIcon.Error);
                txtPrice.Text = "������ ������";
            }
        }


    }
    // ������ ��� �������������� JSON
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
������� ������:
return response?.Bitcoin?.Usd ?? 0m;

response?
�������� ?. � ��� null-�������� (��� ����������) �������� �������.
���� response null, �� �� ��������� ����������� � ���������� null.

response?.Bitcoin?
���� response �� null, �� ��������� ��� ������ � ��������� response.Bitcoin.
���� Bitcoin == null, �� ��������� ���� ����������� � ���������� null.
r
esponse?.Bitcoin?.Usd
���� response � Bitcoin �� null, �� ������������ �������� Usd (decimal).

?? 0m
�������� ?? � ��� �������� "���� null".
���� �� ��������� ����� ����� null, �� ������ null ������������� 0m (0 ���� decimal).
 */