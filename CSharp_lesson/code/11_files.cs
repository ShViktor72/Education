// Создание файла и запись текста
string path = "example.txt";
string content = "Hello, World!";

// Создание файла и запись текста
File.WriteAllText(path, content);

// Проверка существования файла
if (File.Exists(path))
	Console.WriteLine($"Файл '{path}' создан.");
else
	Console.WriteLine($"Файл '{path}' не создан.");

// Чтение из файла
if (File.Exists(path))
{
	// Чтение текста из файла
	string fileContent = File.ReadAllText(path);
	Console.WriteLine($"Содержимое файла:\n {fileContent}");
}
else
{
	Console.WriteLine($"Файл '{path}' не найден.");
}

// Дозапись в файл
string additionalContent = "\nThis is additional content.";

// Добавление текста в файл
File.AppendAllText(path, additionalContent);
// чтение из измененного файла
string fileContent2 = File.ReadAllText(path);
Console.WriteLine($"Содержимое измененного файла:\n {fileContent2}");

// Копирование файла
string sourcePath = path;
string destinationPath = "example_copy.txt";

if (File.Exists(sourcePath))
{
	// Копирование файла
	File.Copy(sourcePath, destinationPath, overwrite: true);
	Console.WriteLine($"Файл скопирован в '{destinationPath}'.");
}
else
{
	Console.WriteLine($"Файл '{sourcePath}' не найден.");
}

// Удаление файла
if (File.Exists(path))
{
	// Удаление файла
	File.Delete(path);
	Console.WriteLine($"Файл '{path}' удалён.");
}
else
{
	Console.WriteLine($"Файл '{path}' не найден.");
}

// перемещение файла
sourcePath = "example_copy.txt";
destinationPath = "moved_example.txt";

if (File.Exists(sourcePath))
{
	// Перемещение файла
	File.Move(sourcePath, destinationPath, overwrite: true);
	Console.WriteLine($"Файл перемещён в '{destinationPath}'.");
}
else
{
	Console.WriteLine($"Файл '{sourcePath}' не найден.");
}