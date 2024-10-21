string path = @"D:\projects\MyApp";

// Создание каталога
if (!Directory.Exists(path))
{
    Directory.CreateDirectory(path);
    Console.WriteLine($"Каталог '{path}' создан.");
}
else
{
    Console.WriteLine($"Каталог '{path}' уже существует.");
}

//Получение списка файлов в каталоге
if (Directory.Exists(path)) // проверка существования каталога
{
    string[] files = Directory.GetFiles(path);
    Console.WriteLine($"Файлы в каталоге '{path}':");
    foreach (string file in files)
    {
        Console.WriteLine(file);
    }
}
else
{
    Console.WriteLine($"Каталог '{path}' не найден.");
}

// Получение списка подкаталогов
if (Directory.Exists(path))
{
    string[] directories = Directory.GetDirectories(path);
    Console.WriteLine($"Подкаталоги в '{path}':");
    foreach (string dir in directories)
    {
        Console.WriteLine(dir);
    }
}
else
{
    Console.WriteLine($"Каталог '{path}' не найден.");
}

// Получение метаданных с помощью DirectoryInfo
DirectoryInfo dirInfo = new DirectoryInfo(path);

if (dirInfo.Exists)
{
    Console.WriteLine($"Каталог: {dirInfo.FullName}");
    Console.WriteLine($"Дата создания: {dirInfo.CreationTime}");
    Console.WriteLine($"Последний доступ: {dirInfo.LastAccessTime}");
    Console.WriteLine($"Последнее изменение: {dirInfo.LastWriteTime}");
    Console.WriteLine($"Атрибуты: {dirInfo.Attributes}");
}
else
{
    Console.WriteLine($"Каталог '{path}' не найден.");
}


// Удаление каталога
if (Directory.Exists(path))
{
    Directory.Delete(path, recursive: true);
    Console.WriteLine($"каталог '{path}' удалён.");
}
else
{
    Console.WriteLine($"каталог '{path}' не найден.");
}