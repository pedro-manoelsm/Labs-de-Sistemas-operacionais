var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Endpoint simples em C#
app.MapGet("/dados", () => new { mensagem = "Olá do .NET!", linguagem = "C#" });

// C# consumindo o serviço do Python
app.MapGet("/consumir-python", async () =>
{
    using var httpClient = new HttpClient();
    var response = await httpClient.GetFromJsonAsync<dynamic>("http://localhost:5000/dados");
    return new { resposta_do_python = response };
});

app.Run("http://localhost:5001");
