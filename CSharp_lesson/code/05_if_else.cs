// Условный оператор if-else
// Проверка четности числа
int number = 7;

if (number % 2 == 0)
{
    Console.WriteLine("Число четное.");
}
else
{
    Console.WriteLine("Число нечетное.");
}

// Оценка успеваемости студента
int score = 85;

if (score >= 90)
{
    Console.WriteLine("Оценка: Отлично");
}
else if (score >= 70)
{
    Console.WriteLine("Оценка: Хорошо");
}
else if (score >= 50)
{
    Console.WriteLine("Оценка: Удовлетворительно");
}
else
{
    Console.WriteLine("Оценка: Неудовлетворительно");
}

// Вложенные условные операторы 
// Проверка температуры и состояния воды
double temperature = 85.0;

if (temperature > 0)
{
    if (temperature < 100)
    {
        Console.WriteLine("Вода в жидком состоянии.");
    }
    else
    {
        Console.WriteLine("Вода в газообразном состоянии.");
    }
}
else
{
    Console.WriteLine("Вода в твердом состоянии.");
}

// Оператор выбора switch-case
// Выбор уровня доступа
string accessLevel = "admin";

switch (accessLevel)
{
    case "admin":
        Console.WriteLine("Полный доступ.");
        break;
    case "user":
        Console.WriteLine("Ограниченный доступ.");
        break;
    case "guest":
        Console.WriteLine("Минимальный доступ.");
        break;
    default:
        Console.WriteLine("Доступ запрещен.");
        break;
}

// Определение сезона по месяцу
int month = 7;

switch (month)
{
    case 12:
    case 1:
    case 2:
        Console.WriteLine("Зима");
        break;
    case 3:
    case 4:
    case 5:
        Console.WriteLine("Весна");
        break;
    case 6:
    case 7:
    case 8:
        Console.WriteLine("Лето");
        break;
    case 9:
    case 10:
    case 11:
        Console.WriteLine("Осень");
        break;
    default:
        Console.WriteLine("Неверный номер месяца");
        break;
}

// Логические операторы
// Использование оператора И (&&)
// доступ разрешен только если возраст пользователя не меньше 18 лет И у него есть удостоверение личности
int age = 25;
bool hasID = true;

if (age >= 18 && hasID)
{
    Console.WriteLine("Доступ разрешен.");
}
else
{
    Console.WriteLine("Доступ запрещен.");
}

// Использование оператора ИЛИ (||)
// вход разрешен, если у пользователя есть билет ИЛИ приглашение.
bool hasTicket = true;
bool hasInvitation = false;

if (hasTicket || hasInvitation)
{
    Console.WriteLine("Вход разрешен.");
}
else
{
    Console.WriteLine("Вход запрещен.");
}

// Использование оператора НЕ (!)
bool isWeekend = false;

if (!isWeekend)
{
    Console.WriteLine("Сегодня рабочий день.");
}
else
{
    Console.WriteLine("Сегодня выходной.");
}

// Комбинирование логических операторов
// скидка предоставляется, если возраст меньше 25 или больше 60,
// и при этом пользователь является членом клуба или у него есть купон на скидку
int Age = 30;
bool isMember = true;
bool hasDiscountCoupon = false;

if ((Age < 25 || Age > 60) && (isMember || hasDiscountCoupon))
{
    Console.WriteLine("Вы получаете скидку.");
}
else
{
    Console.WriteLine("Скидка не предоставляется.");
}
